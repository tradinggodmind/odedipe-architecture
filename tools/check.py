"""Validate output completeness and relative links without a browser."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT.resolve()
errors=[]
class Check(HTMLParser):
    def __init__(self,p): super().__init__(); self.p=p;self.images=0;self.captions=0;self.h1=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='h1':self.h1+=1
        if tag=='figcaption':self.captions+=1
        for key in ['href','src','data-full']:
            link=a.get(key,'')
            if not link or urlsplit(link).scheme or link.startswith('#'):continue
            path=unquote(urlsplit(link).path)
            target=(OUT/path.removeprefix('/odedipe-architecture/') if path.startswith('/odedipe-architecture/') else self.p.parent/path).resolve()
            if not target.exists():errors.append(f'{self.p.relative_to(OUT)}: missing {link}')
        for item in a.get('srcset','').split(','):
            if item.strip() and not (self.p.parent/item.strip().split()[0]).exists():errors.append(f'{self.p.name}: srcset {item}')
        if tag=='img' and a.get('class')!='lightbox-image':
            self.images+=1
            for key in ['alt','width','height','loading']:
                if not a.get(key):errors.append(f'{self.p.name}: image missing {key}')

pages=list(OUT.rglob('*.html'))
for p in pages:
    if p.name.startswith('qa-'):continue
    c=Check(p);c.feed(p.read_text())
    if c.h1!=1:errors.append(f'{p}: {c.h1} H1s')
    if p.parent.parent.name=='projects' and c.captions!=6:errors.append(f'{p}: {c.captions} captions')
projects=json.loads((ROOT/'content/projects.json').read_text())
assert len(projects)==15 and sum(len(p['images']) for p in projects)==90
for p in projects:
    assert len(p['images'])==6 and all(i['caption'] for i in p['images'])
    for i in p['images']:
        for f in i['avif']+i['webp']:
            if not (OUT/f['src']).exists():errors.append(f['src'])
print(f'Checked {len(pages)} published pages, 15 projects, 90 captioned images.')
if errors:print('\n'.join(errors));raise SystemExit(1)
print('PASS: internal files, responsive sources, image attributes, page headings, and project completeness.')
