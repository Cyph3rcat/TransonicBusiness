# Raymer Ch.16 - Stability, Control, and Handling Qualities

*Converted from `Daniel P. Raymer - Aircraft Design_ A Conceptual Approach (2018, American Institute of Aeronautics and Astronautics Inc.) - libgen.li.pdf` by `tools/pdf_to_md.py`. Page markers are printed page numbers.*


<!-- p.585 -->

Stability, Control, 
and Handling 
Qualities 
• Sta bil ity and contr ol ar e addr essed dur in g layout with wing plac ement an d ta il sizing, 
but now we mak e rea l ca lculations to see if all is wel l. 
• Static mar gin is defi ned by geome try and mu st meet the chosen target. 
• Trim , pul l-up, and turn usua lly size ele vators, engi ne-out sizes rudder. 
• Also consider dynamic s and ftexi bil ity. 
Introd uction 
D uring early conce ptual design, the requirements for good stability, 
control, and handling qualities are addressed through the use of 
tail volume coefficients and the proper location of the wing with 
respect to the aircraft center of gravity (see Chapter 6). These rule-of-thumb 
methods result in a design that is probably as stable as desired and probably 
controllable as required. To make sure, a better analysis is required just as 
soon as pos sible. 
There are many ways to calculate stability. In larger aircraft companies, 
the aircraft is analyzed by the controls experts using a six-degree-of -freedom 
(DOF) aircraft dynamics computer program with inputs from computational 
fluid dynamics and/or wind-tunnel test. To really get the right answers, 
structural deflections must also be considered. This is time consuming and 
is probably not done until well into preliminary design. 
A lot can be learned from simpler aerodynamics analysis methods such as 
panel programs and Euler codes. Such methods give good answers for the 
static stab ility derivatives, asses sing things like whether the tails are big 
enough to keep the nose pointing the right directio n. 
585


<!-- p.586 -->

586 Air craf t Desi gn: A Conceptual Approach 
There are also classical stabi lity analysis methods, proven through 
decades of experience to give answers in the "right ballpar k." Of course 
these "handbook" methods are not as reliable as the modern comp utational 
methods, but they are suitable for initial assessm ents of a Dash-On e layout. 
This chapter intro duces the key concepts and equations for stability, 
control, and handling- qualities evaluation. These are based upon classical 
controls methods, many of which were developed by NACA in the period 
from 1925 - 1945. For derivat ions and additional detail on these methods 
see [15, 69, 11 6, 11 7] , and especi ally)13 •11 8l ' 
The basic concept of stab ility is simpl y that a stable aircraft, when disturbed, tends to return by itself to its original state (pitch, yaw, roll, velocity, 
etc.). "St atic stabil ity" is present if the forces created by the disturbe d state 
(such as a pitching moment due to an increased angle of attack) push in 
the correct direction to return the aircraft to its original state. 
If these restor ing forces are too strong, the aircra ft will overshoot the 
original state and will oscillate with greater and greater amplitude until it 
goes comple tely out of control. Although static stabilit y is present, the aircraft does not have "dynamic stabi lity. " 
Dynamic stability is present if the dynamic motions of the aircraft will 
eventually return the aircraft to its original state. The manner in which the 
aircraft returns to its original state depends upon the resto ring forces, 
mass distribution, and damping forces. Damping forces slow the restoring 
rates. For example, a pendulum swinging in air is lightly damped and will 
oscillate back and forth for man y minut es. The same pendulum immersed 
in water is highly damped and will slowly return to vertical with little or 
no oscillation. 
Figure 16.1 illustrates these concepts for an aircraft disturbed in pitch. In 
Fig. 16.la , the aircraft has perfectly neutral stab ility and simply remains at 
whatever pitch angle the disturbance produces. While some aerob atic aircraft 
are nearly neutral in stability, few pilots would care to fly such an aircraft on a 
long trip in gusty conditions. 
Figure 16.lb shows static instabil ity. The forces produced by the greater 
pitch angle actua lly cause the pitch angle to further increase. Pitch-up is an 
example of this. 
In Fig. 16 .lc , the aircraft shows static stability with very high damping. 
The aircraft slowly returns to the original pitch angle without any overshoot. 
Figure 16. ld shows a more typical aircraft response. The aircraft returns 
to its original state but exp eriences some converging oscillation. This is 
acceptable behavior provided that the time to converge is fairly short. 
In Fig. 16.le , the restoring forces are in the right direction, so the 
aircraft is statica lly stable. However, the resto ring forces are high, and the 
damping forces are relatively low, so the aircraft overshoots the original 
pitch angle by a negative amount greater than the pitch angle produce d 
by the distur bance. Restoring forces then push the nose back up, overshooting by an even greater amount. The pitch oscillations continue to increase


<!-- p.587 -->

CHAPTE R 16 Sta bil ity, Contr ol. and Handling Qua li ties 587 
a) Pe rfectly neu tra l 
a 
b) Stati cally un sta ble 
a 
ao - =f-=-- Time 
c) Sta ble, highly da mp ed d) Sta bl e, lig htly damp ed 
a a 
ao ao 
--!----- Ti me 
e) Stati cally sta ble , dyna mically 
uns ta ble 
a 
-t--.:---- Ti me 
--"Div ergen ce" 
Fig. 16 .1 Stat ic arid dyna mic stabil ity. 
in amplitude until the aircraft "diverges" into an unco ntrolled flight mode 
such as a spin. 
Note that instability is not always unacceptable provided that it occurs 
slowly. Most aircraft have at least one unstable mode, the spir al diver gence. 
This divergence mode is so slow that the pilot has plen ty of time to make the 
minor roll correction required to prevent it. In fact, pilots are generally 
unaware of the existence of the spiral- divergence mode because the minor 
corrections required are no greater than the roll corrections required for 
gusts. 
Dynamic -stability analysis is complex and requires comp uter programs 
for any degree of accurac y. Most of the stability- analysis methods presented 
in this chapter evaluate static stability. For conventional aircraft configurations, satisfaction of static -stability requirements will proba bly give acceptable dynamic stability in most flight modes. Rule- of-thumb methods are 
presented for stall depar ture and spin recovery, the dynamic- stabil ity areas 
of greatest concern. 
iiZ!1 Coordin ate Systems and Defi ni tions 
Figure 16.2 defines the axis systems common ly used in aircraft analys is. 
The "body axis system" is rigidly fixed to the aircraft, with the X axis 
aligned with the fuselage and the Z axis upward. The origin is at an arbitrary 
location, usually the nose. The body axis system is more natural for most 
people but suffers from the variation of the direction of lift and drag with 
angle of attack. (Remember that lift, by definition, is perpendicular to the 
wind direct ion.)


<!-- p.588 -->

588 Ai rc raf t Desig n: A Conc eptu al Appro ach 
Body 
axis 
x z 
Fig. 16 .2 Aircraft axis systems. 
x 
Pitch: Cm = M/qSc 
Yaw: Cn = N/qSb 
Ro ll: C1 = L/qSb 
No te: C1 f. li ft! 
The "wind axis system" solves this problem by orienting the X axis into 
the relative wind regardless of the aircraft's angle of attack a or side slip {3. 
The aircraft is not fixed to the axis system, so the axis projections of the 
various le ngths (such as the distance from the wing MAC to the tail) will 
vary for different angles of attack or sideslip. This variation in moment 
arms is us ually ignored in stabil ity analys is because the angles are typically 
small. 
For stability calculations, it is impor tant to make sure that the directions 
of rotat ions are consi stent with the directions of the axes. A "right- hand rule" 
must be maintained, or the equations will be unusable. If nose-up pitch is 
defined as pos itive, it follows that Y be directed out the right wing. Given 
the natural tendency to think of "right" as pos itive, roll to the right requires 
that Xi s forward, and yaw to right requires that Z be downwards! 
There is a problem with a pure wind axis system. When the airplane yaws, 
it becomes unsymmetrical about the X-Z plane. The coefficients would have 
to be incre dibly complicated to take this into account. 
Instead, the commo nly used "stability axis system" is defined as a compromise between these two approaches. The X axis is aligned at the aircraft 
angle of attack, as in the wind axis system, but is not offset to the yaw angle . 
This maintains the aircraft symmetry. The directions of X, Y, Z, and rotations 
are defined as in the wind axis system. 
Note that the rolling moment is called L. This is easi ly confused with lift. 
Also, the yawing moment is called N, which is the same letter used for the 
norma l-force coefficient. (The aerod ynamics crowd must have used up all 
the good letters by the time the stability folks developed their equations !)


<!-- p.589 -->

CH APTER 16 Sta bil ity, Control, and Handling Qua l ities 589 
Wing and tail inci dence angles are denoted by i, which is relative to the 
body-fixed reference axis. The aircraft angle of attack a is also with respect 
to this reference axis, so the wing angle of attack is the aircraft angle of 
attack plus the wing angle of incidence. 
Tail angle of attack is the aircraft angle of attack plus the tail angle of 
incidence, minus the downwash angle E, which is discussed later. 
Note that for stability calculations, angles of attack are us ually measured 
from the zero-lift angle as discussed in Chapter 12. Be careful: the airfoil 
moment data are proba bly tabulated with respect to the geometric chord 
line and might need to be adjusted to the zero- lift line. 
Nondimensional coefficients for lift and drag are defined by dividing by 
dynamic pressure and wing area. For stability calculations, the moments 
about the three axes (M, N, and L) must also be expressed as nondimensional 
coefficients. 
Because the mome nts include a length (the moment arm) , they must be 
divided by a quantity with dimension of length as well as by the dynamic 
pressure and wing area. This length quantity is the wing MAC chord for 
pitching moment and the wing span for yawing and rolling moments, as 
shown in Eqs. (16 .1 - 16.3). Posi tive moment is nose up or to the right. 
Cm = M/qSC 
Cn = N/qSb 
Cf! = L/qSb 
(16.1) 
(16.2 ) 
(16 .3) 
Stability analysis is largely conc erned with the response to changes in 
angular orientation, so the derivatives of these coefficients with respect to 
angle of attack and sideslip are critical. Subscr ipts are used to indica te the 
derivative. For example, Cn/3 is the yawing moment derivative with respect 
to sideslip, a very impo rta.nt parameter in lateral stability. 
Similarly, subscr ipts are used to indicate the response to control deflections, indicated by o. Thus, Cmoe indicates the pitchin g-moment response 
to an elevator deflection. 
Unless otherwise indicated, all sweep angles in this chapter are quarterchord sweeps, and all chord lengths c are the wing MAC. Also, all angles 
are in radians unless otherwise mentioned. Angle terms that are not estimated 
in radians must be con verted to radians before use in stability equat ions. 
!1 Long itud inal Static Stabil ity and Contr ol 
Mefll Pitch ing-M oment Equation and Tri m Calc ulation 
For most aircraft, mode rate changes in angle of attack will have little or 
no influence upon the yaw and roll and vice versa. This perm its the stabil ity 
and control analysis to be divided into longitudinal (pitch only) and lateraldirectional (roll and yaw) analysis.


<!-- p.590 -->

588 Air c raft De si gn: A Con ceptu al Approach 
Body 
axis 
x z 
Fig. 16 .2 Aircraft axis systems. 
x 
Pitch: Cm = M!qSc 
Yaw: Cn = N/qSb 
Rol l: C1 = L!qSb 
No te: C1 i- li ft! 
The "wind axis system" solves this problem by orienting the X axis into 
the relative wind regardless of the aircraft's angle of attack a or sidesli p /3. 
The aircraft is not fixed to the axis system, so the axis projections of the 
various lengths (such as the distance from the wing MAC to the tail) will 
vary for different angles of attack or sideslip. This variation in moment 
arms is usua lly ignored in stabilit y analysis because the angles are typically 
small. 
For stabilit y calculations, it is impor tant to make sure that the directions 
of rotations are consi stent with the directions of the axes. A "right-hand rule" 
must be maintained, or the equations will be unusable. If nose-up pitch is 
defined as pos itive, it follows that Y be directed out the right wing. Given 
the natural tendency to think of "right" as pos itive, roll to the right requires 
that X is forward, and yaw to right requires that Z be downwards! 
There is a problem with a pure wind axis system. When the airplane yaws, 
it becomes unsymmetrical about the X-Z plane. The coefficients would have 
to be incredi bly complicated to take this into account. 
Instead, the common ly used "stabil ity axis system" is defined as a compromise between these two approaches. The X axis is aligned at the aircraft 
angle of attack, as in the wind axis system, but is not offset to the yaw angle. 
This maintains the aircraft symmetry. The directions of X, Y, Z, and rotations 
are defined as in the wind axis system. 
Note that the rolling moment is called L. This is easily confused with lift. 
Also, the yawing moment is called N, which is the same letter used for the 
norma l-force coefficient. (The aerod ynamics crowd must have used up all 
the good letters by the time the stab ility folks developed their equations !)


<!-- p.591 -->

