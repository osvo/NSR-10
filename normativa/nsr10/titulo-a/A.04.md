# A.4 — Método de la fuerza horizontal equivalente

### A.4.0 — NOMENCLATURA

$A_{v}$ = coeficiente de aceleración que representa la velocidad horizontal pico efectiva, para diseño, dado en A.2.2.

$C_{t}$ = coeficiente utilizado para calcular el período de la estructura, definido en A.4.2.2.

$C_{u}$= coeficiente utilizado para calcular el período máximo permisible la estructura, definido en A.4.2.1.

$C_{vx}$= coeficiente definido en A.4.3.

$F_{i}$ , $F_{x}$ = fuerzas sísmicas horizontales en los niveles $i$ o $x$ respectivamente. Véase A.4.3.

$F_{v}$ = coeficiente de amplificación que afecta la aceleración en la zona de períodos intermedios, debida a los efectos de sitio, adimensional.

$f_{i}$ = fuerza sísmica horizontal en el nivel $i$ para ser utilizada en la ecuación A.4.2-1.

$g$ = aceleración debida a la gravedad ($9.8$ m/s²).

$h_{i}$ , $h_{x}$ = altura en metros, medida desde la base, del nivel $i$ o $x$ . Véase A.4.3.2.

$h_{p}$= altura del piso medida desde la superficie del diafragma del piso hasta la superficie del diafragma del piso inmediatamente inferior.

$I$ = coeficiente de importancia dado en A.2.5.2.

$k$ = exponente relacionado con el período fundamental de la edificación dado en A.4.3.2.

$M$ = masa total de la edificación — $M$ debe ser igual a la masa total de la estructura más la masa de aquellos elementos tales como muros divisorios y particiones, equipos permanentes, tanques y sus contenidos, etc.

En depósitos o bodegas debe incluirse además un 25 por ciento de la masa correspondiente a los elementos que causan la carga viva del piso. Capítulos A.4 y A.5 (en kg).

$m_{i}$ , $m_{x}$ = parte de $M$ que está colocada en el nivel $i$ o $x$ respectivamente

$N$ = número de pisos de la edificación.

$n_{w}$= número de muros de la edificación efectivos para resistir las fuerzas sísmicas horizontales en la dirección bajo estudio.

$S_{a}$= valor del espectro de aceleraciones de diseño para un período de vibración dado. Máxima aceleración horizontal de diseño, expresada como una fracción de la aceleración de la gravedad, para un sistema de un grado de libertad con un período de vibración $T$ . Está definido en A.2.6.

$T$ = período fundamental del edificio como se determina en A.4.2.

$T_{a}$ = período de vibración fundamental aproximado. Véase A.4.2.

$V_{s}$ = cortante sísmico en la base, para las fuerzas sísmicas. Véase A.4.3.

$α$ = exponente para ser utilizado en el cálculo del período aproximado $T_{a}$ . Véase A.4.2.2.

$δ_{i}$ = desplazamiento horizontal del nivel $i$ con respecto a la base de la estructura, debido a las fuerzas horizontales $f_{i}$, para ser utilizado en la ecuación A.4.2-1.

<!-- mod:1-decreto-092-2011-15 -->
> **Modificación — Decreto 092 de 2011** · anexo, p. 3
>
> En A.4.0 y en A.13.2 la definición de $N$ queda así: $N$ = número de pisos de la edificación por encima de la base.

<!-- mod:3-decreto-945-2017-49 -->
> **Modificación — Decreto 945 de 2017** · anexo, p. 11
>
> Se suprimen las definiciones de $A_B$, $A_{wi}$, $\ell_{wi}$, $h_n$, $h_{wi}$ y $n_w$, que solo se usaban en la ecuación A.4.2-4, también suprimida.

### A.4.1 — GENERAL

**A.4.1.1** — Los requisitos de este Capítulo controlan la obtención de las fuerzas sísmicas horizontales de la edificación y el análisis sísmico de la misma, de acuerdo con los requisitos dados en el Capítulo A.3 para la utilización del método de la fuerza horizontal equivalente.

### A.4.2 — PERÍODO FUNDAMENTAL DE LA EDIFICACIÓN

**A.4.2.1** — El valor del período fundamental de la edificación, $T$ , debe obtenerse a partir de las propiedades de su sistema de resistencia sísmica, en la dirección bajo consideración, de acuerdo con los principios de la dinámica estructural, utilizando un modelo matemático linealmente elástico de la estructura. Este requisito puede suplirse por medio del uso de la siguiente ecuación:

