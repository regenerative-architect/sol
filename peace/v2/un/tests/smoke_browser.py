from playwright.sync_api import sync_playwright
from pathlib import Path
import re,json
base=Path(__file__).resolve().parents[1]; js=(base/'assets/app.js').read_text();css=(base/'assets/styles.css').read_text();mods=['','sitrep','doctrine','casebook','register','evidence','compliance','framework','cyber','humanitarian','ceasefire','metrics','premortem','nodes','governance'];results=[];errors=[]
def boot(page,mod):
 file=base/'index.html' if not mod else base/'modules'/mod/'index.html';s=file.read_text();s=re.sub(r'<script defer src="[^"]+"></script>','',s);s=re.sub(r'<link[^>]+>','',s)
 page.set_content(s,wait_until='domcontentloaded');page.add_style_tag(content=css);page.add_script_tag(content=js);page.wait_for_selector('.banner h1',timeout=12000)
with sync_playwright() as p:
 br=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage']);ctx=br.new_context(viewport={'width':1350,'height':900},accept_downloads=True)
 for mod in mods:
  page=ctx.new_page();page.on('pageerror',lambda x:errors.append(str(x)))
  boot(page,mod);assert page.locator('.nav-item').count()==15,mod
  assert page.locator('.banner h1').is_visible(),mod
  assert len(page.locator('#main').inner_text())>250,mod
  results.append('Rendered '+(mod or 'home'));page.close()
 page=ctx.new_page();page.on('pageerror',lambda x:errors.append(str(x)));boot(page,'register');page.locator('#rec-title').fill('Public UN verified report reference');page.locator('#rec-date').fill('2026-09-17');page.locator('#rec-url').fill('https://ukraine.un.org/en/323454-protection-civilians-armed-conflict-%E2%80%94-august-2026');page.locator('#rec-finding').fill('OHCHR published documented civilian harm with known caveats.');page.get_by_role('button',name='Save local note').click();assert page.locator('.listitem').count()==1
 page.get_by_role('button',name='Edit',exact=True).click();page.locator('#rec-title').fill('Revised public UN verified report');page.get_by_role('button',name='Save revisions').click();assert 'Revised public UN' in page.locator('.listitem').inner_text()
 page.locator('#site-search').fill('notmatched_foo');assert page.locator('.listitem.hidden').count()==1;page.locator('#site-search').fill('Revised');assert page.locator('.listitem.hidden').count()==0
 with page.expect_download() as d:page.get_by_role('button',name='Download backup').click()
 payload=json.loads(Path(d.value.path()).read_text());assert payload['app']=='un_peace_assurance_research_os' and len(payload['records'])==1;results.append('Local record CRUD, search, export')
 page=ctx.new_page();page.on('pageerror',lambda x:errors.append(str(x)));boot(page,'nodes')
 sample={'schema':'pra.reciprocal_public_handoff','version':1,'handling':'PUBLIC_ONLY','lead':{'id':'old-node-test','title':'Prior edition public case','category':'civilian_protection','summary':'Public-source example without confidential detail','source_url':'https://www.defense.gov/News/Releases/Release/Article/3140007/civilian-harm-mitigation-and-response-action-plan-fact-sheet/'}}
 f=Path('/tmp/military_legacy_node_test.json');f.write_text(json.dumps(sample));page.locator('#import-file').set_input_files(str(f));page.wait_for_selector('#import-dialog[open]');assert '1 validated' in page.locator('#import-preview').inner_text();page.get_by_role('button',name='Apply reviewed import').click()
 with page.expect_download() as d:page.get_by_role('button',name='Download unsigned draft').click()
 obj=json.loads(Path(d.value.path()).read_text());assert obj['handling']=='PUBLIC_ONLY' and obj['submitted']==False and obj['sender_node']=='un_public_concept';results.append('Public-only handoff backward import and unsigned draft')
 page=ctx.new_page();boot(page,'framework');page.locator('[data-check=mandate]').check();assert '1/11' in page.locator('main').inner_text();page.locator('[data-action=theme]').click();assert page.locator('html').get_attribute('data-theme')=='dark';results.append('Review gate and theme')
 page=ctx.new_page();boot(page,'evidence');page.locator('#hash-file').set_input_files({'name':'test_public.txt','mimeType':'text/plain','buffer':b'public test content'});page.wait_for_timeout(250);output=page.locator('#hash-out').inner_text();assert 'Web Crypto unavailable' in output or 'SHA-256' in output,output;results.append('Hash availability/error handling')
 mobile=br.new_context(viewport={'width':390,'height':820},is_mobile=True,has_touch=True);pm=mobile.new_page();pm.on('pageerror',lambda x:errors.append(str(x)));boot(pm,'');pm.locator('[data-action=drawer]').click();assert pm.locator('#sidebar').evaluate('el=>el.classList.contains("open")');pm.keyboard.press('Escape');assert not pm.locator('#sidebar').evaluate('el=>el.classList.contains("open")');results.append('Mobile navigation open and Escape close')
 p1=ctx.new_page();boot(p1,'');p1.screenshot(path=str(base/'tests'/'browser_desktop_preview.png'),full_page=True)
 pm.screenshot(path=str(base/'tests'/'browser_mobile_preview.png'),full_page=True)
 assert not errors,errors;br.close()
print('PASS',len(results));print('\n'.join('- '+r for r in results))
