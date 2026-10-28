"""Posts 2-6, v2: each post has its own composition. Shares fonts/vars via assets/common.css."""
HEAD='''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><title>{t}</title>
<link rel="stylesheet" href="assets/common.css">
<style>{css}</style></head>
<body><div class="post" id="post" style="{bg}">
{body}
</div></body></html>'''
def strip(color='pink', top=1254, left=72):
    w = 'var(--pink)' if color=='teal' else 'var(--white)'
    return f'''<div class="strip" style="top:{top}px;left:{left}px"><div class="booth"><small>BOOTH</small><strong>8428</strong></div>
<div class="when" style="color:{w}">13–15 Nov<span>Suntec City Convention Centre<br>Level 4</span></div></div>'''
def fine(txt,color='rgba(255,255,255,.92)'):
    return f'<div class="fine" style="color:{color}">{txt}</div>'
OUT={}

# ---------------- 2: TEASE (teal, offers lead, Gino supporting) ----------------
css2='''
.q{position:absolute;font-weight:900;color:rgba(255,255,255,.4);line-height:1}
.h2{position:absolute;left:72px;top:222px;z-index:4;font-weight:900;text-transform:uppercase;line-height:.92;color:var(--pink);-webkit-text-stroke:12px var(--white);paint-order:stroke fill;filter:drop-shadow(0 7px 0 var(--black))}
.h2 .a{font-size:122px;display:block}
.h2 .b{font-size:122px;display:block;margin-top:4px;letter-spacing:.01em}
.eyebrow{position:absolute;left:72px;top:130px;z-index:5;background:var(--pink);color:var(--white);font-weight:900;font-size:30px;letter-spacing:.12em;padding:8px 24px;border-radius:12px;border:5px solid var(--white);box-shadow:0 5px 0 var(--black);transform:rotate(-2deg)}
.offer{position:absolute;z-index:5;border-radius:34px;box-shadow:0 10px 0 var(--black);border:7px solid var(--white)}
.o1{left:56px;top:490px;width:968px;background:var(--pink);color:var(--white);transform:rotate(-2.5deg);padding:34px 44px 36px}
.o1 .l1{font-weight:900;font-size:56px;line-height:1}
.o1 .l2{font-weight:900;font-size:140px;line-height:.92;letter-spacing:-.01em;margin-top:4px}
.o1 .l3{display:inline-block;margin-top:14px;background:var(--teal);color:var(--pink);font-weight:900;font-size:38px;letter-spacing:.04em;padding:8px 22px;border-radius:14px}
.o2{left:56px;top:880px;width:620px;background:var(--white);color:var(--pink);transform:rotate(2deg);padding:28px 38px 30px}
.o2 .l1{font-weight:900;font-size:50px;line-height:1}
.o2 .row{display:flex;align-items:center;gap:22px;margin-top:10px}
.o2 .lock{flex:none;width:150px;height:150px}
.o2 .l2{font-weight:900;font-size:44px;line-height:1.05;color:var(--coral)}
.o2 .l3{font-weight:800;font-size:26px;color:#2a2a2a;margin-top:8px}
'''
b2=f'''
<img class="logo" src="assets/logo-lockup.png" alt="giga! 5G+ feels good" style="left:72px;top:52px;width:400px">
<div class="q" style="right:-60px;top:20px;font-size:520px;transform:rotate(14deg)">?</div>
<div class="eyebrow">PSST! BIG DEALS ARE COMING</div>
<h1 class="h2"><span class="a">Tech Show</span><span class="b">2026 Promo</span></h1>
<div class="offer o1"><div class="l1">BUY 1 MONTH,</div><div class="l2">GET 2 FREE!</div><div class="l3">AS LOW AS $5.30/MTH</div></div>
<div class="offer o2"><div class="l1">GOLDEN NUMBERS</div><div class="row"><svg class="lock" viewBox="0 0 100 100"><path d="M30 44V32a20 20 0 0 1 40 0v12" fill="none" stroke="#ED1285" stroke-width="10" stroke-linecap="round"/><rect x="18" y="42" width="64" height="48" rx="12" fill="#FF6F5C" stroke="#ED1285" stroke-width="6"/><circle cx="50" cy="63" r="7" fill="#fff"/><rect x="47" y="66" width="6" height="14" rx="3" fill="#fff"/></svg><div class="l2">PRICE<br>REVEALED<br>AT THE BOOTH</div></div></div>
<img class="gino" src="assets/gino-cool.png" style="left:745px;top:850px;width:230px;z-index:4" alt="Gino">
{strip('teal')}
{fine('Offers available at The Tech Show 2026, 13–15 Nov, while stocks last. T&amp;Cs apply.','rgba(0,0,0,.65)')}'''
OUT['post-2-tease']=HEAD.format(t='Post 2: Tease',css=css2,bg='background:var(--teal)',body=b2)

