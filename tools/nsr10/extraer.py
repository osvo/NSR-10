"""Extrae un Titulo de la NSR-10 (PDF del reglamento, una columna) a Markdown por capitulo.

Uso:
    uv run --with pymupdf python tools/nsr10/extraer.py <pdf> <letra> <carpeta_salida>

- Quita encabezados, numeros de pagina e indice: el texto queda continuo, sin paginas.
- Un archivo por capitulo (CAPITULO A.2 -> A.02.md) y por apendice (APENDICE A-4 -> A-4.md).
- Encabezados Markdown por articulo (solo los numeros en negrita del reglamento).
- Ecuaciones numeradas: recorte en img/ y, si existe, su LaTeX de ecuaciones/<letra>.json.
- Simbolos dentro del texto (fuentes Times/Symbol) pasan a $...$ con subindices.
- Tablas con cuadricula: tabla Markdown.
"""
import json
import os
import re
import sys

import pymupdf

FUENTES_MATE = ("Times", "Symbol", "MTExtra", "Euclid", "CambriaMath")
RE_TAG = re.compile(r"^\(([A-K](?:-[A-Z])?\.\d+(?:\.\d+)*-\d+[a-z]?|[A-K]-\d+(?:\.\d+)*-\d+[a-z]?)\)$")
RE_ART = re.compile(r"^([A-K](?:-[A-Z]|\.[A-Z](?=\.))?\.\d+(?:\.\d+)*|[A-K]-\d+(?:\.\d+)+)\s*[—–-]\s*(.*)$")
LLAVES = set("⎛⎜⎝⎞⎟⎠⎡⎢⎣⎤⎥⎦⎧⎨⎩⎫⎬⎭")
RE_ENCAB = re.compile(r"^(NSR-10\s*[—–-]|REGLAMENTO\s*$|COMENTARIO|[A-K]-\d+\s*$)")
TITULOS_CONOCIDOS = {"C.17": "Elementos compuestos de concreto sometidos a flexión"}
# Los apéndices del Título F llevan capítulo y letra («F.5-A», «F.5.E»): sin la letra se pisaban unos a otros.
RE_CAP = re.compile(r"^(CAP[ÍI]TULO|AP[ÉE]NDICE)\s+([A-K][.-](?:\d+|[A-Z])(?:[.-][A-Z](?![A-Za-z]))?)\b", re.I)


# Las fuentes SymbolMT y MTExtra vienen como subconjuntos sin ToUnicode: cada subconjunto asigna
# códigos propios (el mismo «\x7f» es «=» en una página y «′» en otra). Los nombres de glifo «gN»
# son el índice del glifo en la fuente original de Windows, de donde se recupera el código Symbol.
SYMBOL = dict(zip(range(0x20, 0x7F), " !∀#∃%&∋()∗+,−./0123456789:;<=>?≅ΑΒΧΔΕΦΓΗΙϑΚΛΜΝΟΠΘΡΣΤΥςΩΞΨΖ[∴]⊥_‾αβχδεφγηιϕκλμνοπθρστυϖωξψζ{|}∼"))
SYMBOL.update(zip(range(0xA1, 0xFF), "ϒ′≤⁄∞ƒ♣♦♥♠↔←↑→↓°±″≥×∝∂•÷≠≡≈…⏐⎯↵ℵℑℜ℘⊗⊕∅∩∪⊃⊇⊄⊂⊆∈∉∠∇®©™∏√⋅¬∧∨⇔⇐⇑⇒⇓◊〈®©™∑⎛⎜⎝⎡⎢⎣⎧⎨⎩⎪ 〉∫⌠⎮⌡⎞⎟⎠⎤⎥⎦⎫⎬⎭"))
MTEXTRA = {65: "ℓ"}
# MTExtra como fuente Type0 (Identity-H, sin subconjunto que decodificar): el texto llega con los
# códigos de la fuente. «A» es ℓ (Tablas H.4 y G.6), «D» el grado (θ ≤ 45°) y 0x04 la tilde de k̃.
MTEXTRA_TYPE0 = {"A": "ℓ", "D": "°", "\x04": "˜"}
FAMILIAS_CODIFICADAS = ("SymbolMT", "MTExtra")
_FUENTES = {}


def glifo_a_unicode(familia, nombre):
    m = re.fullmatch(r"g(\d+)", nombre or "")
    if m:
        gid = int(m.group(1))
        if familia == "SymbolMT":
            return SYMBOL.get(gid + 29 if gid <= 97 else gid + 63)
        return MTEXTRA.get(gid)
    from fontTools.agl import toUnicode
    return toUnicode(nombre) or None


def decodificar_fuente(doc, xref, familia):
    """Código del subconjunto -> (unicode, gid en el subconjunto)."""
    import io
    from fontTools.cffLib import CFFFontSet
    nombres = {}
    enc = doc.xref_get_key(xref, "Encoding")
    if enc[0] == "xref":
        dif = doc.xref_get_key(int(enc[1].split()[0]), "Differences")
        if dif[0] == "array":
            codigo = 0
            for tok in re.findall(r"/[^\s/\]]+|\d+", dif[1]):
                if tok.startswith("/"):
                    nombres[codigo] = tok[1:]
                    codigo += 1
                else:
                    codigo = int(tok)
    _, ext, _, buf = doc.extract_font(xref)
    charset = []
    if ext == "cff" and buf:
        cff = CFFFontSet()
        cff.decompile(io.BytesIO(buf), None)
        top = cff[cff.fontNames[0]]
        charset = list(top.charset)
        if not nombres and not isinstance(top.Encoding, str):
            nombres = {i: g for i, g in enumerate(top.Encoding) if g != ".notdef"}
    return {chr(c): (glifo_a_unicode(familia, n), charset.index(n) if n in charset else None)
            for c, n in nombres.items()}


def normalizar_glifos(pagina, pagina_dict):
    doc = pagina.parent
    subconj = {}
    for f in pagina.get_fonts(full=True):
        familia = f[3].split("+")[-1]
        if familia in FAMILIAS_CODIFICADAS:
            clave = (doc.name, f[0])  # el xref solo es único dentro de un mismo PDF
            if clave not in _FUENTES:
                _FUENTES[clave] = decodificar_fuente(doc, f[0], familia)
            subconj.setdefault(familia, []).append(_FUENTES[clave])
    tipo0 = any(f[2] == "Type0" and f[3].split("+")[-1] == "MTExtra" for f in pagina.get_fonts())
    for b in pagina_dict["blocks"]:
        for l in b.get("lines", []):
            for s in l["spans"]:
                if tipo0 and s["font"] == "MTExtra":
                    s["text"] = "".join(MTEXTRA_TYPE0.get(c, c) for c in s["text"])
                if s["font"].startswith("ArialUnicodeMS"):
                    s["text"] = s["text"].replace("\x0e", "†")  # daga de nota al pie (Tabla C.4.4.1)
    if not subconj:
        return pagina_dict
    traza = None
    for b in pagina_dict["blocks"]:
        for l in b.get("lines", []):
            for s in l["spans"]:
                opciones = subconj.get(s["font"])
                if not opciones:
                    continue
                salida = []
                espacios_reales = None
                for k, ch in enumerate(s["text"]):
                    if ch == " " and s["text"].strip():
                        # PyMuPDF inserta espacios sintéticos entre glifos separados; un espacio es glifo
                        # real (p. ej. «=» codificado como 0x20) solo si aparece en la traza de glifos.
                        if espacios_reales is None:
                            if traza is None:
                                traza = [t for t in pagina.get_texttrace() if t["font"] == s["font"]]
                            x0, y0, x1, y1 = s["bbox"]
                            dibujados = sum(len(t["chars"]) for t in traza
                                            if t["bbox"][0] >= x0 - 0.5 and t["bbox"][2] <= x1 + 0.5
                                            and abs(t["bbox"][1] - y0) < 2)
                            espacios_reales = dibujados >= len(s["text"])
                        if not espacios_reales:
                            salida.append(ch)
                            continue
                    candidatos = {o[ch][0] for o in opciones if ch in o and o[ch][0]}
                    if len(candidatos) > 1:
                        # Varios subconjuntos en la página: se decide por el glifo realmente dibujado.
                        if traza is None:
                            traza = [t for t in pagina.get_texttrace() if t["font"] == s["font"]]
                        gid = next((t["chars"][k][1] for t in traza if len(t["chars"]) > k
                                    and abs(t["bbox"][0] - s["bbox"][0]) < 0.5 and abs(t["bbox"][1] - s["bbox"][1]) < 0.5), None)
                        candidatos = {o[ch][0] for o in opciones if ch in o and o[ch][1] == gid} or candidatos
                    salida.append(min(candidatos) if candidatos else ch)
                s["text"] = "".join(salida)
    return pagina_dict


def es_mate(span):
    return any(f in span["font"].replace(" ", "") for f in FUENTES_MATE)


