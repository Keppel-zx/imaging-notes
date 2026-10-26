# Independent visual/source review — Week 05

Status: PASS for source, physical content and asset identity after the corrections below. Integrated browser/MathML/mobile acceptance remains root-owned.

Read each complete visual record and the corresponding source extracts; checked source equations and conditions. Original crop pixels were inspected. Self-drawn SVG geometry/curves were rendered and examined; every SVG label was also read from XML. The local raster renderer lacks CJK fonts, so Chinese font/layout acceptance is explicitly deferred to the live browser.

| Day | Literal source sentence | Key relation / provenance | Figure |
|---|---|---|---|
| 29 | PASS, spad PDF20, 29 words | spad PDF21 (explicitly derived / unnumbered) | original_crop; spad PDF21 Fig./Table 4 |
| 30 | PASS, spad PDF18, 18 words | spad PDF18 (explicitly derived / unnumbered) | redrawn; spad PDF18 Fig./Table 1 |
| 31 | PASS, spad PDF18, 17 words | spad PDF29 (explicitly derived / unnumbered) | redrawn; spad PDF29 Fig./Table Table 1, footnote 3 |
| 32 | PASS, spad PDF18, 16 words | spad PDF18 (explicitly derived / unnumbered) | original_crop; spad PDF24 Fig./Table 8 |
| 33 | PASS, spad PDF24, 21 words | spad PDF24 (explicitly derived / unnumbered) | redrawn; spad PDF23 Fig./Table 7 |
| 34 | PASS, spad PDF16, 19 words | spad PDF16 (explicitly derived / unnumbered) | redrawn; spad PDF16; no fictitious original figure number |
| 35 | PASS, spad PDF20, 16 words | spad PDF32 (explicitly derived / unnumbered) | redrawn; spad PDF33 Fig./Table 18 |

## Physical/source checks
- Single-photon event versus integrated charge is kept distinct. Effective count budget is explicitly a weak-occupancy teaching model.
- PDP/PDE/FF agrees with the original PDF29 footnote. No optics or dead-time efficiency is silently included.
- Quench/recharge wording clarified: afterpulsing constrains an engineering hold-off interval, not the physical possibility of fast capacitive charging.
- Nonparalyzable dead-time and first-event Poisson formulas are explicitly supplementary, with their reception assumptions.
- TDC coverage formula now specifies the width of 2^b quantization intervals, distinguishing the (2^b−1)Δt separation between first/last code centres.
- Fig18 source page corrected from32 to33. Source jitter-tail crop is not mislabeled as an afterpulse measurement.
- Original crops29/32 retain intended complete system/axes; coordinates retained in metadata.

No unresolved source/physical-content blocker identified. No live-browser or GitHub deployment check is claimed by this reviewer.
