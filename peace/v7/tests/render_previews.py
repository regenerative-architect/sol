from pathlib import Path
from playwright.sync_api import sync_playwright
BASE=Path(__file__).parents[1]
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
 page=browser.new_page(viewport={'width':1375,'height':930},device_scale_factor=1)
 page.set_content((BASE/'index.html').read_text(),wait_until='domcontentloaded')
 page.wait_for_function('!!window.SOL_PRA_TEST')
 page.evaluate('document.documentElement.dataset.theme="dark";location.hash="#/overview"')
 page.wait_for_timeout(300)
 page.screenshot(path=str(BASE/'desktop_preview.png'),full_page=True)
 mobile=browser.new_page(viewport={'width':393,'height':852},device_scale_factor=1,is_mobile=True,has_touch=True)
 mobile.set_content((BASE/'index.html').read_text(),wait_until='domcontentloaded')
 mobile.wait_for_function('!!window.SOL_PRA_TEST')
 mobile.evaluate('document.documentElement.dataset.theme="dark";location.hash="#/skills"')
 mobile.wait_for_timeout(300)
 mobile.screenshot(path=str(BASE/'mobile_preview.png'),full_page=True)
 browser.close()
print('Created preview PNGs')
