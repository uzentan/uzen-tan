const { chromium } = require('playwright'); const path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage();await p.goto('file://'+path.resolve(process.argv[2]));
await p.evaluate(()=>document.fonts.ready);
console.log(await p.evaluate(()=>[...document.fonts].map(f=>f.family+' '+f.weight+' '+f.status).join('\n')));
console.log('headline width',await p.evaluate(()=>document.querySelector('.headline').getBoundingClientRect().width));
await b.close()})()
