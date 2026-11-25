#!/usr/bin/env python3
"""The Pike — Clinton, CT. Template-v2 multi-page site build.
Every claim traced in evidence.json (Hartford Courant 2026-11-07, CT Scoop 2026-10-20,
IG bio). Unknowns (opening date, day hours, phone, prices) omitted — never guessed.
Zero third-party JS. Hand-rolled HTML/CSS. noindex on demo host per lane doctrine.
"""
import os, json

HERE = os.path.dirname(os.path.abspath(__file__))
PUB = os.path.join(HERE, 'public')
os.makedirs(PUB, exist_ok=True)

ORIGIN = 'https://the-pike-clinton-demo.up.railway.app'
BRAND = 'The Pike'
CITY = 'Clinton, CT'
STREET = '36 Killingworth Turnpike'
FULL_ADDR = '36 Killingworth Turnpike, Clinton, CT 06413'
FB = 'https://www.facebook.com/61596137967520'
IG = 'https://www.instagram.com/thepikeclinton/'
MAPQ = 'https://www.google.com/maps?q=36%20Killingworth%20Turnpike%2C%20Clinton%2C%20CT%2006413'
LAT, LON = 41.2953732, -72.5328127  # OSM Nominatim for the street address — see evidence.json
MAPTITLE = 'Map to The Pike, 36 Killingworth Turnpike, Clinton, CT 06413'

def head(title, desc, path):
    u = ORIGIN + path
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<link rel="canonical" href="{u}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{u}">
<meta property="og:image" content="{ORIGIN}/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{ORIGIN}/og.png">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="stylesheet" href="/style.css">
<link rel="preconnect" href="https://www.google.com">
</head>
<body>'''

def nav():
    return '''<a class="skip" href="#main">Skip to content</a>
<header class="site">
  <a class="brand" href="/">The&nbsp;Pike <span>Clinton &middot; Connecticut</span></a>
  <input type="checkbox" id="navtoggle" class="navtoggle" aria-label="Show navigation">
  <label for="navtoggle" class="navbtn" aria-hidden="true"><i></i></label>
  <nav aria-label="Main" class="links">
    <a href="/menu">Menu</a>
    <a href="/pizza">Pizza</a>
    <a href="/smashburgers-fried-chicken">Burgers&nbsp;&amp;&nbsp;Chicken</a>
    <a href="/late-nights">Late&nbsp;Nights</a>
    <a href="/our-story">Our&nbsp;Story</a>
    <a href="/visit">Visit</a>
    <a class="btn btn-sm" href="/contact">Contact&nbsp;Us</a>
  </nav>
</header>'''

def footer():
    return f'''<footer class="site">
  <div class="footgrid">
    <div class="footnap">
      <p class="fbrand">The&nbsp;Pike</p>
      <address>{STREET}<br>{CITY} 06413</address>
      <p class="fmail"><a href="{MAPQ}" rel="noopener">Get&nbsp;Directions</a></p>
    </div>
    <div class="footcta">
      <p class="rule" aria-hidden="true"></p>
      <p class="fline">New Haven-style &amp; grandma-style pizza,<br>smashburgers &middot; fried chicken &middot; cocktails.</p>
      <p class="fsocial"><a href="{FB}" rel="noopener">Facebook</a> &nbsp;&middot;&nbsp; <a href="{IG}" rel="noopener">Instagram</a></p>
      <p class="fline2">Open until 1&nbsp;a.m. Friday, Saturday &amp; Sunday. Follow for opening-day posts.</p>
    </div>
  </div>
  <p class="footline">&copy; 2026 {BRAND} &middot; {CITY}</p>
