# Independent review Week 08

Status: PASS for content, source and formula review after author clarification. Root still owns integrated browser/mobile/navigation acceptance and completed flags.

Reviewer fully read all seven original draft bodies and the seven expanded final engineering sections, then reviewed complete citation records. Final bodies contain 2225/2162/2121/2111/2115/2146/2202 Han characters respectively for days50–56 after removing headings, tags and references. They are full original explanatory lessons, not short overview placeholders; added sections address distinct engineering decisions rather than repetitive padding.

## Source and physical-model checks

- Day50: EMVA PDF5–8 formulas5–7; SPAD PDF9/18/20/29. S_y is now explicitly μ_y−μ_y.dark, resolving the review clarity request. PDP versus full-array PDE and CMOS process versus charge-integration architecture are distinguished. Low-flux event counts and SNR are supplementary, with dead-time/afterpulse/crosstalk exclusions. Timing LSB versus jitter versus estimator precision follows actual Table1 PDF29.
- Day51: depth2.6 PDF63,3.14 PDF96, phase-wrap range PDF111, Figs2.8/3.2/4.1 PDF63/95/127 and accuracy/precision PDF127–128 match. Range-dependent photon statistics and motion/registration limitations prevent the ideal propagation equations from being presented as unconditional product rankings.
- Day52: benchmark7.42–44 PDF274 and7.8 PDF256 match actual originals. PSNR is separated from acquisition SNR and perceptual quality. Fig7.11 PDF278 and adjacent discussion support the different-error-structure analysis. The original SSIM denominator discrepancy is disclosed and not silently rewritten.
- Day53: EMVA11/15 PDF7 algebraically support the required-signal root, including total input-noise variance. Same-workpoint and sensor-output constraints follow EMVA31–32. SPAD Table1 PDF29 and benchmark367 support resource/performance and task-specific scope. No invented device recommendation or unverified industry value appears.
- Day54: sample bias/variance/RMSE decomposition and valid-pixel-rate definitions are explicitly supplementary. RMSE identity correctly uses population-denominator residual variance while the separately defined sample standard deviation uses n−1. Depth127–130 and63/96 support terminology and propagation; Fig3.17 is now correctly located at PDF117, with mechanism discussion beginning116.
- Day55: EMVA9 PDF6 is correctly restated; independent-variance sensitivity bound sqrt(V/(V−V_i)) is explicitly derived and valid under fixed signal and independent terms. benchmark107/110/114 support noise regime, sensor blur and black-level color-error diagnostics; depth115/127 support multipath/bias-versus-repeatability.
- Day56: benchmark9.1 PDF336 is correctly transcribed, uses common calibrated JND losses and independent-attribute conditions rather than mixing physical units. Four-stage synthesis preserves units, evidence strength and task boundaries. Historical examples are not asserted as present product performance.

Critical source pages checked include EMVA6–7/31–32; SPAD18/20/29; depth63/96/111/113/115–116/127–130; benchmark256/274/335–336/367 and the cited sensor/ISP passages. The author also rendered and visually checked complex originals256/274/336/63/96; earlier independent review rendered related calibration and fusion pages.

## Citation and copyright checks

All per-source cited PDF page files exist. Formula and figure identity/page pairs match source content for the substantive relations listed above. English quotations match exact source phrases after typographic ligature/whitespace normalization; each lesson has a short original phrase with Chinese interpretation. No original textbook image, large continuous passage or manufactured measurement is reproduced. No Python experiments or revision questions are included.

No unresolved blocking content, source-identity, formula or depth issue remains. Final website formula rendering and responsive reading remain separate root checks.
