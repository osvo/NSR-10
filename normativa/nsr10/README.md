# NSR-10 en Markdown

Texto completo del Reglamento NSR-10 (Títulos A a K) **consolidado con sus decretos modificatorios**,
preparado para consulta rápida y para que un asistente de IA lo lea sin ruido.

| Título | Contenido | Ecuaciones numeradas |
|---|---|---|
| [A](titulo-a/README.md) | Requisitos generales de diseño y construcción sismo resistente (A.1–A.13 y apéndices A-1 a A-6) | 76 en LaTeX |
| [B](titulo-b/README.md) | Cargas (B.1–B.6) | 47 en LaTeX |
| [C](titulo-c/README.md) | Concreto estructural (C.1–C.23 y apéndices C-A a C-G), solo reglamento | 153 en LaTeX |
| [D](titulo-d/README.md) | Mampostería estructural (D.1–D.12 y apéndice D-1) | 86 en LaTeX |
| [E](titulo-e/README.md) | Casas de uno y dos pisos (E.1–E.9 y apéndices E-A y E-B) | 4 en LaTeX |
| [F](titulo-f/README.md) | Estructuras metálicas (F.1–F.5, Apéndice F.4-A y apéndices F.5-A a F.5-J) | 865 en LaTeX |
| [G](titulo-g/README.md) | Estructuras de madera y estructuras de guadua (G.1–G.12 y apéndices G-A a G-G) | 88 en LaTeX |
| [H](titulo-h/README.md) | Estudios geotécnicos (H.1–H.10) | 28 en LaTeX |
| [I](titulo-i/README.md) | Supervisión técnica independiente (I.1–I.5) | — |
| [J](titulo-j/README.md) | Requisitos de protección contra incendios en edificaciones (J.1–J.4) | 3 en LaTeX |
| [K](titulo-k/README.md) | Requisitos complementarios (K.1–K.4) | 18 en LaTeX |

Todas las ecuaciones de D a K se transcribieron desde la geometría del PDF
(`tools/nsr10/transcribir.py`) y se cotejaron una por una contra su recorte. Quedan como recorte
exacto del PDF solo 14 expresiones de ejemplos resueltos y celdas de tablas que mezclan fórmulas,
valores y texto (F.2, F.4, F.5, apéndices F.5-F y F.5-I, G-C).

El PDF del Título F del fork salta de la página F-396 a la F-439. Las 42 páginas que faltan (resto
de F.4.6, F.4.7 y F.4.8) se toman de la compilación completa `NSR10-Completa.pdf`.

## Modificaciones incorporadas

Cada cambio aparece en el artículo afectado, con un recuadro que cita el decreto y la página de
su anexo técnico. Cuando el decreto dice «quedará así», el texto del artículo ya es el vigente.

| Decreto | Cambios en A, B y C | Cambios en D a K | Ejemplos |
|---|---|---|---|
| 092 de 2011 | 154 | 359 | Combinaciones B.2.4 y C.9.2, 29 municipios del Apéndice A-4, Tabla A.3-1, Apéndice E-B, Título F, tablas de J.3 y K.4 |
| 340 de 2012 | 32 | 57 | Efectos ortogonales A.3.6.3, C.21.6.1.2, Apéndice G-F, grupos de ocupación del Título K |
| 945 de 2017 | 63 | 20 | Supervisión técnica independiente (A.1 y Capítulos I.1 a I.5), apéndices A-1, A-5 y A-6, «Supervisor Técnico Independiente» en F y G |
| 2113 de 2019 | 2 | — | A.10.9.2.6 (patrimonio en adobe y tapia pisada) |
| 1711 de 2021 | 7 | 1 | Supía (A-4), Apéndice A-5, mapa de amenaza eólica (Figura B.6.4-1), Apéndice F.4-A |
| 1580 de 2023 | 1 | — | A.10.9.2.7 (viviendas de mampostería, norma AIS 410-23); corrige el Decreto 1401 de 2023 |

No se incluyen el texto de las normas AIS adoptadas por referencia (AIS 180-13, AIS 610-EP-17,
AIS 410-23) ni la Resolución 1019 de 2024 del Ministerio de Comercio, que es un reglamento de
producto (alambre y mallas electrosoldadas, NTC 5806) y no cambia el texto del reglamento. En
octubre de 2026 no hay decretos posteriores a 2023 que modifiquen la NSR-10.

La tabla de municipios de la app (`panel/src/nsr10/municipios.js`) se genera desde el Apéndice A-4
consolidado: 1123 municipios.

## Cómo está organizado

- Un archivo por capítulo o apéndice (`A.02.md`, `C.21.md`, `C-F.md`, `F.4-A.md`). Sin páginas,
  encabezados, índices ni números de página.
- Encabezados por artículo (`### A.2.6`, `#### A.2.6.1`); los artículos más profundos van en
  negrita al inicio del párrafo (`**C.21.6.4.3**`), para buscarlos con `grep` o con la IA.
- Ecuaciones numeradas en LaTeX con su número: `$$ ... \tag{A.2.6-1} $$`. Las pocas expresiones
  que no caben en LaTeX con certeza van como recorte exacto del PDF en `img/`.
- Símbolos y fracciones dentro del texto en `$...$` ($A_a$, $V_{tj}$, $\frac{L}{r_x}$).
- Tablas como tablas Markdown; figuras, tablas con dibujos y páginas apaisadas recortadas del PDF
  en `img/`.

## Calidad

- Los símbolos de las fuentes Symbol y MT Extra se decodifican por subconjunto de fuente: cada
  subconjunto del PDF usa códigos propios y se traducen con el nombre de glifo de la fuente
  incrustada. MT Extra como fuente Type0 (ℓ, °, k̃) se traduce con su tabla de códigos.
- En D a K las fracciones apiladas dentro del texto se reconstruyen desde la barra dibujada en el
  PDF; las 70 resultantes se cotejaron contra su recorte.
- `tools/nsr10/auditar.py` revisa tablas sin cuerpo, caracteres de control y fórmulas mal
  formadas. Resultado de esta versión en los once títulos: 0, 0 y 0. KaTeX lee las 17 105
  fórmulas sin errores ni avisos (`tools/nsr10/validar_katex.mjs`).
- Verificación contra los PDF: no hay enlaces rotos ni imágenes sin usar; el texto conserva entre
  el 86 % y el 130 % de las palabras del PDF por título (las tablas y los decretos suman texto), y
  los artículos del PDF que no aparecen son los que los decretos eliminan o reemplazan
  (K.3.2.7.1–5, K.3.12.1.4–5, K.3.13.1.5, B.2.4.2.7 y los textos anteriores de A-1 y del Título I).
- El Apéndice A-4 se reconstruye desde la geometría del PDF: los 1117 municipios originales
  coinciden con el PDF y las 36 correcciones o adiciones de los decretos 092, 945 y 1711 están
  aplicadas.
- `tools/nsr10/correcciones.json` guarda las correcciones literales verificadas contra el PDF, con
  su página.
- Ante una duda, prevalecen el PDF del reglamento y los anexos de los decretos.

## Regenerar

Fuentes: PDF del reglamento y anexos de los decretos en el fork NSR-10.

```bash
uv run --with pymupdf==1.28.2 --with fonttools python tools/nsr10/generar.py <carpeta_fuentes>
```

El proceso extrae los once títulos, aplica las correcciones, reconstruye el Apéndice A-4 y
consolida los decretos de `tools/nsr10/modificaciones/` en orden cronológico.
