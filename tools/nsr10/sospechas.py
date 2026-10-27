"""Señales objetivas de una transcripción automática dudosa (ecuacion_2d), para revisarla a mano.

No decide que una transcripción es correcta: la que no tiene señales igual se compara contra el
recorte del PDF (verificar.py). Sirve para ordenar la revisión.
"""
import re


def _scripts(latex):
    """Contenido de cada _{…} y ^{…} (con llaves anidadas)."""
    out = []
    for m in re.finditer(r"[_^]\{", latex):
        i, prof = m.end(), 1
        while i < len(latex) and prof:
            prof += {"{": 1, "}": -1}.get(latex[i], 0)
            i += 1
        out.append(latex[m.end():i - 1])
    return out


def sospechas(cand):
    latex = cand["latex"]
    s = []
    if not latex.strip():
        s.append("vacía")
    if not cand.get("completo", True) or cand.get("avisos"):
        s.append("glifos sin usar o avisos")
    if r"\text" in latex:
        s.append("texto dentro de la fórmula")
    for sc in _scripts(latex):
        if re.search(r"=|\\le|\\ge|<|>|\\text", sc):
            s.append("script con relación o texto")
            break
        if re.search(r"\d\.$|^\.\d", sc):
            s.append("número partido en un script")
            break
    if re.search(r"=\s*=|=\s*$|^\s*=", latex):
        s.append("igualdad mal formada")
    if re.search(r"[_^]\{[^{}]*\}[_^]\{[^{}]*\}[_^]", latex):
        s.append("scripts encadenados")
    if latex.count(r"\left") != latex.count(r"\right"):
        s.append("delimitadores desbalanceados")
    if re.search(r"\(F\.\d", latex):
        s.append("número de ecuación dentro")
    return s
