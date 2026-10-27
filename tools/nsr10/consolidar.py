"""Consolida en el Markdown de la NSR-10 las modificaciones de los decretos posteriores.

Uso:
    python tools/nsr10/consolidar.py normativa/nsr10 [carpeta_fuentes_pdf]

Lee tools/nsr10/modificaciones/*.md (en orden de nombre, es decir, cronológico). Cada archivo:

    # Decreto 092 de 2011
    fuente: FORK-DOC-036.pdf (descripción)

    ## <objetivo> | p<página> [| <modo>[: <argumento>]]
    <texto Markdown>

Objetivo: un artículo (A.1.3.9), una tabla («Tabla A.3-1»), una figura («Figura B.6.4-1») o «A-4».
Modos:
    nota (por omisión)    recuadro con el texto del decreto, al final del artículo.
    reemplaza             sustituye el contenido del artículo por el texto dado.
    fila-despues: <ancla> inserta la fila Markdown dada después de la fila que empieza por <ancla>.
    municipios            corrige o agrega filas del Apéndice A-4: «código Nombre | Aa | Av | zona | Ae | Ad».
Dentro del texto, ![](p14:0.20-0.55) se sustituye por un recorte de esa franja de la página del decreto.

Si se pasa la carpeta de fuentes, también regenera panel/src/nsr10/municipios.js a partir de A-4.md.
El proceso es idempotente: cada modificación aplicada deja una marca <!-- mod:ID -->.
"""
import glob
import json
import os
import re
import sys
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
RE_ENTRADA = re.compile(r"^## (.+?)\s*$", re.M)
RE_RECORTE = re.compile(r"!\[\]\(p(\d+):([\d.]+)-([\d.]+)\)")


def leer_modificaciones():
    decretos = []
    for ruta in sorted(glob.glob(os.path.join(AQUI, "modificaciones", "*.md"))):
        texto = open(ruta, encoding="utf-8").read()
        nombre = re.search(r"^# (.+)$", texto, re.M).group(1).strip()
        fuente = re.search(r"^fuente:\s*(\S+)", texto, re.M).group(1)
        clave = os.path.splitext(os.path.basename(ruta))[0]
        partes = RE_ENTRADA.split(texto)
        entradas = []
        for k in range(1, len(partes), 2):
            campos = [c.strip() for c in partes[k].split("|")]
            modo, arg = "nota", ""
            if len(campos) > 2:
                modo, _, arg = campos[2].partition(":")
                modo, arg = modo.strip(), arg.strip()
            entradas.append({
                "id": f"{clave}-{len(entradas) + 1}",
                "objetivo": campos[0],
                "pagina": int(campos[1].lstrip("p")) if len(campos) > 1 else None,
                "modo": modo,
                "arg": arg,
                "texto": partes[k + 1].strip(),
            })
        decretos.append({"nombre": nombre, "fuente": fuente, "clave": clave, "entradas": entradas})
    return decretos


def archivos_md(raiz):
    return sorted(glob.glob(os.path.join(raiz, "titulo-*", "*.md")))


def titulo_de(objetivo):
    if re.fullmatch(r"[A-K]", objetivo):
        return objetivo.lower()
    m = re.search(r"([A-K])[.-]", objetivo)
    return m.group(1).lower() if m else None


def nivel(linea):
    m = re.match(r"^(#+)\s", linea)
    return len(m.group(1)) if m else None


def numero_articulo(linea):
    m = re.match(r"^#+\s+([A-K](?:-[A-Z0-9]+|\.\d+)(?:\.\d+)*)\s", linea) or re.match(r"^\*\*([A-K](?:-[A-Z0-9]+|\.\d+)(?:\.\d+)*)\*\*", linea)         or re.match(r"^([A-K]-[A-Z0-9]+(?:\.\d+)+) — ", linea)
    return m.group(1) if m else None


