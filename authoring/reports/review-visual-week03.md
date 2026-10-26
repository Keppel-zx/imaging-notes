# Independent visual-source review — Week 03

Status: PASS after recorded metadata/diagram refinements. Final integrated webpage/mobile checks remain root-owned.

Read every final excerpt, translation, explanatory comment, formula and variable table in week-03.json. Literal English source tests use NFKC and whitespace normalization against the actual extracted PDF pages. All seven excerpts match; no two-word placeholder excerpts. Every key relation compared with actual original numbered relation or with the clearly labeled supplementary derivation in the stable course.

Actual source pages checked: colour:107, colour:108, colour:109, colour:110, colour:112, colour:113, colour:114, colour:116, colour:117, colour:120.

| Day | Excerpt source | Figure type | Key relation source |
|---|---|---|---|
| 15 | colour PDF107 | redrawn | colour PDF107 / 未编号/补充推导 |
| 16 | colour PDF109 | redrawn | colour PDF109 / 未编号/补充推导 |
| 17 | colour PDF113 | original_crop | colour PDF113 / 未编号/补充推导 |
| 18 | colour PDF112 | redrawn | colour PDF112 / 未编号/补充推导 |
| 19 | colour PDF116 | redrawn | colour PDF117 / 未编号/补充推导 |
| 20 | colour PDF114 | redrawn | colour PDF116 / 未编号/补充推导 |
| 21 | colour PDF120 | redrawn | colour PDF108 / 未编号/补充推导 |

All original figure crops were visually inspected (EMVA Fig1/5/6/7, colour Fig5.5/2.2, benchmark Fig6.27/7.6 as applicable); identities and page labels agree. Crops contain the discussed figure and optional caption, not full pages. EMVA plotted examples remain explicitly labeled simulated. Self-drawn SVGs parsed successfully and were inspected for teaching model, axes/units, colour roles, correct equation/logic, and non-experimental labeling. No invented measured sensor values are asserted.

Corrections: the blue Bayer pixel used in the reconstruction example is now explicitly highlighted and connected to the RGB reconstruction, removing ambiguity about which channel is measured. Variable typography normalized to TeX. White-balance example and operation-order values checked algebraically.

MathML conversion of all seven key formula strings and every variable symbol succeeded without unknown-command tokens. No unresolved substantive source, formula or visual-physics issue found. This does not assert browser rendering acceptance.
