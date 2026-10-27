"""Reconstrucción en LaTeX de una ecuación de presentación a partir de su geometría en el PDF.

Las ecuaciones de MathType del PDF oficial traen glifos con posición y tamaño, más trazos
vectoriales: barras horizontales de fracción, radicales y barras «/». Este módulo arma la
estructura bidimensional sin interpretar el contenido:

1. Átomos: un glifo por carácter (posición de rawdict), los trazos y las palabras de texto.
2. Estructuras de mayor a menor ancho (la exterior contiene a las interiores): fracción
   (numerador arriba y denominador abajo de la barra), radical (lo que cubre) y operadores
   grandes con límites (∑ con lo que tiene encima y debajo). Cada una se resuelve recursivamente.
3. Línea principal en orden de x: los glifos menores que la base (subíndices y superíndices)
   se pegan al átomo anterior según su altura; las piezas de delimitador (⎡⎢⎣) se unen.

Devuelve también los átomos que no se usaron: si queda alguno, la transcripción no es confiable y
la ecuación se revisa a mano. No se corrige ni se completa nada que no esté en el PDF.
"""
from __future__ import annotations

import re

GRIEGAS = {"α": "alpha", "β": "beta", "γ": "gamma", "δ": "delta", "ε": "varepsilon", "ζ": "zeta",
           "η": "eta", "θ": "theta", "ϑ": "vartheta", "ι": "iota", "κ": "kappa", "λ": "lambda", "μ": "mu",
           "ν": "nu", "ξ": "xi", "π": "pi", "ϖ": "varpi", "ρ": "rho", "σ": "sigma", "ς": "varsigma",
           "τ": "tau", "υ": "upsilon", "φ": "phi", "ϕ": "phi", "χ": "chi", "ψ": "psi", "ω": "omega",
           "Γ": "Gamma", "Δ": "Delta", "Θ": "Theta", "Λ": "Lambda", "Ξ": "Xi", "Π": "Pi", "Σ": "Sigma",
           "Φ": "Phi", "Ψ": "Psi", "Ω": "Omega"}
SIMBOLOS = {"≤": r"\le ", "≥": r"\ge ", "≠": r"\ne ", "≈": r"\approx ", "±": r"\pm ", "×": r"\times ",
            "⋅": r"\cdot ", "·": r"\cdot ", "•": r"\bullet ", "−": "-", "–": "-", "′": "'", "″": "''",
            "∞": r"\infty ", "→": r"\rightarrow ", "´": "'", "∂": r"\partial ", "∆": r"\Delta ", "Ω": r"\Omega ",
            "%": r"\%", "°": r"^{\circ}", "∼": r"\sim ", "≅": r"\cong ", "∗": "*", "{": r"\{", "}": r"\}",
            "‾": "", "ℓ": r"\ell ", "∑": r"\sum ", "∫": r"\int ", "√": r"\surd "}
OPERADORES = {"∑", "Σ", "∫"}
FUNCIONES = ("min", "máx", "max", "mín", "cos", "sin", "sen", "tan", "log", "ln", "exp")
PIEZAS = {"⎛": "(", "⎜": "(", "⎝": "(", "⎞": ")", "⎟": ")", "⎠": ")", "⎡": "[", "⎢": "[", "⎣": "[",
          "⎤": "]", "⎥": "]", "⎦": "]", "⎧": "{", "⎨": "{", "⎩": "{", "⎪": "{", "⎫": "}", "⎬": "}", "⎭": "}",
          "⎮": "|"}
APERTURA = {"(": "(", "[": "[", "{": r"\{", "|": "|"}
CIERRE = {")": ")", "]": "]", "}": r"\}", "|": "|"}


class Atomo:
    __slots__ = ("t", "x0", "y0", "x1", "y1", "tam", "tipo", "latex", "texto", "id")

    def __init__(self, t, caja, tam, tipo="g", latex=None, texto=False):
        self.t, self.tam, self.tipo, self.latex, self.texto = t, tam, tipo, latex, texto
        self.x0, self.y0, self.x1, self.y1 = caja

    @property
    def cx(self):
        return (self.x0 + self.x1) / 2

    @property
    def cy(self):
        return (self.y0 + self.y1) / 2