$$ T = 2\pi \sqrt{\dfrac{\sum_{i=1}^{n} \left(m_i\,\delta_i^2\right)}{\sum_{i=1}^{n} \left(f_i\,\delta_i\right)}} \tag{A.4.2-1} $$

Los valores de $f_{i}$ representan unas fuerzas horizontales distribuidas aproximadamente de acuerdo con las ecuaciones A.4.3-2 y A.4.3-3, o utilizando cualquier otra distribución racional que se aproxime a la del modo fundamental de la estructura en la dirección en estudio. Las deflexiones horizontales, $δ_{i}$, deben calcularse utilizando las fuerzas horizontales $f_{i}$.

El valor de $T$ no puede exceder $C_{u} T_{a}$ , donde $C_{u}$ se calcula por medio de la ecuación A.4.2-2 y $T_{a}$ se calcula de acuerdo con A.4.2-3.

$$ C_u = 1.75 - 1.2\,A_v F_v \tag{A.4.2-2} $$

pero $C_{u}$ no debe ser menor de 1.2.

<!-- mod:1-decreto-092-2011-16 -->
> **Modificación — Decreto 092 de 2011** · anexo, p. 3
>
> El tercer párrafo, anterior a la ecuación (A.4.2-2), queda así: El valor de $T$, calculado a partir de las propiedades del sistema de resistencia sísmica, de acuerdo con los principios de la dinámica estructural utilizando un modelo matemático linealmente elástico o mediante la ecuación A.4.2-1, no puede exceder $C_u T_a$, donde $C_u$ se calcula por medio de la ecuación A.4.2-2 y $T_a$ se calcula de acuerdo con A.4.2-3.

**A.4.2.2** — Alternativamente el valor de $T$ puede ser igual al período fundamental aproximado, $T_{a}$ , que se obtenga por medio de la ecuación A.4.2-3.

$$ T_a = C_t\,h^{\alpha} \tag{A.4.2-3} $$

donde $C_{t}$ y $α$ tienen los valores dados en la tabla A.4.2-1.

**Tabla A.4.2-1**

Valor de los parámetros $C_{t}$ y $α$ para el cálculo del período aproximado $T_{a}$

| Sistema estructural de resistencia sísmica | $C_{t}$ | $α$ |
|---|---|---|
| Pórticos resistentes a momentos de concreto reforzado que resisten la totalidad de las fuerzas sísmicas y que no están limitados o adheridos a componentes más rígidos, estructurales o no estructurales, que limiten los desplazamientos horizontales al verse sometidos a las fuerzas sísmicas. | 0.047 | 0.9 |
| Pórticos resistentes a momentos de acero estructural que resisten la totalidad de las fuerzas sísmicas y que no están limitados o adheridos a componentes más rígidos, estructurales o no estructurales, que limiten los desplazamientos horizontales al verse sometidos a las fuerzas sísmicas. | 0.072 | 0.8 |
| Pórticos arriostrados de acero estructural con diagonales excéntricas restringidas a pandeo. | 0.073 | 0.75 |
| Todos los otros sistemas estructurales basados en muros de rigidez similar o mayor a la de muros de concreto o mampostería | 0.049 | 0.75 |


<!-- mod:1-decreto-092-2011-18 -->
> **Modificación — Decreto 092 de 2011** · anexo, p. 4
>
> El texto de la última fila de la Tabla A.4-1 (Tabla A.4.2-1) queda así: «Alternativamente, para sistemas de muros estructurales de concreto reforzado o mampostería estructural…»

<!-- mod:3-decreto-945-2017-50 -->
> **Modificación — Decreto 945 de 2017** · anexo, p. 11
>
> Se suprime la última línea de la Tabla A.4.2-1 (parámetros alternativos para muros estructurales de concreto o mampostería).


Alternativamente, para edificaciones de 12 pisos o menos con alturas de piso, $h_{p}$ , no mayores de 3 m cuyo sistema estructural de resistencia sísmica está compuesto por pórticos resistentes a momentos de concreto reforzado o acero estructural, el período de vibración aproximado, $T_{a}$ , en s, puede determinarse por medio de la ecuación A.4.2-5.

$$ T_a = 0.1\,N \tag{A.4.2-5} $$