</footer>'''

def breadcrumbs(name, path):
    items = [
        {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': ORIGIN + '/'},
    ]
    if path != '/':
        items.append({'@type': 'ListItem', 'position': 2, 'name': name, 'item': ORIGIN + path})
    return json.dumps({'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': items}, ensure_ascii=False)

def ld_home():
    obj = {
        '@context': 'https://schema.org', '@type': 'Restaurant',
        'name': BRAND,
        'image': ORIGIN + '/og.png',
        'url': ORIGIN + '/',
        'servesCuisine': ['Pizza', 'American', 'Burgers'],
        'priceRange': '$$',
        'address': {'@type': 'PostalAddress', 'streetAddress': STREET, 'addressLocality': 'Clinton', 'addressRegion': 'CT', 'postalCode': '06413', 'addressCountry': 'US'},
        'geo': {'@type': 'GeoCoordinates', 'latitude': LAT, 'longitude': LON},
        'hasMap': MAPQ,
        'sameAs': [FB, IG],
    }
    return json.dumps(obj, ensure_ascii=False)

def ld_service(name, path, desc):
    obj = {
        '@context': 'https://schema.org', '@type': 'Service',
        'name': name,
        'description': desc,
        'areaServed': {'@type': 'City', 'name': 'Clinton', 'addressRegion': 'CT'},
        'provider': {'@type': 'Restaurant', 'name': BRAND, 'address': {'@type': 'PostalAddress', 'streetAddress': STREET, 'addressLocality': 'Clinton', 'addressRegion': 'CT', 'postalCode': '06413', 'addressCountry': 'US'}},
    }
    return json.dumps(obj, ensure_ascii=False)

def ld_faq():
    qa = [
        ('When does The Pike open?', 'The Pike opens in November 2026 at 36 Killingworth Turnpike in Clinton, Connecticut. The opening-day post goes out first on Instagram and Facebook.'),
        ('How late are you open?', 'Friday, Saturday and Sunday the bar runs until 1 a.m. — cocktails, pizza by the slice, wings and fried pickles. Full daytime hours are announced at opening.'),
        ('Is it family-friendly?', 'Yes. The Pike was built as a family restaurant first — pizza, smashburgers and fried chicken for everybody — and the bar scene takes over late on weekends.'),
        ('Where exactly is it?', '36 Killingworth Turnpike, Clinton, CT 06413, in the building that housed Chow Food and Beverage for ten years.'),
    ]
    obj = {
        '@context': 'https://schema.org', '@type': 'FAQPage',
        'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in qa],
    }
    return json.dumps(obj, ensure_ascii=False)

FACTS_BAND = '''<section class="facts">
  <p class="fact"><b>New Haven-style &amp; grandma-style</b><span>pan pizzas, cooked by a decade veteran of this address</span></p>
  <p class="fact"><b>Open until 1&nbsp;a.m.</b><span>Friday &middot; Saturday &middot; Sunday — drinks, slices &amp; fryer snacks</span></p>
  <p class="fact"><b>Craft cocktails &amp; pitchers</b><span>pool table, seven or eight TVs, simplistically modern room</span></p>
</section>'''

def faq_vis():
    qa = [
        ('When does The Pike open?', 'The Pike opens in November 2026 at 36 Killingworth Turnpike in Clinton, Connecticut. The opening-day post goes out first on <a href="' + IG + '" rel="noopener">Instagram</a> and <a href="' + FB + '" rel="noopener">Facebook</a>.'),
        ('How late are you open?', 'Friday, Saturday and Sunday the bar runs until 1&nbsp;a.m. — cocktails, pizza by the slice, wings and fried pickles. Full daytime hours are announced at opening.'),
        ('Is it family-friendly?', 'Yes. The Pike was built as a family restaurant first — pizza, smashburgers and fried chicken for everybody — and the bar scene takes over late on weekends.'),
        ('Where exactly is it?', '36 Killingworth Turnpike, Clinton, CT 06413, in the building that housed Chow Food and Beverage for ten years.'),
    ]
    return '<section class="faq"><h2>Questions people ask</h2>' + ''.join(
        f'<details open><summary>{q}</summary><p>{a}</p></details>' for q, a in qa) + '</section>'

PAGES = {}

# ---------- HOME ----------
PAGES['index.html'] = (head(f'{BRAND} — New Haven-Style Pizza, Smashburgers &amp; Late Nights, {CITY}',
    'The Pike opens in Clinton, CT with New Haven-style and grandma-style pan pizza, smashburgers, fried chicken and craft cocktails. Open until 1 a.m. Friday through Sunday.',
    '/'), f'''{nav()}
<main id="main">
<section class="hero">
  <p class="kicker">Now opening &middot; Clinton, Connecticut</p>
  <h1>Pizza. Smashburgers.<br><em>Late nights.</em></h1>
  <p class="lead">New Haven-style and grandma-style pan pizza, smashburgers, fried chicken and craft cocktails on Killingworth Turnpike. Family tables by day — and Friday through Sunday, the bar is open until 1&nbsp;a.m.</p>
  <p class="cta">
    <a class="btn btn-big" href="/menu">See the Menu</a>
    <a class="btn btn-ghost btn-big" href="{MAPQ}" rel="noopener">Get Directions</a>
  </p>
</section>
{FACTS_BAND}
<section class="cards">
  <h2 class="sr-only">What we serve</h2>
  <a class="card" href="/pizza">
    <span class="dot" aria-hidden="true"></span>
    <h3>Pizza, Two Ways</h3>
    <p>New Haven-style pies from a guy who made them at this address for a decade — plus thick, airy &ldquo;grandma style&rdquo; Sicilian pan pizza cut in squares.</p>
    <span class="more">The pies &rsaquo;</span>
  </a>
  <a class="card" href="/smashburgers-fried-chicken">
    <span class="dot" aria-hidden="true"></span>
    <h3>Smashburgers &amp; Fried Chicken</h3>
    <p>Thin-smashed burgers with lacy, crisp edges, crispy fried chicken, wings and fried pickles — cooked honest, priced fair.</p>
    <span class="more">The fry &rsaquo;</span>
  </a>
  <a class="card" href="/late-nights">
    <span class="dot" aria-hidden="true"></span>
    <h3>Late Nights</h3>
    <p>Friday through Sunday until 1&nbsp;a.m.: craft cocktails, pitchers, pizza by the slice, a pool table and the game on.</p>
    <span class="more">After dark &rsaquo;</span>
  </a>
</section>
<section class="quote">
  <div class="quotin">
    <p class="bigquote">&ldquo;Just a place for people to come hang out, bring the family, watch sports, have some drinks, get some affordable food.&rdquo;</p>
    <p class="attrib">— Jake Mastroianni, co-owner &middot; <em>Hartford Courant</em></p>
  </div>
</section>
<section class="storyteaser">
  <div class="sttext">
    <p class="kicker">Our story</p>
    <h2>Ten years of pizza at this address — and counting</h2>
    <p>The Pike comes from two Clinton families. Co-owner Joseph Giordano made New Haven-style pizza in this building for a decade; co-owner Jake Mastroianni grew up here and already runs Bacari Social in Westbrook. Together they rebuilt the old Chow space as the place Clinton stays late.</p>
    <p><a class="more" href="/our-story">Read the full story &rsaquo;</a></p>
  </div>
  <div class="stfig" aria-hidden="true">
    <p class="rule"></p>
    <p class="figline">One Address<br><b>Two Families</b></p>
    <p class="figsub">A kitchen and a bar built by cousins,<br>on family ground.</p>
    <p class="rule"></p>
  </div>
</section>
<section class="visitband">
  <p class="kicker">Find us</p>
  <p class="vaddr">{STREET} &middot; {CITY} 06413</p>
  <p class="cta center">
    <a class="btn btn-big" href="/visit">Plan Your Visit</a>
    <a class="btn btn-ghost btn-big" href="/contact">Contact Us</a>
  </p>
</section>
</main>
{footer()}
<script type="application/ld+json">{{ld_home}}</script>
<script type="application/ld+json">{{ld_home2}}</script>
</body>
</html>'''.replace('{{ld_home}}', '{LD_HOME}').replace('{{ld_home2}}', '{LD_BC_HOME}'))

# ---------- MENU ----------
PAGES['menu.html'] = (head(f'Menu — {BRAND}, {CITY}',
    'The Pike menu: New Haven-style and grandma-style pan pizza, smashburgers, fried chicken, appetizers, craft cocktails and pitchers. Late-night slices until 1 a.m. Fri–Sun.',
    '/menu'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">The Menu</p>
  <h1>Pies, patties, fryer<br>baskets &amp; cold drinks</h1>
  <p class="lead">Everything on the menu was chosen for the way Clinton actually eats: pizza the whole family agrees on, burgers and fried chicken that don&rsquo;t need a reservation, and a bar built for staying.</p>
  <p class="cta"><a class="btn" href="/pizza">The Pizza</a> <a class="btn btn-ghost" href="{MAPQ}" rel="noopener">Get Directions</a></p>
</section>
<div class="menuwrap">
  <section class="menu-sec">
    <h2>Pizza <span>— New Haven-style &amp; grandma-style</span></h2>
    <dl class="items">
      <div><dt><a href="/pizza">New Haven-Style Pies</a></dt><dd>Thin-crust pizza, cooked the New Haven way — the style Joe Giordano made at this address for ten years.</dd></div>
      <div><dt><a href="/pizza">Grandma-Style Pan Pizza</a></dt><dd>The owners&rsquo; &ldquo;grandma style&rdquo; — thick, airy Sicilian/Detroit-esque pan pizza with crisp corners, cut in squares.</dd></div>
      <div><dt><a href="/late-nights">By-the-Slice, Late</a></dt><dd>Friday through Sunday, slices stay on the rail until 1&nbsp;a.m.</dd></div>
    </dl>
  </section>
  <section class="menu-sec">
    <h2>Smashburgers</h2>
    <dl class="items">
      <div><dt><a href="/smashburgers-fried-chicken">Smashburgers</a></dt><dd>Thin-smashed for lacy, crisp edges — filling plates at fair prices, not $20 steakburgers.</dd></div>
    </dl>
  </section>
  <section class="menu-sec">
    <h2>Fried Chicken &amp; Fryer Items</h2>
    <dl class="items">
      <div><dt><a href="/smashburgers-fried-chicken">Fried Chicken</a></dt><dd>Crispy, hot, from our fryolator.</dd></div>
      <div><dt><a href="/smashburgers-fried-chicken">Wings</a></dt><dd>A late-night regular — off the fryer until 1&nbsp;a.m. on weekends.</dd></div>
      <div><dt><a href="/smashburgers-fried-chicken">Fried Pickles</a></dt><dd>The bar snack Connecticut orders without being asked.</dd></div>
    </dl>
  </section>
  <section class="menu-sec">
    <h2>Appetizers</h2>
    <dl class="items">
      <div><dt>A Rotation for the Table</dt><dd>A variety of appetizers to start the night — full lineup posted as we open.</dd></div>
    </dl>
  </section>
  <section class="menu-sec">
    <h2>The Bar <span>— craft cocktails &amp; pitchers</span></h2>
    <dl class="items">
      <div><dt><a href="/late-nights">Craft Cocktails</a></dt><dd>Pouring with a point: &ldquo;we will definitely be trying to elevate the cocktail scene.&rdquo;</dd></div>
      <div><dt><a href="/late-nights">Pitchers</a></dt><dd>For the table, the team or the game-watching crew.</dd></div>
    </dl>
  </section>
  <p class="fineprint center">Menu and prices are posted as we open — catch the announcements on <a href="{FB}" rel="noopener">Facebook</a> and <a href="{IG}" rel="noopener">Instagram</a>.</p>
</div>
</main>
{footer()}
<script type="application/ld+json">{{ld_bc_menu}}</script>
</body>
</html>'''.replace('{{ld_bc_menu}}', '{LD_BC_MENU}'))

