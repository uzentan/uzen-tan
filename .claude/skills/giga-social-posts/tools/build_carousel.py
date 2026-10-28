"""Post 8: gigaAI carousel (cover + 6 feature slides + CTA). 1080x1440, reuses brand system and supplied gigaAI screenshots."""
HEAD='''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><title>{t}</title>
<link rel="stylesheet" href="assets/common.css">
<style>{css}</style></head>
<body><div class="post" id="post" style="{bg}">
{body}
</div></body></html>'''
VENUE='Suntec City Convention Centre<br>Level 4'
def strip(color='pink',top=1254):
    w='var(--pink)' if color=='teal' else 'var(--white)'
    return f'''<div class="strip" style="top:{top}px"><div class="booth"><small>BOOTH</small><strong>8428</strong></div>
<div class="when" style="color:{w}">13–15 Nov<span>{VENUE}</span></div></div>'''
def fine(txt,color='rgba(255,255,255,.92)'):
    return f'<div class="fine" style="color:{color}">{txt}</div>'
CSS='''
.lg{position:absolute;left:56px;top:46px;z-index:6;background:var(--white);border-radius:22px;padding:6px 18px 2px;box-shadow:0 6px 0 var(--black)}
.lg img{display:block;width:210px;height:auto}
.pg{position:absolute;right:56px;top:62px;z-index:6;background:var(--white);color:var(--pink);font-weight:900;font-size:34px;letter-spacing:.06em;padding:8px 24px;border-radius:50px;box-shadow:0 6px 0 var(--black)}
.hd{position:absolute;left:72px;top:200px;z-index:4;font-weight:900;text-transform:uppercase;line-height:1.02;white-space:nowrap}
.hd span{display:block}
.hd.onpink{color:var(--white);text-shadow:0 8px 0 var(--black)}.hd.onpink em{font-style:normal;color:var(--teal)}
.hd.onteal{color:var(--pink);-webkit-text-stroke:8px var(--white);paint-order:stroke fill;filter:drop-shadow(0 6px 0 var(--black))}.hd.onteal em{font-style:normal;color:var(--pink)}
.sub{position:absolute;left:72px;right:72px;z-index:4;font-weight:700;font-size:30px;line-height:1.3}
.win{position:absolute;left:72px;width:936px;z-index:3;background:var(--white);border-radius:28px;overflow:hidden;box-shadow:0 10px 0 var(--black)}
.win .bar{height:52px}
.win .bar b{font-size:20px}
.win img{display:block;width:912px;margin:0 12px 12px;border-radius:14px}
.chips{position:absolute;left:72px;right:72px;z-index:4;display:flex;flex-wrap:wrap;gap:12px}
.chips span{background:var(--white);color:var(--pink);font-weight:800;font-size:24px;padding:8px 20px;border-radius:40px;box-shadow:0 5px 0 var(--black)}
'''
slides=[]
FEATS=[
 ('image-studio','IMAGE STUDIO',('Got an idea?','Just prompt it.'),'Describe any scene in your own words and Image Studio creates it in seconds.',['GPT Image 2.5','Nano Banana Pro','Seedream, FLUX & more'],'pink',-1.2),
 ('video-studio','VIDEO STUDIO',('Turn your ideas','into videos.'),'Describe a scene and Video Studio brings it to life. Then edit it with a prompt.',['Made with Seedance 2.5'],'teal',1.2),
 ('live-websites','LIVE WEBSITES',('Turn your ideas','into live websites.'),'Describe it in one sentence. gigaAI designs, builds and publishes it.',[],'pink',-1.0),
 ('slides','SLIDES',('Turn your ideas into','presentations.'),'Describe your topic and Slides builds a full deck you can edit, present or download.',[],'teal',1.2),
 ('multi-chat','MULTI CHAT',('Why ask one AI?','Ask them all.'),'Send one prompt to multiple AI models and compare every answer side by side.',['ChatGPT','Gemini','Claude','+ many more'],'pink',-1.2),
 ('experts','EXPERTS & LEGENDS',('Talk to experts.','Learn from legends.'),'Get advice from expert guides or chat with history\'s greatest minds, all in one place.',['ChatGPT','Gemini','Claude','+ many more'],'teal',1.0),
]
from PIL import Image
n=len(FEATS)
for i,(slug,label,(l1,l2),sub,chips,bg,tilt) in enumerate(FEATS, start=2):
    w,h=Image.open(f'assets/gigaai/{slug}.png').size
    imgh=round(912*h/w); winh=52+12+imgh
    on='onpink' if bg=='pink' else 'onteal'
    fs=80 if len(max(l1,l2,key=len))<=17 else 66
    subcol='var(--white)' if bg=='pink' else '#0c4f53'
    wintop=482
    chipstop=wintop+winh+34
    chiphtml=''.join(f'<span>{c}</span>' for c in chips)
    body=f'''
<div class="lg"><img src="assets/giga-ai-logo.svg" alt="gigaAI"></div>
<div class="pg">{i-1}/{n}</div>
<h1 class="hd {on}" style="font-size:{fs}px"><span>{l1}</span><span><em>{l2}</em></span></h1>
<p class="sub" style="top:{200+int(fs*2.1)+14}px;color:{subcol}">{sub}</p>
<div class="win" style="top:{wintop}px;height:{winh}px;transform:rotate({tilt}deg)"><div class="bar"><i></i><i></i><i></i><b>{label}</b></div><img src="assets/gigaai/{slug}.png" alt="{label}"></div>
{('<div class="chips" style="top:%dpx">%s</div>'%(chipstop,chiphtml)) if chips else ''}
{strip('teal' if bg=='teal' else 'pink')}
{fine('Try gigaAI at The Tech Show 2026, booth 8428. Features shown are examples of what gigaAI can do.','rgba(0,0,0,.65)' if bg=='teal' else 'rgba(255,255,255,.92)')}'''
    slides.append((f'post-8-giga-ai-{i:02d}-{slug}',HEAD.format(t=f'gigaAI: {label}',css=CSS,bg='background:var(--teal)' if bg=='teal' else 'background:var(--pink)',body=body)))