def es_negrita(span):
    return "Bold" in span["font"]


def texto(spans):
    """Texto de la línea para DETECTAR estructura (ecuaciones, títulos): sin los spans sintéticos."""
    return "".join(s["text"] for s in spans if s["font"] != "MTExtra-trazo")


def solo_mate(linea):
    duros = [s for s in linea["spans"] if s["text"].strip()]
    unidades = {"(m)", "(s)", "(g)", "(m/s)", "(%)", "(kN)", "(MPa)"}
    return bool(duros) and all(es_mate(s) or s["text"].strip() in unidades for s in duros)


TRAZOS = {"radicales": 0, "barras": 0, "cortes": 0, "descartados": 0}
# Bandas de ecuación recortadas: (página, bbox, archivo). transcribir.py las convierte a LaTeX.
REGISTRO_BANDAS = []
# Fracciones en línea reconstruidas (página, caja, LaTeX), para cotejarlas contra el PDF.
REGISTRO_FRACCIONES = []
# Títulos cuyas ecuaciones salen de transcribir.py: el texto de la fila del número va con la ecuación.
TITULOS_FILA_DEL_NUMERO = {"F"}
FILA_DEL_NUMERO = False
# Títulos sin correcciones manuales de fracciones en línea: se reconstruyen desde la barra dibujada.
TITULOS_FRACCIONES_EN_LINEA = set("DEFGHIJK")
FRACCIONES_EN_LINEA = False


def trazos_mate(pagina, alto_max=40):
    """Radicales y barras de fracción dibujados como trazos vectoriales (sin glifo en el texto).

    Radical: polilínea con un trazo largo ascendente y una barra horizontal arriba; devuelve
    (x0, y0, x_fin_barra, y1). Barra «/»: un solo segmento inclinado hacia la derecha.
    """
    radicales, barras = [], []
    for g in pagina.get_drawings():
        r = g["rect"]
        segs = [(it[1], it[2]) for it in g["items"] if it[0] == "l"]
        if not segs or len(segs) != len(g["items"]):
            continue
        if 6 <= r.height <= alto_max and r.width >= 4 and len(segs) >= 3:
            horiz = [s for s in segs if abs(s[0].y - s[1].y) < 0.6 and abs(s[0].x - s[1].x) > 2
                     and min(s[0].y, s[1].y) < r.y0 + 1.0]
            subida = [s for s in segs if abs(s[0].y - s[1].y) > 0.6 * r.height
                      and abs(s[0].x - s[1].x) < 0.5 * abs(s[0].y - s[1].y)]
            if horiz and subida:
                rad = (r.x0, r.y0, max(p.x for s in horiz for p in s), r.y1)
                # El mismo radical suele venir dos veces (trazo y relleno).
                if not any(abs(rad[0] - o[0]) < 1.5 and abs(rad[1] - o[1]) < 1.5 for o in radicales):
                    radicales.append(rad)
                continue
        # Barra «/» de un segmento; en D a K un mismo trazo puede traer varias (h/t_w sobre L_b/b_f).
        if g.get("type") == "s" and (len(segs) == 1 or FRACCIONES_EN_LINEA):
            candidatas = []
            for a, b in segs:
                dx, dy = abs(a.x - b.x), abs(a.y - b.y)
                bajo, alto = (a, b) if a.y > b.y else (b, a)
                if 5 <= dy <= 18 and 0.12 * dy <= dx <= 0.6 * dy and alto.x > bajo.x:
                    candidatas.append((min(a.x, b.x), min(a.y, b.y), max(a.x, b.x), max(a.y, b.y)))
            if len(candidatas) == len(segs):
                barras.extend(candidatas)
    return radicales, barras


def _span_sintetico(texto_, x, y0, y1, tam):
    return {"text": texto_, "bbox": (x, y0, x + 0.01, y1), "font": "MTExtra-trazo", "size": tam,
            "flags": 0, "color": 0, "origin": (x, y1)}


def _centro(s):
    return (s["bbox"][0] + s["bbox"][2]) / 2


def inyectar_trazos(pagina, pagina_dict):
    """Pone «\\sqrt{…}» y «/» en el texto que cubre cada trazo vectorial.

    Una fórmula en línea suele venir partida en varias «líneas» del diccionario (una por span); el
    radical se asigna a la línea cuyo contenido cubre y los spans que cruzan su borde se parten con
    las posiciones de cada carácter (rawdict tiene la misma estructura que dict).
    """
    radicales, barras = trazos_mate(pagina)
    if not radicales and not barras and not FRACCIONES_EN_LINEA:
        return pagina_dict
    ubic = {}
    for bi, b in enumerate(pagina_dict["blocks"]):
        for li, l in enumerate(b.get("lines", [])):
            for si, s in enumerate(l["spans"]):
                ubic[id(s)] = (bi, li, si)
    lineas = [l for b in pagina_dict["blocks"] for l in b.get("lines", [])]
    crudo = []

    def en_banda(y0, y1):
        cy = (y0 + y1) / 2
        return [l for l in lineas if l["bbox"][1] - 2 <= cy <= l["bbox"][3] + 2]

    def partir(banda, x):
        """Parte los spans de la banda que cruzan la abscisa x."""
        for l in banda:
            for k, s in enumerate(l["spans"]):
                if not (s["bbox"][0] + 0.3 < x < s["bbox"][2] - 0.3) or len(s["text"]) < 2 or id(s) not in ubic:
                    continue
                if not crudo:
                    crudo.append(pagina.get_text("rawdict"))
                bi, li, si = ubic[id(s)]
                chars = crudo[0]["blocks"][bi]["lines"][li]["spans"][si]["chars"]
                if len(chars) != len(s["text"]):
                    continue
                corte = next((i for i, c in enumerate(chars) if (c["bbox"][0] + c["bbox"][2]) / 2 > x), None)
                if not corte:
                    continue
                a, b = dict(s), dict(s)
                a["text"], b["text"] = s["text"][:corte], s["text"][corte:]
                if s.get("_x0") and len(s["_x0"]) == len(s["text"]):
                    a["_x0"], b["_x0"] = s["_x0"][:corte], s["_x0"][corte:]
                a["bbox"] = (s["bbox"][0], s["bbox"][1], chars[corte - 1]["bbox"][2], s["bbox"][3])
                b["bbox"] = (chars[corte]["bbox"][0], s["bbox"][1], s["bbox"][2], s["bbox"][3])
                l["spans"][k:k + 1] = [a, b]
                TRAZOS["cortes"] += 1
                break

    for x0, y0, xf, y1 in radicales:
        banda = en_banda(y0, y1)
        partir(banda, x0)
        partir(banda, xf)
        dentro = lambda s: s["text"].strip() and x0 < _centro(s) < xf   # noqa: E731
        cubiertos = [s for l in banda for s in l["spans"] if dentro(s)]
        # Solo es radical si cubre texto matemático (los marcos de algunas tablas tienen la misma forma).
        if not cubiertos or not all(es_mate(s) for s in cubiertos):
            TRAZOS["descartados"] += 1
            continue
        # La línea del glifo base (el mayor cubierto): las líneas diminutas se pegan luego como subíndices.
        destino = max(banda, key=lambda l: max((s["size"] for s in l["spans"] if dentro(s)), default=0))
        tam = max(s["size"] for s in cubiertos)
        # «\sqrt{» antes del primer glifo cubierto y «}» antes del primer glifo que queda fuera.
        x_ab = min(min(s["bbox"][0] for s in cubiertos), x0) - 0.01
        fuera = [s["bbox"][0] for l in banda for s in l["spans"] if s["text"].strip() and _centro(s) >= xf]
        x_ci = min([xf] + fuera) - 0.01
        x_ci = max(x_ci, max(s["bbox"][0] for s in cubiertos) + 0.005)
        destino["spans"] += [_span_sintetico("\\sqrt{", x_ab, y0, y1, tam), _span_sintetico("}", x_ci, y0, y1, tam)]
        TRAZOS["radicales"] += 1
    for x0, y0, x1, y1 in barras:
        banda = [l for l in en_banda(y0, y1) if l["bbox"][0] - 40 <= x1 and x0 <= l["bbox"][2] + 40]
        if not banda:
            continue
        xm = (x0 + x1) / 2
        partir(banda, xm)
        # Va con los glifos de tamaño normal (no en una línea de subíndices, que luego se absorbe),
        # en la línea cuyo glifo queda más cerca de la barra.
        tam_max = max((s["size"] for l in banda for s in l["spans"] if s["text"].strip()), default=0)
        normales = [l for l in banda if any(s["text"].strip() and s["size"] >= 0.95 * tam_max for s in l["spans"])]
        destino = min(normales or banda, key=lambda l: min((abs(_centro(s) - xm) for s in l["spans"] if s["text"].strip()),
                                                         default=1e9))
        tam = max((s["size"] for s in destino["spans"] if s["text"].strip()), default=10)
        destino["spans"].append(_span_sintetico("/", xm, y0, y1, tam))
        TRAZOS["barras"] += 1
    if FRACCIONES_EN_LINEA:
        fracciones_en_linea(pagina, lineas, radicales)
    return pagina_dict