def _caracter(c):
    if c in GRIEGAS:
        return "\\" + GRIEGAS[c] + " "
    if c in "áéíóúÁÉÍÓÚñÑ":                     # letra con tilde de la fuente matemática
        return r"\text{" + c + "}"                # sin espacios: así se distingue de una palabra en Arial
    return SIMBOLOS.get(c, c)


def atomos_de(pagina_dict, caja, es_mate, excluir=None, zonas=None):
    """Átomos dentro de la caja: un glifo por carácter (con `_x0`) o una palabra de texto.

    zonas: cajas de las líneas miembro de la banda. Si se dan, solo entran los spans de esas
    líneas: el texto que cae en la caja sin ser de la ecuación queda en el párrafo y no se repite.
    """
    x0, y0, x1, y1 = caja
    out = []
    for b in pagina_dict["blocks"]:
        for l in b.get("lines", []):
            if zonas is not None and not any(abs(l["bbox"][0] - z[0]) < 0.6 and abs(l["bbox"][1] - z[1]) < 0.6
                                              and abs(l["bbox"][2] - z[2]) < 0.6 for z in zonas):
                continue
            for s in l["spans"]:
                sx0, sy0, sx1, sy1 = s["bbox"]
                cy = (sy0 + sy1) / 2
                if not s["text"].strip() or not (y0 - 1 <= cy <= y1 + 1 and x0 - 2 <= sx0 and sx1 <= x1 + 2):
                    continue
                if excluir and excluir(s):
                    continue
                if not es_mate(s) and s["font"] != "MTExtra-trazo":
                    # Texto en Arial dentro de la ecuación («para», «cuando»): una palabra por átomo.
                    for m in re.finditer(r"\S+", s["text"]):
                        frac = lambda k: sx0 + (sx1 - sx0) * k / max(len(s["text"]), 1)   # noqa: E731
                        out.append(Atomo(m.group(), (frac(m.start()), sy0, frac(m.end()), sy1), s["size"], texto=True))
                    continue
                xs = s.get("_x0")
                txt = s["text"]
                if not xs or len(xs) != len(txt):
                    n = len(txt)
                    xs = [sx0 + (sx1 - sx0) * k / n for k in range(n)]
                for k, ch in enumerate(txt):
                    if not ch.strip():
                        continue
                    xf = next((xs[j] for j in range(k + 1, len(txt)) if txt[j].strip()), sx1)
                    out.append(Atomo(ch, (xs[k], sy0, max(xf, xs[k] + 0.5), sy1), s["size"]))
    return out


def barras_fraccion(pagina, caja):
    """Segmentos horizontales finos dentro de la caja (barras de fracción)."""
    x0, y0, x1, y1 = caja
    out = []
    for g in pagina.get_drawings():
        r = g["rect"]
        if not (x0 - 3 <= r.x0 and r.x1 <= x1 + 3 and y0 - 2 <= r.y0 and r.y1 <= y1 + 2):
            continue
        items = g["items"]
        horiz = lambda it: it[0] == "l" and abs(it[1].y - it[2].y) < 0.4   # noqa: E731
        if items and all(horiz(it) for it in items):
            # Un mismo trazo puede traer varias barras (todas horizontales); el de un radical trae
            # también segmentos inclinados y se descarta aquí.
            for it in items:
                a, b = it[1], it[2]
                if abs(a.x - b.x) >= 4:
                    out.append((min(a.x, b.x), a.y, max(a.x, b.x)))
        elif len(items) == 1 and items[0][0] == "re" and r.height <= 1.2 and r.width >= 4:
            out.append((r.x0, (r.y0 + r.y1) / 2, r.x1))
    unicas = []
    for b in sorted(out):
        if not any(abs(b[0] - u[0]) < 1 and abs(b[1] - u[1]) < 1 and abs(b[2] - u[2]) < 1 for u in unicas):
            unicas.append(b)
    return unicas


