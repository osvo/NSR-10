# F.5-C — Derivacion de los esfuerzos limite del material para usar en el diseño

F.5.C.1 — ESFUERZOS LIMITES PARA EL MATERIAL BASE Los esfuerzos límite $p_{o}$ , $p_{a}$ y $p_{v}$ usados en el diseño de miembros que figuran en las tablas F.5.4.1 y F.5.4.2 se basan en las siguientes expresiones. Estas expresiones pueden usarse para obtener $p_{o}$ , $p_{a}$ y $p_{v}$ para materiales no cubiertos por las tablas F.5.4.1 y F.5.4.2.

(a) Materiales que tienen $f_{u}≤1.4f_{0.2}p_{o}=f_{0.2}$

$p_{a}=0.5 (f_{0.2}+f_{u})$

$p_{v}=0.6p_{o}$

(b) Materiales que tienen $f_{u}>1.4f_{0.2}p_{o}=1.28f_{0.2}−0.2f_{u}$

$p_{a}=1.2f_{0.2}$

$p_{v}=0.6p_{o}$ donde $f_{0.2}$ y $f_{u}$ son normalmente tomados como el esfuerzo de prueba a tensión del 0.2% mínimo garantizado y la resistencia a tensión del material, respectivamente. Cuando no se cita un valor garantizado para uno o ambos, se pueden usar valores supuestos para $f0.2$ y $f_{u}$ como se indica a continuación:

(1) Valores iguales al 80% de los valores típicos dados por los fabricantes, o (2) Los valores para el mismo material en la condición O F.5.C.2 — ESFUERZO LÍMITE PARA EL MATERIAL DE APORTE F.5.C.2.1 — VALORES MEJORADOS DE $p_{w}$ — Los valores para el esfuerzo límite $p_{w}$ del metal de aporte dados en la tabla F.5.6.2 se basan en resultados de ensayos para especímenes soldados a tope. Con ciertas aleaciones permitidas como metal de aporte, se encuentran resistencias de soldadura mayores que las dadas en la tabla F.5.6.2.

Para sacar provecho de ésto en el diseño, se permite tomar $p_{w}$ de la tabla F.5.C.1 en lugar de la tabla F.5.6.2.

Se enfatiza que estos valores más altos son únicamente válidos si se toman todas las precauciones para evitar el agrietamiento.

F.5.C.2.2 — DETERMINACION DE $p_{w}$ PARA OTRO MATERIAL — Cuando las soldaduras sean hechas sobre aleaciones base no cubiertas por la tabla F.5.C.1, el esfuerzo límite $p_{w}$ del metal de aporte debe obtenerse experimentalmente.

F.5.C.3 — ESFUERZO LIMITE PARA EL MATERIAL DE LA ZONA AFECTADA POR EL CALOR F.5.C.3.1 — EXPRESIONES BASICAS — Los esfuerzos límite $p_{az}$ y $p_{vz}$ para el material de la zona afectada por el calor usados en el diseño de uniones soldadas, presentados en la tabla F.5.6.3, se basan en la expresión pertinente de las siguientes. Estas expresiones pueden usarse para materiales no cubiertos en esa tabla.

(a) Material tratable en caliente:

$p_{az}=k_{z} 'p_{a}$

$p_{vz}=0.6p_{az}$ Donde:

$p_{a}$ = esfuerzo límite del material base, dado en la tabla F.5.4.1 o en F.5.C.1

$k_{z}'$ = coeficiente de ablandamiento modificado, encontrado en F.5.E.2

(b) Material no tratable en caliente:

$p_{az}=1.2f_{0.2}$

$p_{vz}=0.6p_{az}$ Donde:

$f_{0.2}$= esfuerzo de prueba del 0.2% mínimo garantizado para el material base considerado, si está en la condición recocida O. Cuando esté disponible solamente un valor típico de $f0.2$, debe usarse una cifra igual al 80% de este valor en la expresión de $p_{az}$ F.5.C.3.2 — MATERIAL DE LA SERIE 7*** — Los valores alternos A y B para $p_{az}$ y $p_{vz}$ se obtienen usando el valor apropiado de $k_{z}'$ en F.5.C.3.1 (a). El valor de $k_{z}'$ es normalmente el dado en F.5.E.2. Cuando se está encontrando el valor A, sin embargo, es algunas veces posible tomar un valor más favorable de $k_{z}'$ . Esto se puede aplicar cuando cualquiera de lo siguiente ocurre:

(a) Una soldadura de una pasada se coloca aislada, o

(b) Se ejerce un control térmico más estricto que el normalmente exigido.

Véase F.5.E.2.3, casos 1 y 2.

**Tabla F.5.C-1**

Esfuerzo límite $p_{w}$ del metal de aporte

| Metal de aporte |  | Metal base |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
| Tipo | Aleación | No tratable en caliente |  |  |  |  |  | Tratable en caliente |  |  |
|  |  | 1200 | 3103 | 5251 | 5454 |  | 5083 | 6063 | 6061 | 7020 |
|  |  |  | 3105 |  |  | 5154A |  |  | 6082 |  |
|  |  | kgf/mm2 | kgf/mm2 | kgf/mm2 | kgf/mm2 | kgf/mm2 | kgf/mm2 | kgf/mm2 | kgf/mm2 | kgf/mm2 |
| 1 | 1080A | 5.5 |  |  |  |  |  |  |  |  |
|  | 1050A | 5.5 |  |  |  |  |  |  |  |  |
| 3 | 3103 |  | 8.0 |  |  |  |  |  |  |  |
| 4 | 4043A | 7.0 | 9.0 |  |  |  |  | 15.0 | 19.0 |  |
|  | 4047A | 7.0 |  |  |  |  |  | 15.0 | 19.0 |  |
| 5 | 5356 |  |  | 20.0 | 21.5 | 21.5 | 24.5 | 15.5 | 20.5 | 25.5 |
|  | 5056A |  |  |  |  |  |  |  |  |  |
|  | 5183 |  |  | 20.0 | 21.5 | 21.5 | 27.5 | 16.5 | 22.0 | 26.5 |
|  | 5556A |  |  |  |  |  |  |  |  |  |
|  | 5554 1) |  |  |  | 19.0 |  |  |  |  |  |
|  | 5154A 1) |  |  |  |  | 21.0 |  |  |  |  |

1) Se deben usar estas aleaciones cuando la corrosión sea un posible problema.

NOTA. Cuando se usan metales base diferentes, se debe dar el menor valor de los dos esfuerzos límite al metal de aporte.