def _pieza(spans):
    """Texto de un numerador o denominador: los glifos menores que la base van como subíndices
    o superíndices, según queden por debajo o por encima de su centro."""
    spans = sorted(spans, key=lambda s: s["bbox"][0])
    # Negrita simulada: el mismo glifo dibujado dos veces casi en el mismo lugar («11/xx»).
    unicos = []
    for s in spans:
        if unicos and s["text"] == unicos[-1]["text"] and abs(s["bbox"][0] - unicos[-1]["bbox"][0]) < 1.5:
            continue
        unicos.append(s)
    spans = unicos
    # Tamaño de referencia: el mayor glifo alfanumérico (los paréntesis grandes no cuentan).
    alfa = [s for s in spans if re.search(r"\w", s["text"])] or spans
    ref = max(alfa, key=lambda s: s["size"])
    cref = (ref["bbox"][1] + ref["bbox"][3]) / 2
    out = []
    for s in spans:
        t = s["text"].strip()
        if s["size"] < 0.85 * ref["size"] and out and s["font"] != "MTExtra-trazo":
            arriba = (s["bbox"][1] + s["bbox"][3]) / 2 < cref - 1
            out.append(("^{" if arriba else "_{") + t + "}")
        else:
            out.append(t)
    return re.sub(r"\s+", " ", "".join(out)).replace("′", "'")


def fracciones_en_linea(pagina, lineas, radicales):
    """Fracciones apiladas dentro del texto corrido (Título F: «L/r_x ≤ 80» escrito con barra
    horizontal). Sin esto, numerador y denominador salían en orden de x («r_{x}L ≤80»).

    Solo actúa si en la altura de la barra hay texto que no es matemático (prosa): las ecuaciones de
    presentación se recortan aparte y no se tocan.
    """
    barras = []
    for g in pagina.get_drawings():
        for it in g["items"]:
            if it[0] == "re" and it[1].height < 1.6 and 3 < it[1].width < 70:
                barras.append((it[1].x0, (it[1].y0 + it[1].y1) / 2, it[1].x1))
            elif it[0] == "l" and abs(it[1].y - it[2].y) < 0.5 and 3 < abs(it[2].x - it[1].x) < 70:
                barras.append((min(it[1].x, it[2].x), it[1].y, max(it[1].x, it[2].x)))
    verticales = []
    for g in pagina.get_drawings():
        for it in g["items"]:
            if it[0] == "re" and it[1].width < 2.5 and it[1].height > 4:
                verticales.append(it[1])
            elif it[0] == "l" and abs(it[1].x - it[2].x) < 0.5 and abs(it[1].y - it[2].y) > 4:
                verticales.append(pymupdf.Rect(it[1].x, min(it[1].y, it[2].y), it[1].x, max(it[1].y, it[2].y)))
    for x0, yb, x1 in barras:
        def es_prosa(s):
            return (re.search(r"[A-Za-zÁÉÍÓÚáéíóúñ]{2}", s["text"]) and not RE_TAG.match(s["text"].strip())
                    and not es_mate(s) and s["font"] not in ("MTExtra-trazo", "MTExtra-frac"))
        fila = [s for l in lineas if l["bbox"][1] - 3 <= yb <= l["bbox"][3] + 3 for s in l["spans"] if es_prosa(s)]
        # Prosa antes de la barra («Cuando L/r_x ≤ 80») o una frase de texto en la fila; una palabra suelta
        # después («… para h′/t ≤ 30») es una ecuación de presentación partida y se deja a las bandas.
        if not (any(s["bbox"][2] <= x0 + 1 for s in fila) or len("".join(s["text"] for s in fila).strip()) >= 25):
            continue
        prosa = [l for l in lineas if l["bbox"][1] - 3 <= yb <= l["bbox"][3] + 3
                 and any(es_prosa(s) for s in l["spans"]) and l["bbox"][0] - 120 <= x0 and x1 <= l["bbox"][2] + 120]
        # Un pie de figura o de tabla no recibe etiquetas del dibujo de encima («d/n» de la Figura G.3.4-3).
        if any(re.match(r"^(Figura|Tabla|TABLA)\s", texto(l["spans"]).strip()) for l in prosa):
            continue
        if not prosa:
            continue
        # Una fila con número de ecuación es una ecuación de presentación («R_e = 1 − […]² para
        # h′/t ≤ 30  (D-1.5-5)»): se recorta como banda y no se toca aquí.
        if any(RE_TAG.match(s["text"].strip()) for l in lineas for s in l["spans"]
               if abs((l["bbox"][1] + l["bbox"][3]) / 2 - yb) < 14):
            continue
        # La raya superior de un radical (√f′m) no es barra de fracción.
        if any(abs(yb - ry0) < 2 and rx0 - 2 <= x0 and x1 <= rxf + 2 for rx0, ry0, rxf, _ in radicales):
            continue
        if any(s["text"].strip().endswith("√") and 0 <= x0 - s["bbox"][2] < 6 and abs(s["bbox"][1] - yb) < 6
               for l in lineas for s in l["spans"]):
            continue
        num, den = [], []
        for l in lineas:
            for s in l["spans"]:
                if not s["text"].strip() or not es_mate(s):
                    continue
                if s["font"] == "MTExtra-trazo" and s["text"] not in ("\\sqrt{", "}", "/"):
                    continue
                cx, cy = _centro(s), (s["bbox"][1] + s["bbox"][3]) / 2
                if not (x0 - 1.5 <= cx <= x1 + 1.5) or s["bbox"][0] < x0 - 4 or s["bbox"][2] > x1 + 4:
                    continue
                if yb - 13 <= cy < yb - 0.5:
                    num.append((l, s))
                elif yb + 0.5 < cy <= yb + 13:
                    den.append((l, s))
        if not [1 for _, s in num if s["font"] != "MTExtra-trazo"] or not [1 for _, s in den if s["font"] != "MTExtra-trazo"]:
            continue
        # Numerales romanos apilados en celdas (Tablas J.3): son dos valores, no una fracción.
        if all(re.fullmatch(r"[IVX]+", s["text"].strip()) for _, s in num + den if s["font"] != "MTExtra-trazo"):
            continue
        # Numerador y denominador pegados a la barra; si no, es una barra superior (x̄) o la raya de un
        # radical sobre la fila siguiente.
        glifos_n = [s for _, s in num if s["font"] != "MTExtra-trazo"]
        glifos_d = [s for _, s in den if s["font"] != "MTExtra-trazo"]
        if yb - max(s["bbox"][3] for s in glifos_n) > 3.5 or min(s["bbox"][1] for s in glifos_d) - yb > 3.5:
            continue
        # Filas de una lista de definiciones (x_i / x̄, P_n / M̄_x): cada fila sigue con «=» o texto.
        propios = [x for _, x in num + den]
        def alto_medio(g):
            return sum((x["bbox"][1] + x["bbox"][3]) / 2 for x in g) / len(g)
        filas_nd = (alto_medio(glifos_n), alto_medio(glifos_d))
        if any(o["text"].strip().startswith("=") and o not in propios and x1 + 3 < o["bbox"][0] < x1 + 45
               and any(abs((o["bbox"][1] + o["bbox"][3]) / 2 - c) < 3 for c in filas_nd)
               for l in lineas for o in l["spans"]):
            continue
        # Valores apilados en una celda: la «barra» es un borde que toca las verticales de la tabla.
        if any(abs(v.x0 - x0) < 2.5 or abs(v.x1 - x1) < 2.5 for v in verticales if v.y0 - 1 <= yb <= v.y1 + 1):
            continue
        texto_ = "\\frac{" + _pieza([s for _, s in num]) + "}{" + _pieza([s for _, s in den]) + "}"
        if texto_.count("{") != texto_.count("}") or re.search("[⎛⎜⎝⎞⎟⎠⎡⎢⎣⎤⎥⎦]", texto_):
            continue
        for l, s in num + den:
            if s in l["spans"]:
                l["spans"].remove(s)
        destino = min(prosa, key=lambda l: abs((l["bbox"][1] + l["bbox"][3]) / 2 - yb))
        # Un radical que envuelve la fracción (4.71√(E/F_y)) quedó en la línea del numerador: sus
        # trazos sintéticos pasan a la línea de destino para no perderse con ella.
        for l in {id(l): l for l, _ in num + den}.values():
            if l is destino:
                continue
            for s in [s for s in l["spans"] if s["font"] == "MTExtra-trazo"]:
                l["spans"].remove(s)
                destino["spans"].append(s)
        tam = max((s["size"] for _, s in num + den), default=10)
        sint = _span_sintetico(texto_, x0, yb - 6, yb + 6, tam)
        sint["font"] = "MTExtra-frac"
        destino["spans"].append(sint)
        destino["spans"].sort(key=lambda s: s["bbox"][0])
        TRAZOS["fracciones"] = TRAZOS.get("fracciones", 0) + 1
        caja = [min(s["bbox"][0] for _, s in num + den), min(s["bbox"][1] for _, s in num),
                max(s["bbox"][2] for _, s in num + den), max(s["bbox"][3] for _, s in den)]
        REGISTRO_FRACCIONES.append({"pagina": pagina.number + 1, "bbox": [round(v, 1) for v in caja], "latex": texto_})


