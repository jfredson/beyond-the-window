#!/bin/sh
# Photographs the running site into docs/site-pictures/<date>/ with a headless Chrome.
#   sh scripts/pictures.sh 2026-11-17
#   sh scripts/pictures.sh 2026-11-20 draft   only the draft of the rebuilt home page, into
#                                             docs/site-pictures/<date>-draft/ (added 2026-11-20)
# The site must already be running on port 4329 (the project's dev server, .claude/launch.json).
# Needs Google Chrome and Python with the Pillow library. Adapted from the design session's
# docs/design/mockups/capture.sh on 2026-11-17.
set -e
cd "$(dirname "$0")/.."
DAY="${1:?give the date, year-month-day}"
BASE="http://localhost:4329"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUT="docs/site-pictures/$DAY"
[ "$2" = draft ] && OUT="docs/site-pictures/$DAY-draft"
TMP=$(mktemp -d)
mkdir -p "$OUT"
# A phone is photographed through a frame 390 points wide, because a headless Chrome window
# cannot be made that narrow.
cat > "$TMP/phone.html" <<'HTML'
<!doctype html><meta charset="utf-8"><style>html,body{margin:0;background:#fff}iframe{border:0;width:390px;height:4000px;display:block}</style>
<iframe id="f"></iframe><script>document.getElementById('f').src = location.hash.slice(1);</script>
HTML
shot() { # name path theme width height
  # 0 is dark and 1 is light in Chrome's setting; without it the pictures follow this Mac's own setting
  DARK="--blink-settings=preferredColorScheme=1"; [ "$3" = dark ] && DARK="--blink-settings=preferredColorScheme=0"
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 $DARK \
    --user-data-dir="$TMP/profile-$3" --window-size="$4,$5" --virtual-time-budget=4000 \
    --screenshot="$TMP/$1.png" "$BASE$2" >/dev/null 2>&1
  python3 - "$TMP/$1.png" "$OUT/$1.jpg" 1600 <<'PY'
import sys
from PIL import Image
im = Image.open(sys.argv[1]).convert('RGB')
w = int(sys.argv[3])
if im.width > w:
    im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
im.save(sys.argv[2], quality=88)
PY
  echo "  $OUT/$1.jpg"
}
phone() { # name path height theme (light when the theme is left off)
  DARK="--blink-settings=preferredColorScheme=1"; [ "$4" = dark ] && DARK="--blink-settings=preferredColorScheme=0"
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
    $DARK --user-data-dir="$TMP/profile-phone-${4:-light}" --window-size=600,"$3" --virtual-time-budget=4000 \
    --screenshot="$TMP/$1.png" "file://$TMP/phone.html#$BASE$2" >/dev/null 2>&1
  python3 - "$TMP/$1.png" "$OUT/$1.jpg" <<'PY'
import sys
from PIL import Image
im = Image.open(sys.argv[1]).convert('RGB')
im.crop((0, 0, 780, im.height)).save(sys.argv[2], quality=88)
PY
  echo "  $OUT/$1.jpg"
}
if [ "$2" = draft ]; then
  # The first screen as a phone shows it (390 by 844 points), then the whole page.
  phone 1-draft-first-screen       /draft/      844
  phone 2-draft-phone              /draft/      6200
  phone 3-draft-phone-dark         /draft/      6200 dark
  phone 4-draft-b-first-screen     /draft/b/    844
  phone 5-draft-b-phone            /draft/b/    2400
  phone 6-draft-acts-phone         /draft/acts/ 5200
  shot  7-draft-light              /draft/      light 1280 3300
  phone 8-published-home-phone      /            3400
  rm -rf "$TMP"
  exit 0
fi
shot  1-home-light        /                                   light 1280 1900
shot  2-home-dark         /                                   dark  1280 1900
phone 3-home-phone        /                                   3400
shot  4-entry-light       /list/kept-files-of-retired-models/ light 1280 2700
shot  5-entry-dark        /list/welfare-assessment-at-release/ dark 1280 3300
shot  6-entry-beside-light /list/law-against-legal-personhood/ light 1280 3000
shot  7-about-light       /about/                             light 1280 3400
shot  8-still-asking-dark /still-asking/                      dark  1280 2300
phone 9-entry-phone       /list/ending-a-conversation/        3900
# Added 2026-11-18, so the sentence at the top can be seen on the home page and the list page in
# both themes at both widths.
phone 10-home-phone-dark  /                                   3400 dark
shot  11-list-light       /list/                              light 1280 2100
shot  12-list-dark        /list/                              dark  1280 2100
phone 13-list-phone       /list/                              3300
phone 14-list-phone-dark  /list/                              3300 dark
# 15 and 16 are close-ups cut by hand from pictures 1 and 7.
shot  17-memory-beside-light /list/memory-across-conversations/ light 1280 3300
rm -rf "$TMP"
