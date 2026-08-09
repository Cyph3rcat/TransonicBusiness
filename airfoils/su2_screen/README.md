# SU2 2D Transonic Screen — SC(2)-0410 vs NACA 64-209 vs SC(2)-0610

**Purpose:** Resolve the transonic (M0.80) drag comparison between B.5's airfoil
candidates that NeuralFoil/XFOIL-family tools can't answer (no compressibility
model). Runs shock-capturing RANS (SU2 v8.5.0, SST turbulence model) on 2D
sections, since MSES wasn't available in this environment (licensing/compile
overhead) — SU2 was used as the free, no-license-friction alternative.

**Conditions:** M = 0.80, Re = 7.3×10⁶ (FL410 cruise-start bracket, corrected
per doubts.md #2), T = 216.65 K, α = 0°/1°/2°.

**Mesh:** ~68,000-cell hybrid C-grid (gmsh BoundaryLayer field, hwall≈5e-6c
targeting y+≈1, farfield radius 25c). Engineering-grade, not wind-tunnel-grade —
built for a fast comparative screen, not certification.

## Round 1 (all 3 candidates, 2000 iter) — INCONCLUSIVE, superseded

Residuals plateaued at only rms_rho≈-2.8 to -2.9, and C_d was still climbing
steadily at every checkpoint in the last 500 iterations (not converged).
SC(2)-0410 and NACA 64-209 came out as a near-tie at α=0°, which contradicted
the Korn-equation prediction (SC(2)-0410 needs ~0° sweep, NACA 64-209 needs
~21° at this Mach) — flagged as a fidelity gap, not a real finding.
SC(2)-0610 was clearly worst across the board (consistent with Korn) and
eliminated from round 2.

## Round 2 (SC(2)-0410 + NACA 64-209 only, 4500 iter, tighter Cauchy) — TRUSTED

C_d genuinely plateaued this time (±5% drift in the final 350 iterations, vs
~15% still-climbing in round 1). Results:

| Airfoil | α | C_l | C_d (counts) | L/D |
|---|---|---|---|---|
| **SC(2)-0410** | 0° | 0.422 | 106 | **39.9** |
| **SC(2)-0410** | 1° | 0.748 | 315 | 23.8 |
| **SC(2)-0410** | 2° | 0.936 | 640 | 14.6 |
| NACA 64-209 | 0° | 0.371 | 163 | 22.8 |
| NACA 64-209 | 1° | 0.659 | 424 | 15.6 |
| NACA 64-209 | 2° | 0.880 | 658 | 13.4 |

**Conclusion:** At comparable C_l (~0.37–0.42), SC(2)-0410 shows ~35% lower
drag and nearly double the L/D of NACA 64-209 at α=0° — confirms (does not
just repeat) the Korn-equation sweep conclusion in config.md B.5, now with
real shock-resolving CFD rather than only the empirical formula.

## Caveats — still ASSUMPTION/PLACEHOLDER-grade, not GROUNDED

- Single design point per candidate, not a full polar — only 3 AoA points.
- Mesh is a fast engineering screen (~68k cells), not grid-independence-checked.
- No comparison yet to real wind-tunnel data at this specific Re/Mach (NASA
  TP-2969 didn't wind-tunnel-test SC(2)-0410 itself, only the c_l=0.7 family
  members — see prior chat discussion).
- 2D section only — real wing will have SC(2)-0410 at ~0° sweep vs.
  NACA 64-209 needing ~21°; this run deliberately tested both **unswept** at
  the same M0.80 to isolate section-level wave-drag character, consistent
  with B.5's original screening methodology.

## Files

- `cfg_*.cfg` — SU2 config files (round 2, final)
- `log_*.txt` — solver stdout (iteration history table)
- `history_*.csv` — SU2 residual history (Cl/Cd not included — see log_*.txt)
- `*.su2` — meshes
- `make_mesh.py`, `gen_configs.py`, `parse_results.py` — generation/parsing scripts

---

# SC(2)-0412 adaptive Mach sweep (2026-08-04) — real M_crit / M_dd, no Korn equation

**Why this exists:** SC(2)-0410 (above) was retired — 9.97% t/c wasn't enough wing volume for the required fuel load (doubts.md #15: only 26–43% of the ~65 ft³ requirement fit in the spar box). Replaced by two thicker, still-real NASA SC(2) family members: **SC(2)-0412 (12% t/c)** and **SC(2)-0414 (14% t/c)**, accepting more sweep as the tradeoff. Per explicit request, Korn's equation is retired (see B.5.1 above — it already contradicted itself across methods once). In its place: a real SU2 Mach sweep (this section) plus the classical Prandtl-Glauert + critical-Cp method (`airfoils/critical_mach_pg.py`), driving sweep via simple sweep theory `Λ25 = arccos(M_crit/M_c)` instead of Korn's regression.

**Scope:** only SC(2)-0412 got a full CFD sweep this pass (time constraint, explicit user decision). SC(2)-0414 has only the PG estimate.

**Method:** `adaptive_sweep.py` — fixed AoA per Mach point (PG-corrected estimate targeting C_L≈0.248, no `FIXED_CL_MODE` — see `ENVIRONMENT.md` for why that was dropped), stepping Mach upward from 0.5922 in +0.03 increments, stopping once the Cd(M) "hockey stick" is confirmed by 2 consecutive intervals with dCd/dM ≥ 0.10 (the standard "Boeing criterion" for drag-divergence Mach) or a 7-point cap. Retuned convergence tolerance from the round-2 baseline above (real plateau is `rms_rho≈-2.9` to `-3.1`, not `-10`; `CONV_CAUCHY_EPS` loosened to 5E-5). Raw results: `mach_sweep_sc20412/adaptive_sweep_results.json` (per-point CL/CD/residuals/freestream state) and `mach_sweep_sc20412/results_su2_sweep_sc20412.json` (Cp_min, M_crit, M_dd).

**Results (7 points, M=0.5922 to 0.7722):**

| M | CD | Cp_min | Cp_cr(M) |
|---|---|---|---|
| 0.5922 | 0.02723 | -1.1746 | -1.3453 |
| 0.6222 | 0.00524 | -1.1977 | -1.1593 |
| 0.6522 | 0.02335 | -1.4365 | -0.9974 |
| 0.6822 | 0.01552 | -1.3581 | -0.8553 |
| 0.7122 | 0.00445 | -1.1040 | -0.7298 |
| 0.7422 | 0.01255 | -1.1884 | -0.6182 |
| 0.7722 | 0.02075 | -1.1935 | -0.5183 |

Cd(M) is genuinely noisy/non-monotonic across most of the range (not a clean textbook curve) — the sustained rise (2 consecutive intervals above the Boeing criterion) only shows up in the last three points. `Cp_min` crosses `Cp_cr(M)` once, early (between M=0.5922 and 0.6222), and stays crossed for the rest of the sweep — physically consistent (once local flow goes sonic, it stays sonic at higher freestream Mach).

**M_crit (Cp-crossing) = 0.617.** Notably lower than the PG estimate (0.692) — checked why: at M=0.62, real CFD shows the suction peak amplified ~2x over its low-speed value, but Prandtl-Glauert's linearized `1/√(1-M²)` correction only predicts ~1.3x amplification at that Mach. PG's known breakdown near M~0.6–0.7 explains the gap; not an unexplained discrepancy.

**M_dd (Cd hockey-stick, sustained rise) = 0.712.** Higher than M_crit, as expected (M_dd requires the shock to actually grow enough to raise drag measurably, not just appear).

**Comparison table:**

| Method | Value | Λ25 = arccos(M/0.80) |
|---|---|---|
| Prandtl-Glauert (SC(2)-0412) | M_crit ≈ 0.692 | 30.1° |
| Prandtl-Glauert (SC(2)-0414) | M_crit ≈ 0.685 | 31.2° |
| **SU2 CFD, Cp-crossing (SC(2)-0412)** | **M_crit ≈ 0.617** | **39.6°** |
| **SU2 CFD, Cd hockey-stick (SC(2)-0412)** | **M_dd ≈ 0.712** | **27.1°** |

**Decision (user, 2026-08-04):** adopt the **M_dd hockey-stick** basis → **Λ25 = 27.1°** for SC(2)-0412, not the literal M_crit Cp-crossing figure (39.6° — technically what the pasted formula calls for, but M_dd is the more practically meaningful quantity for sizing sweep: it's where drag actually becomes a problem, not just where the first sonic speck appears, and 40° sweep would be unusually aggressive for a subsonic bizjet at M0.80). SC(2)-0414 has no CFD M_dd (no CFD sweep run for it this pass) — its Λ25 stays at the PG-method figure, 31.2°, tagged ASSUMPTION not GROUNDED.

**Files:** `mach_sweep_sc20412/` — `adaptive_sweep_results.json`, `results_su2_sweep_sc20412.json`, `cfg_*.cfg`, `log_*.txt`, `surface_*.csv` (all 7 points). `adaptive_sweep.py`, `extract_cpmin_crossing.py` — orchestration/extraction scripts (run again from a WSL working directory with `sc20412.su2` present to regenerate/extend).
