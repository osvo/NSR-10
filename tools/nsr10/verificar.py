"""Arma una página local para comparar cada ecuación candidata con su recorte del PDF.

Uso:
    python tools/nsr10/verificar.py <candidatas.json> <carpeta_img> <salida_dir>

Escribe <salida_dir>/index.html y datos.js. La página muestra, por fila, el número de la ecuación,
el recorte del PDF, la fórmula renderizada con KaTeX y las señales de sospechas.py. ?p=N&n=M pagina de M en M (12 por omisión); ?d=K&n=M muestra M desde la K; ?solo=sospechas muestra solo las que tienen señales. KaTeX se copia a <salida_dir>/katex.
"""
import json
import os
import shutil
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

from sospechas import sospechas  # noqa: E402

HTML = """<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Revisión de ecuaciones</title>
<link rel="stylesheet" href="katex/katex.min.css"><script src="katex/katex.min.js"></script><script src="datos.js"></script>
<style>body{font:13px system-ui;margin:8px;background:#fff;color:#111}table{border-collapse:collapse;width:100%}
td{border-bottom:1px solid #ccc;padding:2px 6px;vertical-align:middle}td.k{width:120px;font:11px monospace}
td.i img{max-width:380px;max-height:100px}td.r{font-size:13px}td.i{width:390px}.s{color:#b00;font-size:11px}.n{color:#666}</style></head>
<body><div id="cab"></div><table id="t"></table><script>
const q=new URLSearchParams(location.search),P=+(q.get('p')||0),N=+(q.get('n')||12);
let L=DATOS; if(q.get('solo')==='sospechas') L=L.filter(d=>d.s.length);
document.getElementById('cab').textContent=`página ${P} de ${Math.ceil(L.length/N)-1} · ${L.length} ecuaciones`;
const D=q.get('d')!==null?+q.get('d'):P*N;
for(const [i,d] of L.slice(D,D+N).entries()){const tr=document.createElement('tr');
 tr.innerHTML=`<td class="k">${D+i}<br>${d.k}<br><span class="s">${d.s.join('<br>')}</span></td><td class="i"><img src="${d.img}"></td><td class="r"></td>`;
 try{katex.render(d.l.replace(/\\\\tag\\{[^}]*\\}/,''),tr.children[2],{displayMode:true,throwOnError:true});}
 catch(e){tr.children[2].innerHTML='<span class="s">KaTeX: '+e.message.slice(0,90)+'</span>';}
 document.getElementById('t').appendChild(tr);}
</script></body></html>"""


def main(candidatas, carpeta_img, salida, manual=None):
    """manual: JSON {clave: latex} transcrito a mano; reemplaza a la candidata y se marca «manual»."""
    d = json.load(open(candidatas, encoding="utf-8"))
    m = json.load(open(manual, encoding="utf-8")) if manual and os.path.exists(manual) else {}
    os.makedirs(os.path.join(salida, "img"), exist_ok=True)
    katex = os.path.join(AQUI, "..", "..", "panel", "node_modules", "katex", "dist")
    if not os.path.isdir(os.path.join(salida, "katex")):
        shutil.copytree(katex, os.path.join(salida, "katex"))
    datos = []
    for k, v in d.items():
        origen = os.path.join(carpeta_img, v["archivo"])
        if os.path.exists(origen):
            shutil.copyfile(origen, os.path.join(salida, "img", v["archivo"]))
        if k in m:
            datos.append({"k": k, "l": m[k], "img": "img/" + v["archivo"], "s": ["manual"]})
        else:
            datos.append({"k": k, "l": v["latex"], "img": "img/" + v["archivo"], "s": sospechas(v)})
    open(os.path.join(salida, "datos.js"), "w", encoding="utf-8").write("const DATOS=" + json.dumps(datos, ensure_ascii=False) + ";")
    open(os.path.join(salida, "index.html"), "w", encoding="utf-8").write(HTML)
    print(f"{len(datos)} ecuaciones; {sum(bool(x['s']) for x in datos)} con señales")


if __name__ == "__main__":
    main(*sys.argv[1:5])
