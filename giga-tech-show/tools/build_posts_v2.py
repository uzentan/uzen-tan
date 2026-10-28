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
<div class="when" style="color:{w}">13–15 Nov<span>Suntec Level 4 · Halls 401–406</span></div></div>'''
def fine(txt,color='rgba(255,255,255,.92)'):
    return f'<div class="fine" style="color:{color}">{txt}</div>'
OUT={}

# ---------------- 2: TEASE (teal, offers lead, Gino supporting) ----------------
css2='''
.q{position:absolute;font-weight:900;color:rgba(255,255,255,.4);line-height:1}
.h2{position:absolute;left:72px;top:128px;z-index:4;font-weight:900;text-transform:uppercase;line-height:.92;color:var(--pink);-webkit-text-stroke:12px var(--white);paint-order:stroke fill;filter:drop-shadow(0 7px 0 var(--black))}
.h2 .a{font-size:150px;display:block}
.h2 .b{font-size:54px;display:block;margin-top:6px;letter-spacing:.01em}
.offer{position:absolute;z-index:5;border-radius:34px;box-shadow:0 10px 0 var(--black);border:7px solid var(--white)}
.o1{left:56px;top:430px;width:968px;background:var(--pink);color:var(--white);transform:rotate(-2.5deg);padding:34px 44px 36px}
.o1 .l1{font-weight:900;font-size:56px;line-height:1}
.o1 .l2{font-weight:900;font-size:150px;line-height:.92;letter-spacing:-.01em;margin-top:4px}
.o1 .l3{display:inline-block;margin-top:14px;background:var(--teal);color:var(--pink);font-weight:900;font-size:38px;letter-spacing:.04em;padding:8px 22px;border-radius:14px}
.o2{left:56px;top:830px;width:600px;background:var(--white);color:var(--pink);transform:rotate(2deg);padding:28px 38px 30px}
.o2 .l1{font-weight:900;font-size:50px;line-height:1}
.o2 .l2{font-weight:900;font-size:176px;line-height:.95;color:var(--coral);letter-spacing:-.02em;margin-top:2px}
.o2 .l3{font-weight:800;font-size:28px;color:#2a2a2a;margin-top:4px}
'''
b2=f'''
<img class="logo" src="assets/logo-lockup.png" alt="giga! 5G+ feels good" style="left:72px;top:52px;width:400px">
<div class="q" style="right:-60px;top:20px;font-size:520px;transform:rotate(14deg)">?</div>
<h1 class="h2"><span class="a">Psst!</span><span class="b">Big deals are coming</span></h1>
<div class="offer o1"><div class="l1">BUY 1 MONTH,</div><div class="l2">GET 2 FREE!</div><div class="l3">AS LOW AS $5.30/MTH</div></div>
<div class="offer o2"><div class="l1">GOLDEN NUMBERS</div><div class="l2">$?.??</div><div class="l3">Price unlocked at the booth</div></div>
<img class="gino" src="assets/gino-cool.png" style="left:735px;top:800px;width:240px;z-index:4" alt="Gino">
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
.ticket:before,.ticket:after{content:"";position:absolute;width:44px;height:44px;border-radius:50%;background:var(--bg-notch,var(--pink));top:137px}
.ticket:before{left:-22px}.ticket:after{right:-22px}
.t1{left:90px;top:470px;transform:rotate(-3deg)}
.t2{left:90px;top:810px;transform:rotate(3deg)}
.k1{font-weight:900;font-size:38px;line-height:1.05}
.k2{font-weight:900;font-size:86px;line-height:.98;letter-spacing:-.01em}
.k3{font-weight:800;font-size:28px;color:#2a2a2a;margin-top:8px}
'''
b4=f'''
<div class="stripe"></div>
<img class="logo" src="assets/logo-lockup-onpink.png" alt="giga! 5G+ feels good">
<div class="pre4">ONLY AT THE BOOTH</div>
<h1 class="h4"><span>Exclusive</span><span><em>offers!</em></span></h1>
<img class="gino" src="assets/gino-cart.png" style="left:775px;top:170px;width:270px;z-index:4" alt="Gino with shopping cart">
<div class="ticket t1"><div class="stub"><small>DEAL</small><b>1</b></div><div class="main"><div class="k1">BUY 1 MONTH, GET</div><div class="k2">2 MONTHS <span style="color:var(--coral)">FREE!</span></div><div class="k3">AS LOW AS $5.30/MTH</div></div></div>
<div class="ticket t2" style="--bg-notch:var(--teal)"><div class="stub"><small>DEAL</small><b>2</b></div><div class="main"><div class="k1">GOLDEN NUMBERS</div><div class="k2" style="font-size:120px;color:var(--coral)">$11.11</div><div class="k3">ONE-TIME PRICE</div></div></div>
{strip('pink')}
{fine('Buy 1 month, get 2 months free (prices as low as $5.30/mth). Golden Numbers at $11.11 one-time. Booth exclusive, while stocks last. T&amp;Cs apply.')}'''
OUT['post-4-exclusive-offers']=HEAD.format(t='Post 4: Exclusive offers',css=css4,bg='background:var(--pink)',body=b4)

# ---------------- 5: GOLDEN NUMBERS (giant price over number pattern) ----------------
css5='''
.pat{position:absolute;left:-80px;top:-60px;width:1300px;height:1500px;transform:rotate(-9deg);font-weight:900;font-size:128px;line-height:1.08;color:rgba(255,255,255,.14);letter-spacing:.04em;white-space:nowrap;overflow:hidden}
.pat div{margin-left:0}.pat div:nth-child(even){margin-left:-260px}
.burst{position:absolute;left:64px;top:150px;z-index:5;width:210px;height:210px;background:var(--teal);color:var(--pink);font-weight:900;font-size:44px;display:flex;align-items:center;justify-content:center;text-align:center;line-height:1;transform:rotate(-10deg);
 clip-path:polygon(50% 0,61% 9%,75% 5%,79% 19%,93% 21%,91% 35%,100% 46%,92% 58%,97% 72%,84% 77%,80% 91%,66% 88%,56% 100%,45% 90%,31% 96%,26% 82%,12% 81%,14% 67%,2% 57%,10% 46%,3% 33%,16% 28%,17% 14%,31% 15%,38% 3%)}
.gn{position:absolute;right:64px;top:176px;z-index:5;text-align:right;font-weight:900;font-size:64px;line-height:1;color:var(--white);text-shadow:0 6px 0 var(--black);letter-spacing:.02em}
.price{position:absolute;left:0;right:0;top:330px;text-align:center;z-index:5;font-weight:900;font-size:262px;line-height:1;color:var(--coral);-webkit-text-stroke:22px var(--white);paint-order:stroke fill;filter:drop-shadow(0 14px 0 var(--black));letter-spacing:-.03em}
.ot{position:absolute;left:0;right:0;top:640px;text-align:center;z-index:5;font-weight:800;font-size:34px;letter-spacing:.2em;color:var(--white)}
.band{position:absolute;left:-60px;right:-60px;top:720px;height:150px;background:var(--teal);z-index:4;transform:rotate(-3deg);display:flex;align-items:center;justify-content:center;font-weight:900;font-size:74px;color:var(--pink);letter-spacing:.02em;box-shadow:0 10px 0 var(--black);white-space:nowrap}
.num{position:absolute;z-index:5;background:var(--white);color:var(--coral);border-radius:22px;padding:14px 28px;font-weight:900;font-size:60px;letter-spacing:.06em;box-shadow:0 8px 0 var(--black);transform:rotate(4deg)}
.prog{position:absolute;z-index:5;left:430px;right:72px;top:1120px}
.prog .l{display:flex;justify-content:space-between;font-weight:900;font-size:22px;letter-spacing:.1em;color:var(--white);margin-bottom:8px}
.prog .t{height:30px;border-radius:15px;background:var(--white);overflow:hidden;border:4px solid var(--white)}
.prog .t i{display:block;width:16%;height:100%;background:var(--pink)}
'''
nums=''.join(f'<div>{"  ".join(["8888 8888","6666 6666","9999 9999","1111 1111"])}</div>' for _ in range(12))
b5=f'''
<div class="pat">{nums}</div>
<img class="logo" src="assets/logo-lockup-onpink.png" alt="giga! 5G+ feels good">
<div class="burst">HURRY!</div>
<div class="gn">GOLDEN<br>NUMBERS</div>
<div class="price">$11.11</div>
<div class="ot">ONE-TIME PRICE</div>
<div class="band">ARE RUNNING OUT!</div>
<img class="gino" src="assets/gino-phone.png" style="left:70px;top:880px;width:270px;z-index:5" alt="Gino with phone">
<div class="num" style="left:430px;top:930px">8888 8888</div>
<div class="prog"><div class="l"><span>GOING FAST</span><span>GRAB YOURS</span></div><div class="t"><i></i></div></div>
{strip('pink')}
{fine('Golden Numbers at $11.11 one-time price. Booth exclusive at The Tech Show 2026, while stocks last. T&amp;Cs apply.')}'''
OUT['post-5-golden-numbers']=HEAD.format(t='Post 5: Golden numbers',css=css5,bg='background:var(--pink)',body=b5)

# ---------------- 6: LAST DAY (giant type, diagonal rocket) ----------------
css6='''
.h6{position:absolute;left:52px;top:130px;z-index:4;font-weight:900;text-transform:uppercase;line-height:.84;font-size:318px;color:var(--pink);-webkit-text-stroke:20px var(--white);paint-order:stroke fill;filter:drop-shadow(0 12px 0 var(--black));transform:rotate(-5deg);transform-origin:left top}
.h6 span{display:block}
.date{position:absolute;right:56px;top:54px;z-index:6;background:var(--pink);color:var(--white);font-weight:900;font-size:44px;letter-spacing:.08em;padding:12px 32px;border-radius:16px;border:6px solid var(--white);box-shadow:0 7px 0 var(--black);transform:rotate(4deg)}
.trail{position:absolute;z-index:1;left:220px;top:640px;width:760px;height:560px}
.sticker{position:absolute;z-index:6;border-radius:26px;border:6px solid var(--white);box-shadow:0 8px 0 var(--black);font-weight:900;line-height:1.02;padding:20px 28px}
.s1{left:56px;top:1040px;width:470px;background:var(--pink);color:var(--white);font-size:44px;transform:rotate(-3deg)}
.s1 small{display:block;font-size:22px;color:var(--teal);margin-top:6px;letter-spacing:.06em}
.s2{left:560px;top:1060px;width:460px;background:var(--white);color:var(--pink);font-size:36px;transform:rotate(3deg)}
.s2 b{display:block;font-size:84px;color:var(--coral);letter-spacing:-.02em;margin-top:2px}
'''
b6=f'''
<img class="logo" src="assets/logo-lockup.png" alt="giga! 5G+ feels good" style="left:72px;top:52px;width:400px;z-index:6">
<div class="date">SUN 15 NOV</div>
<svg class="trail" viewBox="0 0 760 560" fill="none" stroke="#fff" stroke-width="10" stroke-linecap="round" stroke-dasharray="2 26"><path d="M20 540C180 520 330 420 470 300S700 100 740 20"/></svg>
<h1 class="h6" style="top:196px"><span>Last</span><span style="margin-left:90px">day!</span></h1>
<img class="gino" src="assets/gino-rocket.png" style="left:560px;top:560px;width:470px;transform:rotate(10deg);z-index:5" alt="Gino rocket">
<div class="sticker s1">BUY 1 MONTH, GET 2 FREE!<small>AS LOW AS $5.30/MTH</small></div>
<div class="sticker s2">GOLDEN NUMBERS<b>$11.11</b></div>
{strip('teal')}
{fine('Offers valid on 15 Nov only at The Tech Show 2026, booth 8428, while stocks last. Buy 1 month, get 2 months free (prices as low as $5.30/mth); Golden Numbers at $11.11 one-time. T&amp;Cs apply.','rgba(0,0,0,.65)')}'''
OUT['post-6-last-day']=HEAD.format(t='Post 6: Last day',css=css6,bg='background:var(--teal)',body=b6)

for n,h in OUT.items(): open(f'{n}.html','w').write(h)
print(list(OUT))
