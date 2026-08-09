# Transonic Business Jet: Conceptual Design

Hi there, this is a list of all the tools I used to create the ubiquitous amt. of graphs in the report. 
it also contains the .vsp file for the plane (which can be exported as a STEP file and CAD component by component)

it also has the mesh that I used, as well as the gmsh script I used to mesh the file. 

It also lists all the .dat files for all the airfoils I evaluated in the report. 
is anyone even reading this :B 


## The CAD model

The overall aircraft geometry is an OpenVSP `.vsp3` file:

**[`openvsp/vspaero_runs/11_full_v7/final_alpha/final_alpha.vsp3`](openvsp/vspaero_runs/11_full_v7/final_alpha/final_alpha.vsp3)**

This is the final configuration quoted in the preliminary design report: wing,
fuselage, empennage, nacelles, and pylons together, with the empennage sized
off this model's own solved neutral point. `final_beta.vsp3` in the same
campaign is the identical geometry re-run for a sideslip sweep (stability
derivatives instead of the alpha polar).

Everything upstream of it is design history, not alternatives: `openvsp/archive/`
holds the earliest wing-only iterations (v1-v5), and `openvsp/vspaero_runs/`
holds the full-aircraft campaign, 12 numbered run folders, coarse isolation
models up through the final configuration, several of them explicitly
**superseded/retracted** along the way (bad fuselage caps, GUI drift from the
build script, non-converged sweeps; the mistakes are kept, not hidden). See
**[`openvsp/vspaero_runs/README.md`](openvsp/vspaero_runs/README.md)** for the
full run-by-run map and what went wrong in each.

## SU2 CFD meshes

VSPAERO is a vortex-lattice/panel code, so it can't resolve shocks: anything
transonic (the whole point of an M0.80 cruise aircraft) goes through SU2
instead. Meshing for both studies below was done in **gmsh** (scripted via its
Python API, not the GUI), then written out in SU2's native `.su2` format.

**The mesh files themselves, if you want to tortue them aerodynamically!poke at them directly:**
`airfoils/su2_screen/naca64209.su2` and `airfoils/su2_screen/sc0410.su2` (2D
sections), and
`openvsp/vspaero_runs/12_su2_v7/stage1_wing_winglet/wing_winglet_cfdmesh.msh` /
`openvsp/vspaero_runs/12_su2_v7/stage2_wing_fuselage_tail/stage2_cfdmesh.msh`
(3D staged buildup). All four are gmsh output, readable in gmsh itself or any
SU2/CFD viewer. The gmsh scripts that built them are called out per-mesh
below.

- **2D airfoil screening**: `airfoils/su2_screen/naca64209.su2` and
  `airfoils/su2_screen/sc0410.su2`, ~68,000-cell hybrid C-grids (gmsh
  BoundaryLayer field, y+≈1, farfield radius 25c) used to pick the wing
  section by running shock-capturing RANS at M0.80 on 2D cuts. Meshes are
  built by `airfoils/su2_screen/make_mesh.py`; `gen_configs.py` writes the
  matching SU2 `.cfg` files and `parse_results.py` pulls Cl/Cd/residuals back
  out of the solver logs. Methodology and results in
  `airfoils/su2_screen/README.md`.
- **3D staged buildup**, exported from the `11_full_v7` OpenVSP model:
  - `openvsp/vspaero_runs/12_su2_v7/stage1_wing_winglet/wing_winglet_cfdmesh.stl` /
    `.msh`: wing + winglet alone, meshed by
    `stage1_wing_winglet/make_mesh.py`.
  - `openvsp/vspaero_runs/12_su2_v7/stage2_wing_fuselage_tail/stage2_cfdmesh.stl` /
    `.msh`: wing + fuselage + tail added, meshed by
    `stage2_wing_fuselage_tail/make_mesh_stage2.py`.
  - `stage3_wing_fuse_nac/` (nacelles added) was started and not completed.

## Repository layout