# ---------------- 3: WE'RE HERE (photo-forward + slanted panel) ----------------
css3='''
.photo{position:absolute;inset:0;background:repeating-linear-gradient(135deg,#F3E8EE 0 36px,#EBDDE5 36px 72px);display:flex;align-items:flex-start;justify-content:center}
.photo .frame{position:absolute;left:36px;right:36px;top:36px;height:900px;border:6px dashed var(--pink);border-radius:26px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;color:var(--pink);padding-bottom:140px}
.photo strong{font-weight:900;font-size:60px;letter-spacing:.1em}
.photo span{font-weight:700;font-size:28px;color:#2a2a2a;margin-top:10px}
.panel{position:absolute;left:0;bottom:0;width:1080px;height:700px;background:var(--pink);clip-path:polygon(0 17%,100% 0,100% 100%,0 100%);z-index:2}
.pill{position:absolute;z-index:6;background:var(--white);border-radius:60px;padding:12px 30px;box-shadow:0 6px 0 var(--black)}
.h3{position:absolute;left:64px;top:810px;z-index:5;font-weight:900;text-transform:uppercase;line-height:.88;color:var(--white);text-shadow:0 10px 0 var(--black);transform:rotate(-3deg);transform-origin:left top}
.h3 span{display:block;font-size:176px}
.h3 em{font-style:normal;color:var(--teal)}
.tc{position:absolute;right:56px;top:56px;z-index:6;background:var(--pink);color:var(--white);font-weight:900;font-size:30px;letter-spacing:.1em;padding:12px 28px;border-radius:14px;border:5px solid var(--white);box-shadow:0 6px 0 var(--black)}
'''
b3=f'''
<div class="photo" data-placeholder="booth-photo"><div class="frame"><strong>[ BOOTH PHOTO HERE ]</strong><span>Drop in the real booth photo on event day</span></div></div>
<div class="pill" style="left:56px;top:56px"><img src="assets/logo-lockup.png" style="display:block;width:380px" alt="giga! 5G+ feels good"></div>
<div class="tc">THE TECH SHOW 2026</div>
<div class="panel"></div>
<img class="gino" src="assets/gino-dance.png" style="left:700px;top:640px;width:380px;z-index:5" alt="Gino dancing">
<h1 class="h3"><span>We're</span><span><em>here!</em></span></h1>
{strip('pink',top=1262,left=64)}'''
OUT['post-3-were-here']=HEAD.format(t="Post 3: We're here",css=css3,bg='background:#EBDDE5',body=b3)