def anotar_glifos(pagina, pagina_dict):
    """Guarda en cada span matemático la abscisa izquierda de cada carácter (rawdict).

    Un span como «A f» lleva dos bases; sin las posiciones, los subíndices de ambas se pegaban al
    final («A_{g c} f'»). inline() las usa para poner cada subíndice tras su propio glifo.
    """
    crudo = None
    for bi, b in enumerate(pagina_dict["blocks"]):
        for li, l in enumerate(b.get("lines", [])):
            for si, s in enumerate(l["spans"]):
                if not es_mate(s) or len(s["text"].strip()) < 2:
                    continue
                if crudo is None:
                    crudo = pagina.get_text("rawdict")
                chars = crudo["blocks"][bi]["lines"][li]["spans"][si]["chars"]
                if len(chars) == len(s["text"]):
                    s["_x0"] = [c["bbox"][0] for c in chars]
    return pagina_dict


def lineas_pagina(pagina):
    salida = []
    d = anotar_glifos(pagina, normalizar_glifos(pagina, pagina.get_text("dict")))
    for b in inyectar_trazos(pagina, d)["blocks"]:
        for l in b.get("lines", []):
            spans = [s for s in l["spans"] if s["text"] != ""]
            t = texto(spans).strip()
            # Las líneas de índice terminan en número de página («....... C-45»); las de texto con
            # puntos de relleno («Losas sin ábacos ........ 125 mm») se conservan.
            if not t or RE_ENCAB.match(t) or re.search(r"\.{6,}\s*[A-K]-\d+\s*$", t):
                continue
            salida.append({"bbox": list(l["bbox"]), "spans": spans})
    return salida


def _fila_con_texto(lineas, o):
    """¿Hay texto (no matemático) en la misma fila que la línea o, a menos de 60 pt de ella?

    60 pt: en las listas de definiciones el símbolo y el «=» de su descripción están en columnas
    separadas («h_wc      =   altura del alma plana recortada»).
    """
    ox0, oy0, ox1, oy1 = o["bbox"]
    alto = oy1 - oy0
    for t in lineas:
        if t is o or solo_mate(t):
            continue
        txt = texto(t["spans"]).strip()
        if not txt or RE_TAG.match(txt) or not any(c.isalpha() for c in txt):
            continue
        # Un subíndice en Arial («,min» de A_v,min en C.11-13) no es texto de la fila.
        if max(s["size"] for s in t["spans"]) < 0.8 * max(s["size"] for s in o["spans"]):
            continue
        tx0, ty0, tx1, ty1 = t["bbox"]
        traslapo = min(oy1, ty1) - max(oy0, ty0)
        if traslapo > 0.5 * min(alto, ty1 - ty0) and (ox0 - 60 <= tx1 and tx0 <= ox1 + 60):
            return True
    return False


def expandir(lineas, semilla, usados, margen, limites=None):
    """Banda de una ecuación: la línea semilla más las líneas matemáticas que se le traslapan.

    limites (y_min, y_max): el centro de cada línea absorbida debe quedar dentro; evita que una
    ecuación numerada se trague las vecinas cuando están pegadas (F.2.11.2-19 a -21).
    """
    caja, miembros = list(lineas[semilla]["bbox"]), {semilla}
    sy0, sy1 = lineas[semilla]["bbox"][1], lineas[semilla]["bbox"][3]
    # Con límites (ecuación numerada), una línea matemática que comparte fila con texto es parte
    # de ese texto: «E = módulo de elasticidad», «Para P_u ≤ 0.4P_y» (Título F). La fila del número
    # se respeta («b_d = w cuando λ ≤ 0.673 (F.4.2.2-6)»). Las líneas pegadas a una excluida (sus
    # subíndices, que el PDF trae aparte) también quedan fuera.
    fuera = set()
    if limites:
        def en_fila_numero(o):
            return sy0 - 2 <= (o["bbox"][1] + o["bbox"][3]) / 2 <= sy1 + 2
        fuera = {j for j, o in enumerate(lineas) if j != semilla and solo_mate(o) and not en_fila_numero(o)
                 and _fila_con_texto(lineas, o)}
        crece = True
        while crece:
            crece = False
            for j, o in enumerate(lineas):
                if j in fuera or j == semilla or not solo_mate(o) or en_fila_numero(o):
                    continue
                ox0, oy0, ox1, oy1 = o["bbox"]
                cy, tam = (oy0 + oy1) / 2, max(s["size"] for s in o["spans"])
                # Solo los scripts de la línea excluida: menores, pegados en x y con el centro dentro
                # de su franja (un numerador vecino no: F.4.2.2-12 bajo la condición de F.4.2.2-11).
                for k in fuera:
                    kx0, ky0, kx1, ky1 = lineas[k]["bbox"]
                    if tam < 0.9 * max(s["size"] for s in lineas[k]["spans"]) and kx0 - 2 <= ox0 <= kx1 + 2 \
                            and ky0 - 3 <= cy <= ky1 + 3:
                        fuera.add(j)
                        crece = True
                        break
    cambio = True
    while cambio:
        cambio = False
        for j, o in enumerate(lineas):
            if j in miembros or j in usados or j in fuera or not solo_mate(o):
                continue
            if limites and not limites[0] <= (o["bbox"][1] + o["bbox"][3]) / 2 <= limites[1]:
                continue
            if o["bbox"][1] <= caja[3] + margen and o["bbox"][3] >= caja[1] - margen:
                miembros.add(j)
                caja = [min(caja[0], o["bbox"][0]), min(caja[1], o["bbox"][1]),
                        max(caja[2], o["bbox"][2]), max(caja[3], o["bbox"][3])]
                cambio = True
    return caja, miembros


def bandas_ecuacion(lineas):
    usados, bandas = set(), []
    centros = sorted((l["bbox"][1] + l["bbox"][3]) / 2 for l in lineas if RE_TAG.match(texto(l["spans"]).strip()))
    for i, l in enumerate(lineas):
        m = RE_TAG.match(texto(l["spans"]).strip())
        if m:
            # Hasta la mitad de la distancia a la ecuación numerada vecina (si está a menos de 60 pt).
            cy = (l["bbox"][1] + l["bbox"][3]) / 2
            antes = [c for c in centros if cy - 60 < c < cy - 0.5]
            despues = [c for c in centros if cy + 0.5 < c < cy + 60]
            limites = ((cy + max(antes)) / 2 if antes else -1e9, (cy + min(despues)) / 2 if despues else 1e9)
            caja, miembros = expandir(lineas, i, usados, 4, limites)
            # El texto de la fila del número es de la ecuación («cuando», «• Soldada, semi-compacta»):
            # va con ella y sale del párrafo, para que no quede repetido en los dos. Solo en los
            # títulos transcritos con transcribir.py (incluye ese texto); las transcripciones a mano
            # de A, B y C traen solo la fórmula y el texto de la fila («en (N/m2)», «(a)») se perdería.
            sy0, sy1 = l["bbox"][1], l["bbox"][3]
            for j, t in enumerate(lineas):
                if not FILA_DEL_NUMERO or j in usados or j in miembros or solo_mate(t):
                    continue
                ty = (t["bbox"][1] + t["bbox"][3]) / 2
                if sy0 - 2 <= ty <= sy1 + 2 and t["bbox"][0] >= caja[0] - 220 and t["bbox"][2] <= caja[2] + 2:
                    miembros.add(j)
                    caja = [min(caja[0], t["bbox"][0]), min(caja[1], t["bbox"][1]),
                            max(caja[2], t["bbox"][2]), max(caja[3], t["bbox"][3])]
            usados |= miembros
            bandas.append({"tag": m.group(1), "bbox": caja, "miembros": miembros})
    for j, o in enumerate(lineas):
        if j in usados or not solo_mate(o) or len(texto(o["spans"]).strip()) <= 2:
            continue
        caja, miembros = expandir(lineas, j, usados, 3)
        llaves = any(LLAVES & set(texto(lineas[k]["spans"])) for k in miembros)
        if (len(miembros) >= 4 and (caja[2] - caja[0]) > 60) or (llaves and len(miembros) >= 2):
            if FILA_DEL_NUMERO:
                # Banda sin número: el texto de sus filas («ó», «cuando») va con ella (ver arriba).
                filas_m = [(lineas[k]["bbox"][1], lineas[k]["bbox"][3]) for k in miembros]
                for k, t in enumerate(lineas):
                    if k in usados or k in miembros or solo_mate(t):
                        continue
                    ty = (t["bbox"][1] + t["bbox"][3]) / 2
                    if caja[0] - 2 <= t["bbox"][0] and t["bbox"][2] <= caja[2] + 2 \
                            and any(a - 2 <= ty <= b + 2 for a, b in filas_m):
                        miembros.add(k)
            usados |= miembros
            bandas.append({"tag": None, "bbox": caja, "miembros": miembros, "llaves": llaves})
    return bandas, usados


