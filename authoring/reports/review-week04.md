# Independent review: week 04

Reviewed full bodies day22–28 and citations/week-04.json against actual PDF extracts. Sources read: Benchmark pp50–54,140,143,150,209,211–212,220–221,229–233,255–259 plus cited adjacent context; Colour pp57–59,61,64. Rendered and visually checked complex formulas Benchmark p230 and p256, Colour p57. No author-file edits made.

## Result

Content review passed with no blocking formula, physics, figure identity, or source page error found. Han counts excluding reference section: 22=2422, 23=2213, 24=2212, 25=2182, 26=2241, 27=2314, 28=2170. Full explanatory bodies rather than short outlines. Original versus supplementary explanation and formulas clearly separated. Browser/mobile/navigation checks remain root responsibility.

## Formula checks

- Day23 LSF is PSF integrated over transverse coordinate (6.27 p211); MTF is absolute LSF Fourier transform (6.32 p212); normalized DC response (6.33); ESF derivative (6.46 p220). Frequency-unit conversion is correct. Small omission: displayed integrals use implicit all-space limits; text and normalization context make meaning clear, but explicit −∞ to ∞ limits would improve precision.
- Day24 row-vector covariance C′=MᵀDCDM exactly matches source 6.63 p230; column-vector alternative AC Aᵀ correctly distinguished. This avoids a common transpose error. Nonlinear OECF input-equivalent SNR (6.66 p233) correctly interpreted and assumptions given.
- Day25 Lab δ=6/29 constants exactly equivalent to source 24/116, 841/108 and 16/116. Eq2.6 p57–58 and ΔE Eq2.13 p59 correct. CIEDE2000 Eq2.20 is explicitly only a structural reference, not falsely claimed as fully transcribed.
- Day26 dynamic range log conversion and local noise propagation correct; file bit depth not conflated with physical input range.
- Day27 Weber Eq5.1 and Fechner relation Eq5.2–5.3 p140 correctly applied as stimulus-dependent rather than camera total-score formulas.
- Day28 edge acutance Eq7.8 and luminance CSF Eq7.9 p256 visually verified; infinite denominator, shared cycles/degree coordinates, cutoff and viewing-distance conversion all correct.

## Figure/source checks

- Fig2.1 p54: same manipulations at two sizes correctly illustrates global/local attribute visibility.
- Fig6.16 p209: sharpness versus fine-detail resolution correctly distinguished. Fig6.27 p221: row sampling, ESF oversampling, differentiation and SFR flow correctly described.
- Fig6.30 p231 CCM noise appearance, Fig6.31 p232 equal variance / different spectra / ACF, Fig6.32 p233 local slope effects correctly identified. Author appropriately qualifies the source's overly broad CCM-noise-amplification prose using the full covariance formula.
- Colour Fig2.2 p61 Luo/Rigg discrimination ellipses identity and interpretation correct.
- Fig7.6–7.7 p257 screen/print conditions and Fig7.8 p259 JND mapping correctly interpreted without treating the relative-scale anchor as a universal ratio scale.

## Nonblocking index refinements

1. Day23 prose cites Eq6.25 p210 but JSON does not enumerate it; add if index aims to cover all explicit equation references. Integral limits could be made explicit as above.
2. Day24 JSON includes source Eq6.65 noise power spectrum as consulted background; body explains it conceptually but does not display formula. Either label index record as consulted (rather than displayed) or show its formula if necessary. This is an index-semantic issue, not invented source content.
3. Day28 printed pages are PDF255–264 → printed234–243, correctly stated. Benchmark has chapter-dependent page offsets, so do not impose a single global PDF-to-print offset during integration.

## Review scope

No original illustrations copied. English quotations are short (week total Benchmark3 words; Colour2 words). All seven satisfy authoring depth and source-grounding requirements on content review. HTML formula rendering and phone viewport still need integrated QA.
