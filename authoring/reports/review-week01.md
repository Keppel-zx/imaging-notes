# Independent review: week 01

Reviewer: week05 agent. Read full lesson fragments day01–07 plus week01 citation JSON. Read actual source extracts: EMVA pp5–8,16–18,31–32; Benchmark pp104–115; Photon Transfer p9. Rechecked key source identifiers, formulas and units against these pages. This is a content review; browser/mobile QA remains root responsibility.

## Result

No blocking physics or source-identity error found in the seven lesson bodies. Review-ready subject to minor index/scope corrections below. Each lesson contains substantial original engineering explanation and is within 2000–3000 Han characters excluding reference section: day1 2157, day2 2145, day3 2035, day4 2105, day5 2034, day6 2088, day7 2134.

## Checks passed

- EMVA Eq1 QE includes whole pixel area, fill factor and microlenses (p5); Eq2 incident photons and Eq5 mean digital response (pp5–6) correctly interpreted.
- K consistently DN/e−; inverse G is e−/DN. PTC variance slope K versus response slope Kη correctly distinguished. Eq9 p6 correctly transcribed.
- Input-noise conversion subtracts quantization in variance domain; low-output-noise caveat matches p17 Eq31–32.
- Dark current Eq19–21 p8 and independent-noise variance sums correctly discussed. Source background subtraction does not remove shot noise.
- Eq11 SNR p7, its exact SNR=1 root, Eq18 DR p8, dB/bits conversion and Eq33 maximum SNR p18 correctly interpreted.
- Benchmark Fig4.19 p104 Bayer, Fig4.21 p107 arbitrary-unit noise regimes, Fig4.22 p109 SNR regimes, Fig4.23 p114 black-level color errors all match their source identity and the discussion does not fabricate data.
- EMVA Fig5 p16 and Fig6 p17 correctly distinguished; Fig7 p18 correctly separates temporal/total/ideal SNR. Author explicitly identifies example curves as simulated (p12).
- EMVA Table2 p32 and basic-information table p31 correctly support the datasheet lesson. Photon Transfer Table1.1 and “absolute units” wording verified p9.

## Minor actionable corrections

1. Citation JSON day1 benchmark record has §4.3.3–4.4.1 and pages104,112–115, but body added an end-paragraph citation to benchmark pp105–107; add pp105–107 to that record.
2. Day3 source body explicitly displays EMVA Eq1–2 incident photons/QE in addition to Eq5 and Eq9, but the JSON formulas omit Eq1–2. Add named records at p5. Day7 photon-input records already include them.
3. Day1 has supplementary color-matrix offset propagation M b not indexed as a formula; day3 quantization input variance 1/(12K²), day5 exact threshold root, and day6 reciprocal/noise conversion and DR log forms should be explicitly named if the global index is meant to enumerate all displayed relations. The current generic umbrella labels are comprehensible but less precise than requested.
4. Day4 JSON lists Benchmark Eq4.9 as if transcribed, while the body discusses its Poisson consequence without displaying its probability mass function; either mark as a source relation consulted or remove this extra item from displayed-formula index.
5. Optional prose precision: day7 “当N最大时，处于光子散粒噪声区” can be tightened to “当N远大于其余方差项时”. Existing context makes the intended comparison clear, but “最大” alone can sound like maximum exposure rather than dominance within the variance sum.

No author files edited; root retains integration ownership.
