# Independent visual-source review — Week 04

Status: PASS after recorded metadata/diagram refinements. Final integrated webpage/mobile checks remain root-owned.

Read every final excerpt, translation, explanatory comment, formula and variable table in week-04.json. Literal English source tests use NFKC and whitespace normalization against the actual extracted PDF pages. All seven excerpts match; no two-word placeholder excerpts. Every key relation compared with actual original numbered relation or with the clearly labeled supplementary derivation in the stable course.

Actual source pages checked: benchmark:52, benchmark:53, benchmark:54, benchmark:140, benchmark:143, benchmark:192, benchmark:193, benchmark:212, benchmark:221, benchmark:232, benchmark:233, benchmark:256, benchmark:257, colour:59, colour:61.

| Day | Excerpt source | Figure type | Key relation source |
|---|---|---|---|
| 22 | benchmark PDF53 | redrawn | benchmark PDF52 / 未编号/补充推导 |
| 23 | benchmark PDF212 | original_crop | benchmark PDF212 / 6.32 |
| 24 | benchmark PDF233 | redrawn | benchmark PDF233 / 6.66 |
| 25 | colour PDF59 | original_crop | colour PDF59 / 2.13 |
| 26 | benchmark PDF193 | redrawn | benchmark PDF193 / 未编号/补充推导 |
| 27 | benchmark PDF143 | redrawn | benchmark PDF140 / 5.1 |
| 28 | benchmark PDF256 | original_crop | benchmark PDF256 / 7.8 |

All original figure crops were visually inspected (EMVA Fig1/5/6/7, colour Fig5.5/2.2, benchmark Fig6.27/7.6 as applicable); identities and page labels agree. Crops contain the discussed figure and optional caption, not full pages. EMVA plotted examples remain explicitly labeled simulated. Self-drawn SVGs parsed successfully and were inspected for teaching model, axes/units, colour roles, correct equation/logic, and non-experimental labeling. No invented measured sensor values are asserted.

Corrections: equal-noise illustration now states normalized target mean/std and notes integer-display quantization instead of claiming exact integer moments. Dynamic-range electron-ratio teaching approximation now explicitly states read-noise-dominant/SNR≈1 boundary. Lab Eq2.13, input-referred SNR Eq6.66, Weber Eq5.1 and acutance Eq7.8 checked against actual source pages.

MathML conversion of all seven key formula strings and every variable symbol succeeded without unknown-command tokens. No unresolved substantive source, formula or visual-physics issue found. This does not assert browser rendering acceptance.
