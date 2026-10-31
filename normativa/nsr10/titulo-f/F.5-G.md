# F.5-G — Pandeo torsional lateral de vigas

F.5.G.1 — LONGITUD EFECTIVA DE VIGAS F.5.G.1.1 — VIGAS SOPORTADAS EN AMBOS EXTREMOS — La longitud efectiva $I$ de una viga, para usar en F.5.4.5.6 (d), debe obtenerse de la tabla F.5.G.1 si la viga tiene restricción lateral efectiva sólo en sus extremos.

Para vigas con restricciones laterales efectivas en intervalos dentro de su longitud, el valor de l debe tomarse como la longitud entre restricciones.

F.5.G.1.2 — CARGAS DESESTABILIZADORAS — Existen condiciones desestabilizadoras de carga cuando una carga es aplicada a la aleta superior de una viga y tanto la carga como la viga tienen la libertad de deflectarse lateralmente con relación al centroide de la viga. En tales casos, se deben usar las longitudes efectivas incrementadas de la tabla F.5.G.1.

Para vigas que soportan cargas desestabilizadoras pero tienen restricción lateral efectiva a intervalos dentro de su longitud, el valor de l debe tomarse como 1.2 veces la longitud entre soportes laterales.

F.5.G.1.3 — VOLADIZOS — La longitud efectiva $l$ para voladizos sin soporte lateral intermedio y sin momento aplicado en la punta, debe obtenerse de la tabla F.5.G.2.

Si se suministran apoyos laterales intermedios, los valores de l para las longitudes entre restricciones deben tomarse de F.5.G.1.1 o F.5.G.1.2.

Para voladizos sometidos a un momento en la punta, $l$ se debe determinar de acuerdo con F.5.G.1.1 o F.5.G.1.2.

F.5.G.2 — DETERMINACION DE $λ$ El parámetro de esbeltez para pandeo torsional lateral $λ$ se obtiene de la siguiente expresión (véase F.5.4.5.6 (d)):

$$ \lambda =\pi \left(\dfrac{ES}{M_{cr}}\right)^{1/2} $$

Donde:

$M_{cr}$= momento uniforme elástico crítico

$E$ y $S$ = como se definen en F.5.4.5.6 (d) Para una sección uniforme doble-simétrica, $M_{cr}$ está dado por:

$M_{cr}=πl(EI_{y} GJ)1 /2(1+ π^{2}EH / L^{2} GJ)1 /2$ Donde:

$I_{y}$ = segundo momento del área respecto al menor eje centroidal

$G$ , $J$ y $H$ = como se definen en F.5.1.3 Para una sección uniforme simétrica respecto al eje menor solamente, $M_{cr}$ está dado por:

$$ M_{cr}=\dfrac{\pi }{l}(EI_{y}GJ)^{1/2}\left\{\left(1+\dfrac{\pi ^{2}\beta _{x}^{2}}{4l^{2}}\dfrac{EI_{y}}{GJ}\right)^{1/2}+\dfrac{\pi \beta _{x}}{2l}\left(\dfrac{EI_{y}}{GJ}\right)^{1/2}\right\} $$

Donde:

$$ \beta _{x}=\dfrac{l}{I_{x}}\left(\int\limits_{0}^{A} x^{2}ydA+\int\limits_{0}^{A} y^{3}dA\right)-2y_{0} $$

$I_{x}$ = segundo momento del área respecto al mayor eje centroidal

$y_{o}$ = distancia entre el centroide y el centro de corte

$A$ = área de la sección transversal del voladizo En ambos casos se puede consultar la literatura disponible para soluciones de $M_{cr}$ relacionadas con arreglos de carga diferentes a momento uniforme. Cuando ésto se tenga en cuenta para determinar $λ$ , el valor de $M$ en F.5.4.5.6 (b) debe tomarse como el valor máximo en la viga.

F.5.G.3 — VIGAS QUE VARIAN DE SECCION A LO LARGO DE SU LONGITUD Cuando la sección doble-simétrica de una viga o voladizo varía a lo largo de su longitud entre puntos de restricción, se debe determinar el esfuerzo de pandeo $p_{s}$ usando las propiedades de la sección en el punto de momento máximo.

Luego, este valor de $p_{s}$ se aplica a toda la longitud entre puntos de restricción y no se deben hacer consideraciones adicionales para el patrón de momentos.

Siempre que $R_{f}$ no sea menor que 0.2, el valor de $λ$ , basado en la sección transversal en el punto de máximo momento, debe multiplicarse por $(1.5−0.5R_{f})$(pero $≥$ 1.0) Donde: $R_{f}$ es la relación del área de aleta en el punto de mínimo momento sobre el área de aleta en el punto de máximo momento entre puntos de restricción adyacentes. $R_{f}$ se refiere o a la relación de área total de ambas aletas o al área de la aleta de compresión únicamente, la que de el menor valor de $R_{f}$ . Valores de $R_{f}$ menores de 0.2 representan un grado extremo de disminución en la sección de la aleta que no está cubierto por esta cláusula.

**Tabla F.5.G-1**

Longitud efectiva $I$ para vigas de longitud $L$

| Condiciones de restricción en los apoyos |  | Condiciones de carga |  |
|---|---|---|---|
|  |  | Normal | Desestabilizadora |
| Aleta a compresión restringida lateralmente | Ambas aletas totalmente restringidas contra rotación en el plano | $0.7L$ | $0.85L$ |
| Viga totalmente restringida contra torsión | Ambas aletas parcialmente restringidas contra rotación en el plano | $0.85L$ | $1.0L$ |
|  | Ambas aletas libres de rotar en el plano | $1.0L$ | $1.2L$ |
| Aleta a compresión no restringida lateralmente | Restricción contra torsión suministrada únicamente por la conexión positiva de la aleta inferior a los apoyos | $1.0L+2D$ | $1.2L+2D$ |
| Ambas aletas libres de rotar en el plano | Restricción contra torsión suministrada únicamente por apoyo muerto de la aleta inferior sobre los apoyos | $1.2L+2D$ | $1.4L+2D$ |
| NOTA. $D$ es la altura de la viga, $L$ es la longitud de la viga. |  |  |  |

**Tabla F.5.G-2**

Longitud efectiva $l$ para vigas en voladizo de longitud $L$

| Condiciones de restricción |  | Condiciones de carga |  |
|---|---|---|---|
| En el apoyo | En la punta | Normal | Desestabilizadora |
| Continuo con restricción lateral únicamente | Libre | $3.0L$ | $7.5L$ |
|  | Lateralmente restringido en la aleta superior únicamente | $2.7L$ | $7.5L$ |
|  | Torsionalmente restringido únicamente | $2.4L$ | $4.5L$ |
|  | Lateral y torsionalmente restringido | $2.1L$ | $3.6L$ |
| Contínuo con restricción lateral y torsional | Libre | $1.0L$ | $2.5L$ |
|  | Lateralmente restringido en la aleta superior únicamente | $0.9L$ | $2.5L$ |
|  | Torsionalmente restringido únicamente | $0.8L$ | $1.5L$ |
|  | Lateral y torsionalmente restringido | $0.7L$ | $1.2L$ |
| Empotrado lateral y torsionalmente | Libre | $0.8L$ | $1.4L$ |
|  | Lateralmente restringido en la aleta superior únicamente | $0.7L$ | $1.4L$ |
|  | Torsionalmente restringido únicamente | $0.6L$ | $0.6L$ |
|  | Lateral y torsionalmente restringido | $0.5L$ | $0.5L$ |

determinación del parámetro de esbeltez $λ$
