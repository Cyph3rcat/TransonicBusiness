# SU2 environment — where it actually lives

Repeatedly re-discovering this via `wsl -d ... -e bash -lc "find / ..."` wastes a lot of time. Read this file first.

## SU2 is NOT on Windows, and NOT in the default WSL distro

- `SU2_CFD.exe` is **not** installed anywhere on the Windows side (checked PATH, Program Files, pip, conda — nothing).
- WSL has multiple distros installed (`wsl -l -v` to list). The **default** distro is `archlinux` — SU2 is **not** there either.
- SU2 is installed inside the **`Ubuntu`** distro specifically. Every WSL command touching SU2 must explicitly target it:
  ```
  wsl -d Ubuntu -e bash -lc "..."
  ```
  Omitting `-d Ubuntu` silently runs in `archlinux` instead, where none of this exists, and looks like "SU2 isn't installed" — it just means you're in the wrong distro.

## Install locations (inside the Ubuntu distro)

- SU2 binaries: `/home/cyph3r/mses_replacement/su2/bin/` — `SU2_CFD`, `SU2_DEF`, `SU2_DOT`, `SU2_GEO`, `SU2_SOL` (statically-linked ELF executables, SU2 v8.5.0 "Harrier"). No `SU2_CFD.exe` — this is Linux-only, run through WSL.
- Mesh-generation Python env (`gmsh`, `meshio` — **not** in system `python3`, needs this venv): `/home/cyph3r/mses_replacement/venv/bin/python3`
- `make_mesh.py` (gmsh-based O-grid mesh generator, copied from this repo's `airfoils/su2_screen/make_mesh.py`): `/home/cyph3r/mses_replacement/make_mesh.py`
- Working directories used this session:
  - `/home/cyph3r/mses_replacement/` — original SC(2)-0410 vs NACA 64-209 screen (fixed M0.80, 3 AoA each)
  - `/home/cyph3r/mses_replacement/mach_sweep/` — SC(2)-0412 adaptive Mach-sweep work (this session's `adaptive_sweep.py`, meshes, configs, logs)
  - `/home/cyph3r/mses_replacement/mach_sweep/old_fixed_grid_attempt/` — abandoned 14-run fixed-grid attempt (both candidates, superseded by the adaptive single-candidate approach), kept for the record, not used

## Typical invocation pattern

```bash
wsl -d Ubuntu -e bash -lc "
cd /home/cyph3r/mses_replacement/mach_sweep
/home/cyph3r/mses_replacement/su2/bin/SU2_CFD cfg_<tag>.cfg > log_<tag>.txt 2>&1
"
```

For long runs, detach so the calling shell returns immediately (don't let a Bash tool timeout kill a multi-minute SU2 solve):
```bash
wsl -d Ubuntu -e bash -lc "
cd /home/cyph3r/mses_replacement/mach_sweep
nohup /home/cyph3r/mses_replacement/su2/bin/SU2_CFD cfg_<tag>.cfg > log_<tag>.txt 2>&1 < /dev/null &
disown
"
```

## Windows <-> WSL file transfer

The Windows repo is reachable from inside Ubuntu at `/mnt/c/Users/cyphe/Downloads/airplane/...`. `/mnt/c` I/O is slow for repeated small reads (mesh generation, iterative solves) — copy working files into the WSL-native filesystem (`/home/cyph3r/mses_replacement/...`) before running anything, and copy results back to the Windows repo (`airfoils/su2_screen/...`) when done, rather than running SU2 directly against `/mnt/c` paths.

## Known gotchas (learned the hard way, 2026-08-04)

- **`OUTPUT_FILES=(RESTART, SURFACE_CSV)` does not emit a `Pressure_Coefficient` column** for a `MARKER_HEATFLUX` wall in this build — surface CSVs only contain raw conservative variables (`Density, Momentum_x, Momentum_y, Energy, ...`). Derive Cp yourself: `p = (gamma-1)*(Energy - 0.5*(Momentum_x^2+Momentum_y^2)/Density)`, `Cp = (p-p_inf)/(0.5*rho_inf*V_inf^2)`, using freestream values from the run's own log header (`Static Pressure` / `Density` / `Velocity Magnitude` — confirmed `Ref. value = 1` throughout, i.e. plain SI units).
- **`FIXED_CL_MODE` was unstable for this transonic 12%-thick-section sweep** — never engaged an AoA update in 3 pilot attempts (up to 2000 iterations), while the underlying fixed-AoA=0 flow oscillated periodically (~1000-iteration period). Root-caused as `FIXED_CL_MODE` silently perturbing AoA without printing a diagnostic (removing it entirely fixed the oscillation immediately). Use fixed AoA per run instead (Prandtl-Glauert-corrected estimate), matching the original validated SC(2)-0410 vs NACA screen's methodology.
- Real convergence plateau for this mesh/solver combo is `rms_rho ≈ -2.9` to `-3.1` — `CONV_RESIDUAL_MINVAL=-10` (an early guess) is unreachable; don't set it stricter than reality.
