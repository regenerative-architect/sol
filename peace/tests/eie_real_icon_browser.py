"""Real icon vs banner regression (isolated Chromium, no real WebRTC)."""
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
HTML=(ROOT/'index.html').read_text()
checks=[]
def ck(label,ok):
    if not ok:raise AssertionError(label)
    checks.append(label);print('PASS',label,flush=True)
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
 for viewport in [{'width':1440,'height':900},{'width':390,'height':780},{'width':320,'height':700}]:
  size=viewport['width']; ctx=browser.new_context(viewport=viewport, reduced_motion='reduce' if size==320 else 'no-preference')
  page=ctx.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  page.set_content(HTML,wait_until='domcontentloaded')
  page.wait_for_function('window.SOL_PRA_EIE_TEST && document.querySelector("#eieFloatButton") && document.querySelector("#journeyHud .peer-indicator")')
  btn=page.locator('#eieFloatButton');dock=page.locator('#eieFloatingDock');bbox=btn.bounding_box()
  ck(f'{size} start icon exactly 50px',abs(bbox['width']-50)<.5 and abs(bbox['height']-50)<.5)
  ck(f'{size} only icon visible',btn.inner_text()=='🌐' and page.locator('.eie-title').count()==0)
  ck(f'{size} is outside banner row',page.locator('#journeyHud .eie-hud-toggle').count()==0 and btn.evaluate('(e)=>e.parentElement.id')=='eieFloatingDock')
  ck(f'{size} icon viewport anchored',bbox['x']>size-90 and bbox['y']>viewport['height']-100)
  ck(f'{size} EIE starts closed',page.locator('#earthEngine').count()==0 and btn.get_attribute('aria-expanded')=='false')
  page.wait_for_timeout(2000)
  ck(f'{size} remains 50px after delay',btn.bounding_box()['width']==50 and page.locator('.eie-title').count()==0)
  btn.click()
  ck(f'{size} panel visible',page.locator('#earthEngine').is_visible() and btn.get_attribute('aria-expanded')=='true')
  ck(f'{size} launcher stays icon',btn.bounding_box()['width']==50 and btn.inner_text()=='×')
  pb=page.locator('#earthEngine').bounding_box()
  ck(f'{size} panel in viewport',pb['x']>=0 and pb['x']+pb['width']<=size+1 and pb['y']>=-1 and pb['y']+pb['height']<=viewport['height']+1)
  ck(f'{size} research input receives focus',page.evaluate('document.activeElement.id')=='eieQuestion')
  page.locator('#eieQuestion').fill('civilian protection evidence')
  page.locator('#eieForm button[type=submit]').click()
  ck(f'{size} can analyze and show result',page.locator('#earthEngine').is_visible() and page.locator('#eieQuestion').input_value()=='civilian protection evidence')
  page.keyboard.press('Escape')
  ck(f'{size} escape closes and returns focus',page.locator('#earthEngine').count()==0 and page.evaluate('document.activeElement.id')=='eieFloatButton')
  page.evaluate('window.SOL_PRA_TEST.render()')
  ck(f'{size} survives rerender',btn.bounding_box()['width']==50 and page.locator('#journeyHud .eie-hud-toggle').count()==0)
  ck(f'{size} horizontal fit',page.evaluate('document.documentElement.scrollWidth<=innerWidth'))
  ck(f'{size} no JS exceptions',not errors)
  if size in (1440,390):page.screenshot(path=str(ROOT/('eie_icon_desktop.png' if size==1440 else 'eie_icon_mobile.png')),full_page=False)
  ctx.close()
 browser.close()
print('TOTAL',len(checks))
