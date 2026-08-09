# 08_full_v4 — fuselage "plastic surgery" pass (2026-08-05)

Working model for the whole aircraft. Supersedes `07_full_v3`. Write-up: **config.md D.5b / D.5c**.

Brief: make the fuselage resemble a Phenom 300 (cylindrical barrel, round nose cap, body that blends),
drop the area-rule obsession and keep `A(x)` only as a gauge. **Pylons and the dorsal fin were
deliberately left alone** — the user is doing those by hand; recommended values are in config.md D.5c.

## What changed vs v3

| | v3 | v4 |
|---|---|---|
| Nose profile | `r/R = (x/Lnc)^0.6` — slope 0.176 at the barrel, i.e. a tangency break | `r/R = sin[(π/2)(x/Lnc)^0.7]` — round tip, **exactly tangent** at the barrel |
| Nose droop | −0.85 ft, kinked at the barrel | −0.60 ft, `−0.60(1−x/Lnc)²`, tangent |
| Barrel | waisted 6.10 → 5.05 starting at x=17, i.e. 6.6 ft *into* the cabin | **constant 6.10 ft, x = 10.4 → 23.4** (= the whole cabin) |
| Aft top line | dipped to 2.53 @ x=26, rose to 3.00 @ x=38 (the "crooked" S-bend) | monotone 3.05 → 1.98; all taper on the lower line, 15.0° mean upsweep |
| Belly fairing | 10.5 × 5.8 × 1.3 ft, *narrower* than the fuselage, 0.30 ft protrusion — a blister | 14.5 × 7.00 × 3.20 ft, **wider** than the barrel, rounded-rect section, 0.75 ft protrusion |
| Wing / winglet / nacelles / pylons / tails | — | **identical** |

## Results

- **Area rule**: M1.0 metric 1.53 → **1.49** (D/q, ft²) with **+17% volume**. Un-waisting cost nothing.
  The A(x) crest is wing+nacelle+fairing, not the barrel. → doubts.md #10 closed.
- **Induced drag**: v3 reported CD_i = 0.0158 *at zero lift* (impossible). v4 → **0.0021**. The v3 fairing
  was too small to shield the wing-root junction; v3's drag/L-D numbers are **retracted**. → doubts.md #20.
- **Cn_β**: `vspaero -stab` cannot resolve it here (0.01° FD on a signal 100× below the solve's own
  symmetry noise). Real β sweep: v3 = +0.023, v4 = −0.014 /rad. **Fin is undersized** — target
  c_VT ≈ 0.085 → S_VT ≈ 59 ft² (+50%). → doubts.md #21.
- **SM** (from the α sweep fit, not `-stab`): 21.9% → **20.0%**, NP 23.97 → 23.88 ft.

## Files

Build / export
- `build_full_v4.vspscript` — the loft. Station tables are echoed to stdout on every run.
- `export_obj.vspscript`, `export_body_only.vspscript` — OBJ for rendering (`body_only` = fuselage +
  fairing only, for judging the body without the wing/nacelles on top of it)

Analysis
- `run_aero.vspscript` — α sweep 0–8°, M0.30, Re 8e6, Xcg 22.87 (identical to the v3 script)
- `run_beta.vspscript` — β sweep 0/2/4/6° at α=3.7°, the honest way to get Cn_β
- `run_wavedrag.vspscript` — M1.0, 60 slices, 16 rot sects
- `stab/` — `vspaero -stab` run, kept only as the *evidence* for doubts.md #21. **Do not quote its
  derivatives.** To reproduce: copy `full_v4.vspgeom` + `.vkey`, set `AoA` to a single value and
  `VSP_StabilityType = 1` in the `.vspaero`, run `vspaero -stab -omp 6 <base>`.
- `ref_v3_alpha/`, `ref_v3_beta/` — full_v3 re-run under *identical* settings. Needed because
  `07_full_v3/full_v3.polar` had been overwritten at different conditions (M=0, Re=10e6, α=0/5/10),
  so it could not be compared to directly.

Plots
- `full_v4_shaded.png`, `v3_shaded.png` — before/after, 4 views
- `body_only_shaded.png` — fuselage + fairing alone
- `outline_v3_v4.png` (`plot_outline_v3_v4.py`) — side + plan outline overlay, the clearest diagnostic
- `area_dist_v3_v4.png` — A(x) vs Sears-Haack
- `full_v4_post.png` — span load / section cl / induced polar

## Tools added this pass (`../tools/`)

- `shade_obj.py` — depth-sorted Lambert-shaded OBJ render. The old `render_obj.py` point cloud cannot
  show whether a loft *looks* right, which is the whole question here.
- `lat_slopes.py` — Cn_β / Cl_β / CY_β by least squares over a real β sweep, and it prints the
  signal-to-noise against the β=0 symmetry error so a non-resolved derivative is visible as such.
- `long_slopes.py` — CL_α, dCM/dCL, SM, x_np from the α sweep. Use in preference to `-stab`.
