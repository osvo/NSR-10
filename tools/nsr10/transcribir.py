"""Transcribe a LaTeX las ecuaciones recortadas de un título (candidatas para ecuaciones/<letra>.json).

Uso:
    uv run --with pymupdf==1.28.2 --with fonttools python tools/nsr10/transcribir.py <pdf> <letra> <salida.json>

Corre la extracción en una carpeta temporal para conocer cada banda de ecuación con el mismo nombre
que usa el Markdown (número de la ecuación o «img:ec-p<página>-<y>») y la reconstruye con
ecuacion_2d. La salida lleva, por ecuación, el LaTeX, si se usaron todos los glifos y los avisos.
Las candidatas no se publican sin verificarlas contra el PDF (verificar.py arma las láminas).
"""
import json
import re
import os
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import pymupdf  # noqa: E402

import ecuacion_2d as E2  # noqa: E402
import extraer  # noqa: E402


def _es_tag(s):
    # El número de la ecuación suele ir en Arial, pero a veces en la fuente matemática (F.2.6.6-4).
    return extraer.RE_TAG.match(s["text"].strip())


def trazos_sueltos(pagina, caja):
    """Segmentos sueltos (sin extremos compartidos) de los trazos dentro de la caja.

    MathType junta en un mismo trazo piezas de distinta clase: tres barras de fracción con las dos
    barras de valor absoluto (F.2.8.2-1) o la barra de D/t con la «/» del exponente 5/4
    (F.2.7.6-2a). Cada segmento se clasifica por sí mismo:
    - horizontal: barra de fracción;
    - vertical de 8 pt o más: barra «|»;
    - inclinado de 5 a 40 pt, subiendo a la derecha: barra «/» (incluye las de 18 a 40 pt de las
      celdas de tabla y las «⁄» más tendidas, dx/dy ≈ 0.7, que trazos_mate no toma).
    Devuelve (horizontales, verticales, inclinadas, cajas de los trazos sueltos). Un radical tiene
    sus segmentos encadenados y no entra aquí.
    """
    x0, y0, x1, y1 = caja
    hor, ver, inc, cajas = [], [], [], []
    for g in pagina.get_drawings():
        items = g["items"]
        if g.get("type") != "s" or not items or len(items) > 8 or any(it[0] != "l" for it in items):
            continue
        puntos = [(round(p.x, 1), round(p.y, 1)) for it in items for p in it[1:3]]
        if len(set(puntos)) < len(puntos):            # segmentos encadenados: radical u otra figura
            continue
        r = g["rect"]
        if not (x0 - 6 <= r.x1 and r.x0 <= x1 + 6 and y0 - 6 <= r.y1 and r.y0 <= y1 + 6):
            continue
        cajas.append((r.x0, r.y0, r.x1, r.y1))
        for it in items:
            a, b = it[1], it[2]
            dx, dy = abs(a.x - b.x), abs(a.y - b.y)
            bajo, alto = (a, b) if a.y > b.y else (b, a)
            bx0, by0, bx1, by1 = min(a.x, b.x), min(a.y, b.y), max(a.x, b.x), max(a.y, b.y)
            if not (x0 - 3 <= bx0 and bx1 <= x1 + 3 and y0 - 6 <= by0 and by1 <= y1 + 6):
                continue
            if dy < 0.4 and dx >= 4:
                hor.append((bx0, a.y, bx1))
            elif dx < 0.5 and dy >= 8:
                ver.append((bx0, by0, bx1 + 0.5, by1))
            elif 5 <= dy <= 40 and 0.12 * dy <= dx <= 0.9 * dy and alto.x > bajo.x:
                inc.append((bx0, by0, bx1, by1))
    return hor, ver, inc, cajas


