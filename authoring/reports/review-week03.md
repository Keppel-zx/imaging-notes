# Independent review of Week 03

Reviewer: week2 agent. Reviewed complete body of days 15–21, citation JSON, corresponding source-page extracts; no author files edited.

Result: content/citation/formula review passes with metadata refinement recommended. Final integrated navigation, mathematics rendering and mobile QA remain root responsibility. This report does not set completed status.

## Coverage and depth

Han counts (HTML stripped, reference section excluded; headings included): day15 2090, day16 2096, day17 2121, day18 2068, day19 2067, day20 2186, day21 2153. Each lesson contains substantial original conceptual and engineering explanation; no page is a brief summary placeholder. No Python experiments or revision questions. No extensive source-image or prose reproduction.

Read source extracts: colour PDF83,106–120; isp PDF85,119,125,129,137–139,144–145,150,170,177,182–184,205,220–221. Rendered source PDF83,107,108,110,112,113,114,116,119; visually inspected in detail PDF83,112,113,114 for formula and figure fidelity.

## Citation and formula findings

- Day15: CFA observation model explicitly supplemental; fixed-spectrum relative exposure relation dimensionally consistent. RAW may be semi-processed and device-dependent: directly supported by colour PDF117–118. Figs5.1/5.2 correct PDF107/108.
- Day16: black subtraction, normalization and shading error propagation explicitly supplemental. Denominator derivative approximation is disclosed, not presented as exact derivative. Gain multiplies signal/noise together; source does not assert equal postcorrection SNR. Fig5.3 correct PDF110, including two green masks same in shown example.
- Day17: weighted interpolation corresponds to Fig5.5 PDF113 and continuation PDF114. Fixed-weight independent-noise condition stated. Bias/variance relationship is marked supplemental. No false original equation number.
- Day18: diagonal WB appears in Fig5.4 PDF112, while colour regression equations (3.3),(3.4),(3.5),(3.6),(3.7),(3.8) ALL occur on PDF83, printed58. Rendered page confirmed this; no split-page error. Lesson uses row-vector convention and explicitly states equivalence. Original book assembles transposed coefficient vectors into a matrix, so convention disclosure is appropriate. Fig5.6 correct PDF114. The original figure has CIE1932 label while prose says CIE1931; lesson accurately flags rather than propagates the inconsistency.
- Day19: gamma model is labeled approximate, not exact sRGB; exposure fusion is labeled ideal supplemental model. No invented dynamic-range improvement. Figs5.7/5.8 correct PDF116/119.
- Day20: filtering, unsharp mask response, ideal temporal averaging and signal-dependent noise are supplemental, with independence and fixed-signal conditions. No original simulation or experimental data claim. Source supports noise/detail tradeoff and sensor-specific neural training requirement.
- Day21: function composition is an explanatory schematic, not rigid required ISP ordering; affine operations do not generally commute, covariance propagation is correct local small-noise relation. Source pipeline-order and multi-frame caveats accurately represented.

Short quoted English terms checked against cited source extracts. Source attribution year 2024 matches actual chapter copyright, regardless of uploaded filename 2023. No current product claims that require live verification.

## Recommended index refinement

The figures[].analysis fields in week03 citation JSON repeat generic text (“正文原图分析…”). Their page and identity are correct, but meaningful figure-specific index descriptions would improve compliance with the index contract. Suggested mappings:

- 5.1: filter sampling, micro-optics and spectral sensitivity jointly define device-dependent RGB.
- 5.2: typical pipeline combines forward processing and acquisition-control feedback; order is not universal.
- 5.3: per-position, per-channel gain flattens mean shading without proving uniform noise.
- 5.4: diagonal channel scaling neutralizes achromatic illumination response without full spectral correction.
- 5.5: nearby blue similarity controls weights used to reconstruct missing green at a blue pixel.
- 5.6: varying sensor sensitivities motivate mapping to device-independent color; source typo explicitly noted.
- 5.7: rendering combines global/selective color and tone, so visible differences cannot be attributed solely to one operation.
- 5.8: fusion before versus after rendering changes input linearity and noise-model applicability.

For finer index granularity, day18 compound original_number “3.3,3.5–3.8” can be split into separate records, all PDF83. This is a schema readability improvement, not an accuracy correction.

No unresolved blocking citation, physical-model or prose-depth issue identified.
