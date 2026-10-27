# A.5 — Método del análisis dinámico

### A.5.0 — NOMENCLATURA

$E$ = fuerzas sísmicas reducidas de diseño $(E=F_{s}/R)$

$F_{s}$ = fuerzas sísmicas, véase A.3.1.1.

$g$ = aceleración debida a la gravedad ($9.8$ m/s²).

$M$ = masa total de la edificación — $M$ debe ser igual a la masa total de la estructura más la masa de aquellos elementos tales como muros divisorios y particiones, equipos permanentes, tanques y sus contenidos, etc.

En depósitos o bodegas debe incluirse además un 25 por ciento de la masa correspondiente a los elementos que causan la carga viva del piso. Capítulos A.4 y A.5 (en kg).

$M_{j}$ = masa actuante total de la edificación en la dirección $j$. Ecuación A.5.4-1.

$M_{m}$= masa efectiva modal del modo $m$ , determinada de acuerdo con la ecuación A.5.4-2.

$m_{i}$ , $m_{x}$ = parte de $M$ que está colocada en el nivel $i$ o $x$ , respectivamente.

$p$ = número total de modos utilizado en el análisis modal de la estructura.

$R_{0}$ = coeficiente de capacidad de disipación de energía básico definido para cada sistema estructural y cada grado de capacidad de disipación de energía del material estructural. Capítulo A.3.

$R$ = coeficiente de capacidad de disipación de energía para ser empleado en el diseño, corresponde al coeficiente de disipación de energía básico, $R_{0}$ , multiplicado por los coeficientes de reducción de capacidad de disipación de energía por irregularidades en altura, en planta, y por ausencia de redundancia en el sistema estructural de resistencia sísmica $(R= φ_{a} φ_{p} φ_{r}R_{0})$.

$S_{am}$= valor del espectro de aceleraciones de diseño para el período de vibración $T_{m}$, correspondiente al modo de vibración $m$ .

$T_{a}$ = período de vibración fundamental aproximado, en segundos, calculado de acuerdo con A.4.2.

$T_{m}$= período de vibración correspondiente al modo de vibración $m$ , en s.

$V_{mj}$= cortante sísmico en la base correspondiente al modo $m$ en la dirección horizontal $j$.

$V_{s}$ = cortante sísmico de diseño en la base de la estructura, calculado por el método de la fuerza horizontal equivalente del Capítulo A.4.

$V_{tj}$ = cortante sísmico en la base total en la dirección horizontal $j$.

$φ^{m}_{ij}$= amplitud de desplazamiento del nivel $i$ , en la dirección $j$, cuando está vibrando en el modo $m$ .

### A.5.1 — GENERAL

**A.5.1.1** — Los métodos de análisis dinámico deben cumplir los requisitos de este Capítulo y los demás del presente título del Reglamento.

**A.5.1.2** — Los métodos de análisis dinámico pueden utilizarse en el diseño sísmico de todas las edificaciones cubiertas por este Reglamento y deben utilizarse en el diseño de las edificaciones indicadas en A.3.4.2.2.

**A.5.1.3** — Los resultados obtenidos utilizando los métodos de análisis dinámico deben ajustarse a los valores mínimos prescritos en este Capítulo para cada uno de ellos. Los valores mínimos a los cuales deben ajustarse están referidos a los valores que se obtienen utilizando el método de la fuerza horizontal equivalente presentado en el Capítulo A.4. (Véase A.5.4.5).

**A.5.1.4** — Todas las metodologías de análisis dinámico que se utilicen deben estar basadas en principios establecidos de la mecánica estructural, que estén adecuadamente sustentados analítica o experimentalmente.

