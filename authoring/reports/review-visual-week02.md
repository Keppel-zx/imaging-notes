# Independent visual-source review — Week 02

Status: PASS after recorded metadata/diagram refinements. Final integrated webpage/mobile checks remain root-owned.

Read every final excerpt, translation, explanatory comment, formula and variable table in week-02.json. Literal English source tests use NFKC and whitespace normalization against the actual extracted PDF pages. All seven excerpts match; no two-word placeholder excerpts. Every key relation compared with actual original numbered relation or with the clearly labeled supplementary derivation in the stable course.

Actual source pages checked: emva:5, emva:6, emva:7, emva:12, emva:16, emva:17, emva:18, emva:21, emva:22, ptc:42, ptc:57.

| Day | Excerpt source | Figure type | Key relation source |
|---|---|---|---|
| 08 | emva PDF5 | original_crop | emva PDF6 / 9 |
| 09 | ptc PDF42 | redrawn | ptc PDF42 / 4.5 |
| 10 | emva PDF17 | original_crop | emva PDF16 / 未编号/补充推导 |
| 11 | emva PDF7 | original_crop | emva PDF7 / 14 |
| 12 | emva PDF21 | redrawn | emva PDF22 / 46 |
| 13 | emva PDF17 | original_crop | emva PDF6 / 9 |
| 14 | emva PDF12 | original_crop | emva PDF17 / 30 |

All original figure crops were visually inspected (EMVA Fig1/5/6/7, colour Fig5.5/2.2, benchmark Fig6.27/7.6 as applicable); identities and page labels agree. Crops contain the discussed figure and optional caption, not full pages. EMVA plotted examples remain explicitly labeled simulated. Self-drawn SVGs parsed successfully and were inspected for teaching model, axes/units, colour roles, correct equation/logic, and non-experimental labeling. No invented measured sensor values are asserted.

Corrections: variable symbols changed from flattened Unicode labels (e.g. μy and σy²) to explicit TeX subscripts/powers. TeX key strings now use single command backslashes. Key Eq6/9 and inverse-gain conventions checked; PRNU percent conversion clarified. Photon Transfer G (e⁻/DN) explicitly distinguished from EMVA K (DN/e⁻).

MathML conversion of all seven key formula strings and every variable symbol succeeded without unknown-command tokens. No unresolved substantive source, formula or visual-physics issue found. This does not assert browser rendering acceptance.