CH APTE R 16 Sta bil ity, Contr ol, and Handling Qu al ities 589 
Wing and tail inci dence angles are denoted by i, which is relative to the 
body-fixed reference axis. The aircraft angle of attack a is also with respect 
to this reference axis, so the wing angle of attack is the aircraft angle of 
attack plus the wing angle of incidence. 
Tail angle of attack is the aircraft angle of attack plus the tail angle of 
incidence, minus the downwash angle E, which is discussed later. 
Note that for stability calculations, angles of attack are usually measured 
from the zero-lift angle as discussed in Chapter 12. Be careful: the airfoil 
moment data are proba bly tabulated with respect to the geometric chord 
line and might need to be adjusted to the zero- lift line. 
Nondimensio nal coefficients for lift and drag are defined by dividing by 
dynamic pressure and wing area. For stability calculations, the moments 
about the three axes (M, N, and L) must also be expressed as nondimensiona l 
coefficients. 
Because the moment s include a length (the moment arm), they must be 
divided by a quan tity with dimension of length as well as by the dynamic 
pressure and wing area. This length quantity is the wing MAC chord for 
pitching moment and the wing span for yawing and rolling moments, as 
shown in Eqs. (16 .1 - 16.3). Pos itive moment is nose up or to the right. 
Cm = M/qSC 
Cn = N/qSb 
Cf = L/qSb 
(16.1) 
(1 6.2 ) 
(16.3 ) 
Stability analysis is largely conc erned with the response to changes in 
angular orient ation, so the derivatives of these coefficients with respect to 
angle of attack and sideslip are critical. Subscr ipts are used to indicate the 
derivative. For example, Cnf3 is the yawing moment derivative with respect 
to sideslip, a very impo rtant parameter in lateral stability. 
Similarly, subscr ipts are used to indicate the response to control deflections, indicated by 8. Thus, CmBe indicates the pitching -moment response 
to an elevator deflection. 
Unless otherwise indicated, all sweep angles in this chapter are quarterchor d sweeps, and all chord lengths c are the wing MAC. Also, all angles 
are in radians unless otherwise mentioned. Angle terms that are not estimated 
in radians must be con verted to radians before use in stability equations. 
EJ Long itud inal Static Stabili ty and Cont rol 
4ml Pitch in g-Moment Eq uation and Tri m Calcu lation 
For most aircraft, moderate changes in angle of attack will have little or 
no influence upon the yaw and roll and vice versa. This permits the stabil ity 
and control analysis to be divided into longitudinal (pitch only) and lateraldirectional (roll and yaw) analys is.


<!-- p.592 -->

590 Airc raf t De sign: A Con cep tual Approa ch 
Figure 16.3 shows the major contributors to aircraft pitching moment 
about the e.g., including the wing, tail, fuselage, and engine contributions. 
The wing pitchin g-moment contribution includes the lift through the wing 
aero dynamic center and the wing moment about the aerod ynamic center. 
Reme mber that the aerod ynamic center is defined as the point about 
which pitching moment is con stant with respect to angle of attack. This 
consta nt moment about the aerod ynamic center is zero only if the wing is 
uncamb ered and untwisted. Also, the aerod ynamic center is typically at 
25% of the MAC in subson ic flight. 
Another wing moment term is the change in pitching moment due to flap 
deflection. Flap deflection also influences the wing lift, adding to that term. 
Flap deflection has a large effect upon downwash at the tail, as discussed later. 
Drag of the wing and tail produces some pitching moment, but these 
values are negligibly small. Also, the pitching moment of the tail about its 
aerod ynamic center is small and can be ignored. 
On the other hand, the long moment arm of the tail times its lift produce s 
a very large moment that is used to trim and control the aircraft. While this 
figure shows tail lift upward, under many conditions the tail lift will be downward to counteract the wing pitching moment. 
A canard aircraft has a "nega tive" tail moment arm that should be applied 
in the equations that follow. If an aircraft is taill ess, the wing flap must be 
used for trim and control. Because of the short moment arm of such a 
control, the trim drags will proba bly be subst antially higher. 
Wing 
Propulsion 
Fp 
I 
I aP = a + iP + Eu I Xp 
L 
0 
Fig. 16 .3 Longitud inal momen ts. 
Aft propulsion 
aP = a + iP - E I


<!-- p.593 -->

CHAPTER 16 Sta bil ity, Co ntr ol, a nd Han dling Qu ali ties 591 
The fuselage and nacelles produce pitching moments that are difficult to 
estimate without wind-tunnel data. These moment s are influenced by the 
upwash and downwash produced by the wing. 
The engine produces three contributions to pitch ing moment. The 
obvious term is the thrust times its vertical distance from the e.g. Less 
obvious is the vertical force Fp produced at the propeller disk or inlet 
front face due to the turning of the freestream airflow. Also, the prop wash 
or jet-induced flowfield will influence the effective angle of attack of the 
tail and possi bly the wing. 
Equation (1 6.4) expresses the sum of these mome nts about the e.g. The 
-ffect of elevator deflection is included in the tail lift term. Equation (1 6.5) 
-xpresses the moments in coefficient form by dividing all terms by (qSwc) 
ind expressing the tail lift in coefficient form. Note that, to facilitate 
mderstanding, these equations are defined in the body axis coor dinate 
;ystem rather than the stability axis system. 
Meg = L(Xcg -Xacw) + J\1w + Mwof DJ + Mfus -Lh(Xach -Xcg) - Tzt + Fp(Xcg -Xp) (16.4 ) 
This equation in coefficient form has a term representing the ratio 
ietween the dynamic pressure at the tail and the freestream dynamic 
iressure, which is defined in Eq. (16 .6) as T/h· This ranges from about 
1.85 -0.95, with 0.90 as the typical value. 
To simplify the equations, all lengths can be expressed as a fraction of 
he wing mean chord c. These fractional lengths are denoted by a bar. 
['hus, Xcg represents Xcg/ c. This leads to Eq. (16 .7). 
(16.5) 
(16.6 ) 
Cmcg = CL(Xcg -Xacw) + Cmw + CmwoJOf + Cmfus 
Sh - - T - Fp - -- TJh-5 CLh(Xac h- Xcg)- -5 Zt +-5 (Xcg -Xp) w q w q w (16.7 ) 
For a static "trim" condition, the total pitching moment must equal zero. 
or static trim, the main flight conditions of concern are during the takeoff 
nd landing with flaps and landing gear down and during flight at high 
-ansonic speeds. Trim for the high-g pull -up is actually a dynamic 
roblem (discussed later) . Usually the most forward e.g. position is critical 
>r trim. Aft-c.g. position is most critical for stability, as discussed next.


<!-- p.594 -->

592 Aircr aft De sign: A Conceptual Approach 
Equation (16 .7) can be set to zero and solved for trim by varying sorne 
parameter, typically tail area, tail lift coefficient (i.e., tail incidence or elevator 
deflectio n), or some times e.g. posi tion. The wing drag and tail trim drag can 
then be evaluated. Methods for the first-order evaluation of the terms of 
Eq. (16 .7) are presented later. 
4fiff J Static Pit ch Stabil ity 
For static stability to be pres ent, any change in angle of attack must generate moments that oppose the change. In other words, the derivative of 
pitching moment with respect to angle of attack [Eq. (16 .8)] must be negative. 
Note that the wing pitching moment and thrust terms have dropped out, as 
they are essen tially constant with respect to angle of attack. 
Because of down wash effects, the tail angle of attack does not vary directly 
with aircraft angle of attack. A derivative term accounts for the effects of wing 
and propeller downwash, as described later. A similar derivative is provided 
for the propeller or inlet normal-force term Fp. - - sh 8ah - -Cma = Cr)Xcg -Xacw) + Cmafus - Y/h Sw Cr"h oa (Xach -Xcg) 
Fp Bap - -+ s"-(Xcg -X p) q w ua (16.8 ) 
Equation (16 .8) seems to offer no mechanism for stabilizing a tailless aircraft ("flying wing") . In fact, the tailless aircraft must be stabilized in the first 
term by providing that the wing aerod ynamic center is behind the e. g., 
making the first term negative . 
The magnitude of the pitchin g-mo ment derivative [Eq. (16 .8)] changes 
with e.g. loc ation. For any aircra ft there is a e.g. location that provides no 
change in pitching moment as angle of attack is varied. This airplane aerodynamic center, or neutral point Xnp, represents neutral stabil ity (Fig. 16.la ) 
and is the most-aft e.g. location before the aircraft becomes unstable. 
Equation (16 .9) solves Eq. (16 .8) for the neutral point (Cm" = O). Equation 
(16.10 ) then expresses the pitchin g-moment derivative in terms of the distance in percent MAC from the neutral point to the e.g. This perc entage distance, called the "static margin," is the term in parentheses in Eq. (16. 10). 
sh Bah - F Per Bap -CraXacw -Cmafus + YJh5-Cr"h -Xach +-5 -Xp w ua q w ua Xnp = -------------,-------, ,,,-------Sh Bah Fp" Bap Cr + YJh-CL -+- -" Sw "'' Ba q Sw Ba 
- - ( - B-) - -Cm" = -Cr"•ota1 (Xnp -Xcg) = - Cra + Y/h Sw Cr"h Ba (Xnp -Xcg) 
(16. 9) 
- -CrJXnp -Xcg) (16. 10)


<!-- p.595 -->

CHAPTE R 16 Sta bil ity, Contr ol, and Handling Qual ities 593 
- - Cm Static Margin (SM) = (Xnp - Xcg) = - __ a cla (1 6.11 ) 
The static margin is the most impor tant term in the longitudinal stab ility 
of an aircraft, and a target static margin, usually expressed in percent, is both 
a requirement and a key design tool for aircraft designers. Static margin can 
also be calculated as the ratio between pitchin g-moment derivative and lift 
coefficient derivative. 
If the e.g. is ahe ad of the neutral point (pos itive static margin), the 
pitching-moment derivative is negative, so the aircraft is stable. (This is yet 
another confus ing terminolog y.) At the most aft e.g. position, a typical transport aircraft has a pos itive static margin of 5 -1 0%. General aviation designs 
are even more stabl e. The Cessna 172 has a static margin of about 19%! 
Earlier fighters typically had pos itive static margins of about 5%, but 
newer fighters such as the F- 16 , F-22, and F-35 are being designed with 
"relaxed static stability" (RSS) in which a negative static margin (zero to 
-1 5%) is coupled with a computerized flight control system that deflects 
the elevator to provide artificial stability. This reduces trim drag subst antially. 
It is common to neglect the inlet or propeller force term Fp in Eq. (1 6.9) 
to determine "power-off' stabili ty. This removes any strong dependence of 
Xnp on velocity in the subsonic flight regime. Power effects are then 
accounted for using a static -margin allowance based upon test data for a 
similar aircraft. Typically, these allowances for power-on will reduce the 
static margin by about 1- 3% for jets. For propeller-po wered aircraft, every 
mean aerodynamic chord length that the propeller is ahead of the center 
of gravity will reduce the stabili ty by about 2%. 
-1.6 
-1. 4 
-1. 2 
c 
re 
'6 
-1. 0 
Qj -0.8 0. 
-0.6 u 
-0.4 
-0.2 
0 
0 0.5 
• B-747 
• B-727 
Tra nspor t 
Busine ss and 
general aviation 
Fig hte r-sta ble 
• F-4 e F-4 
1. 0 1.5 2.0 
Mach numb er 
2.5 
Fig. 16 .4 Typical pitchi ng-moment derivative valu es. 
3.0


<!-- p.596 -->

594 Ai rcraf t De si gn: A Conc ept ual Approach 
Figure 16 .4 illustrates pitchin g-moment-der ivative values for severa 
classes of aircraft. These can be used as targets for conc eptual design 
Dynamic analysis during later stages of design can revise these targets . 
The evaluation of the terms in Eqs. (16 .7 - 16 .9) is difficult without wind. 
tunnel data. Various semi- empir ical methods are presented next, primaril) 
based upon fi3 ,37,ns ,n9J . Note that these methods are consi dered crude b) 
the stability and control commun ity and are only suitable for conceptual 
design estimates and for student design projects. 
4tfU Aerody namic Cent er 
A critical term in Eq. (1 6.7) is Xacw' the loca tion of the wing aerodynamic 
center. For a high-aspect- ratio wing, the subsonic aerod ynamic center will 
be loca ted at the percent MAC of the airfoil aerod ynamic center. For most 
airfoils this is the quarter-chord point (plus or minus 1 %). At supers onic 
speeds the wing aerod ynamic center typically moves to about 45% MAC. 
Figures 16 .Sa - 16.Sc provide graphical methods for aerod ynamic center 
estimat ion. f67,37J Note that poor results are obtained at transonic speeds. 
These methods are also used for estimating the tail aerod ynamic center. 
A quick approximation of the shift of aerod ynamic center with increasing 
Mach number is given in Eq. (16 .1 2). For a better estimate at supe rsonic 
speeds, even an old aerod ynamic code such as the classic Woodward Panel 
Program will give a good answer, but today many people jump right to a 
CFD analysis. 
Xac = Xc/4 + l:!..xacwhere 
6.xac = 0.2 6 (M - 0.4 )2·5 
6.xac = 0. 11 2 - 0. 004M 
Mf.fll Wing and Tail Lift , Flap s, and El evato rs 
(16. 12) 
(0.4 < M < 1.1 ) 
(M > u; 
The lift-c urve slopes of the wing and tail are obtained with the methods 
presen ted in Chapter 12. The tail lift-c urve slope should be reduced about 
20% if the elevator gap is not sealed. 
The lift coefficients for the wing and tail are simply the lift-c urve slopes 
times the wing or tail angle of attack (measured with respect to the zero- lift 
angle). These are defined in Eqs. (16.13) and (16.14 ) based upon the angleof-attack definitions from Fig. 16 .3. Note that for cambered airfoils, the zerolift angle is a negative value. Also, the tail angle of attack must account for the 
downwash effect E, which will be estimated later [Eq. (1 6.2 4)]. 
Wing: 
(16 . 13)


<!-- p.597 -->

a) 
x •. c. 
c,. 
b) 
x •. c. 
c,. 
CHAPTER 16 Sta bil ity. Control. and Handling Qu al ities 595 
1.2 rTT I i 
1.0 
0.8 
0.6 
I J....'<!i 
: 
',A tan AL£ 
A tan Au :.-- -/ 6I<:-= - 16.J.-- _,... / 4----unswept T .E. ' ' 3 J-- -· -- I - ......_ 2 
0.4 I .-- l 
I L -r I --0.2 ...;- 1 
I I 
0 I Subsonic- ,._ --S up ers onic 
0 0 1 0 
tan ALE 
/3 
1. 4 
I 
1.2 I 
I 
1.0 
- -n ALE 
_......., 
0.8 51 
4 1 
0.6 
- ' 
-3 
0.4 -·- ; 
i I 
0.2 ' 
I 
0 
' 
0 
/3 /3 tan ALE 
tan ALE tan ALE /3 
- A tanlLE 
/ L<i 
_v ,_. 5 - ,;1 
_,.., C:/ 
4---i J? 1 
__j.- i/ 1 
I .... r 
U nswept T.E . v- ---J_ ' 
: 
I 
Subsonic 
,.;;r"-- __ _w-I __ i.---r 
--+ Super so nic 
0 1 0 
A = 0.05 tan ALE f3 f3 tan ALE 
c) 
x •. c. 
c,. 
1.6 
1.4 
1.2 
1.0 
0.8 
0.6 
0.4 
0.2 
0 
0 
/3 
; I 
! 
A tan AL; 6 i 
1-1 
! A 
'3 
! 
I ? 
' 
I 
I I 
I 
I 
i 
A = 0.5 tan ALE 
/3 
tan ALE tan ALE f3 
/ 
v 
vI 
I 
/I 
II 
.,;/ I 
-·1 1 
c: I - l 
- I 
I I I 
A tan ALE 
V-r---. 6 
v-r----._I!:> 
4,3 
,.,.2 
L7 I e-- -Uns wept T.E. I -____ i.-1 
I 
Subsonic /3 
-r---v I 
I 
lo-f--t - Su perso nic 
0 1 0 
/3 tan ALE 
tan ALE tan ALE /3 
Fig. 16 .5 Wing aer odynamic center. 1691


