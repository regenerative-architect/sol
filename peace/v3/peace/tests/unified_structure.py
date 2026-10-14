"""Offline static checks of packaged corpus. Network tests must be done separately."""
from pathlib import Path
import json,re,hashlib
ROOT=Path(__file__).resolve().parents[1]
names=['usmc','usss','cia','fbi','un']
expected={'usmc':(15,16,4,8,10),'usss':(7,7,0,6,7),'cia':(15,18,5,8,10),'fbi':(11,15,4,6,9),'un':(15,20,6,9,11)}
archive=json.loads((ROOT/'data/integrated_public_records.json').read_text())['records']
assert set(archive)==set(names)
for node in names:
    data=archive[node]
    counts=(len(data.get('routes',[])),len(data.get('sources',[])),len(data.get('cases',[])),len(data.get('actions',data.get('interventions',[]))),len(data.get('checks',[])))
    assert counts==expected[node],(node,counts)
    assert (ROOT/node/'index.html').is_file()
    assert (ROOT/node/'assets/app.js').is_file()
    assert (ROOT/node/'assets/styles.css').is_file()
    for route in data['routes']:
        path=route.get('path','')
        assert (ROOT/node/path/'index.html').is_file(),(node,path)
    for source in data['sources']:
        assert source.get('url','').startswith('https://'),(node,source)
    print('PASS',node,counts)
assert '<script type="module">' in (ROOT/'index.html').read_text()
js=re.search(r'<script type="module">(.*?)</script>',(ROOT/'index.html').read_text(),re.S).group(1)
assert js.count('const ARCHIVE=')==1
assert 'function renderAtlas()' in js and 'function renderCampaign()' in js
assert "HANDOFF='pra.reciprocal_public_handoff'" in js
sw=(ROOT/'service_worker.js').read_text();assert "sol-peace-master-shell-v4" in sw
for rel in re.findall(r"'\./((?:usmc|usss|cia|fbi|un)/[^']+)'",sw): assert (ROOT/rel).is_file(),rel
print('PASS embedded source archive, 63 original routes, SW static assets and legacy handoff format')
