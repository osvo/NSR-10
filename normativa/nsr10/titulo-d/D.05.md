# D.5 — Requisitos generales de análisis y diseño

### D.5.0 — NOMENCLATURA

$A_{e}$ = área efectiva de la sección de mampostería, mm2. Véase D.5.4.1.

$A_{mv}$= área efectiva para determinar esfuerzos cortantes, mm2. Véase D.5.4.5.

$A_{se}$= área efectiva de refuerzo en tracción, mm2.

$A_{st}$ = área total de acero de refuerzo en la sección de muro, mm2.

$A_{s1}$= área del refuerzo a tracción equilibrado por la compresión en la mampostería, mm2.

$A_{s2}$= área del refuerzo a tracción equilibrado por el refuerzo a compresión, mm2.

$A_{v}$ = área del refuerzo para cortante, mm2.

$a$ = profundidad del bloque equivalente de compresión (tomar como $0.85c$ ), mm.

$a_{b}$ = profundidad del bloque equivalente de compresión en condiciones balanceadas, ecuación D.5.1-2, mm.

$b$ = ancho efectivo de la sección, mm. Véase D.5.4.4.

$c$ = profundidad del eje neutro en la zona de compresión, mm.

$d$ = distancia de la cara de compresión al centroide del refuerzo en tracción, mm.

$d'$ = distancia desde el centroide del refuerzo en compresión flexión hasta la fibra extrema en compresión.

$E$ = efectos sísmicos reducidos.

$E_{m}$= módulo de elasticidad de la mampostería, MPa.

$E_{r}$ = módulo de elasticidad del mortero de relleno, MPa.

$E_{s}$ = módulo de elasticidad del acero de refuerzo, MPa.

$F_{s}$ = fuerzas sísmicas.

$f_{m}'$ = resistencia a la compresión de la mampostería, MPa.