def asignar_subindices(lineas, ignorar):
    """Lineas diminutas de simbolos (sub/superindices) -> se pegan al simbolo vecino."""
    resultado, absorbidas = {}, set()
    for j, l in enumerate(lineas):
        if j in ignorar or not solo_mate(l):
            continue
        t = texto(l["spans"]).strip()
        tam = max(s["size"] for s in l["spans"])
        if not t or len(t) > 4:
            continue
        def base(caja):
            x0, y0, x1, y1 = caja
            mejor = None
            for k, o in enumerate(lineas):
                if k == j or k in ignorar:
                    continue
                for s in o["spans"]:
                    if not es_mate(s) or not s["text"].strip()[-1:].isalnum() or s["size"] <= tam:
                        continue
                    sx0, sy0, sx1, sy1 = s["bbox"]
                    if sx0 - 1 <= x0 <= sx1 + 4 and sy0 - 8 <= y0 <= sy1:
                        sup = (y0 + y1) / 2 < (sy0 + sy1) / 2 - 1
                        d = abs(x0 - sx1)
                        if mejor is None or d < mejor[0]:
                            mejor = (d, s, sup)
            return mejor

        # Una línea diminuta puede traer los subíndices de dos bases seguidas («g c» de A_g f'_c):
        # cada pieza separada por espacio busca su propia base.
        piezas = [s for s in l["spans"] if s["text"].strip() and s["font"] != "MTExtra-trazo"]
        unidades = [(s["bbox"], s["text"].strip()) for s in piezas] if len(piezas) > 1 else [(l["bbox"], t)]
        bases = [base(c) for c, _ in unidades]
        if len(unidades) > 1 and not all(bases):
            unidades, bases = [(l["bbox"], t)], [base(l["bbox"])]
        mejor = bases[0] if len(bases) == 1 else True
        for (caja, txt), m in zip(unidades, bases):
            if m:
                resultado.setdefault(id(m[1]), []).append((caja[0], txt, m[2]))
        if mejor:
            absorbidas.add(j)
    return resultado, absorbidas


def inline(spans, subindices):
    spans = sorted(spans, key=lambda s: s["bbox"][0])
    partes, mate = [], []
    previo = None

    def cerrar():
        crudo = "".join(mate)
        t = crudo.strip()
        # La prima va pegada a la base (f′c → f'_{c}) y KaTeX no acepta dos subíndices seguidos.
        t = re.sub(r"_\{([^{}]+)\}_\{′\}", r"'_{\1}", t)
        t = re.sub(r"_\{([^{}]+)\}_\{([^{}]+)\}", r"_{\1,\2}", t)
        t = t.replace("′", "'").replace("´", "'")
        # Grados de MTExtra (45° como superíndice) y tilde de k̃ (Título F).
        if re.search(r"\d\s*(\^\{)?°", t):
            t = t.replace("^{°}", r"^{\circ}").replace("°", r"^{\circ}")
        t = re.sub(r"(\w)\^\{˜\}", r"\\tilde{\1}", t)
        t = re.sub(r"\s*[⊥┴]", r"\\perp ", t).strip()   # F_{c⊥} del Título G
        if t == "█":
            # Marca negra de fin de capítulo (Título D): no es contenido.
            mate.clear()
            return
        if t in ("°", "º"):
            # Grados sueltos en la fuente Symbol (45°, ángulos del Título D): es texto, no fórmula.
            partes.append(t + (" " if crudo.endswith(" ") else ""))
            mate.clear()
            return
        m = re.fullmatch(r'"(\w{1,3})"', t)
        if m:
            # Ejes y subíndices citados entre comillas («eje "y"» en el Título F).
            partes.append(f'"${m.group(1)}$"' + (" " if crudo.endswith(" ") else ""))
            mate.clear()
            return
        # Acento circunflejo suelto (b̂ y α̂ de la Tabla B.6.5-2) y texto con tildes dentro de la fórmula.
        t = re.sub(r"\bca,\s*(m[áí][xn])", r"c_{a,\1}", t)   # c_{a,mín} y c_{a,máx} del Apéndice C-D
        t = re.sub(r"ˆ(\w)", r"\\hat{\1}", t)
        t = re.sub(r"(\w)ˆ", r"\\hat{\1}", t)
        t = re.sub(r"([A-Za-záéíóúñÁÉÍÓÚÑ]*[áéíóúñÁÉÍÓÚÑ][A-Za-záéíóúñÁÉÍÓÚÑ]*)", r"\\text{\1}", t)
        if t:
            partes.append(f"${t}$" + (" " if crudo.endswith(" ") else ""))
        mate.clear()

    for s in spans:
        if not s["text"].strip():
            # Un espacio entre simbolos no corta la formula.
            (mate if mate else partes).append(" ")
            continue
        t = s["text"].strip()
        if es_mate(s) and t in ("•", "—", "–", '"', "“", "”", "*"):
            cerrar()
            partes.append(s["text"])
            continue
        if es_mate(s) and previo is not None and mate and re.fullmatch(r"[A-Za-z0-9,]{1,4}", t) \
                and previo["text"].strip()[-1:].isalnum() and s["size"] < 0.95 * previo["size"]:
            centro, centro_prev = (s["bbox"][1] + s["bbox"][3]) / 2, (previo["bbox"][1] + previo["bbox"][3]) / 2
            if abs(centro - centro_prev) > 1:
                while mate and mate[-1] == " ":
                    mate.pop()
                mate.append(("^{" if centro < centro_prev else "_{") + t + "}")
                continue
        if es_mate(s) and s["text"].strip():
            previo = s
            subs_s = sorted(subindices.get(id(s), []))
            xs = s.get("_x0")
            if xs and subs_s and len(s["text"].strip()) > 1 and len(xs) == len(s["text"]):
                # Varias bases en el span: cada subíndice va tras el último glifo que empieza antes que él.
                tras = {}
                for (x, txt, sup) in subs_s:
                    k = max((i for i, xc in enumerate(xs) if xc <= x and s["text"][i].strip()), default=len(xs) - 1)
                    tras.setdefault(k, []).append(("^{" if sup else "_{") + txt + "}")
                for i, ch in enumerate(s["text"]):
                    mate.append(ch.replace("%", r"\%"))
                    mate.extend(tras.get(i, []))
                continue
            mate.append(s["text"].replace("%", r"\%"))
            for (_, txt, sup) in subs_s:
                mate.append(("^{" if sup else "_{") + txt + "}")
        else:
            cerrar()
            partes.append(s["text"])
    cerrar()
    return re.sub(r"\s+", " ", "".join(partes)).strip()


def filas(lineas, excluir):
    """Agrupa las lineas de una misma altura (simbolo + definicion) en una fila."""
    restantes = sorted((j for j in range(len(lineas)) if j not in excluir),
                       key=lambda j: (lineas[j]["bbox"][1], lineas[j]["bbox"][0]))
    grupos = []
    for j in restantes:
        y0, y1 = lineas[j]["bbox"][1], lineas[j]["bbox"][3]
        for g in grupos:
            gy0, gy1 = g["y"]
            if min(y1, gy1) - max(y0, gy0) > 0.5 * min(y1 - y0, gy1 - gy0):
                g["ids"].append(j)
                g["y"] = (min(gy0, y0), max(gy1, y1))
                break
        else:
            grupos.append({"ids": [j], "y": (y0, y1)})
    for g in grupos:
        g["ids"].sort(key=lambda j: lineas[j]["bbox"][0])
    return grupos


def tabla_md(tabla):
    datos = [[(c or "").replace("\n", " ").strip() for c in fila] for fila in tabla.extract()]
    datos = [f for f in datos if any(f)]
    if len(datos) < 2 or max(len(f) for f in datos) < 2:
        return None
    n = max(len(f) for f in datos)
    datos = [f + [""] * (n - len(f)) for f in datos]
    def esc(c):
        c = re.sub(r"\s+", " ", c.replace("|", "\\|"))
        return re.sub(r"\b([A-Z]) ?([≤≥=<>]) ?([\d.,]+) ([a-z])\b", r"\1\4 \2 \3", c)
    md = ["| " + " | ".join(esc(c) for c in datos[0]) + " |", "|" + "---|" * n]
    md += ["| " + " | ".join(esc(c) for c in f) + " |" for f in datos[1:]]
    return "\n".join(md)


