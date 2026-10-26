# Independent visual/source review — Week 06

Status: PASS for source, physical content and asset identity after the corrections below. Integrated browser/MathML/mobile acceptance remains root-owned.

Read each complete visual record and the corresponding source extracts; checked source equations and conditions. Original crop pixels were inspected. Self-drawn SVG geometry/curves were rendered and examined; every SVG label was also read from XML. The local raster renderer lacks CJK fonts, so Chinese font/layout acceptance is explicitly deferred to the live browser.

| Day | Literal source sentence | Key relation / provenance | Figure |
|---|---|---|---|
| 36 | PASS, depth PDF41, 22 words | depth PDF41 Eq.1.51 | original_crop; depth PDF41 Fig./Table 1.14 |
| 37 | PASS, spad PDF15, 22 words | depth PDF96 Eq.3.14 | redrawn; depth PDF96; no fictitious original figure number |
| 38 | PASS, spad PDF15, 26 words | depth PDF96 Eq.3.13 | redrawn; depth PDF96; no fictitious original figure number |
| 39 | PASS, depth PDF113, 21 words | depth PDF109 Eq.3.45 | redrawn; depth PDF109; no fictitious original figure number |
| 40 | PASS, depth PDF115, 15 words | spad PDF103 Eq.14 | redrawn; depth PDF115 Fig./Table 3.16 |
| 41 | PASS, depth PDF113, 17 words | depth PDF113 (explicitly derived / unnumbered) | redrawn; depth PDF113; no fictitious original figure number |
| 42 | PASS, depth PDF113, 17 words | depth PDF96 (explicitly derived / unnumbered) | original_crop; depth PDF112 Fig./Table 3.14 |

## Physical/source checks
- Four-phase sine convention checked against PDF96 Eq3.12–3.14; X=q3−q1 and Y=q0−q2 are compatible.
- Radial/axial geometry and phasor sum match source109 Eq3.45 and sourceSPAD103 Eq14.
- Four independent Poisson bucket count model yields σφ≈√b/(√2a); a,b are clearly electron counts rather than original voltage parameters A,B.
- Fig-number fields incorrectly holding equation numbers3.14/3.45/3.47 were cleared. Equations remain accurately referenced in captions.
- Day42 initial excerpt failed a plain literal match because of a source line-end hyphen. It was replaced with a complete literal sentence about saturation from the same source page113; translation/comment updated.
- Source Fig3.14 before/after plots have different y-axis scales AND different integration-time sets. Explanation now explicitly disallows paired-colour percentage-improvement claims.
- Original crops36/42 inspected; no whole pages reproduced. Added missing propagation-speed and nominal-phase entries to variable tables.

No unresolved source/physical-content blocker identified. No live-browser or GitHub deployment check is claimed by this reviewer.
