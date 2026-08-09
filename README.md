# Transonic Business Jet — Conceptual Design

Conceptual/preliminary design of a twin-engine, over-the-wing-engine-mount (OTWEM)
business jet cruising at M0.80. Work follows Raymer/Sadraey-style conceptual
design methodology: Class-I/Class-II weight estimation, wing and airfoil
selection, empennage sizing against a solved neutral point, and aerodynamic
verification with OpenVSP (VSPAERO, vortex-lattice) and SU2 (RANS CFD).

## The CAD model

The overall aircraft geometry is an OpenVSP `.vsp3` file:

**[`openvsp/vspaero_runs/11_full_v7/final_alpha/final_alpha.vsp3`](openvsp/vspaero_runs/11_full_v7/final_alpha/final_alpha.vsp3)**

This is the final configuration quoted in the preliminary design report — wing,
fuselage, empennage, nacelles, and pylons together, with the empennage sized
off this model's own solved neutral point. `final_beta.vsp3` in the same
campaign is the identical geometry re-run for a sideslip sweep (stability
derivatives instead of the alpha polar).

Everything upstream of it is design history, not alternatives: `openvsp/archive/`
holds the earliest wing-only iterations (v1–v5), and `openvsp/vspaero_runs/`
holds the full-aircraft campaign — 12 numbered run folders, coarse isolation
models up through the final configuration, several of them explicitly
**superseded/retracted** along the way (bad fuselage caps, GUI drift from the
build script, non-converged sweeps — the mistakes are kept, not hidden). See
**[`openvsp/vspaero_runs/README.md`](openvsp/vspaero_runs/README.md)** for the
full run-by-run map and what went wrong in each.

## SU2 CFD meshes

VSPAERO is a vortex-lattice/panel code — it can't resolve shocks, so anything
transonic (the whole point of an M0.80 cruise aircraft) goes through SU2
instead. Two separate SU2 studies, at two different scopes:

- **2D airfoil screening** — `airfoils/su2_screen/naca64209.su2` and
  `airfoils/su2_screen/sc0410.su2`, ~68,000-cell hybrid C-grids (gmsh
  boundary-layer field, y+≈1, farfield radius 25c) used to pick the wing
  section by running shock-capturing RANS at M0.80 on 2D cuts. Methodology
  and results in `airfoils/su2_screen/README.md`.
- **3D staged buildup**, exported from the `11_full_v7` OpenVSP model:
  - `openvsp/vspaero_runs/12_su2_v7/stage1_wing_winglet/wing_winglet_cfdmesh.stl` /
    `.msh` — wing + winglet alone.
  - `openvsp/vspaero_runs/12_su2_v7/stage2_wing_fuselage_tail/stage2_cfdmesh.stl` /
    `.msh` — wing + fuselage + tail added.
  - `stage3_wing_fuse_nac/` (nacelles added) was started and not completed.

## Repository layout

| Path | Contents |
|---|---|
| `openvsp/` | OpenVSP models and VSPAERO runs — see **The CAD model** above. `schrenk_washout.py` is the Schrenk's-method span-loading check used to set wing twist. |
| `airfoils/` | Airfoil selection and transonic screening. See **Airfoils** below. |
| `report/` | The scripts and data behind the preliminary design report: `report/figs/` regenerates every plot in `report/figures/`; `class2_weights.py`, `landing_gear.py`, `performance.py`, `v7_results.py` compute the numbers (each dumps a matching `.json`). The compiled report document itself is not included in this repository. |
| `refs/` | Condensed notes distilled from the design references (Raymer chapters, course lecture slides, NASA/journal/certification documents). These are this project's own summaries, not the source material — the underlying PDFs and slide decks aren't republished here. |
| `fuselage/fuselage.md` | Fuselage lofting notes (station layout, area distribution). |
| `tools/` | Utility scripts used to convert reference PDFs/slides into the markdown under `refs/`. |

Not included: the OpenVSP and flow5 program installers (multi-hundred-MB
third-party binaries — download them directly from
[openvsp.org](http://openvsp.org) and [flow5.tech](https://flow5.tech) instead),
personal working notes, and the reference-literature PDFs (copyright).

## Airfoils

- **`airfoils/dat/`** — raw candidate airfoil coordinates as sourced: the
  NASA SC(2) supercritical family (`sc20410`, `sc20412`, `sc20414`, `sc20606`,
  `sc20610`) and NACA 64-209 as the conventional-section baseline.
- **`airfoils/dat_clean/`** — the same sections re-ordered into single-loop
  Selig format (required by the panel/CFD tooling; the raw NASA files aren't
  in that order).
- **`airfoils/critical_cp.py`**, **`critical_mach_pg.py`** — Prandtl-Glauert +
  critical-Cp estimate of each section's critical Mach number, used for the
  first-pass sweep-angle screen (Korn equation).
- **`airfoils/evaluate_transonic.py`**, **`plot_cd_vs_mach.py`**,
  **`plot_sc20412_results.py`** — compare the Prandtl-Glauert estimate against
  the SU2 CFD sweep results.
- **`airfoils/su2_screen/`** — the SU2 2D transonic screen itself (meshes,
  configs, solver logs, and the round-by-round comparison that picked
  SC(2)-0410 over NACA 64-209). See its `README.md`.

**Result of the screen:** SC(2)-0410 was selected for the wing (lower wave
drag, less sweep required at M0.80); the thicker SC(2)-0412/0414 members were
carried forward later for wing fuel volume.

## Toolchain

- **OpenVSP 3.51.2** + VSPAERO 7.2.2 — geometry and vortex-lattice aerodynamics.
- **SU2 v8.5.0** (SST turbulence model) — shock-capturing RANS for transonic sections and staged 3D meshes.
- **Python 3.12** — post-processing, plotting, and the report figure/data pipeline (numpy, matplotlib; see individual scripts for exact imports).
