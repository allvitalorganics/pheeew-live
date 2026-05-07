#!/bin/bash
# Convert all .md templates to .docx (Word) using _reference.docx for styling.
# .docx is the ONLY output format — PDF was dropped (Word handles its own
# Save-As-PDF cleanly, and we don't need a second untouchable artifact).
set -e

cd "$(dirname "$0")"
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
  pandoc "$md" \
    --from gfm \
    --to docx \
    --reference-doc="$REF" \
    -o "${base}.docx"
  count=$((count+1))
done

echo ""
echo "✓ Converted $count templates to .docx."
echo "  (PDFs intentionally not produced — open .docx in Word and File → Save As → PDF if needed.)"
