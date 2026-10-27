# NSR-10

Compilación del Reglamento Colombiano de Construcción Sismo Resistente NSR-10, con todas sus modificaciones y documentos de referencia.

**Sitio publicado:** [https://kmauqs.github.io/NSR-10/](https://kmauqs.github.io/NSR-10/)

Instrumentos incluidos:

- [Compilación navegable Ley 400 / NSR-10](https://kmauqs.github.io/NSR-10/consolidado-ley-400-nsr10.html)
- [Calculadora del espectro elástico A.2.6](https://kmauqs.github.io/NSR-10/espectro-diseno-nsr10.html)

![Poster-EVALQUAKE-NSR10](https://github.com/Kmauqs/NSR-10/blob/main/Poster-EVALQUAKE-NSR10.jpeg)

## NSR-10 en Markdown

[`normativa/nsr10`](normativa/nsr10/README.md) trae los Títulos A, B y C en Markdown,
consolidados con los decretos 092/2011, 340/2012, 945/2017, 2113/2019, 1711/2021 y 1580/2023.
Hay un archivo por capítulo y un encabezado por artículo, y las ecuaciones están en LaTeX con su número.
Sirve para consultas rápidas, búsquedas con `grep` y lectura por asistentes de IA.

Las herramientas para regenerarlo desde los PDF de este repositorio están en [`tools/nsr10`](tools/nsr10):

```bash
uv run --with pymupdf==1.28.2 --with fonttools python tools/nsr10/generar.py .
```