<!-- mod:1-decreto-092-2011-17 -->
> **Modificación — Decreto 092 de 2011** · anexo, p. 3
>
> La última frase queda así: Alternativamente, para edificaciones de 12 pisos o menos, por encima de la base, con el promedio de las alturas de piso, $h_p$, menor o igual a 3 m, cuyo sistema estructural de resistencia sísmica esté compuesto por pórticos resistentes a momentos de concreto reforzado o acero estructural, el período de vibración aproximado, $T_a$, en s, puede determinarse por medio de la ecuación A.4.2-5, donde $N$ es el número de pisos de la edificación por encima de la base.

<!-- mod:3-decreto-945-2017-51 -->
> **Modificación — Decreto 945 de 2017** · anexo, p. 11
>
> Se suprime la ecuación A.4.2-4.

**A.4.2.3** — El valor de $T$ obtenido al utilizar las ecuaciones A.4.2-1, A.4.2-3 o A.4.2-5 es un estimativo inicial razonable del período estructural para predecir las fuerzas a aplicar sobre la estructura con el fin de dimensionar su sistema de resistencia sísmica. Sin embargo, una vez dimensionada la estructura, debe calcularse el valor ajustado de $T$ mediante la aplicación de análisis modal o de la ecuación A.4.2-1 para compararlo con el estimado inicial; si el periodo de la estructura diseñada difiriera en más del 10% con el periodo estimado inicialmente, debe repetirse el proceso de análisis, utilizando el último periodo calculado como nuevo estimado, hasta que se converja en un resultado dentro de la tolerancia del 10% señalada.

### A.4.3 — FUERZAS SÍSMICAS HORIZONTALES EQUIVALENTES

**A.4.3.1** — El cortante sísmico en la base, $V_{s}$ , equivalente a la totalidad de los efectos inerciales horizontales producidos por los movimientos sísmicos de diseño, en la dirección en estudio, se obtiene por medio de la siguiente ecuación:

$$ V_s = S_a\,g\,M \tag{A.4.3-1} $$

El valor de $S_{a}$ en la ecuación anterior corresponde al valor de la aceleración, como fracción de la de la gravedad, leída en el espectro definido en A.2.6 para el período $T$ de la edificación.

**A.4.3.2** — La fuerza sísmica horizontal, $F_{x}$ , en cualquier nivel $x$ , para la dirección en estudio, debe determinarse usando la siguiente ecuación:

$$ F_x = C_{vx}\,V_s \tag{A.4.3-2} $$

y

$$ C_{vx} = \dfrac{m_x\,h_x^k}{\sum_{i=1}^{n} \left(m_i\,h_i^k\right)} \tag{A.4.3-3} $$

donde $k$ es un exponente relacionado con el período fundamental, $T$ , de la edificación de la siguiente manera:

(a) Para $T$ menor o igual a $0.5$ segundos, $k=1.0$,

(b) Para $T$ entre $0.5$ y $2.5$ segundos, $k=0.75+0.5T$, y

(c) Para $T$ mayor que $2.5$ segundos, $k=2.0$.

### A.4.4 — ANÁLISIS DE LA ESTRUCTURA

**A.4.4.1** — El efecto de las fuerzas sísmicas, obtenidas de acuerdo con los requisitos de A.4.3, correspondientes a cada nivel, debe evaluarse por medio de un análisis realizado utilizando un modelo matemático linealmente elástico de la estructura, que represente adecuadamente las características del sistema estructural. El análisis, realizado de acuerdo con los principios de la mecánica estructural, debe tenerse en cuenta, como mínimo:

(a) Las condiciones de apoyo de la estructura, especialmente cuando se combinen elementos verticales de resistencia sísmica con diferencias apreciables en su rigidez,

(b) El efecto de diafragma, rígido o flexible, de los entrepisos de la edificación, en la distribución del cortante sísmico del piso a los elementos verticales del sistema estructural de resistencia sísmica,

(c) Las variaciones en las fuerzas axiales de los elementos verticales del sistema de resistencia sísmica causadas por los momentos de vuelco que inducen las fuerzas sísmicas,

(d) Los efectos torsionales prescritos en A.3.6.7,

(e) Los efectos de la dirección de aplicación de la fuerza sísmica prescritos en A.3.6.3,

(f) En estructuras de concreto reforzado y mampostería estructural, a juicio del ingeniero diseñador, consideraciones acerca del grado de fisuración de los elementos, compatibles con las fuerzas sísmicas y el grado de capacidad de disipación de energía prescrito para el material estructural, y