| Path | Contents |
|---|---|
| `openvsp/` | OpenVSP models and VSPAERO runs, see **The CAD model** above. `schrenk_washout.py` is the Schrenk's-method span-loading check used to set wing twist. |
| `airfoils/` | Airfoil selection and transonic screening. See **Airfoils** below. |
| `report/` | The scripts and data behind the preliminary design report. Each top-level script computes one chapter's numbers and dumps a matching `.json` so the figures and text can't drift from each other: `class2_weights.py` (Ch.8 Class-II weights and CG envelope), `landing_gear.py` (Ch.7 gear design), `performance.py` (Ch.10 performance, FAR 25 climb/field-length checks), `economics.py` (Ch.11 DAPCA IV pricing), `v7_results.py` (consolidates the full_v7 VSPAERO output into report-ready numbers). `report/figs/` regenerates every plot in `report/figures/`: `ch1_3.py`, `ch5_6.py`, `ch7_10.py`, and `ch11.py` each build the figures for their chapter range from the JSON above, `threeview.py` draws the general-arrangement three-view from the same geometry fed to OpenVSP, `common.py` holds the shared plot style/palette/data readers, `insert_figures.py` drops the generated images into the report HTML, and `run_all.py` runs the whole set in one pass. |
| `refs/` | Condensed notes distilled from the design references (Raymer chapters, course lecture slides, NASA/journal/certification documents). These are this project's own summaries, not the source material; the underlying PDFs and slide decks aren't republished here. |
| `fuselage/fuselage.md` | Fuselage lofting notes (station layout, area distribution). |
| `tools/` | Utility scripts used to convert reference PDFs/slides into the markdown under `refs/`. |

## Airfoils

- **`airfoils/dat/`**: raw candidate airfoil coordinates as sourced, the
  NASA SC(2) supercritical family (`sc20410`, `sc20412`, `sc20414`, `sc20606`,
  `sc20610`) and NACA 64-209 as the conventional-section baseline.
- **`airfoils/dat_clean/`**: the same sections re-ordered into single-loop
  Selig format (required by the panel/CFD tooling; the raw NASA files aren't
  in that order).
- **`airfoils/critical_cp.py`**, **`critical_mach_pg.py`**: Prandtl-Glauert +
  critical-Cp estimate of each section's critical Mach number, used for the
  first-pass sweep-angle screen (Korn equation).
- **`airfoils/evaluate_transonic.py`**: compares the Prandtl-Glauert estimate
  against the SU2 CFD sweep results. **`plot_cd_vs_mach.py`** and
  **`plot_sc20412_results.py`** generate the drag-divergence and Mach-sweep
  comparison graphs from those results.
- **`airfoils/su2_screen/`**: the SU2 2D transonic screen itself (meshes,
  configs, solver logs, and the round-by-round comparison that picked
  SC(2)-0410 over NACA 64-209). See its `README.md`.

**Result of the screen:** SC(2)-0410 was selected for the wing (lower wave
drag, less sweep required at M0.80); the thicker SC(2)-0412/0414 members were
carried forward later for wing fuel volume.

## Plots

Every plot quoted in the report lives as a rendered PNG in
**[`report/figures/`](report/figures/)** (25 figures, `fig_0_0_...` through
`fig_11_1_...`, numbered by report chapter/section). None of them are
hand-drawn: each one is built by matplotlib from a solver output file (SU2
CSVs, VSPAERO `.lod`/`.polar`/`.stab` files) or from the same JSON the report
text quotes, via the scripts in `report/figs/` (see **Repository layout**
above). That's also why the plots can't silently drift out of sync with the
numbers in the text: re-run `report/figs/run_all.py` and every figure in
`report/figures/` regenerates from the current data. Shared styling (colors,
fonts, line weights) lives in one place, `report/figs/common.py`, so all 25
look like they came from the same document instead of 25 different sessions.

## Toolchain

- **OpenVSP 3.51.2** + VSPAERO 7.2.2: geometry and vortex-lattice aerodynamics.
- **SU2 v8.5.0** (SST turbulence model): shock-capturing RANS for transonic sections and staged 3D meshes. opensource CFD by Stanford
- **gmsh**: scripted mesh generation (Python API) for both SU2 studies, see **SU2 CFD meshes** above.
- **Python 3.12**: post-processing, plotting, and the report figure/data pipeline (numpy, matplotlib; see individual scripts for exact imports).


