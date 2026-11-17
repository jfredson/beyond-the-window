#!/bin/sh
# Photographs the mock-up pages into ../pictures with a headless Chrome.
#   sh docs/design/mockups/capture.sh
# Needs Google Chrome and Python with the Pillow library. PROPOSED 2026-11-17.
set -e
cd "$(dirname "$0")"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUT=../pictures
TMP=$(mktemp -d)
shot() { # name page theme width height
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
    --window-size="$4,$5" --screenshot="$TMP/$1.png" "file://$PWD/$2?theme=$3" >/dev/null 2>&1
  python3 - "$TMP/$1.png" "$OUT/$1.jpg" 1600 <<'PY'
import sys
from PIL import Image
im = Image.open(sys.argv[1]).convert('RGB')
w = int(sys.argv[3])
if im.width > w:
    im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
im.save(sys.argv[2], quality=88)
PY
  echo "  $1.jpg"
}
phone() { # name page theme
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
    --window-size=600,1500 --screenshot="$TMP/$1.png" "file://$PWD/phone.html?page=$2&theme=$3" >/dev/null 2>&1
  python3 - "$TMP/$1.png" "$OUT/$1.jpg" <<'PY'
import sys
from PIL import Image
im = Image.open(sys.argv[1]).convert('RGB').crop((0, 0, 780, 3000))
im.save(sys.argv[2], quality=88)
PY
  echo "  $1.jpg"
}
shot 1-glass-first-screen-light        glass-home-count.html        light 1280 1050
shot 2-glass-first-screen-dark         glass-home-count.html        dark  1280 1050
phone 3-glass-first-screen-phone       glass-home-count.html        light
shot 4-glass-headline-answers-table-light glass-home-table.html     light 1280 1050
shot 5-glass-headline-none-dark        glass-home-no-headline.html  dark  1280 1050
shot 6-glass-entry-page-light          glass-entry.html             light 1280 2180
shot 7-glass-entry-page-dark           glass-entry.html             dark  1280 2180
shot 8-page-first-screen-light         page-home-count.html         light 1280 1050
shot 9-page-first-screen-dark          page-home-count.html         dark  1280 1050
shot 10-page-headline-answers-table-light page-home-table.html      light 1280 1050
phone 11-page-first-screen-phone       page-home-count.html         light
rm -rf "$TMP"