$\sqrt{f_{m}'}$ = raíz cuadrada de la resistencia a la compresión de la mampostería, en MPa.

$f_{r}$ = módulo de ruptura de la mampostería, MPa.

$f_{y}$ = resistencia a la fluencia del acero de refuerzo, MPa.

$G_{m}$= módulo de cortante de la mampostería, MPa.

$G_{r}$ = módulo de cortante del mortero de relleno, MPa.

$h'$ = altura efectiva del elemento para evaluar efectos de pandeo, mm. Véase D.5.4.3.

$ℓ$ = luz de una viga o dintel, mm.

$ℓ_{w}$= longitud horizontal del muro, mm.

$M$ = momento actuante que ocurre simultáneamente con $V$ .

$M_{cr}$= momento de agrietamiento del muro de mampostería.

$M_{n}$ = resistencia nominal a flexión.

$M_{u}$ = resistencia solicitada de diseño a flexión

$P_{b}$ = carga axial nominal balanceada, N.

$P_{n}$ = resistencia nominal a carga axial, N.

$P_{o}$ = máxima resistencia axial teórica, N.

$P_{u}$ = resistencia solicitada de diseño a carga axial, N.

$R$ = coeficiente de capacidad de disipación de energía.

$R_{e}$ = coeficiente utilizado para temer en cuenta el efecto de esbeltez de elementos en compresión.

$R_{0}$ = coeficiente básico de capacidad de disipación de energía.

$s$ = separación del refuerzo de cortante medida a lo largo del eje vertical del muro, mm.

$t$ = espesor efectivo de la sección para evaluar efectos de pandeo, mm. Véase D.5.4.2.

$V$ = fuerza cortante actuante que ocurre simultáneamente con $M$ .

$V_{n}$ = resistencia nominal para fuerza cortante, N.

$V_{m}$ = resistencia nominal para fuerza cortante contribuida por la mampostería, N.

$V_{u}$ = resistencia solicitada de diseño de fuerza cortante, N.

$V$ = resistencia nominal para fuerza cortante contribuida por el refuerzo de cortante, N.

$α^{s}$ = coeficiente para ser empleado en la ecuación D.5.8-1.

$ε_{mu}$= máxima deformación unitaria permisible de compresión en la mampostería $(ε_{mu}=0.003)$

$ε_{y}$ = deformación unitaria de fluencia del acero de refuerzo.

$φ$ = coeficiente de reducción de resistencia.

$ρ$ = cuantía de refuerzo a tracción por flexión, $ρ =A_{s}/(bd)$

$ρ_{b}$ = cuantía correspondiente a las condiciones de flexión balanceada.

$ρ_{n}$ = cuantía de refuerzo horizontal que resiste cortante en un muro en un plano perpendicular al plano $A_{mv}$, mm2.

### D.5.1 — HIPÓTESIS Y PRINCIPIOS GENERALES

#### D.5.1.1 — GENERALIDADES

El análisis y diseño de la mampostería estructural debe hacerse utilizando métodos racionales basados en principios aceptados por la buena práctica de la ingeniería y que reflejen las características y propiedades de los materiales componentes, los métodos constructivos utilizados y el comportamiento individual y en conjunto del sistema estructural.

#### D.5.1.2 — METODOLOGÍA DE DISEÑO POR ESTADOS LIMITES DE RESISTENCIA

Los requisitos de análisis y diseño del Título D están basados en el método del estado límite de resistencia, utilizando las combinaciones de carga descritas en B.2.4. No obstante, se permite el diseño de estructuras de mampostería por el método de esfuerzos de trabajo, utilizando las combinaciones de carga descritas en B.2.3, y para el efecto pueden emplearse los requisitos alternos presentados en el Apéndice D-1. Todo el diseño de la estructura debe realizarse por uno de estos dos métodos

#### D.5.1.3 — RESISTENCIA REQUERIDA

La resistencia requerida para los elementos de mampostería estructural se obtiene como el valor máximo, expresado en términos de carga o momentos y fuerzas internas asociadas, que resultan de aplicar a la estructura las diferentes cargas tales como muertas, vivas, sísmicas, de viento e impuestas por cambios de temperatura, retracción de fraguado y flujo plástico, empuje de tierra o líquidos, etc.; combinadas y mayoradas de acuerdo con B.2.4 de este Reglamento.

#### D.5.1.4 — RESISTENCIA DE DISEÑO

La resistencia de diseño que tiene un elemento, sus conexiones con otros elementos y cualquier parte o sección de él, en términos de momentos flectores, carga axial, cortantes y torsión, debe ser igual a su resistencia nominal calculada de acuerdo con los requisitos y suposiciones del presente capítulo, multiplicada por un coeficiente de reducción de resistencia, $φ$ . Por lo tanto:

$$ \text{Resistencia de Diseño} = \phi \times \text{Resistencia Nominal} \ge \text{Resistencia Requerida} = U \tag{D.5.1-1} $$

Resistencia de Diseñox Resistencia Nominal Resistencia Requerida =

#### D.5.1.5 — VALORES DE $φ$

Los coeficientes de reducción de resistencia deben ser los siguientes:

**D.5.1.5.1** — Efectos gravitacionales y fuerzas horizontales perpendiculares al plano del muro — En el diseño de muros de mampostería estructural para efectos gravitacionales solos o acompañados por fuerzas horizontales perpendiculares al plano del muro, deben emplearse los siguientes coeficientes de reducción de resistencia:

(a) Flexión y flexo-compresión..................................................................$φ =0.80$

(b) Cortante ..............................................................................................$φ =0.60$

**D.5.1.5.2** — Fuerzas paralelas al plano del muro — En el diseño de muros de mampostería estructural para efectos causados por fuerzas horizontales paralelas al plano del muro, deben emplearse los siguientes coeficientes de reducción de resistencia:

(a) Flexión .................................................................................................$φ =0.85$

(b) Compresión y flexo-compresión..........................................................$φ =0.60$ Para muros con refuerzo simétrico en los cuales $f_{y}$ no excede 420 MPa, el valor de $φ$ puede incrementarse linealmente hasta $φ =0.85$ en la medida que $φ_{P}$ disminuye desde $0.10f_{m}'A_{e}$ ó $0.25P_{b}$ hasta cero. Para muros con todas sus celdas inyectadas, $P_{b}$ puede calcularse utilizando la ecuación (D.5.1-2).

$$ P_b = 0.80f'_m b a_b \qquad a_b = 0.85d \dfrac{\varepsilon_{mu}}{\varepsilon_{mu} + \dfrac{f_y}{E_s}} \tag{D.5.1-2} $$

y

(c) Cortante...............................................................................................$φ =0.60$ Este valor puede subirse a $φ =0.85$ en muros donde la resistencia nominal a cortante excede el cortante correspondiente al desarrollo de su resistencia nominal a flexión para la combinación de fuerzas mayoradas.

**D.5.1.5.3** — Valores de $φ$ para esfuerzos de aplastamiento — El valor de $φ$ para esfuerzos de aplastamiento debe ser $φ =0.60$

#### D.5.1.6 — SUPOSICIONES DE DISEÑO

El diseño de mampostería estructural por el método del estado límite de resistencia se basa en las siguientes suposiciones:

**D.5.1.6.1** — Resistencia a la tracción de la mampostería — La mampostería no resiste esfuerzos de tracción.

**D.5.1.6.2** — Compatibilidad de deformaciones — El refuerzo está totalmente rodeado y adherido a los materiales de la mampostería de una manera tal, que trabajan como un material homogéneo.

**D.5.1.6.3** — Secciones planas permanecen planas — Las deformaciones unitarias en el refuerzo y en la mampostería deben suponerse proporcionales a la distancia al eje neutro de la sección. La resistencia nominal de las secciones de muros de mampostería para las condiciones de flexo-compresión se debe obtener de la aplicación de los principios de equilibrio y compatibilidad de deformaciones.

**D.5.1.6.4** — Relación esfuerzo deformación para el acero de refuerzo — Los esfuerzos en el acero, para valores menores que el esfuerzo de fluencia, $f_{y}$, deben considerarse linealmente proporcionales a la deformación unitaria multiplicada por $E_{s}$ . Para valores superiores de deformación unitaria correspondiente al esfuerzo de fluencia, $ε_{y} =f_{y}/E_{s}$, el esfuerzo en el acero se debe considerar independiente de la deformación e igual a $f_{y}$.

**D.5.1.6.5** — Deformación unitaria máxima en la mampostería — La máxima deformación unitaria en la fibra extrema en compresión de la mampostería, $ε_{mu}$, debe tomarse como 0.003.

**D.5.1.6.6** — Relación esfuerzo-deformación para la mampostería — En el diseño por el método de resistencia puede considerarse una distribución rectangular de esfuerzos de compresión en la mampostería definida de la siguiente forma:

(a) Se puede suponer un esfuerzo uniforme de compresión en la mampostería con intensidad de $0.80f_{m}'$ sobre una zona equivalente limitada por los bordes de la sección efectiva y una línea recta paralela al eje neutro de la sección.

(b) La dimensión de la zona equivalente de compresión, $a$ , medida en dirección perpendicular al eje neutro a partir de la fibra de máxima compresión, debe ser el 85% de la dimensión comprimida, $c$ , de la sección en esa dirección $(a=0.85c)$.

### D.5.2 — MÓDULOS DE ELASTICIDAD Y DE CORTANTE

#### D.5.2.1 — MÓDULO DE ELASTICIDAD

Para los módulos de elasticidad se deben tomar los siguientes valores:

**D.5.2.1.1** — Acero de refuerzo — El valor para el módulo de elasticidad del acero de refuerzo debe tomarse como:

$$ E_s = 200\,000 \tag{D.5.2-1} $$

MPa

**D.5.2.1.2** — Mampostería — El valor para el módulo de elasticidad de la mampostería se debe establecer por medio de ensayos de laboratorio de muretes fabricados y ensayados como se indica en D.3.7.2, calculando en la curva esfuerzo-deformación obtenida en el ensayo la pendiente de la secante desde $0.05f_{m}'$ hasta $0.33f_{m}'$ . Los registros históricos del módulo de elasticidad determinado experimentalmente para proyectos en construcción, pueden utilizarse en diseños posteriores de obras con materiales similares. En ausencia de los valores experimentales, pueden emplearse los siguientes:

Para mampostería en concreto

$$ E_m = 900f'_m \le 20\,000 \tag{D.5.2-2} $$

MPa Para mampostería en arcilla

$$ E_m = 750f'_m \le 20\,000 \tag{D.5.2-3} $$

MPa

**D.5.2.1.3** — Mortero de relleno — El valor para el módulo de elasticidad del mortero de relleno se debe establecer por medio de ensayos de laboratorio de cilindros fabricados y ensayados como se indica en C.8.5.

En ausencia de valores experimentales, puede emplearse el siguiente:

$$ E_r = 2500\sqrt{f'_{cr}} \le 20\,000 \tag{D.5.2-4} $$

MPa

#### D.5.2.2 — MÓDULO DE CORTANTE

Para los módulos de cortante se deben tomar los siguientes valores: Mampostería

$$ G_m = 0.4E_m \tag{D.5.2-5} $$

Mortero de relleno

$$ G_r = 0.5E_r \tag{D.5.2-6} $$

### D.5.3 — CARGAS

#### D.5.3.1 — SOLICITACIONES A EMPLEAR

Las estructuras de mampostería deben diseñarse para los efectos de las cargas combinadas especificadas en el Título B de este Reglamento. Así mismo en la evaluación de los esfuerzos de diseño, se deben tener en cuenta los efectos de las cargas sobre los desplazamientos.

**D.5.3.1.1** — Combinación de las solicitaciones — Las diferentes solicitaciones que deben ser tenidas en cuenta, se combinan para obtener las fuerzas internas de diseño de la estructura, de acuerdo con los requisitos de B.2.4 por el método del estado límite de resistencia. En cada una de las combinaciones de carga requeridas, las solicitaciones se multiplican por el coeficiente de carga prescrito para esa combinación en B.2.4. En los efectos causados por el sismo se tiene en cuenta la capacidad de disipación de energía del sistema estructural, lo cual se logra empleando unos efectos sísmicos reducidos de diseño, $E$ , obtenidos dividiendo las fuerzas sísmicas $F_{s}$ , determinadas de acuerdo con los requisitos del Título A del Reglamento, por el coeficiente de capacidad de disipación de energía $R (E_{=}F_{s}/R)$. El coeficiente de capacidad de disipación de energía, $R$ , es función de:

(a) El sistema de resistencia sísmica de acuerdo con la clasificación dada en el capítulo A.3,

(b) El grado de irregularidad de la edificación,

(c) La ausencia de redundancia según se especifica en A.3.3.8, y

(d) Los requisitos de diseño y detallado de cada tipo de mampostería estructural, para el grado de capacidad de disipación de energía correspondiente (DMI, DMO, o DES), tal como se especifica en el presente Título y en el capítulo A.3.

**D.5.3.1.2** — Otros efectos — Además de las combinaciones de cargas verticales y horizontales especificadas, se debe capacitar la estructura y sus partes para atender los efectos causados por contracción, expansión, flujo plástico, asentamientos previstos y condiciones ambientales de funcionamiento.

#### D.5.3.2 — DISTRIBUCIÓN DE FUERZA LATERAL

Las fuerzas laterales deben distribuirse al sistema estructural de acuerdo con la rigidez de los elementos y del diafragma de acuerdo con lo prescrito en el Título A del Reglamento.

**D.5.3.2.1** — Efecto de las aletas de la sección — Puede considerarse el incremento en la rigidez de los elementos por el efecto de aleta en muros que se intersectan monolíticamente. El ancho efectivo de aleta a cada lado (tipo T, $I$) no debe exceder 6 veces el espesor del muro intersectado. El ancho efectivo de aleta a un solo lado (tipo L, Z, C), no debe exceder 6 veces el espesor del muro intersectado. La aleta no se deben considerar en la resistencia a cortante.

**D.5.3.2.2** — Efectos torsionales — Las cargas laterales distribuidas deben tener en cuenta los efectos torsionales horizontales de asimetría en las cargas, las masas o la estructura, tal como lo establece el Título A del Reglamento.

#### D.5.3.3 — CARGAS CONCENTRADAS

Los siguientes aspectos referentes a cargas concentradas deben tenerse en cuenta en el análisis y diseño.

(a) Para el cálculo de los esfuerzos de aplastamiento, en aparejo trabado se debe tomar un área cuya profundidad es el espesor neto del elemento de apoyo y cuya longitud no puede ser mayor que el ancho de la pieza soportada más cuatro veces el espesor del apoyo, sin ser mayor que la distancia entre centros de las cargas concentradas. Para mampostería con aparejo de petaca, la longitud del área de cálculo se debe tomar como el tamaño de la unidad de mampostería en esa dirección.

(b) Los esfuerzos de aplastamiento bajo cargas concentradas mayoradas, evaluadas sobre el área especificada en el literal anterior, no deben exceder $φ0.85f_{m}'$ .

(c) Se considera que las cargas concentradas se distribuyen a un ángulo de 45o con la vertical en muros con aparejo trabado y de 30o en muros con aparejo de petaca.

#### D.5.3.4 — CARGA EXCÉNTRICA

Los esfuerzos que producen las cargas con excentricidad paralela o normal al plano del elemento estructural, deben considerarse en el diseño teniendo en cuenta su posición relativa al centro de rigidez de la sección neta. Todo esfuerzo que se produzca debe estar dentro de los límites establecidos en cada caso.

**D.5.3.4.1** — Apoyos provisionales — En la evaluación de los esfuerzos por cargas excéntricas, se debe tener en cuenta la condición transitoria de su acción y los efectos permanentes. Cuando los efectos por la acción transitoria se mitiguen por medio de apoyos provisionales, estos apoyos se deben especificar claramente en los planos de construcción.

### D.5.4 — CARACTERÍSTICAS DIMENSIONALES EFECTIVAS

#### D.5.4.1 — ÁREA EFECTIVA $(A_{e})$

El área efectiva a utilizar para el cálculo de los esfuerzos axiales debe ser la suma del área mínima de contacto entre el mortero de pega y la unidad de mampostería y el área inyectada. Cuando la junta de mortero sea ranurada el área efectiva debe reducirse proporcionalmente. En la mampostería confinada incluye el área de los elementos de confinamiento.

#### D.5.4.2 — ESPESOR EFECTIVO PARA EVALUAR EL EFECTO DE PANDEO $( t)$

El espesor efectivo $t$ a utilizar para el cálculo del coeficiente de reducción por pandeo, se debe tomar de la siguiente forma:

(a) Para muros sin machones o columnas de arriostramiento, el espesor efectivo es su espesor real.

(b) Para muros arriostrados a distancias regulares por machones integrados monolíticamente al muro, el espesor efectivo es el producto del espesor real del muro por el coeficiente de la tabla D.5.4-1

(c) Los muros de cavidad reforzada se deben asimilar para el efecto, a un solo muro con un espesor real medido entre los bordes externos del conjunto.

(d) En elementos de sección rectangular se debe considerar como espesor efectivo la dimensión de la sección en la dirección considerada. Para secciones no rectangulares se debe considerar como espesor efectivo en cada dirección el espesor de una sección rectangular de igual ancho e inercia equivalente.

**Tabla D.5.4-1**

Coeficientes para muros arriostrados por machones (*)

| Espaciamiento machón Espesor machón | Espesor machón Espesor muro |  |  |
|---|---|---|---|
|  | 1.0 | 2.0 | 3.0 |
| 6 ó menos | 1.0 | 1.4 | 2.0 |
| 8 | 1.0 | 1.3 | 1.7 |
| 10 | 1.0 | 1.2 | 1.4 |
| 15 | 1.0 | 1.1 | 1.2 |
| 20 ó más | 1.0 | 1.0 | 1.0 |

(*) Interpolar linealmente para valores intermedios.

#### D.5.4.3 — ALTURA EFECTIVA PARA EVALUAR EL EFECTO DE PANDEO $(h')$

La altura efectiva $h'$ de un elemento para el cálculo del coeficiente de reducción por pandeo se debe tomar de la siguiente forma:

(a) En elementos soportados lateralmente arriba y abajo en la dirección considerada, como la distancia libre entre apoyos.

(b) En elementos no soportados en un extremo en la dirección considerada, como el doble de la dimensión medida desde el apoyo.

(c) Cuando se justifique apropiadamente, se puede utilizar como altura efectiva una dimensión menor a la distancia libre entre apoyos.

**D.5.4.3.1** — La relación entre altura efectiva y espesor efectivo no puede ser superior a 25 en muros estructurales.

#### D.5.4.4 — ANCHO EFECTIVO $( b)$

El ancho efectivo para ser empleado en los cálculos de la resistencia a flexión y flexo-compresión de muros de mampostería construidos con unidades de perforación vertical, debe tomarse de la siguiente manera:

**D.5.4.4.1** — Ancho efectivo $b$ para flexión perpendicular al plano del muro — Cuando la dirección de las fuerzas horizontales es perpendicular al plano del muro, e inducen flexión o flexo-compresión con respecto a un eje paralelo al muro, el ancho efectivo $b$ que se debe tomar para efectos de diseñar la sección es, para aparejo trabado, la mayor entre 6 veces el ancho nominal del muro y la distancia centro a centro entre refuerzos verticales; y para aparejo en petaca, la mayor entre 3 veces el ancho nominal del muro y la distancia centro a centro entre refuerzos verticales. En la mampostería con todas sus celdas inyectadas, la sección se considera sólida y no hay necesidad de aplicar las reducciones indicadas anteriormente.

**D.5.4.4.2** — Ancho efectivo $b$ para flexión paralela al plano del muro — Cuando la dirección de las fuerzas horizontales es paralela al plano del muro, e inducen flexión o flexo-compresión con respecto a un eje perpendicular al plano del muro, el ancho efectivo $b$ que se debe tomar para efectos de diseñar la sección es igual al ancho sólido promedio del muro. El ancho efectivo $b$ , corresponde al área efectiva dividida por la longitud horizontal del muro $b=A_{e}/ℓ_{w}$.

#### D.5.4.5 — ÁREA EFECTIVA PARA DETERMINAR ESFUERZOS CORTANTES $(A_{mv})$

El área efectiva para calcular esfuerzos cortantes en muros de mampostería construidos con unidades de perforación vertical, debe tomarse de la siguiente manera:

**D.5.4.5.1** — Área efectiva $A_{mv}$ para cortante en la dirección perpendicular al plano del muro — Cuando la dirección de la fuerza horizontal es perpendicular al plano del muro, e induce esfuerzos cortantes en esa dirección, el área efectiva para cortante es igual a $A_{e}(A_{mv}=A_{e})$, excepto cuando se emplea mortero de pega sólo en las paredes laterales de la unidad de perforación vertical, véase D.4.5.10.1(b), caso en el cual $A_{mv}$ corresponde a la suma de las porciones del muro inyectadas con mortero de relleno, incluyendo las paredes de las unidades de mampostería que las circundan y que tienen mortero de pega.

**D.5.4.5.2** — Área efectiva $A_{mv}$ para cortante en la dirección paralela al plano del muro — Cuando la dirección de las fuerzas horizontales es paralela al plano del muro, e induce esfuerzos cortantes en esa dirección, sólo el alma de la sección resiste esfuerzos cortantes y $A_{mv}$ es el área neta del alma de la sección.

Generalmente $A_{mv}=bℓ_{w}$, siendo $b$ el ancho efectivo del alma. No obstante, cuando hay concentraciones de celdas inyectadas con mortero de relleno en los extremos del muro, el ancho efectivo para este propósito debe calcularse en la zona central del alma.

#### D.5.4.6 — DISTANCIA ENTRE APOYOS EN VIGAS Y DINTELES

Para vigas y dinteles la distancia máxima entre apoyos que les den soporte lateral debe ser de 32 veces el ancho efectivo.

#### D.5.4.7 — RIGIDEZ MÍNIMA A FLEXIÓN EN VIGAS Y DINTELES

La rigidez mínima a flexión de un elemento debe ser tal que no se produzcan flechas elásticas mayores a $ℓ/500$ bajo la totalidad de las cargas verticales de diseño sin mayorar.

#### D.5.4.8 — VIGAS DE SECCIÓN ALTA

Las vigas que tengan relaciones de longitud/altura menores de 1.25 en luces simples y menores de 2.5 en luces continuas, se deben diseñar teniendo en cuenta relaciones no lineales en la distribución de esfuerzos en la sección.

### D.5.5 — RESISTENCIA PARA CARGA AXIAL DE COMPRESIÓN

#### D.5.5.1 — MÁXIMA RESISTENCIA AXIAL TEÓRICA

La máxima resistencia axial teórica del muro sometido a carga axial sin excentricidad, $P_{o}$ , se obtiene por medio de la siguiente expresión:

$$ P_o = 0.80f'_m \left( A_e - A_{st} \right) + A_{st} f_y \le f'_m A_e \tag{D.5.5-1} $$

#### D.5.5.2 — REDUCCIÓN DE RESISTENCIA AXIAL POR ESBELTEZ

El efecto de la esbeltez del muro en la resistencia nominal para carga axial se obtiene por medio del parámetro $R_{e}$ :

$$ R_e = 1-\left[\dfrac{h'}{42t}\right]^2 \quad \text{para } h'/t \le 30 \tag{D.5.5-2} $$

$$ R_e = \left[\dfrac{21t}{h'}\right]^2 \quad \text{para } h'/t > 30 $$

#### D.5.5.3 — RESISTENCIA NOMINAL PARA CARGA AXIAL

La resistencia nominal para carga axial de compresión $P_{n}$ , sin excentricidad y teniendo en cuenta los efectos de esbeltez, no puede ser mayor que el valor dado a continuación:

$$ P_n = 0.80P_o R_e \tag{D.5.5-3} $$

#### D.5.5.4 — MÁXIMA RESISTENCIA DE DISEÑO PARA CARGA AXIAL

La máxima resistencia de diseño para carga axial de compresión $P_{u}$ , sin excentricidad y teniendo en cuenta los efectos de esbeltez, está dada por la siguiente expresión

$$ P_u \le \phi P_n = \phi 0.80P_o R_e \tag{D.5.5-4} $$

### D.5.6 — RESISTENCIA A FLEXIÓN SIN CARGA AXIAL

#### D.5.6.1 — GENERAL

Cuando la sección del muro esta sometida a momento flector sin la presencia de carga axial, se debe cumplir la siguiente condición:

$$ M_u \le \phi M_n \tag{D.5.6-1} $$

#### D.5.6.2 — SECCIONES SOLO CON REFUERZO A TRACCIÓN

Cuando la sección del muro esta simplemente reforzada, y su cuantía es menor del 75% de la cuantía para condiciones balanceadas, la resistencia nominal a flexión $M_{n}$ , se puede obtener por medio de la ecuación (D.5.6-2).

$$ M_n = A_s f_y \left( d - \dfrac{a}{2} \right) \tag{D.5.6-2} $$

y

$$ a = \dfrac{A_s f_y}{0.80f'_m b} \tag{D.5.6-3} $$

#### D.5.6.3 — SECCIONES CON REFUERZO A COMPRESIÓN

Cuando la sección del muro tiene refuerzo que trabaja a compresión, y se puede probar que el refuerzo a compresión está en fluencia, la resistencia nominal a flexión $M_{n}$ , se puede obtener por medio de la ecuación D.5.6-4.

$$ M_n = A_{s1} f_y \left( d - \dfrac{a}{2} \right) + A_{s2} f_y \left( d - d' \right) \tag{D.5.6-4} $$

### D.5.7 — DISEÑO DE MUROS EN LA DIRECCIÓN PERPENDICULAR A SU PLANO

#### D.5.7.1 — GENERAL

Los requisitos de esta sección se emplean para el diseño por el método del estado límite de resistencia, de muros de mampostería estructural de unidades de perforación vertical y de cavidad reforzada para el efecto de las cargas horizontales perpendiculares al plano del muro, además de las fuerzas verticales que actúan sobre el muro.

#### D.5.7.2 — RESISTENCIA A FLEXIÓN PARA MUROS CON CARGA AXIAL MENOR QUE $0.10f_{m} 'A_{e}$

Cuando la carga axial que actúa sobre el muro $P_{u}$ en la sección bajo estudio es menor que $0.10f_{m} 'A_{e}$, el momento de diseño solicitado, $M_{u}$ , debe cumplir la condición dada por la ecuación D.5.7-1:

$$ M_u \le \phi R_e M_n \tag{D.5.7-1} $$

donde $R_{e}$ está dado por la ecuación D.5.5-2, y $M_{n}$ se obtiene por medio de:

$$ M_n = A_{se} f_y \left( d - \dfrac{a}{2} \right) \tag{D.5.7-2} $$

$$ A_{se} = \dfrac{A_s f_y + P_u}{f_y} \tag{D.5.7-3} $$

y

$$ a = \dfrac{A_s f_y + P_u}{0.80f'_m b} \tag{D.5.7-4} $$

y la cuantía de refuerzo a flexión, $ρ =A_{s}/(bd)$ no debe exceder $0.5ρ_{b}$ .

#### D.5.7.3 — RESISTENCIA A FLEXIÓN PARA MUROS CON CARGA AXIAL MAYOR QUE $0.10f_{m} 'A_{e}$

Cuando la carga axial que actúa sobre el muro $P_{u}$ en la sección bajo estudio es mayor que $0.10f_{m} 'A_{e}$, la relación de esbeltez del muro $h '/t$ no debe ser mayor que 30, y el momento de diseño solicitado, $M_{u}$ , que acompaña la carga axial $P_{u}$ , debe cumplir la condición dada por la ecuación D.5.7-5:

$$ M_u \le \phi R_e M_n \tag{D.5.7-5} $$

donde $R_{e}$ está dado por la ecuación D.5.5-2, y $M_{n}$ se obtiene teniendo en cuenta la interacción entre momento y carga axial, de acuerdo con los principios enunciados en D.5.1.6 y empleando el coeficiente de reducción de resistencia, $φ$ , apropiado de los dados en D.5.1.5.1.

#### D.5.7.4 — RESISTENCIA A CORTANTE EN LA DIRECCIÓN PERPENDICULAR AL PLANO DEL MURO

Se debe cumplir la siguiente condición con respecto a la fuerza cortante que actúa en la dirección perpendicular al plano del muro:

$$ V_u \le \phi V_n \tag{D.5.7-6} $$

donde:

$$ V_n = \dfrac{1}{6} A_{mv} \sqrt{f'_m} \tag{D.5.7-7} $$

donde $A_{mv}$ está definido en D.5.4.5.1 y el valor del coeficiente de reducción de resistencia, $φ$ , está dado en D.5.1.5.1.

### D.5.8 — DISEÑO DE MUROS EN LA DIRECCIÓN PARALELA A SU PLANO

#### D.5.8.1 — GENERAL

Los requisitos de esta sección se emplean para el diseño por el método del estado límite de resistencia, de muros de mampostería estructural de unidades de perforación vertical y de cavidad reforzada para el efecto de las cargas horizontales paralelas al plano del muro, además de las fuerzas verticales que actúan sobre el muro.

#### D.5.8.2 — RESISTENCIA MÍNIMA A LA FLEXIÓN

Cuando el modo de falla dominante del muro es la flexión, la resistencia nominal a flexión del muro $M_{n}$ , debe cumplir la siguiente relación:

$$ M_n \ge \alpha M_{cr} \tag{D.5.8-1} $$

donde $α =1.8$ para mampostería con todas sus celdas inyectadas con mortero de relleno, $α =3.0$ para mampostería donde solo están inyectadas las celdas que contienen refuerzo y $α =3.0$ para mampostería de cavidad reforzada.

$M_{cr}$es el momento de agrietamiento, el cual se obtiene por medio de la ecuación D.5.8-2.

$$ M_{cr} = \dfrac{b\ell_w^2}{6} f_r \tag{D.5.8-2} $$

El módulo de ruptura de la mampostería, $f_{r}$, se obtiene de la tabla D.5.8-1:

**Tabla D.5.8-1**

Módulo de ruptura, $f_{r}$ (MPa)

| Dirección de los esfuerzos de tracción por flexión y tipo de mampostería. | Morteros de cemento portland y cal |  | Morteros de cemento para mampostería |  |
|---|---|---|---|---|
|  | H, M, ó S | N | H, M, ó S | N |
| Perpendicular a las juntas horizontales |  |  |  |  |
| - Unidades Macizas | 0.69 | 0.52 | 0.41 | 0.26 |
| - Unidades de perforación vertical(1) - Sin rellenar | 0.43 | 0.33 | 0.26 | 0.16 |
| - Rellenas con morteros de inyección | 1.12 | 1.09 | 1.06 | 1.00 |
| Perpendicular a la junta vertical |  |  |  |  |
| - Unidades Macizas | 1.38 | 1.03 | 0.83 | 0.52 |
| - Unidades de perforación vertical - Sin rellenar | 0.86 | 0.66 | 0.52 | 0.33 |
| - Rellenas y parcialmente rellenas con morteros de inyección | 1.38 | 1.03 | 0.83 | 0.52 |

(1)Para mampostería parcialmente inyectada, el módulo de ruptura deberá ser determinado por interpolación lineal de los valores dados para las unidades de perforación vertical sin rellenar y las rellenas con mortero de relleno basada en la cantidad (porcentaje) relleno con mortero de relleno.

#### D.5.8.3 — RESISTENCIA A LA FLEXO-COMPRESIÓN

El momento de diseño solicitado, $M_{u}$ , que acompaña la carga axial $P_{u}$ , debe cumplir la condición dada por la ecuación D.5.8-2, para el nivel de carga $P_{u}$ :

$$ M_u \le \phi M_n \tag{D.5.8-3} $$

$M_{n}$ se obtiene teniendo en cuenta la interacción entre momento y carga axial, de acuerdo con los principios enunciados en D.5.1.6, los cuales permiten calcular un diagrama de interacción del muro, empleando el coeficiente de reducción de resistencia, $φ$ , apropiado de los dados en D.5.1.5.2, el cual, a su vez, depende del nivel de carga axial.

<!-- mod:2-decreto-340-2012-33 -->
> **Modificación — Decreto 340 de 2012** · anexo, p. 7
>
> En D.5.8.3 la referencia a la ecuación D.5.8-2 debe ser a la ecuación D.5.8-3.

#### D.5.8.4 — RESISTENCIA A CORTANTE EN LA DIRECCIÓN PARALELA AL PLANO DEL MURO

Se debe cumplir la siguiente condición con respecto a la fuerza cortante que actúa en la dirección paralela al plano del muro:

$$ V_u \le \phi V_n \tag{D.5.8-4} $$

y

$$ V_n = V_m + V_s \tag{D.5.8-5} $$

Si $V_{u}≥φV_{m}$, el refuerzo debe tomar todo el esfuerzo cortante, y entonces:

En las ecuaciones anteriores, $V_{m}$ se calcula de acuerdo con lo indicado en D.5.8.4.2 y $V_{s}$ de acuerdo con D.5.8.4.3.

Además, el cortante nominal total, $V_{n}$ dado por la ecuación D.5.8-5 no puede exceder en ninguna sección horizontal del muro el valor dado en D.5.8.4.4.

**D.5.8.4.1** — Verificación de articulación plástica — Si el cortante nominal del muro, $V_{n}$ , excede el cortante que se produce con la resistencia nominal a flexión del muro, $M_{n}$ , existe la posibilidad de que se desarrolle una articulación plástica en la base del muro y deben adoptarse precauciones especiales dentro de una región que va desde la base del muro hasta una altura igual a $ℓ_{w}$. Todas las secciones dentro de esta región deben tener una resistencia nominal al cortante igual a:

$$ V_n = V_s \tag{D.5.8-6} $$

La resistencia al corte requerida, $V_{u}$ , para esta región puede determinarse con base en el momento resistente $M_{n}$ en una sección localizada a una altura igual a $ℓ_{w} /2$, pero no más de medio piso, por encima de la base del muro. La separación, $s$ , del refuerzo horizontal de cortante dentro de esta región comprendida entre la base y una altura igual a $ℓ_{w}$, no puede exceder tres veces el ancho nominal del muro, $t$ , ni 600 mm.

En el resto del muro hacia arriba, la resistencia nominal al cortante puede determinarse por medio de la ecuación D.5.8-5.

**D.5.8.4.2** — Valor de $V_{m}$ — El cortante nominal resistido por la mampostería, $V_{m}$ , se calcula utilizando las expresiones dadas en la tabla D.5.8-2, donde $M_{u}$ es el momento que ocurre simultáneamente con $V_{u}$ en la sección bajo consideración, y $d$ puede tomarse como $0.8ℓ_{w}$ en ausencia de un análisis de compatibilidad de deformaciones. $A_{mv}$ está definida en D.5.4.5.2. El cociente $M_{u}/(V_{u} d)$ debe tomarse siempre como positivo y no hay necesidad que sea mayor que la unidad.

**Tabla D.5.8-2**

Valor del cortante nominal resistido por la mampostería, $V_{m}$

| $M_{u}$ $V_{u} d$ | $V_{m}$ |
|---|---|
| $M_{u}$ $V_{u} d ≤0.25$ | $V_{m}=0.30A_{mv}\sqrt{f_{m}'}+0.25P_{u}$ |
| $M_{u}$ $V_{u} d ≥1.00$ | $V_{m}=0.20A_{mv}\sqrt{f_{m}'}+0.25P_{u}$ |

$$ 0.25 < \dfrac{M_u}{V_u d} < 1.00 \qquad V_m = \left[ 0.33 - 0.13 \left( \dfrac{M_u}{V_u d} \right) \right] A_{mv} \sqrt{f'_m} + 0.25P_u $$

**D.5.8.4.3** — Valor de $V_{s}$ — El cortante nominal resistido por el refuerzo horizontal de cortante, $V_{s}$ , se calcula utilizando la ecuación D.5.8-7:

$$ V_s = \rho_n f_y A_{mv} \tag{D.5.8-7} $$

donde $f_{y}$ es la resistencia a la fluencia del refuerzo de cortante, y $ρ_{n}$ es la cuantía del refuerzo que contribuye a resistir la fuerza cortante, calculada de acuerdo con la ecuación D.5-8-8:

$$ \rho_n = \dfrac{A_v}{sb} \eta \tag{D.5.8-8} $$

$η$ = Factor de eficiencia del refuerzo horizontal.

$A_{v}$ es el área de refuerzo horizontal que resiste cortante, espaciado una separación $s$ medida verticalmente.

Cuando $A_{v}$ es colocado dentro de elementos horizontales embebidos dentro del muro, como se describe en D.4.5.11.2 .............................................................................$η$ = 0.70 Cuando $A_{v}$, es el refuerzo horizontal de junta descrito en D.4.5.11.1 .................................$η$ = 0.35

**D.5.8.4.4** — Valores máximos de $V_{n}$ – El cortante nominal, $V_{n}$ , no puede exceder los valores dados en la tabla D.5.8-3, donde $M_{u}$ es el momento que ocurre simultáneamente con $V_{u}$ en la sección bajo consideración, y $d$ puede tomarse como $0.8ℓ_{w}$ en ausencia de un análisis de compatibilidad de deformaciones. El cociente $M_{u}/(V_{u} d)$ debe tomarse siempre como positivo y no hay necesidad que sea mayor que la unidad.

**Tabla D.5.8-3**

Valores máximos para el cortante nominal $V_{n}$

| $M_{u}$ $V_{u} d$ | máximo valor permitido para $V_{n}$ |
|---|---|
| $M_{u}$ $V_{u} d ≤0.25$ | $0.50A_{mv}\sqrt{f_{m}'}$ |
| $M_{u}$ $V_{u} d ≥1.00$ | $0.33A_{mv}\sqrt{f_{m}'}$ |

$$ 0.25 < \dfrac{M_u}{V_u d} < 1.00 \qquad \left[ 0.56 - 0.23 \left( \dfrac{M_u}{V_u d} \right) \right] A_{mv} \sqrt{f'_m} $$

#### D.5.8.5 — ELEMENTOS DE BORDE

Se deben utilizar elementos de borde en los muros de mampostería de unidades de perforación vertical y de mampostería de cavidad reforzada, cuando el modo de falla del muro sea en flexión y el esfuerzo de compresión de la fibra extrema en condiciones de cargas mayoradas exceda $0.20f_{m}'$ para mampostería de cavidad reforzada como se define en D.2.1.1 y para mampostería reforzada como se define en D.2.1.2, y cuando exceda $0.30f_{m}'$ para mampostería parcialmente reforzada como se define en D.2.1.3. Deben cumplirse además los siguientes requisitos:

(a) Los elementos de borde se pueden suspender a partir de la sección en la que el esfuerzo de compresión sea inferior a $0.15f_{m}'$ , pero no deben suspenderse antes de llegar a una altura igual a $ℓ_{w}$, medida desde la base del muro.

(b) Los esfuerzos se calculan para las fuerzas mayoradas, utilizando un modelo linealmente elástico y considerando la sección como no fisurada.

(c) Los elementos de borde deben tener estribos de confinamiento de diámetro N° 3 (3/8”) ó 10M (10 mm), separados verticalmente a 200 mm, o su equivalente, dentro del espacio inyectado con mortero de relleno. Las celdas deben tener como mínimo 100 mm x 100 mm.

(d) En muros de cavidad reforzada, los elementos de borde deben cumplir con lo especificado para muros de concreto en C.21.9.6.

█
