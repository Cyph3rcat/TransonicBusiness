# Week 6 (3) — Wing Design: Part 3

*Converted from `lectureslides/Week 6 (3).pdf`. 17 slides. Content is bitmap; renders in `img/`.*


## Slide 1

![Week 6 (3) slide 1](img/week6_3_s01.png)

Text layer:

```
Wing Design: Part 3
```


## Slide 2

![Week 6 (3) slide 2](img/week6_3_s02.png)

Text layer:

```
vKnow the procedure of designing the wing
Learning Outcomes
```


## Slide 3

![Week 6 (3) slide 3](img/week6_3_s03.png)

Text layer:

```
Procedure
```


## Slide 4

![Week 6 (3) slide 4](img/week6_3_s04.png)

Text layer:

```
Procedure
```


## Slide 5

![Week 6 (3) slide 5](img/week6_3_s05.png)

Text layer:

```
Procedure
```


## Slide 6

![Week 6 (3) slide 6](img/week6_3_s06.png)

Text layer:

```
Sweep Angle Selection
See section 5.9 in Sadraey’s textbook for details
```

Transcribed content:

**Figure 5.38 — The effect of the sweep angle on the normal Mach number.** Swept wing at sweep Λ to the fuselage centreline; freestream Mach M resolves to a normal component `M·cos(Λ)` across the wing. Streamwise chord `C` becomes `C/cos(Λ)` measured normal to the quarter-chord line. Stagnation streamline shown with lateral curvature.


## Slide 7

![Week 6 (3) slide 7](img/week6_3_s07.png)

Text layer:

```
Sweep Angle Selection
```

Transcribed content:

μ = sin⁻¹(1/M)   (Mach angle)

Λ = 1.2 · (90 − μ)   (supersonic sweep rule of thumb)


## Slide 8

![Week 6 (3) slide 8](img/week6_3_s08.png)

Text layer:

```
Sweep Angle Selection
3. High subsonic: sweep enough such that the normal component of the
Mach number is under the critical Mach number of the airfoil
```

Transcribed content:

1. **Low subsonic aircraft.** If max speed is below Mach 0.3, no sweep is recommended — its disadvantages negate the improvement. 5 deg of sweep might cut drag ~2% but raise manufacturing cost ~15%. A straight wing is recommended.
2. **High subsonic and supersonic aircraft.** Initial value from Eq. (5.32) as a function of cruise speed. The final value is settled after aerodynamics, performance, stability, control, structures, cost and manufacturability analysis. A tapered wing must have some sweep anyway.
3. **High subsonic:** sweep enough that the normal component of the Mach number is under the critical Mach number of the airfoil.


## Slide 9

![Week 6 (3) slide 9](img/week6_3_s09.png)

Text layer:

```
Dihedral Angle Selection
From Sadraey:
“The balance between lateral stability and roll control is a major criterion for
the determination of dihedral angle.”
“In general, high-wing aircraft have an inherent dihedral effect while low-
wing aircraft tend to be deficient in their inherent dihedral effect. For this
reason, low-wing aircraft tend to have considerably greater dihedral angle
than high-wing aircraft. In contrast, swept wing aircraft tend to have too
much dihedral effect due to the sweep angle. This can be offset in high-wing
aircraft by giving the wing a negative dihedral (i.e., anhedral).”
```


## Slide 10

![Week 6 (3) slide 10](img/week6_3_s10.png)

Text layer:

```
101/27/2026
Dihedral Angle Selection
From Sadraey:
“You can select an initial value for the dihedral angle from this table.
However, the exact value of the dihedral angle is determined during the
stability and control analysis of whole aircraft. When other aircraft
components (e.g., fuselage, tail) are designed, evaluate the lateral stability of
the whole aircraft.”
```

Transcribed content:

