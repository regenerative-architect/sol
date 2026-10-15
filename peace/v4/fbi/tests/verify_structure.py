"""Offline, standard-library smoke test. Run: python tests/verify_structure.py
No network access, execution of app JS, or official access is required.
"""
from pathlib import Path
from urllib.parse import urlparse
import json, re
from html.parser import HTMLParser
ROOT=Path(__file__).resolve().parents[1]
MODULES='sitrep casebook register evidence compliance framework cyber humanitarian nodes governance'.split()
HTML=[ROOT/'index.html']+[ROOT/'modules'/x/'index.html' for x in MODULES]
class Scanner(HTMLParser):
 def __init__(self):super().__init__();self.refs=[];self.data={}
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if tag in ('link','script','a'):
   val=d.get('href') or d.get('src');
   if val and not val.startswith(('https://','http://','#','mailto:','data:')):self.refs.append(val)
  if tag=='body':self.data=d

def check(cond,msg):
 if not cond:raise AssertionError(msg)

for path in HTML:
 check(path.is_file(),f'Missing HTML: {path}')
 raw=path.read_text(encoding='utf-8');s=Scanner();s.feed(raw)
 check('<html lang="en">' in raw,'Missing English language tag '+str(path))
 check('id="main"' in raw,'Missing no-JS main '+str(path))
 check('Skip to main content' in raw,'Missing skip link '+str(path))
 for ref in s.refs:
  parsed=urlparse(ref); rel=parsed.path
  check((path.parent/rel).is_file(),f'Broken local path {path}: {ref}')
 check(s.data.get('data-route') in ['home']+MODULES,'Unknown route '+str(path))

source=json.loads((ROOT/'data/sources.json').read_text())
check(len(source['sources'])>=12,'Expected primary-source registry')
ids=set()
for s in source['sources']:
 check(s['id'] not in ids,'Duplicate source id'); ids.add(s['id'])
 check(s['url'].startswith('https://'),'Non-HTTPS source')
hand=json.loads((ROOT/'data/handoff_schema_v1.json').read_text())
check(hand['schema']=='pra.reciprocal_public_handoff' and hand['version']==1,'Handoff schema mismatch')
check(hand['handling']=='PUBLIC_ONLY' and hand['submitted'] is False,'Handoff must be unsigned and unsubmitted')
scopes=json.loads((ROOT/'data/scope_matrix.json').read_text())
check(all(n['active'] is False for n in scopes['nodes']),'No live agency links permitted')
js=(ROOT/'assets/app.js').read_text()
check('navigator.serviceWorker.register' in js,'Expected optional hosted SW registration')
sw=(ROOT/'service_worker.js').read_text()
m=re.search(r'const FILES=(\[[^;]+\]);',sw)
check(bool(m),'Could not identify SW precache list')
for ref in json.loads(m.group(1)):
 check((ROOT/ref).is_file(),'Unresolved SW cached file: '+ref)
check((ROOT/'site.webmanifest').is_file(),'Missing manifest')
print(f'PASS {len(HTML)} HTML pages, {len(source["sources"])} sources, {len(json.loads(m.group(1)))} cached files, portable schema and scoped offline assets')
