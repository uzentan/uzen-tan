"""Post 5 v2: richer effects (extruded italic type, ghost numerals, sparkles, halftone, grain, glow) in pure HTML/CSS/SVG."""
def ext(n,color,dx=1,dy=1.15):
    return ','.join(f'{dx*i:.1f}px {dy*i:.1f}px 0 {color}' for i in range(1,n+1))
SPARK='<svg class="sp" style="{s}" viewBox="0 0 100 100"><path d="M50 0C53 32 68 47 100 50 68 53 53 68 50 100 47 68 32 53 0 50 32 47 47 32 50 0Z"/></svg>'
sp=''.join(SPARK.format(s=s) for s in [
 'left:940px;top:150px;width:96px','left:64px;top:690px;width:70px','left:612px;top:60px;width:60px','left:560px;top:880px;width:54px','left:40px;top:1090px;width:44px'])
grain="data:image/svg+xml;utf8,"+"<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .55 0'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>".replace('<','%3C').replace('>','%3E')
html=f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Post 5 v2: Golden numbers (effects)</title>
<style>
@font-face{{font-family:Poppins;font-weight:800;font-style:italic;src:url(assets/fonts/Poppins-ExtraBoldItalic.ttf)}}
@font-face{{font-family:Poppins;font-weight:900;font-style:italic;src:url(assets/fonts/Poppins-BlackItalic.ttf)}}
@font-face{{font-family:Poppins;font-weight:700;src:url(assets/fonts/Poppins-Bold.ttf)}}
@font-face{{font-family:Poppins;font-weight:800;src:url(assets/fonts/Poppins-ExtraBold.ttf)}}
@font-face{{font-family:Poppins;font-weight:900;src:url(assets/fonts/Poppins-Black.ttf)}}
:root{{--pink:#ED1285;--teal:#94E0E4;--deep:#9A0B58;--white:#fff}}
*{{box-sizing:border-box;margin:0;padding:0}}html,body{{background:#ddd}}
.post{{position:relative;width:1080px;height:1440px;overflow:hidden;font-family:Poppins,sans-serif;color:#fff;
 background:radial-gradient(ellipse 900px 800px at 55% 42%,#FF63B4 0%,#F52E9B 34%,#ED1285 60%,#C40A70 100%)}}
.band{{position:absolute;left:-120px;right:-120px;top:520px;height:420px;background:linear-gradient(90deg,rgba(120,0,66,.55),rgba(120,0,66,.15));transform:rotate(-8deg);z-index:0}}
.band2{{position:absolute;left:-120px;right:-120px;top:1010px;height:300px;background:rgba(120,0,66,.35);transform:rotate(-8deg);z-index:0}}
.ghost{{position:absolute;font-weight:900;font-style:italic;color:rgba(255,255,255,.11);letter-spacing:-.04em;line-height:.8;white-space:nowrap;z-index:0}}
.halft{{position:absolute;inset:0;z-index:1;background-image:radial-gradient(circle,rgba(255,255,255,.34) 0 4px,transparent 5px);background-size:30px 30px;
 -webkit-mask-image:radial-gradient(ellipse 520px 460px at 100% 30%,#000,transparent 72%);mask-image:radial-gradient(ellipse 520px 460px at 100% 30%,#000,transparent 72%)}}
.halft.b{{-webkit-mask-image:radial-gradient(ellipse 480px 420px at 0% 100%,#000,transparent 70%);mask-image:radial-gradient(ellipse 480px 420px at 0% 100%,#000,transparent 70%)}}
.grain{{position:absolute;inset:0;z-index:9;pointer-events:none;background-image:url("{grain}");mix-blend-mode:overlay;opacity:.38}}
.sp{{position:absolute;fill:#fff;z-index:6;filter:drop-shadow(0 0 14px rgba(255,255,255,.9))}}
.logo{{position:absolute;left:64px;top:50px;width:430px;z-index:6}}
.label{{position:absolute;left:64px;top:140px;z-index:6;background:var(--teal);color:var(--pink);font-weight:900;font-style:italic;font-size:34px;letter-spacing:.04em;padding:10px 34px;transform:skewX(-10deg);box-shadow:8px 8px 0 var(--deep)}}
.label span{{display:block;transform:skewX(10deg)}}
.h{{position:absolute;left:58px;top:238px;z-index:6;font-weight:900;font-style:italic;text-transform:uppercase;line-height:.98;font-size:100px;color:#fff;transform:rotate(-4deg);transform-origin:left top;text-shadow:{ext(9,'#9A0B58')},0 24px 30px rgba(90,0,50,.45)}}
.h span{{display:block}}.h em{{font-style:italic;color:var(--teal);text-shadow:{ext(9,'#0a6c74')},0 24px 30px rgba(0,60,70,.4)}}
.price{{position:absolute;left:30px;top:560px;z-index:6;font-weight:900;font-style:italic;font-size:360px;line-height:1;letter-spacing:-.045em;color:#fff;transform:rotate(-6deg);transform-origin:left top;
 text-shadow:{ext(16,'#9A0B58',1.1,1.3)},0 40px 50px rgba(80,0,45,.55)}}
.glow{{position:absolute;left:60px;top:560px;width:760px;height:380px;border-radius:50%;background:radial-gradient(closest-side,rgba(255,255,255,.55),rgba(255,255,255,0));z-index:2;filter:blur(8px)}}
.up{{position:absolute;left:660px;top:470px;z-index:7;font-weight:800;font-style:italic;font-size:46px;color:#fff;transform:rotate(-6deg);text-shadow:4px 4px 0 var(--deep)}}
.up:after{{content:"";position:absolute;left:-8px;right:-8px;top:54%;height:6px;background:var(--teal);transform:rotate(-4deg)}}
.otp{{position:absolute;left:92px;top:1000px;z-index:7;background:#fff;color:var(--pink);font-weight:900;font-style:italic;font-size:42px;letter-spacing:.04em;padding:10px 38px;transform:skewX(-10deg) rotate(-3deg);box-shadow:8px 8px 0 var(--deep)}}
.otp span{{display:block;transform:skewX(10deg)}}
.gino{{position:absolute;right:-30px;top:900px;width:400px;z-index:7;transform:rotate(-5deg);filter:drop-shadow(14px 18px 0 rgba(120,0,66,.55))}}
.booth{{position:absolute;left:64px;top:1170px;z-index:8;font-weight:900;font-style:italic;text-transform:uppercase;line-height:1}}
.booth .b{{display:inline-block;background:var(--teal);color:var(--pink);font-size:84px;padding:6px 40px 6px 30px;transform:skewX(-10deg);box-shadow:10px 10px 0 var(--deep)}}
.booth .b span{{display:inline-block;transform:skewX(10deg)}}
.booth .d{{display:block;width:620px;margin-top:22px;font-style:normal;font-weight:800;font-size:27px;line-height:1.22;color:#fff;text-shadow:3px 3px 0 var(--deep)}}
.fine{{position:absolute;left:64px;width:640px;bottom:24px;z-index:8;font-weight:700;font-size:17px;color:rgba(255,255,255,.9)}}
</style></head><body><div class="post" id="post">
<div class="band"></div><div class="band2"></div>
<div class="ghost" style="left:520px;top:-10px;font-size:400px;transform:rotate(-8deg)">11.11</div>
<div class="ghost" style="left:-30px;top:1000px;font-size:430px;transform:rotate(-8deg)">11.11</div>
<div class="halft"></div><div class="halft b"></div>
<img class="logo" src="assets/logo-lockup-onpink.png" alt="giga! 5G+ feels good">
<div class="label"><span>TECH SHOW 2026 PROMO</span></div>
<h1 class="h"><span>Golden numbers</span><span>are <em>running out!</em></span></h1>
<div class="glow"></div>
<div class="price">$11.11</div>
<div class="up">U.P. $298</div>
<div class="otp"><span>ONE-TIME PRICE</span></div>
{sp}
<img class="gino" src="assets/gino-phone.png" alt="Gino with phone">
<div class="booth"><span class="b"><span>BOOTH 8428</span></span><span class="d">13–15 NOV<br>SUNTEC CITY CONVENTION CENTRE, LEVEL 4</span></div>
<div class="fine">Golden Numbers at $11.11 one-time price (U.P. $298). Booth exclusive at The Tech Show 2026, while stocks last. T&amp;Cs apply.</div>
<div class="grain"></div>
</div></body></html>'''
open('post-5-v2-fx.html','w').write(html)
