const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [,, file, out] = process.argv;
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1440 } });
  await p.goto('file://' + path.resolve(file));
  await p.evaluate(() => document.fonts.ready);
  await p.locator('#post').screenshot({ path: out });
  await b.close();
})();
