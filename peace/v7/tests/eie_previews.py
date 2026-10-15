from pathlib import Path
from playwright.sync_api import sync_playwright
base=Path(__file__).parents[1];html=(base/'index.html').read_text()
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
 for name,width,height,mobile in [('desktop',1380,930,False),('mobile',393,852,True)]:
  ctx=b.new_context(viewport={'width':width,'height':height},device_scale_factor=1,is_mobile=mobile,has_touch=mobile)
  pg=ctx.new_page();pg.set_content(html,wait_until='domcontentloaded');pg.wait_for_function('!!window.SOL_PRA_EIE_TEST')
  pg.evaluate('window.SOL_PRA_FLOW_TEST.flowSetStep(0)')
  pg.locator('[data-act="eieToggle"]').click();pg.locator('[data-act="eiePreset"]').first.click()
  pg.wait_for_timeout(680)
  pg.evaluate('window.scrollTo(0,0)')
  pg.wait_for_timeout(100)
  pg.screenshot(path=str(base/f'{name}_eie_preview.png'),full_page=True)
  ctx.close()
 b.close()
print('Created two EIE previews')
