# A.8 — Efectos sísmicos sobre elementos estructurales que no hacen parte del sistema de resistencia sísmica

### A.8.0 — NOMENCLATURA

$A_{s}$ = aceleración máxima en la superficie del suelo estimada como la aceleración espectral correspondiente a un período de vibración igual a cero, Véase A.8.2.1.1.

$a_{i}$ = aceleración en el nivel l $i$ , Véase A.8.2.1.1.

$a_{x}$= aceleración horizontal, expresada como un porcentaje de la aceleración de la gravedad, sobre el elemento estructural que no hace parte del sistema de resistencia sísmica, localizado en el piso $x$

$F_{p}$ = fuerza horizontal sobre un elemento estructural que no hace parte del sistema de resistencia sísmica, aplicada en su centro de masa.

$g$ = aceleración debida a la gravedad ($g=9.8$ m/s2).

$h_{i}$ = altura en metros, medida desde la base, del nivel $i$ , véase A.8.2.1.1.

$h_{n}$= altura en metros, medida desde la base, del piso más alto de la edificación, véase A.8.2.1.1.

$h_{eq}$= altura equivalente del sistema de un grado de libertad que simula la edificación, véase A.8.2.1.1.

$M_{p}$ = masa de un elemento estructural que no hace parte del sistema de resistencia sísmica.

$R_{0}$ = coeficiente de capacidad de disipación de energía básico definido para cada sistema estructural y cada grado de capacidad de disipación de energía del material estructural. Véase el Capítulo A.3.

$S_{a}$= valor del espectro de aceleraciones de diseño para un período de vibración dado. Máxima aceleración horizontal de diseño, expresada como una fracción de la aceleración de la gravedad, para un sistema de un grado de libertad con un período de vibración $T$ . Está definido en A.2.6.

### A.8.1 — GENERAL

#### A.8.1.1 — ALCANCE

El presente Capítulo cubre las previsiones sísmicas que deben tenerse en el diseño de los elementos estructurales que no hacen parte del sistema de resistencia sísmica, tal como se define en el Capítulo A.3, y de sus anclajes a él. Dentro de estos elementos se incluyen, pero no están limitados a:

(a) Escaleras, rampas, etc.,

(b) Tanques, piscinas, etc.,

(c) Elementos de cubiertas, tales como cerchas, correas, etc.,

(d) Elementos secundarios de los sistemas de entrepiso, tales como viguetas, etc.,

(e) Columnas, columnetas, machones, y otros elementos que dan soporte a cubiertas y otras partes menores de la edificación,

(f) Apoyos de equipos tales como ascensores, escaleras mecánicas, etc., y

(g) En general todos aquellos elementos estructurales que se incluyen dentro de los planos estructurales y que no hacen parte del sistema de resistencia sísmica.

#### A.8.1.2 — RESPONSABILIDAD DEL DISEÑO

El diseño, ante las solicitaciones establecidas por el presente Reglamento en el Titulo A o en el Titulo B, de todo elemento estructural que figure dentro de los planos estructurales, es responsabilidad del diseñador estructural. Dentro de estos elementos se incluyen los elementos mencionados en A.8.1.1.

#### A.8.1.3 — CRITERIO DE DISEÑO

El diseño ante efectos sísmicos de los elementos estructurales que no hacen parte del sistema de resistencia sísmica, constituido por los elementos estructurales en sí, y de los anclajes, uniones o amarres de estos elementos al sistema de resistencia sísmica, debe realizarse para la situación que controle:

(a) El efecto de las fuerzas sobre el elemento en sí, no hacen parte del sistema de resistencia sísmica

(b) La capacidad de resistir las deformaciones, que al elemento le impone el sistema de resistencia sísmica al responder a los movimientos sísmicos de diseño, y la influencia que pueda tener el elemento en la respuesta sísmica de la estructura, como puede ser el caso de las escaleras y rampas, las cuales pueden actuar como arriostramientos (o diagonales) de un piso con otro.

### A.8.2 — FUERZAS HORIZONTALES DE DISEÑO

#### A.8.2.1 — ACELERACIÓN HORIZONTAL SOBRE EL ELEMENTO

El elemento se ve sometido, ante la ocurrencia de los movimientos sísmicos de diseño, a las mismas aceleraciones horizontales que se ve sometido el sistema de resistencia sísmica en la misma altura sobre la base de la edificación en que se encuentre el elemento.

Las fuerzas inerciales a que se ve sometido el elemento o cualquier porción de él, corresponden a la masa del elemento multiplicada por la aceleración que le imponen los movimientos causados por el sismo. Esta aceleración se determina por medio de uno de los procedimientos siguientes:

