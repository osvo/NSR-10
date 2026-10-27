"""Auditoria del corpus NSR-10 en Markdown.

Uso: python tools/nsr10/auditar.py normativa/nsr10

Informa, por archivo:
- Tablas citadas con titulo ("Tabla X") que no tienen una tabla Markdown a continuacion.
- Caracteres sospechosos: uso privado, reemplazo, controles y glifos sin mapear dentro de $...$.
- Formulas en linea con signos de mala extraccion (subindice al inicio, corchetes partidos).
"""
import os
import re
import sys
import unicodedata

RE_TITULO_TABLA = re.compile(r"^(?:\*\*)?Tabla\s+([A-K][.-][\dA-Z.]+-?\d*[a-z]?(?:\([a-z]\))?)", re.I)
RE_MATE = re.compile(r"(?<!\$)\$([^$\n]+)\$(?!\$)")
PERMITIDOS = set(" _{}^\\.,()=+-/<>'[]:;|%·×′−≤≥αβγδεζηθικλμνξπρστυφχψωΓΔΘΛΞΠΣΦΨΩℓ∑√∞≈≠±∂*")  # * de F_b^{*} y M^{*}_{pc}


def auditar(raiz):
    total = {"tablas_sin_cuerpo": 0, "raros": 0, "formulas_dudosas": 0}
    for dirpath, _, archivos in os.walk(raiz):
        for nombre in sorted(archivos):
            if not nombre.endswith(".md") or nombre == "README.md":
                continue
            ruta = os.path.join(dirpath, nombre)
            lineas = open(ruta, encoding="utf-8").read().split("\n")
            hallazgos = []
            for i, l in enumerate(lineas):
                m = RE_TITULO_TABLA.match(l.strip())
                if m and len(l) < 260:
                    siguiente = "\n".join(lineas[i + 1:i + 6])
                    if "|---" not in siguiente and "![" not in siguiente:
                        hallazgos.append(f"  L{i + 1} tabla sin cuerpo: {l.strip()[:90]}")
                        total["tablas_sin_cuerpo"] += 1
                for ch in l:
                    cat = unicodedata.category(ch)
                    if cat in ("Co", "Cc", "Cs") and ch not in "\t" or ch == "�":
                        hallazgos.append(f"  L{i + 1} caracter raro {hex(ord(ch))}: {l.strip()[:90]}")
                        total["raros"] += 1
                        break
                for f in RE_MATE.findall(l):
                    malos = [c for c in f if not (c.isalnum() or c in PERMITIDOS)]
                    llaves = set("⎛⎜⎝⎞⎟⎠⎡⎢⎣⎤⎥⎦")
                    if malos or f.startswith(("_", "^")) or "_{" in f[:2] or llaves & set(f)                             or re.search(r"\d\.?\d*[A-Za-z]\d", f):
                        hallazgos.append(f"  L{i + 1} formula dudosa ${f}$ {''.join(sorted(set(malos)))}")
                        total["formulas_dudosas"] += 1
            if hallazgos:
                print(ruta.replace(raiz, "").lstrip("\\/"))
                print("\n".join(hallazgos[:40]))
                if len(hallazgos) > 40:
                    print(f"  ... {len(hallazgos) - 40} mas")
    print("TOTAL", total)


if __name__ == "__main__":
    auditar(sys.argv[1])
