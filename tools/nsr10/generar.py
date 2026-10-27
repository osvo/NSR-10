"""Genera la NSR-10 en Markdown, consolidada con sus decretos modificatorios.

Uso:
    uv run --with pymupdf --with fonttools python tools/nsr10/generar.py <carpeta_fuentes>

<carpeta_fuentes> contiene los PDF del fork de la NSR-10 (FORK-DOC-006 = Título A, 008 = B, 014 = C)
y los anexos de los decretos citados en tools/nsr10/modificaciones/.

Pasos:
1. extraer.py convierte cada título del PDF oficial (texto, tablas, ecuaciones en LaTeX o recorte).
2. apendice_a4.py reconstruye la tabla de municipios desde la geometría del PDF.
3. consolidar.py aplica, en orden cronológico, las modificaciones de los decretos y actualiza
   panel/src/nsr10/municipios.js.
"""
import glob
import os
import shutil
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", ".."))
sys.path.insert(0, AQUI)

import apendice_a4  # noqa: E402
import consolidar  # noqa: E402
import extraer  # noqa: E402

TITULOS = {"A": "FORK-DOC-006.pdf", "B": "FORK-DOC-008.pdf", "C": "FORK-DOC-014.pdf"}


def aplicar_correcciones(destino):
    """Correcciones literales verificadas contra el PDF (fracciones y llaves dentro del texto)."""
    import json
    faltan = 0
    for c in json.load(open(os.path.join(AQUI, "correcciones.json"), encoding="utf-8")):
        ruta = os.path.join(destino, c["archivo"])
        texto = open(ruta, encoding="utf-8").read()
        if c["buscar"] not in texto:
            print(f"  corrección sin aplicar ({c['archivo']}, {c['pagina']}): {c['buscar'][:60]}")
            faltan += 1
            continue
        texto = texto.replace(c["buscar"], c["reemplazar"], -1 if c.get("todas") else 1)
        open(ruta, "w", encoding="utf-8", newline="\n").write(texto)
    print(f"Correcciones: {faltan} sin aplicar")


PYMUPDF = "1.28.2"   # la extracción depende de la versión: con 2.0 cambian texto, trazos y tablas


def main(fuentes):
    import pymupdf
    if pymupdf.__version__ != PYMUPDF:
        sys.exit(f"Se requiere PyMuPDF {PYMUPDF} (instalado: {pymupdf.__version__}): "
                 f"uv run --with pymupdf=={PYMUPDF} --with fonttools python tools/nsr10/generar.py <fuentes>")
    destino = os.path.join(RAIZ, "normativa", "nsr10")
    for letra, pdf in TITULOS.items():
        carpeta = os.path.join(destino, f"titulo-{letra.lower()}")
        # Se parte de cero para que la consolidación no se aplique dos veces.
        for nombre in os.listdir(carpeta) if os.path.isdir(carpeta) else []:
            ruta = os.path.join(carpeta, nombre)
            if nombre.endswith(".md"):
                os.remove(ruta)
            elif nombre == "img":
                shutil.rmtree(ruta)
        print(f"Título {letra}: extrayendo")
        extraer.procesar(os.path.join(fuentes, pdf), letra, carpeta)
    # Apéndices transcritos a mano (tablas de ecuaciones que no se pueden extraer celda por celda).
    for ruta in sorted(glob.glob(os.path.join(AQUI, "apendices", "*.md"))):
        nombre = os.path.basename(ruta)
        letra = nombre[0].lower()
        shutil.copyfile(ruta, os.path.join(destino, f"titulo-{letra}", nombre))
        print(f"Apéndice transcrito: {nombre}")
    aplicar_correcciones(destino)
    md, n = apendice_a4.construir(os.path.join(fuentes, TITULOS["A"]))
    open(os.path.join(destino, "titulo-a", "A-4.md"), "w", encoding="utf-8", newline="\n").write(md)
    print(f"Apéndice A-4: {n} municipios")
    pendientes = consolidar.consolidar(destino, fuentes)
    consolidar.exportar_municipios(destino, os.path.join(RAIZ, "panel", "src", "nsr10", "municipios.js"))
    # Los apéndices transcritos, las correcciones y la consolidación reemplazan texto que aún citaba
    # recortes de ecuaciones: se limpian al final, cuando el Markdown ya es el definitivo.
    for letra in TITULOS:
        extraer.limpiar_imagenes(os.path.join(destino, f"titulo-{letra.lower()}"))
    return 1 if pendientes else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
