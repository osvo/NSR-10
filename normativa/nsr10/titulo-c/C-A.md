# C-A — Modelos puntal-tensor

## C-A.1 — Definiciones

Discontinuidad (Discontinuity) — Cambio abrupto en la geometría o en la carga.

Modelo puntal-tensor (Strut-and-tie model) — Un modelo de cercha de un elemento estructural, o de una región-D de ese elemento, hecho con puntales y tensores conectados en los nodos, capaces de transferir las cargas mayoradas a los apoyos o hacia las regiones-B adyacentes.

Nodo (Node) — En un modelo puntal-tensor, donde se intersectan los ejes de los puntales, tensores y fuerzas concentradas que actúan en el nodo.

Puntal (Strut) — Un elemento a compresión en el modelo puntal-tensor. Un puntal representa la resultante de un campo de compresión paralelo o en forma de abanico.

Puntal en forma de botella (Bottle-shaped strut) — Un puntal que es más ancho en el centro que en sus extremos.

Región-B (B-region) — Parte de un elemento en la que pueden aplicarse las suposiciones de secciones planas, mencionadas de la teoría de flexión en C.10.2.2.

Región-D (D-region) — La parte de un elemento dentro de una distancia $h$ de una discontinuidad de fuerza o geométrica.

Tensor (Tie) — Un elemento a tracción en el modelo puntal-tensor.

Viga alta (Deep beam) — Véanse C.10.7.1 y C.11.7.1.

Zona nodal (Nodal zone) — El volumen de concreto alrededor de un nodo que se supone transfiere las fuerzas de los puntales y tensores a través del nodo.

## C-A.2 — Procedimiento de diseño del modelo puntal-tensor

**C-A.2.1** — Se permite diseñar elementos de concreto estructural, o regiones-D en estos elementos, modelando el elemento o región como una cercha idealizada. El modelo de cercha debe contener puntales, tensores y nodos, como se define en C.A.1. El modelo de cercha debe ser capaz de transferir todas las cargas mayoradas hacia los apoyos o regiones-B adyacentes.

**C-A.2.2** — El modelo puntal-tensor debe estar en equilibrio con las cargas aplicadas y las reacciones.

**C-A.2.3** — Para determinar la geometría de la cercha, se deben considerar las dimensiones de los puntales, tensores y zonas nodales.

**C-A.2.4** — Se permite que los tensores atraviesen los puntales. Los puntales deben cruzarse o superponerse sólo en los nodos.

**C-A.2.5** — El ángulo, $θ$ , entre los ejes de cualquier puntal y de cualquier tensor entrando en un solo nodo no debe ser menor de 25°.

### C-A.2.6 — El diseño de los puntales, tensores y zonas nodales debe basarse en:

$φF_{n}≥F_{u}$(C-A-1) donde $F_{u}$ es la fuerza mayorada que actúa en un puntal o en un tensor, o en una cara de una zona nodal; $F_{n}$ es la resistencia nominal del puntal, tensor o zona nodal; $φ$ está especificado en C.9.3.2.6.

## C-A.3 — Resistencia de los puntales

**C-A.3.1** — La resistencia nominal a la compresión de un puntal sin refuerzo longitudinal, $F_{ns}$, debe tomarse como el menor valor de

$F_{ns}=f_{ce} A_{cs}$(C-A-2) en los dos extremos del puntal, donde $A_{cs}$ es el área de la sección transversal en un extremo del puntal, y, $f_{ce}$ es el menor valor entre (a) y (b):

(a) la resistencia efectiva a la compresión del concreto en el puntal dado en C-A.3.2,

(b) la resistencia efectiva a la compresión en el concreto en la zona nodal dada en C-A.5.2.

**C-A.3.2** — La resistencia efectiva a la compresión del concreto, $f_{ce}$, en un puntal debe ser tomada como

$f_{ce}=0.85_{β}f_{c}'$(C-A-3)

**C-A.3.2.1** — Para un puntal de sección transversal uniforme a lo largo de su longitud $β_{s}=1.0$

**C-A.3.2.2** — Para los puntales ubicados de tal manera que el ancho de la sección media del puntal es mayor que el ancho en los nodos (puntales en forma de botella):

(a) Con refuerzo que cumpla con C-A.3.3 $.........................................................................................β_{s} =0.75$

(b) Sin refuerzo que cumpla con C-A.3.3 $.........................................................................................β_{s} =0.60_{λ}$ donde $λ$ está definido en C.8.6.1.

#### C-A.3.2.3 — Para los puntales en elementos sometidos a tracción, o alas en

tracción de los elementos $.........................................................................................................................β_{s} =0.40$

**C-A.3.2.4** — Para todos los demás casos $........................................................................................β_{s} =0.60_{λ}$

**C-A.3.3** — Si se emplea el valor de $β_{s}$ especificado en C.3.2.2(a), el eje del puntal debe ser cruzado por el refuerzo diseñado para resistir la fuerza de tracción transversal resultante de la expansión de la fuerza de compresión en el puntal. Se permite suponer que la fuerza de compresión se expande en los puntales con una pendiente de 2 longitudinal a 1 transversal al eje del puntal.

**C-A.3.3.1** — Para un $f_{c}'$ no mayor a 40 MPa, se admite que las disposiciones de C-A.3.3 se satisfacen cuando el eje del puntal es cruzado por filas de refuerzo que cumplen la ecuación (C-A-4).

