from pathlib import Path
import json,hashlib,zipfile
root=Path(__file__).resolve().parents[1]; manifest=json.loads((root/'file_manifest_sha256.json').read_text())
for rel,obj in manifest['files'].items():
 f=root/rel
 assert f.is_file(),rel
 assert hashlib.sha256(f.read_bytes()).hexdigest()==obj['sha256'],rel
 assert f.stat().st_size==obj['bytes'],rel
print('PASS',len(manifest['files']),'manifest entries')
