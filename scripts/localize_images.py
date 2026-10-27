"""Fetch public customer photos once and generate small, locally hosted WebP assets."""
from concurrent.futures import ThreadPoolExecutor,as_completed
from pathlib import Path
from urllib.request import Request,urlopen
from PIL import Image,ImageOps
from io import BytesIO
import hashlib,json
root=Path(__file__).resolve().parents[1]
entries=json.loads((root/'content/image-manifest.json').read_text())
from lxml import html
node=html.parse(str(root/'index.html'))
urls={e['src'] for e in entries if e['src'].startswith('https://blogger.googleusercontent.com/')}
urls|={x for x in node.xpath('//section[@id="customer-gallery"]//img/@src') if x.startswith('https://blogger.googleusercontent.com/')}
out=root/'assets'/'customer';out.mkdir(parents=True,exist_ok=True)
def convert(url):
 name=hashlib.sha256(url.encode()).hexdigest()[:16]+'.webp'; dest=out/name
 if dest.exists():return url,'/assets/customer/'+name,dest.stat().st_size
 request=Request(url,headers={'User-Agent':'Mozilla/5.0'})
 with urlopen(request,timeout=30) as response: data=response.read(15_000_001)
 if len(data)>15_000_000:raise ValueError('Source image too large')
 with Image.open(BytesIO(data)) as im:
  im=ImageOps.exif_transpose(im).convert('RGB');im.thumbnail((1200,1200),Image.Resampling.LANCZOS)
  im.save(dest,'WEBP',quality=78,method=6)
 return url,'/assets/customer/'+name,dest.stat().st_size
results={}; failures=[]
with ThreadPoolExecutor(max_workers=5) as pool:
 for f in as_completed({pool.submit(convert,u):u for u in urls}):
  try:
   old,new,size=f.result();results[old]=new;print(new,size)
  except Exception as exc:failures.append((pool._threads and 'image' or 'image',str(exc)))
(root/'content'/'localized-images.json').write_text(json.dumps(results,indent=2))
print(f'Localized {len(results)}/{len(urls)} photos; failures={len(failures)}')
for _,err in failures:print(err)
if failures:raise SystemExit(1)
