#!/bin/sh
# Draws the picture a link preview shows for the draft of the rebuilt home page, 1200 by 630,
# into site/public/draft/preview.png, with a headless Chrome.
#   sh scripts/preview_picture.sh
# PROPOSED 2026-11-20. The picture holds the site's name, one line saying what the record is,
# and the address. It holds no figure, so it cannot go out of date when the record changes.
# The colours are the dark skin's (site/src/styles/skin.css). Both sentences are drafts.
set -e
cd "$(dirname "$0")/.."
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUT="site/public/draft/preview.png"
TMP=$(mktemp -d)
mkdir -p "$(dirname "$OUT")"
cat > "$TMP/card.html" <<'HTML'
<!doctype html><meta charset="utf-8">
<style>
  html, body { margin: 0; width: 1200px; height: 630px; background: #141826; color: #f1ece0; overflow: hidden; }
  body { display: grid; grid-template-columns: 1fr 300px; gap: 60px; padding: 76px 80px; box-sizing: border-box; align-items: center; }
  .name { font: 600 25px/1.3 ui-sans-serif, system-ui, -apple-system, sans-serif; letter-spacing: 0.16em; text-transform: uppercase; color: #e9b862; margin: 0 0 30px; }
  .line { font: 400 62px/1.14 Georgia, 'Times New Roman', serif; margin: 0 0 34px; letter-spacing: -0.01em; }
  .sub { font: 400 29px/1.35 ui-sans-serif, system-ui, -apple-system, sans-serif; color: #d3cec2; margin: 0 0 40px; }
  .addr { font: 400 23px/1 ui-monospace, 'SF Mono', Menlo, monospace; color: #979fb3; margin: 0; }
  .frame { width: 300px; height: 400px; border: 5px solid #f1ece0; border-bottom-width: 14px; box-sizing: border-box; display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr 1fr; gap: 5px; background: #f1ece0; }
  .frame i { background: #1c2234; } .frame i.lit { background: #e9b862; }
</style>
<div>
  <p class="name">Beyond the Window</p>
  <p class="line">A dated record of how the world is treating AI models</p>
  <p class="sub">Who has done what, and when, each with a source to open.</p>
  <p class="addr">beyondthewindow.org</p>
</div>
<div class="frame"><i class="lit"></i><i></i><i></i><i class="lit"></i><i></i><i></i></div>
HTML
"$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 \
  --user-data-dir="$TMP/profile" --window-size=1200,630 --virtual-time-budget=2000 \
  --screenshot="$TMP/card.png" "file://$TMP/card.html" >/dev/null 2>&1
python3 - "$TMP/card.png" "$OUT" <<'PY'
import sys
from PIL import Image
im = Image.open(sys.argv[1]).convert('RGB').crop((0, 0, 1200, 630))
im.save(sys.argv[2], optimize=True)
print(im.size)
PY
rm -rf "$TMP"
echo "  $OUT"