def buscar_articulo(lineas, art):
    """Devuelve (inicio, fin) del bloque del artículo, o None."""
    for i, l in enumerate(lineas):
        if numero_articulo(l) == art:
            n = nivel(l)
            for j in range(i + 1, len(lineas)):
                lj = lineas[j]
                if n is not None:
                    if nivel(lj) is not None and nivel(lj) <= n:
                        return i, j
                else:
                    otro = numero_articulo(lj)
                    if nivel(lj) is not None or (otro and not otro.startswith(art + ".")):
                        return i, j
            return i, len(lineas)
    return None


def buscar_tabla(lineas, objetivo):
    tipo, numero = objetivo.split(" ", 1)
    patron = re.compile(r"^\*\*" + tipo + r"\s+" + re.escape(numero) + r"\*\*|^!\[.*" + tipo + r"\s+" + re.escape(numero) + r"\b", re.I)
    for i, l in enumerate(lineas):
        if patron.search(l) or (tipo == "Figura" and re.search(r"\b" + re.escape(numero) + r"\b", l) and l.startswith("![")):
            j, visto = i + 1, False
            continua = re.compile(r"^\*\*" + tipo + r"\s+" + re.escape(numero) + r"\*\*.*continuaci", re.I)
            tras_continuacion = False
            while j < len(lineas):
                if lineas[j].startswith(("|", "![")) or (visto and continua.match(lineas[j])):
                    tras_continuacion = bool(continua.match(lineas[j]))
                    visto = True
                elif visto and tras_continuacion and lineas[j].strip():
                    tras_continuacion = False  # subtítulo repetido de la tabla continuada
                elif visto and lineas[j].strip() and not lineas[j].startswith(("|", "![", "Nota", "*Nota")):
                    break
                elif not visto and (nivel(lineas[j]) or lineas[j].startswith("**Tabla")):
                    break
                j += 1
            return i, j
    return None


def suprimir(lineas, i, j, arg):
    """Borra, dentro de lineas[i:j], las líneas que empiezan por cada patrón (o lo contienen si
    el patrón empieza por ~). Devuelve el nuevo final del bloque, o None si algún patrón no aparece."""
    patrones = [p.strip() for p in arg.split(";;") if p.strip()]
    borrar = set()
    for p in patrones:
        hallado = [k for k in range(i, j) if (p[1:] in lineas[k] if p.startswith("~") else lineas[k].startswith(p))]
        if not hallado:
            return None
        borrar.update(hallado)
        # En las listas de nomenclatura cada definición va seguida de una línea en blanco.
        borrar.update(k + 1 for k in hallado if k + 1 < j and not lineas[k + 1].strip() and not lineas[k].startswith("|"))
    for k in sorted(borrar, reverse=True):
        del lineas[k]
    j -= len(borrar)
    while j > i + 1 and not lineas[j - 1].strip():
        j -= 1
    return j


def tras_recuadros(lineas, j):
    """Avanza j sobre los recuadros de modificaciones ya insertados, para conservar el orden cronológico."""
    k = j
    while k < len(lineas) and (not lineas[k].strip() or lineas[k].startswith(("<!-- mod:", ">"))):
        k += 1
        if lineas[k - 1].startswith(">"):
            j = k
    return j


def recuadro(decreto, e, cuerpo):
    encabezado = f"> **Modificación — {decreto['nombre']}** · anexo, p. {e['pagina']}"
    lineas = [f"<!-- mod:{e['id']} -->", encabezado, ">"]
    lineas += [("> " + l) if l.strip() else ">" for l in cuerpo.split("\n")]
    return lineas + [""]


def recortes(decreto, e, cuerpo, carpeta_img, fuentes):
    def sustituir(m):
        pag, y0, y1 = int(m.group(1)), float(m.group(2)), float(m.group(3))
        nombre = f"mod-{decreto['clave'].split('-', 1)[1]}-p{pag}-{int(y0 * 100)}.png"
        if fuentes:
            import pymupdf
            doc = pymupdf.open(os.path.join(fuentes, decreto["fuente"]))
            p = doc[pag - 1]
            r = pymupdf.Rect(36, y0 * p.rect.height, p.rect.width - 36, y1 * p.rect.height)
            p.get_pixmap(clip=r, dpi=160).save(os.path.join(carpeta_img, nombre))
        return f"![{decreto['nombre']}, anexo, p. {pag}](img/{nombre})"
    return RE_RECORTE.sub(sustituir, cuerpo)


