# Week07 independent source map

Status: source pre-review; waiting for all seven lesson bodies and citation JSON. This is not course acceptance.

Actual depth PDF anchors read:

- p15 Fig1.1 passive/active reflective measurement taxonomy; p16 RGB-D defined as depth map plus corresponding color.
- pp16–19 pinhole geometry, Eq1.4 K projection p18, Eq1.5 K and Eq1.6 world-to-camera rigid transform p19. Important: this book initially uses real-image negative focal length; virtual-image positive conventions require explicit change.
- p25 Eq1.26 z=bf/d for rectified stereo; Eq1.25 point backprojection.
- pp36–39 active projector/camera triangulation Fig1.11 p36, Fig1.12 p37, Eq1.43–45 p37, rectified Eq1.50 p39.
- p41 Fig1.14 roundtrip and Eq1.51 r=cτ/2; p43 Eq1.55 phase range. Ideal fixed timing precision is not universal distance-independent camera performance because returning photon statistics vary.
- p63 Eq2.6 Δz=z²Δd/(bf), Fig2.8 resolution curves with specified baseline/focal/subpixel assumptions. This is geometric resolution propagation, not complete random error model or universal product curve.
- p65 Eq2.7 SAD matching cost, Eq2.9 uniqueness discussed via second-best non-correct matching cost; do not confuse argmin location with cost value.
- p109 Eq3.45 radial-to-z conversion; Eq3.46 point backprojection. Undistort before using ray coordinates.
- pp127–130 accuracy/precision/resolution distinctions and parametric/nonparametric calibration; Fig4.1 p127, Fig4.2 p130. Source has loose terminology in prose; engineering explanation should keep bias, standard deviation and RMSE distinct.
- p139 Eq4.9 calibrated ray K−1p, planar checkerboard calibration steps; Fig4.8 p140.
- p142 Fig4.10 radial/tangential displacement and Eq4.10 multi-pose summed squared reprojection error. Pixel reprojection residual does not alone prove depth metric accuracy.
- pp152–155 structured-light camera calibration; Eq4.14 reciprocal disparity correction p154, Eq4.15 per-pixel depth offset p155, Fig4.17 plane correction example p155.
- pp156–159 ToF calibration: correlated acquisitions limit simple averaging, amplitude images support checkerboard geometry; radial/photometric corrections distinct from intrinsic geometry. Fig4.18 p157; Fig4.19 p159 checker reflectivity depth artifact.
- pp160–161 joint RGB-D calibration: individual intrinsics/distortion/depth correction then rigid extrinsics, planar geometry, Fig4.20 p161 checkers visible in amplitude but not in depth.
- pp171–176 acquisition/registration: Fig5.2 p172 sensor arrangements; Fig5.4 p174 RGB/depth/amplitude/confidence; Eq5.1 p174 depth-to-color reprojection. Fig5.5 sparse projection and Fig5.6 occlusion p175; p176 z-buffer and point-cloud coloring. Equal image dimensions do not imply equal viewpoint or common ray.
- pp177–179 bilateral filtering: Eq5.2–5 standard bilateral; Eq5.6 p178 and Eq5.7 p179 cross-bilateral depth using COLOR similarity weights. Fig5.7 p179 examples. Do not claim all color edges imply depth discontinuities.

Day43 provisional full read: conceptually sound; authoring remains ongoing. Final independent review will read stable body files and match their actual citation lists.
