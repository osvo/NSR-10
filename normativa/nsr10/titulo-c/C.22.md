# C.22 — Concreto estructural simple

### C.22.1 — Alcance

**C.22.1.1** — Este capítulo proporciona los requisitos mínimos para el diseño y construcción de elementos de concreto simple estructural (vaciados en sitio o prefabricados).

**C.22.1.2** — A menos que se encuentren en conflicto con las disposiciones del Capítulo C.22 de este Título C del Reglamento NSR-10, los siguientes requisitos se deben aplicar a los elementos de concreto estructural simple:

Secciones C.1 al C.7.5, C.7.6.1, C.7.6.2, C.7.6.4, C.7.7, C.9.1.3, C.9.2, C.9.3.5, Capítulo C.20, C.21.12.2.5, C.9.2, C.9.3.5 y Apéndice C-D.

**C.22.1.3** — En estructuras especiales, como arcos, estructuras subterráneas para servicios públicos, muros de gravedad, y muros de protección, las disposiciones de este capítulo deben controlar cuando sean aplicables.

### C.22.2 — Limitaciones

**C.22.2.1** — El uso del concreto simple estructural debe limitarse a (a), (b) o (c):

(a) Elementos que están apoyados de manera continua sobre el suelo o que están apoyados sobre otros elementos estructurales capaces de proporcionarles un apoyo vertical continuo;

(b) Elementos en los cuales el efecto de arco genera compresión bajo todas las condiciones de carga;

(c) Muros y pedestales. Véanse C.22.6 y C.22.8 No está permitido el uso de columnas de concreto simple estructural.

**C.22.2.2** — Este capítulo no controla el diseño e instalación de pilas y pilotes construidos en sitio y embebidos en el terreno.

#### C.22.2.3 — Resistencia mínima especificada

La resistencia especificada a compresión del concreto simple estructural no debe ser menor que lo estipulado en C.1.1.1 y los requisitos de durabilidad del Capítulo C.4.

### C.22.3 — Juntas

**C.22.3.1** — Deben proporcionarse juntas de contracción o aislamiento para dividir los elementos de concreto simple estructural en elementos discontinuos en flexión. El tamaño de cada elemento debe escogerse para limitar el esfuerzo causados por la restricción de los movimientos debidos a los efectos de flujo plástico, retracción y variación de temperatura.

**C.22.3.2** — En la determinación del número y ubicación de las juntas de contracción o aislamiento debe prestarse atención a: influencia de las condiciones climáticas; selección y dosificación de materiales; mezclado, colocación y curado del concreto; grado de restricción al movimiento; esfuerzos debidos a las cargas a las cuales está sometido el elemento; y técnicas de construcción.

### C.22.4 — Método de diseño

**C.22.4.1** — Las cargas y fuerzas mayoradas deben combinarse de acuerdo con lo especificado en C.9.2.

**C.22.4.2** — Cuando la resistencia requerida excede a la resistencia de diseño, debe proporcionarse refuerzo y el elemento debe diseñarse como elemento de concreto reforzado de acuerdo con los requisitos apropiados de este Título C del Reglamento NSR-10.

**C.22.4.3** — El diseño por resistencia de elementos de concreto simple estructural para flexión y cargas axiales debe basarse en relaciones esfuerzo-deformación lineales, tanto en tracción como en compresión.

**C.22.4.4** — En el diseño de elementos de concreto simple estructural, se puede considerar la resistencia a tracción del concreto cuando se han seguido las disposiciones de C.22.3.

**C.22.4.5** — No se debe asignar resistencia al refuerzo de acero que pudiera estar presente.

**C.22.4.6** — La tracción no debe transmitirse a través de los bordes exteriores, juntas de construcción, juntas de contracción, o juntas de aislamiento de un elemento individual de concreto simple. No se debe suponer continuidad a la flexión debida a tracción entre elementos adyacentes de concreto simple estructural.

