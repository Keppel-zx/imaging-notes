# Independent review of Week 5

Reviewer: week4 agent; no edits to week5 source by this reviewer.

## Source scope

Read SPAD-Based Sensors source PDF15–21,23–27,29–34,37. Cross-checked equations (2), (6), (7), (8); figure captions 1,4,7,8,9,11,15,18,19,20; Table 1 and PDE footnote3. Visually rendered PDF24 (Fig8 timing tail),29 (Table1 & footnote),33 (Eq7–9 & Fig18).

## Body depth

Counts exclude reference section and headings:

- day-29: 2049 Han
- day-30: 2144 Han
- day-31: 2033 Han
- day-32: 2039 Han
- day-33: 2025 Han
- day-34: 2084 Han
- day-35: 2110 Han

All seven lessons contain substantive original explanation, conditional supplementary derivations, source figure/table interpretation and engineering metrics. No invented device performance data found. Historical scope explicitly stated in day35. Derived count/deadtime/quantization/bandwidth models have assumptions and are not misrepresented as original numbered source equations.

## Citation and formula conclusions

- Eq2 direct-ToF d≈cτ/2, Eq6 phase-to-distance standard deviation, Eq7 range definition, Eq8 SPSD statistical error all match inspected source. Units and dimensional arguments are sound.
- Table1 is used as a qualitative comparison framework rather than copied. PDE footnote accurately distinguishes FF and PDP; short quote `fill factor` appears on p29 with PDF ligature typography.
- Source figure numbers and pages match captions. Day32 distinguishes Gaussian FWHM from long-tail timing response.
- Independent Poisson background subtraction, fixed nonparalyzable dead time, uniform quantization, bias–variance decomposition and event-interface budget are correctly labeled supplementary.

## Defect found and resolution

Day34 raw HTML math contained literal `<` in j<k, which could be parsed as an element and truncate the formula for HTML processors. Root reported repair to j&lt;k. Recheck below confirms matched inline math delimiters and restored complete fragment. No unresolved substantive source/physics defect identified. Integrated mobile/rendering/navigation checks remain root responsibilities.