def _unir_piezas(atomos):
    """Columnas de piezas de delimitador (⎡⎢⎣) -> un solo átomo delimitador alto."""
    piezas = [a for a in atomos if a.t in PIEZAS]
    resto = [a for a in atomos if a.t not in PIEZAS]
    grupos = []
    arriba, abajo = set("⎛⎡⎧⎞⎤⎫"), set("⎝⎣⎩⎠⎦⎭")
    # De arriba abajo (no por x redondeada: ⎛ en x = 91.6 y ⎝ en 91.4 caían en grupos distintos).
    for p in sorted(piezas, key=lambda a: a.y0):
        # Una pieza de arriba abre un delimitador nuevo y una de abajo lo cierra: dos paréntesis
        # alineados en x, uno sobre otro (numerador y denominador de F.3.6.5-4), no se funden.
        # «⎪» es la extensión de las dos llaves: se une a la llave de su x, sea { o } (ecuaciones
        # de la página 471, «{…}^{1/2}»).
        g = None if p.t in arriba else next(
            (g for g in grupos if (PIEZAS[g[0].t] == PIEZAS[p.t] or (p.t == "⎪" and PIEZAS[g[0].t] in "{}"))
             and abs(g[0].x0 - p.x0) < 1.5 and p.y0 <= g[-1].y1 + 2 and g[-1].t not in abajo), None)
        if g:
            g.append(p)
        else:
            grupos.append([p])
    for g in grupos:
        caja = (min(a.x0 for a in g), min(a.y0 for a in g), max(a.x1 for a in g), max(a.y1 for a in g))
        resto.append(Atomo(PIEZAS[g[0].t], caja, g[0].tam, tipo="delim"))
    return resto


def _tam_contenido(atomos):
    """Tamaño de una estructura (fracción, radical): el de su contenido sin delimitadores."""
    tams = [a.tam for a in atomos if a.t not in "()[]{}|" and a.t not in PIEZAS and a.tipo != "delim"]
    return max(tams or [a.tam for a in atomos])


def _tam_base(atomos):
    """Tamaño de la línea base: el mayor que reúne al menos el 25 % de los glifos (±8 %).

    No el máximo: unos paréntesis de 13 pt en una línea de 10 pt harían ver todo como subíndice.
    """
    # Sin delimitadores: dos paréntesis grandes en un grupo pequeño ((a⁄h)²) no son la línea base.
    tams = ([a.tam for a in atomos if a.tipo in ("g", "acc", "comp") and a.t not in "()[]{}|"]
            or [a.tam for a in atomos if a.tipo in ("g", "acc")] or [a.tam for a in atomos])
    # El mayor tamaño de los glifos que no son delimitadores ni operadores grandes: con los
    # paréntesis fuera, no hace falta exigir una proporción mínima (en t_p^{0.167} los scripts son
    # mayoría y la proporción elegía el tamaño de los scripts).
    # Sin las palabras de texto: «Cuando» (Arial 10) haría ver como subíndices los glifos de 9.1 pt.
    sin_op = [a.tam for a in atomos if a.tipo in ("g", "acc", "comp") and a.t not in "()[]{}|"
              and a.t not in OPERADORES and a.t != "op" and not a.texto]   # «op»: ∑/∫ con sus límites
    return max(sin_op or tams)


def _dentro_x(a, x0, x1):
    return x0 - 0.5 <= a.cx <= x1 + 0.5