# ---------------- 4: EXCLUSIVE OFFERS (coupon tickets) ----------------
css4='''
.stripe{position:absolute;left:-100px;right:-100px;top:420px;height:760px;background:var(--teal);transform:rotate(-6deg);z-index:0}
.pre4{position:absolute;left:72px;top:134px;font-weight:800;font-size:38px;letter-spacing:.18em}
.h4{position:absolute;left:72px;top:184px;z-index:4;font-weight:900;text-transform:uppercase;line-height:1.02;font-size:118px;color:var(--white);text-shadow:0 8px 0 var(--black);white-space:nowrap}
.h4 span{display:block}.h4 em{font-style:normal;color:var(--teal)}
.ticket{position:absolute;z-index:3;width:900px;height:318px;background:var(--white);border-radius:26px;box-shadow:0 10px 0 var(--black);display:flex;color:var(--pink)}
.ticket .stub{width:210px;border-right:5px dashed var(--pink);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;font-weight:900}
.ticket .stub small{font-size:22px;letter-spacing:.16em}
.ticket .stub b{font-size:100px;line-height:1}
.ticket .main{flex:1;padding:26px 34px;display:flex;flex-direction:column;justify-content:center}
.ticket:before,.ticket:after{content:"";position:absolute;width:44px;height:44px;border-radius:50%;background:var(--bg-notch,var(--pink));top:calc(50% - 22px)}
.ticket:before{left:-22px}.ticket:after{right:-22px}
.t1{left:90px;top:440px;height:420px;transform:rotate(-3deg)}
.t1 .stub{width:200px}.t1 .stub b{font-size:130px}
.t2{left:90px;top:900px;height:250px;transform:rotate(2.5deg)}
.t2 .stub{width:150px}.t2 .stub b{font-size:76px}
.up{display:inline-block;position:relative;font-weight:800;font-size:34px;color:#555;margin-right:18px}
.up:after{content:"";position:absolute;left:-4px;right:-4px;top:52%;height:5px;background:var(--pink);transform:rotate(-6deg);border-radius:3px}
.k1{font-weight:900;font-size:46px;line-height:1.05}
.k2{font-weight:900;font-size:112px;line-height:.95;letter-spacing:-.01em}
.k3{font-weight:800;font-size:32px;color:#2a2a2a;margin-top:10px}
.t2 .k1{font-size:30px}.t2 .k3{font-size:24px;margin-top:4px}
'''
b4=f'''
<div class="stripe"></div>
<img class="logo" src="assets/logo-lockup-onpink.png" alt="giga! 5G+ feels good">
<div class="pre4">ONLY AT THE BOOTH</div>
<h1 class="h4"><span>Exclusive</span><span><em>offers!</em></span></h1>
<img class="gino" src="assets/gino-cart.png" style="left:775px;top:170px;width:270px;z-index:4" alt="Gino with shopping cart">
<div class="ticket t1"><div class="stub"><small>DEAL</small><b>1</b></div><div class="main"><div class="k1">BUY 1 MONTH, GET</div><div class="k2">2 MONTHS<br><span style="color:var(--coral)">FREE!</span></div><div class="k3">AS LOW AS $5.30/MTH</div></div></div>
<div class="ticket t2" style="--bg-notch:var(--teal)"><div class="stub"><small>DEAL</small><b>2</b></div><div class="main"><div class="k1">GOLDEN NUMBERS</div><div><span class="up">U.P. $298</span><span class="k2" style="font-size:96px;color:var(--coral)">$11.11</span></div><div class="k3">ONE-TIME PRICE</div></div></div>
{strip('pink')}
{fine('Buy 1 month, get 2 months free (prices as low as $5.30/mth). Golden Numbers at $11.11 one-time (U.P. $298). Booth exclusive, while stocks last. T&amp;Cs apply.')}'''
OUT['post-4-exclusive-offers']=HEAD.format(t='Post 4: Exclusive offers',css=css4,bg='background:var(--pink)',body=b4)