**A.8.2.1.1** — Método de la fuerza horizontal equivalente — Cuando se utilice el método de la fuerza horizontal equivalente, tal como lo prescribe el Capítulo A.4, la aceleración horizontal, $a_{i}$, expresada como una fracción de la aceleración de la gravedad, sobre el elemento estructural que no hace parte del sistema de resistencia sísmica, localizado en el piso $i$, se obtiene por medio de la siguiente ecuación:

$$ \begin{cases} a_i = A_s + \dfrac{(S_a - A_s)\,h_i}{h_{eq}} & h_i \le h_{eq} \\[4pt] a_i = S_a\,\dfrac{h_i}{h_{eq}} & h_i \ge h_{eq} \end{cases} \tag{A.8.2-1} $$

$h_{eq}$ puede estimarse simplificadamente como $0.75h_{n}$ Alternativamente a la ecuación A.8.2-1 para calcular las fuerzas que deben resistir los diafragmas de piso o de cubierta, pueden usarse estimaciones más precisas de las aceleraciones absolutas máximas a que estarían sometidos estos diafragmas, resultado por ejemplo, de análisis dinámicos.

**A.8.2.1.2** — Método del análisis dinámico — Cuando se utilice el método del análisis dinámico, la aceleración horizontal, $a_{x}$ , expresada como un porcentaje de la aceleración de la gravedad, sobre el elemento estructural que no hace parte del sistema de resistencia sísmica, localizado en el piso $x$ , es igual a la aceleración a que se ve sometido el piso después de realizar el ajuste de resultados prescrito en A.5.4.5. El valor de la aceleración obtenida por medio del método del análisis dinámico no puede ser menor que el que se obtiene por medio de la ecuación A.8.2-1.

#### A.8.2.2 — FUERZAS HORIZONTALES SOBRE EL ELEMENTO

La fuerza sísmica horizontal reducida de diseño, que puede actuar en cualquier dirección, sobre el elemento estructural que no hace parte del sistema de resistencia sísmica en su centro de masa, se obtiene por medio de la siguiente ecuación:

$$ F_p = \dfrac{a_x\,g}{R_0}\,M_p \tag{A.8.2-2} $$

donde $R_{0}$ es el coeficiente de capacidad de disipación de energía correspondiente a los requisitos de diseño del elemento estructural, como se indica en A.8.4. La anterior ecuación puede aplicarse a elementos que tienen un solo apoyo, o cuando no hay desplazamientos relativos entre sus apoyos.

**A.8.2.2.1** — Cuando el elemento estructural que no hace parte del sistema de resistencia sísmica, tiene características dinámicas que amplifiquen su respuesta ante la aceleración $a_{x}$ , estas características deben tenerse en cuenta en la evaluación de las fuerzas horizontales que lo puedan afectar. Esto ocurre especialmente en apéndices de la edificación.

no hacen parte del sistema de resistencia sísmica

**A.8.2.2.2** — Cuando el elemento estructural que no hace parte del sistema de resistencia sísmica, tiene apoyos que pueden desplazarse relativamente durante el sismo, como es el caso de elementos que están conectados a dos pisos diferentes de la edificación, deben tenerse en cuenta en el diseño, además de las fuerzas calculadas por medio de la ecuación A.8.2-2, las fuerzas que inducen los desplazamientos relativos entre sus apoyos.

#### A.8.2.3 — FUERZAS SOBRE LAS UNIONES AL SISTEMA DE RESISTENCIA SÍSMICA

Además de los requisitos de A.3.6.4, las uniones, empalmes y amarres, de los elementos estructurales que no hacen parte del sistema de resistencia sísmica, deben ser capaces de resistir la totalidad de las fuerzas sísmicas reducidas de diseño sobre el elemento tal como las define A.8.2.2.

### A.8.3 — DEFORMACIONES DE DISEÑO

**A.8.3.1** — Los elementos estructurales que no hacen parte del sistema de resistencia sísmica deben ser capaces de resistir, sin deterioro, las deformaciones que les impone la respuesta sísmica de la estructura. Como mínimo deben ser capaces de resistir las deformaciones que se obtienen de las derivas máximas de diseño determinadas como se indica en el Capítulo A.6.

### A.8.4 — REQUISITOS DE DISEÑO

**A.8.4.1** — Los requisitos que deben seguirse en el diseño de los elementos estructurales que no hacen parte del sistema de resistencia sísmica para cada uno de los materiales cubiertos por el Reglamento, deben ser los que se indiquen en cada uno de los Títulos correspondientes dentro del Reglamento, y en su defecto, los del nivel de capacidad de disipación de energía menor de los dados para cada material.

█ no hacen parte del sistema de resistencia sísmica Notas:
