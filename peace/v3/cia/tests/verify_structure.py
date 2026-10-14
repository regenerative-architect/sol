from pathlib import Path
import json
p=Path(__file__).resolve().parents[1]
routes=['home','sitrep','doctrine','casebook','register','evidence','compliance','framework','cyber','humanitarian','ceasefire','metrics','premortem','nodes','governance']
for r in routes:
 f=(p/'index.html') if r=='home' else p/'modules'/r/'index.html'
 assert f.exists(),f
 assert 'data-route="'+r+'"' in f.read_text()
for x in ['sources.json','actions.json','scope_matrix.json','handoff_schema_v1.json']:
 json.loads((p/'data'/x).read_text())
s=(p/'assets/app.js').read_text()
assert 'cia_peace_analysis_research_os' in s
assert "sender_node:'cia_public_concept'" in s
assert 'us_military_peace_research_os' in s
assert 'pra.reciprocal_public_handoff' in s
print('STATIC PASS: 15 routes, 4 datasets, backward handoff import and CIA sender')
