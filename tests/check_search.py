from pathlib import Path
from lxml import html,etree
import json,subprocess,tempfile
r=Path(__file__).resolve().parents[1]
files=[r/'index.html',*r.glob('services/**/index.html'),r/'blog/index.html',r/'contact/index.html',r/'about/index.html',r/'gallery/index.html',*r.glob('2024/**/*.html'),*r.glob('2025/**/*.html')]
for p in files:
 d=html.parse(str(p));assert d.xpath('//h1'),p
 assert d.xpath('//link[@rel="canonical"]/@href')[0].startswith('https://'),p
 for s in d.xpath('//script[@type="application/ld+json"]'):json.loads(s.text)
 for s in d.xpath('//script[not(@src) and not(@type)]'):
  with tempfile.NamedTemporaryFile(suffix='.js',mode='w') as f:
   f.write(s.text or '');f.flush();subprocess.run(['node','--check',f.name],check=True,capture_output=True)
 for href in d.xpath('//a/@href'):
  if href.startswith('/') and not href.startswith('//'):
   path=href.split('#')[0].split('?')[0];target=r/path.lstrip('/')
   assert target.exists(),(p,href)
for item in json.loads((r/'content/url-map.json').read_text()):assert (r/item['preserved_path'].lstrip('/')).exists()
etree.parse(str(r/'sitemap.xml'));json.loads((r/'vercel.json').read_text())
assert 'OAI-SearchBot\nAllow: /' in (r/'robots.txt').read_text()
assert 'Dimensions:' in (r/'index.html').read_text()
print(f'PASS: {len(files)} HTML pages, JSON-LD, inline JS syntax, internal page links, blog path preservation, sitemap and Vercel config')

assert all(x.get('src').startswith('/assets/customer/') for x in html.parse(str(r/'index.html')).xpath('//section[@id="customer-gallery"]//img'))
assert all(x.get('src').startswith('/assets/customer/') for x in html.parse(str(r/'2025/12/xyz.html')).xpath('//article//img'))

from urllib.parse import urlparse
for loc in etree.parse(str(r/'sitemap.xml')).xpath('//*[local-name()="loc"]/text()'):
 assert urlparse(loc).netloc=='www.big9signages.com',loc
 path=r/urlparse(loc).path.lstrip('/')
 assert path.exists(),loc
for p in files:
 d=html.parse(str(p))
 assert d.xpath('//link[@rel="canonical"]/@href')[0].startswith('https://www.big9signages.com/'),p
 for src in d.xpath('//img/@src'):
  if src.startswith('/assets/'): assert (r/src.lstrip('/')).exists(),(p,src)
