# C.9 — Requisitos de resistencia y funcionamiento

### C.9.1 — Generalidades

**C.9.1.1** — Las estructuras y los elementos estructurales deben ser diseñados para que tengan en cualquier sección una resistencia de diseño al menos igual a la resistencia requerida, calculada esta última para las cargas y fuerzas mayoradas en las condiciones establecidas en el Título C del Reglamento NSR-10.

**C.9.1.2** — Los elementos también deben cumplir todos los demás requisitos del Título C del Reglamento NSR-10 para garantizar un comportamiento adecuado al nivel de carga de servicio.

**C.9.1.3** — Se permite el diseño de estructuras y elementos estructurales usando las combinaciones de mayoración de carga y los factores de reducción de resistencia del Apéndice C-C. No se permite mezclar las combinaciones de mayoración de carga del presente Capítulo con los factores de reducción de resistencia del Apéndice C-C.

### C.9.2 — Resistencia requerida

<!-- mod:1-decreto-092-2011-97 -->
> *Texto vigente según el Decreto 092 de 2011 (anexo, p. 23).*

**Nota Importante**: Las combinaciones de carga dadas en C.9.2.1 contienen factores de carga menores que los que prescribía el Reglamento NSR-98, pero al mismo tiempo en esta nueva versión del Reglamento (NSR-10) se han prescrito valores de los coeficientes de reducción de resistencia, $\phi$, menores que los que contenía el Reglamento NSR 98, siendo los nuevos valores concordantes con la probabilidad de falla estructural que limita el Reglamento. Por lo tanto es incorrecto, e inseguro, utilizar las nuevas ecuaciones de combinación de carga de C.9.2.1 con los valores de los coeficientes de reducción de resistencia, $\phi$, que contenía la NSR-98.

**C.9.2.1** — La resistencia requerida $U$ debe ser por lo menos igual al efecto de las cargas mayoradas en las ecuaciones (C.9-1) a (C.9-7). Debe investigarse el efecto de una o más cargas que no actúan simultáneamente.

$$ U = 1.4D \tag{C.9-1} $$

$$ U = 1.2D + 1.6L + 0.5\,(L_r \text{ ó } G \text{ ó } L_e) \tag{C.9-2} $$

$$ U = 1.2D + 1.6\,(L_r \text{ ó } G \text{ ó } L_e) + (1.0L \text{ ó } 0.5W) \tag{C.9-3} $$

$$ U = 1.2D + 1.0W + 1.0L + 0.5\,(L_r \text{ ó } G \text{ ó } L_e) \tag{C.9-4} $$

$$ U = 1.2D + 1.0E + 1.0L \tag{C.9-5} $$

$$ U = 0.9D + 1.0W \tag{C.9-6} $$

$$ U = 0.9D + 1.0E \tag{C.9-7} $$

**C.9.2.2** — Carga viva — Se permite reducir a 0.5 el factor de carga de carga viva $L$ en las ecuaciones (C.9-3) a (C.9-5), excepto para estacionamientos, áreas ocupadas como lugares de reunión pública y en todas las áreas donde $L$ sea superior a 4.8 kN/m².

**C.9.2.3** — Efectos sísmicos — Las fuerzas sísmicas reducidas de diseño, $E$, utilizadas en las combinaciones (C.9-5) y (C.9-7) corresponden al efecto, expresado en términos de fuerza, $F_s$, de los movimientos sísmicos de diseño prescritos en el Título A, divididos por $R$ ($E = F_s/R$). Cuando se trata de diseñar los miembros, el valor del coeficiente de carga que afecta las fuerzas sísmicas $E$, es 1.0, dado que estas están prescritas al nivel de resistencia. Para la verificación de las derivas obtenidas de las deflexiones horizontales causadas por el sismo de diseño, deben utilizarse los requisitos del Capítulo A.6, los cuales exigen que las derivas se verifiquen para las fuerzas sísmicas $F_s$, sin haber sido divididas por $R$.

