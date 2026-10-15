from pathlib import Path
from playwright.sync_api import sync_playwright
src=Path(__file__).resolve().parents[1]/'index.html'; html=src.read_text()
# Replace ONLY for this isolated test: the actual release retains the real dynamic import.
assert 'const {joinRoom}=await import(moduleUrl);' in html
html=html.replace('const {joinRoom}=await import(moduleUrl);','const {joinRoom}=window.fakeTrystero;',1)
assert "if(peerAuto&&navigator.onLine&&['http:','https:'].includes(location.protocol))queueMicrotask" in html
html=html.replace("if(peerAuto&&navigator.onLine&&['http:','https:'].includes(location.protocol))queueMicrotask", "if(peerAuto&&navigator.onLine)queueMicrotask",1)
mock='''<script>window.sent=[];window.mockRooms=[];window.fakeTrystero={joinRoom:(cfg,code)=>{const r={cfg,code,leave:async()=>{r.left=true},makeAction:(name)=>({send:async(data)=>{window.sent.push({name,data})},onMessage:null})};window.mockRooms.push(r);return r}};</script>'''
html=html.replace('<script type="module">',mock+'<script type="module">',1)
checks=[]
def ok(n, cond):
 if not cond: raise AssertionError(n)
 checks.append(n);print('PASS',n,flush=True)
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
 page=browser.new_page(viewport={'width':1300,'height':860});errs=[];page.on('pageerror',lambda e:errs.append(str(e)))
 page.set_content(html,wait_until='domcontentloaded');page.wait_for_function('window.SOL_PRA_EIE_TEST?.getPeerStatus() === "room ready"')
 ok('Automatically joins Trystero-compatible public lobby',page.evaluate('mockRooms.length===1&&mockRooms[0].code==="sol-peace-public-commons-2026"'))
 ok('Uses same legacy Trystero app namespace',page.evaluate('mockRooms[0].cfg.appId==="pra.sol.peace.commons.v1"'))
 ok('Public lobby correctly has no false shared secret',page.evaluate('mockRooms[0].cfg.password===undefined'))
 ok('Automatic connect does not transmit aliases, private notes or drafts',page.evaluate('sent.length===0'))
 ok('Explicit disconnect immediately turns off auto-connect',page.locator('[data-act="leaveRoom"]').is_visible())
 page.locator('[data-act="leaveRoom"]').first.click()
 page.wait_for_function('window.SOL_PRA_EIE_TEST.getPeerStatus()==="disconnected"')
 ok('Leave calls room cleanup',page.evaluate('mockRooms[0].left===true'))
 ok('Leave prevents next online visit auto-rejoin',page.evaluate('window.SOL_PRA_EIE_TEST.getPeerAuto()===false'))
 ok('No transmission during disconnect',page.evaluate('sent.length===0'))
 page.locator('[data-act="joinPublic"]').first.click()
 page.wait_for_function('window.SOL_PRA_EIE_TEST.getPeerStatus()==="room ready"')
 ok('Manual reconnect joins room',page.evaluate('mockRooms.length===2'))
 ok('Manual reconnect also sends no profile',page.evaluate('sent.length===0'))
 page.evaluate('''() => {window.SOL_PRA_TEST.getState().projects.unshift({id:'mock-private',title:'Public water resilience research',source:'https://www.un.org/',summary:'Review independently sourced civilian water access records and stop if the evidence is insufficient for any claimed outcome.',nodes:['un','usmc'],createdAt:new Date().toISOString(),gates:{source:{note:'PRIVATE REVIEW GATE',source:'https://www.un.org/',date:'2026-10-14'}}});location.hash='#/workshop'}''')
 page.wait_for_function('location.hash==="#/workshop" && document.querySelector("[data-act=shareProject]")')
 page.on('dialog',lambda d:d.accept())
 page.locator('[data-act="shareProject"]').first.click()
 page.wait_for_function('sent.length===1')
 ok('Manual public share sends a proposal only after confirmation',page.evaluate('sent.length===1&&sent[0].name==="public-proposal-v1"'))
 ok('Private review-gate notes are stripped from peer payload',page.evaluate('Object.keys(sent[0].data.proposal.gates).length===0 && !JSON.stringify(sent).includes("PRIVATE REVIEW GATE")'))
 ok('No JavaScript errors in mock peer flow',not errs)
 browser.close()
print('TOTAL',len(checks),'checks')
