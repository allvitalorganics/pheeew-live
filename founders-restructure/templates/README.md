# Pheeew · Justin Onboarding · Templates Folder

This folder contains every email and document template needed for Justin Kim's onboarding as 4th co-founder of Pheeew, Inc.

## File formats present

Each template ships in TWO formats:
- **`.pdf`** — print-ready, Pheeew-branded, attach directly to email
- **`.md`** — source Markdown, edit blanks (`[DATE]`, `[SIGNATURE]`, etc.) before re-rendering

The live tracker at `/founders-restructure/` links to the **`.pdf`** versions by default.

## How to use these files

**Emails** (E01-E11)
- Open the `.pdf` to read the formatted version
- For sending: open the `.md`, copy/paste body into Gmail or your email client, replace `[BRACKETS]`
- Save sent emails to `_Communications/` for the paper trail

**Documents** (D01-D15)
- Open the `.pdf` for review, sharing, or as the attached template
- For editing the blanks before signing: open the `.md` in any text editor, fill in `[DATE]`, `[SIGNATURE]`, party-specific data, then re-render to PDF (see "Regenerating PDFs" below)
- Sign the final PDF (DocuSign, HelloSign, or print-and-wet-sign + scan)
- Save signed PDFs to `_Signed/` (for corporate documents) or proper folder per Records Index

## Regenerating PDFs after editing

After filling blanks in any `.md` file, regenerate the matching `.pdf`:

```bash
cd /tmp/pheeew-live/founders-restructure/templates
./_build-pdfs.sh           # rebuilds ALL 27
# or single-file:
pandoc D04_RSPA_Justin-Kim.md --from gfm --to html5 --standalone -o _tmp.html
weasyprint _tmp.html D04_RSPA_Justin-Kim.pdf --stylesheet _pdf-style.css
rm _tmp.html
```

Requires `pandoc` and `weasyprint` (install: `brew install pandoc weasyprint`).

## Folder destinations after signing

| File | Final location |
|---|---|
| D01 Board Resolution (signed) | `_Signed/D01_Board-Resolution_signed.pdf` |
| D02 Stockholder Consent (signed) | `_Signed/D02_Stockholder-Consent_signed.pdf` |
| D03 Certificate of Amendment + DE Stamped Copy | `_DE_Filing/` |
| D04 Justin RSPA (signed) | `../../03_RSPAs/_Justin/D04_Justin-Kim_RSPA_signed.pdf` |
| D05 Alex Refresh RSPA (signed) | `../../03_RSPAs/_Justin/D05_Alex-Kim_Refresh-RSPA_signed.pdf` |
| D06 Jason Refresh RSPA (signed) | `../../03_RSPAs/_Justin/D06_Jason-Ko_Refresh-RSPA_signed.pdf` |
| D07 Justin CIIAA (signed) | `../../05_CIIAAs/Pheeew_CIIAA_Justin-Kim_signed.pdf` |
| D08 Co-Founder Agreement v3 (signed) | `_Signed/D08_Co-Founder-Agreement-v3_signed.pdf` |
| D09/D10/D14 83(b) (signed) | `../../06_83b_Elections/_Round-2/` + `_Proof_of_Filing/` for USPS receipts |
| D11/D12a/D12b Stock Certs (signed) | `../../04_Stock_Certificates/` |
| D13 Capital Contribution Receipt | `../../08_Capital_Contributions/Justin_Kim_RSPA_Payment_Completion_2026-05-XX.md` |
| D15 Cap Table v2 | `../../07_Cap_Table/Pheeew_CapTable_v2_20260514.html` (and .pdf) |

## Sequence

Follow the live tracker at:
**https://allvitalorganics.github.io/pheeew-live/founders-restructure/**

Phase by phase. Step by step. Don't skip ahead.

## Critical timing

**83(b) elections (D9, D10, D14)** must be mailed via USPS Certified Mail with Return Receipt **within 30 days of grant date** (RSPA execution date). Aim to mail within 5-10 days of signing. **No extensions, no exceptions.**

## Master document

Full inline-context version: `/Pheeew/Deliverables/Pheeew_Justin_Onboarding_Master.md`