**C.9.2.4** — Efectos de impacto — Si en el diseño se toma en cuenta la resistencia a los efectos de impacto, éstos deben incluirse en $L$.

**C.9.2.5** — Efectos auto deformantes — Cuando sea aplicable, los efectos estructurales de $T$ deben considerarse en combinación con otras cargas. El factor de carga para $T$ debe establecerse considerando la incertidumbre asociada con la magnitud esperada de $T$, la probabilidad de que el máximo efecto ocurra simultáneamente con otras cargas aplicadas, y las consecuencias potencialmente adversas en caso de que el efecto $T$ sea mayor que el supuesto. El factor de carga de $T$ no puede ser menor que la unidad (1.0).

**C.9.2.6** — Cargas de fluidos — Cuando $F$ esté presente, debe incluirse con el mismo factor de carga de $D$ en las ecuaciones (C.9-1) a (C.9-5) y en la ecuación (C.9-7).

**C.9.2.7** — Empuje lateral del suelo — Cuando $H$ esté presente, se debe incluir en las combinaciones de carga de C.9.2.1, con factores de carga que se ajusten a lo indicado en (a), (b), o (c):

(d) cuando $H$ actúe solo o incremente el efecto de otras cargas, debe incluirse con un factor de carga de 1.6,

(e) cuando el efecto de $H$ es permanente y contrarresta el efecto de otras cargas, debe incluirse con un factor de carga de 0.9,

(f) cuando el efecto de $H$ no es permanente, pero cuando está presente contrarresta el efecto de otras cargas, no se debe incluir $H$.

**C.9.2.8** — Cargas de inundación y hielo — Si una estructura se encuentra ubicada en una zona de inundación, o está sometida a fuerzas por cargas de hielo atmosférico (granizo), deben usarse las cargas por inundación o por hielo y a las combinaciones de carga adecuadas de ASCE/SEI 7.

**C.9.2.8** — Carga de gateo del acero de preesforzado — Para el diseño de zonas de anclaje de postensado debe usarse un factor 1.2 para la fuerza de preesfuerzo máxima aplicada por el gato.

<!-- mod:2-decreto-340-2012-19 -->
> **Modificación — Decreto 340 de 2012** · anexo, p. 6
>
> En las modificaciones al Reglamento NSR-10 introducidas en el Decreto 092 de 2011, donde se modifica la sección C.9.2 aparecen dos secciones con la denominación C.9.2.8. La segunda sección C.9.2.8 debe numerarse como C.9.2.9 y quedar así:
>
> **C.9.2.9** — Para el diseño de zonas de anclaje de postensado debe usarse un factor 1.2 para la fuerza de preesfuerzo máxima aplicada por el gato.

### C.9.3 — Resistencia de diseño

**C.9.3.1** — La resistencia de diseño proporcionada por un elemento, sus conexiones con otros elementos, así como sus secciones transversales, en términos de flexión, carga axial, cortante y torsión, deben tomarse como la resistencia nominal calculada de acuerdo con los requisitos y suposiciones del Título C del Reglamento NSR-10, multiplicada por los factores $φ$ de reducción de resistencia dados en C.9.3.2, C.9.3.4. y C.9.3.5

**C.9.3.2** — El factor de reducción de resistencia, $φ$ , debe ser el dado en C.9.3.2.1 a C.9.3.2.7:

**C.9.3.2.1** — Secciones controladas por tracción como se define en 10.3.4 $.......................................................$ 0.90 (Véase también C.9.3.2.7)

**C.9.3.2.2** — Secciones controladas por compresión como se definen en C.10.3.3:

(a) Elementos con refuerzo en espiral según C.10.9.3 ........................................................................... 0.75

(b) Otros elementos reforzados. .............................................................................................................. 0.65 Para las secciones en las que la deformación unitaria neta a la tracción en el acero extremo en tracción en el estado de resistencia nominal, $ε_{t}$, se encuentra entre los límites para secciones controladas por compresión y las secciones controladas por tracción, se permite que $φ$ aumente linealmente desde el valor correspondiente a las secciones controladas por compresión hasta 0.90, en la medida que $ε_{t}$ aumente desde el límite de deformación unitaria controlado por compresión hasta 0.005.