CSS5ADD=""".bg5{position:absolute;inset:0;z-index:0;background:radial-gradient(ellipse 760px 700px at 42% 58%,#FF6FB5 0%,#F43A9E 38%,#ED1285 65%,#D60F7A 100%)}
.rings{position:absolute;left:-260px;top:150px;width:1100px;height:1100px;z-index:1;border-radius:50%;border:0;background:repeating-radial-gradient(circle at center,rgba(255,255,255,.0) 0 62px,rgba(255,255,255,.13) 62px 66px)}
.halft{position:absolute;right:-40px;top:380px;width:520px;height:520px;z-index:1;background-image:radial-gradient(circle,rgba(255,255,255,.28) 0 5px,transparent 6px);background-size:34px 34px;-webkit-mask-image:radial-gradient(circle at 100% 40%,#000 0,transparent 70%);mask-image:radial-gradient(circle at 100% 40%,#000 0,transparent 70%)}
.vig{position:absolute;inset:0;z-index:1;background:linear-gradient(180deg,rgba(0,0,0,0) 70%,rgba(150,0,80,.18) 100%)}
"""
PTS5='380.0,8.0 426.4,57.3 484.8,23.1 515.4,83.5 581.1,67.1 593.5,133.6 661.1,136.4 654.2,203.8 718.4,225.5 692.8,288.2 748.2,327.1 706.0,380.0 748.2,432.9 692.8,471.8 718.4,534.5 654.2,556.2 661.1,623.6 593.5,626.4 581.1,692.9 515.4,676.5 484.8,736.9 426.4,702.7 380.0,752.0 333.6,702.7 275.2,736.9 244.6,676.5 178.9,692.9 166.5,626.4 98.9,623.6 105.8,556.2 41.6,534.5 67.2,471.8 11.8,432.9 54.0,380.0 11.8,327.1 67.2,288.2 41.6,225.5 105.8,203.8 98.9,136.4 166.5,133.6 178.9,67.1 244.6,83.5 275.2,23.1 333.6,57.3'
# ---------------- 5: GOLDEN NUMBERS (clean: one big starburst price sticker) ----------------
css5='''
.chip5{position:absolute;left:72px;top:128px;z-index:5;background:var(--teal);color:var(--pink);font-weight:900;font-size:38px;letter-spacing:.08em;padding:10px 28px;border-radius:14px;border:6px solid var(--white);box-shadow:0 7px 0 var(--black);transform:rotate(-2deg)}
.h5{position:absolute;left:72px;top:226px;z-index:4;font-weight:900;text-transform:uppercase;line-height:1.02;font-size:80px;color:var(--white);text-shadow:0 7px 0 var(--black);white-space:nowrap}
.h5 span{display:block}.h5 em{font-style:normal;color:var(--teal)}
.burstwrap{position:absolute;left:44px;top:430px;width:740px;height:740px;z-index:3;transform:rotate(-4deg)}
.burstwrap svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.burstin{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;color:var(--white)}
.burstin .gn{font-weight:900;font-size:46px;letter-spacing:.04em;text-shadow:0 5px 0 var(--black)}
.burstin .up{position:relative;display:inline-block;font-weight:800;font-size:46px;color:var(--white);opacity:.95;margin-top:6px}
.burstin .up:after{content:"";position:absolute;left:-8px;right:-8px;top:54%;height:7px;background:var(--black);transform:rotate(-5deg);border-radius:4px}
.burstin .pr{font-weight:900;font-size:230px;line-height:.95;letter-spacing:-.03em;text-shadow:0 12px 0 var(--black);margin-top:4px}
.burstin .ot{font-weight:900;font-size:36px;letter-spacing:.2em;color:var(--pink);background:var(--white);border-radius:12px;padding:6px 22px;margin-top:10px;box-shadow:0 5px 0 var(--black)}
.tagx{position:absolute;left:64px;top:470px;z-index:6;background:var(--teal);color:var(--pink);font-weight:900;font-size:30px;letter-spacing:.1em;padding:10px 24px;border-radius:12px;border:5px solid var(--white);box-shadow:0 6px 0 var(--black);transform:rotate(-8deg)}
.spk{position:absolute;fill:var(--white);z-index:2}
'''
b5=f'''
<img class="logo" src="assets/logo-lockup-onpink.png" alt="giga! 5G+ feels good">
<div class="chip5">TECH SHOW 2026 PROMO</div>
<h1 class="h5"><span>Golden numbers</span><span>are <em>running out!</em></span></h1>
<div class="burstwrap"><svg viewBox="0 0 760 760"><polygon points="__PTS__" transform="translate(0,16)" fill="#000"/><polygon points="__PTS__" fill="#FF6F5C" stroke="#fff" stroke-width="14" stroke-linejoin="round"/></svg>
<div class="burstin"><div class="up">U.P. $298</div><div class="pr">$11.11</div><div class="ot">ONE-TIME PRICE</div></div></div>
<img class="gino" src="assets/gino-phone.png" style="left:800px;top:920px;width:225px;z-index:5" alt="Gino with phone">
{strip('pink')}
{fine('Golden Numbers at $11.11 one-time price (U.P. $298). Booth exclusive at The Tech Show 2026, while stocks last. T&amp;Cs apply.')}'''.replace('__PTS__','__PTS_VAL__')
b5='<div class="bg5"></div><div class="rings"></div><div class="halft"></div><div class="vig"></div>'+b5
OUT['post-5-golden-numbers']=HEAD.format(t='Post 5: Golden numbers',css=css5+CSS5ADD,bg='background:var(--pink)',body=b5.replace('__PTS_VAL__',PTS5))

