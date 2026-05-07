#!/bin/bash
# Convert all .md templates in this folder to .pdf via pandoc → HTML → weasyprint
set -e

cd "$(dirname "$0")"
CSS="_pdf-style.css"
HEADER='<meta charset="utf-8"><title>Pheeew Founder Restructure</title>'

count=0
for md in [DE]*.md; do
  pdf="${md%.md}.pdf"
  echo "  → $md → $pdf"
  pandoc "$md" \
    --from gfm \
    --to html5 \
    --standalone \
    --metadata title="${md%.md}" \
    -o "_tmp.html"
  weasyprint "_tmp.html" "$pdf" --stylesheet "$CSS" 2>&1 | grep -v "^WARNING\|^INFO" || true
  count=$((count+1))
done
rm -f _tmp.html
echo ""
echo "✓ Converted $count files."
ls -la *.pdf | wc -l | xargs echo "  PDF count:"
