# C-G — Procedimiento alterno de diseño a la flexion por el método de esfuerzos admisibles

## C-G.0 — NOMENCLATURA

$A_{s}$ = área del refuerzo, no preesforzado, que trabaja a tracción, expresada en mm².

$A_{s}φ$ = área del refuerzo a compresión, expresada en mm².

$b$ = ancho de la cara a compresión del elemento, en mm.

$d$ = distancia de la fibra extrema en compresión al centroide del acero de refuerzo en tracción, en mm.

$dφ$ = distancia de la fibra extrema en compresión al centroide del acero de refuerzo en compresión, en mm.

$E_{c}$ = módulo de elasticidad del concreto, expresado en MPa (véase C.8.5.4).

$E_{s}$ = módulo de elasticidad del refuerzo, expresado en MPa (véase C.8.5.5).

$f_{c}$ = esfuerzo de compresión en la fibra extrema en compresión del concreto, expresado en MPa.

$f_{c}φ$ = resistencia nominal del concreto a la compresión, expresada en MPa.

$f_{s}$ = esfuerzo de tracción en el acero de refuerzo, expresado en MPa.

$f_{s}φ$ = esfuerzo de compresión en el acero de refuerzo en compresión, expresado en MPa

$f_{y}$ = resistencia nominal a la fluencia en el acero de refuerzo, expresada en MPa.

$n$ = relación modular de elasticidad.

$= E_{s}/E_{c}$

$φ$ = coeficiente de reducción de resistencia (véase C.9.3).

$ρ$ = cuantía del refuerzo no preesforzado en tracción $(=A_{s}/bd)$.

$ρφ$ = cuantía del refuerzo a compresión, $(=A_{s}φ/bd)$.

## C-G.1 — ALCANCE

**C-G.1.1** — Los elementos de concreto no preesforzado se pueden diseñar a la flexión utilizando cargas de servicio (sin factores de carga) y esfuerzos admisibles bajo cargas de servicio de acuerdo con las disposiciones del presente apéndice.

C-G.1.2. - Para el diseño de los elementos que no se incluyen en el apéndice C-G, deben aplicarse las disposiciones apropiadas del Título C del Reglamento.

**C-G.1.3** — Todas las disposiciones aplicables del Reglamento para concreto no preesforzado, excepto C.8.5.12, deben aplicarse a los elementos diseñados por el presente método alterno de diseño.

**C-G.1.4** — Los elementos sometidos a flexión deben cumplir con los requisitos para control de deflexiones de C.9.5 y los requisitos C.10.4 a C.10.7 de este Reglamento.

## C-G.2 — DEFINICIONES

**C-G.2.1** — Los factores de carga y los coeficientes de reducción de resistencia, $φ$ , deben tomarse como la unidad para elementos diseñados por el presente método alterno de diseño. (Véase B.2.3)

**C-G.2.2** — Los elementos pueden dimensionarse para el 75% de la capacidad requerida en otras partes del apéndice C-G, cuando se consideran fuerzas de viento o sísmicas combinadas con otras cargas, siempre y cuando la sección que resulte no sea menor que la requerida para la combinación de carga viva y muerta. (véase B.2.3)

**C-G.2.3** — Cuando la carga muerta reduce los efectos de otras cargas, los elementos deben diseñarse para el 85% de la carga muerta en combinación con las demás cargas. (Véase B.2.3)

## C-G.3 — ESFUERZOS ADMISIBLES BAJO CARGAS DE SERVICIO

**C-G.3.1** — El esfuerzo en el concreto, $f_{c}$, en la fibra extrema en compresión, no debe exceder de $0.45f_{c}'$ , expresado en MPa.

### C-G.3.2 — El esfuerzo de tracción en el refuerzo $f_{s}$ no debe exceder de:

Acero de refuerzo con $f_{y}≤240$ MPa ................................................................................ 120 MPa Acero de refuerzo con $f_{y}≥420$ MPa y malla de alambre electrosoldada (liso o corrugado) ...................................................................................... 170 MPa Para acero de refuerzo colocado para flexión de diámetro Nº 3 (3/8”) ó 10M (10 mm) o menor, en losas en una dirección de luz inferior a 3.50 metros, no debe exceder .................................................... $0.50f_{y}$ o 210 MPa

## C-G.4 — FLEXIÓN

Para la investigación de esfuerzos ante cargas de servicio, debe utilizarse la teoría de la elástica (para flexión) con las siguientes suposiciones:

**C-G.4.1** — Las deformaciones varían linealmente con la distancia medida desde el eje neutro, excepto para elementos de gran altura sometidos a flexión con relaciones de altura total a la luz libre mayores de 2/5 para luces continuas y 4/5 para luces simples, en las cuales debe considerarse una distribución no lineal de deformación unitaria. (véase C.10.7).

**C-G.4.2** — La relación esfuerzo-deformación del concreto, es una línea recta bajo cargas de servicio dentro del rango de esfuerzos admisibles.

### C-G.4.3 — En elementos de concreto reforzado, el concreto no resiste tracción.

**C-G.4.4** — La relación modular $n=E_{s}/E_{c}$ se puede tomar como el número entero más cercano (pero no menor de 6). Excepto en el cálculo de las deflexiones, el valor de $n$ para concreto ligero debe considerarse igual que para concreto de peso normal de la misma resistencia.

**C-G.4.5** — En elementos doblemente reforzados sometidos a flexión, debe utilizarse una relación modular efectiva de $2E_{s}/E_{c}$ para transformar el refuerzo de compresión en el cálculo de esfuerzos. El esfuerzo de compresión en dicho refuerzo no debe exceder del esfuerzo de tracción permisible.

**C-G.4.6** — Los requisitos anteriores pueden considerarse satisfechos cuando los esfuerzos en los materiales se determinan por medio de las siguientes ecuaciones:

Esfuerzos en el acero de refuerzo en tracción:

$f_{s}=A_{s}M jd≤( f_{s} )admisible$(C-G-1) Esfuerzos en el acero de refuerzo en compresión:

$d'$ $k−$

$f_{s}' =2f_{s}1−kd≤( f_{s} )admisible$(C-G-2) Esfuerzos en compresión el concreto:

$f_{c}=2M≤( f_{c})admisible$(C-G-3) $bd^{2} jk$ donde:

$j=1−k$(C-G-4) $3$ y para secciones solo con refuerzo en tracción:

$k=\sqrt{(nρ)2+2nρ} − nρ$ (C-G-5) o para secciones con refuerzo a compresión:

$$ k = \sqrt{n^2\left(\rho + \rho'\right)^2 + 2n\left(\rho + \rho'\dfrac{d'}{d}\right)} - n\left(\rho + \rho'\right) $$

(C-G-6) b Notas
