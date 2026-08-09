# Fuselage Design Plan

**Status:** Planning only — no CAD yet. This document works the fuselage the way `config.md` works the wing: numbers first, geometry second, CAD third. Do not loft anything from this file until the numbers below are reconciled with `doubts.md`.

**Status-tag legend** (same convention as `config.md`):
- **GROUNDED** — computed from a stated formula and traceable inputs, or a verifiable published spec.
- **ASSUMPTION** — a deliberate design choice, defensible but not derived from a constraint.
- **PLACEHOLDER** — a stand-in number with weak or no sourcing; expected to change.
- **CONFLICT** — two different values exist for the same quantity elsewhere in the project.

**Original design intent (2026-08-04, preserved verbatim from the first pass):**
> ok fuselage time. remember, 8 pax. similar to hondajet 2. wing is about 197 ft². I need to prepare the top side and front view diagram. ig we could sort of rig most of this from hondajet, maybe make the interior just a little bit more spacious. make the nose cap and tail cap ideal and make sure volume and overall variation in volume obeys area law because flight is at mach 0.8.

---

## 1. Theoretical basis: shaping the fuselage for transonic wave drag

The generic nosecap taxonomy (spherically-blunted cone, tangent ogive, secant ogive, parabolic/power-series, Haack series) is written for a wide span of flight regimes — most of it (blunted cones for reentry heating, secant ogives for radar-dish clearance) is **not applicable to a subsonic/transonic business jet with no radar and no thermal-protection requirement**. What's actually load-bearing for us is the transonic-specific subset:

### 1.1 Whitcomb's Transonic Area Rule (the governing principle)
Wave drag at high subsonic/transonic Mach is driven by the rate of change of the airplane's **total cross-sectional area distribution**, `A(x)`, along the fuselage axis — not by the fuselage shape in isolation. The wing, the OTWEM nacelle/pylon, and the fuselage all add cross-sectional area at their respective stations; a smooth `A(x)` (small `dA/dx`, no kinks) delays drag rise and raises `M_dd`, while an abrupt jump (e.g., wing root + nacelle area landing on top of the fuselage's own area at the same station) drops `M_dd`. This is why fuselages get "waisted" near the wing — it's compensating cross-section, not styling. **GROUNDED (established theory, Whitcomb 1952/NACA RM L52H08, validated on F-102).**

### 1.2 Sears-Haack body — reference minimum-wave-drag closed shape
For a closed body of revolution of fixed length `L` and volume `V`, the theoretical minimum-wave-drag area distribution (linearized transonic/supersonic small-disturbance theory) is:

```
S(x) = (16V)/(3πL) · [4(x/L)(1 − x/L)]^(3/2),   0 ≤ x ≤ L
D_wave = 128·q·V² / (π·L⁴)
```

This is the *target curve* the whole-airplane `A(x)` should approximate once the wing/nacelle contributions are added to the fuselage's own area — this is the practical tool for checking the "coke-bottle" question, not a shape to CAD directly. **GROUNDED (closed-form classical result).**

### 1.3 Correction (2026-08-04): the nose cap is NOT a von Kármán ogive — it's a rounded ellipsoid/paraboloid, and here's why
**The first pass of this section (Haack-series/von Kármán ogive nose) was wrong for this application, and got corrected before it reached CAD.** Worth recording *why*, not just the new answer:

The Sears-Haack/Haack-series family (§1.2) is the right tool for the **whole-airplane area distribution** (§1.1, §1.8) — that theory is genuinely transonic-applicable, which is why it's still used for the area-rule waist. But applying the *same* family to shape the **nose tip specifically** is a different claim, and it doesn't hold up here:

