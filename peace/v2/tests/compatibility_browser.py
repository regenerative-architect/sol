from playwright.sync_api import sync_playwright
from pathlib import Path
BASE=Path(__file__).resolve().parents[1];tests=[]
apps=['pra_financial_integrity_os','fbi_integrity_research_os','us_military_peace_research_os','cia_peace_analysis_research_os','un_peace_assurance_research_os']
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 pg=b.new_page();pg.set_content((BASE/'index.html').read_text());pg.wait_for_function('!!window.SOL_PRA_TEST')
 for app in apps:
  fixture={'app':app,'schemaVersion':1,'records':[{'title':f'Public note from {app}','sourceUrl':'https://www.un.org/en/','finding':'Dated publicly sourced test note'}]}
  if app=='pra_financial_integrity_os':fixture['leads']=fixture.pop('records')
  result=pg.evaluate('(x)=>window.SOL_PRA_TEST.legacyToInbox(x)',fixture)
  assert len(result)==1 and result[0]['source']=='https://www.un.org/en/' and not result[0]['reviewed'],app
  tests.append(app+' accepts public backup')
 bad={'schema':'pra.reciprocal_public_handoff','version':1,'handling':'PUBLIC_ONLY','lead':{'title':'Cannot load','source_url':'javascript:alert(1)'}}
 try:pg.evaluate('(x)=>window.SOL_PRA_TEST.legacyToInbox(x)',bad);raise AssertionError('Bad URL was accepted')
 except Exception as e:
  if isinstance(e,AssertionError):raise
  tests.append('Unsafe URL rejected')
 assert pg.evaluate('window.SOL_PRA_TEST.validUrl("https://example.com/")')
 assert not pg.evaluate('window.SOL_PRA_TEST.validUrl("http://example.com/")')
 tests.append('HTTPS-only source policy')
 # malformed XP claims invalid; prereq and skill budget are checked.
 badstate={'schema':'pra.sol_peace_master','version':1,'profile':{'classId':'mediator','alias':'Test'},'skills':['v1'],'completed':{},'projects':[],'inbox':[]}
 try:pg.evaluate('(x)=>window.SOL_PRA_TEST.validateState(x)',badstate);raise AssertionError('Unearned skills were accepted')
 except Exception as e:
  if isinstance(e,AssertionError):raise
  tests.append('Unearned skill points rejected on import')
 # XSS neutralization check on local editable content
 pg.evaluate('location.hash="#/workshop"');pg.wait_for_timeout(90)
 pg.locator('#projTitle').fill('<img src=x onerror=alert(1)>')
 pg.locator('#projSource').fill('https://www.un.org/en/')
 pg.locator('#projSummary').fill('A cited test of safe HTML escaping in this non-operational public research workspace.')
 pg.locator('#projNodes').select_option(['fbi','un'])
 pg.locator('#projectForm button[type="submit"]').click()
 assert pg.locator('#view img[src="x"]').count()==0
 assert '&lt;img' in pg.locator('#view').inner_html()
 tests.append('User-entered HTML escaped')
 b.close()
print('PASS',len(tests));print('\n'.join('- '+t for t in tests))