def aplicar_municipios(lineas, decreto, e):
    hechos = []
    for fila in e["texto"].split("\n"):
        m = re.match(r"^(\d{5})\s+(.+?)\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*\|\s*(\w+)\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*$", fila.strip())
        if not m:
            continue
        cod, nombre, aa, av, zona, ae, ad = m.groups()
        nueva = f"| {nombre} | {cod} | {aa} | {av} | {zona} | {ae} | {ad} |"
        pos = next((i for i, l in enumerate(lineas) if re.match(r"^\|[^|]+\|\s*" + cod + r"\s*\|", l)), None)
        if pos is not None:
            lineas[pos] = nueva
        else:
            # Municipio nuevo: al final de la tabla de su departamento (códigos con el mismo prefijo).
            dep = [i for i, l in enumerate(lineas) if re.match(r"^\|[^|]+\|\s*" + cod[:2] + r"\d{3}\s*\|", l)]
            lineas.insert(dep[-1] + 1, nueva)
        hechos.append(f"{nombre} ({cod})")
    return hechos


def consolidar(raiz, fuentes=None):
    md = {ruta: open(ruta, encoding="utf-8").read().split("\n") for ruta in archivos_md(raiz)}
    pendientes, aplicadas = [], 0
    notas_a4 = []
    for decreto in leer_modificaciones():
        for e in decreto["entradas"]:
            letra = titulo_de(e["objetivo"])
            candidatos = [r for r in md if os.path.basename(os.path.dirname(r)) == f"titulo-{letra}"]
            if not candidatos:
                pendientes.append((e["id"], e["objetivo"], "título no incluido"))
                continue
            if any(f"<!-- mod:{e['id']} -->" in "\n".join(md[r]) for r in candidatos):
                continue
            carpeta_img = os.path.join(raiz, f"titulo-{letra}", "img")
            cuerpo = recortes(decreto, e, e["texto"], carpeta_img, fuentes)
            if e["modo"] == "sustituye":
                viejo, nuevo = [x.strip() for x in e["arg"].split("=>")]
                total = 0
                for ruta in candidatos:
                    lineas = md[ruta]
                    k = next((i for i, l in enumerate(lineas) if viejo in l), None)
                    if k is None:
                        continue
                    total += sum(l.count(viejo) for l in lineas)
                    md[ruta] = lineas = [l.replace(viejo, nuevo) for l in lineas]
                    lineas[k + 1:k + 1] = [""] + recuadro(decreto, e, cuerpo)[:-1]
                if total:
                    aplicadas += 1
                else:
                    pendientes.append((e["id"], e["objetivo"], f"no aparece «{viejo}»"))
                continue
            if e["modo"] == "apendice":
                ruta = os.path.join(raiz, f"titulo-{letra}", e["arg"])
                # Un archivo de capítulo (I.05.md, Capítulo I.5 del Decreto 945) no es un apéndice.
                clase = "Capítulo" if re.match(r"^[A-K]\.\d+\.md$", e["arg"]) else "Apéndice"
                md[ruta] = [f"<!-- mod:{e['id']} -->", f"> *{clase} incorporado por el {decreto['nombre']} (anexo, p. {e['pagina']}).*", ""] + cuerpo.split("\n") + [""]
                # Apéndice nuevo: se enlaza en el índice del título, tras su capítulo (F.4-A tras F.4) o al final.
                indice = md.get(os.path.join(raiz, f"titulo-{letra}", "README.md"))
                titulo = re.match(r"# (.+)", cuerpo)
                if indice is not None and titulo and not any(f"]({e['arg']})" in l for l in indice):
                    enlaces = [k for k, l in enumerate(indice) if l.startswith("- [")]
                    padre = e["objetivo"].split("-")[0]
                    hijos = [k for k in enlaces if re.match(r"- \[" + re.escape(padre) + r"[ -]", indice[k])]
                    k = (hijos or enlaces)[-1] + 1
                    indice.insert(k, f"- [{titulo.group(1)}]({e['arg']})")
                aplicadas += 1
                continue
            if e["modo"] == "municipios":
                ruta = next(r for r in candidatos if os.path.basename(r) == "A-4.md")
                hechos = aplicar_municipios(md[ruta], decreto, e)
                notas_a4.append((ruta, decreto, e, hechos))
                aplicadas += 1
                continue
            hecho = False
            es_tabla = e["objetivo"].startswith(("Tabla ", "Figura "))
            # Primera pasada: la tabla o figura; segunda: el artículo (o el que contiene la tabla).
            pasadas = [(r, True) for r in candidatos] + [(r, False) for r in candidatos] if es_tabla else [(r, False) for r in candidatos]
            for ruta, como_tabla in pasadas:
                lineas = md[ruta]
                if como_tabla:
                    pos = buscar_tabla(lineas, e["objetivo"])
                    if not pos:
                        continue
                    if e["modo"] == "suprime":
                        fin = suprimir(lineas, pos[0], pos[1], e["arg"])
                        if fin is None:
                            continue
                        fin = tras_recuadros(lineas, fin)
                        lineas[fin:fin] = [""] + recuadro(decreto, e, cuerpo)
                    elif e["modo"] in ("fila-despues", "fila-reemplaza"):
                        k = next((i for i in range(*pos) if lineas[i].startswith("| " + e["arg"])), None)
                        if k is None:
                            continue
                        filas_nuevas = [f for f in cuerpo.strip().split("\n") if f.startswith("|")]
                        if e["modo"] == "fila-despues":
                            lineas[k + 1:k + 1] = filas_nuevas
                            verbo = "agregada"
                        else:
                            lineas[k:k + 1] = filas_nuevas
                            verbo = "modificada"
                        fin = pos[1] + len(filas_nuevas) - (e["modo"] == "fila-reemplaza")
                        nombres = ", ".join("«" + f.split("|")[1].strip() + "»" for f in filas_nuevas)
                        lineas[fin:fin] = ["", f"<!-- mod:{e['id']} -->",
                                           f"> Fila {nombres} {verbo} por el {decreto['nombre']} (anexo, p. {e['pagina']}).", ""]
                    else:
                        fin = tras_recuadros(lineas, pos[1])
                        lineas[fin:fin] = [""] + recuadro(decreto, e, cuerpo)
                    hecho = True
                    break
                if es_tabla and e["modo"] != "nota":
                    continue
                art = re.sub(r"-.*$", "", e["objetivo"].split(" ", 1)[1]) if es_tabla else e["objetivo"]
                while art:
                    pos = buscar_articulo(lineas, art)
                    if pos:
                        break
                    art = art.rsplit(".", 1)[0] if art.count(".") > 1 else None
                if not pos:
                    continue
                i, j = pos
                if e["modo"] == "suprime":
                    j = suprimir(lineas, i, j, e["arg"])
                    if j is None:
                        continue
                    lineas[j:j] = [""] + recuadro(decreto, e, cuerpo)[:-1]
                elif e["modo"] in ("reemplaza", "reemplaza-todo") and art == e["objetivo"]:
                    if e["modo"] == "reemplaza":
                        # Solo el texto propio del artículo: hasta su primer hijo numerado.
                        j = next((k for k in range(i + 1, j) if numero_articulo(lineas[k])), j)
                    marca = [f"<!-- mod:{e['id']} -->",
                             f"> *Texto vigente según el {decreto['nombre']} (anexo, p. {e['pagina']}).*", ""]
                    cab = re.match(r"^\*\*" + re.escape(art) + r"\*\* — (.+?) — (.*)$", cuerpo, re.S)
                    if nivel(lineas[i]) and cab and cab.group(1).isupper():
                        nuevo = [f"{'#' * nivel(lineas[i])} {art} — {cab.group(1)}", ""] + marca + [cab.group(2), ""]
                    elif nivel(lineas[i]):
                        nuevo = [lineas[i], ""] + marca + [re.sub(r"^\*\*" + re.escape(art) + r"\*\* — ", "", cuerpo), ""]
                    else:
                        nuevo = marca + [cuerpo, ""]
                    lineas[i:j] = nuevo
                else:
                    while j > i + 1 and not lineas[j - 1].strip():
                        j -= 1
                    lineas[j:j] = [""] + recuadro(decreto, e, cuerpo)[:-1]
                hecho = True
                break
            if hecho:
                aplicadas += 1
            else:
                pendientes.append((e["id"], e["objetivo"], "no se encontró el destino"))
    for ruta, decreto, e, hechos in notas_a4:
        lineas = md[ruta]
        lineas[2:2] = [f"<!-- mod:{e['id']} -->",
                       f"> **{decreto['nombre']}** (anexo, p. {e['pagina']}): valores corregidos o municipios agregados: {', '.join(hechos)}.", ""]
    for ruta, lineas in md.items():
        open(ruta, "w", encoding="utf-8", newline="\n").write("\n".join(lineas))
    print(f"modificaciones aplicadas: {aplicadas}")
    for p in pendientes:
        print("  pendiente:", *p)
    return pendientes