**Sadraey Table 5.12 — Dihedral (or anhedral) angles for several aircraft.** Selected rows: Cessna 750 Citation X, business jet, low wing — **3 deg**; Falcon 900B, business jet transport, low wing — 0 deg 30 min; MD-11 jet transport low wing — 6; Boeing 767 low wing — 4 deg 15 min; Boeing 747 low wing — 7; Airbus 310 low wing — 11 deg 8 min; Pilatus PC-9 low wing — 7 outboard; F-16 mid-wing — 0; BAE Sea Harrier high wing — −12; C-130 high wing — 2 deg 30 min.


## Slide 11

![Week 6 (3) slide 11](img/week6_3_s11.png)

Text layer:

```
111/27/2026
Dihedral Angle Selection
From Raymer:
“Table 4.2, developed by the author from data taken from16l , provides
initial estimates of dihedral. For a wing in which the center section is flat
and the outer sections alone have dihedral, a first approximation of the
required dihedral for the outer panels is the one that places the wing tips
as high as they would be for a wing with dihedral starting at the root.”
```

Transcribed content:

**Raymer Table 4.2 — Dihedral Guidelines** (deg), by wing position:

| | Low | Mid | High |
|---|---|---|---|
| Unswept (civil) | 5 to 7 | 2 to 4 | 0 to 2 |
| Subsonic swept wing | **3 to 7** | −2 to 2 | −5 to −2 |
| Supersonic swept wing | 0 to 5 | −5 to 0 | −5 to 0 |

Quoted note: for a wing with a flat centre section and dihedral only on the outer panels, a first approximation is the dihedral that puts the tips as high as they would be with dihedral starting at the root.


## Slide 12

![Week 6 (3) slide 12](img/week6_3_s12.png)

Text layer:

```
121/27/2026
AR, Taper, Twist and Selection
Play with these parameters to minimize drag
Oswald efficiency factor e is equal to 1.0
for a wing with an ideal elliptical lift
distribution
```

Transcribed content:

C_Di = C_L² / (π · e · AR)

Oswald efficiency factor e = 1.0 for a wing with an ideal elliptical lift distribution. "Play with these parameters to minimize drag."


## Slide 13

![Week 6 (3) slide 13](img/week6_3_s13.png)

Text layer:

```
131/27/2026
AR, Taper, Twist and Selection
Having elliptical distribution has many other desirable properties:
```


## Slide 14

![Week 6 (3) slide 14](img/week6_3_s14.png)

Text layer:

```
141/27/2026
AR, Taper, Twist and Selection
Having elliptical distribution has many other desirable properties:
```


## Slide 15

![Week 6 (3) slide 15](img/week6_3_s15.png)

Text layer:

```
151/27/2026
AR, Taper, Twist and Selection
Large AR has desirable and undesirable properties: see section 5.6 in
Sadraey’s textbook
```

Transcribed content:

13. A shorter wing costs less to build than a long wing — for cost, low AR is desired.
14. As AR increases, aileron reversal becomes more likely since the wing is more flexible — for this reason low AR is desired.
15. In general, a rectangular high-AR wing is gust sensitive.


## Slide 16

![Week 6 (3) slide 16](img/week6_3_s16.png)

Text layer:

```
161/27/2026
AR, Taper, Twist and Selection
Regarding twist:
```

Transcribed content:

Two major goals for employing twist in wing design:
1. Avoiding tip stall before root stall.
2. Modification of the lift distribution to an elliptical one.

One unwanted output of twist:
3. Reduction in lift.

**Figure 5.48** — negative (wash-out) twist unloads the outboard wing, pulling the span load down near the tip relative to the untwisted case.


## Slide 17

![Week 6 (3) slide 17](img/week6_3_s17.png)

Text layer:

```
In Sadraey M. H., Aircraft Design: A Systems Engineering
Approach:
Chapter 5
In Raymer D. P., Aircraft Design: A Conceptual Approach:
Chapter 4
In Sforza, P. M., Commercial Airplane Design Principles:
Chapter 5
171/27/2026
Readings
```