def transcribir_banda(pagina, caja, zonas=None):
    d = extraer.anotar_glifos(pagina, extraer.normalizar_glifos(pagina, pagina.get_text("dict")))
    atomos = E2.atomos_de(d, caja, extraer.es_mate, excluir=_es_tag, zonas=zonas)
    x0, y0, x1, y1 = caja

    def en_zonas(r):
        """Con líneas miembro, un trazo cuenta solo si toca alguna (la «/» de una condición que quedó
        en el párrafo no entra: F.2.15.2-6b)."""
        if not zonas:
            return True
        rx0, ry0, rx1, ry1 = r if len(r) == 4 else (r[0], r[1], r[2], r[1])
        return any(rx0 <= z[2] + 4 and rx1 >= z[0] - 4 and ry0 <= z[3] + 4 and ry1 >= z[1] - 4 for z in zonas)

    radicales, barras = extraer.trazos_mate(pagina, alto_max=90)   # radicales de ecuaciones altas (F.2.6.2-6)
    radicales = [r for r in radicales if en_zonas(r)]
    barras = [b for b in barras if en_zonas(b)]
    # La barra superior de un radical sobresale del texto de la banda (3.4 pt en F.2.6.2-6).
    dentro = lambda r: x0 - 3 <= r[0] and r[2] <= x1 + 3 and y0 - 6 <= r[1] and r[3] <= y1 + 6   # noqa: E731
    hor, ver, inc, cajas_sueltas = trazos_sueltos(pagina, caja)
    hor, ver, inc = [h for h in hor if en_zonas(h)], [v for v in ver if en_zonas(v)], [i for i in inc if en_zonas(i)]
    todas = list(barras)
    for b in inc:                                   # sin repetir las que ya dio trazos_mate
        if not any(abs(b[0] - o[0]) < 1 and abs(b[1] - o[1]) < 1 and abs(b[3] - o[3]) < 1 for o in todas):
            todas.append(b)
    # Un «radical» que coincide con un trazo de segmentos sueltos es un |…| con barras (F.2.8.2-1).
    radicales = [r for r in radicales if not any(abs(r[0] - c[0]) < 1.5 and abs(r[1] - c[1]) < 1.5 and abs(r[3] - c[3]) < 1.5
                                                 for c in cajas_sueltas)]
    for v in ver:
        atomos.append(E2.Atomo("⎮", v, max((a.tam for a in atomos), default=10)))   # se une como delimitador «|»
    for b in filter(dentro, todas):
        # La barra toma el mayor tamaño de los glifos que tiene a los lados (en su franja vertical):
        # en un exponente, el del exponente; en h_c/t_w, el de h y t (no el del subíndice c).
        ancho = b[2] - b[0] + 6
        vecinos = [a for a in atomos if b[1] - 2 <= a.cy <= b[3] + 2 and b[0] - ancho <= a.cx <= b[2] + ancho
                   and a.t not in "()[]{}|" and a.t not in E2.PIEZAS]          # no los paréntesis de (a⁄h)
        atomos.append(E2.Atomo("/", b, max((a.tam for a in vecinos), default=10)))
    fracciones = [f for f in E2.barras_fraccion(pagina, caja) if en_zonas(f)]
    for h in hor:                                   # barras de trazos mixtos (con «|» o «/»)
        if not any(abs(h[0] - o[0]) < 1 and abs(h[1] - o[1]) < 1 and abs(h[2] - o[2]) < 1 for o in fracciones):
            fracciones.append(h)
    # El gancho de un radical sobresale a la izquierda del texto (6 pt en F.4.3.3-13).
    dentro_rad = lambda r: x0 - 10 <= r[0] and r[2] <= x1 + 3 and y0 - 6 <= r[1] and r[3] <= y1 + 6   # noqa: E731
    rec = E2.Reconstruccion(atomos, fracciones, [r for r in radicales if dentro_rad(r)])
    latex = rec.latex()
    # El número de la ecuación partido en varios spans (F.2.10.10-5b) no lo excluye _es_tag.
    latex = re.sub(r"\s*\(\s*F\.[\d.]+\s*-\s*\d+[a-z]?\s*\)\s*$", "", latex)
    latex = re.sub(r"\s*(\\qquad\s*)?\\text\{\s*\(\s*F\.[\d.]+-\d+[a-z]?\)\s*\}\s*$", "", latex)
    return latex, rec.completo(), rec.avisos


def main(pdf, letra, salida):
    extraer.REGISTRO_BANDAS.clear()
    with tempfile.TemporaryDirectory() as tmp:
        extraer.procesar(pdf, letra, tmp)
    doc = pymupdf.open(pdf)
    out = {}
    for np_, caja, archivo, zonas in extraer.REGISTRO_BANDAS:
        nombre = os.path.splitext(archivo)[0]
        tag = nombre[3:] if extraer.RE_TAG.match(f"({nombre[3:]})") else None
        clave = tag if tag else f"img:{nombre}"
        try:
            latex, completo, avisos = transcribir_banda(doc[np_], caja, zonas or None)
        except Exception as exc:                       # una banda rara no detiene las demás
            latex, completo, avisos = "", False, [f"error: {exc}"]
        out[clave] = {"latex": latex, "completo": completo, "avisos": avisos, "pagina": np_ + 1,
                      "archivo": archivo, "bbox": [round(v, 1) for v in caja]}
    json.dump(out, open(salida, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    n_ok = sum(v["completo"] and not v["avisos"] for v in out.values())
    print(f"{len(out)} ecuaciones; {n_ok} con todos los glifos y sin avisos")


if __name__ == "__main__":
    main(*sys.argv[1:4])
