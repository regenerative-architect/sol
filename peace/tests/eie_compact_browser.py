# Compatibility alias for the corrected v2.6 icon-only test.
from pathlib import Path
exec((Path(__file__).parent/'eie_real_icon_browser.py').read_text(), {'__name__':'__main__','__file__':str(Path(__file__).parent/'eie_real_icon_browser.py')})
