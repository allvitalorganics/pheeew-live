#!/usr/bin/env python3
"""
Build a reference.docx for pandoc that styles all 27 templates as legal
documents matching the existing Pheeew, Inc. signed corpus:
  - Times New Roman 11pt body, 1.15 line spacing
  - 1-inch margins all sides
  - Centered serif H1 (document title) with bottom rule
  - Centered serif H2 (entity name)
  - Bold ALL CAPS H2 article headings with bottom rule (left-aligned)
  - Bold left-aligned H3 sub-headings
  - Justified body paragraphs
  - Light-grey table headers, no fill on body cells
"""

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.shared import Pt, Inches, RGBColor, Cm
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import sys

OUT = sys.argv[1] if len(sys.argv) > 1 else "_reference.docx"

doc = Document()

# ─── Page margins ─────────────────────────────────────────────────────
for section in doc.sections:
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)

# ─── Styles ───────────────────────────────────────────────────────────
styles = doc.styles

def set_font(style, name="Times New Roman", size=11, bold=False, italic=False,
             color=None, all_caps=False):
    f = style.font
    f.name = name
    # Set East Asian + complex script font too (so Word doesn't fallback)
    rpr = style.element.get_or_add_rPr()
    rfonts = rpr.find(qn('w:rFonts'))
    if rfonts is None:
        rfonts = OxmlElement('w:rFonts')
        rpr.append(rfonts)
    rfonts.set(qn('w:ascii'), name)
    rfonts.set(qn('w:hAnsi'), name)
    rfonts.set(qn('w:cs'), name)
    rfonts.set(qn('w:eastAsia'), name)
    f.size = Pt(size)
    f.bold = bold
    f.italic = italic
    if all_caps:
        f.all_caps = True
    if color:
        f.color.rgb = RGBColor(*color)

def set_paragraph(style, alignment=None, space_before=0, space_after=8,
                  line_spacing=1.15, keep_with_next=False, keep_lines=True):
    pf = style.paragraph_format
    if alignment is not None:
        pf.alignment = alignment
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    pf.line_spacing = line_spacing
    pf.keep_with_next = keep_with_next
    pf.keep_together = keep_lines

# Normal (body)
normal = styles['Normal']
set_font(normal, "Times New Roman", 11)
set_paragraph(normal, WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=8, line_spacing=1.25)

# Title (H1) — centered, large, bold serif
h1 = styles['Heading 1']
set_font(h1, "Times New Roman", 18, bold=True, color=(0, 0, 0))
set_paragraph(h1, WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=8,
              line_spacing=1.15, keep_with_next=True)

# H2 — entity name OR article heading
# Default H2 → article heading: bold ALL CAPS, left-align, bottom border via direct format on rendering
h2 = styles['Heading 2']
set_font(h2, "Times New Roman", 11, bold=True, color=(0, 0, 0), all_caps=True)
set_paragraph(h2, WD_ALIGN_PARAGRAPH.LEFT, space_before=18, space_after=10,
              line_spacing=1.15, keep_with_next=True)

# H3 — section sub-headings: bold, left-align, normal case
h3 = styles['Heading 3']
set_font(h3, "Times New Roman", 11, bold=True, color=(0, 0, 0))
set_paragraph(h3, WD_ALIGN_PARAGRAPH.LEFT, space_before=12, space_after=4,
              line_spacing=1.15, keep_with_next=True)

# Block Quote — used for restrictive legends and Collaboration Principle quote
try:
    bq = styles['Quote']
except KeyError:
    bq = styles.add_style('Quote', 1)
set_font(bq, "Times New Roman", 11, italic=True)
set_paragraph(bq, WD_ALIGN_PARAGRAPH.LEFT, space_before=8, space_after=8,
              line_spacing=1.25)
bq.paragraph_format.left_indent = Inches(0.4)
bq.paragraph_format.right_indent = Inches(0.4)

# List paragraph
try:
    lp = styles['List Paragraph']
    set_font(lp, "Times New Roman", 11)
    set_paragraph(lp, WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=4, line_spacing=1.25)
except KeyError:
    pass

# Table styles — pandoc uses "Table" style for tables
# We'll set this so default tables render with thin borders + light-grey header
try:
    tbl = styles['Table Grid']
    set_font(tbl, "Times New Roman", 10.5)
except KeyError:
    pass

# ─── Add a placeholder so reference doc has content (pandoc requires this) ─
p = doc.add_paragraph("Placeholder — this paragraph is removed during conversion.")
doc.save(OUT)
print(f"✓ Wrote {OUT}")
