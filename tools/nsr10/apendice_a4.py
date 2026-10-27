"""Reconstruye el Apéndice A-4 (municipios) desde la geometría del PDF del Título A.

Uso: python tools/nsr10/apendice_a4.py <Titulo-A.pdf> normativa/nsr10/titulo-a/A-4.md

Cada fila del PDF se arma con las palabras alineadas a la misma altura; el código DANE de cinco dígitos
separa el nombre del municipio de sus valores. Los encabezados «Departamento de …» abren una tabla nueva.
"""
import re
import sys

import pymupdf

RE_DEP = re.compile(r"^(Departamento|Archipi[eé]lago|Distrito|Bogot[aá]).*")
RE_FILA = re.compile(r"^(.+?)\s+(\d{5})\s+(0\.\d\d)\s+(0\.\d\d)\s+(Alta|Intermedia|Baja)\s+(0\.\d\d)\s+(0\.\d\d)$")
ENCABEZADO = "| Municipio | Código Municipio | $A_{a}$ | $A_{v}$ | Zona de Amenaza Sísmica | $A_{e}$ | $A_{d}$ |\n|---|---|---|---|---|---|---|"


def filas_pdf(doc):
    for pagina in doc:
        palabras = pagina.get_text("words")
        if not any(re.fullmatch(r"\d{5}", w[4]) for w in palabras):
            continue
        grupos = []
        for w in sorted(palabras, key=lambda w: ((w[1] + w[3]) / 2, w[0])):
            y = (w[1] + w[3]) / 2
            if grupos and abs(grupos[-1][0] - y) < 3:
                grupos[-1][1].append(w)
            else:
                grupos.append([y, [w]])
        for _, ws in grupos:
            yield " ".join(w[4] for w in sorted(ws, key=lambda w: w[0])).strip()


def construir(pdf):
    doc = pymupdf.open(pdf)
    titulo = None
    for pagina in doc:
        t = pagina.get_text()
        if "Departamento de Amazonas" in t:
            break
    salida, actual, total = [], None, 0
    for texto in filas_pdf(doc):
        m = RE_FILA.match(texto)
        if m:
            if actual is None:
                continue
            nombre, cod, aa, av, zona, ae, ad = m.groups()
            salida.append(f"| {nombre} | {cod} | {aa} | {av} | {zona} | {ae} | {ad} |")
            total += 1
        elif RE_DEP.match(texto) and len(texto) < 80 and "Código" not in texto:
            actual = re.sub(r"\s+", " ", texto).strip()
            salida += ["", f"**{actual}**", "", ENCABEZADO]
    cuerpo = "\n".join(salida).strip()
    titulo = "# A-4 — VALORES DE $A_{a}$, $A_{v}$, $A_{e}$ Y $A_{d}$ Y DEFINICIÓN DE LA ZONA DE AMENAZA SÍSMICA DE LOS MUNICIPIOS COLOMBIANOS"
    return f"{titulo}\n\n{cuerpo}\n", total


if __name__ == "__main__":
    md, n = construir(sys.argv[1])
    open(sys.argv[2], "w", encoding="utf-8", newline="\n").write(md)
    print(f"municipios: {n}")