En forma alternativa, cuando se usa el Apéndice C-B, para elementos en los cuales $f_{y}$ no exceda 420 MPa, con refuerzo simétrico, y cuando $(d−d')/ h$ no es menor de 0.70, se permite aumentar $φ$ linealmente hasta 0.90, en la medida que $φ_{P}$disminuye desde $0.10f_{c} 'A_{g}$ hasta cero. Para otros elementos reforzados $φ$ puede incrementarse linealmente a 0.90 en la medida que $φ_{P}$disminuye desde $0.10f_{c} 'A_{g}$ o$φ_{P}$, el que sea menor, hasta cero.

**C.9.3.2.3** — Cortante y torsión $...................................................................................................................................$ 0.75

**C.9.3.2.4** — Aplastamiento en el concreto (excepto para anclajes de postensado y modelos puntal-tensor) $....................................................................................................................................................$ 0.65

**C.9.3.2.5** — Zonas de anclaje de postensado $.........................................................................................................$ 0.85

**C.9.3.2.6** — Los modelos puntal-tensor (Apéndice C-A) y puntales, tensores, zonas de nodos y áreas de apoyo en esos modelos $.....................................................................................................$ 0.75

**C.9.3.2.7** — Las secciones a flexión en los elementos pretensados donde la longitud embebida del torón es menor que la longitud de desarrollo, como se establece en C.12.9.1.1:

(a) desde el extremo del elementos hasta el extremo de la longitud de transferencia$.....................................$ 0.75

(b) Desde el extremo de la longitud de transferencia hasta el extremo de la longitud de desarrollo, debe permitirse que $φ$ sea incrementado linealmente de 0.75 hasta 0.9.

Donde la adherencia del torón no se extiende hasta el extremo del elemento, se debe asumir que el embebido del torón se inicia en el extremo de la longitud no adherida. Véase también C.12.9.3

**C.9.3.3** — Las longitudes de desarrollo especificadas en el Capítulo C.12 no requieren de un factor $φ$ .

**C.9.3.4** — Para estructuras con capacidad de disipación de energía moderada (DMO) o especial (DES) que dependen de muros estructurales, construidos en sitio o prefabricados, o pórticos resistentes a momento para resistir los efectos sísmicos, $E$, $φ$ debe modificarse de acuerdo con lo indicado en (a) hasta (c):

(a) En cualquier elemento estructural que se diseñe para resistir $E$, $φ$ para cortante debe ser 0.60 si la resistencia nominal a cortante del elemento es menor que el cortante correspondiente al desarrollo de la resistencia nominal a flexión del elemento. La resistencia nominal a flexión debe determinarse considerando las cargas axiales mayoradas más críticas e incluyendo $E$;

(b) En diafragmas $φ$ para cortante no debe exceder el mínimo $φ$ para cortante usado para los elementos verticales del sistema primario de resistencia ante fuerzas sísmicas;

(c) En nudos y vigas de acople reforzadas en forma diagonal $φ$ para cortante debe ser 0.85.

**C.9.3.5** — En el Capítulo C.22, $φ$ deben ser 0.60 para flexión, compresión, cortante y aplastamiento en concreto estructural simple.

### C.9.4 — Resistencia de diseño para el refuerzo

Los valores de $f_{y}$ y $f_{yt}$ usados en los cálculos de diseño no deben exceder de 550 MPa, excepto para aceros de preesforzado y para los refuerzos transversales en espiral en C.10.9.3 y C.21.1.5.4.

### C.9.5 — Control de deflexiones

**C.9.5.1** — Los elementos de concreto reforzado sometidos a flexión deben diseñarse para que tengan una rigidez adecuada con el fin de limitar cualquier deflexión que pudiese afectar adversamente la resistencia o el funcionamiento de la estructura.

#### C.9.5.2 — Elementos reforzados en una dirección (no preesforzados)

**C.9.5.2.1** — Las alturas o espesores mínimos establecidos en la tabla C.9.5(a) deben aplicarse a los elementos en una dirección que no soporten o estén ligados a particiones u otro tipo de elementos susceptibles de dañarse debido a deflexiones grandes, a menos que el cálculo de las deflexiones indique que se puede utilizar un espesor menor sin causar efectos adversos.

**C.9.5.2.2** — Cuando se calculen las deflexiones, aquéllas que ocurran inmediatamente con la aplicación de la carga deben calcularse mediante los métodos o fórmulas usuales para deflexiones elásticas, tomando en consideración los efectos de la fisuración y del refuerzo en la rigidez del elemento.

**C.9.5.2.3** — A menos que los valores de rigidez se obtengan mediante un análisis más completo, las deflexiones inmediatas deben calcularse usando el módulo de elasticidad del concreto, $E_{c}$ , que se especifica en C.8.5.1 (para concreto de peso normal o liviano) y el momento de inercia efectivo, $I_{e}$, que se indica a continuación, pero sin tomarlo mayor que $I_{g}$.

$$ I_e = \left(\dfrac{M_{cr}}{M_a}\right)^3 I_g + \left[1 - \left(\dfrac{M_{cr}}{M_a}\right)^3\right] I_{cr} \tag{C.9-8} $$

donde

$$ M_{cr} = \dfrac{f_r\,I_g}{y_t} \tag{C.9-9} $$

y para concreto de peso normal,

$$ f_r = 0.62\,\lambda\sqrt{f'_c} \tag{C.9-10} $$

**C.9.5.2.4** — Para elementos continuos se permite tomar $I_{e}$como el promedio de los valores obtenidos de la ecuación (C.9-8) para las secciones críticas de momento positivo y negativo. Para elementos prismáticos, se permite tomar$I_{e}$ como el valor obtenido de la ecuación (C.9-8) en el centro de la luz para tramos simples y continuos, y en el punto de apoyo para voladizos.

**C.9.5.2.5** — A menos que los valores se obtengan mediante un análisis más completo, la deflexión adicional a largo plazo, resultante del flujo plástico y retracción de elementos en flexión (concreto normal o liviano), debe determinarse multiplicando la deflexión inmediata causada por la carga permanente por el factor $λ_{Δ}$

$$ \lambda_\Delta = \dfrac{\xi}{1 + 50\,\rho'} \tag{C.9-11} $$

donde $ρ'$ es el valor en la mitad de la luz para tramos simples y continuos y en el punto de apoyo para voladizos.

Puede tomarse $ξ$ , el factor dependiente del tiempo para cargas sostenidas, igual a:

5 años o más$...................................................................$ 2.0 12 meses$..........................................................................$ 1.4 6 meses$............................................................................$ 1.2 3 meses$............................................................................$ 1.0

**C.9.5.2.6** — La deflexión calculada de acuerdo con C.9.5.2.2 a C.9.5.2.5 no debe exceder los límites establecidos en la tabla C.9.5(b).

**Tabla C.9.5(a)** — Alturas o espesores mínimos de vigas no preesforzadas o

losas reforzadas en una dirección a menos que se calculen las deflexiones

| Elementos | Simplemente apoyados | Con un extremo continuo | Ambos extremos continuos | En voladizo |
|---|---|---|---|---|
| | Elementos que **NO** soporten o estén ligados a divisiones u otro tipo de elementos susceptibles de dañarse debido a deflexiones grandes. | | | |
| Losas macizas en una dirección | $\ell/20$ | $\ell/24$ | $\ell/28$ | $\ell/10$ |
| Vigas o losas nervadas en una dirección | $\ell/16$ | $\ell/18.5$ | $\ell/21$ | $\ell/8$ |

Espesor mínimo, $h$. NOTAS: Los valores dados en esta tabla se deben usar directamente en elementos de concreto de peso normal y refuerzo grado 420 MPa. Para otras condiciones, los valores deben modificarse como sigue:

(a) Para concreto liviano estructural con densidad $w_{c}$ dentro del rango de 1 440 a 1 840 kg/m3, los valores de la tabla deben multiplicarse por (1.65–0.0003$w_{c}$), pero no menos de 1.09.

(b) Para $f_{y}$ distinto de 420 MPa, los valores de esta tabla deben multiplicarse por (0.4 + $f_{y}/$700).

#### C.9.5.3 — Elementos reforzados en dos direcciones (no preesforzados)

**C.9.5.3.1** — Debe emplearse la sección C.9.5.3 para definir el espesor mínimo de losas u otros elementos reforzados en dos direcciones diseñados de acuerdo con las disposiciones del Capítulo C.13 y que se ajusten a los requisitos de C.13.6.1.2. El espesor de las losas sin vigas interiores que se extiendan entre los apoyos en todos sentidos debe satisfacer los requisitos de C.9.5.3.2 ó C.9.5.3.4. El espesor de las losas con vigas que se extiendan entre los apoyos en todos sentidos debe satisfacer los requisitos de una de C.9.5.3.3 ó C.9.5.3.4.

**Tabla C.9.5(b)** — Deflexión máxima admisible calculada

| Tipo de elemento | Deflexión considerada | Límite de deflexión |
|---|---|---|
| Cubiertas planas que no soporten ni estén ligadas a elementos no estructurales susceptibles de sufrir daños debido a deflexiones grandes. | Deflexión inmediata debida a la carga viva, $L$ | $\ell/180$* |
| Entrepisos que no soporten ni estén ligados a elementos no estructurales susceptibles de sufrir daños debido a deflexiones grandes. | Deflexión inmediata debida a la carga viva, $L$ | $ℓ/360$ |
| Sistema de entrepiso o cubierta que soporte o esté ligado a elementos no estructurales susceptibles de sufrir daños debido a deflexiones grandes. | La parte de la deflexión total que ocurre después de la unión de los elementos no estructurales (la suma de la deflexión a largo plazo debida a todas las cargas permanentes, y la deflexión inmediata debida a cualquier carga viva adicional)† | $ℓ/480$‡ |
| Sistema de entrepiso o cubierta que soporte o esté ligado a elementos no estructurales no susceptibles de sufrir daños debido a deflexiones grandes. |  | $\ell/240$§ |

* Este límite no tiene por objeto constituirse en un resguardo contra el empozamiento de aguas. Este último se debe verificar mediante cálculos de deflexiones adecuados, incluyendo las deflexiones debidas al agua estancada, y considerando los efectos a largo plazo de todas las cargas permanentes, la contraflecha, las tolerancias de construcción y la confiabilidad en las medidas tomadas para el drenaje.

† Las deflexiones a largo plazo deben determinarse de acuerdo con C.9.5.2.5 ó C.9.5.4.3, pero se pueden reducir en la cantidad de deflexión calculada que ocurra antes de unir los elementos no estructurales. Esta cantidad se determina basándose en datos de ingeniería aceptables correspondiente a las características tiempo-deflexión de elementos similares a los que se están considerando.

‡ Este límite se puede exceder si se toman medidas adecuadas para prevenir daños en elementos apoyados o unidos.

§ Pero no mayor que la tolerancia establecida para los elementos no estructurales. Este límite se puede exceder si se proporciona una contraflecha de modo que la deflexión total menos la contraflecha no exceda dicho límite.

**C.9.5.3.2** — El espesor mínimo de las losas sin vigas interiores que se extiendan entre los apoyos y que tienen una relación entre lados no mayor que 2, debe cumplir con lo requerido en la tabla C.9.5(c) y no debe ser inferior que los siguientes valores:

(a) Losas sin ábacos como se definen en C.13.2.5125 mm

(b) Losas con ábacos como se definen en C.13.2.5100 mm

<!-- mod:1-decreto-092-2011-98 -->
> **Modificación — Decreto 092 de 2011** · anexo, p. 24
>
> El literal C.9.5.3.2 debe corregirse para que los valores de 125 mm y 100 mm queden apropiadamente alineados a la derecha, así:
>
> **C.9.5.3.2** — El espesor mínimo de las losas sin vigas interiores que se extiendan entre los apoyos y que tienen una relación entre lados no mayor que 2, debe cumplir con lo requerido en la Tabla C.9.5(c) y no debe ser inferior que los siguientes valores:
>
> (a)  Losas sin ábacos como se definen en C.13.2.5.............................................................125 mm
>
> (b)  Losas con ábacos como se definen en C.13.2.5............................................................100 mm

**C.9.5.3.3** — El espesor mínimo $h$ para losas con vigas que se extienden entre los apoyos en todos los lados debe ser:

(a) Para $α_{fm}$ igual o menor que 0.2, se aplican las disposiciones de C.9.5.3.2.

(b) Para $α_{fm}$ mayor que 0.2 pero no mayor que 2.0, $h$ no debe ser menor que:

$$ h = \dfrac{\ell_n \left(0.8 + \dfrac{f_y}{1400}\right)}{36 + 5\beta\,(\alpha_{fm} - 0.2)} \tag{C.9-12} $$

pero no menor que 125 mm.

(c) Para $α_{fm}$ mayor que 2.0, $h$ no debe ser menor que:

$$ h = \dfrac{\ell_n \left(0.8 + \dfrac{f_y}{1400}\right)}{36 + 9\beta} \tag{C.9-13} $$

y no menor que 90 mm.

(d) En bordes discontinuos debe disponerse una viga de borde que tenga una relación de rigidez $α_{f}$ no menor de 0.80, o bien aumentar el espesor mínimo requerido por las ecuaciones (C.9-12) ó (C.9-13), por lo menos un 10 por ciento en el panel que tenga un borde discontinuo.

**Tabla C.9.5(c)** — Espesores mínimos de losas sin vigas interiores*

| $f_{y}$, MPa † | Sin ábacos ‡ |  |  | Con ábacos ‡ |  |  |
|---|---|---|---|---|---|---|
|  | Paneles exteriores |  | Paneles inte- riores | Paneles exteriores |  | Paneles inte- riores |
|  | Sin vigas de borde | Con vigas de borde§ |  | Sin vigas de borde | Con vigas de borde§ |  |
| 280 | $ℓ_{n}$ $33$ | $ℓ_{n}$ $36$ | $ℓ_{n}$ $36$ | $ℓ_{n}$ $36$ | $ℓ_{n}$ $40$ | $ℓ_{n}$ $40$ |
| 420 | $ℓ_{n}$ $30$ | $ℓ_{n}$ $33$ | $ℓ_{n}$ $33$ | $ℓ_{n}$ $33$ | $ℓ_{n}$ $36$ | $ℓ_{n}$ $36$ |
| 520 | $ℓ_{n}$ $28$ | $ℓ_{n}$ $31$ | $ℓ_{n}$ $31$ | $ℓ_{n}$ $31$ | $ℓ_{n}$ $34$ | $ℓ_{n}$ $34$ |

* Para construcción en dos direcciones, $ℓ_{n}$, es la luz libre en la dirección larga, medida entre caras de los apoyos en losas sin vigas y entre caras de las vigas, para losas con vigas u otros apoyos en otros casos.

†Para $f_{y}$ entre los valores dados en la tabla, el espesor mínimo debe obtenerse por interpolación lineal.

‡ Ábaco, como se define en C.13.2.5.

§ Losas con vigas entre las columnas a lo largo de los bordes exteriores. El valor de $'f$ para la viga de borde no debe ser menor que 0.8.

El término $ℓ_{n}$ en (b) y (c) corresponde a la luz libre en la dirección larga medida cara a cara de las vigas. El término $β$ en (b) y (c) corresponde a la relación de la luz libre en la dirección larga a la luz libre en la dirección corta de la losa.

**C.9.5.3.4** — Puede utilizarse espesores de losas menores que los mínimos requeridos en C.9.5.3.1, C.9.5.3.2 y C.9.5.3.3 cuando las deflexiones calculadas no exceden los límites de la tabla C.9.5(b). Las deflexiones deben calcularse tomando en cuenta el tamaño y la forma del panel, las condiciones de apoyo y la naturaleza de las restricciones en los bordes de la losa. El módulo de elasticidad del concreto, $E_{c}$ , debe ser el especificado en C.8.5.1.

El momento de inercia efectivo, $I_{e}$, debe ser el obtenido por medio de la ecuación (C.9-8); se permite emplear otros valores si los resultados del cálculo de la deflexión concuerdan razonablemente con los resultados de ensayos de alcance apropiado. La deflexión adicional a largo plazo debe calcularse de acuerdo con C.9.5.2.5.

#### C.9.5.4 — Elementos de concreto preesforzado

**C.9.5.4.1** — Para elementos a flexión diseñados de acuerdo con el Capítulo C.18, las deflexiones inmediatas deben ser calculadas por los métodos o fórmulas usuales para deflexiones elásticas, y se permite utilizar el momento de inercia de la sección total de concreto, $I_{g}$, para los elementos a flexión Clase U, como se define en C.18.3.3.

**C.9.5.4.2** — Para los elementos en flexión Clase C y Clase T, como se definen en C.18.3.3, los cálculos de deflexión deben basarse en un análisis de la sección agrietada transformada. Se permite que los cálculos se basen en una relación momento-deflexión bilineal o en un momento efectivo de inercia, $I_{e}$, como lo define la ecuación (C.9-8).

**C.9.5.4.3** — La deflexión adicional a largo plazo en elementos de concreto preesforzado debe calcularse teniendo en cuenta los esfuerzos en el concreto y en el acero bajo carga permanente, e incluyendo los efectos del flujo plástico y la retracción del concreto, así como la relajación del acero.

**C.9.5.4.4** — La deflexión calculada de acuerdo con C.9.5.4.1 ó C.9.5.4.2, y C.9.5.4.3 no debe exceder los límites establecidos en la tabla C.9.5(b).

#### C.9.5.5 — Elementos compuestos

**C.9.5.5.1** — Elementos apuntalados Si los elementos compuestos sometidos a flexión se apoyan durante su construcción de tal forma que después de retirar los apoyos temporales la carga muerta es soportada por la sección compuesta total, el elemento compuesto se puede considerar equivalente a un elemento construido monolíticamente para el cálculo de la deflexión. En elementos no preesforzados, la parte del elemento en compresión determina si se usan los valores de la tabla C.9.5(a) para concreto de peso normal o liviano. Si se calcula la deflexión, debe tenerse en cuenta la curvatura que resulta de la retracción diferencial de los componentes prefabricados y construidos en obra, y los efectos del flujo plástico a lo largo el eje del elemento de concreto preesforzado.

**C.9.5.5.2** — Elementos sin apuntalar Si el espesor de un elemento prefabricado no preesforzado sujeto a flexión cumple con los requisitos de la tabla C.9.5(a), no se requiere calcular la deflexión. Si el espesor de un elemento compuesto no preesforzado cumple con los requisitos de la tabla C.9.5(a), no se necesita calcular la deflexión que ocurre después de que el elemento se vuelve compuesto; sin embargo, la deflexión a largo plazo del elemento prefabricado debe investigarse en función de la magnitud y duración de la carga antes del inicio efectivo de la acción compuesta.

**C.9.5.5.3** — La deflexión calculada de acuerdo con los requisitos de C.9.5.5.1 ó C.9.5.5.2 no debe exceder de los límites establecidos en la tabla C.9.5(b).

" Notas:
