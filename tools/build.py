"""Rebuild the portable static portfolio from the approved project manifest.

Run with Python 3. No application framework or JavaScript build is required.
All internal links are relative, including nested project pages on GitHub Pages.
"""
from pathlib import Path
import json, html, re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT
PROJECTS = json.loads((ROOT / 'content/projects.json').read_text())
PORTRAIT = json.loads((ROOT / 'content/portrait.json').read_text())
EMAIL = 'odedipeoluwafemi@gmail.com'
BASE_URL = 'https://tradinggodmind.github.io/odedipe-architecture/'

def esc(s): return html.escape(str(s), quote=True)

def decorate(markup):
    arrows = {'↗':'M5 19 19 5M5 5h14v14', '←':'M20 12H4m0 0 7-7M4 12l7 7', '→':'M4 12h16m0 0-7-7m7 7-7 7', '↓':'M12 4v16m0 0-7-7m7 7 7-7', '↑':'M12 20V4m0 0-7 7m7-7 7 7'}
    parts = re.split(r'(<[^>]+>)', markup)
    for n in range(0,len(parts),2):
        for char,d in arrows.items():
            parts[n]=parts[n].replace(char,f'<svg class="svg-arrow" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.2"><path d="{d}"/></svg>')
    return ''.join(parts)
def path(prefix, s): return prefix + s

def picture(item, prefix='', sizes='100vw', eager=False, extra=''):
    avif = ', '.join(f'{prefix}{v["src"]} {v["width"]}w' for v in item.get('avif', []))
    webp = ', '.join(f'{prefix}{v["src"]} {v["width"]}w' for v in item['webp'])
    source = f'<source type="image/avif" srcset="{avif}" sizes="{sizes}">' if avif else ''
    return f'<picture>{source}<img src="{prefix}{item["src"]}" srcset="{webp}" sizes="{sizes}" width="{item["width"]}" height="{item["height"]}" alt="{esc(item.get("alt", "Odedipe Michael, architectural visualiser"))}" loading="{"eager" if eager else "lazy"}" decoding="async" {"fetchpriority=high" if eager else ""} {extra}></picture>'

def head(title, description, prefix='', canonical='', image_path='assets/cala-shell-residence/view1-1536.webp'):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(description)}"><meta name="theme-color" content="#293028">
<link rel="canonical" href="{BASE_URL}{canonical}"><meta property="og:type" content="website"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}"><meta property="og:url" content="{BASE_URL}{canonical}"><meta property="og:image" content="{BASE_URL}{image_path}"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="{prefix}assets/mark.svg"><link rel="preload" href="{prefix}assets/fonts/instrument-serif.woff2" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="{prefix}style.css"><script defer src="{prefix}app.js"></script></head><body id="top"><a class="skip" href="#main">Skip to content</a>'''

def header(prefix='', inner=False):
    return f'''<header class="site-header {'inner-header' if inner else ''}"><a class="brand" href="{prefix}index.html" aria-label="Odedipe Michael, home"><span class="brand-mark" aria-hidden="true">O/M</span><span class="brand-name">Odedipe<br>Michael</span></a><span class="header-role">Architectural visualisation<br>Form / Light / Atmosphere</span><div class="header-actions"><a class="enquire" href="mailto:{EMAIL}">Start a conversation ↗</a><button class="menu-toggle" aria-expanded="false" aria-controls="navigation"><span>Index</span><span class="menu-lines" aria-hidden="true"><i></i><i></i></span></button></div></header>
<dialog class="menu-panel" id="navigation" aria-label="Site navigation"><div class="menu-top"><a class="brand" href="{prefix}index.html"><span class="brand-mark">O/M</span><span class="brand-name">Odedipe<br>Michael</span></a><button class="menu-close" aria-label="Close navigation">Close &nbsp; ×</button></div><div class="menu-content"><nav class="menu-links" aria-label="Main navigation"><a href="{prefix}index.html#work"><span>01</span>Selected work</a><a href="{prefix}index.html#approach"><span>02</span>Approach</a><a href="{prefix}index.html#about"><span>03</span>About Michael</a><a href="{prefix}index.html#contact"><span>04</span>Get in touch</a></nav><div class="menu-note"><p>Architecture begins as an idea.<br>I give it light, material and presence.</p><a class="text-link" href="mailto:{EMAIL}">Discuss your project <span class="arrow">↗</span></a></div></div><div class="menu-bottom"><span>Architectural visualisation / Nigeria</span><span>15 concept studies · 2026</span></div></dialog>'''

def footer(prefix=''):
    return f'''<footer class="contact" id="contact"><div class="contact-top"><span class="label">A new perspective starts here</span><p>Have an architectural idea in mind?<br>Let’s find the image that makes it real.</p></div><a class="contact-title" href="mailto:{EMAIL}">Let’s make it <em>felt.</em> <span aria-hidden="true">↗</span></a><div class="contact-bottom"><a class="contact-email" href="mailto:{EMAIL}">{EMAIL}</a><a class="back-top" href="#top">Back to the top ↑</a></div><div class="legal"><p>© 2026 Odedipe Michael. Portfolio images are conceptual visualisations in proposed real-world settings. The projects shown are unbuilt studies.</p><a href="{prefix}index.html#work">Explore all 15 projects ↗</a></div></footer>'''

def lightbox():
    return '''<dialog class="lightbox" id="lightbox" aria-label="Project image viewer"><div class="lightbox-top"><span class="lightbox-count label"></span><button class="lightbox-zoom" aria-pressed="false">View detail +</button><button class="lightbox-close" aria-label="Close image viewer">Close ×</button></div><div class="lightbox-stage"><img class="lightbox-image" alt=""></div><div class="lightbox-bottom"><p class="lightbox-caption"><strong></strong><span></span></p><div class="lightbox-controls"><button data-prev aria-label="Previous image">←</button><button data-next aria-label="Next image">→</button></div></div></dialog>'''

def figure(item, number, prefix, eager=False, sizes='100vw'):
    return f'''<figure class="reveal"><button class="image-button" data-full="{prefix}{item['src']}" data-alt="{esc(item['alt'])}" data-title="{esc(item['title'])}" data-caption="{esc(item['caption'])}" aria-label="Enlarge {esc(item['title'])}">{picture(item,prefix,sizes,eager)}<span class="expand" aria-hidden="true">↗</span></button><figcaption class="image-caption"><div class="caption-label"><span class="label">{number}</span><span class="caption-title">{esc(item['title'])}</span></div><p>{esc(item['caption'])}</p></figcaption></figure>'''

CATEGORY_NAMES = {'Civic Landmark':'Landmarks','Skyscraper':'Towers','Mansion Villa':'Villas','Mansion':'Villas','Duplex':'Duplexes','Hotel':'Hotels','House':'Houses','Home':'Houses'}

def cat(p):
    c=p['category']
    return CATEGORY_NAMES.get(c, c+'s')

def home():
    hero=PROJECTS[6]
    intro=PROJECTS[0]['images'][2]
    order=[6,0,3,1,7,4,8,2,5,11,9,12,10,13,14]
    cards=[]
    for i in order:
        p=PROJECTS[i]; img=p['images'][0]
        cards.append(f'''<article class="project-card reveal {'portrait' if img['height']>img['width'] else ''}" data-category="{esc(cat(p))}" id="project-{p['id']}"><a class="cover-link" href="projects/{p['slug']}/" aria-label="Explore {esc(p['name'])}">{picture(img,sizes='(max-width:600px) calc(100vw - 44px), 55vw')}<span class="view-cue" aria-hidden="true">↗</span></a><div class="card-meta"><span>{p['id']} / {esc(p['category'])}</span><span>{esc(p['place'].split(',')[-1].strip())}</span></div><h3 class="card-title"><a href="projects/{p['slug']}/">{esc(p['name'])}</a></h3><p class="card-caption">{esc(img['caption'])}</p></article>''')
    filters='<button class="filter" data-filter="all" aria-pressed="true">All projects <sup>15</sup></button>'
    for c in ['Landmarks','Towers','Villas','Duplexes','Hotels','Houses']:
        count=sum(cat(p)==c for p in PROJECTS)
        if count:filters+=f'<button class="filter" data-filter="{c}" aria-pressed="false">{c} <sup>{count:02}</sup></button>'
    body=head('Odedipe Michael — Architectural Visualiser','An independent eye for architecture. Explore fifteen concept projects through exterior and interior visualisations, charcoal perspectives and drawing studies.')+header()
    body+=f'''<main id="main"><section class="hero" aria-label="Featured project, Cala Shell Residence"><div class="hero-visual">{picture(hero['images'][0],sizes='(max-width:600px) 1300px, 100vw',eager=True)}</div><p class="hero-kicker label">An independent eye<br>for extraordinary spaces.</p><h1 class="hero-title">Unbuilt.<em>Unforgettable.</em></h1><div class="hero-bottom"><div class="hero-project"><span class="number">07</span><div><strong>Cala Shell Residence</strong><span>Luštica Peninsula, Montenegro · Exterior study</span></div></div><a class="hero-scroll" href="#work">Discover the work<span aria-hidden="true">↓</span></a><a href="projects/cala-shell-residence/">Explore the project &nbsp; ↗</a></div></section>
<section class="section intro" aria-labelledby="intro-title"><span class="label">A practice in seeing<br>01 / Perspective</span><div><h2 id="intro-title">I turn architectural ideas into images that feel <em>inhabited, tangible,</em> and impossible to pass by.</h2><div class="intro-bottom"><p>I’m Odedipe Michael, an architectural visualiser. My work explores the moment when form, material and light become a place you can imagine yourself in.</p><a class="text-link" href="#about">The eye behind the image <span class="arrow">↗</span></a></div></div></section>
<section class="section work" id="work" aria-labelledby="work-title"><div class="section-heading"><h2 id="work-title">Selected work<span class="count">(15)</span></h2><span class="label">Concept studies<br>2026 collection</span></div><div class="filters" role="group" aria-label="Filter projects by type">{filters}<span class="filter-status" role="status" aria-live="polite">15 projects</span></div><div class="project-grid">{''.join(cards)}</div></section>
<figure class="interlude"><div class="interlude-image">{picture(intro,sizes='(max-width:600px) 960px, 100vw')}<p class="interlude-title">The quiet<br><em>inside the extraordinary.</em></p></div><figcaption class="interlude-caption"><span>01 / Crescent Current Centre<br>Lake foyer · Interior study</span><p>{esc(intro['caption'])}</p><a href="projects/crescent-current-centre/">View project ↗</a></figcaption></figure>
<section class="section process" id="approach"><div><span class="label">02 / The approach</span><h2>Every image.<br><em>A deliberate point of view.</em></h2></div><div class="process-list"><div class="process-step"><span class="label">01</span><div><h3>Read the architecture.</h3><p>Find the gesture that defines the project. Understand the approach, the threshold, and the spaces where its character comes into focus.</p></div></div><div class="process-step"><span class="label">02</span><div><h3>Give materials a voice.</h3><p>A stone edge catching sunlight. Timber grain at hand height. Fabric softening a monumental room. The atmosphere lives in these relationships.</p></div></div><div class="process-step"><span class="label">03</span><div><h3>Compose the experience.</h3><p>Choose the camera, light and moment together. Build a sequence that moves from the scale of a landscape to the intimacy of an interior.</p></div></div></div></section>
<section class="section about" id="about"><figure class="portrait-frame">{picture(PORTRAIT,sizes='(max-width:600px) 80vw, 42vw')}<figcaption><span>Odedipe Michael</span><span>Architectural visualiser</span></figcaption></figure><div><span class="label">03 / Behind the perspective</span><h2>A feeling<br><em>for space.</em></h2><p>I’m Michael, an architectural visualiser based in Nigeria. I’m drawn to expressive architecture and the quieter details that make a space believable.</p><p>From a sculptural landmark to a home at the edge of a forest, I bring a careful eye to proportion, atmosphere, furnishings and the way light meets a surface.</p><p>This collection follows fifteen concepts from drawn studies to finished exterior and interior imagery. Each is a different exploration of how architecture can be seen and felt.</p><ul class="services-list"><li><span>Exterior visualisation</span><span>01</span></li><li><span>Interior visualisation</span><span>02</span></li><li><span>Concept imagery &amp; presentation</span><span>03</span></li></ul><a class="text-link" href="mailto:{EMAIL}">Let’s discuss your vision <span class="arrow">↗</span></a></div></section></main>'''
    body+=footer()+'</body></html>'
    (OUT/'index.html').write_text(decorate(body))