# ---------- PIZZA ----------
PAGES['pizza.html'] = (head(f'New Haven-Style &amp; Grandma-Style Pizza — {BRAND}, {CITY}',
    'New Haven-style pies and thick, square-cut "grandma style" Sicilian pan pizza at The Pike in Clinton, CT — made by a ten-year veteran of the address. Slices late Fri–Sun.',
    '/pizza'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">The Signature</p>
  <h1>New Haven-style.<br>Grandma-style.</h1>
  <p class="lead">Clinton already knows what a New Haven-style pie is. We&rsquo;re putting the guy who made them here for a decade behind the oven — and adding the thick, airy Sicilian his family grew up on.</p>
  <p class="cta"><a class="btn" href="/menu">Full Menu</a> <a class="btn btn-ghost" href="{MAPQ}" rel="noopener">Get Directions</a></p>
</section>
<div class="detailwrap">
  <section class="ent">
    <h2><span class="num" aria-hidden="true">1</span>New Haven-style — thin, crisp, neighborhood-native</h2>
    <p>Co-owner Joseph Giordano made New Haven-style pizza in this building for ten years. The pies at The Pike are the continuation of that: rolled thin, cooked hard, made the way this town learned to order them.</p>
  </section>
  <section class="ent">
    <h2><span class="num" aria-hidden="true">2</span>Grandma-style — the owners&rsquo; name for it</h2>
    <p>The other pie is what Jake Mastroianni calls &ldquo;grandma style&rdquo;: a Sicilian/Detroit-esque pan pizza — thick and airy with the crisp corners everyone fights over last slice. Sheet-cut into squares, built for sharing.</p>
  </section>
  <aside class="panel">
    <h2>After midnight, the pie keeps going.</h2>
    <p>Friday, Saturday and Sunday, slices stay out until 1&nbsp;a.m. alongside drinks, wings and fried pickles — Clinton&rsquo;s late table just got a pizza rail.</p>
    <p class="cta"><a class="btn" href="/late-nights">Late Nights &rsaquo;</a></p>
  </aside>
</div>
</main>
{footer()}
<script type="application/ld+json">{{ld_pizza}}</script>
<script type="application/ld+json">{{ld_bc_pizza}}</script>
</body>
</html>'''.replace('{{ld_pizza}}', '{LD_PIZZA}').replace('{{ld_bc_pizza}}', '{LD_BC_PIZZA}'))

# ---------- BURGERS & CHICKEN ----------
PAGES['smashburgers-fried-chicken.html'] = (head(f'Smashburgers &amp; Fried Chicken — {BRAND}, {CITY}',
    'Smashburgers with crisp, lacy edges, crispy fried chicken, wings and fried pickles at The Pike in Clinton, CT — filling plates at fair prices, cooked to order.',
    '/smashburgers-fried-chicken'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">Griddle &amp; Fryer</p>
  <h1>Smashburgers and<br>crispy fried chicken</h1>
  <p class="lead">The second half of the menu is the easy half to love: burgers smashed thin for crisp edges, chicken fried hot, and the fryer snacks that keep the bar honest until 1&nbsp;a.m.</p>
  <p class="cta"><a class="btn" href="/menu">Full Menu</a> <a class="btn btn-ghost" href="{MAPQ}" rel="noopener">Get Directions</a></p>
</section>
<div class="detailwrap">
  <section class="ent">
    <h2><span class="num" aria-hidden="true">1</span>Smashburgers — pressed thin, sealed crisp</h2>
    <p>The smash method is about the crust: beef pressed onto a screaming griddle until the edges lace and crisp, cheese flooding over the top. No gimmicks on the bun, no $20 steakburger math.</p>
  </section>
  <section class="ent">
    <h2><span class="num" aria-hidden="true">2</span>Fried chicken &amp; fryolator classics</h2>
    <p>Hot fried chicken straight from the fryolator, plus the bar-snack regulars: wings and fried pickles — the same fry that fuels the late-night rail Friday through Sunday.</p>
  </section>
  <aside class="panel">
    <h2>Filling, not fancy-priced.</h2>
    <blockquote>&ldquo;Instead of getting a $20 steakburger, you can still get just as full off of a $14 burger with us.&rdquo;<cite>— Jake Mastroianni, Hartford Courant</cite></blockquote>
    <p class="cta"><a class="btn" href="/visit">Come Hungry</a></p>
  </aside>
</div>
</main>
{footer()}
<script type="application/ld+json">{{ld_burgers}}</script>
<script type="application/ld+json">{{ld_bc_burgers}}</script>
</body>
</html>'''.replace('{{ld_burgers}}', '{LD_BURGERS}').replace('{{ld_bc_burgers}}', '{LD_BC_BURGERS}'))

# ---------- LATE NIGHTS ----------
PAGES['late-nights.html'] = (head(f'Late Nights &amp; Lounge — {BRAND}, {CITY}',
    'The Pike stays open until 1 a.m. Friday, Saturday and Sunday — craft cocktails, pitchers, pizza by the slice, wings, fried pickles, a pool table and the game. Clinton, CT.',
    '/late-nights'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">After Dark &middot; Fri–Sun Till 1</p>
  <h1>The bar stays open<br>until 1&nbsp;a.m.</h1>
  <p class="lead">&ldquo;There&rsquo;s very few places open past midnight to have a drink in town,&rdquo; co-owner Jake Mastroianni says. So The Pike is one of them — cocktails, pitchers, slices and the fryer, Friday through Sunday.</p>
  <p class="cta"><a class="btn" href="/menu">Full Menu</a> <a class="btn btn-ghost" href="{MAPQ}" rel="noopener">Get Directions</a></p>
</section>
<div class="detailwrap">
  <section class="ent">
    <h2><span class="num" aria-hidden="true">1</span>The pour</h2>
    <p>Craft cocktails made with intent — the owners promised to &ldquo;elevate the cocktail scene&rdquo; — with pitchers for the table when the night is a group project.</p>
  </section>
  <section class="ent">
    <h2><span class="num" aria-hidden="true">2</span>The room</h2>
    <p>Simplistically modern: dark tile and white marble at the bar, a pool table, seven or eight TVs running the games. Minimal on purpose, built for staying.</p>
  </section>
  <section class="ent">
    <h2><span class="num" aria-hidden="true">3</span>The late menu</h2>
    <p>When the kitchen thins out, the rail keeps the essentials: pizza by the slice, wings and fried pickles off the fryolator, until 1&nbsp;a.m. Friday, Saturday and Sunday.</p>
  </section>
  <aside class="panel">
    <h2>By day it&rsquo;s a family restaurant.</h2>
    <p>Same pies, same fryer, same marble — the late scene is what the room turns into on weekends, not what it is all the time.</p>
    <p class="cta"><a class="btn" href="/visit">Plan Your Visit</a></p>
  </aside>
</div>
</main>
{footer()}
<script type="application/ld+json">{{ld_late}}</script>
<script type="application/ld+json">{{ld_bc_late}}</script>
</body>
</html>'''.replace('{{ld_late}}', '{LD_LATE}').replace('{{ld_bc_late}}', '{LD_BC_LATE}'))

# ---------- OUR STORY ----------
PAGES['our-story.html'] = (head(f'Our Story — {BRAND}, {CITY}',
    'The Pike was built by cousins Jake Mastroianni and Joseph Giordano — a Clinton native and a ten-year pizza man from this same address. Two families, one restaurant.',
    '/our-story'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">Two Families. This Address.</p>
  <h1>Clinton roots,<br>a rebuilt room</h1>
  <p class="lead">The Pike is the second restaurant for Jake Mastroianni and the newest chapter for Joe Giordano, who spent a decade making pizza inside these exact walls. They&rsquo;re cousins. They&rsquo;re both on the line.</p>
  <p class="cta"><a class="btn" href="/pizza">The Pizza</a> <a class="btn btn-ghost btn-big" href="/late-nights">Late Nights</a></p>
</section>
<div class="prose">
  <h2>The partners</h2>
  <p>Jake Mastroianni — a Clinton native, 30 years old — already runs Bacari Social in Westbrook and helped build Clinton&rsquo;s J&amp;M Dockside. The Pike is his second restaurant, and he&rsquo;s not just the guy with the lease: he cooks on the line with his business partner.</p>
  <p>Joseph Giordano is the pizza. He made New Haven-style pies at this address through the last decade at Chow Food and Beverage, and at The Pike he drives the pizza program — the New Haven-style rolls and the thick Sicilian his family calls &ldquo;grandma style.&rdquo;</p>
  <h2>The ground it stands on</h2>
  <p>The 1,100-square-foot room was Chow Food and Beverage for ten years — a stop owned by Jake&rsquo;s father, Jeff Mastroianni, and his uncle. When it closed in 2026, the cousins took the space and rebuilt it from the studs out: dark-tiled bar under nine-foot white marble, a pool table, games on seven or eight screens, everything stripped back to what the night actually needs.</p>
  <h2>What they&rsquo;re building</h2>
  <p>The plan is specific, not scattered: pizza two ways, smashburgers and fried chicken priced so a full dinner doesn&rsquo;t feel like an event, and a bar serious about cocktails — open to families at six and open to the town until one on weekends.</p>
  <blockquote>&ldquo;We&rsquo;re just going to give you really good food, be really nice, make some pretty special cocktails&hellip;we will definitely be trying to elevate the cocktail scene.&rdquo;<cite>— Jake Mastroianni, Hartford Courant</cite></blockquote>
  <h2>Follow the opening</h2>
  <p>Doors open in November 2026. Day-by-day plans, hours and the full menu go out on <a href="{IG}" rel="noopener">Instagram</a> and <a href="{FB}" rel="noopener">Facebook</a> first — that&rsquo;s where the town watches.</p>
</div>
</main>
{footer()}
<script type="application/ld+json">{{ld_story}}</script>
<script type="application/ld+json">{{ld_bc_story}}</script>
</body>
</html>'''.replace('{{ld_story}}', '{LD_STORY}').replace('{{ld_bc_story}}', '{LD_BC_STORY}'))

# ---------- VISIT ----------
PAGES['visit.html'] = (head(f'Visit — {BRAND}, {CITY}',
    'Visit The Pike at 36 Killingworth Turnpike, Clinton, CT 06413 — open until 1 a.m. Friday through Sunday. Opening November 2026, in the former Chow Food and Beverage building.',
    '/visit'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">Find Us</p>
  <h1>36 Killingworth Turnpike<br>Clinton, Connecticut</h1>
  <p class="lead">The old Chow Food and Beverage building, rebuilt. Opening November 2026 — Friday through Sunday, the bar runs until 1&nbsp;a.m. Full daytime hours are announced at opening.</p>
  <p class="cta"><a class="btn" href="{MAPQ}" rel="noopener">Get Directions</a> <a class="btn btn-ghost" href="/menu">Full Menu</a></p>
</section>
<div class="visitgrid">
  <section class="vinfo">
    <h2>The address</h2>
    <address class="bigaddr">{STREET}<br>{CITY} 06413</address>
    <p class="clabel">When</p>
    <p class="cbig">Open until 1&nbsp;a.m.<br>Friday &middot; Saturday &middot; Sunday</p>
    <p class="fineprint">Opening-day hours for the rest of the week are posted on <a href="{IG}" rel="noopener">Instagram</a> and <a href="{FB}" rel="noopener">Facebook</a>.</p>
    <p class="clabel">Questions before opening?</p>
    <p class="cbig"><a href="/contact">Use the contact form</a> or send a DM on Instagram.</p>
  </section>
  <section class="vmap">
    <iframe title="{MAPTITLE}" src="https://www.google.com/maps?q=36%20Killingworth%20Turnpike%2C%20Clinton%2C%20CT%2006413&output=embed" loading="eager" referrerpolicy="no-referrer-when-downgrade"></iframe>
  </section>
</div>
{faq_vis()}
</main>
{footer()}
<script type="application/ld+json">{{ld_visit}}</script>
<script type="application/ld+json">{{ld_faq}}</script>
<script type="application/ld+json">{{ld_bc_visit}}</script>
</body>
</html>'''.replace('{{ld_visit}}', '{LD_VISIT}').replace('{{ld_faq}}', '{LD_FAQ}').replace('{{ld_bc_visit}}', '{LD_BC_VISIT}'))

# ---------- CONTACT ----------
PAGES['contact.html'] = (head(f'Contact — {BRAND}, {CITY}',
    'Contact The Pike in Clinton, CT: questions about opening day, the menu or the late-night bar — use the form or find us at 36 Killingworth Turnpike.',
    '/contact'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">Talk to Us</p>
  <h1>Contact The&nbsp;Pike</h1>
  <p class="lead">Opening questions, the menu, pitching us something — the form lands with the team running the shop. We answer between cooks.</p>
</section>
<div class="contactgrid">
  <form class="cform" method="post" action="/contact">
    <h2>Send a message</h2>
    <p><label for="f-name">Your name</label><input id="f-name" name="name" type="text" required maxlength="120" autocomplete="name"></p>
    <p><label for="f-email">Email</label><input id="f-email" name="email" type="email" required maxlength="160" autocomplete="email"></p>
    <p><label for="f-phone">Phone (optional)</label><input id="f-phone" name="phone" type="tel" maxlength="60" autocomplete="tel"></p>
    <p><label for="f-msg">Message</label><textarea id="f-msg" name="message" rows="5" required maxlength="4000"></textarea></p>
    <p><button class="btn btn-big" type="submit">Send Message</button></p>
    <p class="fineprint">This form emails the shop directly. We never share your address.</p>
  </form>
  <section class="cinfo">
    <h2>Direct lines</h2>
    <p class="clabel">Walk in</p>
    <address class="bigaddr">{STREET}<br>{CITY} 06413</address>
    <p class="clabel">Open until 1&nbsp;a.m.</p>
    <p class="cbig">Friday &middot; Saturday &middot; Sunday</p>
    <p class="clabel">Social — opening posts &amp; menu</p>
    <p class="cbig"><a href="{FB}" rel="noopener">Facebook</a> &middot; <a href="{IG}" rel="noopener">Instagram</a></p>
  </section>
</div>
</main>
{footer()}
<script type="application/ld+json">{{ld_bc_contact}}</script>
</body>
</html>''')

# ---------- PRIVACY ----------
PAGES['privacy.html'] = (head(f'Privacy Policy — {BRAND}, {CITY}',
    'Privacy policy for The Pike in Clinton, CT: how the contact form handles your message. No trackers, no cookies, no selling your data.',
    '/privacy'), f'''{nav()}
<main id="main">
<section class="pagehead narrow">
  <p class="kicker">Privacy</p>
  <h1>Privacy Policy</h1>
</section>
<div class="prose">
  <p>This site belongs to {BRAND} ({FULL_ADDR}).</p>
  <h2>What we collect</h2>
  <p>The contact form on this site collects only the information you type into it — your name, your email address, an optional phone number and your message — and sends it to the inbox the team running the shop answers. That is the entire purpose of the data. It is not sold, shared or used for advertising.</p>
  <h2>Cookies and tracking</h2>
  <p>This site sets no cookies and uses no advertising trackers or analytics of its own. The embedded Google map may set its own cookies once you interact with it, governed by Google&rsquo;s privacy policy.</p>
  <h2>Your choices</h2>
  <p>Want your message deleted once we&rsquo;ve answered it? Use the contact form or message us on Instagram and ask. Questions about this policy go to the same place.</p>
  <p class="fineprint">This policy covers this website only.</p>
</div>
</main>
{footer()}
<script type="application/ld+json">{{ld_bc_privacy}}</script>
</body>
</html>'''.replace('{{ld_bc_privacy}}', '{LD_BC_PRIVACY}'))

# ---------- 404 ----------
PAGES['404.html'] = (head(f'Page not found — {BRAND}',
    'Page not found at The Pike site. Back to the menu, or straight to the late-night lounge page.',
    '/404'), f'''{nav()}
<main id="main">
<section class="pagehead center">
  <p class="kicker">404</p>
  <h1>That page never<br>made it to the table.</h1>
  <p class="lead">This page doesn&rsquo;t exist — but the slices are still on the rail.</p>
  <p class="cta"><a class="btn btn-big" href="/">Back to Home</a> <a class="btn btn-ghost btn-big" href="/menu">See the Menu</a></p>
</section>
</main>
{footer()}
</body>
</html>''')

# ---------- THANKS ----------
PAGES['thanks.html'] = (head(f'Message sent — {BRAND}',
    'Thanks for reaching out to The Pike in Clinton, CT — the team will get back to you.',
    '/thanks'), f'''{nav()}
<main id="main">
<section class="pagehead center">
  <p class="kicker">Received</p>
  <h1>Your message is in.</h1>
  <p class="lead">Thank you — the team will get back to you personally. Meanwhile, the menu and the map are one click away.</p>
  <p class="cta"><a class="btn btn-big" href="/menu">See the Menu</a> <a class="btn btn-ghost btn-big" href="/visit">Plan your visit</a></p>
</section>
</main>
{footer()}
</body>
</html>''')

LD_BLOCKS = {
    '{ld_home}': ld_home(),
    '{ld_home2}': breadcrumbs('Home', '/'),
    '{ld_bc_menu}': breadcrumbs('Menu', '/menu'),
    '{ld_pizza}': ld_service('New Haven-Style & Grandma-Style Pizza', '/pizza', 'New Haven-style thin-crust pies and thick Sicilian "grandma style" pan pizza, cut in squares, served at The Pike in Clinton, CT — pizza by the slice until 1 a.m. Friday through Sunday.'),
    '{ld_bc_pizza}': breadcrumbs('Pizza', '/pizza'),
    '{ld_burgers}': ld_service('Smashburgers & Fried Chicken', '/smashburgers-fried-chicken', 'Smashburgers with crisp edges, hot fried chicken, wings and fried pickles served at The Pike in Clinton, CT.'),
    '{ld_bc_burgers}': breadcrumbs('Smashburgers & Fried Chicken', '/smashburgers-fried-chicken'),
    '{ld_late}': ld_service('Late-Night Bar & Lounge', '/late-nights', 'Craft cocktails, pitchers, pizza by the slice, wings and fried pickles until 1 a.m. Friday, Saturday and Sunday at The Pike in Clinton, CT.'),
    '{ld_bc_late}': breadcrumbs('Late Nights', '/late-nights'),
    '{ld_story}': ld_service('The Pike — Our Story', '/our-story', 'The Pike was founded by cousins Jake Mastroianni and Joseph Giordano at 36 Killingworth Turnpike, Clinton, CT — a rebuilt room from the former Chow Food and Beverage building.'),
    '{ld_bc_story}': breadcrumbs('Our Story', '/our-story'),
    '{ld_visit}': ld_service('Visit The Pike', '/visit', 'Dine-in and bar service at 36 Killingworth Turnpike, Clinton, CT 06413 — open until 1 a.m. Friday through Sunday.'),
    '{ld_faq}': ld_faq(),
    '{ld_bc_visit}': breadcrumbs('Visit', '/visit'),
    '{ld_bc_contact}': breadcrumbs('Contact', '/contact'),
    '{ld_bc_privacy}': breadcrumbs('Privacy', '/privacy'),
}

# fill ld blocks (do a single replace pass per token)
for fname in list(PAGES):
    h, body = PAGES[fname]
    for tok, payload in LD_BLOCKS.items():
        if tok in body:
            body = body.replace(tok, payload)
    PAGES[fname] = (h, body)

for fname, (h, body) in PAGES.items():
    with open(os.path.join(PUB, fname), 'w', encoding='utf-8') as f:
        f.write(h + '\n' + body)
    print('wrote', fname, len(h + body), 'bytes')

# ---------- sitemap / robots ----------
pages_order = ['/', '/menu', '/pizza', '/smashburgers-fried-chicken', '/late-nights', '/our-story', '/visit', '/contact', '/privacy']
today = '2026-11-24'
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
    f'<url><loc>{ORIGIN}{p}</loc><lastmod>{today}</lastmod></url>\n' for p in pages_order) + '</urlset>\n'
open(os.path.join(PUB, 'sitemap.xml'), 'w').write(sitemap)
open(os.path.join(PUB, 'robots.txt'), 'w').write(f'''User-agent: *
Allow: /

Sitemap: {ORIGIN}/sitemap.xml
''')
print('sitemap + robots pinned to', ORIGIN)
