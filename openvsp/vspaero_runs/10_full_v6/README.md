# 10_full_v6 — empennage right-sizing + fuselage closure (2026-08-07)

Working model for the whole aircraft. Supersedes `09_full_v5`.
Write-up: **config.md D.6**. CG chapter update: **weight.md §4**.

Brief (user, 2026-08-07): run the ground-truth analysis, fix the over-stability
(doubts.md #23), and check whether the aircraft is aerodynamically sound —
against a v5 whose fuselage had been reworked in the GUI.

## What the GUI edits had actually changed

`09_full_v5/full_v5.vsp3` (edited 2026-08-06) differs from what
`build_full_v5.vspscript` writes and from what config.md D.5d documents, in
**three** ways, only one of which was known:

| | build script / config.md D.5d | the file as edited |
|---|---|---|
| Fuselage | 10 XSecs, nose tip z=−1.30, windshield dent at x=8.2, tail closed to a Point | **7 XSecs**, nose tip z=−1.93, no dent, tail on a 1.667 ft **Circle with `CapUMaxOption = 0`** |
| Horizontal tail | 51.68 ft² (cr 4.6 / ct 2.2 / b 15.2) | **62.42 ft²** (cr 5.496 / ct 2.629 / b 15.365) |
| Belly fairing | 14.5 ft long at x=12.9 | 17.07 ft long at x=11.01 |

The tail-tip one is not cosmetic: `CapUMaxOption = 0` leaves the body **open** —
a 2.18 ft² hole at x=42.2. An unclosed body is ill-posed in a panel method, and
it shows: v5-as-is returns a **wiggly** pitching moment (CMy = −0.284, −0.304,
−0.299, −0.323, −0.368 across α = 0–8°) and reports SM = 11.6% with a *larger*
tail than v6's 41.1% with a smaller one. That ordering is backwards, so the
v5-as-is longitudinal numbers are not usable. v6 closes the tail (0.60 ft tip +
round cap) and its CMy is linear to R² = 0.997.

## The headline finding: the tails were sized against the wrong arm

v5 moved the wing 3.1 ft forward for the CG fix, which lengthened **both** tail
arms by 3.1 ft — but neither tail was re-sized afterwards. Recomputed at the
true arms (`size_tails.py`):

| | v5 as-in-file | Sadraey Table 6.4 | Raymer Table 6.4 (+T-tail credit) |
|---|---|---|---|
| c_HT | **1.34** | 1.1 (jet transport) | 0.95 |
| c_VT | **0.1225** | 0.09 | 0.0855 |

But re-applying the historical coefficients does *not* fix it: at c_HT = 1.1 the
solve returns S_HT ≈ 53 ft², essentially v5's as-scripted 51.68 ft² that already
measured SM = 37.7%. **Neither textbook has a light-business-jet row**; the
nearest class (jet transport, 46,000 lb+) over-sizes the tail for an 11,660 lb
aircraft. So the horizontal tail is sized from the requirement instead, and the
divergence from the taught method is the finding, not an oversight.

## Sizing method actually used

- **Horizontal tail — from the measured neutral point.** Five α-sweeps at
  S_HT ∈ {30, 38, 46, 54, 62.4} ft², everything else fixed, give a strikingly
  linear `x_np = 18.597 + 0.06450·S_HT` ft (per-run Cm fits R² > 0.999).
  Target SM = 20% at MTOW CG (conservative end of the 10–20% bizjet band, to
  hedge against VLM optimism on a T-tail in clean air) → **S_HT = 34.0 ft²**,
  c_HT = 0.678 — which lands on Raymer's *jet trainer* row (0.70), a far better
  class analogue than *jet transport*.
- **Vertical tail — from the volume coefficient.** Both books agree on
  c_VT = 0.09 → **S_VT = 45.0 ft²**. The β-sweep could not rank fin sizes (see
  below), so the textbook value governs and the VLM only confirms stability.
- **Cross-check on the wing-body.** The fit's intercept puts the tail-off NP at
  1.0% MAC. Raymer Eq. (16.25) / NACA TR 711 with w_f = 6.1, L_f = 42.2,
  K_fus ≈ 0.017 gives a fuselage ac shift of −33% MAC, i.e. wing-body ≈ −8% MAC
  from a 25% MAC wing-alone ac. Independent methods, same picture: on this
  aircraft the fuselage is hugely destabilising and the tail does nearly all the
  stabilising work.

## Results

| Quantity | v5 (as documented) | **v6** | note |
|---|---|---|---|
| S_HT | 51.68 (file: 62.42) | **34.0 ft²** | c_HT 1.10 → **0.678** |
| S_VT | 59.0 | **45.0 ft²** | c_VT 0.1225 → **0.090** |
| SM @ MTOW CG | 37.7% | **17.0%** | in band |
| SM @ aft CG | ~34% | **13.7%** | in band |
| SM @ fwd CG | ~41% | 22.5% | slightly above band |
| Cnβ | +0.143 | **+0.217/rad** | S/N 215, stable |
| Clβ | −0.179 | −0.145/rad | in the −0.05…−0.20 band |
| CL_α | 4.698 | 4.463 /rad | smaller tail |
| wake e | — | **0.92–0.96** | CDiw → 0.00016 at CL≈0 |
| CD0 | *never computed* | **0.0252** | Raymer buildup, FL410/M0.80 |
| L/D cruise | 12 (PLACEHOLDER) | **12.1** | MTOW; 10.9 end-cruise |

Empennage weight saved: 69 lb (HT 105→69, VT+dorsal 140→107), which moves the
MTOW CG from 27.6% to **24.6% MAC** — accounted for inside the solve, not after.

**The L/D = 12 placeholder is vindicated.** weight.md §2.4's Breguet calc used
L/D = 12 with a "High risk — historical trend only" flag; the component buildup
returns 12.13 at start of cruise. Raymer's own `L/D_max = K_LD·√(AR_wet)` check
agrees too: AR_wet = 1.35 → implied K_LD = 14.6 against Raymer's 15.5 for a
civil jet, a 6% spread.

## What could not be resolved

**Cnβ cannot be ranked against fin area by this toolchain.** Across
S_VT = 38–59 ft², Cnβ scatters 0.118–0.241 with a rank correlation against area
of −0.43 (i.e. the wrong sign — physically impossible), while correlating
**−0.87 with the solve's own symmetry error** |CMz| at β = 0. Removing the
dorsal fin from the analysis set changes nothing (0.1855 → 0.1888 at 59 ft²), so
the dorsal/fin overlap is not the cause. This is the same family of problem as
doubts.md #21 and is logged as a new item.

What *is* solid: **every fin size tested is comfortably stable**, the worst being
+0.118/rad against a +0.06 floor. So shrinking the fin 59 → 45 ft² does not
endanger directional stability even though the sweep cannot say by how much.
S_VT = 44 happens to be the best-resolved run in the whole campaign
(S/N = 10,120, Cnβ = +0.241).

## Still open after this pass

- **Controllability line not computed.** The tail is sized on the stability
  constraint only. The forward-CG trim case (flaps down) and the nose-wheel
  liftoff case set a *minimum* S_HT that has not been checked — and forward CG
  is exactly where SM came out highest (22.5%), so elevator authority there is
  the next thing to verify. Until then S_HT = 34 ft² is a stability-driven
  answer, not a jointly-constrained one.
- **Nose geometry.** Transcribed faithfully from the user's loft and verified
  against the mesh: the tip sits at z = −1.93, i.e. **63% of a barrel radius
  below the axis** (bizjets typically run 30–40%), and the round radome cap
  extends 0.35 ft ahead of x = 0. The shaded views read as a drooping snout.
  Not an error — a styling call to confirm.
- **Wave drag.** The drag polar is pre-wave-drag. At M0.80 the design sits *at*
  its swept M_dd (config.md B.5.3), so 10–20 counts is expected. That is what
  the staged SU2 Euler pass is for.
- The windshield dent that D.5d argued for is absent from the current loft.

## Files

Sizing / analysis
- `size_tails.py` — coupled empennage/CG solve; historical vs requirement-driven
  sizing side by side. `--np A,B` takes the measured NP fit; `--fix-wing` pins
  the wing (required with `--np`, since the fit is only valid at the wing
  position it was measured at).
- `gen_v6.py` — builds full_v6 and every parametric variant, runs VSPAERO.
  `--baseline | --ht-sweep | --vt-sweep | --final S_HT S_VT XW`
- `drag_buildup.py` — Raymer Ch.12 component buildup + cruise polar. Applies
  Raymer's Q factors (OpenVSP writes Q = 1.0 for everything) and the 3% leakage
  allowance.
- `component_moment.py` — leave-one-out pitching-moment buildup: rebuilds the
  config with each component in turn excluded from the VSPAERO analysis set
  (built but contributing zero force) and diffs Cmy against the full config, at
  a single α=3.7° point. Writes `component_moment_results.json`. Compares
  v5-equivalent (v6 fuselage + v5's documented tail areas) against v6, so the
  tail-resizing effect is isolated from the fuselage/open-tail fix.
- `drag_moment_compare.py` — the parasitic / induced / interference / moment
  before-after figure below, built from `drag_buildup.py`'s Q table and
  `component_moment_results.json`.
- `plots.py` — the four sizing/CG/drag figures.

Models
- `final_alpha/`, `final_beta/` — **the v6 configuration** (S_HT 34, S_VT 45)
- `ht{30,38,46,54,62.4}/` — S_HT parametric, α sweeps
- `vt{38..59}_beta/` — S_VT parametric, β sweeps
- `nd{44,51,59}_beta/` — same fins with the dorsal out of the analysis set
- `00_baseline/` — v6 fuselage carrying v5's tail areas, for the isolated
  comparison
- `ref_v5_asis/` — the user's `full_v5.vsp3` run unmodified: the true "before"

Figures — `v6_sizing.png`, `v6_cg_sm.png`, `v6_drag.png`, `v6_views.png`,
`v5_asis_views.png`, `v6_drag_moment_compare.png`

## v5 -> v6 drag and moment comparison (2026-08-07)

`v6_drag_moment_compare.png`, four panels, v5-equivalent vs v6 (defined above):

- **Parasitic drag by component**: total CD0 264 → 252 counts (−12), entirely
  from the tails (HT 22.7→15.4, VT 21.5→16.5 counts); every other component is
  identical since only the empennage changed.
- **Induced drag**: essentially unchanged (CDi = 0.0353·CL² → 0.0346·CL², wake
  e 1.011 → 1.032) — expected, since the wing/winglet are untouched and the
  tails carry very little lift at cruise AoA.
- **Interference drag** (Raymer Q-factor increment, `ΔCD0 = Cf·FF·Swet·(Q−1)`):
  the nacelle (Q=1.30, OTWEM proximity) dominates at ~9.3 counts in **both**
  configs, unchanged since the nacelle didn't move; the tails' own interference
  increment (Q=1.05 each) shrinks with their area, same ~1 count total as the
  parasitic saving.
- **Pitching-moment buildup** (leave-one-out at α=3.7°, `component_moment.py`):
  **HorizTail's contribution is the whole story** — −0.158 → −0.082 (a 48%
  cut, more than the 34% area cut, because the smaller tail also rides a
  shorter fin and gets a shorter arm). Every other component's contribution is
  within ±0.02 of unchanged. Fuselage and belly fairing are destabilizing
  (nose-up, consistent with Raymer Eq. 16.25 — see config.md D.6); wing and
  nacelle are mildly stabilizing at this trim point.

**Caveat, stated plainly:** the two configs are evaluated at their own solved
Xcg (19.90 for v5eq, 19.749 for v6) because that is what each configuration
actually flies at — but it means part of each component's *changed* moment
contribution is the different moment-reference point, not purely a change in
that component's own aerodynamics. Also: leave-one-out contributions do not
sum to the full-config Cmy (v5eq: components sum to −0.128 vs full −0.233;
v6: −0.058 vs −0.167) — the ~−0.105 gap in both is multi-component
interference that a single-removal buildup cannot attribute to one part. This
is expected for a nonlinear panel/VLM solve and is reported, not hidden.

## Re-running

```
python gen_v6.py --ht-sweep --vt-sweep
python size_tails.py --np 18.5969,0.064497 --sm 0.20
python gen_v6.py --final 34.0 45.0 15.9
python drag_buildup.py && python plots.py
```

## Fidelity caveats

Inherited from the parent README, plus: the α/β sweeps are VLM at **M0.30** and
the drag buildup is at **M0.80** — they are combined into one polar because
induced drag is weakly Mach-dependent below drag divergence, but that is an
assumption, not a measurement. Nothing here is transonic.