1. **Wave drag isn't the nose's problem at M0.80.** The wing needed a supercritical section (config.md B.1) specifically because it *does* see local supersonic flow at cruise. A well-faired fuselage nose, by contrast, can be shaped to stay fully subsonic locally with no shock at all — its drag budget is dominated by skin friction and separation avoidance, not wave drag. Minimum-wave-drag shaping is solving a problem the nose mostly doesn't have.
2. **A sharp, highly-pointed tip is actually counterproductive at these speeds.** Tight local curvature accelerates the flow hard right at the point (same mechanism as why a sharp subsonic airfoil leading edge is worse than a rounded one) — a von Kármán ogive's pointed tip can locally punch into a small supersonic pocket of its own at M0.80, and risks earlier separation, which a gentler rounded profile avoids. The theoretical wave-drag-minimum shape can be a practical own-goal outside the regime it was derived for.
3. **Every real bizjet in this class agrees.** Phenom 100/300, HondaJet, Citation — none of them use a pointed ogive nose; they use a rounded, ellipsoidal/paraboloid fairing blending into the windscreen. That's not styling, it's the same physics in #1–#2 playing out in certified hardware.
4. **Weather radar.** Not currently a stated requirement anywhere in `config.md`/`market.md`, but every certified competitor in this class carries a weather radar dish behind the nosecone as a de facto safety standard — **adding this as a new ASSUMPTION** rather than silently designing around it. A rotating parabolic dish needs a wide, blunt radome to sweep in, which a sharp ogive tip cannot house without wasting length. This reinforces #1–#3, it isn't the only reason.
5. **Manufacturability.** A gently-curved ellipsoid/paraboloid of revolution is a standard composite-mold shape. A mathematically exact Haack-family curve down to a fine point adds tooling complexity and produces a fragile, damage-prone tip (bird strike, ground handling) for no aerodynamic benefit in this regime.

**Adopted family: rounded ellipsoid/paraboloid nose fairing** (an ellipse of revolution, or an equivalent low-order power-law profile — `r(x)/R = (x/L_nc)^n` with `n` in roughly the 0.5–0.7 range gives an ellipsoid-like rounded profile, tunable for radome volume vs. friction), blending tangentially into the constant-diameter cabin barrel and into the windscreen per the visibility note below. **ASSUMPTION** (family and blend), consistent with §1.4 and every named competitor.

For the **tail cone**: same correction applies in spirit — it's not a Sears-Haack-style pointed closure either. It's a smooth, moderately-tapered upsweep closure (§7), shaped by the upsweep-angle constraint and empennage/pylon attach structure far more than by any minimum-wave-drag target. Don't model it as "the nose math, mirrored."

