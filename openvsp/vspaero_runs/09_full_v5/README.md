# 09_full_v5 — fuselage reloft + CG-solved stability pass (2026-08-05)

Working model for the whole aircraft. Supersedes `08_full_v4`. Write-up: **config.md D.5d**, CG chapter: **weight.md §3**.

Brief (user, 2026-08-05): the v4 fuselage was jagged at the nose cap, tail cap and belly; the nose
read as an airliner (on-axis tip) instead of a Phenom-style nose tapering to a low tip. Also: justify
or drop the dorsal fin, assess the pylon, and run a real stability analysis at a computed CG instead
of the D.1 placeholder.

## The headline finding: fewer XSecs, not more

Three failed attempts (16 → 28 → 36 → 46 fuselage stations, densely sampled off the analytic nose/tail
laws in `design_lines.py`) all made the loft *more* rippled, not less — up to 0.21 ft of scallop between
stations (`ripple_metric.py`, mesh-vs-analytic residual), worst exactly at the nose and tail caps. OpenVSP's
skinning spline treats every XSec as a hard interpolation knot; stacking stations transfers every small
table inconsistency into a visible ring. **The fix was 10 sections total** — one per actual curvature
event (nose tip, cap rounding, mid-nose, windshield dent, barrel×3, tail cone×2, tail tip) — letting the
spline fair the surface between them. Same principle applied to the belly fairing (8 → 5 sections).

## What changed vs v4

| | v4 | v5 |
|---|---|---|
| Nose tip | z=−0.60, read as axial/"Airbus" | **z=−1.30**, low tapered tip |
| Fuselage sections | 18 | **10**, sparse |
| Windshield | none (body of revolution) | **canopy dent** at x=8.2 (top line pulled 0.27 ft below fair) |
| Belly fairing sections | 8 | 5, same envelope |
| Nacelle Z | +0.1 | **+1.0** (gap 0.16D → **0.47D**, per D.5c choking flag) |
| Pylon | span 1.5, default t/c | span 3.2 (reaches raised nacelle), t/c 9%, Sweep_Location=0 |
| Vertical tail | 39.65 ft² | **59.0 ft²** (1.22× scale), c_VT ≈ 0.085 |
| Dorsal fin | none | **added**, D.5c recipe (76° LE sweep, sharp t/c 5%) |
| Wing root LE | x=19.0 (eyeball) | **x=15.9** (Class-I CG solve, weight.md §3) |
| CG | placeholder, quarter-MAC x=22.87 | **computed**, MTOW x=19.90 (27.6% MAC) |

## Results

- **Fuselage**: smooth by inspection and by the ripple metric (max residual near render-invisible).
  See `zoom_check.png` (nose/tail/belly close-ups + mesh-vs-analytic scatter).
- **Wing-to-nacelle gap**: 1.37 ft = 0.47 × nacelle diameter, matching the D.5c target exactly.
- **Cnβ**: v4 = −0.014/rad (unstable, S/N 4–6, unresolved) → v5 = **+0.143/rad (stable, S/N 15.8)**.
  Fin growth + dorsal fin fixed it, and it's now a real number, not noise. doubts.md #19/#21 closed.
- **SM**: v4 20.0% → v5 **37.7% MAC** — a new finding, not a target. Growing the tail (yaw fix) and
  moving the wing forward (CG fix) both push static margin the same direction; the aircraft is now
  safely but wastefully over-stable. See doubts.md #23. Not blocking, flagged for the next iteration.
- **CL_α**: 4.823 → 4.698/rad. **NP**: x=23.88 → 21.79 ft (wing moved forward faster than the bigger
  tail moved it back).

## Files

Build / export
- `design_lines.py` — designs and checks the analytic nose/tail-cone lines (tangency at the barrel,
  upsweep angle) before committing station values to the vspscript. Also emits `profile_v5.png`.
- `build_full_v5.vspscript` — the loft. Station tables and realized dimensions echoed to stdout.
- `export_obj.vspscript`, `export_body_only.vspscript` — OBJ export for rendering.

Diagnostics (the actual debugging tools from this pass)
- `ripple_metric.py` — extracts the fuselage centerline from an OBJ, compares to the analytic design
  curve, and reports max residual + a second-difference "ripple" number. This is what caught the
  16/28/36-station failures and confirmed the 10-station fix.
- `zoom_check.py` — shaded close-ups of the nose, tail cap, and belly regions, plus the raw mesh
  centerline scatter (ripples show as scatter off a smooth curve, not just as shading artifacts).
- `tune_tail.py` — parameter scan for the tail-cone height/centerline law against the upsweep-angle
  and top-line-monotonicity constraints.

Weights / CG
- `weights_cg.py` — Class-I group-weight buildup, solves for the wing position that gives a sane
  MTOW CG, prints the full loading table. Backing detail for weight.md §3.

Analysis
- `run_aero.vspscript` — α sweep 0–8°, M0.30, Re 8e6, Xcg=19.90 (Class-I MTOW CG, not v4's placeholder)
- `beta/run_beta.vspscript` — β sweep 0/2/4/6° at α=3.7°, same Xcg. Run from inside `beta/` (its own
  copy of `full_v5.vsp3`) since the β sweep would overwrite the α polar otherwise.

Plots
- `full_v5_shaded.png` — 4-view shaded render, current configuration
- `body_only_shaded.png` — fuselage + fairing alone
- `zoom_check.png` — smoothness diagnostic (see Diagnostics above)
- `full_v5_post.png` — span load / section cl / induced polar (`../tools/vspaero_post.py`)

## Re-running

```
cd 09_full_v5
..\..\..\OpenVSP-3.51.2-win64-Python3.13\OpenVSP-3.51.2-win64\vspscript.exe -script build_full_v5.vspscript
..\..\..\OpenVSP-3.51.2-win64-Python3.13\OpenVSP-3.51.2-win64\vspscript.exe -script run_aero.vspscript
python ..\tools\long_slopes.py 19.90 5.0236 v5=full_v5.polar

cd beta
..\..\..\..\OpenVSP-3.51.2-win64-Python3.13\OpenVSP-3.51.2-win64\vspscript.exe -script run_beta.vspscript
python ..\..\tools\lat_slopes.py v5=full_v5.polar
```

## Fidelity caveats

Same as `08_full_v4` and inherited project-wide (see the parent README's Fidelity caveats section):
VLM at M0.30 is valid for induced drag, span loading, lift curve, and stability derivatives at *this*
Mach — not for absolute CLmax, transonic behavior, or friction/parasite drag beyond a crude estimate.
The pitching-moment increment from raising the nacelle/thrust line was absorbed into the CG-based
α-sweep result, not isolated as a separate number — a future pass could difference it out explicitly.