def exportar_municipios(raiz, destino):
    """Actualiza municipios.js con los valores del Apéndice A-4 consolidado.

    Los valores salen de A-4.md (por código DANE). El departamento se conserva del archivo actual,
    porque en el PDF algunas tablas continúan de una página a otra sin encabezado de departamento;
    para municipios nuevos se toma del prefijo DANE de dos dígitos.
    """
    actuales = {}
    for l in open(destino, encoding="utf-8"):
        l = l.strip().rstrip(",")
        if l.startswith('["'):
            f = json.loads(l)
            actuales[f[2].zfill(5)] = f
    dep_por_prefijo = {cod[:2]: f[1] for cod, f in actuales.items()}
    filas, vistos = [], set()
    for l in open(os.path.join(raiz, "titulo-a", "A-4.md"), encoding="utf-8"):
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c) == 7 and re.fullmatch(r"\d{5}", c[1]) and c[1] not in vistos:
            vistos.add(c[1])
            previo = actuales.get(c[1])
            dep = previo[1] if previo else dep_por_prefijo[c[1][:2]]
            nombre = c[0]
            filas.append([nombre, dep, previo[2] if previo else c[1], float(c[2]), float(c[3]), c[4], float(c[5]), float(c[6])])
    filas.sort(key=lambda f: (unicodedata.normalize("NFD", f[1]), unicodedata.normalize("NFD", f[0])))
    cuerpo = ",\n".join("  " + json.dumps(f, ensure_ascii=False) for f in filas)
    open(destino, "w", encoding="utf-8", newline="\n").write(
        "// NSR-10 Apendice A-4 consolidado con sus modificaciones (Decretos 092/2011, 945/2017, 1711/2021).\n"
        "// Generado por tools/nsr10/consolidar.py desde normativa/nsr10/titulo-a/A-4.md. Campos:\n"
        "// [municipio, departamento, codigo DANE, Aa, Av, zona de amenaza, Ae, Ad]\n"
        f"export const MUNICIPIOS_NSR10 = [\n{cuerpo},\n];\n")
    print(f"municipios exportados: {len(filas)}")


if __name__ == "__main__":
    raiz = sys.argv[1]
    fuentes = sys.argv[2] if len(sys.argv) > 2 else None
    consolidar(raiz, fuentes)
    exportar_municipios(raiz, os.path.join(AQUI, "..", "..", "panel", "src", "nsr10", "municipios.js"))