# ---------------- 6: LAST DAY (simplified: giant type, rocket Gino, one offer card) ----------------
css6='''
.chip6{position:absolute;left:72px;top:128px;z-index:6;background:var(--teal);color:var(--pink);font-weight:900;font-size:38px;letter-spacing:.08em;padding:10px 28px;border-radius:14px;border:6px solid var(--white);box-shadow:0 7px 0 var(--black);transform:rotate(-2deg)}
.h6{position:absolute;left:60px;top:240px;z-index:4;font-weight:900;text-transform:uppercase;line-height:.86;font-size:272px;color:var(--white);text-shadow:0 12px 0 var(--black);transform:rotate(-4deg);transform-origin:left top}
.h6 span{display:block}.h6 em{font-style:normal;color:var(--teal)}
.when6{position:absolute;left:72px;top:760px;z-index:4;font-weight:900;font-size:50px;line-height:1.1;color:var(--white);text-transform:uppercase}
.when6 span{display:block;font-size:30px;font-weight:800;color:var(--teal);margin-top:6px;letter-spacing:.04em}
.offer6{position:absolute;left:56px;top:1030px;width:968px;height:178px;z-index:6;background:var(--white);color:var(--pink);border-radius:28px;box-shadow:0 10px 0 var(--black);transform:rotate(-1deg);display:flex}
.offer6 > div{flex:1;padding:22px 32px;display:flex;flex-direction:column;justify-content:center}
.offer6 > div + div{border-left:5px dashed var(--pink)}
.offer6 .a{font-weight:900;font-size:40px;line-height:1.02}
.offer6 .a b{display:block;font-size:56px}
.offer6 .s{font-weight:800;font-size:24px;color:#2a2a2a;margin-top:4px}
.offer6 .p{font-weight:900;font-size:92px;line-height:.95;color:var(--coral);letter-spacing:-.02em}
'''
b6=f'''
<img class="logo" src="assets/logo-lockup-onpink.png" alt="giga! 5G+ feels good">
<div class="chip6">TECH SHOW 2026 PROMO</div>
<h1 class="h6"><span>Last</span><span><em>day!</em></span></h1>
<div class="when6">Sun 15 Nov<span>COME DOWN TO BOOTH 8428</span></div>
<img class="gino" src="assets/gino-rocket.png" style="left:665px;top:605px;width:370px;transform:rotate(10deg);z-index:5" alt="Gino rocket">
<div class="offer6"><div><div class="a">BUY 1 MONTH,<b>GET 2 FREE!</b></div><div class="s">As low as $5.30/mth</div></div><div><div class="a">GOLDEN NUMBERS</div><div class="pr6"><span class="p">$11.11</span><span class="up6">(U.P. $298)</span></div></div></div>
{strip('pink')}
{fine('Offers valid on 15 Nov only at The Tech Show 2026, booth 8428, while stocks last. Buy 1 month, get 2 months free (prices as low as $5.30/mth); Golden Numbers at $11.11 one-time (U.P. $298). T&amp;Cs apply.')}'''
CSS6ADD=""".pr6{display:flex;align-items:baseline;gap:14px}
.up6{position:relative;font-weight:800;font-size:26px;color:#555;white-space:nowrap}
.up6:after{content:"";position:absolute;left:-3px;right:-3px;top:54%;height:4px;background:var(--pink);transform:rotate(-5deg);border-radius:2px}
.bg6{position:absolute;inset:0;z-index:0;background:linear-gradient(155deg,#FF5FB0 0%,#ED1285 48%,#C90D74 100%)}
.moon{position:absolute;left:520px;top:430px;width:700px;height:700px;border-radius:50%;z-index:1;background:radial-gradient(circle at 35% 30%,rgba(255,255,255,.42),rgba(255,255,255,.12) 55%,rgba(255,255,255,0) 72%)}
.orbit{position:absolute;left:380px;top:300px;width:1000px;height:1000px;z-index:1;border-radius:50%;border:5px dashed rgba(255,255,255,.16);transform:rotate(-20deg)}
.stars6{position:absolute;inset:0;z-index:1;background-image:radial-gradient(circle,rgba(255,255,255,.55) 0 3px,transparent 4px);background-size:140px 140px;background-position:30px 40px;-webkit-mask-image:linear-gradient(135deg,transparent 35%,#000 100%);mask-image:linear-gradient(135deg,transparent 35%,#000 100%)}
"""
b6='<div class="bg6"></div><div class="moon"></div><div class="orbit"></div><div class="stars6"></div>'+b6
OUT['post-6-last-day']=HEAD.format(t='Post 6: Last day',css=css6+CSS6ADD,bg='background:var(--pink)',body=b6)

for n,h in OUT.items(): open(f'{n}.html','w').write(h)
print(list(OUT))