def tabla_md_rica(tabla, lineas, subs, absorbidas, usados):
    """Tabla Markdown con el texto de cada celda armado desde los spans (subindices, simbolos).

    Si una celda trae varios valores numéricos apilados (p. ej. Tabla B.6.5-4: «0.85 / 0.85»),
    la fila se divide en subfilas alineando cada valor con el texto de su misma altura."""
    filas_md, total, vacias = [], 0, 0
    numerico = re.compile(r"^[\d.,\s*†‡§−-]+$")
    for fila in tabla.rows:
        celdas = []
        for caja in fila.cells:
            total += 1
            if caja is None:
                celdas.append([])
                vacias += 1
                continue
            cx0, cy0, cx1, cy1 = caja
            ids = [j for j, l in enumerate(lineas) if j not in absorbidas and j not in usados
                   and cx0 - 1 <= (l["bbox"][0] + l["bbox"][2]) / 2 <= cx1 + 1
                   and cy0 - 1 <= (l["bbox"][1] + l["bbox"][3]) / 2 <= cy1 + 1]
            partes = []
            for g in filas(lineas, set(range(len(lineas))) - set(ids)):
                spans = [s for j in g["ids"] for s in lineas[j]["spans"]]
                t = inline(spans, subs).replace("|", "\\|")
                if t:
                    partes.append(((g["y"][0] + g["y"][1]) / 2, t))
            if not partes:
                vacias += 1
            celdas.append(sorted(partes))
        if not any(celdas):
            continue
        apiladas = [k for k, c in enumerate(celdas) if len(c) >= 2 and all(numerico.match(t) for _, t in c)]
        if apiladas:
            anclas = [y for y, _ in celdas[apiladas[0]]]
            subfilas = [[[] for _ in celdas] for _ in anclas]
            for k, c in enumerate(celdas):
                for y, t in c:
                    i = min(range(len(anclas)), key=lambda n: abs(y - anclas[n]))
                    subfilas[i][k].append(t)
            for sf in subfilas:
                filas_md.append([" ".join(x) for x in sf])
        else:
            filas_md.append([" ".join(t for _, t in c) for c in celdas])
    if len(filas_md) < 2 or max(len(f) for f in filas_md) < (1 if getattr(tabla, "una_columna", False) else 2):
        return None, 1.0
    n = max(len(f) for f in filas_md)
    filas_md = [f + [""] * (n - len(f)) for f in filas_md]
    # Columnas de rejilla sin ningún contenido (celdas combinadas en el PDF): se eliminan.
    utiles = [j for j in range(n) if any(f[j] for f in filas_md)]
    filas_md = [[f[j] for j in utiles] for f in filas_md]
    n = len(utiles)
    md = ["| " + " | ".join(filas_md[0]) + " |", "|" + "---|" * n]
    md += ["| " + " | ".join(f) + " |" for f in filas_md[1:]]
    return "\n".join(md), vacias / max(total, 1)


class _Fila:
    def __init__(self, cells):
        self.cells = cells


class _TablaUnaColumna:
    """Lista en recuadro de una sola columna (Tablas K.2.2-2 y similares), que find_tables no detecta."""
    una_columna = True

    def __init__(self, x0, ys, x1):
        self.bbox = (x0, ys[0], x1, ys[-1])
        self.rows = [_Fila([(x0, a, x1, b)]) for a, b in zip(ys, ys[1:])]


def tablas_una_columna(pagina, existentes):
    """Rejillas de una columna dibujadas con rectángulos finos: líneas horizontales del mismo ancho,
    apiladas y cerradas por dos verticales en sus extremos."""
    horiz, vert = {}, []
    for d in pagina.get_drawings():
        for it in d["items"]:
            if it[0] != "re":
                continue
            r = it[1]
            if r.height <= 2.5 and r.width > 40:
                # Los bordes exteriores llegan con 1-2 pt más de ancho que las divisiones interiores.
                clave = next((k for k in horiz if abs(k[0] - r.x0) < 3 and abs(k[1] - r.x1) < 3),
                             (round(r.x0), round(r.x1)))
                horiz.setdefault(clave, []).append((r.y0 + r.y1) / 2)
            elif r.width <= 2.5 and r.height > 4:
                vert.append(r)
    tablas = []
    for (x0, x1), ys in horiz.items():
        ys = sorted(set(round(y, 1) for y in ys))
        grupo = [ys[0]]
        for y in ys[1:] + [None]:
            if y is not None and y - grupo[-1] < 40:
                grupo.append(y)
                continue
            cerrada = all(any(abs(v.x0 - x) < 3 and v.y0 <= a + 2 and v.y1 >= b - 2 for v in vert)
                          for x in (x0, x1) for a, b in zip(grupo, grupo[1:]))
            solapa = any(t.bbox[0] - 3 <= x0 and x1 <= t.bbox[2] + 3 and t.bbox[1] - 3 <= grupo[0]
                         and grupo[-1] <= t.bbox[3] + 3 for t in existentes)
            if len(grupo) >= 3 and cerrada and not solapa:
                tablas.append(_TablaUnaColumna(x0, grupo, x1))
            if y is not None:
                grupo = [y]
    return tablas