**A.5.1.5** — El ingeniero diseñador debe asegurarse que los procedimientos de análisis dinámico, manuales o electrónicos, que utilice, cumplen los principios de la mecánica estructural y en especial los requisitos del presente Capítulo. El Reglamento no exige un procedimiento determinado y deja en manos del diseñador su selección y por ende la responsabilidad de que se cumplan los principios enunciados aquí. Es responsabilidad del diseñador garantizar que los procedimientos electrónicos, si son utilizados, describan adecuadamente la respuesta dinámica de la estructura tal como la prescriben los requisitos del presente Capítulo.

### A.5.2 — MODELO MATEMÁTICO

#### A.5.2.1 — MODELO MATEMÁTICO A EMPLEAR

El modelo matemático de la estructura debe describir la distribución espacial de la masa y la rigidez de toda la estructura, de tal manera que sea adecuado para calcular las características relevantes de la respuesta dinámica de la misma. Como mínimo debe utilizarse uno de los siguientes procedimientos:

**A.5.2.1.1** — Modelo tridimensional con diafragma rígido — En este tipo de modelo los entrepisos se consideran diafragmas infinitamente rígidos en su propio plano. La masa de cada diafragma se considera concentrada en su centro de masa. Los efectos direccionales pueden ser tomados en cuenta a través de las componentes apropiadas de los desplazamientos de los grados de libertad horizontales ortogonales del diafragma. Este procedimiento debe utilizarse cuando se presentan irregularidades en planta del tipo 1aP, 1bP, 4P o 5P, tal como las define A.3.3.4 (tabla A.3-6), y en aquellos casos en los cuales, a juicio del ingeniero diseñador, este es el procedimiento más adecuado.

**A.5.2.1.2** — Modelo tridimensional con diafragma flexible — En este tipo de modelo se considera que las masas aferentes a cada nudo de la estructura pueden desplazarse y girar en cualquier dirección horizontal o vertical. La rigidez de los elementos estructurales del sistema de resistencia sísmica se describe tridimensionalmente. El diafragma se representa por medio de elementos que describan adecuadamente su flexibilidad. Este procedimiento debe utilizarse cuando no existe un diafragma propiamente dicho, cuando el diafragma es flexible en comparación con los elementos estructurales verticales del sistema estructural de resistencia sísmica, o cuando se presentan irregularidades en planta del tipo 2P o 3P, tal como las define A.3.3.4 (tabla A.3-6), y en aquellos casos en los cuales, a juicio del ingeniero diseñador, éste es el procedimiento más adecuado.

**A.5.2.1.3** — Modelos limitados a un plano vertical — En este tipo de modelo la respuesta de la estructura se limita a movimientos horizontales en una sola dirección. Este modelo se permite en todos los casos que no están cubiertos por A.5.2.1.1. y A.5.2.1.2. Los efectos torsionales de los pisos deben evaluarse independientemente y adicionarse a los valores obtenidos del análisis en un plano cuando el diafragma es rígido y pueden despreciarse cuando el diafragma es flexible. De igual manera los efectos producidos por la dirección de incidencia de los movimientos sísmicos del terreno deben evaluarse por separado y adicionarse a los valores obtenidos del análisis dinámico.

**A.5.2.1.4** — Otros modelos — Si a juicio del ingeniero diseñador las características de rigidez o de masa de la estructura lo requieren, se permite el uso de modelos de análisis inelástico dinámico o de métodos alternos, tal como lo indica A.3.4.1.

#### A.5.2.2 — MASA DE LA EDIFICACIÓN

Las masas de la edificación que se utilicen en el análisis dinámico deben ser representativas de las masas que existirán en la edificación cuando ésta se vea sometida a los movimientos sísmicos de diseño. Para efectos de los requisitos de este Reglamento, la masa total de la edificación se puede tomar como $M .$ La distribución de la masa de la edificación debe representar la distribución real de las distintas masas de la edificación.

#### A.5.2.3 — RIGIDEZ EN LOS MÉTODOS DINÁMICOS ELÁSTICOS