### 1.4 Why not the other families from the generic list
- **Spherically blunted cone** — driven by aerothermal/reentry or hypersonic bird-strike concerns. Not our regime; drop it. (Ordinary bird-strike/pitot structural provisions still cap how sharp the physical tip can be, but that's a structures detail, not a shape-family driver.)
- **Tangent/secant ogive (circular arc), Haack series / von Kármán ogive** — all four are supersonic/transonic-wave-drag-minimum-derived families (§1.3). Correct for a missile or rocket nose; not correct for a subsonic-friction-dominated bizjet nose fairing at M0.80, per §1.3. Dropped as the governing family for the nose cap specifically (they remain correct for the *whole-airplane area distribution*, §1.1–§1.2 — that's a different claim).
- **Parabolic / power-series** — this is actually the **right** family, not a fallback. An ellipsoid is a special case of a power-law profile; tuning the exponent trades radome volume against friction/separation behavior. This is what §1.3 adopts.

### 1.5 Link back to the wing chapter
`config.md` B.5 originally picked NASA SC(2)-0410 (supercritical, t/c≈9.97%) recommending ~0° sweep at M0.80 via the incompressible Korn-equation screen. **This has since been reopened by doubts.md #12** (2026-08-03/04, `airfoils/evaluate_transonic.py`): a Mach-corrected re-screen reverses the pick — NACA 64-209 now looks stronger and needs ~0° sweep, while SC(2)-0410's L/D collapses unless swept ~20°, and that decision is still unresolved. Either way, the surviving candidate lands near **0° sweep**, so the area-ruling implication below holds regardless of which airfoil wins: a ~0° sweep wing gives area-ruling *less slack* than a swept wing would (sweep smears the wing's area addition over a longer axial run), so the fuselage waist has to do more of the work here than on a swept-wing competitor. Keep this in mind in §8 — but don't lock the wing-fuselage intersection geometry until doubts.md #12 actually resolves, since a 20°-swept SC(2)-0410 would move the wing's area contribution to a different (and longer) axial run than a 0°-swept NACA 64-209 would.

---

## 2. Reference benchmark — HondaJet Elite II

Cross-checked across two independent secondary sources (Honda's own brochure PDF returned HTTP 403, so this is **not primary-sourced** — treat as ASSUMPTION-grade until a primary spec sheet is found):

| Parameter | Value | Source |
|---|---|---|
| Overall length | 42.58 ft (42′7″) | Quantum Jets spec compilation |
| Wingspan | 39.75 ft (39′9″) | Quantum Jets spec compilation |
| Height | 14.92 ft (14′11″) | Quantum Jets spec compilation |
| Cabin length (total) | 17.8 ft | Cross-checked: Quantum Jets + SimpleFlying |
| Cabin width | 5.0 ft (60 in) | Cross-checked: Quantum Jets + SimpleFlying |
| Cabin height | 4.83 ft (58 in) | Cross-checked: Quantum Jets + SimpleFlying |
| Baggage volume | 62 ft³ (53 aft + 9 nose) | SimpleFlying |
| MTOW | 11,100 lb | Quantum Jets |
| Fuel capacity | 468 US gal | Quantum Jets |
| Typical / max pax | 5–6 typical / 7 max | Cross-checked |

**ASSUMPTION (ours, not sourced):** external fuselage diameter ≈ 5.8 ft, backed out from cabin width (5.0 ft) + an assumed ~0.8 ft combined double-wall/insulation/structure allowance. No source gives this directly. Used only to sanity-check our own fineness ratio in §5 — don't treat 5.8 ft as a HondaJet fact.

**First divergence from "just copy HondaJet": we're targeting 8 pax against their 5–7.** That's the headline driver for why our fuselage comes out longer than a straight HondaJet scale-up — see §3 and §4.

---

## 3. Inputs pulled from the rest of the project, and pax count confirmed

| Quantity | Value | Source |
|---|---|---|
| W_TO | 11,660 lb | config.md A.3 |
| S (wing) | 193.7 ft² | config.md B.2 |
| AR | 8.9 | config.md B.1 |
| Cruise Mach | 0.80 | config.md A.1 |
| Fuel weight fraction | 0.2634 | config.md A.3 |

**RESOLVED 2026-08-04 — doubts.md #1 and #14 both closed.** Confirmed: the design point is **6 passengers + 2 crew = 8 total occupants**, matching what `config.md` A.3's W_PL was already built on (1,720 lb). The earlier draft of this section (8 pax + 2 crew = 10 occupants) was a misreading of the original scratch note ("remember, 8 pax" meant *8 total occupants*, not 8 passengers) and has been corrected throughout §4–§11 below. No W_PL/W_TO rework needed — this chapter is now consistent with A.3, not in conflict with it.

---

## 4. Cabin layout sizing (Sadraey Eq. 7.1 / 7.2)

Single-aisle, 2-abreast (matches every twin in this weight class — there's no cabin-width budget for 2+2 at ~5.5 ft width). Seat/pitch data chosen from Table 7.4's "first class" band (60–75 cm width, 92–104 cm pitch), scaled down slightly since a VLJ-class cabin can't fit true first-class airliner dimensions — this is a deliberate "roomier than HondaJet, not as roomy as a widebody" target:

| Parameter | Value | Tag |
|---|---|---|
| Seats abreast, n_S | 2 | ASSUMPTION (only geometrically viable layout at this width) |
| Aisles, n_A | 1 | ASSUMPTION |
| Seat width, W_S | 25 in | ASSUMPTION (mid of Table 7.4 first-class band) |
| Aisle width, W_A | 16 in | ASSUMPTION |
| **Cabin width, W_C** | **W_C = 2(25) + 1(16) = 66 in = 5.5 ft** | GROUNDED (formula, given inputs) — **+10% over HondaJet's 5.0 ft**, matching the "slightly more spacious" brief |
| Rows | 3 (6 seats total) | GROUNDED (given n_pax = 6, n_S = 2 — see §3, doubts.md #1/#14 resolved) |
| Seat pitch, P_S | 40 in | ASSUMPTION (Table 7.4 first-class band, low end) |
| Passenger section length | 3 × 40 in = 10.0 ft | GROUNDED (Eq. 7.1, given inputs) |
| **Enclosed lavatory** | 3.0 ft | ASSUMPTION — see below, not a generic "galley/lav allowance" anymore |
| **Cabin length, L_C** | **13.0 ft** | GROUNDED (sum, given inputs above) |

**Enclosed lavatory — explicit requirement, and the actual OTWEM payoff.** HondaJet's own marketing of OTWEM is specifically that mounting the engines over the wing eliminates the aft-fuselage support structure (ducting, firewall, engine-mount carry-through) that a rear-fuselage-mounted-engine competitor (Citation CJ-series, most Learjets) has to build into that same volume — see §1's OTWEM discussion, confirmed by SimpleFlying's HondaJet engineering writeup: *"typical private jets require large support structures inside the fuselage for the rear-mounted engines… With the HondaJet's engines placed above the wings, these supports are eliminated and deliver a more spacious cabin area."* That freed aft-fuselage volume is exactly where a **fully enclosed lavatory** (not a belted potty) goes — competitors with rear-mounted engines often can't fit one in this size class. This is a genuine, structurally-grounded differentiator, not just a comfort nice-to-have, and it should be called out in the market chapter alongside the existing cabin-volume claim. 3.0 ft is a rough placeholder length (enough for an enclosed door + fixture), not sized against a specific fixture yet.

Versus HondaJet: their 17.8 ft cabin seats 5–7 at generous pitch (implied ~50+ in for 6 pax across 12.1 ft of pax section); ours is shorter (13.0 ft) at the same headcount (6) because pitch is tighter (40 in) and the enclosed-lav allowance (3.0 ft) is more conservative than whatever HondaJet folds into their number. **Total fuselage length still converges within 1% of HondaJet's (§5)** — a good sign the overall sizing is self-consistent even though the internal split of that length is a rough first cut.

---

## 5. Fineness ratio and overall length

**Fuselage external diameter:** `d = W_C + 0.6 ft (wall allowance) = 6.1 ft`. **ASSUMPTION** (wall/insulation/structure allowance, not derived from a structural sizing pass).

**Two independent checks, cross-validated:**

**(a) Comparable-class benchmarking (Table 7.7):** twin-turbofan light transports run L/d ≈ 7.5–10.7 (Cessna Citation III = 8, Fairchild Metro VI = 10.7, Fokker 100 = 9.85). Our own backed-out HondaJet estimate: L/d ≈ 42.58/5.8 ≈ **7.34**.

**(b) Cabin-length correlation (Fig. 3.16, fit across civil transports):**
```
L/d = 5 + 0.9(L_C/d)
(L_nc + L_tc)/d = 5 − 0.1(L_C/d)
```
With `L_C/d = 13.0/6.1 = 2.13`:
```
L/d = 5 + 0.9(2.13) = 6.92
(L_nc + L_tc)/d = 5 − 0.1(2.13) = 4.79  →  L_nc + L_tc = 29.2 ft
```

Our correlation-driven L/d = 6.92 sits just under the Table 7.7 comparable band (7.5–10.7) and under the HondaJet backed-out value (7.34) — expected, since a shorter 3-row cabin (§4) pulls the correlation down a bit. Not a red flag; it's the correlation responding correctly to a shorter cabin at the same diameter. Adopting **L/d = 6.92 → L = 42.2 ft total fuselage length. GROUNDED (given inputs and stated correlation).** This lands within 1% of HondaJet Elite II's actual 42.58 ft — a good convergence check given how different the two derivations are (ours: cabin-length correlation; HondaJet: a real certified airframe).

**On "needa choose a good L/D":** the Sforza `C_D,fus`-vs-fineness chart (Week 8 slide, M0.85/FL350) bottoms out around F ≈ 3–4 for *fuselage-alone friction+form drag*, then rises steadily out to F = 14. Our F = 6.92 is well past that pure-friction minimum — but that minimum assumes cabin volume is free, which it isn't. Real aircraft (Table 7.7) all sit at F = 7–12 because cabin-length packaging dominates. Being on the "slenderer than friction-optimal" side is actually the *right* direction for area-ruling at M0.80 (slenderer nose/tail closures = smaller local dA/dx), so the extra skin-friction cost of F = 6.92 vs. F ≈ 3–4 is being spent on something that also helps wave drag, not wasted. **ASSUMPTION (F target), reasoning GROUNDED.**

**Nose/tail split (Fig. 3.17):** open/filled-square clusters put typical `L_nc/d ≈ 1.5`, `L_tc/d ≈ 2.7` (tail cones consistently longer than nose cones in the source data — makes sense, tail cones carry the upsweep taper + empennage attach). Scaling proportionally to our required sum of 4.79·d:

| | L/d | Length (ft) |
|---|---|---|
| Nose cone | 1.71 | 10.4 |
| Tail cone | 3.08 | 18.8 |

**ASSUMPTION** (proportional split from a generic correlation, not derived for this airframe — and notably, this doesn't yet reflect the OTWEM pylon/empennage structural loads that will actually size the tail cone in a later chapter).

**Total length check:** 13.0 (cabin) + 10.4 (nose) + 18.8 (tail) = **42.2 ft** ✓, vs. HondaJet's real 42.58 ft — within 1%, at essentially the same pax count (6 vs. HondaJet's typical 5–6) and MTOW class. Good self-consistency check.

---

## 6. Nose cap definition

**Profile equation fixed 2026-08-05 (config.md D.5b).** The family in this section was right; the *equation first lofted from it* was not. The CAD used `r/R = (x/L_nc)^0.6`, a power law. A power law with exponent < 1 has a **non-zero slope where it meets the barrel** — `dr/dx = 0.6·R/L_nc = 0.176` here — so the nose met the constant section at a 10° tangency break. That break is what made the nose read as "a cone stuck on a tube" rather than a Phenom-style rounded cap. Adopted instead:

```
r(x)/R = sin[ (π/2) · (x/L_nc)^0.7 ],   0 ≤ x ≤ L_nc
```

Both endpoint conditions now come out right by construction: `dr/dx → ∞` at `x = 0` (a genuinely **round, blunt tip** — radome-compatible, no fine point to protect) and `dr/dx → 0` at `x = L_nc` (**exact tangency** into the barrel, C¹ continuous). The exponent 0.7 sets fullness: it sits between a plain power law (too lean near the tip) and a true prolate ellipsoid (too blunt at this 3.41 axis ratio). Length (10.4 ft), base diameter (6.1 ft) and family (rounded ellipsoid/paraboloid, §1.3) are all unchanged — this is a blend fix, not a redesign. Realised stations are echoed by `openvsp/vspaero_runs/08_full_v4/build_full_v4.vspscript`.

**Nose droop, same pass:** −0.60 ft at the tip (was −0.85), shaped `z = −0.60·(1 − x/L_nc)²` so `dz/dx → 0` at the barrel as well. The pilot-visibility intent below is preserved; the earlier version had a residual centreline kink at the barrel joint on top of the radius kink.

- **Family:** rounded ellipsoid/paraboloid of revolution, per §1.3 (**not** a von Kármán ogive — corrected 2026-08-04). Friction/separation-driven, radome-compatible, matches Phenom/HondaJet/Citation practice.
- **Length:** 10.4 ft (§5), base diameter 6.1 ft, L_nc/d = 1.71 — comparable proportions to a real bizjet nose.
- **Radome:** weather radar dish assumed as a de facto requirement (§1.3 point 4 — not currently written anywhere in `market.md`/`config.md`, flagging as a new ASSUMPTION now rather than silently designing around it). The rounded profile's wider cross-section near the base gives room for the dish/gimbal to sweep without the volume-starved tip a pointed ogive would leave.
- **Tip:** rounded (ellipsoid, not pointed) by construction — no separate "leave a finite radius" patch needed the way a true ogive would require. Still needs a bird-strike/pitot-static structural check, but that's sizing the skin/structure at the tip, not the outer mold line. **ASSUMPTION** (profile), structures detail **PLACEHOLDER**.
- **Pilot visibility constraint:** same as before — the upper nose profile still gets locally cropped/flattened near the windscreen for forward-down visibility, same as every real bizjet. An ellipsoid nose actually blends into this crop more naturally than a sharp ogive would have. **Not blocking at this planning stage — flag for the CAD pass, don't model the nose as a perfect body of revolution.**
- **Manufacturability:** this was a specific concern raised and is a real point in the ellipsoid's favor — gentle, continuous curvature is a standard composite-mold shape with no fragile fine point to protect, unlike a mathematically exact ogive tip.

---

## 7. Tail cone and upsweep angle

- **Length:** 18.8 ft (§5), tapering from d = 6.1 ft down to whatever the empennage attach/APU/tailcone-closure diameter ends up being (not yet sized). Per §1.3, this is a smooth upsweep-driven taper, not a minimum-wave-drag closure shape.
- **Upsweep angle, α_us:** Week 8 criterion is `α_us < 20°` (flow separation limit). Civil-transport comparables run 10–17° (Boeing 777-300 ≈ 17°, Cessna 172 ≈ 10°). **Target α_us ≈ 13–15°, ASSUMPTION** (mid-range, no rotation/gear-geometry calc behind it yet).
- **Open dependency:** the real driver of α_us is landing-gear height (H_LG) and takeoff rotation angle (α_TO), per the Week 8 figure — neither exists yet in this project (no landing-gear chapter). This number is a placeholder until that chapter exists; don't lock the tail-cone CAD spline to 13–15° yet.
- **OTWEM interaction:** because the engines pylon-mount above/aft of the wing rather than on the aft fuselage (contrast: Learjet/Falcon-style aft-fuselage-mounted engines), the upsweep region is comparatively unobstructed by nacelle structure — likely *less* of a packaging conflict than a rear-fuselage-mounted-engine competitor would have. Not quantified, just noted as a favorable side effect of the OTWEM choice.

---

## 8. Area-rule waisting and the OTWEM interaction (the "coke bottle" question)

> **ANSWERED 2026-08-05 — no waist. See config.md D.5b and doubts.md #10.** This section's premise (that the barrel must lose section where the wing/nacelle add it) was tested by actually building both and measuring, and it did not hold for this configuration. full_v4 removed the waist entirely — a true constant 6.10 ft circular barrel over the whole 13.0 ft cabin — and OpenVSP's M1.0 wave-drag metric went **down**, 1.53 → 1.49 (D/q, ft²), while enclosed volume went **up** 17%. Two reasons, both worth keeping:
>
> 1. **The metric responds to `dA/dx` smoothness, not to peak height.** A fuller (tangent-blended, §6) nose plus a flat barrel plus a monotone tailcone has lower `dA/dx` everywhere except the crest — which more than pays for the taller peak.
> 2. **The crest at x ≈ 21–27 is produced by wing + nacelle + fairing, not by the fuselage.** Pinching the barrel was never the lever; it was moving the wrong variable. If that crest is to come down, it comes down through wing-root/pylon/nacelle *shaping*, which is a 3-D CFD job (config.md D.5), not more slicing.
>
> **Manufacturability was the independent second reason, and on its own it is decisive.** A constant section means one frame drawing, single-curvature (developable) skin panels rolled to a single radius, straight stringers, and one window-belt jig. A continuously-varying "coke" section means every frame is unique, every skin panel is double-curvature, and there is no panel commonality — a large recurring-cost penalty at bizjet rates. The waisted loft was aerodynamically defensible in principle and unbuildable in practice, for a benefit its own gauge says was not there.
>
> `A(x)` is retained as a **check** on future geometry changes, not as a shaping driver. What follows is the original 2026-08-04 reasoning, kept because §8.1–§8.3's *station bookkeeping* is still correct and still feeds the CG chapter.

Per §1.1, the fuselage needs to lose cross-sectional area wherever the wing + OTWEM pylon/nacelle are adding it, to keep whole-airplane `A(x)` smooth. Station-wise, using the nose-tip-origin lengths from §5–7:

- Nose cone: x = 0 → 10.4 ft
- Cabin: x = 10.4 → 23.4 ft
- Tail cone: x = 23.4 → 42.2 ft

The wing (low-mounted) and OTWEM nacelle/pylon will land somewhere in the aft half of the cabin / forward tail-cone region — the exact station depends on CG placement for static margin, which is a **later chapter that doesn't exist yet**. That means:

1. **The waist station can't be finalized until CG/wing-longitudinal-placement is done.** Don't CAD a specific waist location yet — this document can only say "aft cabin / forward tailcone, roughly x ≈ 24–30 ft," not a number.
2. **This directly sharpens doubts.md #10** (area-ruling vs. the "largest cabin" marketing claim): the waist is landing right where the wing box competes for cabin cross-section with passenger shoulder room — and now we know it's in the aft-cabin region specifically, not a vague "somewhere," because that's also where 8-pax packaging is tightest (rows 3–4 of the cabin). That's a real, now-concrete tension between the market chapter and this chapter.
3. **Practical tool, not full CFD:** OpenVSP's built-in Wave Drag analysis (computes the equivalent Sears-Haack area distribution directly from VSP geometry) is the right tool to actually check this once wing + fuselage + nacelle are assembled — see the earlier discussion in this session. This document doesn't run it; it's a to-do for the OpenVSP assembly step, after this geometry is locked enough to loft.

---

## 9. Baggage/luggage compartment (Week 8 formula, Step 11)

Per-bag volume from the FAR-style checked-bag envelope (158 cm combined L+W+H, cubed/27):
```
V_b = (158/3)³ cm³ = 146,085.6 cm³ = 0.146 m³ per bag
```
Worst-case (2 bags/pax, airline rule, n_t = 12 bags for 6 pax):
```
V_C = 12 × 0.146 m³ = 1.75 m³ = 61.9 ft³      [GROUNDED, formula + stated count]
```
**Reality check:** this formula assumes airline-style 70 lb/2-bag checked baggage, which overstates what a private/VLJ passenger actually loads. HondaJet Elite II's real baggage volume (62 ft³) works out to ≈ 9.5 ft³/pax at typical 6.5-pax loading. Scaling that ratio to 6 pax gives ≈ 57 ft³ — **close to the worst-case formula result (61.9 ft³), and coincidentally almost exactly HondaJet's own absolute number.**

**Adopted target: 60 ft³**, split roughly nose (~10 ft³, in the rounded nose fairing behind the radome — now a more generous, less tip-starved volume than the ogive gave, per §6) + aft (~50 ft³, ahead of the tail-cone taper, alongside the enclosed lav). **ASSUMPTION** (split), **GROUNDED** (total, cross-checked two ways).

---

## 10. Fuel tank volume (Week 8 formula, Step 12)

```
W_F = W_TO × 0.2634 = 11,660 × 0.2634 = 3,071 lb   [config.md A.3, PLACEHOLDER-chain — see doubts.md #9]
V_f = m_f / ρ_f,  ρ_f (Jet A, mid) ≈ 800 kg/m³ (Table 7.9 range 775–840)
```
```
m_f = 3,071 lb = 1,393 kg
V_f = 1,393 / 800 = 1.741 m³ = 61.5 ft³ = 460 US gal
+6% expansion/unusable-fuel margin (ASSUMPTION) → 65.2 ft³ = 488 US gal
```
**Sanity check:** HondaJet Elite II's actual tank capacity is 468 US gal, and HondaJet Elite II carries 3,100 lb of fuel — both essentially identical to our required 460–488 gal / 3,071 lb, at nearly the same MTOW and wing area class. This number is only as solid as the L/D=12 and SFC=0.70 placeholders feeding `W_F` (doubts.md #9) — **if those get corrected, this whole section needs re-running before it's trusted past formula-level** — but it isn't an obviously-wrong figure.

### Can it all go in the wing, like the Phenom (and, notably, like HondaJet itself)?

**Real-world precedent says yes, mostly.** Two sourced data points:
- **Phenom 300** carries its full ~5,400 lb fuel load in **wing tanks only — no fuselage/center tank at all.**
- **HondaJet Elite** — the closer analog, since it's also OTWEM — carries fuel primarily in the wing, with only a small **90 lb supplemental center tank** (≈3% of its ~3,100 lb total). So OTWEM does not, in practice, force fuel out of the wing; Honda's own airframe proves wing-primary storage works with this exact engine-mount architecture.

**But a rough volume check on *our own* wing doesn't reproduce that easily**, and the discrepancy is worth being honest about rather than hand-waving past. Using B.1's current geometry (b ≈ 41.5 ft, AR 8.9, taper 0.35 → root chord 6.92 ft / tip chord 2.42 ft, t/c = 9.97%) and a simple spar-box volume estimate (front-to-rear-spar chord fraction ≈ 0.40–0.50, airfoil-cross-section/structure shape factor ≈ 0.65–0.85, usable span from the fuselage side out to 85% semispan):

```
Estimated usable wing-tank volume ≈ 17–28 ft³ (≈ 130–210 US gal)
Required (incl. 6% margin) ≈ 65 ft³ (≈ 488 US gal)
→ this crude estimate only covers ~26–43% of the requirement
```

**That's a real gap, but I don't think it's a real result** — it's more likely evidence that the box-fraction/shape-factor guesses in a five-minute hand integral are too conservative, not evidence that HondaJet's own architecture (nearly identical wing area, nearly identical required fuel weight, same OTWEM layout) is somehow infeasible for us. The right way to close this is a proper wing-tank volume calc using the actual SC(2)-0410 offset curves integrated between real spar station lines — not a box-volume guess — which is a legitimate follow-up, not a blocker.

**Recommendation:** design the fuel system as **wing-primary, HondaJet-style**, with a **small supplemental fuselage/center tank held in reserve** (following HondaJet's ~3% precedent, call it a placeholder ~100–150 lb / 2–3 ft³ contingency) rather than either (a) assuming the wing takes 100% with no fallback, or (b) defaulting to a large fuselage tank the way the generic Week-8 diagram suggests. This also resolves the "we can't have a tail tank" concern directly — the tail cone doesn't need to carry fuel at all under this architecture; it's needed for the enclosed lav (§4) and empennage/pylon structure instead, not competing with a fuel bay. **ASSUMPTION**, pending the real spar-box volume check. Logged as doubts.md #15, updated rather than closed.

---

## 11. Sanity checks against the wing

```
S_front = π·d²/4 = π·(6.1)²/4 = 29.2 ft²
S_front / S_wing = 29.2 / 193.7 = 15.1%
```
Typical business jets run fuselage-frontal-area-to-wing-area in roughly the 12–18% band — **15.1% is squarely inside that range.** GROUNDED (formula), reasonable-by-comparison (not benchmarked against a specific named aircraft here).

```
S_wet ≈ k·π·L·d,  k = 0.9 (ASSUMPTION, empirical non-cylinder factor)
S_wet ≈ 0.9 · π · 42.2 · 6.1 ≈ 728 ft²
```
Carried forward for a later parasite-drag buildup; not used yet.

---

## 12. Status summary / what this reopens in doubts.md

**Locked enough to proceed to OpenVSP lofting**, with the explicit caveat that every number below is ASSUMPTION or PLACEHOLDER-chain, not GROUNDED-from-constraint:

| Quantity | Value | Tag |
|---|---|---|
| Fuselage max external diameter, d | 6.1 ft | ASSUMPTION |
| Total length, L | 42.2 ft | ASSUMPTION (converged via 2 independent methods, within 1% of HondaJet Elite II's real 42.58 ft) |
| Cabin length / width | 13.0 / 5.5 ft | ASSUMPTION |
| Nose cone length | 10.4 ft | ASSUMPTION |
| Tail cone length | 18.8 ft | ASSUMPTION |
| Nose cap family | Rounded ellipsoid/paraboloid of revolution | ASSUMPTION — corrected 2026-08-04 from an earlier (wrong-for-this-regime) von Kármán ogive pick, see §1.3 |
| Nose cap profile | `r/R = sin[(π/2)(x/L_nc)^0.7]` | GROUNDED (formula; endpoint conditions exact) — replaces the `(x/L_nc)^0.6` power law lofted 2026-08-04, which broke tangency at the barrel. See §6 |
| Cabin barrel | **Constant 6.10 ft circular section, x = 10.4 → 23.4 ft (no waist)** | GROUNDED (measured decision, 2026-08-05) — see §8's boxed note, config.md D.5b, doubts.md #10 |
| Belly / wing-root fairing | 14.5 ft long (x = 16.0 → 30.5), 7.00 ft max width, 3.20 ft tall, bottom at z = −3.80, rounded-rectangle sections | ASSUMPTION (proportions), but it is the component that fixed the wing-root junction that had been corrupting the VSPAERO solve — see doubts.md #20 |
| Aft-body upsweep (as lofted) | 15.0° mean lower-line, x = 26.5 → 40.5 | GROUNDED to the loft; inside §7's 13–15° ASSUMPTION target, which is itself still gated on the missing landing-gear chapter |
| Pax / occupants | 6 pax + 2 crew = 8 total | **RESOLVED** — matches config.md A.3, no longer a conflict (doubts.md #1/#14 closed) |
| Enclosed lavatory | 3.0 ft, OTWEM-enabled | ASSUMPTION, new explicit differentiator |
| Upsweep angle | 13–15° | PLACEHOLDER (no gear chapter yet) |
| Baggage volume | 60 ft³ | GROUNDED-ish (cross-checked two ways) |
| Fuel volume | 65 ft³ / 488 gal, wing-primary + small supplemental tank | PLACEHOLDER-chain (inherits doubts.md #9); architecture backed by HondaJet/Phenom precedent but not yet by our own spar-box volume calc |
| Area-rule waist station | **None — waist removed** | **RESOLVED 2026-08-05**, and not by the CG chapter: it was resolved by measuring both lofts. See §8's boxed note. doubts.md #10 closed. |

**doubts.md status:** #1 and #14 (pax count) now **resolved** — this chapter matches config.md A.3. #15 (fuel tank architecture) is **updated, not closed** — real-aircraft precedent (HondaJet, same OTWEM layout, nearly identical fuel requirement) supports wing-primary storage, but this file's own rough spar-box estimate only accounts for ~26–43% of the required volume, so the gap needs a proper wing-offset-curve volume calc before this is trusted past "probably fine."
