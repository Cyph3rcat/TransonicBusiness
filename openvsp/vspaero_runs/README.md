# VSPAERO campaign (2026-08-04) — file map & how to re-run

Toolchain: OpenVSP 3.51.2 / VSPAERO 7.2.2 (repo-local install), Python 3.12 for post-processing.
Full findings are written into `config.md` B.6 + Part D and `doubts.md` #6/#10/#17–#20 — this file is just the map.

## Directory layout (isolation models, coarse → complete)

| Dir | Model | What it isolates |
|---|---|---|
| `01_wing_baseline/` | `wing_v6_baseline.vsp3` — SC(2)-0412 wing, Λ25=13.8° **applied at quarter chord** (fixes the v1–v5 `Sweep_Location` bug, doubts.md #17) | Clean-wing lift curve, span load vs elliptical, e, stall-onset station. `stab/` holds the wing-alone Clβ run. |
| `02_taper_twist/` | 8 auto-generated variants (`tools/gen_sweep.py`) | Taper 0.25–0.45 and twist 0…−4.5° sweeps → doubts.md #6 closure |
| `03_wing_winglet/` | `wing_v6_winglet.vsp3` | Winglet on/off comparison at identical refs |
| `04_fuselage/` | `fuselage_v1.vsp3` | Fuselage loft alone (NOTE: built before the XLocPercent clamping fix; superseded by the fuselages inside 05/06) |
| `05_wingbody/` | `wingbody_v2.vsp3` | Wing+fuselage (unwaisted barrel) — fuselage interference on the wing |
| `06_full/` | `full_v1.vsp3` = **aero model** (unwaisted); `full_v2.vsp3` = **area-ruled geometry model** (waisted; do NOT run VSPAERO on it — doubts.md #20) | Full aircraft: sweep, `stab/` stability run, `wavedrag_*.csv` + `area_dist_v1_v2.png` area-rule comparison, `full_v2_views.png` 3-view |
| `07_full_v3/` | `full_v3.vsp3` — superseded. Real-size nacelles, tapered pylons, first belly fairing, drooped nose, softened waist | **Its drag/L-D and Cnβ figures are retracted** (doubts.md #20, #21). Kept for the geometry history only. Its `.polar` has also been overwritten at non-standard conditions — use `08_full_v4/ref_v3_*/` for any v3 comparison. |
| `08_full_v4/` | `full_v4.vsp3` — superseded. Constant-section barrel (no waist), tangent-blended nose, rebuilt belly fairing | **Cnβ/SM figures retracted — see 09_full_v5.** Kept for the fuselage-un-waisting history. → config.md D.5b/D.5c |
| `09_full_v5/` | `full_v5.vsp3` — superseded. **Its longitudinal figures are retracted**: the file's fuselage tail was left open (`CapUMaxOption = 0`), which corrupts the pitching moment, and GUI edits had silently moved the HT to 62.42 ft² and reworked the belly fairing, so config.md D.5d's SM = 37.7% does not describe the file. Kept for the fuselage-reloft history. Sparse-section (10 XSec) fuselage reloft with a low Phenom-style nose tip and windshield dent, VT grown to 59 ft² + dorsal fin, nacelle raised (gap 0.16D→0.47D), wing moved to a Class-I-CG-solved position | Full aircraft at a real CG (not a placeholder): α sweep (SM), β sweep (**Cnβ resolved, S/N 15.8, now stable**), CG loading table. See its own README. → config.md D.5d, weight.md §3 |
| `10_full_v6/` | `final_alpha/final_alpha.vsp3` — superseded by v7. Empennage right-sized against the *measured* neutral point (S_HT 51.7→34.0, S_VT 59→45 ft²), the user's 7-station fuselage adopted with its open tail closed, and the project's first Raymer parasite-drag buildup / real drag polar. Closes doubts.md #23; opens #24–#26. See its own README. → config.md D.6, weight.md §4 |
| `11_full_v7/` | `final_alpha/final_alpha.vsp3` (α sweep) and `final_beta/final_beta.vsp3` (β sweep, same geometry) — **this is the overall CAD model quoted in the preliminary design report.** S_HT/S_VT trimmed again to 29.10/43.20 ft² off the v6 neutral point; `ht30–ht54` subfolders are the horizontal-tail-area sensitivity sweep behind that trim; `diag_wing159` is a wing-alone diagnostic. Consumed directly by `report/v7_results.py`. |
| `12_su2_v7/` | No `.vsp3` of its own — geometry exported *from* `11_full_v7` into SU2 volume meshes for 3D CFD (VLM can't do transonic). `stage1_wing_winglet/` meshes the wing+winglet alone (`wing_winglet_cfdmesh.stl`/`.msh`); `stage2_wing_fuselage_tail/` adds the fuselage and tail (`stage2_cfdmesh.stl`/`.msh`). `stage3_wing_fuse_nac/` (nacelles added) was started and abandoned — empty. |

## Re-running

Geometry+analysis scripts are self-contained `.vspscript` files; run from *inside the model's directory*:

```
cd <dir>
<repo>\OpenVSP-3.51.2-win64-Python3.13\OpenVSP-3.51.2-win64\vspscript.exe -script build_run.vspscript
```

Post-processing (from `vspaero_runs/`):
```
python tools\vspaero_post.py 01_wing_baseline\wing_v6_baseline --clmax2d 2.11 --cltargets 0.34 0.60 1.27
python tools\compare_sweep.py          # taper/twist summary table
python tools\plot_area_dist.py out.png 06_full\wavedrag_full_v1.csv 08_full_v4\wavedrag_full_v4.csv
python tools\shade_obj.py 08_full_v4\full_v4.obj views.png "full_v4"     # shaded, readable
python tools\render_obj.py 08_full_v4\full_v4.obj views.png              # point cloud, legacy
python tools\long_slopes.py 22.87 5.0236 v4=08_full_v4\full_v4.polar     # CL_a, SM, x_np
python tools\lat_slopes.py v4=08_full_v4\beta\full_v4.polar              # Cn_b, Cl_b, CY_b
python tools\long_slopes.py 19.90 5.0236 v5=09_full_v5\full_v5.polar     # v5, real CG
python tools\lat_slopes.py v5=09_full_v5\beta\full_v5.polar              # v5, Cn_b now +0.143/rad, S/N 15.8
```

Stability runs are done by copying the `.vspgeom` **and `.vkey`** + editing the `.vspaero` file (single AoA, `VSP_StabilityType = 1`) and calling `vspaero.exe -omp 6 -stab <basename>` — see `01_wing_baseline/stab/` and `06_full/stab/`.

⚠️ **`-stab` derivatives are not reliable for the full configuration** (doubts.md #21). It differences over 0.01°, which for this model puts ΔCMz two orders of magnitude *below* the solve's own β=0 symmetry error. Get Cnβ/Clβ/CYβ from a real β sweep (`08_full_v4/run_beta.vspscript` + `tools/lat_slopes.py`, which prints the signal-to-noise) and CL_α/SM from the α sweep (`tools/long_slopes.py`). The `-stab` route remains fine for the isolated wing, whose signals are far larger.

## OpenVSP scripting gotchas discovered this session (cost real debugging time)

1. **`Sweep_Location` defaults to 0 (LE)** — always set it to 0.25 when the sweep figure is a quarter-chord number.
2. **`InsertXSec` resets the shared boundary XSec chord to 1.0** — set section params per-section with `Update()` between, then re-set boundary tip chords in a fix-up pass afterward.
3. **Fuselage `XLocPercent` is limit-clamped against neighbors' current positions** — a single assignment pass silently loses stations; loop the assignments in alternating ascending/descending passes with `Update()` after each set until converged (see `06_full/build_full_v2.vspscript`).
4. **Mixed thick/thin runs**: put bodies in one user set (`GeomSet`), lifting surfaces in another (`ThinGeomSet`). Wings default-shown as thin camber surfaces; leaving the fuselage in the thin set garbage-ifies it.
5. **Airfoil file paths are cwd-relative and fail silently into a default section** (planform verification won't catch it) — check for `ReadFileAirfoil` errors in the console output every time.
6. **An unclosed body silently corrupts the solve — it does not just add drag.** A FUSELAGE geom whose end XSec has a finite diameter and `CapUMaxOption = 0` is left *open*. VSPAERO's mixed panel/VLM still converges and still prints plausible forces, but the pitching moment goes non-monotone and the static margin comes out wrong by a factor of ~3 (found in `09_full_v5`, 2026-08-07). Check `CapUMinOption`/`CapUMaxOption` on every body, and check that CMy vs α is linear (R² > 0.99) before trusting any stability number.
7. **A GUI-edited `.vsp3` drifts from its build script and nothing warns you.** `full_v5.vsp3` carried three undocumented changes vs `build_full_v5.vspscript` (HT area 51.68 → 62.42 ft², belly fairing length and position, fuselage reloft) — so a documented result no longer described the file. Parse the `.vsp3` and diff planform areas + end-cap options against the script before trusting a published figure.
8. **More fuselage cross-sections make the loft WORSE, not better** (found in `09_full_v5`, cost most of a session). The skinning spline treats every XSec as a hard interpolation knot; densely stacking stations sampled off an analytic curve (tried 16/28/36/46) produces visible rippling, worst at the nose/tail caps where curvature is highest. Fix: use the fewest XSecs that capture actual curvature changes (10 sufficed for the whole fuselage) and let the spline fair the surface between them. Verify with `09_full_v5/ripple_metric.py` (mesh-vs-analytic residual) rather than judging by eye.

## Fidelity caveats (also in config.md B.6/D.5)

VLM at M0.30 with Prandtl-Glauert: valid for induced drag, span loading, lift-curve, stability derivatives, stall *onset* (linear local-cl vs 2-D clmax). NOT valid for: absolute CLmax, transonic anything, friction/parasite drag beyond a crude estimate, panel-body drag (leaves residuals — compare configurations, not absolute body drag). The M0.80 story rests on the SU2 2-D work (config.md B.5.3) + sweep theory + the area-rule slicing here.