La rigidez que se utilice en los elementos estructurales del sistema de resistencia sísmica cuando se empleen métodos dinámicos elásticos, debe seleccionarse cuidadosamente y debe ser representativa de la rigidez cuando éstos se vean sometidos a los movimientos sísmicos de diseño. En las estructuras de concreto y mampostería, la rigidez que se asigne debe ser consistente con el grado de fisuración que puedan tener los diferentes elementos al verse sometidos a las deformaciones que imponen los movimientos sísmicos de diseño. Cuando haya variaciones apreciables en la rigidez de los diferentes elementos verticales del sistema de resistencia sísmica que contribuyen a la resistencia de las mismas componentes del movimiento, la rigidez que se le asigne a cada uno de ellos debe ser consistente con los niveles de deformación.

#### A.5.2.4 — RIGIDEZ EN LOS MÉTODOS DINÁMICOS INELÁSTICOS

Los modelos matemáticos utilizados para describir la rigidez de los elementos estructurales del sistema de resistencia sísmica, cuando se empleen métodos dinámicos inelásticos, deben ser consistentes con el grado de capacidad de disipación de energía del material, con los niveles esperados de deformación y con las secuencias de esfuerzos y deformaciones que se presenten durante la respuesta, a través de modelos histeréticos que describan la degradación de rigidez y resistencia, los efectos de estrangulamiento de las formas histeréticas, y los efectos del endurecimiento por deformación del acero. Los modelos de rigidez utilizados deben estar adecuadamente sustentados analítica o experimentalmente.

### A.5.3 — REPRESENTACIÓN DE LOS MOVIMIENTOS SÍSMICOS

#### A.5.3.1 — GENERALIDADES

De acuerdo con la representación de los movimientos sísmicos de diseño empleada en el análisis dinámico, los procedimientos se dividen en:

(a) Procedimientos espectrales, y

(b) Procedimientos de análisis cronológico.

#### A.5.3.2 — PROCEDIMIENTOS ESPECTRALES

En los procedimientos espectrales debe utilizarse el espectro de diseño definido en A.2.6.

#### A.5.3.3 — PROCEDIMIENTOS CRONOLÓGICOS

En los procedimientos cronológicos deben utilizarse familias de acelerogramas, tal como las define A.2.7.

### A.5.4 — ANÁLISIS DINÁMICO ELÁSTICO ESPECTRAL

#### A.5.4.1 — METODOLOGÍA DEL ANÁLISIS

Deben tenerse en cuenta los siguientes requisitos, cuando se utilice el método de análisis dinámico elástico espectral:

(a) Obtención de los modos de vibración — Los modos de vibración deben obtenerse utilizando metodologías establecidas de dinámica estructural. Deben utilizarse todos los modos de vibración de la estructura que contribuyan de una manera significativa a la respuesta dinámica de la misma, cumpliendo los requisitos de A.5.4.2.

(b) Respuesta espectral modal — La respuesta máxima de cada modo se obtiene utilizando las ordenadas del espectro de diseño definido en A.5.3.2, para el período de vibración propio del modo.

(c) Respuesta total — Las respuestas máximas modales, incluyendo las de deflexiones, derivas, fuerzas en los pisos, cortantes de piso, cortante en la base y fuerzas en los elementos, se combinan de una manera estadística para obtener la respuesta total de la estructura a los movimientos sísmicos de diseño. Deben cumplirse los requisitos de A.5.4.4 en la combinación estadística de las respuestas modales máximas.

(d) Ajuste de los resultados — Si los resultados de la respuesta total son menores que los valores mínimos prescritos en A.5.4.5, los resultados totales del análisis dinámico deben ser ajustados como se indica allí.

El ajuste debe cubrir todos los resultados del análisis dinámico, incluyendo las deflexiones, derivas, fuerzas en los pisos, cortantes de piso, cortante en la base y fuerzas en los elementos.

(e) Evaluación de las derivas — Se debe verificar que las derivas totales obtenidas, debidamente ajustadas de acuerdo con los requisitos de A.5.4.5, no excedan los límites establecidos en el Capítulo A.6.

