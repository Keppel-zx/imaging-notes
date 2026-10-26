# Independent visual/source review — Week 08

Status: PASS for source, physical content and asset identity after the corrections below. Integrated browser/MathML/mobile acceptance remains root-owned.

Read each complete visual record and the corresponding source extracts; checked source equations and conditions. Original crop pixels were inspected. Self-drawn SVG geometry/curves were rendered and examined; every SVG label was also read from XML. The local raster renderer lacks CJK fonts, so Chinese font/layout acceptance is explicitly deferred to the live browser.

| Day | Literal source sentence | Key relation / provenance | Figure |
|---|---|---|---|
| 50 | PASS, spad PDF20, 29 words | spad PDF29 (explicitly derived / unnumbered) | redrawn; spad PDF20; no fictitious original figure number |
| 51 | PASS, depth PDF63, 21 words | depth PDF96 (explicitly derived / unnumbered) | redrawn; depth PDF96; no fictitious original figure number |
| 52 | PASS, benchmark PDF274, 16 words | benchmark PDF274 Eq.7.44 | original_crop; benchmark PDF278 Fig./Table 7.11（a–d） |
| 53 | PASS, emva PDF31, 19 words | emva PDF7 (explicitly derived / unnumbered) | redrawn; emva PDF7; no fictitious original figure number |
| 54 | PASS, depth PDF128, 19 words | depth PDF175 (explicitly derived / unnumbered) | redrawn; depth PDF127; no fictitious original figure number |
| 55 | PASS, emva PDF7, 26 words | emva PDF6 Eq.9 | redrawn; benchmark PDF107; no fictitious original figure number |
| 56 | PASS, benchmark PDF336, 30 words | benchmark PDF336 Eq.9.1 | redrawn; benchmark PDF336; no fictitious original figure number |

## Physical/source checks
- PDE comparison uses originalSPAD29 footnote; no equivalence between event amplitude and integrated electron number is asserted.
- iToF uncertainty propagation requires small phase variation in the correct cycle; periodic errors and multipath remain outside the formula.
- PSNR exact8bit relation matches source274 Eq7.44. Source278 Fig7.11(a–d) caption confirms equal30dB for the three shown degradation types; no missing panels claimed.
- Required-electron-number inversion agrees with S=N/√(N+B), using numerical electron-count statistics and stated assumptions.
- Coverage V is clearly an added evaluation definition. RMSE/coverage/latency are not aggregated into arbitrary mixed-unit scores.
- Minkowski combination matches source336 Eq9.1 and explicitly requires a common meaningful loss scale.
- Day51 carriage-return escape in σρ variable repaired; all key relation TeX/variable strings convert successfully.

No unresolved source/physical-content blocker identified. No live-browser or GitHub deployment check is claimed by this reviewer.
