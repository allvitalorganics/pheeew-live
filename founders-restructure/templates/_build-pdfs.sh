#!/bin/bash
# Convert all .md templates to BOTH .docx (Word, primary editable format) and
# .pdf (read-only print version). Uses _reference.docx for Word styling and
# _pdf-style.css for the PDF.
set -e

cd "$(dirname "$0")"
CSS="_pdf-style.css"
REF="_reference.docx"

# Regenerate the reference docx (idempotent)
if [ ! -f "$REF" ] || [ "_make-reference-docx.py" -nt "$REF" ]; then
  echo "  Building $REF ..."
  python3 _make-reference-docx.py "$REF" > /dev/null
fi

count=0
for md in [DE]*.md; do
  base="${md%.md}"
  echo "  → $md"

  # .docx via pandoc + reference styling
  pandoc "$md" \
    --from gfm \
    --to docx \
    --reference-doc="$REF" \
    -o "${base}.docx"

  # .pdf via pandoc → html5 → weasyprint
  pandoc "$md" \
    --from gfm \
    --to html5 \
    --standalone \
    --metadata title="${base}" \
    -o "_tmp.html"
  weasyprint "_tmp.html" "${base}.pdf" --stylesheet "$CSS" 2>&1 \
    | grep -v "^WARNING\|^INFO" || true

  count=$((count+1))
done
rm -f _tmp.html

echo ""
echo "✓ Converted $count templates."
echo "  .docx files: $(ls *.docx 2>/dev/null | wc -l | xargs)"
echo "  .pdf files:  $(ls *.pdf 2>/dev/null | wc -l | xargs)"