(f) Fuerzas de diseño en los elementos — Las fuerzas sísmicas internas totales de los elementos, $F_{s}$ , debidamente ajustadas de acuerdo con los requisitos de A.5.4.5, se dividen por el valor del coeficiente de capacidad de disipación de energía, $R$ , del sistema de resistencia sísmica, modificado de acuerdo con la irregularidad y la ausencia de redundancia según los requisitos de A.3.3.3, para obtener las fuerzas sísmicas reducidas de diseño, $E$ , y se combinan con las otras cargas prescritas por este Reglamento, de acuerdo con el Título B.

(g) Diseño de los elementos estructurales — Los elementos estructurales se diseñan y detallan siguiendo los requisitos propios del grado de capacidad de disipación de energía correspondiente del material, de acuerdo con los requisitos del Capitulo A.3.

#### A.5.4.2 — NÚMERO DE MODOS DE VIBRACIÓN

Deben incluirse en el análisis dinámico todos los modos de vibración que contribuyan de una manera significativa a la respuesta dinámica de la estructura. Se considera que se ha cumplido este requisito cuando se demuestra que, con el número de modos empleados, $p$ , se ha incluido en el cálculo de la respuesta, de cada una de las direcciones horizontales de análisis, $j$, por lo menos el 90 por ciento de la masa participante de la estructura. La masa participante, $M_{j}$ , en cada una de las direcciones de análisis, $j$, para el número de modos empleados, $p$ , se determina por medio de las siguientes ecuaciones:

$$ \bar{M}_j = \sum_{m=1}^{p} \bar{M}_{mj} \ge 0.90\,M \tag{A.5.4-1} $$

$$ \bar{M}_{mj} = \dfrac{\left(\sum_{i=1}^{n} m_i\,\phi_{ij}^{m}\right)^2}{\sum_{i=1}^{n} m_i \left(\phi_{ij}^{m}\right)^2} \tag{A.5.4-2} $$

#### A.5.4.3 — CÁLCULO DEL CORTANTE MODAL EN LA BASE

La parte del cortante en la base contribuida por el modo $m$ en la dirección horizontal $j$, $V_{mj}$, debe determinarse de acuerdo con la siguiente ecuación:

$$ V_{mj} = S_{am}\,g\,\bar{M}_{mj} \tag{A.5.4-3} $$

donde $M_{mj}$ está dado por la ecuación A.5.4-2, y $S_{am}$ es el valor leído del espectro elástico de aceleraciones, $S_{a}$ , para el período de vibración $T_{m}$ correspondiente al modo de vibración $m$ . El cortante modal total en la base, $V_{tj}$ , en la dirección $j$ se obtiene combinando los cortantes contribuidos por cada modo, $V_{mj}$, en la misma dirección de acuerdo con el procedimiento de A.5.4.4.

#### A.5.4.4 — COMBINACIÓN DE LOS MODOS

Las respuestas máximas obtenidas para cada modo, $m$ , de las deflexiones, derivas, fuerzas en los pisos, cortantes de piso, cortante en la base y fuerzas en los elementos, deben combinarse utilizando métodos apropiados y debidamente sustentados, tales como el de la raíz cuadrada de la suma de los cuadrados u otros. Debe tenerse especial cuidado cuando se calculen las combinaciones de las derivas, calculando la respuesta máxima de la deriva causada por cada modo independientemente y combinándolas posteriormente. No es permitido obtener las derivas totales a partir de deflexiones horizontales que ya han sido combinadas. Cuando se utilicen modelos matemáticos de análisis tridimensional deben tenerse en cuenta los efectos de interacción modal, tales como la combinación cuadrática total.

#### A.5.4.5 — AJUSTE DE LOS RESULTADOS

El valor del cortante dinámico total en la base, $V_{tj}$ , obtenido después de realizar la combinación modal, para cualquiera de las direcciones de análisis, $j$, no puede ser menor que el 80 por ciento para estructuras regulares, o que el 90 por ciento para estructuras irregulares, del cortante sísmico en la base, $V_{s}$ , calculado por el método de la fuerza horizontal equivalente del Capítulo A.4. Además, se deben cumplir las siguientes condiciones:

(a) Para efectos de calcular este valor de $V_{s}$ el período fundamental de la estructura obtenido en el análisis dinámico, $T$ en segundos no debe exceder $C_{u} T_{a}$ , de acuerdo con los requisitos del Capítulo A.4, y cuando se utilicen los procedimientos de interacción suelo-estructura se permite utilizar el valor de $V_{s}$ reducido por esta razón.

(b) Cuando el valor del cortante dinámico total en la base, $V_{tj}$ , obtenido después de realizar la combinación modal, para cualquiera de las direcciones de análisis, $j$, sea menor que el 80 por ciento para estructuras regulares, o que el 90 por ciento para estructura irregulares, del cortante sísmico en la base, $V_{s}$ , calculado como se indicó en (a), todos los parámetros de la respuesta dinámica, tales como deflexiones, derivas, fuerzas en los pisos, cortantes de piso, cortante en la base y fuerzas en los elementos de la correspondiente dirección $j$ deben multiplicarse por el siguiente factor de modificación:

$$ 0.80\,\dfrac{V_s}{V_{tj}} \quad \text{para estructuras regulares} \tag{A.5.4-4} $$

$$ 0.90\,\dfrac{V_s}{V_{tj}} \quad \text{para estructuras irregulares} \tag{A.5.4-5} $$

(c) Cuando el cortante sísmico en la base, $V_{tj}$ , obtenido después de realizar la combinación modal, para cualquiera de las direcciones principales, excede los valores prescritos en (a), todos los parámetros de la respuesta dinámica total, tales como deflexiones, derivas, fuerzas en los pisos, cortantes de piso, cortante en la base y fuerzas en los elementos, pueden reducirse proporcionalmente, a juicio del diseñador.

#### A.5.4.6 — EFECTOS DIRECCIONALES

Los efectos direccionales de los movimientos sísmicos de diseño deben tenerse en cuenta de acuerdo con los requisitos de A.3.6.3. Los efectos de la aceleración vertical de los movimientos sísmicos en los voladizos y elementos preesforzados debe tenerse en cuenta siguiendo los requisitos de A.3.6.13 o alternativamente por medio de un procedimiento de análisis dinámico, pero en ningún caso los resultados obtenidos por medio de este procedimiento alternativo puede conducir a resultados menores que los obtenidos por medio de A.3.6.13.

#### A.5.4.7 — TORSIÓN

El análisis dinámico debe tener en cuenta los efectos torsionales de toda la estructura según lo indicado en A.3.6.7.

#### A.5.4.8 — SISTEMAS DUALES

Cuando el sistema de resistencia sísmica corresponda a un sistema dual, tal como lo define A.3.2.1.4, el sistema debe ser capaz, en conjunto, de resistir el cortante total en la base que se obtiene por medio del análisis dinámico. El análisis del pórtico espacial resistente a momentos, actuando independientemente como lo prescribe A.3.2.1.4 (b), puede llevarse a cabo por medio de un análisis dinámico apropiado, o por medio de un análisis de fuerza horizontal equivalente de acuerdo con los requisitos del Capítulo A.4.

### A.5.5 — MÉTODO DE ANÁLISIS DINÁMICO CRONOLÓGICO

#### A.5.5.1 — GENERALIDADES

La metodología de análisis dinámico cronológico puede ser utilizada cuando a juicio del ingeniero diseñador ella describe adecuadamente las propiedades dinámicas de la estructura y conduce a resultados representativos de los movimientos sísmicos de diseño. El modelo matemático empleado puede ser linealmente elástico o inelástico. Si se utilizan métodos de análisis dinámico inelástico, debe tenerse especial cuidado en cumplir lo requerido en A.3.4.2.3.

