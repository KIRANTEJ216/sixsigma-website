"""Rebuild crawlable pages from the preserved Blogger export. No network required."""
from pathlib import Path
from urllib.parse import urlparse
from html import escape as E
from lxml import html
import json, re, os
ROOT=Path(__file__).resolve().parents[1]
BASE=os.environ.get('SITE_URL','https://sixsigma-website.vercel.app').rstrip('/')
OLD='https://www.big9signages.com'
posts=json.loads((ROOT/'content/blogger-posts.json').read_text())['feed']['entry']
paths={urlparse(next(l['href'] for l in p['link'] if l['rel']=='alternate')).path for p in posts}
urls=['/','/blog/','/services/','/contact/']
business={'@context':'https://schema.org','@type':'LocalBusiness','@id':BASE+'/#business','name':'Big 9 Signages','url':BASE,'telephone':'+919381556456','areaServed':['Hyderabad','Telangana']}
def write(path,text):
 p=ROOT/path.lstrip('/');p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
def page(path,title,desc,body,schema=None,canonical=None):
 url=BASE+path; canon=canonical or url
 data=[business,{'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'Home','item':BASE+'/'},{'@type':'ListItem','position':2,'name':title,'item':url}]}]
 if schema:data.append(schema)
 out=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{E(title)} | Big 9 Signages</title><meta name="description" content="{E(desc,quote=True)}"><link rel="canonical" href="{canon}"><meta property="og:type" content="website"><meta property="og:title" content="{E(title,quote=True)}"><meta property="og:description" content="{E(desc,quote=True)}"><meta property="og:url" content="{canon}"><meta property="og:image" content="{BASE}/assets/photo/hero-before.webp"><link rel="stylesheet" href="/search-pages.css"><script type="application/ld+json">{json.dumps(data).replace('</','<\\/')}</script></head><body><a class="skip" href="#main">Skip to content</a><header><a class="brand" href="/">BIG 9 <span>SIGNAGES</span></a><nav aria-label="Main"><a href="/services/">Signage</a><a href="/blog/">Guides</a><a href="/contact/">Contact</a><a href="/#quote">Get a quote</a></nav></header><main id="main"><p class="eyebrow">Designed for visibility · Hyderabad</p><h1>{E(title)}</h1><p class="lead">{E(desc)}</p>{body}</main><footer>Big 9 Signages · <a href="tel:+919381556456">+91 9381 556 456</a><p><a href="/blog/">Signage guides</a> · <a href="/services/">Explore services</a> · <a href="/contact/">Contact and enquiries</a></p></footer></body></html>'''
 write(path+'index.html' if path.endswith('/') else path,out)
 if path not in urls:urls.append(path)
items=[]; images=[]
for p in posts:
 old=next(l['href'] for l in p['link'] if l['rel']=='alternate');path=urlparse(old).path;title=p['title']['$t']
 node=html.fragment_fromstring(p['content']['$t'],create_parent='div')
 for bad in node.xpath('.//script|.//style|.//iframe|.//object|.//form'):bad.drop_tree()
 for el in node.iter():
  for a in list(el.attrib):
   if a.lower().startswith('on') or a in ('style','srcset'):del el.attrib[a]
  for a in ('src','href'):
   v=el.get(a) or ''
   if v.strip().lower().startswith(('javascript:','data:')):el.attrib.pop(a,None)
   if a=='href' and urlparse(v).netloc=='www.big9signages.com' and urlparse(v).path in paths:el.set(a,urlparse(v).path)
 for im in node.xpath('.//img'):
  im.set('loading','lazy');im.set('decoding','async');im.set('alt',im.get('alt') or title.split('|')[0].strip())
  if im.get('src'):images.append({'src':im.get('src'),'article':old,'alt':im.get('alt')})
 text=' '.join(node.text_content().split());desc=text[:157].rsplit(' ',1)[0]+'…'
 author=p.get('author',[{}])[0].get('name',{}).get('$t','Big 9 Signages')
 schema={'@context':'https://schema.org','@type':'BlogPosting','headline':title,'datePublished':p['published']['$t'],'dateModified':p['updated']['$t'],'author':{'@type':'Person','name':author},'publisher':{'@id':BASE+'/#business'},'mainEntityOfPage':old}
 body=f'<p class="meta">By {E(author)} · Published {p["published"]["$t"][:10]} · Updated {p["updated"]["$t"][:10]}</p><article>'+html.tostring(node,encoding='unicode')+'</article><aside><h2>Planning a similar sign?</h2><p>Choose your signage and share your requirements for a site assessment.</p><a class="button" href="/#quote">Request a quotation</a></aside>'
 # Old blog remains authoritative until an intentional domain cutover.
 page(path,title,desc,body,schema,old)
 items.append((title,path,desc))
write('content/image-manifest.json',json.dumps(images,indent=2))
page('/blog/','Signage guides and ideas','Explore the existing Big 9 Signages articles on materials, lighting and signage for businesses.', '<div class="grid">'+''.join(f'<article class="card"><h2><a href="{path}">{E(title)}</a></h2><p>{E(desc)}</p></article>' for title,path,desc in items)+'</div>')
services=[('led-sign-boards','LED sign boards','Illuminated signboards for shopfronts, salons and commercial entrances.','LED modules, acrylic faces and an aluminium or ACP backing','Lighting layout, board size, installation height and electrical access','led'),('acrylic-signs','Acrylic signage','Acrylic lettering and panels for reception areas, shops and interior branding.','Cut acrylic, optional printed graphics and suitable mounting hardware','Acrylic thickness, letter size, finish and lighting','acrylic'),('pylon-signs','Pylon signage','Freestanding signage to identify entrances from an approach road.','Engineered supporting structure, sign faces and optional illumination','Structural design, foundation, height, access and permissions','pylon'),('wayfinding-signs','Wayfinding signage','Directional signs and directories that help people navigate a building or campus.','Printed or engraved panels, pictograms and wall or post mounts','Number of destinations, reading distance, languages and installation locations','wayfinding'),('safety-signs','Safety signage','Clear signs for hazards, emergency routes and workplace instructions.','Suitable printed panels, reflective or photoluminescent materials where specified','Site requirements, applicable standards, visibility and quantities','safety'),('vehicle-branding','Vehicle branding','Graphics and wraps that carry business identity on vehicles.','Vehicle-grade printed vinyl and a suitable protective laminate','Vehicle dimensions, surface condition, coverage and artwork','vehicle')]
servicecards=[]
for slug,name,intro,materials,factors,key in services:
 path='/services/'+slug+'/'
 related=[x for x in items if key in x[0].lower()][:3]
 body=f'<h2>Where does it work best?</h2><p>{intro} The final specification depends on your location, surface and viewing distance.</p><h2>Materials and options</h2><p>{materials}. Confirm the finish and indoor or outdoor exposure during the site assessment.</p><h2>What affects the price?</h2><p>{factors}. Share photographs and approximate dimensions for an initial discussion; a firm price requires an agreed specification.</p><h2>Installation and maintenance</h2><p>Ask the team to confirm access requirements, electrical work where needed, cleaning instructions and the warranty for your selected materials in the written quotation.</p><h2>What should I send for a quotation?</h2><p>Your location, a frontage or installation photo, approximate width and height, quantity, preferred lighting and target date.</p><a class="button" href="/#quote">Request {E(name.lower())}</a><h2>Related guides</h2><ul>'+''.join(f'<li><a href="{x[1]}">{E(x[0])}</a></li>' for x in related)+'</ul>'
 photo=next((im for im in images if key in im['article'].lower()),None)
 if photo:body='<img class="service-image" loading="lazy" decoding="async" src="'+E(photo['src'],quote=True)+'" alt="'+E(photo['alt'],quote=True)+'">'+body
 page(path,name+' in Hyderabad',intro,body,{'@context':'https://schema.org','@type':'Service','name':name,'serviceType':name,'provider':{'@id':BASE+'/#business'},'areaServed':'Hyderabad','url':BASE+path})
 servicecards.append(f'<article class="card"><h2><a href="{path}">{name}</a></h2><p>{intro}</p></article>')
page('/services/','Signage solutions in Hyderabad','Compare signage options and choose the right starting point for your enquiry.','<div class="grid">'+''.join(servicecards)+'</div>')
page('/contact/','Contact Big 9 Signages','Discuss your signage requirements in Hyderabad and Telangana.','<h2>Speak with the team</h2><p><a href="tel:+919381556456">Call +91 9381 556 456</a></p><p><a class="button" href="https://wa.me/919381556456">Chat on WhatsApp</a></p><p>Share the signage type, city, approximate dimensions, quantity and target date. Confirm site-visit availability directly with the team.</p><h2>Your enquiry details</h2><p>The website prepares your enquiry for WhatsApp. You review and send it there. Do not include payment details or sensitive documents. For questions about your enquiry data, contact the team using the number above.</p>')
write('robots.txt','User-agent: *\nAllow: /\n\nUser-agent: OAI-SearchBot\nAllow: /\n\nUser-agent: GPTBot\nDisallow: /\n\nSitemap: '+BASE+'/sitemap.xml\n')
# Imported posts retain original canonical until domain cutover; omit duplicates from sitemap.
indexurls=[u for u in urls if u not in paths or BASE==OLD]
write('sitemap.xml','<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+BASE+u+'</loc></url>' for u in indexurls)+'</urlset>')
write('content/url-map.json',json.dumps([{'original':OLD+p,'preserved_path':p,'preview':BASE+p} for p in sorted(paths)],indent=2))
print(f'Built {len(posts)} preserved articles and {len(services)} service pages; {len(indexurls)} canonical sitemap URLs')