$∑b_{s}A_{si} s_{i}sen_{α ≥}0.003$(C-A-4) donde $A_{si}$ es el área total del refuerzo de superficie con un espaciamiento $s_{i}$ en la capa i de refuerzo con barras a un ángulo $α_{i}$ con respecto al eje del puntal.

**C-A.3.3.2** — El refuerzo exigido en C-A.3.3 debe colocarse en alguna de las siguientes formas: en direcciones ortogonales en ángulos $α_{1}$ y $α_{2}$ con respecto al eje del puntal, o en una dirección en un ángulo $α$ con respecto al eje del puntal. Si el refuerzo se coloca en una sola dirección, $α$ no debe ser menor de 40°.

**C-A.3.4** — Si se encuentra documentado mediante ensayos y análisis, se permite usar una resistencia efectiva a la compresión incrementada del puntal debido al refuerzo de confinamiento.

**C-A.3.5** — Se permite el uso de refuerzo de compresión para aumentar la resistencia de un puntal. El refuerzo de compresión debe colocarse dentro de él, paralelo al eje del puntal, anclarse adecuadamente, y rodearse por estribos o espirales que cumplan con C.7.10. En estos casos, la resistencia nominal de un puntal reforzado longitudinalmente es:

$F_{ns}=f_{ce} A_{cs}+A_{s} '+f_{s}'$(C-A-5)

## C-A.4 — Resistencia de los tensores

### C-A.4.1 — La resistencia nominal de un tensor, $F_{nt}$, debe calcularse como

$F_{nt}=A_{ts} f_{y}+A_{tp}(f_{se}+Δf_{p})$(C-A-6) donde $(f_{se}+Δf_{p})$ no debe exceder $f_{py}$, y $A_{tp}$ es igual a cero para los elementos no preesforzados.

En la ecuación(C-A-6), se permite tomar $Δf_{p}$ igual a 420 MPa para el refuerzo preesforzado adherido, o 70 MPa para el refuerzo preesforzado no adherido. Se permiten otros valores de $Δf_{p}$ cuando se justifiquen por medio de análisis.

**C-A.4.2** — El eje del refuerzo en un tensor debe coincidir con el eje del tensor en el modelo puntal-tensor.

**C-A.4.3** — El refuerzo del tensor debe anclarse mediante dispositivos mecánicos, dispositivos de anclaje postensados, ganchos estándar o mediante el desarrollo de barra rectas, como lo exigen C-A.4.3.1 a C-A.4.3.4.

**C-A.4.3.1** — Las zonas nodales deben desarrollar la diferencia entre la fuerza en el tensor en un lado del nodo y la fuerza en el tensor en el otro lado del nodo.

**C-A.4.3.2** — En las zonas nodales que anclan un solo tensor, la fuerza en el tensor debe desarrollarse en el punto donde el centroide del refuerzo del tensor sale de la zona nodal extendida y entra en la luz del elemento.

**C-A.4.3.3** — En las zonas nodales que anclan dos o más tensores, la fuerza del tensor en cada dirección debe desarrollarse en el punto donde el centroide del refuerzo del tensor sale de la zona nodal extendida.

**C-A.4.3.4** — El refuerzo transversal requerido por C-A.3.3 debe anclarse de acuerdo con C.12.13.

## C-A.5 — Resistencia de las zonas nodales

**C-A.5.1** — La resistencia nominal a la compresión de una zona nodal, $F_{nn}$, debe ser

$F_{nn}=f_{ce} A_{nz}$(A-7) donde $f_{ce}$ es la resistencia efectiva a la compresión del concreto en una zona nodal, como se da en C-A.5.2 y $A_{nz}$ es la menor de (a) y (b):

(a) el área de la cara de una zona nodal en donde actúa $F_{u}$ , tomada en forma perpendicular a la línea de acción de $F_{u}$ , o

(b) el área de una sección a través de la zona nodal, tomada en forma perpendicular a la línea de acción de la fuerza resultante en la sección.

**C-A.5.2** — A menos que se coloque refuerzo de confinamiento dentro de la zona nodal y que sus efectos sean respaldados por ensayos y análisis, los esfuerzos de compresión efectivos, $f_{ce}$, calculados en una cara de una zona nodal debidos a las fuerzas del modelo puntal-tensor, no deben exceder el valor dado por:

$f_{ce}=0.85β_{n}f_{c}'$(C-A-8) donde el valor de $β_{n}$ está dado en C-A.5.2.1 a C-A.5.2.3.

**C-A.5.2.1** — En zonas nodales limitadas por puntales o áreas de apoyo, o ambas ........................ $β_{n}=1.0$

**C-A.5.2.2** — En zonas nodales que anclan un tensor $............................................................................β_{n} =0.80$ ó

**C-A.5.2.3** — En zonas nodales que anclan dos o más tensores $.........................................................β_{n} =0.60$

**C-A.5.3** — En un modelo puntal-tensor tridimensional, el área de cada cara de una zona nodal no debe ser menor a la dada en C-A.5.1, y la forma de cada cara de las zonas nodales debe ser similar a la forma de la proyección del extremo de los puntales sobre las caras correspondientes de las zonas nodales.

"