#### A.5.5.2 — RESPUESTA MÁXIMA

Deben determinarse las respuestas máximas de las deflexiones, derivas, fuerzas en los pisos, cortantes de piso, cortante en la base y fuerzas en los elementos, para el conjunto de registros de la familia de acelerogramas requerida por A.2.7.1, los cuales, en este caso, no deben ser menos de tres registros.

#### A.5.5.3 — AJUSTE DE LOS RESULTADOS

El valor del máximo cortante dinámico total en la base, $V_{tj}$ , obtenido para cualquiera de las direcciones principales, $j$, no puede ser menor que el cortante sísmico en la base, $V_{s}$ , calculado por el método de la fuerza horizontal equivalente del Capítulo A.4 y cumpliendo lo indicado en A.5.4.5(a).

Debe notarse que en caso de utilizar modelo matemático inelástico, los resultados ya tienen involucrado el efecto asociado al $R$ , lo que debe tomarse en cuenta para el ajuste requerido.

Cuando el valor máximo del cortante dinámico total en la base, $V_{tj}$ , obtenido para cualquiera de las direcciones principales, $j$, sea menor que el cortante sísmico en la base, $V_{s}$ , calculado como se indicó anteriormente, todos los parámetros de la respuesta dinámica, tales como deflexiones, derivas, fuerzas en los pisos, cortantes de piso, cortante en la base y fuerzas en los elementos de la correspondiente dirección $j$ deben multiplicarse por el siguiente factor de modificación:

$$ \dfrac{V_s}{V_{tj}} \tag{A.5.5-1} $$

Si se utilizan siete o más acelerogramas, en vez del valor máximo del cortante dinámico total en la base, $V_{tj}$ , obtenido para cualquiera de las direcciones principales, $j$, se puede utilizar el valor promedio de los valores obtenidos de todos los acelerogramas empleados, para efectos de cumplir los requisitos de esta sección.

#### A.5.5.4 — FUERZAS DE DISEÑO EN LOS ELEMENTOS

Para obtener las fuerzas de diseño de los elementos, se utilizan las fuerzas sísmicas internas máximas en los elementos, $F_{s}$ , debidamente ajustadas de acuerdo con los requisitos de A.5.5.3, así:

(a) Cuando se trate de un análisis dinámico elástico, se dividen por el valor del coeficiente de capacidad de disipación de energía, $R$ , del sistema de resistencia sísmica, modificado de acuerdo con la irregularidad y ausencia de redundancia según los requisitos de A.3.3.3, para obtener las fuerzas sísmicas reducidas de diseño, $E$ , y se combinan con las otras cargas prescritas por este Reglamento, de acuerdo con los requisitos del Título B, y

(b) En los casos de análisis dinámico inelástico, las fuerzas al nivel en que ocurre la plastificación corresponde a las fuerzas sísmicas reducidas de diseño, $E$ , y no deben ser divididas por el coeficiente de capacidad de disipación de energía. En este caso al aplicar el ajuste de los resultados indicado en A.5.5.3, se permite dividir el valor de $V_{s}$ por $R$ para efectos de hacer las comparaciones indicadas allí.

Debe verificarse que las combinaciones de carga prescritas por este Reglamento, de acuerdo con los requisitos del Título B, exceptuando aquellas que incluyen sismo, en ningún caso conducen a esfuerzos mayores que los de plastificación.

#### A.5.5.5 — FUERZAS DE DISEÑO EN LA CIMENTACIÓN

Para obtener las fuerzas de diseño de la cimentación, se debe cumplir lo prescrito en A.3.7.2 cuando se trate de un análisis dinámico elástico. En el caso de un análisis dinámico inelástico no hay necesidad de dividir por $R$ para encontrar las fuerzas sísmicas reducidas de diseño, $E$ , de los elementos estructurales de la cimentación ni los esfuerzos sobre el suelo, los cuales solo deben multiplicarse por el coeficiente de carga igual a $0.7$.

█