def project(p, nxt):
    prefix='../../'
    lead=p['images'][0]
    out=head(p['name']+' — Odedipe Michael',p['description'],prefix,'projects/'+p['slug']+'/',lead['src'])+header(prefix,True)
    out+=f'''<main id="main"><section class="project-head"><div class="project-topline label"><a href="../../index.html#work">← All projects</a><span>Study {p['id']} / 15</span></div><h1>{esc(p['name'])}</h1><div class="project-subline"><span>{esc(p['place'])}</span><span>{esc(p['programme'])} · Concept visualisation · 2026</span></div></section><div class="project-hero {'tower' if lead['height']>lead['width'] else ''}">{figure(lead,'01',prefix,True)}</div>
<section class="project-story"><dl class="project-facts"><div><dt>Setting</dt><dd>{esc(p['place'])}</dd></div><div><dt>Typology</dt><dd>{esc(p['programme'])}</dd></div><div><dt>Work</dt><dd>Exterior &amp; interior visualisation<br>Perspective &amp; drawing studies</dd></div><div><dt>Status</dt><dd>Unbuilt concept</dd></div><div><dt>Collection</dt><dd>2026 · Study {p['id']}</dd></div></dl><div class="project-description"><h2>{esc(p['description'])}</h2><p>{esc(p['arrival'])}</p></div></section>
<section class="project-sequence" aria-label="Exterior and interior image sequence">{''.join(figure(i,str(n+2).zfill(2),prefix,sizes='100vw' if n==0 else '(max-width:600px) calc(100vw - 44px), 46vw') for n,i in enumerate(p['images'][1:4]))}</section>
<section class="material-note"><div><span class="label">Material &amp; atmosphere</span><h2>At the scale<br><em>of touch.</em></h2></div><p>{esc(p['palette'])} {esc(p['furniture'])}</p></section>
<section class="drawings" aria-labelledby="drawings-title"><div class="drawings-header"><h2 id="drawings-title">Behind the image.</h2><span class="label">Perspective / General arrangement</span></div><div class="drawing-grid">{figure(p['images'][4],'05',prefix,sizes='(max-width:600px) calc(100vw - 44px), 46vw')}<div>{figure(p['images'][5],'06',prefix,sizes='(max-width:600px) calc(100vw - 44px), 46vw')}<a class="text-link" href="{prefix}{p['downloads']['blueprint']}" target="_blank" rel="noopener">Open full-resolution drawing PDF <span class="arrow">↗</span></a></div></div><p class="drawing-note">Concept design studies for visual presentation. These drawings describe the proposed spatial arrangement and are not construction documents.</p></section>
<a class="next-project" href="../{nxt['slug']}/"><div><span class="label">Next perspective / {nxt['id']}</span><h2>{esc(nxt['name'])}</h2><span class="text-link">Explore the project <span class="arrow">↗</span></span></div>{picture(nxt['images'][0],prefix,sizes='(max-width:600px) 100vw, 50vw')}</a></main>'''
    out+=footer(prefix)+lightbox()+'</body></html>'
    folder=OUT/'projects'/p['slug'];folder.mkdir(parents=True,exist_ok=True);(folder/'index.html').write_text(decorate(out))

home()
for i,p in enumerate(PROJECTS): project(p,PROJECTS[(i+1)%len(PROJECTS)])
(OUT/'404.html').write_text(head('Page not found — Odedipe Michael','Return to the architecture portfolio.','/odedipe-architecture/')+header('/odedipe-architecture/',True)+'''<main class="error-page" id="main"><span class="label">404 / A different perspective</span><h1>This space<br><em>is still unbuilt.</em></h1><p>The page may have moved. The complete collection is waiting in the project index.</p><a class="text-link" href="/odedipe-architecture/index.html#work">Return to the work <span>↗</span></a></main>'''+footer('/odedipe-architecture/')+'</body></html>')
(OUT/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+BASE_URL+'sitemap.xml\n')
urls=[BASE_URL]+[BASE_URL+'projects/'+p['slug']+'/' for p in PROJECTS]
(OUT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+u+'</loc></url>' for u in urls)+'</urlset>')
print(f'Built homepage, {len(PROJECTS)} project pages and 404. All 90 project visuals included.')
