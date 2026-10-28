"""Builds the redrawn hall floor plan (SVG) for The Tech Show 2026 from hand-read coordinates
of the organiser's plan (source image px). Outputs assets/floorplan-hall.svg and assets/floorplan-zoom.svg."""
PINK="#ED1285"; TEAL="#94E0E4"

# (x0,y0,x1,y1)
B=[]
def b(x0,y0,x1,y1): B.append((x0,y0,x1,y1))
# row 85xx
for r in [(280,114,386,145),(388,114,435,145),(436,114,482,145),(484,114,580,145),(586,114,665,145),(686,114,740,145),(742,114,800,145),(802,114,892,145),(897,114,1000,145),(1004,114,1085,145),(1090,114,1175,145),(1182,114,1255,145)]: b(*r)
# row 84xx
for r in [(296,162,330,214),(330,162,360,214),
          (380,162,438,185),(438,162,468,185),(468,162,502,185),(380,185,452,214),(452,185,502,214),
          (523,162,567,188),(567,162,605,188),(605,162,645,214),(523,188,567,214),(567,188,605,214),
          (668,162,712,188),(712,162,740,188),(740,162,777,214),(668,188,740,214),
          (797,165,870,190),(797,190,845,214),
          (910,165,950,188),(950,165,985,188),(985,165,1013,188),(910,188,955,214),(955,188,1013,214),
          (1033,165,1100,188),(1100,165,1128,188),(1033,188,1128,214),
          (1143,162,1175,188),(1175,162,1190,188),(1190,162,1232,188),(1143,188,1232,214)]: b(*r)
# row 83xx
for r in [(297,237,353,288),(375,237,460,288),(468,237,553,288),(560,237,610,288),(610,237,655,288),(673,237,777,288),(800,237,870,288),
          (893,237,930,288),(930,237,970,288),(990,237,1107,288),(1128,237,1170,288),(1170,237,1213,288)]: b(*r)
# row 82xx
for r in [(297,310,328,410),(328,310,358,410),(378,310,415,402),(415,310,452,402),(462,310,476,345),(488,310,525,402),(525,310,562,402),
          (582,310,655,402),(697,310,770,402),(790,310,825,402),(825,310,860,402),(878,310,892,332),(898,310,968,402),
          (988,310,1075,402),(1105,310,1128,345),(1107,310,1157,402),(1177,310,1227,402)]: b(*r)
# row 81xx
for r in [(297,422,358,540),(365,422,407,540),(407,422,452,540),(475,422,505,540),(505,422,555,540),(575,422,673,540),(685,422,770,540),
          (790,422,830,540),(835,422,875,540),(898,422,968,540),(975,422,1038,540),(1057,422,1150,540),(1157,422,1196,540),(1196,422,1230,540)]: b(*r)
# slim bottom row + right column
for r in [(413,560,468,574),(498,560,555,574),(795,560,855,573),(910,560,965,573),(1180,560,1230,573),
          (1250,155,1280,235),(1252,237,1280,262),(1252,263,1280,288),(1253,345,1280,370)]: b(*r)

OURS=(845,190,895,222)  # booth 8428

def hall(extra=""):
    s=[]
    s.append(f'<rect x="62" y="85" width="1228" height="500" fill="#E4F9FA" stroke="{PINK}" stroke-width="4" rx="4"/>')
    s.append('<g stroke="#ED1285" stroke-width="1.6" stroke-dasharray="7 5" opacity=".45"><path d="M275 85V585M680 85V585M893 85V585"/></g>')
    s.append('<text x="167" y="345" text-anchor="middle" font-family="Poppins" font-weight="800" font-size="26" letter-spacing="3" fill="#ED1285" opacity=".55">GAME</text><text x="167" y="376" text-anchor="middle" font-family="Poppins" font-weight="800" font-size="26" letter-spacing="3" fill="#ED1285" opacity=".55">FEST</text>')
    for (x0,y0,x1,y1) in B:
        s.append(f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" fill="#fff" stroke="{PINK}" stroke-width="1.6" rx="2"/>')
    # entrance band
    s.append(f'<path d="M62 585H1290L1250 690H100Z" fill="#fff" stroke="{PINK}" stroke-width="3" stroke-linejoin="round"/>')
    for (cx,lab,sub) in [(258,"ENTRANCE / EXIT","406 · 405"),(672,"ENTRANCE / EXIT","404 & 403"),(1088,"ENTRANCE / EXIT","402 & 401")]:
        s.append(f'<text x="{cx}" y="627" text-anchor="middle" font-family="Poppins" font-weight="800" font-size="19" fill="{PINK}">{lab}</text>'
                 f'<text x="{cx}" y="652" text-anchor="middle" font-family="Poppins" font-weight="900" font-size="24" fill="{PINK}">{sub}</text>')
    s.append(extra)
    return "\n".join(s)

# our booth + callout (hall view)
x0,y0,x1,y1=OURS; cx,cy=(x0+x1)/2,(y0+y1)/2
ours=f'''<circle cx="{cx}" cy="{cy}" r="64" fill="{PINK}" opacity=".2"/>
<circle cx="{cx}" cy="{cy}" r="42" fill="none" stroke="{PINK}" stroke-width="7"/>
<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" fill="{PINK}" stroke="#fff" stroke-width="3" rx="3"/>
<g transform="translate({cx},{y1+54})"><rect x="-140" y="-21" width="280" height="42" rx="21" fill="{PINK}" stroke="#fff" stroke-width="4"/>
<text x="0" y="9" text-anchor="middle" font-family="Poppins" font-weight="900" font-size="25" fill="#fff" letter-spacing=".5">WE'RE HERE · 8428</text></g>'''

full=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="55 62 1240 640" width="1240" height="640">{hall(ours)}</svg>'
open('/home/user/uzen-tan/giga-tech-show/assets/floorplan-hall.svg','w').write(full)

# zoom inset: row 84 around 8428 with booth numbers
labs=[("8425",853,181),("8427",824,205),("8428",870,209),("8430",930,181),("8432",968,181),("8435",999,181),("8431",932,205),("8433",984,205)]
zx0,zy0,zw,zh=788,148,236,76
z=[f'<rect x="{zx0}" y="{zy0}" width="{zw}" height="{zh}" fill="#E4F9FA"/>']
for (x0_,y0_,x1_,y1_) in B:
    if x1_>zx0 and x0_<zx0+zw and y1_>zy0 and y0_<zy0+zh:
        z.append(f'<rect x="{x0_}" y="{y0_}" width="{x1_-x0_}" height="{y1_-y0_}" fill="#fff" stroke="{PINK}" stroke-width="1.4"/>')
ox0,oy0,ox1,oy1=OURS
z.append(f'<rect x="{ox0}" y="{oy0}" width="{ox1-ox0}" height="{oy1-oy0}" fill="{PINK}" stroke="#fff" stroke-width="2"/>')
for t,x,y in labs:
    fill="#fff" if t=="8428" else PINK
    wgt=900 if t=="8428" else 700
    sz=11 if t=="8428" else 9
    z.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Poppins" font-weight="{wgt}" font-size="{sz}" fill="{fill}">{t}</text>')
open('/home/user/uzen-tan/giga-tech-show/assets/floorplan-zoom.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{zx0} {zy0} {zw} {zh}" width="{zw*3}" height="{zh*3}">{"".join(z)}</svg>')
print(len(B),'booths')
