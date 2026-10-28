"""Post 7: Come on down for big prizes (grand prize placeholder, free bubble tea, and more)."""
import math,re
exec(open('tools/build_posts_v2.py').read().split("OUT={}")[0])  # reuse HEAD, strip(), fine()
def star(n,R,r,cx,cy):
    pts=[]
    for i in range(n*2):
        rad=R if i%2==0 else r; ang=math.pi*i/n-math.pi/2
        pts.append(f"{cx+rad*math.cos(ang):.1f},{cy+rad*math.sin(ang):.1f}")
    return " ".join(pts)
cup=re.search(r'<svg class="bbt".*?</svg>',open('post-1-find-us.html').read(),re.S).group(0)
cup_hold=cup.replace('class="bbt"','class="cuphold"')
cup_card=cup.replace('class="bbt"','class="cupcard"')
pts=star(20,158,134,160,160)
css='''
.chip7{position:absolute;left:72px;top:128px;z-index:6;background:var(--teal);color:var(--pink);font-weight:900;font-size:38px;letter-spacing:.08em;padding:10px 28px;border-radius:14px;border:6px solid var(--white);box-shadow:0 7px 0 var(--black);transform:rotate(-2deg)}
.h7{position:absolute;left:68px;top:226px;z-index:4;font-weight:900;text-transform:uppercase;line-height:1;font-size:104px;color:var(--white);text-shadow:0 8px 0 var(--black);white-space:nowrap}
.h7 span{display:block}.h7 em{font-style:normal;color:var(--teal)}
.cuphold{position:absolute;z-index:5;left:768px;top:96px;width:84px;transform:rotate(-9deg);transform-origin:50% 100%}
.gp{position:absolute;z-index:3;left:56px;top:600px;width:968px;height:330px;background:var(--white);color:var(--pink);border-radius:34px;box-shadow:0 10px 0 var(--black);transform:rotate(-2deg);border:0}
.gp .coins{position:absolute;left:22px;top:14px;width:300px;height:300px;overflow:visible}
.gp .txt{position:absolute;left:340px;top:34px;right:30px}
.gp h2{font-weight:900;font-size:58px;line-height:1;margin-top:12px;letter-spacing:.01em}
.gp .gb{font-weight:900;font-size:98px;line-height:.92;margin-top:10px;color:var(--pink);letter-spacing:-.02em;text-transform:none}
.bbtcard{position:absolute;z-index:3;left:70px;top:960px;width:560px;height:236px;background:var(--teal);color:var(--pink);border-radius:30px;border:6px solid var(--white);box-shadow:0 9px 0 var(--black);transform:rotate(2deg);display:flex;align-items:center;gap:22px;padding:0 30px}
.cupcard{flex:none;width:118px;height:auto;margin-top:-34px}
.bbtcard .t1{font-weight:900;font-size:60px;line-height:.98}
.bbtcard .t1 small{display:block;font-size:30px;letter-spacing:.14em;color:var(--white);text-shadow:0 3px 0 var(--black);margin-bottom:4px}
.more{position:absolute;z-index:4;left:650px;top:900px;width:340px;height:340px;transform:rotate(8deg)}
.more svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.more div{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;text-align:center;font-weight:900;color:var(--pink);font-size:50px;line-height:1}
.more small{display:block;font-size:30px;letter-spacing:.06em}
.spk{position:absolute;fill:var(--white);z-index:2}
'''
body=f'''
<img class="logo" src="assets/logo-lockup-onpink.png" alt="giga! 5G+ feels good">
<div class="chip7">TECH SHOW 2026 PROMO</div>
<h1 class="h7"><span>Come on</span><span>down for</span><span><em>big prizes!</em></span></h1>
<img class="gino" src="assets/gino-wave.png" style="left:810px;top:190px;width:250px;z-index:4" alt="Gino waving">
{cup_hold}
<svg class="spk" style="left:620px;top:140px" width="60" height="60" viewBox="0 0 100 100"><path d="M50 0C54 30 70 46 100 50 70 54 54 70 50 100 46 70 30 54 0 50 30 46 46 30 50 0Z"/></svg>
<div class="gp"><svg class="coins" viewBox="0 0 300 300">
  <g transform="rotate(14 232 96)"><circle cx="232" cy="106" r="78" fill="#000"/><circle cx="232" cy="96" r="78" fill="#E5503D" stroke="#fff" stroke-width="8"/><circle cx="232" cy="96" r="58" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="5 7"/></g>
  <g transform="rotate(-8 140 168)"><circle cx="140" cy="182" r="122" fill="#000"/><circle cx="140" cy="168" r="122" fill="#FF6F5C" stroke="#fff" stroke-width="10"/><circle cx="140" cy="168" r="96" fill="none" stroke="#fff" stroke-width="4" stroke-dasharray="6 8"/>
   <text x="140" y="198" text-anchor="middle" font-family="Poppins" font-weight="900" font-size="76" fill="#000" letter-spacing="-2">$100</text><text x="140" y="191" text-anchor="middle" font-family="Poppins" font-weight="900" font-size="76" fill="#fff" letter-spacing="-2">$100</text>
   <path d="M60 110C70 70 110 46 150 46" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round" opacity=".55"/></g>
  <path d="M276 190C279 205 289 215 304 218 289 221 279 231 276 246 273 231 263 221 248 218 263 215 273 205 276 190Z" fill="#fff"/>
</svg><div class="txt"><h2>GRAND PRIZE</h2><div class="gb">gigaBucks<br>Credits</div></div></div>
<div class="bbtcard">{cup_card}<div class="t1"><small>FREE</small>BUBBLE<br>TEA!</div></div>
<div class="more"><svg viewBox="0 0 320 320"><polygon points="{pts}" transform="translate(0,12)" fill="#000"/><polygon points="{pts}" fill="#94E0E4" stroke="#fff" stroke-width="10" stroke-linejoin="round"/></svg><div><span>...AND<br>MORE!</span></div></div>
{strip('pink')}
{fine('Prizes and giveaways at The Tech Show 2026, 13–15 Nov, while stocks last. T&amp;Cs apply.')}'''
html=HEAD.format(t='Post 7: Come on down for big prizes',css=css,bg='background:var(--pink)',body=body)
open('post-7-big-prizes.html','w').write(html)