(g) Deben consultarse lo requisitos de A.3.4.3.

#### A.4.4.2 — Como resultados del análisis se deben obtener, como mínimo:

(a) Los desplazamientos horizontales de la estructura, incluyendo los efectos torsionales, que se emplean para evaluar si las derivas de la estructura cumplen los requisitos dados en el Capítulo A.6,

(b) La distribución del cortante de piso, incluyendo los efectos torsionales, a todos los elementos verticales del sistema de resistencia sísmica,

(c) Los efectos de las fuerzas sísmicas en la cimentación de la edificación, y

(d) Las fuerzas internas (momentos flectores, fuerzas cortantes, fuerzas axiales y momentos de torsión) correspondientes a cada elemento que haga parte del sistema de resistencia sísmica.

### A.4.5 — USO DEL SISTEMA INTERNACIONAL DE MEDIDAS (SI) EN EL CÁLCULO DE LAS

FUERZAS SÍSMICAS DE ACUERDO CON ESTE CAPÍTULO En el Sistema Internacional de Medidas (SI) el kg (kilogramo) es una unidad de masa, por lo tanto la masa de la estructura se debe expresar en kg. Aplicando la 2a Ley de Newton que dice que la fuerza inercial es igual a la masa del cuerpo multiplicada por su aceleración; si la masa está sometida a una aceleración en m/s2, se obtiene una fuerza cuyas unidades son (kg · m/s2). Por definición, en el sistema SI la unidad de fuerza es un newton (N) y corresponde a la fuerza inercial de una masa de 1 kg sometida a una aceleración de 1 m/s2 (1 N = 1 kg · 1 m/s2). Entonces, si la masa se expresa en kg y las aceleraciones en m/s2, se obtiene fuerzas inerciales en newtons.

La ecuación A.4.3-1 es una aplicación de la 2a Ley de Newton y se emplea para determinar las fuerzas inerciales horizontales que producen los movimientos del terreno causados por el sismo de diseño. El valor de la aceleración horizontal máxima que tiene el terreno donde se apoya la estructura, se lee del espectro de aceleraciones, $S_{a}$ , definido en el Capítulo A.2 para el período fundamental de vibración de la estructura $T$ . El espectro $S_{a}$ es adimensional, y corresponde a la aceleración horizontal que impone el sismo en la base de la estructura, expresada como una fracción de la gravedad, por lo tanto para obtener la aceleración en m/s2, debe multiplicarse por la aceleración de la gravedad, $g$ ($g=9.8$ m/s2). Al utilizar la ecuación A.4.3-1, si la masa total de la edificación, $M$ , se expresa en kg, entonces la totalidad de las fuerzas inerciales horizontales que actúan sobre la estructura cuando ésta se ve sometida al sismo de diseño, $V_{s}$ , se obtiene en newtons así:

$$ V_s = S_a \cdot g\ (\mathrm{m/s^2}) \cdot M\ (\mathrm{kg}) = S_a \cdot g \cdot M\ (\mathrm{kg \cdot m/s^2}) = S_a \cdot g \cdot M\ (\mathrm{N}) $$

Pero en el diseño práctico de edificaciones, tanto el kg como el N, son unidades muy pequeñas; por esta razón es conveniente expresar la masa en Mg (Megagramos, 1 Mg = 1 000 kg = 10⁶ g). En este caso la aplicación de la ecuación A.4.3-1 conduce a una fuerza, $V_{s}$ , en kN (kilonewtons):

$$ V_s = S_a \cdot g\ (\mathrm{m/s^2}) \cdot M\ (\mathrm{Mg}) = S_a \cdot g \cdot M\ (\mathrm{Mg \cdot m/s^2}) = S_a \cdot g \cdot M\ (1000 \cdot \mathrm{kg \cdot m/s^2}) = S_a \cdot g \cdot M\ (1000 \cdot \mathrm{N}) = S_a \cdot g \cdot M\ (\mathrm{kN}) $$

A modo de referencia, en el antiguo sistema mks (m-kgf-s, metro-kilogramo fuerza-segundo) 1 kgf = 9.8 N ≅ 10 N, y análogamente 1 000 kgf = 1 ton = 9 806.65 N ≅ 10 000 N = 10 kN. Entonces un kN es aproximadamente un décimo de tonelada.

█
