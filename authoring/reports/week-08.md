# Week 08 author verification

Status: review_ready. Final integrated browser/mobile/navigation acceptance belongs to root.

All seven interrupted drafts were expanded with distinct original engineering discussion. No placeholders, exercises or Python experiments. Source information and supplementary derivation are separately labeled. No original images or full source tables are reproduced.

| Day | Han characters, reference section excluded |
|---|---:|
|50|2283|
|51|2220|
|52|2183|
|53|2173|
|54|2179|
|55|2209|
|56|2266|

## Source and formula audit

Actual relevant page extracts read: EMVA5–8,17–18,31–32; spad9,16,18,20,29; depth63,95–96,111,113–117,127–130; benchmark107,110,113–115,255–256,274–279,335–336,367. Some page ranges in citations record the complete scope of the original drafts; key displayed source formulas and figures were rechecked directly.

Rendered and visually inspected original pages benchmark256 (Eq7.8),274 (Eqs7.42–44),336 (Eq9.1), depth63 (Eq2.6/Fig2.8),96 (Eq3.14). Rendered depth127/130 retained in internal qa/week08 for the independent reviewer. Source PNGs must not enter public bundle.

- Day50 explicitly defines S_y as dark-subtracted digital mean, preserves EMVA DN/e− gain convention; SPAD PDE text definition is marked symbolic rewriting, counting budget is low-flux independent-events only.
- Day51 compares disparity/phase/time in consistent length units; does not confuse radial range with optical-axis depth or claim any current product ranking.
- Day52 reproduces checked PSNR/MSE and edge acutance; source Eq7.47 is intentionally not reproduced because printed structure denominator differs from conventional SSIM. The note preserves this uncertainty rather than silently inventing a corrected book equation.
- Day53 required-electron quadratic root is explicitly derived from EMVA11/15; same-workpoint and mode constraints retained.
- Day54 bias/sample deviation/RMSE and valid-rate equations are engineering definitions, not invented numbered source equations. Fig3.17 located accurately at117 while discussion starts116, and no universal area-average range model is asserted.
- Day55 variance fractions and removal upper-bound SNR ratio are supplementary independent-variance derivations; variables and units are explicit.
- Day56 Eq9.1 combines same-scale JND losses, not heterogeneous physical units.

Each lesson has one indexed, literal short English phrase and Chinese interpretation, checked with only whitespace/ligature normalization: dead time (spad18); Accuracy and precision (depth127); viewing conditions (benchmark255); Operation point(s) (emva31); true value (depth127); shot noise (emva6); quality loss (benchmark336). Quote totals: spad2,depth5,benchmark4,emva4 English words.

Citation JSON enumerates substantive source formulas, derived relations and all analyzed numbered figures/tables with real PDF anchors and descriptions. HTML TeX delimiters balanced; no control characters or raw math less-than tags. Han counts all2000–3000.

No known unresolved source/physics blocker. Independent review by review_final7_8 remains authoritative for cross-check findings; root owns final status.
