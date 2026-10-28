"""Generates posts 2-6 (HTML) from one template so layout/style stay consistent with post 1."""
STRIP='''<div class="strip" style="top:1254px"><div class="booth"><small>BOOTH</small><strong>8428</strong></div>
<div class="when">13–15 Nov<span>Suntec Level 4 · Halls 401–406</span></div></div>'''
def page(title,body,fine=''):
    f=f'<div class="fine">{fine}</div>' if fine else ''
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><title>{title}</title>
<link rel="stylesheet" href="assets/common.css">
<style>{{CSS}}</style></head>
<body><div class="post" id="post">
<img class="logo" src="assets/logo-lockup-onpink.png" alt="giga! 5G+ feels good">
{body}
{STRIP}
{f}
</div></body></html>'''

posts={}

# ---- 2: tease
posts['post-2-tease']=page('Post 2: Tease',
'''<div class="pre" style="top:138px">SNEAK PEEK</div>
<h1 class="headline" style="top:190px;font-size:94px"><span>Big deals</span><span>are <em>coming!</em></span></h1>
<img class="gino" src="assets/gino-cool.png" style="left:800px;top:196px;width:230px" alt="Gino">
<div class="window" style="top:580px;height:660px">
 <div class="bar"><i></i><i></i><i></i><b>COMING TO THE TECH SHOW</b></div>
 <div class="screen" style="display:flex;flex-direction:column;gap:20px">
  <div class="deal" style="flex:1;padding:22px 30px"><span class="tag">DEAL #1</span>
   <div style="font-weight:900;font-size:46px;line-height:1.05;margin-top:14px">BUY 1 MONTH,<br><span style="font-size:76px">GET 2 FREE!</span></div>
   <div style="font-weight:800;font-size:28px;margin-top:8px;color:#2a2a2a">Prices as low as $5.30/mth</div></div>
  <div class="deal" style="flex:1;padding:22px 30px"><span class="tag">DEAL #2</span>
   <div style="font-weight:900;font-size:46px;line-height:1.05;margin-top:14px">GOLDEN NUMBERS<br><span style="font-size:76px;color:var(--coral)">$?.??</span></div>
   <div style="font-weight:800;font-size:28px;margin-top:8px;color:#2a2a2a">Price unlocked at booth 8428</div></div>
 </div></div>''',
'Offers available at The Tech Show 2026, 13–15 Nov, while stocks last. T&amp;Cs apply.')

# ---- 3: we're here (real photo placeholder)
posts['post-3-were-here']=page("Post 3: We're here",
'''<div class="pre" style="top:128px;font-size:36px">THE TECH SHOW 2026</div>
<h1 class="headline" style="top:176px;font-size:178px;line-height:.98"><span>We're</span><span><em>here!</em></span></h1>
<img class="gino" src="assets/gino-dance.png" style="left:690px;top:170px;width:340px" alt="Gino dancing">
<div class="window" style="top:600px;height:620px" data-placeholder="booth-photo">
 <div class="bar"><i></i><i></i><i></i><b>LIVE FROM BOOTH 8428</b></div>
 <div class="screen"><div class="ph"><strong>[ BOOTH PHOTO HERE ]</strong><span>Drop in the real booth photo on event day</span></div></div></div>''')

# ---- 4: exclusive offers
posts['post-4-exclusive-offers']=page('Post 4: Exclusive offers',
'''<div class="pre" style="top:138px;font-size:38px">ONLY AT THE BOOTH</div>
<h1 class="headline" style="top:186px;font-size:100px"><span>Exclusive</span><span><em>offers!</em></span></h1>
<img class="gino" src="assets/gino-cart.png" style="left:735px;top:238px;width:300px" alt="Gino with shopping cart">
<div class="window" style="top:560px;height:660px">
 <div class="bar"><i></i><i></i><i></i><b>BOOTH EXCLUSIVES</b></div>
 <div class="screen" style="display:flex;gap:20px">
  <div class="deal" style="flex:1;padding:24px 26px;text-align:center"><span class="tag">DEAL #1</span>
   <div style="font-weight:900;font-size:34px;line-height:1.1;margin-top:22px">BUY 1 MONTH,<br>GET</div>
   <div style="font-weight:900;font-size:88px;line-height:.95;margin-top:6px">2 MONTHS<br><span style="color:var(--coral)">FREE!</span></div>
   <div style="font-weight:800;font-size:26px;margin-top:22px;color:#2a2a2a">AS LOW AS</div>
   <div style="font-weight:900;font-size:60px;line-height:1">$5.30<span style="font-size:30px">/mth</span></div></div>
  <div class="deal" style="flex:1;padding:24px 26px;text-align:center"><span class="tag">DEAL #2</span>
   <div style="font-weight:900;font-size:36px;line-height:1.1;margin-top:22px">GOLDEN<br>NUMBERS</div>
   <div style="font-weight:900;font-size:124px;line-height:1;margin-top:26px;color:var(--coral);letter-spacing:-.02em">$11.11</div>
   <div style="font-weight:800;font-size:26px;margin-top:20px;color:#2a2a2a">ONE-TIME PRICE</div>
   <div style="font-weight:900;font-size:40px;margin-top:22px;letter-spacing:.06em">8888 8888</div></div>
 </div></div>''',
'Buy 1 month, get 2 months free (prices as low as $5.30/mth). Golden Numbers at $11.11 one-time. Booth exclusive, while stocks last. T&amp;Cs apply.')

# ---- 5: golden numbers running out
posts['post-5-golden-numbers']=page('Post 5: Golden numbers running out',
'''<div class="pre" style="top:136px;color:var(--teal)">HURRY!</div>
<h1 class="headline" style="top:190px;font-size:80px"><span>Golden numbers</span><span>are <em>running out</em></span></h1>
<div class="window" style="top:420px;height:790px">
 <div class="bar"><i></i><i></i><i></i><b>BOOTH 8428 · THE TECH SHOW</b></div>
 <div class="screen">
  <div style="position:absolute;left:30px;top:26px;width:520px;text-align:left">
   <span class="tag">GRAB YOURS</span>
   <div style="font-weight:900;font-size:36px;color:var(--pink);margin-top:20px;line-height:1">GOLDEN NUMBERS</div>
   <div style="font-weight:900;font-size:176px;line-height:1;color:var(--coral);-webkit-text-stroke:12px var(--white);paint-order:stroke fill;filter:drop-shadow(0 8px 0 var(--black));letter-spacing:-.02em;margin-top:6px">$11.11</div>
   <div style="font-weight:800;font-size:30px;color:var(--pink);margin-top:20px">ONE-TIME PRICE</div>
   <div class="deal" style="margin-top:26px;padding:16px 22px;text-align:center;font-weight:900;font-size:60px;letter-spacing:.06em;color:var(--coral)">8888 8888</div></div>
  <img src="assets/gino-phone.png" style="position:absolute;right:20px;bottom:150px;width:300px" alt="Gino with phone">
  <div style="position:absolute;left:30px;right:30px;bottom:26px">
   <div style="display:flex;justify-content:space-between;font-weight:900;font-size:24px;letter-spacing:.1em;color:var(--pink);margin-bottom:8px"><span>GOING FAST</span><span>GET THEM WHILE YOU CAN</span></div>
   <div style="height:34px;border-radius:17px;background:var(--white);border:4px solid var(--white);overflow:hidden"><div style="width:18%;height:100%;background:var(--pink)"></div></div></div>
 </div></div>''',
'Golden Numbers at $11.11 one-time price. Booth exclusive at The Tech Show 2026, while stocks last. T&amp;Cs apply.')

# ---- 6: last day
posts['post-6-last-day']=page('Post 6: Last day',
'''<div class="pre" style="top:136px;color:var(--teal)">FINAL CALL</div>
<div class="chip" style="right:72px;top:98px;transform:rotate(3deg)">SUN 15 NOV</div>
<h1 class="headline" style="top:186px;font-size:134px"><span>Last <em>day!</em></span></h1>
<div class="window" style="top:420px;height:790px">
 <div class="bar"><i></i><i></i><i></i><b>LAST CHANCE · BOOTH 8428</b></div>
 <div class="screen">
  <div class="deal" style="position:absolute;left:24px;top:24px;width:530px;padding:22px 26px"><span class="tag">DEAL #1</span>
   <div style="font-weight:900;font-size:36px;line-height:1.05;margin-top:12px">BUY 1 MONTH,</div>
   <div style="font-weight:900;font-size:68px;line-height:1">GET 2 FREE!</div>
   <div style="font-weight:800;font-size:26px;margin-top:6px;color:#2a2a2a">As low as $5.30/mth</div></div>
  <div class="deal" style="position:absolute;left:24px;top:290px;width:530px;padding:22px 26px"><span class="tag">DEAL #2</span>
   <div style="font-weight:900;font-size:36px;line-height:1.05;margin-top:12px">GOLDEN NUMBERS</div>
   <div style="font-weight:900;font-size:96px;line-height:1;color:var(--coral);letter-spacing:-.02em">$11.11</div>
   <div style="font-weight:800;font-size:26px;margin-top:2px;color:#2a2a2a">One-time price</div></div>
  <div style="position:absolute;left:24px;right:24px;bottom:22px;background:var(--pink);color:var(--white);border-radius:18px;border:5px solid var(--white);padding:12px 22px;font-weight:900;font-size:34px;text-align:center;letter-spacing:.04em">GONE WHEN THE SHOW ENDS!</div>
  <img src="assets/gino-rocket.png" style="position:absolute;right:6px;top:30px;width:330px;transform:rotate(4deg)" alt="Gino rocket">
 </div></div>''',
'Offers valid on 15 Nov only at The Tech Show 2026, booth 8428, while stocks last. Buy 1 month, get 2 months free (prices as low as $5.30/mth); Golden Numbers at $11.11 one-time. T&amp;Cs apply.')

for name,html in posts.items():
    open(f'{name}.html','w').write(html.replace('{CSS}',''))
print(list(posts))