<!-- p.598 -->

596 Ai rcraf t De si gn: A Concep tual Approach 
Aft tail: 
where aoL is the angle of attack for zero lift, which is a negative value for , 
wing or tail with pos itive camber and/or downward flap/ elevation deflection 
The elevator acts as a flap to increase the tail lift. Flap deflec tion al 
moderate angles of attack does not change the lift-c urve slope, so the lifi 
increment due to flaps can be acco unted for by a reduction in the zero-lifi 
angle (i.e., more negative). This reduction in zero- lift angle is equal to thE 
increase in lift coefficient due to flap deflection divided by the lift-cu rve slope 
11CL 11aoL = --CL,, (1 6.1 5) 
For the complicated high-lift devices seen on most transpor t wings, the 
increase in lift coefficient can be approximated using the methods in 
Chapter 12 or from Fig. 5.3. The change in zero-li ft angle can then be determined from Eq. (16 .15 ) and applied to Eq. (16.13 ). 
Plain flaps are used for a modest increase in wing lift and as the control 
surfaces (elevator, aileron, and rudder) for most aircraft. The change in 
zero- lift angle due to a plain flap is expressed in Eq. (16. 16 ), where the lift 
increment with flap deflection is expressed in Eq. (1 6.17 ). The 0.9 factor is 
an approximate adjustment for flap tip losses 
where 
( 1 8CL) 11aoL = -CL,, 881 81 
8CL (8Ce) Sflapped 
88 = 0.9Kf 88 S cos AH.L . 
'f 'f airfoil ref 
(16. 16) 
(16. 17) 
Figures 16 .6 and 16 .7 provide the theoretical airfoil lift increment for flaps 
at small def lections and an empirica l adjustment for larger deflections. A 
typical flap used for control will have a maximum deflection of about 
30 deg. Flap deflection must be converted to radians for use in Eq. (16.16 ). 
(Note that L is lift in these equatio ns.) 
This empirically corrected theoretical method from [69l sometimes 
overpredicts the flap or control surface effectiveness, implying that a flap 
deflection gives even more lift than an equal-incidence deflection of the 
entire wing or tail. This should not norma lly occur and can be avoided by 
ensuring that the product of the first two terms in Eq. (16. 16 ) is less than 
1. Equation (16.18 ) is a purely empirical expression of data from [82l that 
provides a reasonable upper limit on the surface effectiveness terms, and it


<!-- p.599 -->

CHAPTE R 16 Sta bil ity, Contr ol, and Handling Qual ities 597 
tic 
6 
.------------------ 0.15 
0.12 0.08 0.04 
5 
(ace) 4 
\a81 
(pe r rad) 
3 
2 
0.00 
0 0.1 0.2 0.3 0.4 0.5 
Fig. 16 .6 Theore tical lif t in crement for plain flops. 1691 
1.0 r-------.-----,----------,---------, 
0.8 
c/c 
0.6 
0.10 
0.15 
"' "--, "" - 0.20 
0.25 
0.30 
0.40 
0.4 
0.50 
0.2 t 
- i 
I 
t 
--+- ·· 
20 40 60 80 
Flap de flec tion, 81 (deg) 
Fig. 16 .7 Empir ical correc tion for plain flop lif t inc rement 1691


<!-- p.600 -->

598 Aircr aft Desi gn: A Conceptual Approach 
can be applied to Eq. (16.15). 
-aoL __!___._ 8Cr 
8e Cra 88! 
= l.5 76(Cj/C)3-3.458(Cf /C)2 + 2. 882( C 1/C) (1 6.18 
Figure 16 .8 defines the geom etry for these equat ions. H.L. refers to th1 
flap hinge-line sweep, and Sflapped refers to the portion of the wing or tai 
area with the flap or control surface. The MAC of the flapped portion 0 
the wing or tail c' is determined geome trically by con sidering the flappec 
portion as a sep arate surface. 
If a flap, elevator, rudder, or aileron has an unsealed hinge gap, the effective 
ness will be reduced because of the air leaking through the opening. Thi: 
reduction will be appro ximately 15% of the lift increment due to flap deflection 
These flap lift approximations are reasonable at low Mach numbers. A 
higher speeds flap lift tends to follow the trends of Fig. 12 .6, so as a rougapproximation one can adjust flap lift by Cra at the given Mach, divided bJ 
Cra at Mach 0. 
4f.flj Wing Pit ch ing Momen t 
The wing pitching moment about the aerod ynamic center is largel1 
determined by the airfoil pitching moment. Equation (16 .19 ) provides ar 
adjustment for wing aspect ratio and sweep for a straight wing or ar 
untwisted swept wing at low subson ic speeds. The wing twist adds an incre· 
ment of approxima tely ( -0 .01) times the twist (in degrees) for a typical swep1 
wing. A more detailed estimatio n of the wing twist effect is available in[69l 
Transonic effects increase the magnitude of the wing pitching moment b} 
Fig. 16 .8 Flapp ed area and flapp ed MAC (c ').


<!-- p.601 -->

CHAP TER 16 Sta bil ity. Contr ol, and Handling Qual ities 599 
8 Flap li ft 
center of 
pre ssur e 
0.50 
0.45 
Sl otted flap s 
Xcp 0.40 
c , 0.35 
0.30 
0.25 0 0.2 0.4 0.6 0.8 
Fla p-chor d ratio (c1!c) 
Fig. 16 .9 Center of pressure for li ft in crement due to flaps (after. 1691) 
about 30% at Mach 0.8. 
( A cos 2 A ) Cm =C m w Oaicfoil A + 2 COS A 
1.0 
(16. 19) 
The pitching -moment increment due to flap deflection is approximated 
as the lift increment due to the flap times the moment arm from the center 
of pressure of the flap lift increment to the e.g. [Eq. (1 6.20 )]. The center of 
pressure of the flap lift increment (Xcp) is determined as a percent of 
the flapped MAC (c') using Fig. 16 .9. The first term comes from Eq. (16.17 ). 
· 
8Cr - Cmwof = - 00 (Xcp - Xcg ) 
'! 
(16.2 0) 
For a highly swept wing the center of pressure of the flap lift increment 
can be ahead of the e.g., creating a pos itive moment increment. This 
reduces the download required by the tail. Conversely, a canard configuration 
will put the center of pressure of the flap lift increment well behind the e.g., 
requiring a huge balancing force. 
4t!D Downwash and Upwash 
The remaining terms in Eq. (16 .7) are strong ly influenced by the wing 
flowfield, as shown in Fig. 16.10. Ahead of the wing, the air in subson ic 
flight is pulled upward by the reduced pressures above the wing. This 
upwash pushes upward on the fuselage forebod y and also turns the flow 
prior to reaching a propeller or inlet loca ted ahead of the wing.


<!-- p.602 -->

600 Ai rc raft Des ign : A Concept ual Appr oa ch 
Fig. 16 . 10 Wing tlowfield effect on pi tch ing mome nt. 
Behind the wing, the flow has an initial downward direction theoreticall} 
equal to the wing angle of attack. This downwash angle diminishes aft ol 
the wing to a value of approxi mately half the wing angle of attack at thE 
tail of a typical aircraft. Also, the downwash varies across the span and 
approaches zero near the wing tips. 
The downwash reduces the tail angle of attack and pushes downward on 
the aft fuselage, contributing to the fuselage pitching moment. Downwash istro ngly affected by the prop wash. 
The upwash- angle Eu derivative with respect to wing angle of attack is 
determined from Fig. 16 .11. The downwash angle E derivative is determined 
from Fig. 16. 12 at low subs onic speeds (unswept wing) . The spanwise 
variati on in downwash behind the wing reduces the average downwash 
experienced by the tail by approxima tely 5%. The additional downwash 
due to flap deflection is determined from Fig. 16. 13 in which h is the tail 
height above the wing. 
At transonic speeds (around Mach 0.9) the downwash- angle derivative 
increases by about 30 -4 0% then reduces at higher speeds. Equatio ns 
(16 .21) provide a rough approximation of the downwash at high subsonic 
and supersonic speeds. 
Subsonic: 
Supersonic: 
OE 
aa 
(16. 2la ) 
(1 6.2l b) 
The resulting angle of attack consi dering the effect of upwash or downwash is determined by adding an upwash or subtract ing a downwash from


<!-- p.603 -->

CHAPTER 16 Sta bil ity, Contr ol, and Handling Qual ities 60 1 
the freestream angle of attack. The angle- of-attack derivatives are therefore 
as expressed in Eqs. (1 6.22) and (16 .23). Equation (1 6.23) is the tail 
angle-of-attack derivative from Eq. (16 .8), called f3 in many texts, which is 
easily confused with yaw angle. The downwash derivative is with respect to 
the wing angle of attack, so the tail angle of attack can now be determined 
as shown in Eq. (1 6.24) . 
Vpwash: 
Down wash: 
8au 8Eu - = 1+ -8a 8a (16 .22) 
(16 .23) 
(16 .24) 
A canard will obviously experience no downwash from the wing, but 
its own downwash will influence the wing. The estimation of the effect of 
canard downwash on the wing is very difficult because the downwash 
2.0 --t--------------.,-------t-1.6 I + 
I , 
1.2 A 
+ 
0.8 
0.4 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
t 
o --------------'-· :::::::;oo==:==:::::=::::-.J 
2.0 1.6 1.2 0.8 0.4 0 -0.4 
Dis ta nce forward of root quar ter -c hor d point in root chords 
Fig. 16 .1 1 Upwash esti mation (subsonic onl y). 1691 
-0.8


<!-- p.604 -->

602 Ai rcraf t Des1g . 1 Appr oach . n· A Concep tua 
de 0.7 
da 0.6 
II 
<"<! 
A=6 
m 
-: -:: -l"' 0.5 ·2 ci 0.4 - 0.3 
0.2 
m 
0 
A = 9 
8:- o.- 0.2 --=:::::::::: 
m 
de 0.7 0 o.-21- a:- ': :: - 02
- ci 0.4 
- 0.3 
Wing 
Tail Geome try 
/ Zi 
O.- 0.2 ----=:::::::::: 
zero lif t 
angle of atta ck 
. 
= o) (afte r[l 3l). ash esti mation (M Fig. 16 .12 Downw 
d tip vortices actually the canar d because nard span an 
f the canard. 
roximated 
varies across th--the wing outbo"';-eo wing can be crudely a!-thods uni· cceate an upwacanacd downwash onh 
as cfilculated with thde-:s the angle of 
The effect o 
a<d downwas 
d tips. This re u 
. g that the can 
d f the canar 
by assumm 
he wing inboar o formly affects t . t 
k at the wmg roo . attac


<!-- p.605 -->

CHAP TER 16 Stabil ity, Contr ol, and Handling Qual ities 603 
fDBU Wing Vertic al Position 
The vertical position of the wing also has an effect on stability. This is easy 
0 visualize-if the nose comes up on a high wing configuration, and the wing 
:ctually moves to the rear relative to the center of gravity and thus provides 
'.n additional nose- down pitching moment. As a rough approximation, it can 
1e assumed that a high wing increases the static margin by 10% of the vertical 
[istance of the wing above the e.g., divided by wing MAC. 
ftl:I Fuselage and Nac elle Pitch ing Moment 
The pitching-moment contributions of the fuselage and nacelles can be 
pproximated by Eq. (16 .25) from NACA TR 711. The WJ- is the maximum 
iidth of the fusela ge or nacelle, and Lf is the length. Figure 16.14 provides 
Ile empirical pitchin g-moment factor Kfus· 
Kfus W}L! 
Cmaruse1age = cSw per deg (16 .25) 
1efp Th rust Effects 
The remaining terms in Eq. (16 .7) are thrust effects upon pitching 
10ment. Thrust has three effects, namely, the direct moment of the 
(LiE )A (b/(b/2)] 
Li Cr 
-0.2 -0. 1 
15 
10 
5 
0 0.1 0.2 0.3 0.4 
hh is horizonta l 
ta il height 
ab ove wing 
0. 5 (_!!!!_ ) b/2 
Fig. 16 .13 Downwash inc rement due to flaps.


<!-- p.606 -->

604 Air c raf t De si gn: A Conceptual Approach 
0.05 
0.04 
0.03 
0.02 
0.01 NACA TR 71 1 
O -t----t----t---+---t----i---10 20 30 40 50 60 
Pos ition of root qua rte r-c hor d as pe rce nt of fuselage length 
Fig. 16 .14 Fuselage moment term . 
thrust, the propeller or inlet normal force due to turning of the air, and thi 
influence of the propwash or jet-induced flows upon the tail, wing, anc 
aft fuselage. 
The direct moment of the thrust is simply the thrust times the momen 
arm about the e.g., as defined in Eq. (16 .7). If the thrust axis passes through 01 
near the e.g., this term can be ignored. 
The normal force due to the turning of the air at an inlet front face F1 
can be calculated from momentum consi derat ions. This normal fom 
equals the mass flow into the inlet times the change in vertical velocity 
Because the angles are small, the change in vertical velocity is approximate!) 
the turning angle (ap-see Fig. 16.3) times the aircraft velocity [Eq. (16.26)] 
The engine mass flow can be approximated by assuming a capture- area ratic 
of one [Eq. (1 6.27)] if installed engine mass-f low data are unavail able. NotE 
that in British units the mass flow is in slugs per seco nd, which equah 
pounds per second divided by 32.2. 
Fp = rhV tan ap - rhVap (16 .26; 
rh - pVAinlet (16. 27; 
(16. 28) 
The derivative of the normal force with respect to angle of attack ithe mass flow times the velocity [Eq. (1 6.28 )]. The derivative of ap with 
respect to angle of attack [see Eq. (1 6.9)] is the upwash derivative


<!-- p.607 -->

CH APTE R 16 Stabil ity, Contr ol, and Handling Qu al ities 605 
£q. (16.22) if the inlet is ahead of the wing and the downwash derivative 
£q. (16.23) if the inlet is behind the wing. For an inlet mounted under the 
wing, the wing turns the flow before it reaches the inlet front face so that 
the normal force is approximatel y zero. 
for a propelle r-po wered aircraft, a normal force contribution to pitching 
moment is also produced by the momentum change caused by the turning of 
the airstream. Unlike the jet inlet, the actual turning angle is not apparent 
because the propeller does not fully turn the airflow to align with the 
propeller axis. 
Equation (1 6.29) is an empi rical method for estimation of the propeller 
normal force based upon charts inf11 9l ; NB is the number of blades per 
propeller, and Ap is the area of one propeller disk. The derivative term is 
the normal force exerted by one blade when the propeller is oper ating at 
zero thrust, found in Fig. 16.15 as a function of advance ratio. The function 
j(T) adjusts for nonzero thrust and is found in Fig. 16.16. 
F = qN A 8CNb1ad•j(T) 
Pa B P 8a (16 .29) 
Note in Eq. (1 6.7) that a propeller mounted aft of the e.g. is stabilizing. 
This is one of the advantages of the pusher-propeller configuratio n. 
The propwash affects the downwash seen by the horizontal tail and 
reduces the tail's effectiveness. Equation (1 6.30) estimates this propeller 
downwash effect as a derivative that is added to the wing downwash 
0.125 (At th rust = 0) 
dCNblade da 
'O .ro 'O 
:0 cu cu 
0.10 0 
0.0 75 
0.050 
0.025 
0 
+--->-- --+---+---+--___,,__ Adva nce 
O 1 2 3 4 5 ratio 
Referenced to prop eller 
disk ar ea ! = J!_ nD 
Fig. 16 .15 Prope ll er norma l force coefficient (ofter l1 1 9l).


<!-- p.608 -->

606 Ai rcraf t Desig n: A Conc eptu al Appr oach 
derivative. The constant terms come from Fig. 16.17. 
___!?_ = /( + /(. N 
blade __ 
OE acNi (Oap) oa 1 2 B oa oa (16.3 0: 
If largely in the prop wash, the tail will experience an increased dynamic 
press ure, as sh own in Eq. (16. 31) . The tail dynamic pressure ratio T/h fo1 
zero thrust is approximately 0.9. If the tail is only partly in the propwash 
the right-side term in the parentheses should be reduced propor tionately. 
This term can also be applied to estimate increase in dynamic pres sure at 
the wing, which might especia lly affect the pitching moment due to flap 
deflecti on. 
(16 .31) 
The increase in dynamic pressure at the tail will increase the magnitude 
of the tail lift that, being downward in most cases, causes a nose-u p trim 
change with application of power. It is not uncommon in single- engine 
propeller aircraft to incline the propeller axis several degrees downward to 
counteract the power effect upon trim. 
4f#lll•1 Tri m Analy sis 
We now have all of the information required for trim analysis. Trim 
requires that the total moment about the e.g. [Eq. (1 6.7)] equals zero. For a 
h 
......., 
2.00 
1. 75 
1. 50 
1. 25 
1. 00 
0.75 +--___,l------+----+----+---1------+-0.5 0 0.5 1.52 2.0 
Fig. 16 .16 Propeller nor mal force factor (atte rf1 1 9l). 
2.5


<!-- p.609 -->

"' 
£ u 
"' u.. 
0.5 
0.4 
0.3 
0.2 
0.1 
CHAPTER 16 Sta bil ity, Contr ol, and Handling Qual ities 607 
After NACA WR L-25 
O +----t-----t----+----+---+----+-0.5 0 0.50 1. 50 2.00 
Fig. 16 .1 7 Propeller downwash factor s (after 111 9l). 
2.50 
ven flight condition, we can determine the values in the equation and see 
they sum to zero. If not, we can vary the tail lift by changing elevator 
-flection or tail incidence until the total moment is zero. 
However, the change in tail lift will change the aircraft total lift, which 
ust equal the weight. Therefore, as the tail lift changes, the aircraft angle 
' attack must change. This can be solved by a computerized iterative 
'.ocess or by a graphical technique. 
For the graphical solution, arbitrarily assumed aircraft angles of attack 
id elevator deflection angles 0£ are used to calcu late the total-pitching.oment coefficient Cmcg using Eq. (1 6.7) . Equation (16 .32) is used to deterine the tail- lift term. 
Crh = Crah [(a+ iw) (1 - ::) + (ih - iw) - aorh] 
. sh Crtotal = Cra [a + tw] + Y/h Sw Crh 
(16.3 2) 
(16. 33) 
For the arbitrarily assumed angles of attack and elevator deflection, 
e total lift coefficient Crtotat can be estimated using Eq. (16 .33). This 
1uation sums the wing and tail lift coefficients, including the effects of 
·namic pressure at the tail. Remember that by definition an upload on 
e tail is posi tive. If a download exists on the tail, the tail lift reduces 
e total lift.


<!-- p.610 -->

608 Air c raf t Des ign: A Conceptual Approach 
The total- pitching- moment coefficient is then plotted vs the total lift 
coefficient for the various elevator-de flection angles. The elevator deflection for trim is determined by interpolating for zero pitching moment 
at the required total lift coefficient. This is illustrated in Fig. 16.18 . 
The total induced drag including trim-drag effects can now be calculated 
at the trim angle of attack and elevator deflection angle using Eq. (1 6.3 4). 
Note that the term Kh is the drag- due-to-lift factor for the horizon tal tail. 
This is determined using the methods of Chapter 12, treating the horizontal 
tail as a wing. Because the tail's induced drag is much smaller than the 
wing-induced drag, it is permissible to use the simpler empirical methods 
Ca lcu lation ta ble 
a= Od eg cm = 0.033 cg 
cltotal = -0.07 
a= 5 deg c mcg 
= 0.012 
cltotal = 0.53 
a= lO deg cm = -0.005 cg 
cltotal = l.03 
Trim crossplo t 
0.06 Calcu la ted point s 
0.04 I 
0.02 
0 
-0.02 
-0.04 
0 0.2 0.4 0.6 0.8 
O deg 
0.018 
-0.05 
-0.004 
0.54 
-0.021 
1.04 
Trim 
points 
1.0 
Wli+M 
1.2 
0.002 
-0.03 
-0.02 
0.56 
-0.038 
1.06 
OE 
-2 deg 
O deg 
2 deg 
cltotal 
(N ote: Pos iti ve oE as de fin ed prod uc es an upload on the ta il. ) 
Fig. 16 .18 Graphical tri m ana lysis.


<!-- p.611 -->

CHAPTER 16 Stabil ity, Control. and Handling Qua lities 609 
for f( (or e) rather than the leading-edge-suction method. 
[ 
. ]2 sh [ 12 CD;,,;mmed = ]( CLa( a + lw) + Y/h Sw ](h CLh (16.3 4) 
For an aircraft with an aft tail, the downwash off the wing has an 
additional effect on total trimmed drag. The directions of lift and drag of 
the tail are slightly rotated because they are always perpendicular and parallel 
to the local flow direct ion. The change in drag direction has a trivial effect on 
total drag, but the change in lift direction might be nontrivial. For a stable 
aircraft, the tail is often experiencing a download (neg ative lift) to trim the 
aircraft, and this downward lift vector is rotated by the wing's downwash 
so that it has a slight forward componen t. This is in effect a reduction of 
trimmed drag, and as a result, the conventional aft tail does not have as 
much trim drag as might be assumed. On the other hand, if we design so 
that the aft tail is lifting to minimize trim drag, the lift vector is rotated to 
the rear. This causes a slight increase in drag that reduces the trim drag 
savings expected for such an aircraft (wl}ich usua lly requires an unstable aircraft with a computerized flight control system). 
This downwash effect on the direction of tail lift can be estimated by 
determining the downwash angle as already described, then multiplying 
the lift on the tail by the sine of the angle and adding or subtracting the 
result to the aircraft's total drag. 
Another small trim drag contribution is the parasitic drag of the elevator, 
if it must be deflected to maintain trim. This drag can be estimated using Eq. 
(12. 37) , although test data on a similar configurati on are preferred. Avoidance of this drag contribution is one reason that many aircraft have a variable 
incidence (all- moving) horizo ntal tail. 
For an all- moving tail, the tail incidence angle is varied rather than elevator angle. For a tailless configuration, the wing flap acts as the eleva tor. 
Otherwise the proced ure is similar. 
Because of the amount of computation involved, it is common in early 
conceptual design to calcula te the trim condition without including the 
thrust effects unless the thrust axis is well above or below the e.g. 
(Most stability and control textbooks introduce a secon dary derivative 
term Cm8E that directly relates the elevator deflection to its influence upon 
pitching moment. I chose to leave the elevator effect as a change in tail lift 
to avoid further compl exity in terminolog y and to leave the tail momen t as 
a clearly understood "force-times- distance" term. This understanding is 
especially impo rtant in conce ptual design because the designer still has the 
freedom to change the "dista nce.") 
4ftlll Ground Effect on Tri m Calcu lation 
The trim equation (1 6.7) is stro ngly influenced by ground effect (Chapter 
12). When the aircraft approaches the ground to within about 20% of the


<!-- p.612 -->

61 0 Air craft Desi gn: A Conceptu al Ap pr oa ch 
span, the wing and tail lift-c urve slopes will increase by about 10%. Furthermore, the downwash is reduced to about half of the normal value, which 
requires a greater elevator deflection to hold the nose up. 
The aircraft must have sufficient elevator effectiveness to trim in ground 
effect with full flaps and full-for ward e.g. loca tion, at both power-off and full 
power. Some additional elevator authority must then be available for control 
including landing flare at maximum forward e.g. ' 
4tflf I Takeoff Rotation 
Some times the elevator of an aircraft is sized by the requirem ent for 
takeoff rotation. For a tricycle-g ear aircraft the elevator should be powerful 
enough to rotate the nose at 80% of takeoff speed with the most-for ward 
e.g. For a taildragger aircraft the elevator should be powerful enou gh to lift 
the tail at half the takeoff speed with the most-aft c.g )117 l 
For rotation analys is, Eq. (1 6.7) can be emplo yed with the addition of two 
landing-gear terms. The analysis assumes that the nose wheel or tailwheel is 
ju st resting on the ground without carrying any of the weight. The weight on 
the wheels is the aircraft weight minus the total lift at that angle of attack. 
This exerts a vertical force with a moment arm equal to the distance from 
the main gear to the e.g. as measured parallel to the ground. 
The rolling friction of the main wheels exerts a rearward force equal to the 
weight on the wheels times the rolling-friction coefficient (0.03 is typical). 
This rollin g-fri ction force acts through a moment arm equal to the vertical 
height of the e.g. above the ground. 
These additional momen ts due to the vertical and rearward landing gear 
forces must be converted to moment coefficien ts by dividing them by (qSwc). 
The alread y described changes in lift-curve slopes and downwash angles 
due to ground effect must be considered in takeoff rotation analysis. 
4tflfl Velocit y Stabil ity 
This brief discussion of longitudinal stabil ity and control has focused 
upon the ang le-of -attack stabil ity derivatives. The aircraft must also have 
veloc ity stabil ity, implying that an increase in veloc ity must produce forces 
that slow the aircraft down, usually by raising the nose. For most contributors 
to pitching momen t, angle-of -attack stabilit y implies veloc ity stabil ity as well. 
One additional term that affects velocity stabil ity is the variation in thrust 
with veloc ity. For propellers, the thrust reduces with increased aircraft 
velocit y. If the propeller is mou nted substantially above the e.g., an increase 
in veloc ity will reduce the thrust, causing the aircraft to pitch nose up. This 
produces a slight climb that will reduce the velocity, so a high-mo unted propeller is stabilizing. 
Roughly speaking, the apparent static margin increases one- quarter of a 
percent for every 1 % MAC that the thrust axis is above the e.g. Conversely ,


<!-- p.613 -->

CHAPTE R 16 Sta bil ity. Contr ol. and Handling Qu al ities 61 1 
a propelle r mounted below the e.g. is destabilizing by the same amount. 
However, this apparent stabil ity response only occurs after enough time 
has passed for the aircraft's veloc ity to increase or decrease enough to 
affect the propeller's thrust. This doesn't change the immedi ate response of 
the aircraft to a pitch distur bance, so the benefit of a high thrust axis 
cannot be used to lessen the aircraft's power-off static margin. On the 
other hand, the veloc ity stabil ity detriment for a low-thrust axis prob ably 
should be considered as it will tend to exaggerate the effect of a slight 
out-of-trim condition over a long period of time. (But how can you put a propeller below the aircraft without having it hit the ground?) . 
The high-mounted propeller also demands a large trim force required to 
counter the nose- down pitching momen t of the high thrust axis. The highmounted propeller is us ually used only to provide water clearance in 
a seaplane. 
For jet aircraft, the veloc ity effect upon thrust being negligib le, engine 
vertical posi tion has little effect upon veloc ity stability. 
f!rJ Lateral- Dir ecti onal Static Stabili ty and Co ntro l 
l@ll Yaw /Rol l-Moment Eq uations and Tri m 
In many ways the lateral -di rectional analys is resembles the longitudinal 
analysis. You draw a picture of the airplane, look for moments and forces, 
and write an equat ion. However, the lateral -directional analysis really 
embraces two clos ely coupled analyses: the yaw (directional) and the roll 
(lateral). 
It is impor tant to realize that both are driven by the yaw angle {3, and that 
the roll angle 'P actually has no direct effect upon any of the moment terms. 
Furthermore, the deflection of either rudder or aileron will produce mome nts 
in both yaw and roll. (Note: to reduce verbiage, "lateral" is used synonymously with "lateral -directional" in the following discussion.) 
The geom etry for lateral analysis is illustrated in Fig. 16.19 , showing the 
major contributors to yawing moment N and rolling moment L. By definition, yaw and roll are positive to the right. Note that unlike the longitudinal 
terms, most of these terms have a zero value when the aircraft is in straight 
and level flight. Also, by the sign conventions used for {3 and yaw, a posi tive 
value of yawing-m oment derivative with respect to {3 is stabilizing. However, 
a negative value of the rolling-mo ment derivative with respect to {3 is 
stabilizing (dihedral effect) . 
The major yawing moment is due to the lateral lift of the vertical tail, 
denoted by Fv. This counteracts the fuselage yawing moment, which is generally negative to the sense shown in the figure. Rudder deflect ion acts as a 
flap to increase the lateral lift of the vertical tail. 
A vertical tail immersed in the propwash experiences an additional force. 
The air in the propwash has a rotational compo nent caused by the propeller


<!-- p.614 -->

612 Ai rcraf t Design : A Conceptu al Appr oach 
Dengine out 
/3 v 
r; 
y 
B 
8 (- T 
a, 
B-B 
Fig. 16 .19 Latera l geome try. 
v 
x 
and in the same direction that the propeller rotate s. A propeller usually 
rotates clockwise when seen from behind. For a vertical tail above the 
fuselage, the propwash rotational component causes the angle of sides lip at 
the tail to become more negative, thus slightly yawing the nose of the aircraft 
to the left. 
A stronger yawing moment caused by the propeller occu rs when the disk 
of the propeller is at an angle to the freestream flow, typically during a 
low-speed climb. The blade going downward has a higher angle of attack 
and is also at a slightly higher velocity because it is advancing into the relative 
flow. Therefore it experiences higher thrust, causing the effective thrust axis 
to move toward that side. This is called "p-effect," yawing the nose to the left 
for a clockwise propeller rotation and is difficult to predict. 
Many single- engine aircraft have 1 or 2 deg of incidence built into the 
vertical tail to cou nteract p-effect. Alternat ively, some aircr aft have the propeller axis angled to the right. 
The wing yawing moment can be visualized as an increase in drag on the 
side of the wing that is more nearly perpendicular to the oncom ing flow. If 
the wing is swept aft, this yawing moment is stabilizing as shown. 
Another wing yawing moment occurs with aileron deflection. The wing 
with increased lift due to aileron deflection has more induced drag, so the


<!-- p.615 -->

CHAP TER 16 Sta bil ity, Contr ol, and Handling Qual ities 61 3 
yawing moment is in the opposi te direction from the rolling moment due to 
the aileron deflection. This is known as "adverse yaw." 
The engines have the same three effects upon lateral mome nts that they 
have on longi tudinal momen ts (direct thrust, normal force, and pro pwash or 
jet-induced flowfield effects). In yaw, the thrust is balanced unless an engine 
fails. Then the remaining engine (s) create a huge yawing moment that is 
made worse by the drag of the failed engine. 
The inle t front face or propeller disk has the same normal force term 
discussed for longitudinal stabili ty. As in pitch, this is destabilizing in yaw 
if the inlet or propeller is in front of the e.g. 
The propwash or jet-induced flowfield effects are gene rally negligible in 
yaw unless the vertical tail is in the propwash or near the jet exhaust. In 
this case the dynamic pressure and angle of sideslip at the tail will be affected 
much as the horizo ntal tail is affected by propwash. 
In roll, the major influence is the wing rolling moment due to dihedral effect. As discussed in Chapter 4, this rolling moment tends to 
keep the aircraft level because it sideslips downward whenever a roll is 
introduced. The dihedral effect rolls the aircraft away from the sideslip 
direction. 
The ailerons, the primary roll-con trol device, ope rate by increasing lift on 
one wing and reducing it on the other. The aileron deflection Da is defined as 
the average of the left and right aileron deflections in the directions shown. 
(Some texts define aileron deflection as the total of left and right.) Positive 
aileron deflection rolls the aircraft to the right. 
Spoilers are an alternative roll -con trol device. These are plates that rise 
up from the top of the wing, usua lly just aft of the maximu m-thickness 
point. This disturbs the airflow and "spoils" the lift, dropping the wing on 
that side. Spoiler deflection also increases drag, so the wing yaws in the 
same direction that it roll - (proverse yaw). 
The vertical tail contributes pos itively to the roll stability because it is 
above the e.g. Note that the moment arm for the vertical tail roll contribution 
is from the vertical tail MAC to the X axis in the stabil ity (wind) axis system. 
This X axis is through the e.g. and is aligned with the relative wing. Thus, this 
term changes substantially with angle of attack. 
The major thrust effect on static roll momen ts is the engine-out case. The 
air in the propwash has higher dynamic pressu re and thus produces more lift 
on the wing. With propwash on only one side of the wing, there is a difference 
in lift between the left and right wing. This can freque ntly be ignored because 
the resulting roll moment is so much less than the engine-out yaw moment. 
The equivalent jet-induced effect on roll is negligible unless the jet exhaust 
impinges upon the flaps, as in the YC- 15. 
Propwash can also alter the wing dihedral effect. When the aircraft yaws, 
one side of the wing gets more propwash than the other, producing a destabilizing roll moment. This is more severe for single-eng ine aircraft where the 
propeller is way in front of the wing.


<!-- p.616 -->

614 Ai rcraf t Desi gn: A Conceptual Approach 
There will be a thrust nor mal force contribution to rolling moment at 
angle of sideslip if the engines are sub stantially above or below the e.g. A 
high-moun ted engine would be stabilizing. This is usually negligible. 
N = Nwing + Nwoa Da + Nfus + Fv(Xacv - Xcg) 
- TYp - DYp - Fp(Xcg - Xp) 
L = Lwing + Lwoa Da - Fv(Zv) 
(16.35) 
(16.36) 
These yaw and roll moments are summed in Eqs. (16 .35) and (16 .36) for a 
twin- engine aircraft with one engine out. Similar equations for other engine 
arrangement s should be obvious from inspection of Fig. 16.19. These are 
strict ly static equatio ns. Dynamic terms will be consid ered in a later section. 
The lateral lift force on the vertical tail appears in both equat ions. This is 
much like the horizontal- tail lift and must be calculated using the local 
dynamic pressure and angle of sideslip. The loca l angle of sideslip is less 
than the freestream sideslip angle because of a "si dewash" effect largely 
due to the fuselage. Propw ash can also reduce the effective angle of sideslip. 
Equation (1 6.37) expresses the lateral lift force on the vertical tail. Note that 
the tail lateral -lift-force derivative CF13 is equival ent to Cr,, in long itudinal 
notation and is calculated the same way. 
(16 .37) 
The yaw- and roll -mom ent equations are expressed in coefficient form by 
dividing through by (qSwb), as shown in Eqs. (1 6.38) and (1 6.40) . Lengths are 
expressed as a fraction of wing span using the "bar" notation. Thus, (Y) denotes 
(Y/b) . The ratio between dynamic pressure at the tail and the freestream 
dynamic pressure is denoted by Y/v· The vertical- tail contributions to yaw 
and roll are expressed by the derivatives defined in Eqs. (1 6.39) and (1 6.41). 
Yaw: 
N Cn = -5 b = Cn13 {3 + Cn0 oa + Cn13 {3 + Cn13 {3 
q W w a fus v 
(16 .38) 
where 
(16 .39) 
Roll: 
(16.40)


<!-- p.617 -->

CH APTE R 16 Stabil ity, Contr ol, and Handling Qual ities 61 5 
where 
(16. 41) 
SfJ Later al-Tri m Ana lysis 
The main static lateral-trim cond ition of concern is the engine -out case 
on takeoff. The vertical tail with rudder deflected must produce sufficient 
yawing moment to keep the aircraft at zero angle of sideslip at takeoff 
speed (1. 1 times the stall speed) with one engine out and at the aft-most 
e.g . location. Rudder deflection should proba bly be no more than 20 deg to 
allow additional deflection for control. 
Another lateral-trim cond ition that should be checked is the 
crosswind-landing case. The aircraft must be able to oper ate in cross winds 
equal to 20% of takeoff speed, which i!i equivalent to holding an 11 .5-d eg 
sideslip at takeoff speed. Again, no more than 20 deg of rudder should 
be used. 
If the vertical tail cannot provide sufficient force to produce zero yawing 
moment in Eq. (16 .38) for either of these cases, there are several approaches 
to correct the problem. The brute-force method simply increases the verticaltail size, but this penalizes aircraft weight and drag. 
The rudder chord and/ or span can be increased to improve the rudder 
effectiveness. This can also be increased by using a double- hinged rudder, 
as seen on the DC- 10. An all-mo ving vertical tail as seen on the F-10 7 and 
SR-71 provides the greatest yaw control power for a given tail area, but 
is heavy. 
Sometimes the engines can be moved inward to reduce the engine-out 
moment. However, this increases wing structural weight as discussed. 
The rudder deflection and pro pwash effects for the engine -ou t case will 
also cause a rolling moment. Usually, this is small enough to be ignored, 
but a short-coupled aircraft with widely sepa rated engines might require 
excessive aileron deflections to coun ter the rolling moment s. The adverse 
yaw of the aileron deflections will then make the yawing situation even 
worse! 
The aileron control autho rity must also be checked at the 11 .5- deg 
sideslip condition using Eq. (1 6.40) . An aircraft with a large amount of effective dihedral might not have sufficient aileron area to prevent the aircraft 
from rolling away from the sideslip. 
ltJp Static Later al -Dir ecti onal Stabil ity 
The yaw- and rolling- moment derivatives with respect to sideslip are 
provided in Eqs. (1 6.42) and (1 6.4 3). The power-off Cn13 is simply the sum


<!-- p.618 -->

616 Aircr aft Desi gn: A Conce ptu al Appr oach 
0.4 
0.3 
CQ. 
Per 
ra dian 
• Gr umman 
Mohawk 
T-38 
• 
1\1,qs: 
cJ 0.2 Hawk 
4 1'1\f " Sugge sted D,.,<3 
goal va lues 
0.1 
• 
- 0.25 0.50 0.75 1.0 1.25 1. 50 
Mach numb er 
Fig. 16 .20 Typical yaw-moment der ivativ e valu es. 
of the wing, fuselage, and vertical-t ail contribut ions. 
1. 75 
F-4 • 
2.00 
(16.4 2) 
(16 .43) 
It would be possible to solve Eq. (1 6.42) for the e.g. position for zero 
yaw stabil ity. This would be the lateral neutral poi nt. This is not usua lly calculated because it is common practice to determine the most aft e.g. position 
from longitudinal consid erations and then vary the vertical- tail area until 
gaining sufficient yaw stabil ity. 
Figure 16 .20 provides sugges ted goal values for Cnf3 · These are somewhat 
less than those suggested by the NASA curve. Cgf3 should be of negative sign 
with magnitude about half that of the Cnf3 value at subsonic speeds, and about 
equal to it at transonic speeds. 
Final selection of these values requires dynamic analysis based upon 
wind-tunnel data, and it is not unheard of for the vertical- tail size or wing 
dihedr al to be changed after the protot ype flies (F- 100, B-25). 
The following sections provide crude estimation procedures for the 
terms of these lateral equat ions. Many of these terms are identical to 
longitudinal terms as alread y discussed, and the reader should refer 
back to that material. These include the tail aerod ynamic center, tail-force 
(lift) curve slope, rudder (flap ) effectiveness, and prope ller or inlet normal 
force.


<!-- p.619 -->

CHAPTER 16 Stabil ity, Contr ol, and Handling Qual ities 61 7 
1#11 Wing Later al-Di rectional Deriv ativ es 
Reference [69] provides an empiric al expression for the wing yawing 
moment due to sideslip [Eq. (1 6.44)]. 
C _ C2 { -1 _ [ tan A ] 
n13., - L 47TA 1TA (A + 4 cos A) 
[ A A A 2 6(Xacw - Xcg) sin A] } (16.4 4) x cos - - - --- + -------2 Sc os A A 
The rolling moment due to sideslip, or dihedral effect, is propor tional to 
the dihedral angle but also includes the effects of sweep and wing vertical 
position on the fuselage; C113 for a straight wing is approximately 0.0002 
times the dihedra l angle in deg, so 1 deg of "effective dihedral" is defined 
to be a Ct13 of 0.0002 per deg, or 0.0115 per radian. 
Figure 16.21 provides an estimate of the wing dihedral effect due to sweep 
for a wing with no geometric dihedral. Two taper ratios are provided, requiring interpolation or extrapolation for other taper ratios. The values from the 
figure are per unit lift coefficient, so the final value is obtained by multiplying 
by the wing Cr . 
Equation (1 6.45) from [69l estimates the effect of the geom etric dihedral 
angle (radia ns) . Equation (1 6.46) from [11 9l determines the effect of wing vertical placement on the fuselage; Zwf is the vertical height of the wing above 
the fuselage centerline, and DJ and Wf are the depth and width of the fuselage. 
These two additional dihedral co ntributi ons are added to the value 
from Fig. 16.21, as shown in Eq. (1 6.47) . All terms should be neg ative 
except that the wing vertical placement term will be positive (destabilizing) 
As pect ratio · 
0 1 2 3 4 5 6 7 8 
o ----------0 
-0.1 
-0.2 
-0.3 
-0.4 
-0.5 
-0.6 Ta per ratio = 0.5 
-0.7 
Ce13 · 
- (per radian ) 
cl 
10 20 30 
40 45 
t:-.,14 (deg) 
Aspect ratio 
0 2 3 4 5 6 0 
-0.1 
-0.2 
-0.3 
-0.4 
-0.5 
-0.6 
-0.7 
Fig. 16 .21 Dihedr al effect of aspect ratio, taper ratio, and sweep. 11 61 
7 8 
0 10 20 
30 
40 
45 50 
55


<!-- p.620 -->

618 Airc raf t Desi gn: A Con ceptu al Appr oach 
for a low wing. 
(C ) = _ Cr,,f [2(1 + 2A)] 
£13 r 4 3(1 + A) 
VAZwf(Dj + WJ') Ce/3wr = -1. 2 b2 
c,,_ - (c-;') c, + (Ce,k + c,"" 
(1 6.45) 
(1 6.46) 
(1 6.47) 
The aileron control power can be approximated using a strip method. 
The portion of the wing having the aileron is broken into strips as shown 
in Fig. 16.22. The lift increment due to aileron deflection is estimated as a 
flap effect using the method presen ted in Eq. (16 .17 ). This lift incr ement is 
then multiplied by the strip 's moment arm from the aircraft centerli ne Y1, 
as shown in Eq. (1 6.48), where Kj and the lift derivative with flap deflection 
come from Figs. 16.6 and 16.7. Remember to reduce the aileron effectiveness 
about 15% if the hinge gap is not sealed. 
Fig. 16 .22 Ai leron stri p geome try. 
(16. 48) 
(16.4 9)


<!-- p.621 -->

CHAPTER 16 Sta bil ity, Contr ol, and Handling Qu al ities 61 9 
The yawing moment due to aileron deflection depends upon the spanwise 
distribution of induced drag with the aileron deflected. This varies with the 
wing lift coefficient as well as the aileron deflection. Yawing moment due 
to aileron deflection can be approximated by Eq. (1 6.49), a simplification of 
the method from [69l ; Cr is the wing lift coefficient. 
Sii Fus elage and Nac elle Late ral-Dir ection al Deriv atives 
The yawing moment due to sideslip is expressed in Eq. (1 6.50) as a function of the fuselage or nacelle volume, depth, and width. The fuselage contribution to roll is usually negligible except for its influence upon the wing 
effective dihedral, as already discussed. 
Cn = - 1 .3 volume (DJ) 
/31u, Swb WJ 
lfJP Later al-Dir ecti onal Deriv atives 
(16.5 0) 
The vertical- tail lateral derivatives were expressed in Eqs. (1 6.39) 
and (16. 41). The lateral lift-cur ve slope is found using the methods in 
Chapter 12. The vertical-tail aspect ratio should be increased for the endpla te 
effects of the fuselage and horizo ntal tail. Typically the effective aspect ratio 
will be about 55% higher than the actual aspect ratio. Also, the lateral lift-cur ve 
slope should be reduced by about 20% if the rudder hinge gap is not sealed. 
The remaining unknowns in Eqs. (1 6.39) and (16 .41) are the local 
dynamic pressure ratio and sideslip derivative. These can be estimated in 
an empirical Eq. (16.51) from [69l ; S-5 is the area of the vertical tail extended 
to the fuselage centerline. 
S' . 3 06 __y§_ 
(f) f3v ) . Sw Zwf - T/v = 0. 724 + A - 0.4 - + 0.0 09Awing u{3 1 + cos DJ (16.51) 
l@ff Th rust Effects on Later al-Dir ecti onal Tri m and Stabil ity 
The thrust effects on the lateral trim and stabil ity are similar to the 
longitudinal effects. There are direct thrust momen ts, normal force 
moments, and propwash or jet-induced effects. 
When all engines are running, the direct thrust momen ts cancel each 
other. The normal force momen ts of the engines are additive . 
When one engine fails, the remaining engin e(s) produce(s) a substantial 
yawing moment. Also, the failed engine contributes an additional drag term 
as already presen ted in Chapter 13. 
The propwash dynamic pressure effect is estimated using Eq. (16.31). The 
propwash effect upon sidewash can be estimated using Eqs. (1 6.3 0) and 
(1 6.23) and then be applied to the result from Eq. (1 6.5 1).


<!-- p.622 -->

620 Air c raf t Desi gn: A Concep tual Approach 
(With the exception of rudder sizing for engine-o ut, the lateral analysis is 
freque ntly ignored in early conc eptual design. To obtain good later al results 
usua lly requires six- DOF analysis using wind-tunnel data. During early concept ual design, previous aircraft data and rule -of-thumb methods such as the 
tail volume coefficient are relied upon to select tail areas, dihedral angle, and 
the rudder and aileron areas .) 
Stick -Fr ee Stabil ity 
The previous analysis has assumed that the control surfaces are rigidly 
held to the desired deflect ion. This "stick -fixed" assumption is reason able 
for modern fighters and large transpor ts that employ fully powered flightcontrol systems. 
Many smaller aircraft use purely manual or si mply boo sted control 
systems in which the airloads upon the control surfaces cause them to 
change deflection angle as the angles of attack and sideslip vary. Such a 
case requires a "stick -free" stabil ity analysis. 
A worst-case analysis for stick-free longitudinal stabil ity would assume 
that the elevator "floats" up so much that it contributes nothing to the tail 
lift. In this case the percent reduction in total tail lift-c urve slope would 
equal the elevator's area as a percent of total tail area. 
This is generally not the case, and the elevator will usually float to a lesser 
angle depending upon the airfoil pressure distribution and the amount of 
"aerod ynamic balance" (i.e., the portion of the elevator ahead of the hinge 
line) . Data in[82l indicate that a typical free elevator with aero dynamic 
balance will reduce the total tail lift-c urve slope by approximately 50% of 
the elevator's area as a percent of total tail area. Thus, a stick -free elevator 
that is 40% of the total tail area will experience a reduction in the tail slope 
of the lift curve of about 20%. 
In fact, the elevator can be "overbalanced" so that it floats into the relative 
wind and therefore adds to the stability. However, this can produce unusual 
control forces. Because of the strong effect of the bound ary layer, controlsurface float is difficult to predict even with wind-tunnel data. 
References (13, 11 8] provide detailed methods for analyzing the stickfree stability based upon test data for co ntrol surface hinge moments. Typically, the stick-free neutral point is 2- 5% ahead of the stick-fixed 
neutral point. 
Stick-free directional stability is also reduced as a result of rudder float. 
This can be approximated using the percent reduction in tail slope of the 
lift curve ju st described. 
Effects of Fle xi bili ty 
The previous discussion also assumes that the aircraft is rigid. In fact, 
many aircraft are quite flexible, espec ially in fuselage longitudinal bending,


<!-- p.623 -->

CHAPTER 16 Sta bili ty, Contr ol. and Handling Qu al ities 62 1 
wing spanwise bending, and wing torsional deflection. These can have a 
major effect upon the stability characteristics . 
If the fuselage is flexible in longitudinal bend ing, the horizontal-tail 
incidence angle will reduce when the aircraft angle of attack is increased. 
This reduces the effectiveness of the tail as a restoring force for pitch stabil ity. 
The vertical tail experiences the same effectiveness reduction due to lateral 
fuselage bend ing. 
Similarly, a swept flexible wing will deflect such that the wing tips have a 
reduced angle of attack compared to the rigid aircraft. This reduces the slope 
of the lift curve and moves the wing aerod ynamic center forward, destabilizing the aircraft. These effects are shown in Fig. 16.23. 
A typical swept-wing transport at high subsonic speeds will experience a 
reduction in wing lift-cur ve slope of about 20%, a reduction in tail pitchingmoment contribution of about 30%, and a reduction in elevator effectiveness 
of about 50% due to flexibility effects. The wing aerod ynamic center will shift 
forward about 10% MAC due to flexibility. 
In addition, the aileron effectiveness can be reduced by 50 to over 100%! 
At high dynamic pressures the ailerons will produce torsional moments on 
the wing that twist it in the opposi te direction from the aileron deflect ion. 
This wing twist produces a rolling moment in the opposi te direction from 
the desired rolling moment. 
If the wing twists enough, this effect can overpower the aileron forces, 
producing "aileron reversal." To retain roll authority, many jet transpor ts 
lock the outboard ailerons at high speeds and rely upon spoilers or small 
inboard ailero ns. 
Figure 16 .24 shows the aileron reversal experienced with the B-47, the 
first transonic jet having thin, highly swept wings. Tec hnically, this aircraft 
was in many ways the forerunner of today's jet transpor ts. As can be seen, 
the ailerons had zero-roll: rate effectiveness at about 470 kt due to flexibility 
Fig. 16 .23 Effects of flexi bil ity on stabil ity. 
Red uced 
ta il 
angle of 
atta ck


<!-- p.624 -->

622 Ai rcraf t Design : A Concept ual Approach 
Roll rat e-d eg/s 
40 
30 
20 
10 
0 
-10 
150 200 
t 
250 300 350 
Veloc ity- kn ots 
l 
B-47 ailer on reversa l 
400 450 500 
Fig. 16 .2 4 Ail eron reversal caused by flexi bil ity effects. 
effects. At higher speeds, the ailerons worked backward; an "up" left aileron 
would twist the wing trailing edge down so much that lift would increase, 
causing a roll to the right rather than to the left as expected! By addin g 
wing spoi lers, roll cont rol was poss ible at a much higher speed. Pilot s were 
taught that if the spoi lers failed to operate at a speed greater than 470 kt, 
they should simply move the control stick in the opposi te direction from 
the way that they wished to roll. 
Toda y, of course, we could use a compu terized flight control system to do 
the same thing without the pilot ever being aware of it. This could save hundreds or even thousands of pounds compared to adding eno ugh structural 
rigidit y to avoid aileron reversal at all speeds. 
These effects are functions of dynamic pressure, with the greatest impact 
seen at the low- altitude, high -speed condition. A "stiffer" aircraft such as a 
fighter, with a low wing aspect ratio and a short fuselage, will have less 
impact on its static stabil ity derivatives due to flexibility. 
Dynami c Stabil ity 
Dynamic stabil ity concerns the motions of the aircraft, so two new 
classes of force must be consid ered: the iner tia forces and the damping 
forcPs.


<!-- p.625 -->

CHAP TER 16 Sta bil ity, Contr ol. and Handling Qu al ities 623 
,,.,,. Mass Mome nts of Inertia 
Inertia forces derive from the tendency of mass to resist acceler ations. The 
mass for rotational accelerations is represented by "mass- moment- of-inertia" 
terms, denoted by I. Mass moment of inertia describes a body's resistance to 
rotational accelerations and is calculated by integrating the products of 
mass elements and the square of their distance from the Ref. axis. 
For aircraft dynamic analys is, the mass momen ts of inertia about the 
three prin cipal axes must be determined: I:xx about the roll axis, fyy about 
the pitch axis, and fzz about the yaw axis. 
These can be initially determined using historical data based upon 
the nondimensional radii of gyration R, as described in[18 l . Equations 
(16.52-1 6.54) are used with typical R values from Table 16.1. 
Roll: 
Pitch: 
Yaw: 
L2MR2 I - y yy - 4 
4g 
4g 
I = (b + L)2MR; = (b + L)2WR; zz 2 4 2 4g 
Table 16 .1 Nondi mensio nal Rad ii of Gyration* 
Ai rcraft Class ! Rx -Single -engine pr op 0.25 0.3 8 0.3 9 
Twin- engine prop 0.3 4 0.2 9 0.44 
Busi ness jet twin 0.3 0 0.30 0.43 
Twin turbopr op tra nsport 0.22 0.3 4 0.3 8 
Jet tran spor t-Fuselage-mou nted eng ines 0.2 4 0.3 6 0.44 
2 wing-mou nted eng ines 0.25 0.38 0.46 
4 wi ng-mou nted eng ines 0.31 0.3 3 0.45 
Mil itar y jet train er 0.2 2 0. 14 0.25 
Jet fighter 0.23 0.3 8 0.5 2 
Jet heavy bomber 0.34 0.31 0.47 
Flying wi ng (B-49 type) 0.32 0.3 2 0.51 
Flying boat 0.25 0.32 0.41 
*Typical value s (see [1 8] for exa mp les) . 
(16 .52) 
(16 .53) 
(16.5 4)


<!-- p.626 -->

624 Aircr aft Desig n: A Concep tual Approach 
(Results are in slug-ft 2. In metric units, don't apply the g term, and results 
are in gram-M 2.) 
For a full six- DOF dynamic analysis as discussed below, there are three 
more mass iner tia terms that must considered and can play an important 
role in the analysis. "Produ cts of inertia" are a little confusing at first 
because they can have a zero value, an odd result for a mass term. These 
are found by taking each mass in the airplane and multiplying it by the distances to two of the three reference axes (X Y, Z), and then summin g them 
all. For a symmetrical airplane, the product of inertia for the XZ plane is in 
fact zero. All of the terms on one side of the airplane are cancelled by the 
negative terms on the other side of the airplane. 
Product of iner tia is related to the mass principal axis, the line about 
which the airplane "prefers" to rotate. For a normal airplane with a long 
fuselage, this is approximately the center axis of the fuselage. However, the 
mass of the tail will "pull" the principle axis upwards, tipping it downwards 
in front by a few degrees. This "tip" is zero if the product of iner tia about 
the XY plane is zero. If these are not zero, the airplane will "fight" an 
attempt to rotate about the fuselage centerline (X axis) and instead will try 
to rotate about the principa l axis. The product of inertia terms in the 
six- DOF equations make that happen. 
These are difficult to estimate at the conc eptual level. As a rough gue ss, 
values from similar airplanes can be ratioed by weight. Normally, products of 
iner tia are ignored until the stabil ity and control group does a complete 
six- DOF analysis including a detailed mass buildup. 
MOIJ Da mping Derivativ es 
Aerod ynamic damping forces resist motion. The rotational damping 
forces are propor tiona l to the pitch rate Q, roll rate P, and yaw rate R. 
(Note: Avoid confusing Q with dynamic pressure q.) 
These damping forces arise because of a change in effective angle of 
attack due to the rotational motion, as shown in Fig. 16.25 for the lift 
on the horizo ntal tail during a steady pitchup and for the lift on a 
segment of the wing during a steady roll. The lateral lift on a vertical 
tail in a steady yawing motion would change simil arly to the horizontal 
tail. 
The change in effective angle of attack, and hence the change in lift, is 
direct ly propor tional to the rotation rate and the distance from the e.g. 
The momen t is propor tional to the lift times the distance from the e.g. 
Rotational damping moment is therefore propor tional to the rotational 
rate and the square of the distance from the e.g. 
Equations (16 .55) and (1 6.56) provide first-order estimates of the pitchand yaw-damp ing derivatives. The wing drag term in Eq. (16 .56) accounts 
for the yaw-damping effect of the wing. Dynamic pressure ratios TJ for 
horizo ntal and vertical tails can be approximated as 0.9.


<!-- p.627 -->

Rea r 
view 
CHAP TER 16 Sta bil ity, Control. and Handling Qua li ties 625 
... ... ... Jl. ... ... v . '..J-_,., v v = pl 
P =0 
' ,- ' 
Tail 
v -+Qlt 8.lXetfective = V 
Wi ng strip "i" 
Vv 
v -+ c::::::::::. 
PI 
8.CXeffective = \f 
Fig. 16 .2 5 Origin of dampin g forces . 
Roll damping is estimated with Fig. 16 .26, based upon data in NACA 
109 8 covering the lower aspect ratios and NACA 868 covering the higher 
aspect ratios. The sweep factor is multiplied times the unswept damping 
derivative. 
(16. 55) 
(16. 56) 
There are also "cross -.derivative" damping terms. The yaw rate will affect 
the roll mome nt, and the roll rate will affect the yaw moment. These are both 
functions of wing lift coefficient. As a rough approximation, the rolling 
moment due to yaw rate CeR is about Cr/4, and the yawing momen t due 
to roll rate Cnp is about - CL/8. 
MttH One-DOF Dynami c Eq uations 
A six- DOF analysis is required to fully evaluate aircraft dynamic stabil ity 
and control. The six- DOF allows simultaneous rotations in pitch, yaw, and 
roll and allows the aircraft veloc ity to change in the vertical, lateral, and 
longitudinal directio ns. All of these motions affect each other, requiring 
a tremendous number of cross derivatives to account fully for all forces 
and moments. References [69, 11 8] are recommended for the equations for 
six-DOF analysis. 
The one-DOF equations can be used for initial analysis of several flight 
conditions, such as pull-up and steady roll. The one-DOF rotation equations


<!-- p.628 -->

626 Air c raf t Desig n: A Conc ept ual Appr oa ch 
are based upon the fact that the rotational acceleration times the mass 
momen t of iner tia equals the sum of the applied moments (which include s 
the damping moment s). Equations (16 .57 -1 6.59) provide these: 
Pitch: 
(16.5 7) 
Yaw: 
(1 6.5 8) 
Roll: 
(1 6.59 ) 
These are second- order differential equat ions because Q, R, and P are the 
derivatives with time of pitch, yaw, and roll. Note that there is no first- order 
term in the roll equation because the roll angle does not affect the roll 
momen ts if the sideslip remains zero. 
Meul Air craft Dynamic s: Three-DOF and Six-DOF 
With proper input data, these one-DOF equati ons can be solved for time 
histor y after a given distur bance. However, the results will be inco rrect 
because real aircraft motions always involve more than one-DO F. 
-0.5 
-0.4 
-0.3 
-0.2 
Sweep factor 
-------- 0° - - 1.0 
I 
- - - __ 300 + o.9 
... ... 
- - ... ... ... ... 450 + o.s 
- .... ..... .... 
I 
... ._ T 0.7 
..... .... .... I ... ... ... ... 600 i 0.6 
NACA 10 98 
-0. 1 +---+---+---->-----<>----+----+----+ 
2 4 6 8 10 12 
As pect ratio 
Fig. 16 .26 Roll dampin g parame ter. 
14 16


<!-- p.629 -->

CH APTE R 16 Sta bil ity, Control, and Handling Qua lities 627 
Longitudinal analysis requires a minimum of three-DOF to account for the 
interplay between pitch angle, vertical velocity, and changes in horizo ntal 
velocity. An additional equation is required for elevator deflection in a 
stick-free ana lysis. 
Lateral analysis with stick fixed also requires a minimum of three-DOF, 
which accou nt for lateral velocity, sideslip angle, and rolling angle. For stickfree lateral analysis, two additional equations are required to account for the 
aileron and rudder deflecti ons. A full six-DOF (nine-DOF for stick-free) is 
preferable because of the interplay between lift coefficient and the lateral 
derivatives, espec ially at higher angles of attack. 
Analytical techniques for three- or six-DOF simulations are beyond the 
scope of this book, but a few com ments on typical results are in order. Longitudinally, there are two oscillator y solutions to the equations of motion. One 
is a short-p eriod mode, which is typically heavily damped and provides the 
desired dynamic stabil ity in response to a pitch disturba nce. The other 
solution is a long-period lightly damped mode called the "pitch phugo id." 
This involves a slow pitch osci llation qver many seconds in which energy 
is exchanged between vertical and forward velocit y. Many aircraft have a 
slight unnoticeable pitch phugoid, easily and unconscious ly corrected by 
the pilot. An excessi ve phugoid should be avoided. 
The lateral equations of motion yield three solutions to a yaw disturbance. One is the desired heavily damped direct convergence. The spiral divergence mode, another solution, involves an increasing bank angle with the 
aircraft turning more and more tightly until control is lost. However, the 
time to diverge is so long that pilots can easily correct for spiral divergence. 
The third lateral solution, a short-period osci llation called Dutch roll, sees 
the aircraft waddle from side to side, exchanging yaw and roll. If the Dutch 
roll is excessi ve, this osci llation will be objectionable to passen gers and 
crew. Dutch roll is largely caused by the dihedral effect. 
Dutch roll damping is determined mainly by the size of the vertical tail 
and is usually the driving criteria for tail sizing other than engine-out 
control. For this reason, vertical-t ail size should not be reduced below the 
size indicated by the tail volume coefficient method until a six- DOF analysis 
has been cond ucted, prefe rably with wind-tunnel data for the dynamic 
derivatives. 
Dutch roll is aggravated by flexibil ity effects at high speeds. Most large, 
swept-wing aircraft use a powered rudder mechanized with a gyro to deflect 
into a yaw, thus increasing the effective Dutch roll damping. 
b Quasi Steady State 
Setting the rotational accelerations in Eqs. (16 .57 -1 6.59) to zero yields 
quasi-steady- state equations. These represent a steady pitch, yaw, or roll 
rate and are iden tical to the steady-state trim equations presented earlier, 
but with the addition of damping terms .


<!-- p.630 -->

628 Ai rcraft Desig n: A Con ceptu al Approach 
4(:1:11 Pul l-up 
Pull-up is a quasi- steady-st ate trim cond ition in which the aircraft 
acceler ates vertically at a load factor n. Level flight implies that n = 1. The 
longitudinal-t rim equation alread y presen ted [Eq. (16 .7)], with the addition 
of the pitch damping moment (CmQ times Q), is solved to provide a total 
aircraft lift equal to n times the aircraft weight. The required elevator deflection is then determined from the required tail lift. The pitch rate Q is related 
to the load factor in a pull-up as follows: 
MfJ:f J Leve l Turn 
Q = g(n - 1) v (16. 60) 
A level turn is similar to the pull-up in that the aircraft experiences an 
increased load factor and a stead y pitch rate. Note that the sidesli p 
remains zero during a coordina ted turn so that the level turn is strictly a 
longitudinal problem! The load factor due to a bank angle cf> is obtained 
from Eq. (16 .61), and the resulting pitch rate is obtained from Eq. (1 6.62) . 
n = 1/ cos cf> 
Q = t(n - -) 
MfJ:p Steady Roll 
(16.6 1) 
(16.6 2) 
The steady roll is found by setting Eq. (1 6.59) to zero. Equation (16. 40) Ce 
indicates that the only rolling-moment term that remains when the sideslip 
equals zero is the roll due to aileron deflecti on. This leads to Eq. (16. 63), 
which is solved for roll rate (radians) as a function of aileron deflection in 
Eq. (1 6.6 4). 
IxxP = 0 = qSwbCe8• 8a + qSwbCepP (16.6 3) 
P -- (-: }a (16 .64) 
For many years the roll- rate requirement was based upon the wing helix 
angle Pb/2V. NACA flight tests (NACA 715) determined that most pilots 
consider an aircraft to have a good roll rate if the wing helix angle is at 
least equal to 0.07 (0.09 for fighters ). 
Military speci fications (MIL- F-8785B or Mil Std 17 97) require that the 
aircraft reach a certain roll angle in a given number of seconds, as noted in 
Table 16.2. These assume that the aircra ft is in level flight upon initiation of


<!-- p.631 -->

Il l 
IV A 
IV B 
IV C 
CHAPTE R 16 Sta bil ity, Contr ol. and Handling Qu al ities 629 
Table 16 .2 MI L-F-8 785 B Roll Requir emen ts 
Ai rcraft Type ! Requir ed Roll 
Ligh t uti lity, obs ervation , pri mar y train er 60 deg in 1. 3 s 
Medium bomber , cargo, tran spor t, ASW, recce . 45 deg in l .4 s 
Heav y bomber , cargo, tran spor t 30 deg in l .5 s 
Fig hter -atta ck, int erceptor 90 deg in 1. 3 s 
Ai r-to-a ir dogfig hter { 90 deg in l .0 s 
360 deg in 2.8 s 
Fig hter with air -to-g round stores 90 deg in l. 7 s 
the roll, so the rotationa l acceleration should be accounted for. However, aircraft generally reach maximum roll rate quickly; the quasi- steady-state roll 
rate therefore can be used to initially estimate the time to roll. 
fl Ine rtia Coupling 
The F-10 0 prototype, the first fighter capable of level supersonic flight, 
featured a thin swept wing and long heavy fuselage compared to previous 
fighters. During flight testing, a series of high-speed rolls sudden ly diverged 
in angle of attack and sideslip, much to the surprise of all concerned. Detailed 
analysis and simulation discovered the cause to be "iner tia coupling,' ' 
Figure 16.27 shows a typical fighter in roll. The mass of the forebod y and 
aft-fuselage are concen trated like a barbell for illustr ative purposes. 
v 
90° roll 
ab out 
body axis 
Centrif ugal 
force 
Principal axis 
Fig. 16 .27 In ertia couplin g. 
Wind 
axis 
Actual 
roll 
axis 
Principal 
axis


<!-- p.632 -->

630 Air craf t Desi gn: A Concep tual Approach 
Like all objects, the fighter tends to roll about its principal (longit udinal) 
axis. However, if the fighter rolled 90 deg about its long itudinal axis, the angle 
of attack would be exchanged with the angle of yaw, as shown. The Cn13 effect 
of the vertical tail would oppose this increase in yaw angle with roll. 
In addition, the aileron rolling mome nts are about the wind axis. The aircraft thus actua lly rolls around an axis somewhere between the principa l axis 
and the wind axis . 
The masses of the forebod y and aft-fuselage are above and below this 
actual roll axis. Centrifugal force tends to pull them away from the roll 
axis, creating a nose-up pitching moment. The combi nation of the increase 
in yaw angle with roll and the nose-up pitching moment due to inertia is 
called inertia coupling. 
Iner tia coupling becom es a problem only when the moments produce d 
by the inertia forces are stronger than the aerod ynamic restoring moments. 
This is most likely to happen at high altitudes (lower air dens ity) and at 
high Mach numbers where the tail loses lift effectiveness. 
The solution to inertia coupling in the F- 100 was a larger vertical tail. This 
remains the typical solution. For this reason the vertical- tail area should not 
be reduced below the statistica l tail-v olume- method result until a more 
detailed analysis is available. 
Hand lin g Qual ities 
4Ql1ll Coop er-Har per Sca le 
Aircraft handling qualities are a subj ective assessment of the way the 
plane feels to the pilot. Few modern pilots fully apprecia te the great advances 
in handling qualities made since the dawn of aviation. Early fighters such as 
the Fokker Eindecker had handling qualities that were so poor that the pilots 
felt that without constant attention, the aircraft would "turn itself inside out 
or literally swap ends" (movie stunt pilot Frank Tallman, quoted from [120l ). 
A number of "goodness" criteria such as the wing helix angle have already 
been discussed. It is impor tant that the aircraft have a nearly linear response 
to control inputs and that the control forces be appropr iate for the type of 
aircraft. The control forces required due to flap deflection or power application should be small and predictable. 
These handling- qualities criteria are genera lly con sidered later in the 
design cycle. Figure 16 .28 illustrates the Cooper - Harper Handling Qualities 
Rating Scale, which is used by test pilots to categorize design deficiencies and 
cons ists of a series of descr iptive choices leading to a numerica l rating. l121l 
Handling qualities are discussed in detail in[122 l . 
4Ql1f I Depart ure Criteria 
One of the most impor tant aspe cts of handling qualities is the behavior of 
the aircraft at high angles of attack.


<!-- p.633 -->

Adequacy for sele cted task or 
req uir ed operation* 
•:nmr._mat1r.ut• 
Deficiencies 
warrant 
im provement 
Deficiencies 
warrant 
impr ovement 
Im prov ement 
man datory 
Fig. 16 .28 
Ai rcraft 
char acteristics 
Exce llent 
highly desirable 
Good 
negligible deficiencies 
Fair -Some mil dly 
un pleasant deficiencies 
Min or but an noyi ng 
deficiencies 
Moderately objec tionable 
deficiencies 
Very objec tionable but 
toler a ble deficiencies 
Major deficiencies 
Major deficiencies 
Major deficiencies 
Major deficienc ies 
Demands on the pi lot 
in sel ected task or requir ed operation* 
Pilo t compensation not a factor for 
desir ed per formanc e 
Pilo t compensation not a factor for 
desir ed perf ormance 
Minimal pilo t compensation req uir ed for 
desir ed performance 
Desi red perf ormance req uir es moder ate 
pi lot compensation 
Adequate perf ormance req uir es 
consider able pi lot compensation 
Adequ ate performance req uir es exte ns ive 
pi lo t compensation 
Adequate performance not att ainable with 
maxi mum toler able pi lot compensation. 
Contr ollabili ty not in que stion 
Consid erable pilo t compensation is req ui red 
for control 
In tense pi lot compensation is req ui red to 
reta in control 
Control will be lost dur ing some portion of 
req uir ed operation 
Pilot 
rati ng 
*Defini tion of req uir ed operation involv es designation of fi ight phase an d/or 
su bphases with acc ompanying conditions. 
Cooper -H arper Handlin g Qual ities Rating Sca le. 
0 
:c 
;a:.. 
"O 
-c 
m 
::0 
°' 
C./) 
0 
0:::;: 
() 
0 
::J 
-+ 
Q_ 
0 
::J 
0. 
I 
0 
::J 
0. 
s· 
co 
([) 
c 
0 
:::;: 
Cii" 
(J) 
°' 
w


<!-- p.634 -->

632 Air c raf t Des ign : A Conceptual Appr oa ch 
As the angle of attack increases, a "good" airplane experiences mild buffeting to warn the pilot, retains control about all axes, and stalls straight 
ahead with imme diate recovery and no tendency to enter a spin. If a spin 
is forced, the good airplane can be immediately recov ered. 
A "bad" airplane loses cont rol in one or more axes as angle of attack 
increases. A typical bad characteristic is the loss of aileron roll control 
and an increase in aileron adverse yaw. When the aircraft is near the stall 
angle of attack, any minor yaw resulting from aileron deflecti on can slow 
down one wing enough to stall it. With only one wing generating lift, the 
"bad" airplane will sudde nly depart into a spin or other uncon trolled 
flight mode. 
Design features for good dep arture and spin characteristics have been discussed in earlier chapters. There have been many criteria proposed for good 
depa rture characterist ics. Several aerod ynamic coeffic ients are import ant to 
departure characteristics, espe cially Cnw Cn& ' Ce13 , and Ce& . 
These are combined in the lateral control departure parameter (LCDP), 
som etimes called the lateral control spin parameter or the aileron-alone 
divergence parameter [Eq. (16 .65 )]. The LCDP focuses upon the relationship 
between adverse yaw and directional stability. 
Equatio n (1 6.66) shows another departure parameter Cna . , which !-'dynamic 
includes the effects of the mass moments of inertia. Both of these parameters 
should be positive for good departure resistance. A typical goal is to have 
Cn13dymmic greater than 0.004. 
Cn8a 
LCDP = Cn13 - Ce13 C (16 .6 5) 
e8a 
fzz . Cna . = Cna cos a - - Ce" sm a 
f-'dynarrnc I-' 
fxx ,_, 
(16.6 6) 
Figure 16.29 shows a crossplot of the LCDP and Cna . with increase in 
[123 ] /Jdynam.c 
angle of attack. In the bound aries for acceptable departure resistance 
were determined from high-g simulator tests using experienced pilots. The 
earlier Weissman criteria are also shown. 
Note the depart ure-p arameter crossplot for the F-5. This aircraft is widely 
considered to be one of the best fighters at high angle of attack. Both departure parameters are increasing with angle of attack. 
On the other hand, the F-4 has poor departure characteristics. Its 
departure-p arameter crossplot starts in the acceptable zone, but crosses 
into the unacc eptable zone as angle of attack increases. 
The HiMat fighter shows that even an advanced supersonic canard configuration can have good departure characteristi cs. The HiMat has highly 
cambered outboard wing leading edges and has large twin tails with a substantial portion below the wing. 
Unfortun ately, the stabil ity derivatives used to calcu late these departur e 
parameters become very nonlinear near the stall. First- order est imation


<!-- p.635 -->

0.008 
0.006 
0.004 
0.002 
Q) 
c 
LCDP 
e 
0. 
CHAPTER 16 Sta bil ity. Control, and Handling Qual ities 633 
No departur es 
Mild 
depa rtu res 
lo w spin 
su scep tibili ty 
Poor roll control 
(Weiss man criteria) 
-0.004 +------>f-----+----+----+--'---t-----+----+-----1 
-0.002 0 0.002 0.004 0.0 06 0.008 0.010 0.012 0.014 
Fig. 16 .29 Depar tur e suscepti bil ity. 
techniques used in conceptual design might not give usable results for 
departure estimat ion. However, the configuration designer can expect to 
be instructed to "fix it" when the first wind-tunnel data are available! 
There are a few design rules that can be applied during early configuration layout. The fuselage forebod y shape has a huge effect upon the stabil ity 
characteristics at high angles of attack. This is mostly due to a tendency of 
vortices to form asymm-trically, that is, stronger on one side than the 
other thus pulling the nose strong ly to one side. An elliptical nose cross 
section that has width greater than height is desirable. Also, some sort of 
strake or sharp edge on each side of the nose tends to create symmetric vortices, reducing this problem. 
Wing-tip stalling should be prevented by the use of wing twist, fences, 
notches, or movable leading-edge devices. It is also desirable for depa rture 
prevention to have a substantial ventral -tail surface. 
llJl1H Spin Recovery 
After stall, a spin will develop in a "bad" airplane or a good airplane severely 
abused. Figure 16 .30 shows the forces acting in a fully developed spin. The 
fuselage and wing masses are represented by barbells. The centrifugal forces 
acting on the fuselage tend to raise the nose, further increasing the wing stall. 
The spin is primarily driven by the difference in lift between the outer, 
faster wing and the inner, slower wing, which is more fully stalled. The


<!-- p.636 -->

634 Air craf t Des ign: A Concep tual Approach 
Mor e 
li ft 
/ / 
/ / 
Centrif ugal / 
force 
/ / / / 
Spin 
Spin 
axis 
/ / 
Rudder deflection 
-?>-/ -:1.-0-/ 
o'-' / -.(/./ / 
Centrif ugal 
force 
Less 
lif t 
Fig. 16 .30 Forces in spin. 
spin is opposed by damping forces, primarily from portions of the aft fuselage 
and vertical tail undernea th the horizont al tail (SF- see Fig. 16.3 1). 
For recovery, the rudder is deflected against the spin. However, only the 
part of the rudder not blanketed by the stalled air from the horizo ntal tail will 
aid the recovery (SR1 and SR2). 
Figure 16 .32 presen ts an emp irical estimation of the required tail damping 
and rudder area for spin recovery for straight-winged aircraft. l124l This 
determines the minimum allowable tail-damping power factor (TDPF ), 
I:= -2 
Fig. 16 .31 Geome try for spin recovery estimation.


<!-- p.637 -->

CHAPTER 16 Sta bil ity, Control. and Handling Qual ities 635 
defined in Eq. (16 .67) where TDR is the tail damping ratio [Eq. (16 .68)] and 
VRVC is the unshielded rudder volume coefficient [Eq. (1 6.69 )]. The airplane 
relative density parameter µ, is defined in Eq. (1 6.70). 
TDPF = (TDR )(URVC) (16.6 7) 
(16 .68) 
(16.6 9) 
WjS µ, = -pgb (16.7 0) 
This empirical estimation techniqu e· is dominated by the ability of the 
rudder, vertical tail, and aft fuselage to oppose the aircraft's rotation in the 
spin. One can also delay spin entry or enhance spin recovery by reshaping 
the wing leading edges to minimize the lift imbalance, typically with a 
drooped leading edge near the wing tips. This, however, imposes some 
drag penalty during regular flight. 
TDPF 
{x l0-4) 
28 - Rudder alone 
24 
20 
16 
14 
8 
4 
0 
recovery 
Rudder and 
ele vator 
-240 -200 -1 60 -12 0 -80 -40 0 40 80 120 160 {x 10- 4) 
Wing heavy Body heavy Spin recovery [ lx- ly] 
crite rion lb2 W!g 
Fig. 16 .32 Spin recovery criteri a.


<!-- p.638 -->

636 Ai rcraf t Des ign: A Conceptu al Approach 
What We've Lea rned 
Calculation of the static margin tells you if the wing needs to be moved, while 
trim, pull-up, and turn calculations tell you if the elevator and horizontal tail 
are large enou gh. Lateral stability calculations tell you if the vertical tail, 
rudder, and ailerons need to be revised. 
Thunder bir d F-1 6 showing stro kes (U .S. Air Force photo) .


<!-- p.639 -->

Performance and 
Flight Mechanics 
• Performa nce equations ar e derived from simple physi cs, mostly Newton . 
• Ai rplane mus t meet design req uir emen ts such as sta ll, rate of climb , turn rate, 
acc eler ation, and ta keoff and landing dis tanc es . 
• En ergy ma neuver abil ity methods ar e powe rfu l tools for fig hter ana lysis and can als o 
optimi ze climb for tra nspor ts. 
In troduc tion and Eq uations of Motion 
T he previous chapter discussed stabil ity and control, which concerns 
the rotational motions of the aircraft. This chapter introduces flight 
mechanics, the study of aircraft translational motions. Here, we 
assume the airplane is stabilized and controlled to the desired angles of 
attack, bank, and sideslip. The question is: what does it do then? 
The geom etry for flight mechanics is shown in Fig. 17.1. Equations are 
written in a wind axis system, with the X axis being in the velocity direction 
and the Z axis being perpendicular and upwards. The climb angle y is the 
angle between the X axis and the horizon. The climb gradient G is the 
tangent of the climb angle and is found as the vertical velocity divided by 
the horizontal veloc ity. 
Summing forces in the X and Z directions yields Eqs. (17.1) and (17 .2). 
The resulting accelera tions on the aircraft in the X and Z directions are 
found from Newton (F = ma), determined by summing these forces then 
dividing by the aircraft mass (W/g): 
"i.Fx = T cos ( a + <PT) - D - W sin ')' 
"i.Fz = T sin ( a + </>y) + L - W cos ')' 
(17.1) 
(17.2 ) 
637


<!-- p.640 -->

638 Air c raft Des ign : A Con ceptu al Approach 
Vv= Vsin y 
VH= Vcos y 
v G=t an r= ..'.....ll 
VH 
Hor izon ta l 
Fig. 17 .1 Geome try for performanc e calculation. 
W =- CT 
T = PYJp/V = 550 bhp YJp/V 
(17 .3) 
(17. 4) 
(17 .5) 
Equation (17. 3) defines the time rate of change in aircraft weight as the 
speci fic fuel con sumption C times the thrust. For a piston-p ropeller 
engine, Eq. (1 7.4) determines the equivalent C based upon the piston- engine 
definit ion of Cpower or Cbhp (see Chapter 5), and Eq. (1 7.5) determines the 
thrust of the propeller. 
These simple equations are the basis of the most detailed sizing and performance programs used by the major airframe companies. The angle of 
attack and thrust level are varied to give the required total lift (including 
load factor) and the required longitudinal accelera tion depending upon 
what maneu ver the aircraft is to perform (level cruise, climb, accelerate, 
turn, etc.) . Angle of attack and lift are restricted by the maximum lift available. The thrust level is restricted to the available thrust , as obtained from 
a table of installed engine thrust vs altitude and velocity (or Mach number ). 
What makes the sizing and performance programs complicated is not the 
actual calculation of the aircraft response to the forces at a given angle of 
attack and thrust level. The complications arise in determining what the 
angle of attack and thrust level should be to perform some maneu ver.
