# NSR-10

Compilación del Reglamento Colombiano de Construcción Sismo Resistente NSR-10, con todas sus modificaciones y documentos de referencia.

**Sitio publicado:** [https://kmauqs.github.io/NSR-10/](https://kmauqs.github.io/NSR-10/)

Instrumentos incluidos:

- [Compilación navegable Ley 400 / NSR-10](https://kmauqs.github.io/NSR-10/consolidado-ley-400-nsr10.html)
- [Calculadora del espectro elástico A.2.6](https://kmauqs.github.io/NSR-10/espectro-diseno-nsr10.html)

![Poster-EVALQUAKE-NSR10](https://github.com/Kmauqs/NSR-10/blob/main/Poster-EVALQUAKE-NSR10.jpeg)

## NSR-10 en Markdown

[`normativa/nsr10`](normativa/nsr10/README.md) trae los once títulos (A a K) en Markdown,
consolidados con los decretos 092/2011, 340/2012, 945/2017, 2113/2019, 1711/2021 y 1580/2023,
incluido el Apéndice F.4-A. Hay un archivo por capítulo y un encabezado por artículo. Las ecuaciones
numeradas de A, B y C están en LaTeX con su número; las de D a K van como recorte exacto del PDF
mientras se cotejan una por una. Sirve para consultas rápidas, búsquedas con `grep` y lectura por
asistentes de IA.

Las herramientas para regenerarlo están en [`tools/nsr10`](tools/nsr10). El generador recibe una
carpeta con los PDF nombrados `FORK-DOC-NNN.pdf` (títulos de `Capitulos/` y anexos de
`Modificaciones/`); la correspondencia está en `tools/nsr10/generar.py` y en la línea `fuente:` de
cada archivo de `tools/nsr10/modificaciones/`.

```bash
uv run --with pymupdf==1.28.2 --with fonttools python tools/nsr10/generar.py <carpeta_fuentes>
```