def procesar(pdf, letra, salida):
    global FILA_DEL_NUMERO, FRACCIONES_EN_LINEA
    FILA_DEL_NUMERO = letra in TITULOS_FILA_DEL_NUMERO
    FRACCIONES_EN_LINEA = letra in TITULOS_FRACCIONES_EN_LINEA
    doc = pymupdf.open(pdf)
    ruta_json = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ecuaciones", f"{letra}.json")
    latex = json.load(open(ruta_json, encoding="utf-8")) if os.path.exists(ruta_json) else {}
    os.makedirs(os.path.join(salida, "img"), exist_ok=True)
    indice = {}
    for pagina in doc:
        for linea in pagina.get_text().splitlines():
            m = re.match(r"^\s*CAP[ÍI]TULO\s+([A-K]\.\d+)\s*[—–-]\s*(.+?)\s*\.{3,}", linea)
            if m:
                indice.setdefault(m.group(1), m.group(2).strip())
    eventos = []
    # Portada, comisión e índices (con listas de tablas y figuras) van antes del primer capítulo:
    # se omiten para que no se confundan con el texto ni con las figuras reales.
    inicio = 0
    for np_, pagina in enumerate(doc):
        cap = [l for l in pagina.get_text("dict")["blocks"] for l in l.get("lines", [])
               if RE_CAP.match("".join(s["text"] for s in l["spans"]).strip())
               and max(s["size"] for s in l["spans"]) >= 13]
        if cap:
            inicio = np_
            break
    for np_, pagina in enumerate(doc):
        if np_ < inicio:
            continue
        if pagina.rotation:
            # Página apaisada (tablas de coeficientes de G.2 y G.4): el texto viene girado y no se puede
            # leer como filas; va completa como imagen, con el rótulo de su tabla como pie.
            girado = sum(len(s["text"]) for b in pagina.get_text("dict")["blocks"] for l in b.get("lines", [])
                         for s in l["spans"] if abs(l["dir"][0]) < 0.9)
            if girado > 200:
                rotulo = re.search(r"Tabla\s+[A-K]\.[\d.]+-\d+[a-z]?", pagina.get_text())
                pie = rotulo.group(0) if rotulo else "Página apaisada del original"
                archivo = f"pagina-p{np_ + 1}.png"
                pagina.get_pixmap(dpi=130).save(os.path.join(salida, "img", archivo))
                eventos.append((np_, 0, "fig", (pie, archivo)))
                continue
        lineas = lineas_pagina(pagina)
        bandas, usados = bandas_ecuacion(lineas)
        # 1) Figuras: pie "Figura X" con bloques de simbolos encima -> una sola imagen.
        figuras, en_figura = [], set()
        for j, l in enumerate(lineas):
            t = texto(l["spans"]).strip()
            # «Figura G 4.3-3 — …» va sin punto; con espacio se exige la raya tras el número.
            if not re.match(r"^Figura\s+[A-K](?:[.-]|\s\d[\d.]*-\d+\s*[—–])", t):
                continue
            cy = l["bbox"][1]
            # En D a K la figura no sube más allá de la última línea de prosa ni de una tabla que haya
            # encima: las definiciones con símbolos (bandas sin número) no son parte de ella (F.2.9.8-1).
            # También frenan el pie de otra figura y una ecuación numerada (F.5.5.1-2, F.5.6.9-2).
            # Prosa y notas (≥ 7.5 pt): los rótulos dentro del dibujo van en letra menor (≈ 6 pt).
            limite = [o["bbox"][3] for o in lineas if o["bbox"][3] < cy - 2
                      and max(s["size"] for s in o["spans"]) >= 7.5
                      and (len(texto(o["spans"]).strip()) >= 50 or texto(o["spans"]).strip().startswith("Figura"))]
            limite += [b["bbox"][3] for b in bandas if b["tag"] and b["bbox"][3] < cy - 2]
            try:
                # Solo tablas con texto en la mayoría de sus celdas: el marco de una figura también se
                # detecta como «tabla» (Figura G.3.4-3).
                for tb in pagina.find_tables().tables:
                    celdas = [c for fila in tb.extract() for c in fila]
                    if tb.bbox[3] < cy - 15 and celdas and sum(1 for c in celdas if c and c.strip()) >= 0.5 * len(celdas):
                        limite.append(tb.bbox[3])
            except Exception:
                pass
            tope = max(limite, default=0)
            arriba = [b for b in bandas if b["tag"] is None and cy - 400 < b["bbox"][1] < cy
                      and (b["bbox"][1] >= tope - 1 or not FRACCIONES_EN_LINEA)]
            if arriba:
                y0 = min(b["bbox"][1] for b in arriba)
            else:
                # Figura vectorial sin bandas de símbolos (Figura G 4.3-3): el recorte empieza en el primer
                # trazo de los que hay sobre el pie, bajo el encabezado de la página.
                trazos = [d["rect"] for d in pagina.get_drawings()
                          if cy - 450 < d["rect"].y0 and d["rect"].y1 <= cy and d["rect"].y0 > 70
                          and d["rect"].y0 >= tope - 1]
                # Las figuras raster (G.3.4-3, F.2.9.8-1) cuentan aunque no tengan trazos.
                fotos = [pymupdf.Rect(im["bbox"]) for im in pagina.get_image_info()
                         if tope - 1 <= im["bbox"][1] and im["bbox"][3] <= cy + 2 and im["bbox"][1] > 70]
                if len(trazos) < 3 and not fotos:
                    continue
                trazos += fotos
                y0 = min(r.y0 for r in trazos)
            for b in arriba:
                bandas.remove(b)
            for k, o in enumerate(lineas):
                if k != j and y0 - 2 <= o["bbox"][1] and o["bbox"][3] <= cy + 1:
                    en_figura.add(k)
            figuras.append((y0, cy, t))
        usados |= en_figura
        for b in [b for b in bandas if b["tag"] is None and not b.get("llaves")]:
            bandas.remove(b)
            usados -= (b["miembros"] - en_figura)
        # 2) Subindices de toda la pagina (texto y celdas de tablas).
        subs, absorbidas = asignar_subindices(lineas, usados)
        # 3) Tablas: celdas con formulas en linea; graficos y recuadros dudosos -> imagen.
        tablas, recortes = [], []
        try:
            encontradas = pagina.find_tables().tables
        except Exception:
            encontradas = []
        def contiene(a, b):
            return a is not b and a.bbox[0] <= b.bbox[0] + 1 and a.bbox[1] <= b.bbox[1] + 1                 and a.bbox[2] >= b.bbox[2] - 1 and a.bbox[3] >= b.bbox[3] - 1
        def marco_de_tabla(t):
            # Marco con el rótulo «Tabla X» dentro (Título B): se descarta y queda la tabla interior.
            return any(re.match(r"^Tabla\s+[A-K][.-]", texto(l["spans"]).strip())
                       and t.bbox[1] - 2 <= l["bbox"][1] <= t.bbox[3] and t.bbox[0] - 2 <= l["bbox"][0] <= t.bbox[2]
                       for l in lineas)
        encontradas = [t for t in encontradas
                       if not (marco_de_tabla(t) and any(contiene(t, o) for o in encontradas))]
        encontradas += tablas_una_columna(pagina, encontradas)
        imagenes = pagina.get_image_info()
        for t in encontradas:
            x0, y0, x1, y1 = t.bbox
            if any(fy0 - 6 <= y0 and y1 <= fcy + 6 for fy0, fcy, _ in figuras):
                continue
            con_titulo = any(re.match(r"^(Tabla|TABLA)\s+[A-K][.-]", texto(l["spans"]).strip())
                             and y0 - 80 <= l["bbox"][1] <= y0 + 2 for l in lineas)
            dentro = [b for b in bandas if b["tag"] and x0 - 2 <= b["bbox"][0] and b["bbox"][2] <= x1 + 2
                      and y0 - 2 <= b["bbox"][1] and b["bbox"][3] <= y1 + 2]
            fotos = sum(1 for im in imagenes if x0 - 2 <= im["bbox"][0] and im["bbox"][2] <= x1 + 2
                        and y0 - 2 <= im["bbox"][1] and im["bbox"][3] <= y1 + 2)
            if dentro and fotos:
                # Tabla con ecuaciones numeradas e imágenes en las celdas (Tablas F.2.11.1-1 a F.2.11.3-2):
                # no cabe en Markdown celda por celda; va completa como recorte del PDF.
                recortes.append(t.bbox)
                for b in [b for b in bandas if x0 - 2 <= b["bbox"][0] and b["bbox"][2] <= x1 + 2
                          and y0 - 2 <= b["bbox"][1] and b["bbox"][3] <= y1 + 2]:
                    bandas.remove(b)
                continue
            md, vacias = tabla_md_rica(t, lineas, subs, absorbidas, usados)
            if md is None:
                continue
            if not con_titulo and vacias > 0.45:
                recortes.append(t.bbox)
            else:
                tablas.append((t.bbox, md))
        # Rótulo «Tabla X» sin tabla debajo: recuadros que find_tables no reconoce (bloque FUNCIONES y
        # límites de aplicación de las Tablas F.2.11, ejemplos ilustrativos de la Tabla F.2.17-1).
        # Se recorta el marco dibujado que empieza justo bajo el rótulo y se extiende sin cortes.
        ocupadas = [bb for bb, _ in tablas] + recortes + [(0, fy0, 9999, fcy) for fy0, fcy, _ in figuras]
        rects = [d["rect"] for d in pagina.get_drawings() if d["rect"].width > 0.5 or d["rect"].height > 0.5]
        for j, l in enumerate(lineas):
            rotulo = texto(l["spans"]).strip()
            if not (re.match(r"^(Tabla|TABLA)\s+[A-K][.-]", rotulo) or rotulo == "FUNCIONES"):
                continue
            # El encabezado FUNCIONES va dentro del marco: el recorte empieza en su borde superior.
            cy = l["bbox"][3] if rotulo != "FUNCIONES" else l["bbox"][1] - 4
            if any(cy - 2 <= bb[1] <= cy + 80 or bb[1] - 2 <= l["bbox"][1] <= bb[3] for bb in ocupadas):
                continue
            marco = [r for r in rects if cy - 2 <= r.y0 <= cy + 40 and r.width > 150]
            if not marco:
                continue
            caja = pymupdf.Rect(marco[0])
            for r in marco[1:]:
                caja |= r
            creciendo = True
            while creciendo:
                creciendo = False
                for r in rects:
                    if r.y0 <= caja.y1 + 1.5 and r.y1 > caja.y1 + 0.5 and r.x1 > caja.x0 and r.x0 < caja.x1:
                        caja |= r
                        creciendo = True
            if caja.height < 15:
                continue
            recortes.append(tuple(caja))
            ocupadas.append(tuple(caja))
            for b in [b for b in bandas if caja.y0 - 2 <= b["bbox"][1] and b["bbox"][3] <= caja.y1 + 2]:
                bandas.remove(b)
        en_tabla = set()
        for j, l in enumerate(lineas):
            cx, cy = (l["bbox"][0] + l["bbox"][2]) / 2, (l["bbox"][1] + l["bbox"][3]) / 2
            if any(b[0] - 2 <= cx <= b[2] + 2 and b[1] - 2 <= cy <= b[3] + 2 for b in [bb for bb, _ in tablas] + recortes):
                en_tabla.add(j)
        for y0, cy, t in figuras:
            nombre = re.sub(r"[^A-Za-z0-9.-]", "", t.split("—")[0].replace("Figura", "fig"))
            archivo = f"{nombre}.png"
            clip = pymupdf.Rect(36, y0 - 6, pagina.rect.width - 36, cy - 1)
            pagina.get_pixmap(clip=clip, dpi=160).save(os.path.join(salida, "img", archivo))
            eventos.append((np_, y0, "fig", (t, archivo)))
        for k, (x0, y0, x1, y1) in enumerate(recortes):
            archivo = f"recuadro-p{np_ + 1}-{int(y0)}.png"
            clip = pymupdf.Rect(max(x0 - 4, 0), y0 - 4, min(x1 + 4, pagina.rect.width), y1 + 4)
            pagina.get_pixmap(clip=clip, dpi=160).save(os.path.join(salida, "img", archivo))
            eventos.append((np_, y0, "fig", ("Recuadro de la página original", archivo)))
        for b in bandas:
            x0, y0, x1, y1 = b["bbox"]
            nombre = b["tag"] or f"p{np_ + 1}-{int(y0)}"
            archivo = f"ec-{nombre}.png"
            k = 2
            while os.path.exists(os.path.join(salida, "img", archivo)):
                archivo = f"ec-{nombre}-{k}.png"
                k += 1
            clip = pymupdf.Rect(max(x0 - 4, 0), y0 - 3, min(x1 + 4, pagina.rect.width), y1 + 3)
            pagina.get_pixmap(clip=clip, dpi=200).save(os.path.join(salida, "img", archivo))
            REGISTRO_BANDAS.append((np_, tuple(b["bbox"]), archivo,
                                    [tuple(lineas[j]["bbox"]) for j in b.get("miembros", ())]))
            eventos.append((np_, y0, "ec", (b["tag"], archivo)))
        for bb, md in tablas:
            eventos.append((np_, bb[1], "tabla", md))
        for g in filas(lineas, usados | en_tabla | absorbidas):
            spans = [s for j in g["ids"] for s in lineas[j]["spans"]]
            primero = next((s for s in spans if s["text"].strip()), spans[0])
            info = {"negrita": es_negrita(primero), "tam": max(s["size"] for s in spans),
                    "x0": lineas[g["ids"][0]]["bbox"][0]}
            eventos.append((np_, g["y"][0], "fila", (inline(spans, subs), info)))
    eventos.sort(key=lambda e: (e[0], round(e[1], 1)))
    escribir(eventos, letra, salida, latex, indice)
    limpiar_imagenes(salida)


