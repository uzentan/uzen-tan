"""Adds the subtle 'depth' overlay (glow + gradient) to posts that have a flat background. Idempotent. Run after the build scripts."""
import re,glob,sys
SKIP={'post-5-golden-numbers.html','post-6-last-day.html'}   # these carry their own layered backgrounds
for f in sorted(glob.glob('post-*.html')):
    if f in SKIP or f.endswith(('-v3.html','-v4-sunburst.html','-v6.html','-v9-placeholder.html','-teal-v1.html')): continue
    s=open(f).read()
    if 'class="depth' in s: continue
    m=re.search(r'<div class="post" id="post"([^>]*)>',s)
    if not m: continue
    teal='var(--teal)' in m.group(1)
    s=s.replace(m.group(0),m.group(0)+'\n<div class="depth%s"></div>'%(' teal' if teal else ''),1)
    if f=='post-3-were-here.html':
        s=s.replace('.panel{position:absolute;left:0;bottom:0;width:1080px;height:700px;background:var(--pink);','.panel{position:absolute;left:0;bottom:0;width:1080px;height:700px;background:linear-gradient(160deg,#F5329C 0%,#ED1285 55%,#DB0F7C 100%);')
    open(f,'w').write(s); print('depth ->',f,'teal' if teal else 'pink')
