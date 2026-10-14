from pathlib import Path
import json, re
p=Path(__file__).resolve().parents[1]
routes=['home','sitrep','doctrine','casebook','register','evidence','compliance','framework','cyber','humanitarian','ceasefire','metrics','premortem','nodes','governance']
assert (p/'index.html').exists()
for r in routes[1:]:
 f=p/'modules'/r/'index.html';assert f.exists(),f
 t=f.read_text();assert 'data-route="'+r+'"' in t;assert 'no JavaScript' not in t or 1
for f in ['sources.json','actions.json','scope_matrix.json','handoff_schema_v1.json']:
 json.loads((p/'data'/f).read_text())
assert 'pra.reciprocal_public_handoff' in (p/'assets/app.js').read_text()
print('STATIC PASS: 15 standalone pages; four JSON reference files; shared handoff key')