def limpiar_imagenes(salida):
    """Borra los recortes que ningun capitulo usa (ecuaciones ya pasadas a LaTeX)."""
    usadas = set()
    for nombre in os.listdir(salida):
        if nombre.endswith(".md"):
            usadas |= set(re.findall(r"img/([^)\s]+)", open(os.path.join(salida, nombre), encoding="utf-8").read()))
    carpeta = os.path.join(salida, "img")
    for nombre in os.listdir(carpeta):
        if nombre not in usadas:
            os.remove(os.path.join(carpeta, nombre))


def escribir(eventos, letra, salida, latex, indice=None):
    indice_tit = indice or {}
    capitulos = []
    estado = {"id": f"{letra}.0", "titulo": ["Preliminares"], "lineas": [], "abierto_titulo": False}
    parrafo = []
    usadas = set()

    def volcar():
        if parrafo:
            estado["lineas"] += [" ".join(parrafo).strip(), ""]
            parrafo.clear()

    def cerrar_capitulo():
        volcar()
        capitulos.append((estado["id"], " ".join(estado["titulo"]).strip(), estado["lineas"]))

    for _, _, tipo, cont in eventos:
        if tipo == "ec":
            volcar()
            estado["abierto_titulo"] = False
            tag, archivo = cont
            clave = "img:" + os.path.splitext(archivo)[0]   # ecuaciones sin número o repetidas
            if tag and tag in latex and tag not in usadas:
                usadas.add(tag)
                estado["lineas"] += [f"$$ {latex[tag]} \\tag{{{tag}}} $$", ""]
            elif latex.get(clave) == "__omitir__":
                pass   # recorte repetido: su contenido ya está en el texto o en una tabla corregida
            elif clave in latex:
                etiqueta = f" \\tag{{{tag}}}" if tag else ""
                estado["lineas"] += [f"$$ {latex[clave]}{etiqueta} $$", ""]
            else:
                estado["lineas"] += [f"![Ecuación{' ' + tag if tag else ''}](img/{archivo})", ""]
            continue
        if tipo == "fig":
            volcar()
            pie, archivo = cont
            estado["lineas"] += [f"![{pie}](img/{archivo})", ""]
            continue
        if tipo == "tabla":
            volcar()
            estado["abierto_titulo"] = False
            estado["lineas"] += [cont, ""]
            continue
        t, info = cont
        if not t:
            continue
        # «APENDICE F.5.I» llega con la I como letra matemática («F.5.$i$»).
        t_cap = re.sub(r"\$([A-Za-z])\$", r"\1", t)
        mcap = RE_CAP.match(t_cap)
        if mcap and info["tam"] >= 13:
            cerrar_capitulo()
            estado.update(id=re.sub(r"\.([A-Z])$", r"-\1", mcap.group(2).upper()), titulo=[], lineas=[], abierto_titulo=True)
            resto = t_cap[mcap.end():].strip(" —–-")
            if resto:
                estado["titulo"].append(resto)
            continue
        if estado["abierto_titulo"] and info["tam"] >= 13:
            estado["titulo"].append(t)
            continue
        estado["abierto_titulo"] = False
        m = RE_ART.match(t)
        if m and info["negrita"] and m.group(1).startswith((letra + ".", letra + "-")):
            volcar()
            # «C.C.9.2» es una errata del original por «C-C.9.2».
            num, resto = re.sub(r"^([A-K])\.([A-Z])\.", lambda x: x.group(1) + "-" + x.group(2) + ".", m.group(1)), m.group(2).strip()
            cap_art = ".".join(num.split(".")[:2])
            if re.match(r"^[A-K]\.\d+$", estado["id"]) and cap_art != estado["id"] \
                    and int(cap_art.split(".")[1]) == int(estado["id"].split(".")[1]) + 1:
                cerrar_capitulo()
                estado.update(id=cap_art, titulo=[indice_tit.get(cap_art, "")], lineas=[], abierto_titulo=False)
            mdoble = re.match(r"^([A-K][.-]\d+(?:\.\d+)*)\s*[—–-]?\s*(.*)$", resto)
            if mdoble and num.count(".") == 1:
                parrafo_num = f"{num}-{mdoble.group(1)}"
                volcar()
                parrafo.append(f"**{parrafo_num}** — {mdoble.group(2).strip()}")
                continue
            nivel = num.count(".")
            partes = re.split(r"\s+[—–]\s+", resto, maxsplit=1)
            titulo = partes[0].strip(" —–")
            es_titulo = nivel <= 3 and (len(partes) == 2 or titulo.isupper() or len(titulo) < 70)
            if es_titulo:
                estado["lineas"] += [f"{'#' * (nivel + 1)} {num} — {titulo}", ""]
                if len(partes) == 2 and partes[1].strip():
                    parrafo.append(partes[1].strip())
            else:
                parrafo.append(f"**{num}** — {resto}")
            continue
        mtab = re.match(r"^(Tabla|TABLA)\s+([A-K][.-][\dA-Z.]+(?:\s?-\s?(?:[A-K]\.)?[\d.]*\d[a-z]?)?(?:\s*\([a-zA-Z]+\))?)\s*[—–-]?\s*(.*)$", t)
        if mtab:
            volcar()
            numero = re.sub(r"\s+", "", mtab.group(2))
            estado["lineas"] += [f"**Tabla {numero}** — {mtab.group(3).strip()}".rstrip(" —"), ""]
            continue
        if re.match(r"^\(?[a-z]\)\s", t) or re.match(r"^\d+\.\s", t) or t.startswith("$") and "=" in t[:40]:
            volcar()
        parrafo.append(t)
        if t.endswith((".", ":")):
            volcar()
    cerrar_capitulo()

    # Un capítulo repetido (encabezado mal leído) se une al anterior: nunca se pisa un archivo.
    unidos = {}
    for cid, titulo, lineas in capitulos:
        if cid in unidos:
            print(f"  capítulo {cid} repetido: se une al anterior")
            unidos[cid][1].extend(lineas)
        else:
            unidos[cid] = [titulo, list(lineas)]
    capitulos = [(cid, t, l) for cid, (t, l) in unidos.items()]
    os.makedirs(salida, exist_ok=True)
    indice = [f"# NSR-10 — Título {letra}", "",
              "Texto del reglamento sin paginación, organizado por capítulo y artículo.", ""]
    for cid, titulo, lineas in capitulos:
        if sum(1 for x in lineas if x.strip()) < 3:
            continue
        titulo = titulo or TITULOS_CONOCIDOS.get(cid, "")
        if titulo.isupper():
            titulo = titulo[:1] + titulo[1:].lower()
            titulo = re.sub(r"(nsr-10|dmo|des|dmi|aci)", lambda m: m.group(1).upper(), titulo)
        nombre = (cid.replace(".", ".0") if re.match(r"^[A-K]\.\d$", cid) else cid) + ".md"
        cuerpo = [f"# {cid} — {titulo}", ""] + lineas
        # Viñetas cuadradas de Wingdings (0x83, informe de supervisión del Título I) -> lista Markdown.
        cuerpo = [re.sub(r"^\x83\s*", "- ", x) for x in cuerpo]
        open(os.path.join(salida, nombre), "w", encoding="utf-8").write("\n".join(cuerpo).rstrip() + "\n")
        indice.append(f"- [{cid} — {titulo}]({nombre})")
    open(os.path.join(salida, "README.md"), "w", encoding="utf-8").write("\n".join(indice) + "\n")


if __name__ == "__main__":
    procesar(sys.argv[1], sys.argv[2], sys.argv[3])