# cover
cover_css=CSS+'''
.cv-lg{position:absolute;left:56px;top:52px;z-index:6;background:var(--white);border-radius:28px;padding:10px 26px 4px;box-shadow:0 8px 0 var(--black)}
.cv-lg img{display:block;width:330px}
.cv-chip{position:absolute;right:56px;top:70px;z-index:6;background:var(--teal);color:var(--pink);font-weight:900;font-size:34px;letter-spacing:.08em;padding:10px 26px;border-radius:14px;border:6px solid var(--white);box-shadow:0 7px 0 var(--black);transform:rotate(3deg)}
.cv-h{position:absolute;left:68px;top:290px;z-index:4;font-weight:900;text-transform:uppercase;line-height:.95;color:var(--white);text-shadow:0 10px 0 var(--black)}
.cv-h span{display:block}.cv-h .a{font-size:170px;color:var(--teal)}.cv-h .b{font-size:170px}.cv-h .c{font-size:92px;margin-top:10px}
.feat{position:absolute;left:72px;top:830px;width:600px;z-index:4;display:flex;flex-wrap:wrap;gap:12px}
.feat span{background:var(--white);color:var(--pink);font-weight:800;font-size:25px;padding:8px 20px;border-radius:40px;box-shadow:0 5px 0 var(--black)}
.swipe{position:absolute;left:72px;top:1130px;z-index:5;background:var(--black);color:var(--white);font-weight:900;font-size:34px;letter-spacing:.04em;padding:12px 32px;border-radius:60px;border:6px solid var(--white)}
'''
feats=''.join(f'<span>{x}</span>' for x in ['Image Studio','Video Studio','Live Websites','Slides','Multi Chat','Experts & Legends'])
cover_body=f'''
<div class="cv-lg"><img src="assets/giga-ai-logo.svg" alt="gigaAI"></div>
<div class="cv-chip">TECH SHOW 2026</div>
<h1 class="cv-h"><span class="a">Try</span><span class="b">Giga AI</span><span class="c">at the booth!</span></h1>
<div class="feat">{feats}</div>
<img class="gino" src="assets/gino-phone.png" style="left:720px;top:820px;width:290px;z-index:5" alt="Gino with phone">
<div class="swipe">SWIPE TO SEE WHAT IT CAN DO →</div>
{strip('pink')}
{fine('Try gigaAI at The Tech Show 2026, booth 8428. Features shown are examples of what gigaAI can do.')}'''
slides.insert(0,('post-8-giga-ai-01-cover',HEAD.format(t='gigaAI: cover',css=cover_css,bg='background:var(--pink)',body=cover_body)))

# CTA
cta_css=CSS+'''
.cta-lg{position:absolute;left:56px;top:52px;z-index:6;background:var(--white);border-radius:28px;padding:10px 26px 4px;box-shadow:0 8px 0 var(--black)}
.cta-lg img{display:block;width:330px}
.cta-h{position:absolute;left:68px;top:270px;z-index:4;font-weight:900;text-transform:uppercase;line-height:.98;color:var(--pink);font-size:124px;-webkit-text-stroke:11px var(--white);paint-order:stroke fill;filter:drop-shadow(0 9px 0 var(--black))}
.cta-h span{display:block}
.cta-card{position:absolute;left:56px;top:720px;width:640px;z-index:5;background:var(--pink);color:var(--white);border-radius:32px;border:7px solid var(--white);box-shadow:0 10px 0 var(--black);padding:28px 36px;transform:rotate(-2deg)}
.cta-card .k{font-weight:900;font-size:36px;letter-spacing:.12em;color:var(--teal)}
.cta-card .b{font-weight:900;font-size:118px;line-height:1;letter-spacing:-.01em}
.cta-card .v{font-weight:800;font-size:30px;line-height:1.2;margin-top:6px}
'''
cta_body=f'''
<div class="cta-lg"><img src="assets/giga-ai-logo.svg" alt="gigaAI"></div>
<h1 class="cta-h"><span>Try giga AI</span><span>for yourself.</span></h1>
<div class="cta-card"><div class="k">COME DOWN TO</div><div class="b">BOOTH 8428</div><div class="v">Suntec City Convention Centre, Level 4<br>13–15 Nov 2026</div></div>
<img class="gino" src="assets/gino-wave.png" style="left:730px;top:760px;width:290px;z-index:5" alt="Gino waving">
{strip('teal')}
{fine('Try gigaAI at The Tech Show 2026, booth 8428. Features shown are examples of what gigaAI can do.','rgba(0,0,0,.65)')}'''
slides.append(('post-8-giga-ai-08-cta',HEAD.format(t='gigaAI: try it',css=cta_css,bg='background:var(--teal)',body=cta_body)))
for name,html in slides: open(f'{name}.html','w').write(html)
print([s[0] for s in slides])