class Reconstruccion:
    def __init__(self, atomos, barras, radicales):
        self.atomos = _unir_piezas(atomos)
        self.total = len(self.atomos)
        self.barras = list(barras)
        self.radicales = list(radicales)
        self.usados = 0
        self.avisos = []

    def latex(self):
        estructuras = ([("frac", b) for b in self.barras] + [("sqrt", r) for r in self.radicales])
        texto = self._nivel(self.atomos, estructuras)
        return re.sub(r"\s+", " ", texto).strip()

    # ---------------------------------------------------------------- un nivel
    def _nivel(self, atomos, estructuras):
        atomos = list(atomos)
        # Estructuras de mayor a menor ancho: la más ancha contiene a las demás de su zona.
        estructuras = sorted(estructuras, key=lambda e: -(e[1][2] - e[1][0]) if e[0] == "frac" else -(e[1][2] - e[1][0]))
        pendientes = list(estructuras)
        while pendientes:
            tipo, e = pendientes.pop(0)
            if tipo == "frac":
                bx0, by, bx1 = e
                arriba = [a for a in atomos if _dentro_x(a, bx0, bx1) and a.cy < by]
                abajo = [a for a in atomos if _dentro_x(a, bx0, bx1) and a.cy > by]
                # Solo lo pegado a la barra: se corta donde haya un hueco vertical grande.
                # Barras y radicales interiores (en el ancho de esta barra) unen las partes de un
                # numerador o denominador que tiene su propia fracción.
                puentes = [y for t2, e2 in pendientes if bx0 - 0.5 <= e2[0] and e2[2] <= bx1 + 0.5
                           for y in ((e2[1],) if t2 == "frac" else (e2[1], e2[3]))]
                arriba = self._contiguo(arriba, by, -1, puentes)
                abajo = self._contiguo(abajo, by, +1, puentes)
                # Barra corta sobre un solo glifo y nada encima: es una barra de acento (r̄_o).
                xm = (bx0 + bx1) / 2
                bajo = sorted((a for a in abajo if a.tipo == "g" and a.x0 - 1 <= xm <= a.x1 + 1), key=lambda a: -a.tam)
                if not arriba and bajo and bx1 - bx0 <= 1.6 * (bajo[0].x1 - bajo[0].x0) + 2:
                    a = bajo[0]
                    atomos.remove(a)
                    self.usados += 1
                    atomos.append(Atomo(a.t, (a.x0, by, a.x1, a.y1), a.tam, tipo="acc",
                                        latex=r"\bar{" + _caracter(a.t).strip() + "}"))
                    continue
                if not arriba or not abajo:
                    self.avisos.append(f"barra en y={by:.1f} sin numerador o denominador")
                    continue
                internas = [p for p in pendientes if self._contenida(p, bx0, bx1, min(a.y0 for a in arriba),
                                                                    max(a.y1 for a in abajo))]
                for p in internas:
                    pendientes.remove(p)
                num = self._nivel(arriba, [p for p in internas if self._lado(p, by) < 0])
                den = self._nivel(abajo, [p for p in internas if self._lado(p, by) > 0])
                for a in arriba + abajo:
                    atomos.remove(a)
                tam = _tam_contenido(arriba + abajo)
                caja = (bx0, min(a.y0 for a in arriba), bx1, max(a.y1 for a in abajo))
                atomos.append(Atomo("frac", caja, tam, tipo="comp", latex=rf"\dfrac{{{num}}}{{{den}}}"))
            else:
                rx0, ry0, rx1, ry1 = e
                dentro = [a for a in atomos if rx0 < a.cx < rx1 and ry0 - 2 <= a.cy <= ry1 + 2]
                if not dentro:
                    self.avisos.append(f"radical en x={rx0:.1f} vacío")
                    continue
                internas = [p for p in pendientes if self._contenida(p, rx0, rx1, ry0 - 2, ry1 + 2)]
                for p in internas:
                    pendientes.remove(p)
                # Índice de la raíz (⁴√ en F.4.2.1-1): glifo pequeño en la mitad superior, antes del
                # contenido de tamaño normal.
                tmax = _tam_contenido(dentro)
                normales = [a for a in dentro if a.tam >= 0.9 * tmax]
                x_cont = min((a.x0 for a in normales), default=rx1)
                indice = [a for a in dentro if a.tipo == "g" and a.tam < 0.85 * tmax and a.x1 <= x_cont + 0.5
                          and a.cy < (ry0 + ry1) / 2]
                cuerpo = self._nivel([a for a in dentro if a not in indice], internas)
                orden = f"[{self._linea(indice)}]" if indice else ""
                for a in dentro:
                    atomos.remove(a)
                atomos.append(Atomo("sqrt", (rx0, ry0, rx1, ry1), tmax, tipo="comp",
                                    latex=rf"\sqrt{orden}{{{cuerpo}}}"))
        atomos = self._operadores(atomos)
        return self._linea(atomos)

    @staticmethod
    def _contiguo(grupo, by, signo, puentes=()):
        """Átomos de un lado de la barra que forman su numerador (signo −1) o denominador (+1).

        Solo los glifos de tamaño normal deciden la contigüidad: hueco de 3 pt como máximo, salvo que
        lo cruce una barra o radical interior (`puentes`, alturas en y). Una línea vecina a 6 pt no es
        del numerador aunque el subíndice de una de sus letras cuelgue hasta él (F.2.6.5-4). Los
        scripts entran si se traslapan con lo ya aceptado.
        """
        if not grupo:
            return []
        maxt = max(a.tam for a in grupo)
        grandes = sorted((a for a in grupo if a.tam >= 0.85 * maxt or a.tipo != "g"), key=lambda a: abs(a.cy - by))
        if not grandes or abs((grandes[0].y1 if signo < 0 else grandes[0].y0) - by) > 8:
            return []
        # El primer glifo puede quedar a 8 pt de la barra (su caja incluye el descendente); desde él
        # rige el hueco de 3 pt.
        out = [grandes[0]]
        borde = grandes[0].y0 if signo < 0 else grandes[0].y1
        for a in grandes[1:]:
            # Las barras y radicales interiores entre el borde y el átomo cierran el hueco.
            for y in sorted(puentes, reverse=signo < 0):
                if (signo < 0 and borde - 3 <= y <= borde) or (signo > 0 and borde <= y <= borde + 3):
                    borde = y
            cerca = (a.y1 >= borde - 3) if signo < 0 else (a.y0 <= borde + 3)
            if not cerca:
                break
            out.append(a)
            borde = min(borde, a.y0) if signo < 0 else max(borde, a.y1)
        lim0, lim1 = (borde, by) if signo < 0 else (by, borde)
        out += [a for a in grupo if a not in out and a.tam < 0.85 * maxt and a.tipo == "g"
                and a.y1 > lim0 + 0.5 and a.y0 < lim1 - 0.5]
        return out

    @staticmethod
    def _contenida(p, x0, x1, y0, y1):
        tipo, e = p
        if tipo == "frac":
            return x0 - 0.5 <= e[0] and e[2] <= x1 + 0.5 and y0 - 1 <= e[1] <= y1 + 1
        return x0 - 0.5 <= e[0] and e[2] <= x1 + 0.5 and y0 - 2 <= (e[1] + e[3]) / 2 <= y1 + 2

    @staticmethod
    def _lado(p, by):
        tipo, e = p
        y = e[1] if tipo == "frac" else (e[1] + e[3]) / 2
        return -1 if y < by else 1

    def _operadores(self, atomos):
        """∑ y ∫ con límites encima y debajo (átomos menores centrados sobre el operador)."""
        for op in [a for a in atomos if a.t in OPERADORES and a.tipo == "g"]:
            # Un límite queda casi todo fuera de la altura del operador y centrado sobre él; el
            # integrando de ∫_A x³dA está a la derecha y a media altura, y no es límite (F.4.3.3-19).
            h = op.y1 - op.y0
            arriba = [a for a in atomos if a is not op and a.tipo == "g" and a.tam < op.tam * 0.85
                      and op.x0 - 2 <= a.cx <= op.x1 + 1 and a.y1 <= op.y0 + 0.4 * h]
            abajo = [a for a in atomos if a is not op and a.tipo == "g" and a.tam < op.tam * 0.85
                     and op.x0 - 2 <= a.cx <= op.x1 + 1 and a.y0 >= op.y1 - 0.4 * h]
            if not arriba and not abajo:
                continue
            # El límite sigue a la derecha del operador («i=1» bajo un ∑ estrecho): se añaden los
            # glifos pequeños contiguos en la misma franja vertical.
            for lim in (arriba, abajo):
                cambio = bool(lim)
                while cambio:
                    cambio = False
                    y_lo, y_hi, x_fin = min(a.cy for a in lim) - 2, max(a.cy for a in lim) + 2, max(a.x1 for a in lim)
                    for a in atomos:
                        if a is not op and a not in arriba and a not in abajo and a.tipo == "g" \
                                and a.tam < op.tam * 0.85 and y_lo <= a.cy <= y_hi and x_fin - 0.5 <= a.x0 <= x_fin + 1.5:
                            lim.append(a)
                            cambio = True
            ltx = r"\sum" if op.t in "∑Σ" else r"\int"
            if abajo:
                ltx += "_{" + self._linea(abajo) + "}"
            if arriba:
                ltx += "^{" + self._linea(arriba) + "}"
            self.usados += 1                                   # el operador; los límites cuentan en _linea
            for a in arriba + abajo + [op]:
                atomos.remove(a)
            caja = (min(a.x0 for a in arriba + abajo + [op]), min(a.y0 for a in arriba + abajo + [op]),
                    max(a.x1 for a in arriba + abajo + [op]), max(a.y1 for a in arriba + abajo + [op]))
            atomos.append(Atomo("op", caja, op.tam, tipo="comp", latex=ltx + " "))
        return atomos

    # ---------------------------------------------------------------- línea principal
    def _linea(self, atomos):
        """Una o varias filas: las filas se apilan con gathered (p. ej. «P_nc = A_e F_n» y «φ_c = 0.85»)."""
        if not atomos:
            return ""
        base = _tam_base(atomos)
        # Las filas se forman solo con glifos de tamaño normal: un corchete alto o una fracción
        # se traslapan con la fila vecina (F.2.3.2-2b) y las fundirían.
        grandes = sorted((a for a in atomos if a.tipo == "g" and a.tam >= 0.92 * base), key=lambda a: a.y0)
        altos = [a for a in atomos if a.tipo != "g"]
        filas = []
        for a in grandes:
            # Va a la fila con la que se traslapa en vertical (al menos 30 % del menor alto).
            f = next((f for f in filas if min(f[1], a.y1) - max(f[0], a.y0) > 0.3 * min(f[1] - f[0], a.y1 - a.y0)), None)
            if f:
                f[0], f[1] = min(f[0], a.y0), max(f[1], a.y1)
                f[2].append(a)
            else:
                filas.append([a.y0, a.y1, [a]])
        if len(filas) <= 1:
            return self._fila(atomos, base)
        for a in altos:
            # Delimitadores, fracciones y radicales: a la fila cuyo centro está más cerca del suyo.
            min(filas, key=lambda f: abs((f[0] + f[1]) / 2 - a.cy))[2].append(a)
        for a in atomos:
            if a.tipo == "g" and a.tam < 0.92 * base:
                # Cada script va con la fila cuyo átomo más cercano lo tiene a su derecha.
                f = min(filas, key=lambda f: min(abs(a.cy - b.cy) + 0.2 * max(a.x0 - b.x1, 0) + (50 if b.x0 > a.x0 else 0)
                                                 for b in f[2]))
                f[2].append(a)
        filas.sort(key=lambda f: f[0])
        return r"\begin{gathered}" + r" \\ ".join(self._fila(f[2], base) for f in filas) + r"\end{gathered}"

    def _fila(self, atomos, base):
        # Una barra «/» inclinada empieza a la izquierda de su centro: se ordena por el centro
        # (si no, en h_c/t_w queda antes del subíndice c).
        atomos = sorted(atomos, key=lambda a: (a.cx if a.t == "/" else a.x0, a.y0))
        nodos = []          # [átomo base, primas, [sub], [sup]]
        for a in atomos:
            b = nodos[-1][0] if nodos else None
            # La prima va con su base aunque quede entre la base y su subíndice: F′_nt → F'_{nt}
            # (si no, el subíndice se parte en dos y KaTeX rechaza «F_{n}'_{t}»).
            # Tilde sobre la letra anterior (k̃_φfg de F.4.3.3-37): el PDF la trae como el carácter
            # de control 0x04 de la fuente de símbolos, sin decodificar.
            if a.tipo == "g" and a.t in "\x04˜" and b is not None and b.tipo == "g" and not b.texto:
                b.tipo, b.latex = "acc", r"\tilde{" + _caracter(b.t).strip() + "}"
                self.usados += 2
                continue
            if a.tipo == "g" and a.t in "′'" and b is not None and b.tipo in ("g", "acc") and not b.texto \
                    and a.x0 - max([b.x1] + [g.x1 for g in nodos[-1][2] + nodos[-1][3]]) < 3:
                nodos[-1][1] = (nodos[-1][1] or "") + "'"
                self.usados += 1
                continue
            # Script: menor que la base de la línea y desplazado en vertical respecto al átomo anterior.
            # Dentro de un exponente la razón es ~0.85 (6.9 → 5.9 pt) y hay subíndices de 8.9 en 9.9 pt
            # (0.899, F.4.3.4-20): por eso el 0.92.
            es_script = (a.tipo == "g" and not a.texto and b is not None and a.tam < 0.92 * base
                         and abs(a.cy - b.cy) > 0.1 * (b.y1 - b.y0))
            if es_script:
                # Superíndice si su centro está claramente por encima del centro de la base.
                alto = (b.y1 - b.y0)
                sup = a.cy < b.cy - 0.12 * alto
                # Scripts encadenados (subíndice de varias letras) siguen al mismo nodo.
                (nodos[-1][3] if sup else nodos[-1][2]).append(a)
                continue
            nodos.append([a, None, [], []])
        partes = []
        x_prev = None
        for a, primas, sub, sup in nodos:
            # Hueco grande en la misma fila: dos expresiones lado a lado (ecuación y su φ).
            if x_prev is not None and a.x0 - x_prev > 2.5 * base:
                partes.append(r"\qquad ")
            x_prev = max([a.x1] + [g.x1 for g in sub + sup])
            self.usados += 1 if a.tipo in ("g", "delim") else 0   # comp y acc ya contaron lo suyo
            if a.tipo in ("comp", "acc"):
                t = a.latex
            elif a.tipo == "delim":
                t = (r"\left" + APERTURA[a.t]) if a.t in "([{" or (a.t == "|" and not self._abierto(partes)) else (r"\right" + CIERRE[a.t])
            elif a.texto and re.fullmatch(r"[=<>≤≥+−-]", a.t):
                t = _caracter(a.t)                     # «=» en Arial que continúa una definición
            elif a.texto:
                t = rf"\text{{ {a.t} }}"
            else:
                t = _caracter(a.t)
            t += primas or ""
            for grupo, marca in ((sub, "_"), (sup, "^")):
                if grupo:
                    # El script es una línea propia: puede traer sus propios subíndices (F_y/F_e).
                    t += marca + "{" + self._linea(grupo) + "}"
            partes.append(t)
        out = "".join(partes)
        # Palabra con tilde en un subíndice («flexión»): una sola palabra en \text{…}, no «flexi ó n».
        # Solo la letra de la fuente matemática (\text{ó} sin espacios): la conjunción «ó» en Arial
        # viene como \text{ ó } y no se pega a sus vecinos («0.8A ó 0.8A_e»).
        out = re.sub(r"(?<![\\A-Za-z])([A-Za-z]+)\\text\{([áéíóúñÁÉÍÓÚÑ])\}([a-z]*)",
                     lambda m: r"\text{" + m.group(1) + m.group(2) + m.group(3) + "}", out)
        # Letra con tilde suelta de la fuente matemática («0.9 ó 1.2»): con espacios a los lados.
        out = re.sub(r"\\text\{([áéíóúñÁÉÍÓÚÑ])\}", lambda m: r"\text{ " + m.group(1) + " }", out)
        # Palabras seguidas: un solo \text{…} («cuando el alma está a tensión»).
        out = re.sub(r"\\text\{ ([^{}]*?) \}(?:\\text\{ ([^{}]*?) \})+",
                     lambda m: r"\text{ " + " ".join(re.findall(r"\\text\{ ([^{}]*?) \}", m.group(0))) + " }", out)
        # Nombres de función solo fuera de \text{…}: «sin platina de enchape» no es \sin (F.5.5.4-1).
        trozos = re.split(r"(\\text\{[^{}]*\})", out)
        for i in range(0, len(trozos), 2):
            for f in FUNCIONES:
                rep = {"máx": r"\text{máx}", "mín": r"\text{mín}", "sen": r"\operatorname{sen}"}.get(f, "\\" + f + " ")
                trozos[i] = re.sub(rf"(?<![A-Za-z\\]){f}(?![a-z])", lambda _m, r=rep: r, trozos[i])
        return "".join(trozos)

    @staticmethod
    def _abierto(partes):
        return sum(p.count(r"\left") for p in partes) > sum(p.count(r"\right") for p in partes)

    def completo(self):
        """True si cada átomo se usó una vez (los compuestos no cuentan)."""
        return self.usados == self.total
