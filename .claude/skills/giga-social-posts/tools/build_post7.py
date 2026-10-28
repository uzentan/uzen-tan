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
.gp{position:absolute;z-index:3;left:56px;top:600px;width:968px;height:330px;background:var(--white);color:var(--pink);border-radius:34px;box-shadow:0 10px 0 var(--black);transform:rotate(-2deg);padding:26px 40px;border:0}
.gp .tag{font-size:26px}
.gp h2{font-weight:900;font-size:62px;line-height:1;margin-top:10px;letter-spacing:-.005em}
.gp .prize{margin-top:12px;border-radius:18px;background:var(--teal);height:150px;display:flex;align-items:center;justify-content:center;gap:28px;padding:0 24px}
.gp .prize b{font-weight:900;font-size:158px;line-height:1;color:var(--coral);letter-spacing:-.03em;-webkit-text-stroke:9px var(--white);paint-order:stroke fill;filter:drop-shadow(0 6px 0 var(--black))}
.gp .prize span{font-weight:900;font-size:60px;line-height:.98;color:var(--pink);text-align:left}
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
<div class="gp"><span class="tag">WIN BIG</span><h2>GRAND PRIZE</h2><div class="prize"><b>$100</b><span>gigaBucks<br>Credits</span></div></div>
<div class="bbtcard">{cup_card}<div class="t1"><small>FREE</small>BUBBLE<br>TEA!</div></div>
<div class="more"><svg viewBox="0 0 320 320"><polygon points="{pts}" transform="translate(0,12)" fill="#000"/><polygon points="{pts}" fill="#94E0E4" stroke="#fff" stroke-width="10" stroke-linejoin="round"/></svg><div><span>...AND<br>MORE!</span></div></div>
{strip('pink')}
{fine('Prizes and giveaways at The Tech Show 2026, 13–15 Nov, while stocks last. T&amp;Cs apply.')}'''
html=HEAD.format(t='Post 7: Come on down for big prizes',css=css,bg='background:var(--pink)',body=body)
open('post-7-big-prizes.html','w').write(html)
