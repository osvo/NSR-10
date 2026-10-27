# NSR-10 en Markdown

Texto del Reglamento NSR-10 (Títulos A, B y C) **consolidado con sus decretos modificatorios**,
preparado para consulta rápida y para que un asistente de IA lo lea sin ruido.

| Título | Contenido | Ecuaciones en LaTeX |
|---|---|---|
| [A](titulo-a/README.md) | Requisitos generales de diseño y construcción sismo resistente (A.1–A.13 y apéndices A-1 a A-6) | 56 |
| [B](titulo-b/README.md) | Cargas (B.1–B.6) | 47 |
| [C](titulo-c/README.md) | Concreto estructural (C.1–C.23 y apéndices C-A a C-G), solo reglamento | 148 |

## Modificaciones incorporadas

Cada cambio aparece en el artículo afectado, con un recuadro que cita el decreto y la página de
su anexo técnico. Cuando el decreto dice «quedará así», el texto del artículo ya es el vigente.

| Decreto | Cambios en A, B y C | Ejemplos |
|---|---|---|
| 092 de 2011 | 154 | Combinaciones B.2.4 y C.9.2 (viento 1.0W y 0.5W), 29 municipios del Apéndice A-4, Tabla A.3-1 (muros de mampostería reforzada externamente), Tabla B.4.2.1-2 |
| 340 de 2012 | 32 | Efectos ortogonales A.3.6.3, Figura A.6.5-1, C.21.6.1.2 (relación de dimensiones de columnas), C.7.12.2.1 |
| 945 de 2017 | 63 | Supervisión técnica independiente (A.1), apéndices A-1, A-5 y A-6, supresión de la ecuación A.4.2-4, ℓdh de C.12.5.2, tolerancias C.6.5, 6 municipios nuevos |
| 2113 de 2019 | 2 | A.10.9.2.6 (patrimonio en adobe y tapia pisada), Resolución 0017 de 2017 |
| 1711 de 2021 | 7 | Supía (A-4), Apéndice A-5, mapa de amenaza eólica (Figura B.6.4-1) |
| 1580 de 2023 | 1 | A.10.9.2.7 (viviendas de mampostería, norma AIS 410-23); corrige el Decreto 1401 de 2023 |

No se incluyen el Apéndice F.4-A (Título F) del Decreto 1711 de 2021, el texto de las normas AIS
adoptadas por referencia (AIS 180-13, AIS 610-EP-17, AIS 410-23) ni la Resolución 1019 de 2024 del
Ministerio de Comercio, que es un reglamento de producto (alambre y mallas electrosoldadas,
NTC 5806) y no cambia el texto del reglamento. En octubre de 2026 no hay decretos posteriores a 2023
que modifiquen la NSR-10.

La tabla de municipios de la app (`panel/src/nsr10/municipios.js`) se genera desde el Apéndice A-4
consolidado: 1123 municipios.

## Cómo está organizado

- Un archivo por capítulo o apéndice (`A.02.md`, `C.21.md`, `C-F.md`). Sin páginas, encabezados,
  índices ni números de página.
- Encabezados por artículo (`### A.2.6`, `#### A.2.6.1`); los artículos más profundos van en
  negrita al inicio del párrafo (`**C.21.6.4.3**`), para buscarlos con `grep` o con la IA.
- Ecuaciones numeradas en LaTeX con su número: `$$ ... \tag{A.2.6-1} $$`. Las que aún no tienen
  transcripción van como recorte exacto del PDF en `img/`.
- Símbolos dentro del texto en `$...$` con subíndices ($A_a$, $V_{tj}$, $ℓ_o$).
- Tablas como tablas Markdown; figuras y recuadros complejos recortados del PDF en `img/`.

## Calidad

- Los símbolos de las fuentes Symbol y MT Extra se decodifican por subconjunto de fuente: cada
  subconjunto del PDF usa códigos propios y se traducen con el nombre de glifo de la fuente
  incrustada.
- `tools/nsr10/auditar.py` revisa tablas sin cuerpo, caracteres de control y fórmulas mal
  formadas. Resultado de esta versión: 0, 0 y 0.
- El Apéndice A-4 se reconstruye desde la geometría del PDF: los 1117 municipios originales
  coinciden con el PDF y las 36 correcciones o adiciones de los decretos 092, 945 y 1711 están
  aplicadas.
- `tools/nsr10/correcciones.json` guarda las correcciones literales (fracciones dentro del texto)
  verificadas contra el PDF, con su página.
- Ante una duda, prevalecen el PDF del reglamento y los anexos de los decretos.

## Regenerar

Fuentes: PDF del reglamento y anexos de los decretos en el fork NSR-10.

```bash
uv run --with pymupdf==1.28.2 --with fonttools python tools/nsr10/generar.py <carpeta_fuentes>
```

El proceso extrae los tres títulos, aplica las correcciones, reconstruye el Apéndice A-4 y
consolida los decretos de `tools/nsr10/modificaciones/` en orden cronológico.