**C.22.4.7** — Al calcular la resistencia a flexión, flexión y carga axial combinada, y cortante, debe considerarse en el diseño la sección completa de un elemento, excepto para el concreto construido contra el suelo en donde la altura total $h$ debe tomarse como 50 mm menor que la dimensión real.

### C.22.5 — Diseño por resistencia

**C.22.5.1** — El diseño de secciones transversales sometidas a flexión debe basarse en:

$$ \phi M_n \ge M_u \tag{C.22-1} $$

donde

$$ M_n = 0.42\,\lambda \sqrt{f'_c}\,S_m \tag{C.22-2} $$

si controla la tracción, y por

$$ M_n = 0.85\,f'_c S_m \tag{C.22-3} $$

si controla la compresión, donde $S_{m}$ es el módulo elástico de la sección correspondiente.

**C.22.5.2** — El diseño de secciones transversales sometidas a compresión debe basarse en:

$$ \phi P_n \ge P_u \tag{C.22-4} $$

donde $P_{n}$ se calcula como:

$$ P_n = 0.60\,f'_c \left[1 - \left(\dfrac{\ell_c}{32\,h}\right)^2\right] A_1 \tag{C.22-5} $$

y$A_{1}$ es el área cargada.

**C.22.5.3** — Los elementos sometidos a una combinación de flexión y carga axial de compresión deben diseñarse de manera que en la cara de compresión:

$$ \dfrac{P_u}{\phi P_n} + \dfrac{M_u}{\phi M_n} \le 1 \tag{C.22-6} $$

y en la cara de tracción:

$$ \dfrac{M_u}{S_m} - \dfrac{P_u}{A_g} \le \phi\,0.42\,\lambda \sqrt{f'_c} \tag{C.22-7} $$

**C.22.5.4** — El diseño de secciones transversales rectangulares sometidas a cortante debe basarse en:

$$ \phi V_n \ge V_u \tag{C.22-8} $$

donde $V_{n}$ se calcula como:

$$ V_n = 0.11\,\lambda \sqrt{f'_c}\,b_w h \tag{C.22-9} $$

para la acción como viga, y como:

$$ V_n = 0.11 \left[1 + \dfrac{2}{\beta}\right] \lambda \sqrt{f'_c}\,b_o h \tag{C.22-10} $$

para la acción en dos direcciones, pero no mayor $0.22λ\sqrt{f_{c} '}b_{o} h$. En la ecuación (C.22-10), $β$ corresponde a la relación de lado largo a lado corto de la carga concentrado o del área de la reacción.

**C.22.5.5** — El diseño de superficies de apoyo sometidas a compresión debe basarse en:

$$ \phi B_n \ge B_u \tag{C.22-11} $$

donde $B_{u}$ es la carga de aplastamiento mayorada y $B_{n}$ es la resistencia nominal al aplastamiento del área cargada $A_{1}$ , calculada como:

$$ B_n = 0.85\,f'_c A_1 \tag{C.22-12} $$

excepto cuando la superficie de apoyo es más ancha en todos los lados que el área cargada, caso en el cual $B_{n}$ debe multiplicarse por $\sqrt{A_{2}/A_{1} }$, pero no por más de 2.

#### C.22.5.6 — Concreto liviano

**C.22.5.6.1** — En este capítulo, el factor de modificación $λ$ para el concreto de peso liviano debe estar de acuerdo con 8.6.1 a menos que se especifique de otro modo.

### C.22.6 — Muros

**C.22.6.1** — Los muros de concreto simple estructural deben estar apoyados de manera continua en el terreno, en zapatas, muros de cimentación, vigas de cimentación, o en otros elementos estructurales capaces de proporcionar un apoyo vertical continuo.

**C.22.6.2** — Los muros de concreto simple estructural deben diseñarse para las cargas verticales, laterales o de otro tipo a las cuales estén sometidos.

**C.22.6.3** — Los muros de concreto simple estructural deben diseñarse para una excentricidad correspondiente al momento máximo que puede acompañar a la carga axial, pero no menor a $0.10h$ . Si la resultante de todas las cargas mayoradas se ubica dentro del tercio central del espesor total del muro, el diseño debe realizarse de acuerdo con C.22.5.3 ó C.22.6.5. En caso contrario, los muros deben diseñarse de acuerdo con C.22.5.3.

#### C.22.6.4 — El diseño por cortante debe realizarse de acuerdo con C.22.5.4.

#### C.22.6.5 — Método empírico de diseño

**C.22.6.5.1** — Los muros de concreto simple estructural de sección rectangular sólida se pueden diseñar por medio de la ecuación (C.22-13), siempre que la resultante de todas las cargas mayoradas se ubique dentro del tercio central del espesor total del muro.

**C.22.6.5.2** — El diseño de muros sometidos a cargas axiales de compresión debe basarse en :

$$ \phi P_n \ge P_u \tag{C.22-13} $$

donde $P_{u}$ es la fuerza axial mayorada y $P_{n}$ es la resistencia nominal axial, calculada como:

$$ P_n = 0.45\,f'_c A_g \left[1 - \left(\dfrac{\ell_c}{32\,h}\right)^2\right] \tag{C.22-14} $$

#### C.22.6.6 — Limitaciones

**C.22.6.6.1** — A menos que se demuestre mediante un análisis detallado, la longitud horizontal de un muro considerada como efectiva para cada carga vertical concentrada no debe exceder la distancia entre los ejes de las cargas, ni el ancho de la zona de apoyo más 4 veces el espesor del muro.

**C.22.6.6.2** — Excepto en lo establecido en C.22.6.6.3, el espesor de muros de carga no debe ser menor que 1/24 de la longitud o altura no apoyada, la que sea menor, ni que 140 mm.

**C.22.6.6.3** — El espesor de muros exteriores de sótano y de cimentación no debe ser menor que 190 mm.

**C.22.6.6.4** — Los muros deben estar arriostrados contra el desplazamiento lateral. Véanse C.22.3 y C.22.4.7.

**C.22.6.6.5** — Se deben proporcionar no menos de dos barras No. 5 (5/8”) ó 16M (16 mm) alrededor de todas las aberturas de ventanas y puertas. Dichas barras deben extenderse al menos 600 mm más allá de las esquinas de las aberturas.

### C.22.7 — Zapatas

**C.22.7.1** — Las zapatas de concreto simple estructural deben diseñarse para las cargas mayoradas y las reacciones inducidas, de acuerdo con los requisitos de diseño apropiados de este Título C del Reglamento NSR-10 y según lo indicado en C.22.7.2 a C.22.7.8.

**C.22.7.2** — El área de la base de la zapata debe determinarse a partir de las fuerzas y momentos no mayorados transmitidos por la zapata al suelo y la capacidad admisible del suelo determinadas de acuerdo con los principios de la mecánica de suelos.

#### C.22.7.3 — No debe usarse concreto simple para zapatas sobre pilotes.

**C.22.7.4** — El espesor de las zapatas de concreto simple estructural no debe ser menor que 200 mm. Véase C.22.4.7.

#### C.22.7.5 — Los momentos mayorados máximos deben calcularse en (a), (b) y (c):

(a) En la cara de la columna, pedestal o muro, para zapatas que soporten estos elementos.

(b) A media distancia entre el eje y el borde del muro, en zapatas que soporten un muro de albañilería.

(c) A la mitad de la distancia entre el borde de la columna y el borde de la platina de base de acero en zapatas que soportan columnas con una platina de base de acero.

#### C.22.7.6 — Cortante en zapatas de concreto simple

**C.22.7.6.1** — $V_{u}$ debe calcularse de acuerdo con C.22.7.6.2, con la sección crítica ubicada en la cara de la columna, pedestal o muro en zapatas que soporten estos elementos. En zapatas que soporten columnas con platina de base de acero, la sección crítica debe ubicarse de acuerdo con lo definido en C.22.7.5(c).

**C.22.7.6.2** — $φV_{n}$ de zapatas de concreto simple estructural, en la cercanías de cargas concentradas o reacciones, está controlada por la más restrictiva de las dos condiciones siguientes:

(a) Acción como viga de la zapata, con la sección crítica extendiéndose a través de todo el ancho de la zapata y ubicada a una distancia $h$ del borde de la carga concentrada o área de reacción. Para esta condición, la zapata debe diseñarse de acuerdo con la ecuación (C.22-9).

(b) Acción en dos direcciones de la zapata, con la sección crítica perpendicular al plano de la zapata y ubicada de manera que su perímetro $b_{o}$ sea mínimo, pero no necesita estar más cerca que $h /2$ del perímetro de la carga concentrada o área de carga. Para esta condición, la zapata debe diseñarse de acuerdo con la ecuación (C.22- 10).

**C.22.7.7** — Para la ubicación de las secciones críticas de momento y cortante, se pueden tratar a las columnas con forma circular o de polígono regular, como elementos cuadrados de la misma área.

**C.22.7.8** — Las cargas de aplastamiento mayoradas, $B_{u}$ , en el concreto en la superficie de contacto entre elementos soportantes y soportados no debe exceder, en cualquiera de las superficies, la resistencia de diseño al aplastamiento, $φB_{n}$, para cualquiera de las dos superficies según lo indicado en C.22.5.5.

### C.22.8 — Pedestales

**C.22.8.1** — Los pedestales de concreto simple deben diseñarse para las cargas verticales, laterales o de otro tipo a las cuales estén sometidos.

**C.22.8.2** — La relación entre la altura no apoyada y el promedio de la menor dimensión lateral de pedestales de concreto simple no debe exceder 3.

**C.22.8.3** — La carga axial mayorada máxima, $P_{u}$ , aplicada a pedestales de concreto simple no debe exceder la resistencia de diseño al aplastamiento, $φB_{n}$, dada en C.22.5.5.

### C.22.9 — Elementos prefabricados

**C.22.9.1** — En el diseño de elementos prefabricados de concreto simple debe considerar todas las condiciones de carga desde la fabricación inicial hasta completar la estructura. Incluyendo el desencofrado, almacenamiento, transporte y montaje.

**C.22.9.2** — Las limitaciones de C.22.2 aplican a elementos prefabricados de concreto simple no sólo en su condición final sino también durante la fabricación, transporte y montaje.

**C.22.9.3** — Los elementos prefabricados deben estar conectados de manera segura para que transfieran todas las fuerzas laterales a un sistema estructural capaz de resistir dichas fuerzas.

**C.22.9.4** — Los elementos prefabricados deben estar adecuadamente arriostrados y apoyados durante el montaje para asegurar el adecuado alineamiento y la integridad estructural hasta que se completen las conexiones permanentes.

### C.22.10 — Concreto simple en estructuras resistentes a sismos

**C.22.10.1** — Las estructuras con capacidad de disipación de energía especial (DES) no pueden tener elementos de cimentación de concreto simple, excepto cuando:

(a) En viviendas aisladas para una o dos familias, de tres pisos o menos en altura con muros de carga de aporticamiento ligero, se pueden usar en zapatas de concreto simple sin refuerzo longitudinal que soporten los muros y zapatas aisladas de concreto simple;

(b) Para todas las demás estructuras, se permiten las zapatas de concreto simple que soporten muros de concreto reforzado construidos en obra o muros de albañilería reforzada, siempre y cuando las zapatas sean reforzadas longitudinalmente con no menos de dos barras continuas, no menores a No. 4 (1/2”) ó 12M (12 mm) y con un área no menor que 0.002 veces la sección bruta de la zapata. Debe proporcionarse continuidad al refuerzo en las esquinas e intersecciones.

(c) En viviendas aisladas para una o dos familias, de tres pisos o menos en altura con muros de carga de aporticamiento ligero, se pueden usar cimentaciones o muros de cimentación de concreto simple, siempre y cuando el muro no tenga menos de 190 mm de ancho y no esté conteniendo más de 1.2 m de relleno no balanceado.

"
