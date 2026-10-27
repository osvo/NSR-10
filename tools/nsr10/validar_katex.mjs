// Valida con KaTeX todas las fórmulas $...$ y $$...$$ de los archivos Markdown dados.
// Uso: node tools/nsr10/validar_katex.mjs normativa/nsr10/titulo-c/*.md
import fs from 'fs';
import katex from '../../panel/node_modules/katex/dist/katex.mjs';
let malos = 0, total = 0; const avisos = [];
for (const f of process.argv.slice(2)) {
  const t = fs.readFileSync(f, 'utf8');
  const re = /\$\$([\s\S]+?)\$\$|\$([^$\n]+?)\$/g; let m;
  while ((m = re.exec(t))) {
    const ex = (m[1] || m[2]).replace(/\tag\{[^}]*\}/, '');
    total++;
    try { katex.renderToString(ex, { throwOnError: true, displayMode: !!m[1], strict: (c, msg) => { avisos.push(f.split(/[\/]/).pop() + ' | ' + ex.slice(0, 90) + ' | ' + msg.slice(0, 60)); return 'ignore'; } }); }
    catch (e) { malos++; console.log(f.split(/[\/]/).pop(), '|', ex.slice(0, 90), '|', e.message.slice(0, 80)); }
  }
}
avisos.forEach(a => console.log('aviso', a));
console.log('formulas', total, 'con error', malos, 'avisos', avisos.length);
