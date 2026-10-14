from pathlib import Path
import json,subprocess,re,hashlib,zipfile
BASE=Path(__file__).resolve().parents[1]
req=['index.html','service_worker.js','site.webmanifest','icon.svg','README.md','DEPLOYMENT.md','ATTRIBUTIONS_AND_LICENSES.md','LICENSE','data/public_handoff_example.json','tests/smoke_browser.py']
assert all((BASE/x).is_file() for x in req)
html=(BASE/'index.html').read_text()
assert all(x in html for x in ['/sol/peace/','const NODES=','const CLASSES=','const QUESTS=','const SKILLS=','const ROUTES=','makeAction(\'public-proposal-v1\')','PROJECT_GATES','indexedDB','pra.reciprocal_public_handoff'])
assert len(html.encode()) < 2_000_000
assert all('id="'+x+'"' in html for x in ['nav','view','sidebar','siteSearch','menuBtn'])
subprocess.run(['node','--check',str(BASE/'tests/app_syntax.mjs')],check=True)
json.loads((BASE/'site.webmanifest').read_text())
schema=json.loads((BASE/'data/public_handoff_example.json').read_text())
assert schema['schema']=='pra.reciprocal_public_handoff' and schema['version']==1 and schema['handling']=='PUBLIC_ONLY' and not schema['submitted']
print('Structure and JS syntax OK; bundle HTML bytes:', len(html.encode()))
