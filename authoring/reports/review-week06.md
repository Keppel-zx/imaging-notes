# Independent review: week 06, lessons 36–42

Reviewer: week3 author agent. Result: PASS after authorized citation-index fixes and short-excerpt additions. Root owns final browser QA/status.

Read all7 fragments and citations/week-06.json. Independently read depth40–49,93–97,107–117 and spad94–103,114–117,120. Depth37 page93 correctly warns its optical demodulation sketch is conceptual, not a literal receiver circuit. ToF classification difference between old source and modern engineering language is explicitly acknowledged.

Formula checks:
- depth Eq1.51@41: c*tau/2 and factor two correct;100ps→15mm is explicitly theoretical, not product data.
- depth Eq3.12@96 and3.16@97: q0=B+A sinphi, q1=B−A cosphi, q2=B−A sinphi, q3=B+A cosphi; atan2(Y,X) convention correctly preserved. Background mean cancellation is distinguished from shot fluctuations.
- Eq3.14@96,3.17–3.18@97: distance conversion and finite-window phase claim align; no invented Eq number for Ru.
- Eq3.45–3.46 are BOTH on depth109; grouped citation correct. Pixel coordinates are undistorted before geometric conversion.
- spad Eq12–15 are ALL on103; grouped citation correct. Mixed path complex addition and two-phasor perturbation expressions correct. Lesson40 appropriately limits the first book’s overly general convex-distance-mixture explanation.
- depth Eq3.48–3.49 are BOTH on116; grouped citation correct.
- depth Eq3.47@113: source uses signal-amplitude units without full counting normalization. Lesson41 avoids false unit conversion, supplies an explicitly independent four-bucket Poisson derivation. Its sigma_phi²=b/(2a²) follows from VarX=VarY=2b and radius²=4a². Conditions and nonuniversality of prefactor clearly stated.
- RMSE finite-sample factor (N−1)/N, quantization Δt/sqrt12, independent averaging and covariance caveats correct. Temperature linear coefficient explicitly supplemental, not fabricated book parameter.
- Phase/frequency first-order error derivative correct. Systematic bias, periodic ambiguity, multipath, random precision and output quantization carefully separated.

Figure checks: depth1.14@41,1.15a@42,1.16@45,1.17@47,3.1@93,3.2@95,3.11@108,3.12@110,3.13/3.14@112,3.16@115,3.17/3.18@117; spad2@96,3@97,4/5@99 all align with descriptions. No unsupported numerical plot extraction or experimental data added.

Required citation-index completeness fixes (no concurrent author edits made):
1. day38 body cites depth92–97 but pdf_pages omits92–93. Add pages or narrow body reference; page92 is chapter opener,93 is already independently checked.
2. day39 loc/body cites depth41, but its record omits41. Add41.
3. day40 body cites spad114–117 for recovery burden; its source record ends103. Add114–117. Independently read114–117 and claim is supported (large measurement sequences/iterative computational burden/long integration and high data rates).
4. day42 derived equation anchors depth96 while its pdf_pages begins107. Add96, since phase conversion belongs there.
5. day36–39 and41 lack necessary short English excerpt/quote records in reviewed version. Exact available options:36 “stop-watch”@depth42;37 “Sinusoidal Modulation”@depth94;38 “Direct CW”@depth43;39 “precision, or repeatability”@depth113;41 “background illumination”@depth113. With existing42 “phase wrapping”, this remains a short quote budget. Root should coordinate total-source quotation budget.

All7 have balanced inline/display TeX delimiters and no unexpected control characters. Han counts excluding references and tags at review: {"36": 2134, "37": 2023, "38": 2054, "39": 2026, "40": 2062, "41": 2110, "42": 2103}.

## Corrections applied after root authorization

All five items above resolved: pages added, literal English terms and Chinese explanation inserted in36–39/41, quote metadata updated. No original formula-page split was needed: all grouped original-number anchors were already on single correct pages. Original report findings retained for audit.
