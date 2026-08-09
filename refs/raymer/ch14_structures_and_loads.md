# Raymer Ch.14 - Structures and Loads

*Converted from `Daniel P. Raymer - Aircraft Design_ A Conceptual Approach (2018, American Institute of Aeronautics and Astronautics Inc.) - libgen.li.pdf` by `tools/pdf_to_md.py`. Page markers are printed page numbers.*


<!-- p.491 -->

- ... 
f - Chapter 14 
-t 
Structures 
an d lo ads 
• Stron g- enough structur e is essenti al, but too strong is too heav y. 
• Loads definition is a cri tic a l and no ntriv ial task -bring in an expert. 
• The structur es g roup does the deta ils, but the configur ation designer does the overa ll 
struc tural ar ra ngement. 
• Classical struc tura l ana lysis is presented ; modern FEM is di scussed . 
In trodu ction 
I n a large aircraft comp any, the conc eptual designer might never do any 
structural analysis. The concept ual designer develops the overall structural arrangement, placing the wing box, major frames, and other key 
components, and then relies upon an experienced eye to ensure that sufficient space is provided for the required structural members. The only 
direct impact of structures during the initial stages of conceptual design is 
in the weights estimation. As will be shown in the next chapter, the statistical 
weights methods usually used in conceptu al design do not require any actual 
structural analysis. 
Designers at small aircraft companies and designers of homebuilt aircraft are more likely to perform an initial structural analysis as a part of 
the concept ual design process. This is espe cially true for a novel design 
concept such as the Rutan Voyager. To attain a design range of 26,000 
miles {48,000 km}, the Voyager needed an empty-weight fraction of 
about 0.20 (!) and a wing aspect ratio over 30. Clearly, the knowledge 
that this was structura lly pos sible was required before the design concept 
could be frozen. 
Before the actual structural members can be sized and analyzed, the loads 
they will sustain must be determined. Aircraft loads estimation, a separate 
491


<!-- p.492 -->

492 Aircraf t De sign : A Conceptual Approach 
discipline of aerospace engineer ing, combines aerod ynamics, stru ctures 
and weights. 
' 
In the past, the Loads Group was one of the larger in an aircraft company. 
Loads were estimated for each structural member of the aircraft using a combination of handbook techniques and wind-tunnel- data reduction. 
Today's computer programs have mechanized much of the timeconsuming work in loads estimation. Modern aero dynamic panel pro grams 
determine the airloads as an intermediate step toward determining aerodynamic coefficients. Also, modern wind tunnels employ compu terize d data 
reduct ion. These have reduced the workload so much that in some companies today there is no longer a sep arate loads group . 
However, loads estimation remains a critical area because an error or 
faulty ass umption will make the aircraft too heavy or will result in structural 
failure when the real loads are encou ntered in flight. 
This chapter intro duces the concepts of loads estimation and summari zes 
the subj ects of aircraft materials and structural analys is. This material is presented from the viewpoint of the conce ptual designer and is not intended to 
serve as a general introduction to structu res. 
Furthermore, many of the methods presented are no longer in regular 
usage, having been supplanted by finite element methods, as discussed at 
the end of this chapter. The older methods are useful, however, for approximating the correct answer to ensure that the finite element method results 
are in the right "ballpark ." Also, study of the classica l methods is useful for 
learning the vocabu lary of structural design. 
Loads Categor ies 
When one thinks of aircraft loads, the airloads due to gusts and high-g 
maneu vering immedia tely come to mind. While very impor tant, these loads 
are only a part of the total loa ds that must be withstood by the aircraft 
structure. 
Table 14. 1 lists the major load categories experienced by aircraft. Civil 
and military specifications define specific loading conditions for these categories, as discussed later. Key gov ernment documents for loads analysis 
are FAR Vol. III (23 and 25), Mil-A- 8860/8870, and NA VAIR SD-2 4. 
For each structural member of the aircra ft, one of the loads listed in 
Table 14.1 will dominate. Figures 14. 1 and 14.2 show typical critical loads 
for a fighter and a transport. Note that the lifting surfaces are almost 
always critical under the high-g maneu ver conditions. 
The largest load the aircraft is actually expected to encou nter is called the 
"limit" or "applied" load. For the fighter of Fig. 14. 1, the limit load on the wing 
occu rs during an 8-g maneu ver. To provide a margin of safety, the aircraft 
structure is always designed to withstand a higher load than the limit load. 
The highest load the structure is designed to withstand without breaking is 
the "design," or "u ltimat e," load.


<!-- p.493 -->

CHAPTE R 14 Structu res and Loa ds 493 
Table 14 .1 Aircraft Loads 
Ai rloads Landing Other 
Mane uver Vertica l load factor Towing 
Gust Spin -up Jacki ng 
Control deftection Spri ng-back Press urization 
Component in terac tion Crabb ed Bir d strike 
Buffet One wheel Actuation 
Hails tones (3/4 in. ) Arrested Crash 
Braking Fuel pressure 
Inertia Loads Takeoff Powerplant 
Acceleration 
Rotation 
Dynamic 
Vibr ation 
Fl utter 
Cata pult 
Aborted 
Taxi 
Bumps . 
Tur nin g 
Th rust 
Torq ue 
Gyrosco pic 
Vibration 
Duct pressu re 
Hamme rshock 
Prop /blade loss 
Seizur e 
In term ediat e fuselage 
Inb oar d wing n2 = 8 g, fuel pressur e 
nz = 8g M=0 .9 
buckling 
Canar d 
nz = 8g 
Can opy ------// 
bir dstrik e 
operat ing pressu re 
Forwa rd fuselage ---nz = 8g M = 0.9 
Nose boom ----nz = 8g 
deflec tion criteria 
wavi ness criteria 
ham mer s hock 
Fig. 14 .1 Typical fig hter limit loads. 
Vertica l yaw 
n2 = 1.0 M = 0.9 
AFT fuselage 
·-----, Control su rfaces 
n2 = B g M = 0.9 
-'8'11''--- Outboar d wing 
stiffn ess


<!-- p.494 -->

494 Ai rcraf t Des ign: A Concept ual Appr oach 
Positive 
dynamic 
gu st 
Positive maneu ver 
Negativ e and static 
man euv er gust 
and braking 
Neg ative 
mane uver 
Positiv e 
dyna mi c 
gu st and 
Landing Pos itive 
taxi, jackin g, mane uver 
and towi ng 
later al gu st 
Yaw man euver and 
late ral gu st 
Negative gu st 
Fig. 14 .2 LlOl l critic al loads. 
The "factor of safety" is the multiplier used on limit load to determine 
the design load. Since the 19 30s, the factor of safety has usually been 1. 5. 
This was defined in an Air Corps spec ification based upon the ratio 
between the ultimate tensile load and yield load of 24ST aluminum alloy 
and has proven to be suitable for other aircraft materials in most cases. For 
the fighter in Fig. 14.1, the design load for the wing structure would then 
be based upon a 12- g maneu ver, above which the wing would break. 
Ai r Loads 
A(QI Maneu ver Loads 
The greatest air loads on an aircr aft usually come from the generation of 
lift during high-g maneu vers or in response to an extreme gust. For many 
parts of the aircra ft, this lift-induced vertical acceleration will prove to be 
the "sizing criteria, " that is, the worse- case load that sets the structural 
stren gth requirement of the part. Even the fuselage is almost always structurally sized by vertical acceleration rather than by the air pressures produce d 
direct ly on the fuselage. 
Aircraft load factor n expresses the maneu vering of an aircraft as a multiple of the standa rd accele ration due to gravity (g = 32.2 ft/s 2 = 9.8 m/s2).


<!-- p.495 -->

CHAPTE R 14 Structu res and Loa ds 495 
Table 14 .2 Typical Limi t Load Factors 
Gener al aviation-n ormal 
Gener al aviatio n-uti lity 
Gener al aviation-aerobatic 
Homebu il t 
Transport 
Strat egic bomber 
Tactic al bomber 
Fig hter 
MIMlllJA 
2.5 to 3.8 
4.4 
6 
5 
3 to 4 
3 
4 
6.5 to 9 
nnegative 
-1 to -1. 5 
-1. 8 
- 3 
-2 
- 1 to - 2 
-1 
- 2 
- 3 to - 6 
The Wright Brothers designed their Flyer to a 5-g load, * performing 
careful structural calculations of the spars, struts, and bracing wires prior 
to flight. 
At lower speeds the highest load (actor an aircra ft can experience is 
limited by the maximum lift available. At higher speeds the maximum load 
factor is limited to some arbitrary value based upon the expected use of 
the aircraft. Table 14.2 lists typical limit load factors. Note that the required 
negative load factors are usually much less in magnitude than the 
positive values. 
The V-n diagram depicts the aircraft limit load factor as a function of 
airspeed and is a standard tool early in structural analysis. While we think 
of "calculating" the V-n diagram, in fact most of the diagram consists of 
parameters that we select, including maximum posit ive load factor, most 
negative load factor, and maximum dive speed. The pos itive and negative 
stall lines are calculated. The straight line from negative load factor at 
cruise speed, to zero load factor at dive speed, is a common assumption. 
The V-n diagram of Fig. 14.3 is typical for a general aviation aircraft. Note 
that the maximum lift load factor equals 1.0 at level-flight stall speed, as 
would be expected. The aircraft can be stalled at a higher speed by trying 
to exceed the available load factor, such as in a steep turn. 
The point labeled "high AOA'' (angle of attack) is the slowest speed at 
which the maximum load factor can be reached without stalling. This part 
of the flight envelope is important because the load on the wing is approximately perpendicular to the flight direction, not the body-axis vertical 
direction. 
At high angle of attack, the load direction can actua lly be forward of the 
aircraft body-axis vertical direction, causing a forward load compo nent on 
the wing structure (Fig. 14.4) . During World War I, several aircraft had a 
*That was probably an ultimate load by today's definitions. In a letter to his concerned father, 
Wilbur said, "I am constructing my machine to sustain about five times my weight." If it would 
break just beyond that, then it is a 5-g ultimate load, corresponding to a 3.33- g limit load. This is 
about the same as today's general aviation design practice.


<!-- p.496 -->

496 Aircr aft Design: A Conc ept ual Approach 
3 
vs tall 
1-g 
High AOA Max "q" 
Vequivalent = -pl Psi Vactua1 
vcruise 
Fig. 14 .3 V-n diagr am (ma neuver ). 
problem with the wings shedding forward due to this unexpected load. 
Velocity conversion methods are presented in Appendix C. 
The aircraft maximum spee d, or dive speed, at the right of the V-n 
diagram represen ts the maximum dynamic pressure q. The point representing maximum q and maximum load factor is clearly important for structural 
sizing. At this condition the aircraft is at a fairly low angle of attack beca use of 
v I::==> 
Body-axis forces 
Vertica l N = L cosa + D sin a 
Chor dwise C = D cosa - L sin a 
Low angle of attack 
Body axis vertica l 
High angle of attack 
Fig. 14 .4 Wing load dir ection at angle of attack.


<!-- p.497 -->

CHAP TER 14 Structu res and Loa ds 497 
the high dynamic pressure, so the load is approxim ately vertical in the 
body axis. 
For a subsonic aircraft, maximum or dive speed is typically 40-50% 
higher than the level-flight cruise speed. For a supersonic aircraft the 
maximum speed is typically about Mach 0.2 faster than maximum level-flight 
speed, although many fighters have enough thrust to accelerate past their 
maximum structu ral speed. 
Note that aircraft speeds for loads calculation are in "equivalent" airspeeds Ve. An aircraft airspeed indicator uses a pitot probe to determine airspeed from the dynamic press ure, so the "airspeed" as measured by a pitot 
probe is based upon the dynamic pressure at the aircraft's velo city and 
altitude and not the actual veloc ity. This dynamic pressure-based equivalent 
airspeed will be less than the actual airspeed at altitude due to the reduction 
in air density, as this expression descri bes: 
(1 4. 1) 
For loads estimation, Ve is a convenient measure of veloc ity because it is 
constant with respect to dynamic pressure regardl ess of altitude. However, 
pilots must convert Ve to actual velocity to determine how fast they are 
really flying. Also, the dynamic pressure as measured by a pilot tube has a 
compressi bility error at higher Mach numbers, so the "indicated" airspeed 
Vi as displayed to the pilot must be corrected for compress ibility to 
produce the equivalent airspeed Ve, which can then be con verted to 
actual airspeed. 
-lfif'..J Gust loads 
The loads experienced when the aircraft encoun ters a strong gust can 
exceed the worst maneuver loads in some cases. For a transport aircraft 
flying near thunderstorms or enco untering high- altitude "clear air turbulence," it is not unheard of to experience load factors due to gusts ranging 
from a negative 1.5 to a pos itive 3.5 g or more. 
When an aircraft experiences a gust, the effect is an increase (or decrease) 
in angle of attack. Figure 14.5 illustrates the geometry for an upward gust of 
velocity U. The change in angle of attack, as shown in Eq. (1 4.2), is approximately U divided by V, the aircraft velocity. The change in aircraft lift is 
Fig. 14 .5 Gust encounter.


<!-- p.498 -->

498 Air craf t Des ign: A Conc ept ual Approach 
shown in Eq. (1 4.3) to be propor tional to the gust velocity. The resulting 
change in load factor is derived in Eq. (14 .4) . 
Lia = tan 
- l U ::::: U 
v v 
1 2 1 Lil = 2pv S( Cr"Lia) = 2pVSCr" U 
Lin = Lil = pUVCr" 
W 2W/S 
(1 4.2) 
(1 4.3) 
(1 4.4) 
Figure 14.5 and Eq. (1 4.4) assume that the aircr aft inst antly enco unters 
the gust and that it inst antly affects the entire aircraft. These assum ptions 
are unrealistic. 
Gusts tend to follow a cos ine-like intensi ty increase as the aircraft flies 
through, allowing it more time to react to the gust. This reduces the acceleration experienced by the aircraft by as much as 40%. To account for this effect, 
a statistical gust alleviati on factor K has been devised and applie d to 
measured gust data (Ude> discussed later) . The gust veloc ity in Eq. (1 4.4) 
can be defined in the following terms [94l : 
where 
Subsonic: 
Supersonic: 
Mass ratio: 
K = _o_. 8_8_µ,_ 5.3 + µ, 
f.l l .03 
K= ---- 6.9 5 + µ,L0 3 
2(W/S) µ, = pgcCr" 
(14. 5) 
(14.6) 
(14.7 ) 
(14.8) 
The mass ratio term accoun ts for the fact that a small, light plane encou nters the gust more rapidly than a larger plane. 
The design requirements for gust velocities are "der ived" from flight-test 
data and are in "equi valent" airspeed (hence Ude)· Actual accel erations 
experienced in flight have been applied to Eqs. (14 .4- 14.8) to determine 
what the vertical gust ve locities must have been to produce those accelerations in the various flight-resea rch aircraft employ ed. 
For many years the standard vertical gust Ude has been 30 ft/s {9.1 m/ s} 
(posit ive and negativ e) . For most aircraft this produces roughly a 3-g pos itive 
load factor. This is still a suitable gust Ude for normal, utility, and aerob atic


<!-- p.499 -->

ft m 
50,000 15,000 
40,000 
10,000 
CH APTE R 14 Stru ctu res and Loa ds 499 
<IJ 30,000 
-0 
.3 
:;::; 
<( 
20,000 
5000 
10,000 
5 10 15 20 mis 
O +-----------------;----0 10 20 30 40 50 60 
Gus t verti cal velocity -Ude 
Fig. 14 .6 Derived equ ival ent gus t velocitie s (transpor t). 
ft/s 
civil aircraft at speeds up to cruise speed. For higher speeds it can be assumed 
that Uae drops line arly to 15 ft/s {4.6 m/s} at maximum dive speed. 
For transport and other classes of aircra ft, a more detailed requirement of 
Uae is shown in Fig. 14.6 (data from [95l ). Note that the expected gusts are 
reduced at higher altitud e. The maximum tur bulence speed Vg can be specified in the design requirements or can be a fallout parameter. 
One interesting point conc erning gusts is that, as shown in Eq. (14 .4), the 
load factor due to a gust increases if the aircraft is lighter. This is counter to 
the natural assumption that an aircraft is more likely to have a structural 
failur e if it is heavily loaded. 
In fact, the change in lift due to a gust [Eq. (1 4.3)] is unaffected by aircraft 
weight, so the change in wing stress is the same in either case. However, if the 
aircraft is lighter, the same lift increase will cause a greater vertical acceleration (load factor) so that the rest of the aircraft will experience more stress, 
the downward inertial reaction equal to the load factor times the weight of 
each part. 
Aeroelast ic effects can also influence the load factor due to gusts. An 
aft-swept wing will bend up under load, which twists the wing and reduces 
the outboard angle of attack. This reduces total lift and also moves the spanwise lift distribution inbo ard, reducing the wing bending stres s. An aft-swept 
wing will experience roughly 15% lower load factor due to a given gust than 
an unswept wing. 
The gust load factors as calculated with Eqs. (14 .4- 14.8) and using the 
appropriate Uae (po sitive and negative) can then be plotted on a V-n


<!-- p.500 -->

500 Air craf t Desig n: A Conceptual Appr oach 
3 
2 
n 1 
.... 1 
_.. _.. I _.. I 
_.. _.. I 
_.. I ----- r - ------' , I 
0 _,.,__,----------+---+--------..- V1 
.... 
.... 
-1 
' 
' 
' 
'---------Fig. 14 .7 V-n diagr am (gust). 
diagram as shown in Fig. 14.7. It is assumed that the aircraft is in 1-g level 
flight when the gust is experienced. Few pilots will "pull g" in severe turbulence conditions. The load factor between Vdive' Vcruise' and Vg is assumed 
to follow straight lines, as shown. 
In Fig. 14.8, the V-n diagrams of Figs 14.3 and 14.7 are combined to determine the most critical limit load- factor at each speed. Because the gust loads 
are greater than the assumed limit load, it might be desirable to raise the 
assumed limit load at all velocities, as shown by the dotted line. Remember 
that the structural design load factors will be 50% higher to provide a 
margin of safety. 
This method for estimation of gust loads is not as com plete or accurate as 
the methods used at most large aircraft companies. The more accurate 
Fig. 14 .8 Combined V-n diagr am.


<!-- p.501 -->

CHAPTER 14 Structures and Loa ds 501 
methods rely upon a power-sp ectral -de nsity approach in which the gusts 
are included in an atmospheric transfer function and the actual aircraft 
dynamics are modeled. However, the methods just presented are useful for 
initial analysis and provide an introduction to the more detailed techniques 
(see[96l ). 
ltf P Air Loads on Lifti ng Surf aces 
Now that the V-n diagram is complete, the actual loads and load distributions on the lifting surfaces can be determined. In most cases this needs 
to be done only at the high AOA and max q velocities (see Fig. 14.3) and 
any velocities where the gust load factor exceeds the assumed limit load factor. 
The first step involves a stabil ity-and-con trol calculation to determine the 
required lift on the horizo ntal tail to balance the wing pitching moment at the 
critical conditions. Note that the required tail lift will increase or decrease 
the required wing lift to attain the same load factor. 
Methods for estimating the lift on the trimmed tail and wing for a given 
load factor are prese nted in Chapter 16. These can be initially approximated 
by a simple summation of wing and tail moments about the aircraft center of 
gravity, ignoring the effects of downwash, thrust axis, etc. 
Once the total lift on the wing and tail are known, the spanwise and 
chordwise load distributions can be determined (Fig. 14.9). Wind-t unnel 
and aerodynamic panel program data are used if available. For initial 
design and design of light aircra ft, classical approximation methods give 
reasonably good results. 
Spa nwise 
li ft 
dis tribution 
Chor dwise 
li ft 
dis tribution 
Fig. 14 .9 Wing lif t dis tri but ion.


<!-- p.502 -->

502 Air c raf t De si gn: A Conceptual Approach 
Spa nwise 
lif t 
load 
Rect angular pla nform 
Plan form shap e 
/-Ellip tic -j Sp anwis e 
Ave rage -j- lif t 
--=-'-"---""l'---0:..:::..:.._ -- ·- ·. 
lo ad 
·---------- r ·-- :,; I ) ) I ---J 
Fig. 14 .10 Schrenk's appr oxi mat ion. 
According to classi cal wing theo ry, the span wise lift (or load) distributioi 
is propor tional to the circulation at each span station. A vortex lifting-Jin, 
calculat ion will yield the spanwise lift distribut ion. For an elliptical planforn 
wing, the lift distribution is of elliptical shape. 
For a nonelliptical wing, a good semi- empirical method for span wise loac 
estimation is known as Sch renk's approximation J97l This method assume. 
that the load distribution on an untwisted wing or tail has a shape that i. 
the average of the actual planform shape and an elliptic shape of the sam 1 
span and area (Fig. 14.10). The total area under the lift load curve mus 
sum to the required total lift. Equa tions (14 .9) and (14 .11 ) descr ibe th1 
chord dist ributions of a trapezoidal and elliptical wing. 
Trapezo idal chord: 
where 
Ellip tical chord: 
45 -(2y)2 C(y) = 'TTh v 1 - \ b) 
(14.9 
(14. 10: 
(14. 11 : 
Note in Fig. 14.10 that the load is assumed to continue to the centerline oi 
the aircraft. This has proven to be a good assumption in subsonic flight. Alsc 
remember that if subs tantial dihedral is used, the perpendicular load on thE 
wing is greater than the lift. Divide the lift by the cosine of the dihedr al anglE 
to get the perpend icular load. 
If a wing has subst antial geometric or aerod ynamic twist, the effect upon 
the spanwise lift distribution can be approximated by determining the load 
distribution when the wing is generating no net lift (the "basic load") and


<!-- p.503 -->

CH AP TE R 14 Structu res and Loa ds 503 
adding it to the "additional" load, which is determined as just shown for the 
net lift being produced. l98l 
When a twisted wing has no net lift, part of the wing is gene rating an 
upload (usually the inboard sect ion), and the rest of the wing is gener ating 
a download (usua lly the tips). The basic load can be approximated by ignoring the induced effects and basi ng the load at each spanwise station on the 
chord and section lift. The sec tion lift is the section lift coefficient times 
the section's twist angle with respect to the wing angle of attack when no 
lift is b eing generated. This no-l ift angle is approximately the angle of the 
mean aerodynamic chord and must be found by trial and error. 
Schrenk's approximation does not apply to highly swept planforms 
experiencing vortex flow. Vortex flow tends to greatly increase the loads at 
the wing tips. Loads for such a planform must be estimated using computers 
and wind tunnel s. 
The spanwise distribution of drag loads must also be consi dered, 
especially for fabric -covered aircraft in which drag loads are carried by 
internal "drag wires." Dr ag loads tend t? be greatest near the wing tips and 
should be determined from wind-tunnel or aerodynamic panel program data. 
As a first approximation, the spanwise distribution of drag loads can be 
roughly approximated as a constant 95% of the average drag loading from 
the root to 80% of the span, and 12 0% of the average loading from 80% of 
span to the wing tip. 
The aerodynamic interaction of various aircraft compo nents can produce 
additional loads. For example, the downwash from a canard will reduce the 
effective angle of attack of the inboard part of the wing. This moves the lift 
distribution of the wing outboard, producing greater wing bending stresses 
than expected. 
A vortex from a leading-edge strake can cause vibrational stresses on any 
component of the aircraft it touches. The F- 18 had a problem with verticaltail fatigue for this reason. A similar problem can occur due to propeller 
propwash. These effects are difficult to predict but must be consi dered 
during conceptual design. 
Once the spanwise load dist ribution is known, the wing or tail bending 
stress can be determined as described in a later section. To determine torsional stresses, the airfoil moment coefficient is applied to spanwise strips, 
and the total torsio nal moment is summed from tip to root. When windtunnel data are available, the torsional moments are summed from the chordwise pressure data. 
Actual chordwise pressure distributions for a NACA 4412 airfoil at 
various angles of attack are shown in Fig. 14.11. 
Mlfll Ai rloads Due to Contr ol Deflec tion 
Operation of the control surfaces produces airloads in several ways. The 
greatest impact is in the effect of the elevator on angle of attack and hence


<!-- p.504 -->

504 Ai rc raft Desig n: A Conceptual Appr oa ch 
-----Freestr eam 
Fr eestrea m 
Fr eestrea m 
Fr eestrea m 
NACA 441 2 
Fig. 14 .1 1 Airfoil chordwise pressures. 
a = -7d eg 
load factor. The rudder's effect on yaw angle can also impose large loads. 
Deflection of control surfaces produces additional loads direc tly upon the 
wing or tail structure. 
Maneuver speed, or pull-up speed Vp, is the maximum speed at which the 
pilot can fully deflect the controls without damaging either the airframe or 
the controls thems elves.* For most aircraft the maneu ver speed is less than 
the maximum level cruise speed Vr. 
Maneu ver speed Vp is established in the design requirements or can be 
selected using an empirical relationship, Eq. (14.12). In this old but useful 
equation, aircraft weight Wi s in pounds, and so if using mks units, first multiply kg by 2.2. Velocities are in feet or meters per second. Stall speed Vs is 
with high-lift devices deployed. The factor Kp is estimated in Eq. (1 4.13) 
but should not be allowed to fall below 0.5 or above 1. 0. For general aviation 
aircr aft, Kp usua lly does not exceed 0.9. 
5400 Kp = O.l5 + W + 330 0 
(1 4. 12) 
(1 4. 13) 
* Pilots beware: This has commonly been taught from the beginning of flight training as "do whatever you want, you can't hurt it below maneuvering speed," but that is not completely true. In the 
aftermath of the crash of AA Flight 587, an Airbus A300 that crashed when its vertical tail broke 
off upon encountering wake turbulence right after takeoff, the pilot was blamed for too aggressively 
using the sensitive rudder pedals to regain control. If he were alive to argue, he would say, "But I was 
always told ... . "


<!-- p.505 -->

CHAPTER 14 Structu res and Loa ds 505 
At the selected maneuver speed, a control analys is using the methods of 
Chapter 16 determines the angle of attack or sideslip obtained by maximum 
control deflection. The airloads imposed upon the structure can then 
be determined. 
Note that the instantane ous loads imposed by maximum aileron deflection while at maximum load factor (rolling pull-up) are frequent ly critical 
to the wing structu re. 
The maximum speed allowed with flaps down is also needed for 
estimation of the maximum loads on the flaps. Flap speed VJ will usually 
be twice the flaps- down stall speed. 
Control deflection will typically provide a change in section lift coefficient 
of about 0.8- 1.1 at 25-deg deflection. Estimation methods are provided in 
Chapter 16. 
In the absence of better data, the change in airfoil moment coefficient 
can be estimated as (- 0.0 1) times the control deflection in degre es. 
The additional load tends to be concen trated at the hingeline of the 
moving surface. Note that the deflecti9n of a control surface increases 
the load on the fixed part of the airfoil as well as on the moving 
control surface . 
For an aircraft with a manual flight-con trol system, the control loads can 
be limited by the strength of the pilot. For a stick -con trolled aircraft, the pilot 
strength is limited to 167 lb {0.7 kN} for the elevator and to 67 lb {0.3 kN} for 
the ailerons. For a wheel-con trolled aircraft, the pilot strength is limited to 
200 lb {0.9 kN} for the elevator and to 53 (times the wheel diameter) in.-l b 
{0.1 times diameter N-m} for the ailero ns. The rudder force is limited to 
200 lb {0.9 kN}. 
In addition to the maneuvering and control -surface loads just determined, the tail group of an aircraft is designed to withstand some arbitrarily 
determined loads at maneuver speed. These loads are based upon normal 
force coefficients Cn assum ing that the spanwise load distribution is proportional to chord length. For the horizo ntal tail, the required Cn values 
are (- 0.55) downward and (0.35) upward. For the vertical tail the required 
Cn value is (0.4 5). 
Ine rtial Loads 
Inertial loads come from the resistance of mass to acceleration, as 
described long ago by Newton (F =m a) . The various accelerations due to 
maneuver and gust, already descr ibed, establish the stresses for the aerod ynamic surfaces. 
Every object in the aircraft experiences a force equal to the object's weight 
times the aircraft load factor. This creates additional stresses throughout 
the aircraft, which must be determined. Note that the weight of the wing 
structure will produce torsional loads on the wing in addition to the aerod ynamic torsional loads .


<!-- p.506 -->

506 Ai rcraft Des ign: A Conceptual Appro ach 
Iner tial loads due to rotation must also be considered. For examp le, the tip 
tanks of a fighter rolling at a high rate will experience an outward centrifugal 
force. This force produces an outward load factor equal to the distan ce from 
the aircraft e.g. times the square of the rotation rate, divided by g. 
A tangent ial accele ration force is produced throughout the aircraft by a 
rotational accel eration such as is caused by a gust, a sudden elevator deflection, or by nose-w heel impact. This force is equal to the distance from the 
aircraft e.g. times the angular acceleration, divided by g. 
The loa ds produced by vibration and flutter are actually acceleration 
forces of a special nature. Calculation of these loads goes beyond this 
book. Proper design should avoid flutter and reduce vibrat ions to a negligib le 
level. 
Powerplan t Loads 
The engine mounts must obviously be able to withstand the thrust of the 
engine as well as the extra drag when stopped or windmilling. The mounts 
must also vertically support the weight of the engine times the design load 
factor. The engine mounts are usually designed to support a lateral load 
equal to one- third of the vertical design load. The mounts must withstand 
the gyrosc opic loads caused by the rotating machiner y (and prop eller) at 
the maximum pitch and yaw rates. 
For a propeller-po wered aircraft, the engine mount s must withstand the 
torque of the engine times a safety factor based upon the number of cylinders. 
This reflects the greater jerkiness of an engine with few cylinders when one 
cylinder malfunct ions. The torque moment load can be calculated from 
power and rotation rate. 
For an engine with two cylinders, the safety factor is 4.0; with three cylinders, 3. 0; and with four cylinders, 2.0. An engine with five or more cylinders 
requires a safety factor of 1. 33. These safety factors are multiplied times the 
maximum torque in normal oper ation to obtain the design torque for the 
engine mounts. 
For a je t engine, air loads within the inlet duct must be consi dered, as they 
will frequent ly bound a part of the flight envelope. At M3 at 65,0 00 ft 
{20,000 m}, the B-7 0 experienced inlet duct pressures of 4,320 psf 
{207 kN/m2}, which is 30 times the outside air pressure. 
A pressure surge known as "hammershock" is esp ecially severe. This is 
usually caused by pressure waves propa gating forward from a compr essor 
stall. "Duct buzz, " caused by shock waves bouncing in and out of the duct 
in rapid oscillation, can overstress the structure and cause loss of thrust. 
La ndi ng- Gear Loads 
The landing gear's main purpose is to reduce the landing loads to a level 
that can be withstood by the aircraft. The vertical load factor applied to the


<!-- p.507 -->

CHAP TE R 14 Structures and Loa ds 507 
airframe structure by the landing gear is actually something that we pick. 
When calcul ating the required shock absorber stroke, we select an acceptable 
gear load factor such as N = 3 (see Table 11. 5). This is used along with the 
worse-case landing sink rate to calculate the stroke. 
When analyzing aircraft structure, it can be assumed that the landing gear 
does its job and the vertical loads are limited to that selected load factor. For 
certificatio n the aircraft will prob ably be subj ected to drop tests, in which an 
actual aircraft is dropped from a height of somewhere between 9.2- 18.7 in. 
(23-48 cm} . The required drop distance typically will be 3.6 times the 
square root of the wing loading. 
While the purely vertical touchdo wn is very impor tant, there are other, 
less favorable landing scenarios that be examined. These include the 
extreme tail-do wn landing, a one -wheel landi ng, and a crabbed land ing. 
Another loading condition occurs when the tires contact the ground, they 
are not rotatin g. During the brief fraction of a second it takes for them to spin 
up, they exert a large rearward force by friction with the runway. This spin-up 
force can be as much as half the vertical force due to landing. 
When the tire is finally rotat ing at the correct speed, the rearward force is 
relieved, and the gear strut "spri ngs back" forward, overshooting the original 
position and producing a sprin g-back deflection load equal to or greater than 
the spin-up load. 
Another landing-gear load is the obvious braking load. This can be 
estimated by assuming a braking coefficient of 0.8, applied in a rearward 
direction at the bottom of the tires. The deceleration of the aircraft can 
also be calculated based upon its mass and the amount of aircraft weight 
applied to the braked tires, and that inertial reaction can be applied to all 
of the parts of the aircraft. 
The load on the landing gear during retraction is usually based upon the 
airloads plus the ass umption that the aircraft is in a 2-g turn. Other landinggear loads such as taxiing and turning are usual ly of lesser importance, but 
must be considered during detail design of the landing gear and suppor ting 
structure. 
Structu res Fundam ent als 
Timoshenko' s classic 19 30 book Strength of Materials [99] begins with this 
overall descr iption of the action of structural members: 
We assume that a body cons ists of small particles, or molecules, between 
which forces are acting. These molecular forces resist the change in the 
form of the body which external forces tend to produce. If such external 
forces are applied to the body, its particles are displaced and the mutual displacements continue until equilibrium is established between the external 
and internal forces. It is said in such a case that the body is in a state of strain. 
Thus, a structural member responds to a load by deforming in some fashion 
until the structure is pushing back with a force equal to the external load. The


<!-- p.508 -->

508 Air c raf t Des ign: A Conceptual Appr oa ch 
internal forces produced in response to the external load are called "stress," 
and the deformation of the structure is called "strain ." 
Figure 14. 12 shows the three basic types of structural loading: tension, 
compression, and shear. The meanings of tension and compression should 
be clear from the illustration. Shear can be viewed as a combinat ion of 
forces tending to cause the object to deform into two parts that slide with 
respect to each other. Scissors cut paper by application of shear. 
Figure 14. 12 also shows the load on a rivet, a typical example of shea r. 
Figure 14.13 shows three other types of structural loading. These can be 
considered as variations and combinations of tension, compressio n, and 
shear. Bend ing due to a load at the end of a beam is a combinat ion of 
tension and compression. The top part of the beam in Fig. 14. 13 is in compression, while the bottom part is in tension. 
Torsion is due to a combination of forces producing a moment (torqu e), 
which tends to twist the object. Torsion produces tangential shear forces that 
resist the torque. 
Thermal stresses are due to the expansion of materials with an increase in 
temperature. If a structural member is not free at one end, it will push against 
its suppo rts as it is heated. This produces compression loads. Similarly, a 
Tension 
Co mpr ession 
I'll 
- L 
, , 
I I 
L:::::::> p p ¢=:::::'{ : 
I 
I 
\ \ ' - Cross-sec tion ar ea A 
I'll 
-I 
I , 
p L:::::::> 
I I 
I I 
I I I 
' \ I 
Fig. 14 .1 2 Three basic struc tural load ings. 
¢=:::::'{ p


<!-- p.509 -->

CHAP TE R 14 Structu res and Loa ds 509 
p 
Heat 
add ition 
Fig. 14 .1 3 Other struc tur al loadings. 
severe reduction in material temp erature will produce tension loads unless at 
least one end is free. 
The unit stress (<T or F) is the stress force P per unit area [i.e., total stress 
divided by area-see Eq. (14 .14 )]. The unit strain (s or e) is the deformation 
per unit length [i.e., total strain divided by length-see Eq. (14 .15 )] . 
<T = P/A (14. 14) 
s= M/L (14. 15) 
The relationship between stress (load) and strain (defo rmation) is critically important to the desi gn of structure. Figure 14.14 illustrates a typical 
stress-strain diagram for an aluminum alloy. Over most of the stress 
range, the strain is directly propor tional to the stress (Hooke's law) , with a 
constant of propor tiona lity defined as Young's modulus, or the modulus of elasticity E [Eq. (14 .16 )] . 
(14. 16) 
The highest stress level at which the strain is propor tional to the stress is 
called the "prop ortional limit, " and stresses less than this value are consi dered 
within the "elastic range ." Within the elastic range a structure will return to 
its original shape when the load is removed. 
At higher stress levels a permanent deformation (set) remains when the 
load is removed, as shown by the dotted line on Fig. 14.14. The "yield 
stress" is the stress level at which a substantial permanent set occurs.


<!-- p.510 -->

510 Ai rc raft Design : A Conce ptua l Appr oach 
Yield stress is arbitrar ily defined as a permanent set of 0.002 in. per inc] 
{or meter per meter} and is typically only slightly higher than t he pro 
por tional limit. Above the yield stress is called the inelast ic range. 
Within the inelastic range, Hoo ke's law is no longer true, and th1 
modulus of elast icity can no lon ger be applied to Eq. (14 .16 ) to determin1 
the strain for a given stre ss. However, for some stress calculat ions it i: 
useful to define an artificial modulus called the tangent modulus Et, whicl 
is the slope of the stress- strain curve at a given point in the inelastii 
range. This modulus cannot be applied to Eq. (14 .16 ). The tangen 
modulus varies with stress and strain and is plotted in material -properti 
tables such as f 10°1 . 
· 
The ultimate stress is the highest stress level the material can withstan d 
Ultimate stress goes well past the elastic range. A material subj ected to it! 
ultimate stress will suffer a large and per manent set. 
For aluminum alloys, ultimate stress is about 1.5 times the yield stress 
If an aircraft is designed such that the application of a limit load facto1 
causes some aluminum structur al member to attain its yield stress, ther 
the ultimate stress will not be reached until a load factor of 1.5 time! 
the limit load factor is applied (i.e., at the design or ultimate load factor) 
However, when the aircraft exceeds its limit load factor, some structura 
elements will be permane ntly deformed and must be repaired after thE 
aircraft lands. 
The specific stren gth of a material is defined as the ultimate stress dividec 
by the material dens ity. The specific stiffness is defined as the modulus oJ 
elastici ty E divided by the mater ial dens ity. These parameters are us eful for 
comparing the suitab ility of various materials for a given application. 
Not all materials behave like the aluminum alloy of Fig. 14.14 . Composites such as fiberg lass and graphite -ep oxy will fracture without warning at 
a stress just past the propor tional limit )101 l as shown in Fig. 14. 15. ThesE 
Typical aluminum al loy 
Ultimate stress 
/ Fractu re 
o-stress 
Yield 
stress 
Proportio nal 
limi t 
/ 
L---f------------f- .s-str ain 
El astic Ine las tic ra nge 
ra nge 
Fig. 14 .14 Stress-str ain diagr am.


<!-- p.511 -->

·v; 
0. 
"' 
0 
"' 
"' 
- ..... 
Vl 
140 
120 
100 
80 
60 
40 
20 
Graph ite/e poxy 
E-glass /epo xy 
CHAPTER 14 Structu res and Loa ds 51 1 
Aluminum 2024 T3 
0 +-----J--+---+--+-----J--+---+--+-----J--+---+----+ 
0 O.Dl 0.02 0.03 0.04 0.05 0.06 0.07 0.08 0.09 0.10 0. 11 0. 12 
Str ain -in. fin. 
Fig. 14 .15 Com posite mater ial stress-stra in. 
materials do not have a "built -in" 1.5 safety factor, so a safety factor must be 
assumed for design purposes. 
Typically a safety factor for compo sites is assumed by desi gning to a stress 
level that provides a strain equal to two-thirds (i.e., 1/1. 5) of the strain at the 
ultimate stress level. If this stress level is higher than the propor tional limit, 
then the propor tional limit stress is used for desi gning to limit loads. 
When a material elongates due to a tension load, the cross- sectional area 
decreases as shown in Fig. 14. 16 (much exaggera ted) . Experimentation has 
shown that the ratio of lateral to axial strain is constant within the elastic 
range. This ratio (Poisson's ratio, µ, or v) is approxima tely 0.3 for steel and 
0.33 for nonferrous materials such as aluminum. 
The deformation due to she ar, which was not shown in Fig. 14. 12, is illustrated in Fig. 14. 17. At the top is a bar subj ected to a shear loading typical for 
a rivet, with a download and an upload sepa rated by some very small distan ce. 
These loads are assumed to be provided by loads applied to two plates (not 
shown) that the bar or rivet connects. 
The deformation of the bar is shown to the right. Shear intro duces a kink 
within the material. The deformation is not a change in length, as with 
tension or compression, but instead is an angular deformation (shearing 
strain, or y). 
The upper- right illustration in Fig. 14. 17 cannot be a complete free-b ody 
diagram because of the unbalanced moment of the two forces. Additional


<!-- p.512 -->

51 2 Air craft Des ign: A Conceptu al Approach 
p <=::::r- ................ .................. 
- p 
,---:i:I--- - - - - - -- f--t-;.jii " -- - -- p - Uni t length bar -,.- ........................ :,-.... . .. . . . . 
........................ : ..... , 
. 
. . . 
: 
Fig. 14 .16 Poisso n's ratio. 
forces must exist to balance this moment. The lower- right figure illustrates 
the total forces on a square element within the "kinked" portion of the bar. 
Again, the angle 'Y defines the shearing strain within the bar. The unit 
shear stress r is defined in Eq. (14 .17 ). 
These additional balancing forces, horizo ntal in the example in Fig. 14,17, 
are thems elves shear forces that must be resisted by the material, For a riveted 
wing spar, the rivets that attach the shear web to the spar caps must be 
designed to resist these shear forces. Simil arly, in a wood or compo site wing 
No load 
i . . 
( [ ) [) [) t 
t 
p 
y y 
- r r . I 
D ..... x 
! r - r 
--------------- x 
Fig. 14 .1 7 Shear defor mat ion.


<!-- p.513 -->

CH APTE R 14 Structu res and Loa ds 513 
boX the glue that attaches the upper and lower covers must resist these 
shear forces. 
Note in Fig. 14. 17 that the transverse deformation (i.e., Y direction) due to 
the shear stress is equal to the longitudinal distance (X direction) from the 
point of no shear, times the shearing strain angle y in radians because y 
is small. 
As with tension or compression, there is a linear relationship between 
shear stress and shear strain provided that the shear force is below the 
proportional limit. The shear modulus, or modulus of rigidity G, is defined 
in Eq. (1 4. 18). Also, it can be shown that the shear modulus is related to 
the modulus of elastici ty by Poisson's ratio, l99l as shown in Eq. (14.19). 
Material Sel ection 
T = Pshear /A 
G = r/y 
E G = ---2(1 + µ,) 
(14. 17) 
(14. 18 ) 
(14. 19) 
A number of properties are impor tant to the selec tion of materials for an 
aircraft. The selection of the "best" material depends upon the applicat ion. 
Factors to be considered include yield and ultimate strength, stiffness, 
density, fracture toughness, fatigue crack resistance, creep, corrosion resistance, temperature limits, producibi lity, repairabil ity, cost, and availability. 
Strength, stiffness, and dens ity have been discussed already. Fracture 
toughness measures the total energy per unit volume required to deflect 
the material to the fracture point and is equivalent to the area under the 
stress- strain curve. A ductile material with a large amount of inelas tic 
deformation prior to fracture will absorb more work energy in fracturing 
than a material with the same ultimate stress but with little inelastic 
deformation prior to fracture. 
A material subjected to a repeated cyclic lo ading will eventually experience failure at a much lower stress than the ultimate stress. This "fatigue" 
effect is largely due to the formation and propagation of cracks and is 
probably the single most common cause of aircraft material failure. There 
are many causes of fatigue, including gust loads, landing impact, and the 
vibrations of the engine and prope ller. 
Creep is the tendency of some materials to slowly and permane ntly 
deform under a low but sustained stress. For most aerospace materials, 
creep is a problem only at elevated temperatures. However, some titaniu ms, 
plastics, and compo sites will exhibit creep at room temper ature s. Creep 
deformation data are presented in materials handb ooks as a function of 
time, temperature, and stress loading.


<!-- p.514 -->

514 Ai rcr aft Desig n: A Conceptu al Ap proa ch 
Corrosion of aircraft materials has been a major problem since the early 
days of aviation. Aircraft materials are exposed to atmospheric moisture 
salt-w ater spray, aircraft fuel, oils, hydraulic fluids, batter y acid, enginexhaust products, missile plumes, gun gases, and even leaking toilets . 
Furthermore, elec trically dissimilar materials such as aluminu m and 
graphite-ep oxy compo site will experience galvanic corrosion in which an 
electrical current is formed that deteriorates the more anodic material 
' 
converting it into ions or an oxide. 
Corrosion of materials is greatly acceler ated when the materials experience a sust ained stress level. The corrosion products at the surface tend to 
form a prote ctive coating that delays further corrosion. When the m aterial 
is subj ected to a tension stress, however, cracks in the protect ive coating 
that accel erate the corrosion are formed. 
Once corrosion begins, it tends to follow cracks opened in the material by 
the stress. This "stress corrosion" can cause fracture at a stress level onetenth the normal ultimate stress level. For this reason it is impo rtant to 
avoid manu facturing processes that leave residual tension stres ses. 
Operating temper ature can play a major role in determining material 
suitabilit y. Stainless steel or some other high-temper ature material must be 
used as a firewall around the engine. For high-speed aircraft, aerodynamic 
heating may determine what materials can be used. Figure 14.18 shows 
typical skin temperatures at spee ds of Mach 2.2 and 3.0. 
The stagnation (total) tempe rature is the highest possible temperature 
due to aerod ynamic heating [Eq. (14 .20) ]. Actual skin temperatures are difficult to calcula te because they depend upon the airflow conditions, surface 
finish, and atmospheric cond itions. Figure 14. 19 provides a reaso nable 
675 B-70 at Mach 3 
- 600 
540 
240 250 250 
Conc orde at Mach 2.2 
Fig. 14 .18 Su pers onic skin temper atu res (°F) .


<!-- p.515 -->

<11 
" 
:::i .... 
:;:; 
<i: 
100 
90 
80 
70 
60 
50 
40 
30 
20 
10 
CHAP TER 14 Structu res and Loa ds 51 5 
0.5 1.0 1 .5 2.0 2.5 3 .0 3.5 4.0 4.5 5 .0 
Mach numb er 
Fig. 14 .19 Ski n-temperatu re estimate. Average valu es (°F), not leading edge. 
estimate of the expected skin tempe ratures over most of the airframe. 
Tstagnation = Tambient(l + 0.2M2) [Tin (0R) or{ K}] (14.2 0) 
Producib ility and repairabili ty are also impor tant in material selection. As 
a rule, the better the material proper ties, the more difficult it is to work with. 
For example, a major difficulty in the development of the SR-71 was in 
learning how to work with the selected titanium alloy. Simil arly, composite 
materials offer a large reduct ion in weight, but pose problems both in fabrication and repair. 
Cost is also important in material selection, both for raw material and fabrication. The better the material, the more it usually costs. Wood, mild steel, 
and standard aluminums are all relatively inexpe nsive. Titaniums and 
composites have higher cost. 
Another factor to consi der is material availability. Titanium and some of 
the materials used to produce high-temperature alloys are obtained from 
sometimes unfriendly or unstable countries, and it is possible that the 
supply might somed ay be cut off. Also, aircraft- quality wood, where every 
piece obtained will match the spe cification properties, is in fairly short 
supply these days. 
Figures 14.20- 14.22 illustrate the materials selected for the Rockwell 
proposal for the X-29. These are typical of modern desi gn practice for 
fighter aircraft, although composi te rather than metallic honeycomb panels


<!-- p.516 -->

5 1 6 Ai rc raft Design : A Con ceptu al Appr oach 
Al bul kheads 
(TYP) 
AI HC top 
ac cess doors 
Steel tube Al HC lo wer ac cess door 
Fig. 14 .2 0 Materi als -fore body. 
Heat shi eld 
STA 331 to 435 
Eng ac cess 
do ors (3) 
• Ext er nal skin . 
0.050 Al " ·(, 
0.020 cres· ht '· 
shield .., 
0.070 Al skin Al mach 
0.030 stain less 
\ 
0.070 Al skin s 
•l nn er skin-I 
Servi ce/i nsp . -.....,_,_ 
,,... 
,, ' 
panel .........._" ,; --- Over boar d drain (2 plac es) 
ven tra l fin 
atta ched to aft 
door (2 plac es) 
Fig. 14 .21 Mater ial sel ection -aft fuse lage.


<!-- p.517 -->

,?, / 
/' _,,/" / 
CHAPTER 14 Structu res and Loads 51 7 
Non -sta ndar d 
//<J, / 
// 
27 , 12' :> ,,,,,, n . . . , 
gr aph ite com posite 
skin 
U · \ , 
-\y- - fr- Al and fiber g lass (FG) 
le ading edge 
Fig. 14 .22 Wing mater ials. 
might be preferable today. Note the stainless-s teel heat shield and nozzle 
interface, required because of the high temp eratures around the engine. The 
alternative, seen on the F-22, is an all-titanium structure around the engine. 
Also, for a production fighter the windshield would be a bulletproof material. 
Material Propertie s 
This section covers vario us commo nly used aircraft materials. Tables of 
representative material properties are at the back of this section. 
MtQI Wood 
The Wright Brothers selected spruce as the prim ary structura l material 
for their aircraft, and it remained the material of choice for many years. 
Rarely used today in production aircraft, wood offers good strengthto-weight ratio and is easy to fabricate and repair. It is actually much like 
composite materials in that it has different proper ties in different directio ns. 
Wood makes a natural bending beam for wing spars because of the 
lengthwise fibers. 
The wooden Hughes H-4 Hercules Flying Boat was built like a modern 
composite aircraft. Multiple thin plies of wood were placed in molds along 
with a resin glue and subj ected to pressure during cure. Ply orienta tion 
was varied to give specific proper ties. 
The disadvantages of wood are its sens itivity to moist ure and its susceptibility to rot and insect damage. Wood must be regul arly maintained and


<!-- p.518 -->

518 Ai rc raf t Desig n: A Conceptual Approach 
should not be left exposed to the elements. The Hughes H-4 looks virtually 
new today because it was kept in a climate -con troll ed hangar. Also, wood is 
produced by nature with poor " qualit y control !" Each piece of wood is unique, 
so it requires crafts man-li ke skills to manufacture aircraft with wood. 
Toda y, wood is used largely in homeb uilt and specia lty, low-volume 
production aircraft. Wood has one additional advantage for homeb uilders 
in that almost everyone knows how to saw, drill, and glue wood. However, 
the various composi te materials have largely replaced wood in homebuilt 
aircraft. 
4flf J Aluminum 
Aluminum remains by far the most widely used aircraft material. It has an 
excellent strengt h-to-w eight ratio, is readily formed , is of mode rate cost, and 
is resistant to chemical corrosion. 
Aluminum is the most abundant metal in the Earth's crust, occurring 
mostly as silicates in clays. Disco vered in 18 27, it remained an expensive 
novelty until an elect rical extraction method was developed in 18 85. In 
18 56 aluminum cost $90 a pound. By 19 35 the cost had dropped to 23 
cents per pound. Inflation has raised this to several dollars per pound 
today depending upon its form. 
Being relatively soft, pure aluminum is alloyed with other metals for aircraft use. The most common aluminum alloy is 2024 (or 24ST), sometimes 
called "dur alumin." This 2024 cons ists of 93.5% aluminum, 4.4% copper, 
1. 5% manganese, and 0.6% magnesium. 
For high- strength applications, the 7075 alloy is widely used. The 7075 is 
alloyed with zinc, magnesium, and copper. Because the corrosion resistance 
is lessened by alloying, aluminum sheet is freque ntly clad with a thin layer of 
pure aluminum. Newer alloys such as 7050 and 7010 have improved 
corrosion resistance and streng th. An extensive discussion of aluminum 
alloys can be found in [102l . 
The strength and stiffness prop erties of aluminum are affected by the 
form (sheet, plate, bar, extrusion, or forging) and by heat treatment and 
tempering. In general, the stronger the aluminum, the more brittle it is. 
While composi te materials are considered the latest state of the art for 
lightweight aircraft structure s, there are new aluminum alloys such as 
aluminum- lithium that offer nearly the same weight savings and can be 
formed by standard aluminum techniq ues. The Eurofighter Typhoon uses 
aluminum- lithium in the wing and tail leading edges. Aluminum will 
remain impor tant in aircraft design for many years to come. 
4tm steel 
A major early advance in aircraft structures was the adoption of welded 
mild-steel tubing for the fuselage. Previousl y, aircraft such as the Sopwith


<!-- p.519 -->

CHAPTER 14 Structu res and Loa ds 519 
camel had fuselages of wire-braced wood construction that required constant maintenanc e. The steel-tube fuselage, used extensively by Fokker, 
greatly improved strength and required less maintenance. 
Today, steel is used for applications requiring high strength and fatigue 
resistance, such as wing attachment fittings. Also, steel is used wherever 
high temperatures are enco untered such as for firewalls and engine 
mounts. The Mach 3 XB-70 (Fig. 14.18) was constructed largely of brazed 
steel honeycomb. This material proved strong at high temperatures but 
was extremely difficult to fabricate. 
Steel is primarily an alloy of iron and carbon, with the carbon adding 
strength to the soft iron. As carbon content increases, strength and brittleness increase. Typical steel alloys have about 1 % of carbon. Other materials 
such as chromium, molybdenum, nickel, and cobalt are alloyed with steel to 
provide various characteristi cs. The stainl ess- steel alloys are commo nly used 
where corrosion resistance is impor tant. 
The proper ties of steel are strongly influenced by heat treatment and tempering. The same alloy can have mode rate strength and good ductility or can 
have much higher strength but at the expense of brittleness, depending upon 
the heat treatment and tempering employed. 
Heat treatment begins by raising the temperature of the steel to about 
1400-16 00°F {760-8700°C} at which poin t the carbon goes into solid solution with the iron. The rate at which the steel is then cooled defines the 
grain structure, which determines strength and ductility. 
If the steel is slowly cooled by steadily reducing the temperature in the 
furnace (a process called annealin g), a coarse grain structure is formed, 
and the steel is very ductile but weak. This is sometimes done before 
working with steel to make it easier to cut, drill, and bend. 
If the heated steel is allowed to air-cool (to be "nor malized "), it becomes 
much stronger but retains. good ductility. Welded steel tubing structure is 
usually normalized after all welding is completed to return the steel 
around the welds to the original strength. 
If quenched with water or oil, the steel becomes "martensitic" with a 
needle-like grain structure, great strength, and extreme brittleness. 
To regain some ductility, the steel must be tempered by reheating it to 
about 1000° F {538°C} for an hour or more. Standard heat-treatment and 
tempering processes are defined in material handbooks along with the 
resulting material proper ties. 
Steel is very cheap, costing about one-si xth what aluminum does. Steel is 
also easy to fabricate. 
MtQI Titanium 
Titanium would seem to be the ideal aerospace material. It has a better 
strength-to-w eight ratio and stiffness than aluminum and is capable of temperatures almost as high as steel. Titanium is also corrosion- resistant.


<!-- p.520 -->

520 Ai rcraf t Des ign : A Concept ual Appr oa ch 
However, titanium is difficult to form for these same reasons. Mo st titanium alloys must be formed at temperatures over l0 00°F { 538°C} and at 
very high forming stresses. Titanium is seriously affected by any impurities 
that might be accide ntly introduced during forming. One of the worst 
impu rity elements for "emb rittling" titanium is hydrogen, followed by 
oxygen and nitrogen. After forming, titanium must be treated for embrittlement by chemical "pickling" or through heat treatment in a controlled 
environmen t. 
Today, these problems are largely solved and titanium has become 
the preferred material for high temperature environmen ts such as fuselage 
structure around the engine, and for many fittings and complicated parts. 
Moder n mili tary aircraft have 10 -30% of their structure made from titanium 
(by weight) . 
Titanium is still relatively expensive, costing about five to ten times as 
much as aluminum per pound. In the past it was also more expensive to 
fabricate in titanium than aluminum due to tooling and handling issues. 
"Cost factors" of double or triple were applied to cost estimates of the same 
part designed in aluminum. Today the technolog y has impro ved, and the 
cost of titanium fabrication is ju st slightly higher than aluminum fabrication. 
To handle the aerod ynamic heating of Mach 3+ flight, the structure of the 
SR-7 1 is about 93% titanium. The XB-70 uses a substant ial amount of titanium 
in the fore bod y area. The midbod y of the F-22 is largely titanium due to engine 
heating. Titanium is extensi vely used in jet-engine componen ts and is also 
used in lower-speed aircraft for such high-stress airframe com pon ents as 
landing gear beams and spindles for all-mo ving tails. Because it does not 
cause galvanic corrosion with graphite -ep oxy, titanium is sometimes used 
as the sub structure to graphite -epoxy skins. 
Because of its material prop erties, titanium lends itself to a unique forming 
process called "sup erplastic forming/ diffusion bond ing" (SPF /DB). SPF /DB 
is a process where the titanium is placed in a press mold under extreme temperature and pressure such that it virtually "flows" to the shape of the mold. 
Furthermore, separ ate pieces of titanium are diffusio n-bonded at the same 
time, forming a jo int that is indistinguishable from the origina l metal. This 
process offers both cost reduction and the abilit y to form very compli cated 
parts, all having the good material prop erties of titanium. The Euro-fi ghter 
Typhoon uses SPF /DB titanium for its canards rather than the originally 
intended comp osites because of its better producib ility. 
Reference [1 03] gives a more detailed discussion of titanium and its 
alloys . 
4fQj Magne si um 
Magnesium has a good strength-to -weight ratio, tolerates high temperatures, and is easily formed, espe cially by casting, forging, and machining. It 
has been used for engine mounts, wheels, control hinges, brackets, stiffeners,


<!-- p.521 -->

CHAP TE R 14 Structu res and Loa ds 521 
fuel tanks, and even wings. However, magnesium is very prone to corrosion 
and must have a protective finish. Furthermore, it is flammable! 
Mil Specs advise against the use of magnesium except to gain significant 
weight savings. Also, magnesium should not be used in areas that are difficult 
to inspect or where the protecti ve finish would be eroded by rain (leading 
edges) or engine exhaust. 
ICfU High- Temper atu re Nic kel Allo ys 
Inconel, Rene 41, and Hastelloy are high-tempe rature nickel -based alloys 
suitable for hypersonic aircraft and reentry vehicles. Inconel was used extensively in the X- 15, and Rene 41 was to have been used in the X-20 Dynas oar. 
Nickel alloy honeycomb sandwich is used for the stealth nozzles of the F-1 17. 
Hastelloy is used primarily in engine parts. 
These alloys are substantially heavier than aluminum or titanium and are 
difficult to form. For these reasons, the space shuttle uses an aluminum structure with heat-prote ctive tiles. While a subst antially lighter structure was 
obtained, the difficulties experienced with the tiles should be noted by the 
designers of the next- generation shuttle. 
llQI Com posit es 
The greatest revolution in aircraft structures since the all-aluminum 
Northrop Alpha has been the ongoing adoption of compo site materials for 
primary structure. In a typical aircraft part, the direct substitution of graphite-epoxy composite for aluminum yields a weight savings of 25%. 
The F-22 and F / A- 18 E/F are about 25% composi tes by structural weight, 
while the newer F-35 is about 30% composi tes. The Boeing 787, today's 
state-of-the- art for com-ercial aircraft structure, is almost 50% compo sites 
by structural weight. 
Composites consist of a reinforcing material suspen ded in a "matrix" 
material that stabilizes the reinfo rcing material and bonds it to adjacent 
reinforcing materials. Composi te parts are usua lly molded and can be 
cured at room conditions or at elevated tempera ture and pressure for 
greater strength and quality. Figure 14.23 shows the two major composi te 
forms, filamen t-reinforced and whisker- reinforced. 
In the whisker-reinforced compo site, short strands of the reinforcing 
material are rando mly loca ted throughout the matrix. The most common 
example of this is chopped fiberglass, which is used for low- cost fabrication 
of boats and fast- food restaurant seats. Whisker reinforcing is sometimes 
used in advanced metal matrix compo sites such as boron -aluminum. 
Most of the advanced composites used in aircraft structure are of the 
filament-reinforced type because of outstanding strength-to -weight ratio. 
Also, filament compo sites can have their structural prop erties tailored to 
the expected loads in different direct ions.


<!-- p.522 -->

522 Ai rc raf t De si gn: A Con ceptu al Approach 
"whisk er" 
re infor ced 
or "fi ber" 
reinfor ced 
Fig. 14 .23 Com posite mater ial types. 
Fiber 
Matrix 
Metals and whiske r-r einforced compo sites are isotropic, having the same 
material prop erties in all dire ctions. Filament compo sites, like wood, are 
strongest in the direct ion the fibers are running. If a structural element such 
as a spar cap is to carry substant ial load in only one direction, all of the fibers 
can be oriented in that direct ion. This offers a tremendous weight savings. 
Figure 14.24 shows four common arrangements for tailoring fiber orientation. In part a), all fibers are aligned with the principal axis so that the 
composite has maximum streng th in that direction and has little strength 
in other direct ions. Arrangement b) offers strength in the vertical direction 
as well. 
In c), the fibers are at 45-d eg angles with the principal axis. This provides 
streng th in those two directions and also provides good shear strength in the 
principal axis direct ion. For this reason, this arrangement is commonly 
seen in a composi te-wing-box shear web. Also, the 45-d eg orie ntation is 
freque ntly used in structure that must resist torqu e. 
a) O deg b) O deg /90 deg LJ 
--1 -1- -111 11111 1.[L 
c) ±45 deg 
< < 
d) O deg/ ±45 de g/90 deg 
< £ < 
[-/ 
> > 
Fig. 14 .2 4 Composite ply tailor ing.


<!-- p.523 -->

CHAPTER 14 Structu res and Loa ds 523 
Arrangement d) combines b) and c), providing alternate layers (plies) of 
fibers at 0-, 45-, and 90-deg orient ations. By varying the number of plies at 
these orie ntations, the designer can obtain virtually any combination of 
tensile, compression, and shear streng th in any desired directio ns. 
Another ply-orien tation scheme uses plies that are 60 deg apart. Composites are sometimes designed with comp letely arbitrary ply directio ns to 
provide special characterist ics. 
Note that an odd number of plies is common ly used. This tends to reduce 
warpage, as has long been known by the makers of plywood. 
The common forms of fiber used in compos ite production are shown in 
Fig. 14.25 . The chopped form is simply sprayed or pressed into the mold. 
Unidirectional tape comes on large rolls and is placed in the mold by hand 
or by a robotic tape- laying machine. Tape is usua lly pre- impregnated 
("prepreg") with the matrix material. 
Fabrics can be bidirectional, with fibers running at 0 and 90 deg, or 
unidirectional, with the fibers running in one direction. (A few fibers run 
at 90 deg to bind the fabric together.) .Fabrics can also be prepreg. Fabrics 
are sometimes called "broad goods." 
Prepreg tape and fabric is typically about 0.005 -0.01 in. {0.0 1- 0.03 cm} 
thick per ply. 
In another form of composi te, the individual filaments are wound around 
plugs to form shapes such as missile bodies and golf club shafts. This is called 
"filament-wound" construct ion. 
There are a number of fiber and matrix materials used in composite 
aircraft structure. Fiberglass with an epoxy- resin matrix has been used for 
years for such nonst ructural componen ts as radomes and minor fairings. 
More recently, fiberglass-ep oxy has been used by homebuilders. 
Loose Batti ng 
Unidir ect ional 
fabric 
Unidir ect ional tape 
Bidir ect ional 
fabric 
Fig. 14 .25 Composite production forms .


<!-- p.524 -->

524 Ai rcraf t Desi gn: A Conceptual Appr oa ch 
While fiberg lass-epoxy has good strength characteristics, its excessive 
flexibil ity (tensile E) prevents its use in highly loaded structure in commercial 
or military aircraft. However, it is cheap and easy to form, and is suitable for 
some applicatio ns. 
The most commo nly used advanced compos ite is graphite -epo xy, called 
"carbon-fiber composite" by the British who developed it. Graphit e-epoxy 
compos ite has excellent strengt h-to-w eight ratio and is not difficult to 
mold. It is sub stantially more expensi ve than aluminum at the prese nt time 
(roughly 20 times) , but unlike metals, little material is wasted in manufacturing operations such as milling and cutting from flat patterns. 
Boron-epo xy was developed in the United States and initially used for 
complete part fabrication. An F- 111 horizontal tail and F-4 rudder were 
built of boron-epo xy. However, boron-epo xy cost s over four times as 
much as graphite- epoxy, so boron is used today largely to provide additional 
stiffness to graphite -ep oxy parts, especia lly in compression. 
Aramid, sold under the trade name Kevlar, is used with an epoxy matrix in 
lightly loaded applicat ions. Aramid has a low compression strength but exhibits much more gradual failure than other composi tes (i.e., less brittle). A 
graphite -aramid -epo xy hybrid composi te offers more ductilit y than pure 
graphite -ep oxy. It is used in the Boeing 757 for fairings and landing gear doors. 
Compo sites using epoxy as the matrix are limited to maximum temperatures of about 350°F {l 77°C} and normally are not used in applications where 
temperatures will exceed 26 0°F {12 7°C}. For higher-tempe rature appli cations, 
several advanced matrix materials are in development. The polyimide resins 
show great promise. One polyimide, bismaleimide (BMI), shows good 
strength at 350°F {17 7°C}. A material called polymide shows good strength 
at up to 600°F {3 15 °C} but is difficult to process. 
The matrix materials just described are all "thermoset" resins, chemical 
mixtures that "cure," producing a change in the material's chemist ry at the 
molecular level upon the applica tion of heat. The thermoset process is not 
reversib le. If the compos ite part is heated up again, the thermoset ting 
matrix does not revert to a liquid state. 
In contrast, a "thermoplastic" matrix material does not undergo a chemical 
change when heated. It merely "runs" and can be heated up again and 
reformed. Much like the plastics used in model airplanes, thermopla stic 
materials can be readily formed with heat. 
Thermop lastic materials include polyester, acrylic, polycarbonate, 
phen oxy, and polyethersulfone. Thermoplastic matrix materials can be 
used with the same fiber materials (graphite, boron, etc.) as the thermoset 
composites. Thermoplastics are espec ially good for higher tempera ture 
applications and where toughness is desired. The F- 11 7s were retrofi tted 
with graphite thermoplastic vertical tails, probably due to their proximity 
to the hot nozzles. Thermoset materials tend to be readily damaged, so 
thermoplastics are desirable for doors, access panels, and anywhere on the 
bottom where rocks can bounce up from the landing gear.


<!-- p.525 -->

CHAPTER 14 Structu res and Loa ds 525 
for higher-temperature, high-s trength applications, "metal- matrix composites" are in development. These use metals such as aluminum or titanium 
as the matrix with boron, silicon carbide, or aramid as the fiber. 
There is a never-e nding stream of improved composi te materials for 
aerospace applicat ions. We often put the word "advanced" in front of "composites" to indicate that, whatever the latest thing is, our design will use it! 
One of the newest things is called "Spread Tow" in which the fibers are 
spread out in a thin, flat uni- directional tow (untwisted bundle of fibers) 
aligned with the direction of load. This improves the mechanical proper ties 
and reduces the weight. Something similar can be done with tapes. 
Composi te materials offer impressi ve weight savings, but have problems 
too, one proble m being a reluctance to accept concen trated loads. Joints and 
fittings that smoot hly spread the concent rated load out over the composi te 
part must be used. If a compon ent such as a fuselage or wing has a large 
number of cutouts and doors, the fittings to spread out those concen trated 
loads can eliminate the weight savings. Wing attachment is another area 
where large and heavy metal fittings 111ust be used to spread the load out 
into the composite skins. This is especia lly true where a composi te wing is 
joined to a ring frame carrythrough structure. The Eurofi ghter (Typhoon) 
has about 70% of its structure built from graphite composi te and uses 
three large titanium root joints to attach each wing box to the fuselage 
carrythrough frames. 
Delamination is another issue. A composi te material is basic ally many 
layers of "clot h" all glued together. Sometimes these laminates come apart. 
This is especia lly proble matic if there are any voids, defects, or impurities 
in the laminates, but can occur just due to excess strain or some sort of 
impact. This problem can be minimized by using out-of -plane "stitching" 
but at a consi derable cost. Another approach uses carbon nanotube infusion 
to tie the laminates together. Cost and overall producibility are as yet 
unknown. 
· 
The strength of a composi te is affected by moisture content, cure cycle, 
temperature exposure, ultravi olet exposure, and the exact ratio of fiber to 
matrix. These are difficult to control, and every composite part will prob ably 
have slightly different properties. Manufac turing voids are difficult to avoid 
or detect, and the scrappage rate for compo site parts can be high (but is 
improving as composi tes are more widely used) . 
Composites in general are more likel y to be damaged than aluminum. 
Unfortunately, mild damage to compo sites can occur interna lly after some 
impact, yet not show up by outside visual inspect ion. For this reason, composites must be designed to carry their full limit load after such nondetectable 
damage. 
Furthermore, composi tes are difficult to repair because of the need to 
match strength and stiffness characteristi cs. A patch that is weak is obvious ly 
undesirable, but one that is overly strong can cause excessi ve deflection on 
adjoining areas . This can lead to fracture. Proper repair of an impor tant


<!-- p.526 -->

526 Ai rcraf t Desig n: A Concept ual Approach 
compos ite part requires running a computer program to ensure that the 
repaired part will match the original design specifications. 
The prop erties of a composi te material are not simply the algebraic sum 
of the prop erties of the individual ply layers. Actual material proper ties must 
be calculated using tensor calculus equat ions, such as are outlined in[l04J. 
Furthermore, extensive coupon testing is required to determine design 
allowables for the selected materials and ply orientation. Introduc tions to 
comp osites are provided in[l05,l06J . 
There is a designer's rule of thumb for compo sites called the "ten-p ercent 
rule" [lO?] which gives a quick and reaso nably good stre ngth approxi mation 
for typical composites. This rule is valid for composi tes with plies oriented 
at 0 deg (i.e., the direction of the load), 90 deg, and + /-45 deg, and 
assumes that the 0-deg plies contribute their full streng th while the other 
plies contribute only 10% of their full strength. In other words, simply add 
the number of plies times the streng th per ply, but multiply all plies that 
are not running in the direction of the applied load by 0. 10 . Needless to 
say, this rough approximation is only for ini tial sizing purposes and should 
never be relied upon for a final design analysis! 
Mftll Sand wich Cons truc tion 
While not proper ly classed a "materia l," sandwich const ruction has 
spe cial characteristics and is very impor tant to aircraft design. A structural 
sandwich is composed of two face sheets bonded to and separated by a 
core (Fig. 14.26) . 
Fig. 14 .2 6 Sandwich construc tion .


<!-- p.527 -->

CH APTE R 14 Structu res and Loa ds 527 
The face sheets can be of any material, but are typically aluminum, 
fiberglass-ep oxy, or graphite-ep oxy. The core is usua lly an aluminum or 
phenolic honeycomb material for commercial and military aircra ft, but 
various types of rigid foam are used as the core in some cases. Many homebuilt aircraft today are constructed of foam-core sandwich with fiberglass 
composite skins. Seventy percent of the B-70s airframe was stainl ess-st eel 
honeycomb sandwich, typically 2 in. {5 cm} thick. 
In a sandwich, the face sheets carry most of the tension and compression 
loads due to bending. The core carries most of the shear loads as well as the 
compression loads perpendicular to the skin. As with composi tes, joints and 
fittings are a problem with sandwich const ructio n. Analysis of sandwich 
construction is discuss ed in[108l . 
ltm Material Property Table s 
Tables 14.3-14 .5 provide typical material proper ties for various metals, 
woods, and composites. Note that these are typical values only, and that 
actual material proper ties for use in detail design should be obtained from 
the producer or from a specification document such as[100l . 
For example )100l contains 68 pages of desi gn data on 2024 aluminum 
alone, covering many different forms, heat treatments, tempering, gauges, 
etc. The values for 2024 in Table 14.3 are merely typical, suitable for rough 
estimates and studen t design projects. 
lfJ Structu ral-Analy sis Fundam entals 
Aircraft concept ual designers don't norma lly do the structural analysis 
for their designs, but they are respo nsible for the overall vehicle configuration 
including the major structural arrangement. Structure is critically important 
for the success of an airplane development projec t, and all designers conceptual or detail -should be familiar with the methods of structural 
design and analysis. 
The following sections will introduce the key equations for structural 
analysis of aircraft components. Derivations will not be presented as they 
are available in many references, such as[9s,99,i os] . 
4tll1ll Prope rtie s of Sections 
A number of geometric proper ties of cross sections are repea tedly used in 
structural calcula tions. Three of the most important- centroid, moment of 
inertia, and radius of gyratio n-are discussed next. Note that the cross sections of interest in tension and compression calculations are perpendicular 
to the stress, whereas in shear calculations they are in the plane of the


<!-- p.528 -->

Ai rcraft stee l (5 0.281 
Cr-M o-V) 
Low carbon steel 
I 
0.2 84 
I (AISI 10 25 ) I 
Low al loy steel 0.2 83 
(D6AC-wro ug ht) 
Chrom-moly steel (AISI 41 30) 
sheet/ pla te /tubing 0.2 83 
I 
wrought 
' 
0.2 83 I I 
Sta inle ss steel 0.2 82 
(AM-350) 
Sta in le ss (PH 15 -7 0.277 
Mo-sh eet/pl ate) 
Aluminum 
Al umin um-20 17 0. 10 1 
Clad 2024( 24 I 0.1 00 
I 
st)-( sheet/ pl ate) 
extrusions 0. 10 0 
606 1 T6 O. G98 
Table 14 .3 Typical Metal Properties (Room Temper atu re) 
[ Ftu 
Temp 10 3 
Lim its, °F psi 
10 00 260 
900 55 
10 00 220 
900 90 
900 18 0 
800 18 5 
600 19 0 
250 55 
250 61 
250 70 
250 42 
220 240 
36 36 
19 0 19 8 
70 70 
16 3 17 3 
15 0 15 8 
17 0 17 9 
32 32 
45 37 
52 49 
35 35 
15 5 
35 
13 2 
54 
10 8 
12 0 
12 3 
33 
37 
34 
30 
E 10 6 G 10 6 
psi psi 
30 11 
I 
29 11 
29 11 
29 11 
29 11 
29 11 
29 11 
10 .4 3.95 
10 .7 40} 
10 .8 4. 1 
10 0 4.0 
Commen ts 
Heat treat to l 850 °F 
Shop use only today 
Widely used 
Good corr osion resi sta nce 
B-70 hone ycomb materi al 
Widely used . weldable 
Affordable (homebuilt s) 
UI 
N 
QI) 
;r:: 
0 
9. 0 
CD 
CJ) 
ci5' 
:i 
)> 
0 
0 
:i 
() 
CD 
'U c 
Q 
)> 
'U 
'U 
0 
Q 
() 
::r


<!-- p.529 -->

Clad 7l 78-T6 (78 
st)-(she et/plate) 
extrusions 
Clad 707 5-T6-(sh eet) 
forgin gs 
extrusions 
Magnesium 
Mag nesi um HK 31A 
-HM 21A 
Titanium 
Titanium- Ti-6A l 4V 
-Ti- l3 V-l 1C r-3Al 
I 
I 
0. 10 2 
0. 10 2 
0. 10 1 
0. 10 1 
0. 10 1 
0.067 4 
0.0 640 
0. 16 0 
0.1 74 
High-temperature ni ckel al loys 
lnconel X-750 
Rene 41 
Hast ello y B 
0.3 00 
0. 298 
0.3 34 
I 
250 
250 
250 
250 
250 
700 
800 
750 
600-1 000 
10 00-1 500 
12 00-1 800 
14 00 
80 
84 
72 
74 
81 
34 
30 
16 0 
17 0 
15 5 
16 8 
10 0 
7 1 
76 
64 
63 
72 
24 
21 
14 5 
16 0 
10 0 
12 7 
45 
71 
75 
63 
66 
72 
22 
17 
15 4 
16 2 
10 0 
13 5 
48 
42 
43 
43 
42 
23 
19 
10 0 
10 5 
10 1 
10 7 
10 .3 
10 .4 
10 .3 
10 .0 
10 .4 
6.5 
6.5 
16 .0 
15 .5 
31 .0 
31 .6 
30.8 
3.9 } 
4.0 
39 } 
3.8 
4.0 
2.4 } 
2.4 
6.2 
11. 0 
12 .l 
Hi gh stren gth, not weldable, 
subject to stress 
corros ion 
High stren gth, not wel dable, 
common in hig h-speed 
air craft 
Hi gh-temp & stren gth 
subject to corros ion 
B-70 
SR-7 1 titanium 
X-15 
X-20, very dif ficult to form 
Engin e parts 
(") 
:c 
,.. 
.,, 
.... 
m 
::0 
.,.. 
CJ) 2 
(") -c 
(j) 
(J) 
c 
::J 
a. 
r0 
c 
a. 
(J) 
UI 
N 
"°


<!-- p.530 -->

UI 
w 
0 
2:'. 
'"' 
0 
'"' 
a 
CJ 
<D 
V> 
c.0· 
::; 
:I> 
0 
0 
::; 
Table 14 .4 Wood Properties (ANC-5) 0 
<D 
• 
-0 
..... 
c 
Q 
:I> 
-0 
-0 
1 .4 1 .46 0 
Q 
Ash 0.0 24 14 .8 8.9 7 .0 5.3 2 .3 
I 
1. 3 1 .78 0 
:; 
Bi rch 0 .026 15 .5 I 9.5 7.3 5.5 1. 6 
Afric an mahogany 0.01 9 10 .8 7.9 5.7 4.3 1 .4 1 .0 1 .28 
0.8 l. 70 Douglas fir 0.0 20 11. 5 8.0 7.0 5.6 1. 3 
I 
Western pine 0.01 6 9.3 6.0 5.3 4.2 0.8 0.6 1 .31 
Spr uce 0.01 6 9.4 6.2 5.0 4.0 0.8 0.7 1. 30


<!-- p.531 -->

Hi gh stren gth { ±-5 
Graphit e-epoxy 
Hi gh-mo dulus { ±-5 
Graphit e-epoxy 
Boroun-epo xy 0 
Gra phite-pol yimide 0 
S-Fi bergla ss-ep oxy 0 
E-Fi bergla ss-e poxy 0 
Ara mid- epoxy 0 
. Fsu (L T) 
Material ! l o3 psi 
Hi gh stren gth 12 
Graphit e-epoxy { 65.5 
Hi gh-mod ulus 9.0 
Graph ite-epoxy { 43 .2 
Borou n-e poxy 15 .3 
Graphit e-po lyi mide 8.5 
S-F ib ergla ss-ep oxy E-Fiber gla ss-epo xy 7 .9 
Ara mid- epoxy 9 
I 
: 
Table 14 .5 Typical Com posite Mate rial Proper ties (Room Temper ature) 
60 0.0 56 350 
60 0.056 350 23.2 
60 0.056 I 350 11 0.0 
60 0. 058 350 16 .9 
50 0. 073 350 19 5 
- - - 204 
- O. Q74 350 219 
45 0.071 350 10 5 
60 0 .052 350 200 
1 .... 1 
13 0. 0087 0. 0048 21 .00 1 .70 
- 0. 022 0.0 22 2. 34 2. 34 i 
10 0.0 046 0.0 025 25 .00 l. 70 
- 0. 01 2 0.01 2 2. 38 2.38 
13 0.0065 0.004 30 2.7 
- - 0.0036 20 1 .35 
11 - - 7.7 0 2.70 
- 0. 025 0. 01 9 4. 23 1 .82 
- 0. 01 8 0.006 11 0.8 
L = Longit udinal dir ecti on: T = trans verse dir ection: F;5u = in terla mi nate shear stress (ultim ate): t = ten sion; c = compr ess ion . 
23 .2 23.9 23.9 
4.0 10 0 20 
16 .9 18 18 
10 .4 353 40 
4 .85 111 18 .5 
I 
7.4 
I 
73.9 I 22 .4 I I I 
10 .2 69 33 
4.3 40 20 
mw•llJllH 
(") 
:i: 
> 
21 .00 1. 70 0.65 "O 
.... 
I m 
2. 34 2.3 4 5.5 2 
::0 
.... 
25.0 0 1 .70 0.65 
.,.. 
2 .38 2. 38 6. 46 
(/) 
_,. 
2 
30 2. 7 0.70 () 
_,. 
c 
17 .4 1 .4 0. 84 co "' 
6.80} 2.5 - 0 
::J 
4. 43 1. 8 0.51 Q. 
r11 0.8 0.3 0 
0 
Q. "' 
UI 
w


<!-- p.532 -->

532 Airc raf t Desig n: A Con ceptu al Approach 
shearing stres s. 
LX· dA x - l l 
e - A 
Ly·dA · Y. - l l 
e - A 
(14.21) 
(14.22) 
The centroid of a cross section is the geomet ric center, or the point at 
which a flat cutout of the cross-s ection shape would balance. The coor dinates 
of the centroid (Xe, Ye) of an arbitrary shape (Fig. 14.27) are found from Eqs 
(14 .21) and (14 .22) . A symmetrical cross section always has its centr oid on 
the axis of symmetry, and if a cross section is symmetric in two dire ctions, 
the centroid is at the intersection of the two axes of symmetry. 
A centroidal axis is any axis that passes through the centroid. An axis of 
symmetry is always a centroidal axis. 
Centroids for simple shapes are provided in Table 14.6 . The centroi d of a 
complex shape built up from simple shapes can be determined using Eqs. 
(14 .21) and (14 .22) using the centroids and areas of the simple shapes. 
The moment of inertia I is a difficult- to- define parameter that appears in 
bending and buckling equat ions. Moment of iner tia can be viewed as the 
cross -se ction's resistance to rotation about some axis, assuming that the 
cross-s ectional shape has unit mass. Moment of inertia is the sum of 
y 
Arb itra ry body 
Bisym me tric body 
Centroid 
---11-11""1-----Ye 
Fig. 14 .27 Section proper ty defi nitions.


<!-- p.533 -->

Table 14 .6 Proper ties of Simple Sections 
J _centroid_ Moment of Inertia _
_ 
_\ _Radiu s_- Gyration _
_ 
_ 
Illustrations Area I X Y Ix Iy Px Py 
-et 
H X 
. . y 
- I B I 
b 
:&· I I 
X B Y 
y 
R 
.. 
y , R 
H X 
-I I f 
B 
BH 
BH-bh 
wR2 
7r(R2 - r2) 
BH 
2 
B/2 H/2 
I 
B/2 H/2 
I 
R R 
R R 
I I I 
0 H/3 
I l 
BH3 HB3 H B - 12 12 v1i2 v1i2 
BH3 - bh3 HB3 - hb3 
J 
BH3 - bh3 
J 
HB3 - hb3 
12 12 12 (BH - bh) 12 (BH - bh) 
wR4 wR4 R/2 R/2 - 4 4 
I 
w(R4 - r4) w(R4 - r4) )R2 + r2 )R2 + r2 
4 4 2 2 
BH3 B3H H B - 36 48 v'18 v'24 
(') 
:::r: 
J> 
"'O 
... 
m 
::0 
CJ) c 
() c 
co 
(/) 
Q 
:::i 
Q. 
,..... 
0 
Q 
Q. 
(/) 
UI 
w 
w


<!-- p.534 -->

534 Air craf t Des ign: A Concep tual Approach 
the eleme ntal areas times the square of the distance to the select ed axis 
[Eqs. (1 4.23) and (14 .24) ] and has units of length to the fourth power. 
The polar moment of inertia (]o r Ip) is the momen t of inertia about an 
axis perpe ndicular to the cross section [Eq. (1 4.2 5)]; 1 is impor tant in 
torsion calculat ions. 
Ix = 2-yzdAi 
1y = 2-xz dAi 
Ip = J = 2-rf dAi = Ix + fy 
(14 .23) 
(14.24) 
(14.25) 
Note that there are two prop erties called "moment of inert ia." Here we 
refer to the "area" moment of inertia which is purely a prop erty of the 
geomet ry and is used in structural calcula tions. The "mass" moment of 
inertia, used in dynamic stabil ity calculations (Chapter 16), is a measure of 
a body's tendency to resist angular accelerat ions. I-a rea has units of 
length4 (area times leng th2), whereas I-mass has units of mass times length2. 
Structural calculations usually require the moments of inertia about centroidal axes. Table 14.6 provides moments of inertia for simple shapes about 
their own centroidal axis. For a complex built- up shape, the combined 
centroid must be determined, and then Eqs. (1 4.26) and (14 .27) can be 
used to transfer the moments of inertia of the simple shapes to the combined 
centroidal axes. The £ terms are the x and y distances from the simple shapes' 
centroidal axes to the new axes (see Fig. 14.27, bottom). 
Once the simple shapes' mome nts of inertia are transferred to the combined centroidal axes, the momen ts of inertia are added to determine the 
combined momen t of inertia (Ix and fy). The new 1 is determined from the 
new Ix and fy using Eq. (1 4.2 5): 
Ix = fxc +A e; 
fy =l ye +A e; 
(1 4.26 ) 
(1 4.2 7) 
The radius of gyration p is the distance from the centroidal axis to a point 
at which the same moment of inertia would be obtained if all of the 
cross -sectional area were concen trated at that point. By Eq. (14 .23), the 
moment of iner tia is the total cross -sec tional area times p squared, so p is 
obtained as follows: 
p= VTfA (14.2 8) 
The main use of p is in column-b uckling analysis. Also, the p values in 
Table 14.6 can be used to approx imate I for the given shapes. 
Other cross-s ectional proper ties such as the product of inertia and the 
principal axes will not be used in this overview of structures. See (98, 108] 
or other structures' textbooks for more information about section prop erties.


<!-- p.535 -->

JfJl1f I Ten sio n 
CHAP TER 14 Structu res and Loa ds 535 
Tension, the easiest stress to analyze, is sim ply the applied load divided by 
the cross-sectional area [Eq. (14 .14), repea ted next as Eq. (1 4.29 )]. The shape 
of the cross section is unimp ortant in most cases. 
The appropriate cross section is the smallest area in the loaded part. For 
example, if the part has rivet or bolt holes, the smallest cross- sectional area 
will probably be where the holes are loca ted because the areas of the holes 
are not included for tensiona l calculat ions. 
Usually the relevant cross section is perpend icular to the load. If a line of 
holes forms a natural "zipper" at an angle off the perpendi cular, the part 
might fail there if the cross -se ctional area along the zipper line is less than 
the smallest perpendicular cross section. 
a = P/A (14. 29) 
Remember that the stress level at the limit load should be equal to or less 
than the yield stress or, for comp osite materials, the stress level corresponding to a strain equal to the ultimate strain capab ility of the material divided by 
the selected factor of safety (often 1. 5, matching that used for metals). 
41111fl Compr ession 
The compression stress is also given by Eq. (1 4.29) (load divided by area) . 
For the determination of the limit stress, this equation can only be applied to 
parts that are very short compared to cross-se ctional dimensions (such as 
fittings) or to parts that are laterally constrained (such as spar caps and 
sandwich face sheet s). Long unco nstrained members in compression, 
called "columns" or "strut s," are discussed next. 
For short or laterally constrained parts in compression, the ultimate compressive strength is usuaUy assumed to equal the tensile value. For ductile 
metals this is a cons ervative assumption as they never actually fail, but 
merely "squish" out and suppor t the load by the increased area. 
Rivet and bolt holes are included in the cross-sec tional area calculation 
for compression because the rivets or bolts can carry compressi ve loads. 
Columns in compression usua lly fail at a load well below that given by 
applying the ultimate stress to Eq. (1 4.29). Columns in compression fail 
either by "prima ry buckling" or by "loca l buckling." 
An important parameter is the column's slenderness ratio: the column's 
effective length Le divided by the cross-sec tional radius of gyration [Eq. 
(14.30)]. The effective length of a column is determined by the end connections (pinned, fixed, or free) as shown in Fig. 14.28. 
Slenderness ratio: 
(14. 30)


<!-- p.536 -->

536 Air craf t Des ign: A Concept ual Appr oa ch 
0 
Pin 
. 
\ . 
. 
I 
. . 
I . 
0 0 
Free Pin 
I . . . I \ 
. . 
I 
. 
I 
. 
. . 
I 
I 
. 
. 
Fixed 
I 
Fixed 
0 
\ . . 
' . 
. 
I . , 
I 
. 
Fixed . 
I 
LE = O.S L Perfectly rigid 
LE = 0.71L Welded ends 
LE = 0.82 L Riv eted or bolt ed 
Fig. 14 .28 Column effective length . 
When you push down on an upright yardstick, the middle part bends 
outward in a direction perpe ndicular to the load. This bending action 
produces internal stresses much greater than the direct compression stress 
due to the applied load and is called "pri mary column buckling." If the 
bending action after buckling involves stresses below the prop ortional 
limit, the column is said to experience "elastic buckling." 
The highest compression load that will not cause this elastic column 
buckling-t he so- called Euler load, or critical load Pc-will be determined 
from the Euler column equation [Eq. (1 4.3 1)]. The resulting compressi ve 
stress is found from Eq. (14 .32) . 
Note in Eq. (14 .3 1) that the total load a column can carry without 
buckling does not depend upon either the cross-se ctional area or the ultimate 
compres sive stress of the material ! Only the column's effective length, its 
cross-se ctional moment of iner tia, and the material 's modulus of elasticity 
affect the buckling load if the column is long. 
n2EI n2E F -----c - AL- - (L/p)2 
(14.3 1) 
(1 4.32 ) 
The buckling stresses of Eq. (1 4.32) are failure stresses and do not have 
any margin of safety. For design purposes the limit loads should be 
reduced, usually to two-thirds of these values.


<!-- p.537 -->

CHAPTER 14 Structu res and Loa ds 537 
A column with an open or highly irregular cross section might fail at a 
lower load due to cross- sectional twisting or deformation. Methods for analysis of such members can be found in [106,l08J . 
Equation (1 4.3 1) implies that, as column length is reduced to zero, the Euler 
load goes to infinity. However, the compression stresses experienced due to 
bending in a buckled column are much greater than the applied load would 
directly produce. At some point, as column length is reduced the internal 
compressive stresses produced at the onset of buckling will exceed the pro portional limit, and the column will no longer be experiencing elastic buckling. 
This has the effect of reducing the buckling load compa red to the Euler load. 
The critical slenderness ratio defines the shortest length at which elastic 
buckling occurs. At a lower slenderness ratio, the stresses at buckling exceed 
the proportional limit. The column experiences inelastic buckling, so the 
Euler equation cannot be used as shown. The critical slenderness ratio 
depends upon the material used. It is about 77 for 2024 aluminum, 5 1 for 
7075 aluminum, 91.5 for 4130 steel, and 59-76 for alloy steel depending 
upon heat treatment. Most columns us.ed in aircraft are below these critical 
slenderness values, so the elastic Euler equation cannot usua lly be used in aircraft column analysis. 
The buckling load for inelast ic buckling can be determined by Eq. (1 4.32), 
with one modification. The modulus of elastici ty must be replaced by the 
tangent modulus, described earlier. As the tangent modulus is a function 
of the stress, iteration is required to find the buckling load for a particular 
column. However, handbook graphs such as Fig. 14.29 are usua lly used for 
design (see [10 0, 108]). 
As discussed at the beginning of this section, a very short "column" 
experiences pure compression without any danger of prima ry column 
buckling. This is sometimes called "block compressi on." The compression 
yield value is used as the -imit load, providing a cutoff value for the buckling 
load of a short column with either a solid cross section or with relatively thick 
walls (structural tubing) . A column can usua lly be considered in block 
compres sion if the slenderness ratio is less than about 12. 
When you step on an upright soda can, it fails in a form of local buckling 
called "cripplin g." The walls of the cross- section collapse without warning, 
and the load-c arrying ability drops to virtually zero. This is typical for short 
columns with very thin walls. Methods for estimation of thin-wall crippling 
are found inl 108l. A rough estimate for the crippling stress of a thin-wall 
cylindrical tube is shown in Eq. (1 4.33), where ti s the wall thickn ess and R 
is the radius. 
Fcrippling - 0.3( Et / R) (14. 33) 
A flat sheet or panel under compression fails by buckling in a manner 
similar to a column. The buc kling load [Eq. (14 .34)] depends upon the


<!-- p.538 -->

538 Air craf t Desig n: A Conceptual Approach 
160 
140 
120 
·v; 100 
c.. 
0 
0 
80 0 
:::. 
r.J.., " 
60 
40 
20 
0 
0 20 40 
Allo y steel 
Ftu = 18 0,000 psi } /, Ftu = 15 0,000 ps'. 
Ftu = 12 5,000 psi 
60 80 100 
Heat 
trea tme nts 
120 
Fig. 14 .29 Column buckl ing loads (rou nd tubing). 
140 
length a in the load direction, the width b, the thickness, and the manner in 
which the sides are constrained. 
Clamped sides cannot rotate about their axis and provide the greatest 
strength. Simpl y suppor ted sides are equivalent to a pinned end on a 
column and can rotate about their axis but cannot bend perpendicu larly. A 
free side can rotate and bend perpend icular ly and provides the least strength. 
Figure 14.30 provides the buckling coefficient K for Eq. (14 .34) based 
upon panel length-to-w idth ratio and end constraints. Most aircraft panels 
are clamped, but with some flexibility to rotate about the side axes. A K 
value between the clamped and simpl y supported values should be used in 
such a case. 
Fbuckling = KE ( t / h) 2 (14.3 4) 
4lll1fl Trus s Ana lysis 
A truss is a structural arrangement in which the structural members 
(struts) carry only compression or tension loads ("c olumns" and "ties "). In 
the ideal truss, the struts are weightless and connected by frictio nless pins. 
No loads are applied except at the pins, and no moments are applied 
anywhere. These ideal assumpt ions guarantee that the struts carry only 
compression or tension.


<!-- p.539 -->

CHAPTE R 14 Structu res and Loa ds 539 
The strut loads calcu lated with these ideal ass umptions are called primar y 
truss loads. Additiona l loads such as those caused by the attachment of an 
aircraft component to the middle of a strut must be calculated sep arately 
and added to the primary load during analys is of each individual strut. The 
impact of rigid welded connections in a typical aircraft applic ation is con sidered only in the definition of effective length in the column-buck ling 
equation (see Fig. 14.28). 
Truss structure was used extensively in welded steel-tube fuselages. 
Today the truss structure is largely used in piston- engine motor mounts, 
the ribs of large aircraft, and landing gear. 
Figure 14.31 shows a typical truss structure, a light aircraft motor mount. 
For illustration purposes this will be analyzed as if it were a two- dimensional 
12 
11 
10 
9 
8 
7 
K 
6 
5 
4 
3 
2 
1 
0 
0 
t 
/ Clam ped side s and ends 
One side cla mped, one side free, 
ends simply supported 
One side free, one si de and ends simp ly su ppo ed 
0.385 
2 3 4 
alb 
Fig. 14 .30 Panel buckl ing coefficient (NACA TN378 l ).


<!-- p.540 -->

540 Airc raf t Des ign: A Concep tual Appro ach 
truss with only the three struts shown. Analysis of three-dimension al space 
structures will be discussed later. 
The bottom of Fig. 14.31 shows an equival ent truss that includes the lines 
of force to the e.g. of the engine, and the vertical resist ing forces due to the 
rigid attachment of the fuselage and engine to the truss. This equivalent 
truss can be sol ved by several methods. 
The most general truss solution, the "method of jo ints," relies upon the 
fact that at each jo int of the truss, the sums of the vertical and horizo ntal 
forces must each total zero. 
To obtain a solution from the two equations (vertical and horizo ntal), the 
solution must begin at and always proceed to a jo int with only two unknown 
struts . The method usua lly begins at a free jo int with an applied external load, 
in this case at the engine load. 
Figure 14.32 shows the forces at the jo ints . All of the forces are shown as 
radiating outward from the join ts so that a pos itive force is a tension and a 
negative force is a compression. 
When summing forces at a jo int, the pos itive or negative force is added to 
the sum if it is up (when summing vertical forces) or to the right (when 
summing horizo ntal forces) and subtracted if down or to the left. Confusion 
about the appro priate sign is the most common error in truss analysis. (The 
author did jo int three wrong the first time!) 
Joint one is at the engine's e.g. The unkn own forces Fa and Fb must react 
to the engine load of 4000 lb. Solving the equations shown yields Fa of 
4400 lb (tension) and Fb of - 4400 lb (com pression) . 
Selection of the next jo int to analyze depends upon the number of 
unknown struts. At jo int three, there are three unkno wn struts at this 
n-gine = 4000 lb 
2 
22 _ _ _ _ 
: 1 o:' : 20 
0;·2----4000 1b 
50 4 
' 
: 30 
' 
' 
' 
51 
5 
Fig. 14 .31 Typica l truss structu re. 
Fuselage


<!-- p.541 -->

2 
l,fH = 0 = FA cos 27 + FB cos 27 
Uv = 0 = FA sin 27- F8 sin 27 - 4000 
FA = 4400 (T) 
Fs 
= -4400 (C) 
CHAP TER 14 Structu res and Loa ds 54 1 
Joint 2 
'LFH = 0 = Fe - FA cos 27 
'LFv = 0 =- FD - FA sin 27 
Fe = -3919 (T) 
FD= -2000 (C) 
Joint 3 
Fig. 14 .32 Method of join ts. 
time, so we select joint two. Solving the equations yields Fe of 3919 lb 
(tension) . Fd is found to be -2000 lb, a compression load on the engine 
due to the motor mount. If this load is in excess of what the engine can withstand, a vertical motor-mount strut should be welded between jo ints two 
and three. 
At joint three there are now only two unknown strut loads. Solving the 
equations yields Fe of 57-5 lb (tension) and Ff of - 9463 lb (com pressio n). 
In some cases, a quicker method can be emplo yed to determine the forces 
in selected struts without having to solve the whole truss as in the method of 
joints. This quicker method is actually two methods, the "method of 
mome nts" for the upper and lower struts and the "method of shears" for 
the inner struts . 
The top illustration of Fig. 14.33 shows the use of the method of moments 
to solve the force in the top strut of the motor mount. The whole structure is 
replaced by two rigid bodies con nected by a pin, with rotation about the pin 
prevented by the unkn own force in the strut under analysis. The moments 
about the pin are readily summed and solved for the unknown strut force, 
which is found to be 3919 lb. 
A similar technique is shown in the middle illustration for the lower strut, 
which has a load of 9463 lb. Note that this technique, where applicable, 
allows direct solution for the desired unknown forces. 
The lower illustration of Fig. 14.33 shows the use of the method of shears 
to solve for the inner strut. This method involves severing the structure along


<!-- p.542 -->

542 Ai rcraf t Des ign: A Con ceptu al Appr oa ch 
t--- 69.6 
LM = 0 = -69.9 (4000) - 30 FF cos 11 
4000 
4000 
-Fe 
.,..,..,- h? 
22° 
- 11 " 
-..... FF 
3o FF = -9463 
LFH = 0 = 3919.2 +F E cos 22 + (-9 463) cos 1 1 
h = 5775 
'LFv = 0 = -4000 +F E sin 22 - (-9 463) sin 11 
FE = 5775 
Fig. 14 .33 Method of moment s/me thod of shears. 
a plane that cuts only three members, the upper and lower strut and the inner 
strut under analysis. 
The severed part of the structure is analyzed as a free body, summing 
either the vertical and horizo ntal forces, which must total zero. Note that 
by calcul ating the unkno wn strut force bot h ways (vertical and horizontal 
summat ion), a check of your result can be made. This example gives a 
result of 5775 lb. 
These methods are only applicable if the truss structure is "statically 
determina te." In general, a truss is statically determina te if every strut can 
be cut by some plane that cuts only two other struts. This ensures that 
there is always a jo int with only two unknown struts, permitting solution 
by the method of joints. For "ind eterminate" trusses, more compli cated 
methods based upon deflection analysis can be used (see [98, 108]), or a 
finite element structural analysis can be performed (see Sec. 14.1 1). 
Once the loads in each member of the truss are known, the struts can be 
analyzed using the equations ju st presen ted for tension or compression. Use 
the approp riate effective length for welded, riveted, or bolted columns from 
Fig. 14.28. To provide an extra margin of safety, it is custo mary to assume 
that welded steel-tube motor moun ts act as though the ends were pinned 
(Le = L). 
The three- dimensional trusses, or space structures, are solved similarly to 
the two-dimensiona l truss. Square cross -sec tion three-d imensional trusses, 
such as a typical welded-t ube fuselage, can sometimes be solved separately 
in side view and top view as two-dimensiona l structures. The resulting


<!-- p.543 -->

CHAPTER 14 Structu res and Loads 543 
strut loads are then summed for the various members. This is permitted provided that the combined loads on all struts are within the elastic range. 
For more complicated three- dimensional trusses, the method of joi nts 
can be applied using three equations and three unknown strut loads. This 
involves simultaneous solution of equations, for example, with a simple computer iteration program. In some cases, the momen ts about some selected 
point can be used to obtain the solution with less effort. Space structures 
are discussed in detail in[9SJ . 
JJll•f J Beam Shear and Bend ing 
A common problem in aircraft desi gn is the estimation of the shear and 
bending stresses in the wing spars or fuselage. This is a two-step process. 
First, the shear and bending moment distrib utions must be determined, 
and then the resulting stresses must be found. 
Figure 14.34 shows a simple beam with a distributed vertical load. The 
beam is shown cut to depict internal .forces. The right side of the beam 
being a free body, the sum of the vertical forces, and the sum of the 
moments must equal zero. 
If the severed part of the beam is to remain in vertical equilibrium, the 
externally applied vertical forces must be opposed by a vertical shear force 
within the cross section of the material, as shown. Thus, for any span 
Su pport shear 
rea ction 
moment 
rea ction Moment rea ction 
due to spa nwise 
com pression and 
tension 
Fig. 14 .34 Shear and momen t in bea ms. 
Shear 
Moment


<!-- p.544 -->

544 Air craft Desi gn: A Conc eptu al Approach 
station the shear force is simply the sum of the vertical loads outboar d of that 
station, or the integral of a distributed load. 
The momen ts produced by the vertical loads must be balance d by a 
moment at the cut cross section. This moment is equal to the summation 
of the discrete loads times their distance from the cut station or the integral 
of a distributed load with respect to the distance from the cut. 
Figure 14.35 shows the typical loads on a wing. This shows the critical 
case of a rolling pull-up with the additional lift load of full aileron defl ection. 
The lift and wing-weight loads are distributed, while the nacelle weight is 
conc entrated. Remember that wing and nacelle weights are multip lied by 
the aircraft load factor to determine the load on the wing. 
The easiest way to calculate the shear and moment distribution along a 
wing is to replace the distributed loads (lift and wing weight) by conce ntrated 
loads. The lift distribution can be determined with Schrenk's approximatio n, 
ju st described. The wing weight will be determined in the next chapter and 
can be assumed to be distributed propor tional to the chord length. 
Figure 14.36 shows the trapezoidal approximation for a distributed 
load, giving the total equival ent force and the span wise location of that 
force. About 10 to 20 spanwise stations will provide an accurate enough 
approxim ation for initial design purposes. 
Once the distributed loads are replaced by conc entrated loads, determi nation of the shear and bending moment distribut ions is easy. The shear at 
lb /i n. t t t -iler on 
t 0 I 
I 
irl oad 
Actu al 
- t 0 -t Wing loads 
::::::...---"----J l wei ght 
lb ! V Nacel le 
t (f} 1 1 1 1 t--· ·t t 1 1 t t t ! c!--------:d 
lb 
t 
in. -Jb 
t 
"· _ J 
l t loads 
Shear 
=u 
Ben ding 
moment 
Fig. 14 .35 Wing loads, shear , and bending moment.


<!-- p.545 -->

b 
r=x -1 
F =S (a +b ) 2 
s ---X = s[2a + bl 
3a + 3bj 
a 
CH AP TER 14 Structures and Loads 545 
Fig. 14 .36 Trapezoidal ap proximation for 
dis trib uted loads. 
each span station is the sum of the vertical 
loads outboard of that station. The shear 
is found by starting at the wing tip and 
working inward, adding the load at each 
station to the total of the outboard 
stations. 
The bending moment can be found 
for each span station by multiplying the 
load at each outboard station times its distance from the span station. However, it is 
easier to graphic ally integrate by starting 
at the tip and working inward, adding to the total the area under the shear 
distribution at that statio n. 
Referring back to Fig. 14.34, the bending moment at a cross -sec tional cut 
is opposed by a combination of tension and compression forces in the spanwise directio n. For a posi tive bend ing moment such as shown, the internal 
forces produce compression on the upper part of the beam and tension on 
the lower part. The vertical loca tion in the beam at which there is no spanwise force due to bending is called the "neu tral axis" and is at the centroid of 
the cross- sectional shape. 
As long as the stresses remain within the elastic limit, the stresses vary 
linearly with vertical distance from the neutral axis regardless of the 
cross-sectional shape. These compression or tension stresses are found 
from Eq. (1 4.35) (for derivation, see [99] ), where Mi s the bending moment 
at the spanwise location and z is the vertical distance from the neutral axis. 
The maximum stresses due to bend ing are at the upper and lower surfaces. 
crx = Mz/Iy (1 4. 35) 
The vertical shear stresses within a beam are not evenly distrib uted from 
top to bottom of the cross section, so the maximum shear stress within the 
material cannot be calculated simply as the total shear divided by the 
cross-sectional area. 
Referring back to Fig. 14. 17, it should be remembered that the vertical 
shear stresses on an element are balanced by and equal to the horizo ntal 
shear stresses. One cannot exist without the other. Therefore, the vertical 
shear distribution must be related to the horizo ntal shears in the beam. 
Figure 14.37 shows a beam in bending, with the vertical distribution of 
compression and tension stresses. The total horizont al force on any 
elemen t is the horizontal stress at the element's vertical loca tion times the 
elemen tal area. If this beam is split lengthwise as shown, the upper section 
has only leftward forces, so a shear force must be exerted along the cut.


<!-- p.546 -->

546 Ai rcraf t De sign: A Concept ual Ap proach 
This shear force must be the sum of the horizo ntal stresses times th( 
element al areas above the cut. This reaches a maximum at the neutral axis. 
At the upper and lower surfaces, this shear force is zero. 
The bottom of Fig. 14.37 shows the resu lting vertical distribution of shear 
forces, expressed as magnitude toward the right. (Do not be confused by this 
prese ntation; the shear forces are exerted in a vertical direction, but we show 
the magnitude to the right to illustrate the distribution of magnitude from 
top to bottom.) 
T = - Jh/2 zdA bly z 
(14 .36) 
Equation (14 .36) describes this mathematic ally, where the integral term 
represe nts the area above the cut located at z = z1. Note that the distrib ution 
of shear stresses depends upon the shape of the cross section. For a beam of 
rectangular cross section, the maximum shearing stress (at the neutral axis) is 
1. 5 times the averaged shearing stress (total shear divided by cross-sec tional 
area) . For a solid circular cross section, the maximum shearing stress is 1.33 
times the averaged value. 
z 
-y x 
Bending 
stresses 
Shear 
stress 
dis tribution 
·_:::: E:> 
• Bending 
stresses 
Fig. 14 .37 Relation ship between shear and bend ing.


<!-- p.547 -->

CHAP TER 14 Structu res and Loa ds 547 
Spar ap proxima tions 
Q 
' ' 
' ' 
' ' 
k Be nding Shear 
Shear 
stress magni tude 
Fig. 14 .38 Typical ai rcraft spar in bend ing and shear. 
Figure 14.38 shows a typical aircraft wing spar consis ting of thick "spar 
caps" separated by a thin "shear web." The cross-sec tional area of the shear 
web is insignificant compared to the area of the spar caps, so the caps 
absorb virtually all of the bending force (stress times area) . The shear 
stress depends upon the cross-sec tional area above the point of interest 
and is therefore essen tially constant within the thin shear web, as shown to 
the right. 
In aircraft wing spar analysis, it is common to assume that the caps absorb 
all of the bending stresses · and that the web (exte nded to the full depth of the 
spar) absorbs all of the shear. This is shown at the bottom of Fig. 14.38. It is 
also assumed that the shear is co nstant within the web, and therefore the 
maximum shear stress equals the average shear stress (shear divided by 
web area) . 
The shear web will fail in buckling long before the material maximum 
shear stress is reached. Equation (14 .37) defines the critical buckling shear 
stress for a shear web. The value of J( is obtained from Fig. 14.39. 
Fshear buckle = KE ( t / b) 2 (14. 37) 
ltll1p Braced- Wing Ana lysis 
A wing braced with a strut will have the bending moments greatly 
reduced compa red to a fully cantilevered wing. However, the analysis is 
more complex because of the spanwise compression loads exerted upon


<!-- p.548 -->

548 Ai rcraf t Design : A Concept ual Appr oach 
the wing by the strut. This can increase the bending moment by as much as a 
third compared to an analysis that ignores this compression effect. 
Figure 14.40 shows a typical braced wing. The compression load P is the 
horizo ntal component of the force on the strut S. The vertical compo nent of 
S is found from summing the moments about the pin at the wing root , using 
the equival ent concen trated lift loads as discussed earlier. 
The shear loads of the braced wing are analyzed as before, taking into 
account the large conc entrated vertical load of the strut. The bending 
moment must be analyzed with special equations provided next. 
The por tion of the wing outboard of the strut is analyzed as before, and 
the bending moment at the strut loca tion is determined M2. The roo t 
bending moment M1 is usua lly zero unless the hinge point is above or 
below the neutral axis, causing a bend ing moment due to the compressio n 
load P. 
The lift distribution on the portion of the wing inboard of the strut must 
be approximated by a uniform load distribution w. This is usually a reaso nable approximation inboard of the strut. The following equations describe 
J( 
16 
14 
12 
10 
8 
6 
4 
2 
/ Sim ply sup po rted edges 
J I f l 
r f L; T 
2 4 6 
alb 
8 
.. 
10 
Fig. 14 .39 Shear web buckl ing (NACA TN37 81). 
+t 
t


<!-- p.549 -->

Lift di stri bution 
w 
CHAP TER 14 Structu res and Loa ds 549 
Fig. 14 .40 Brace wing analy sis. 
bending- moment distrib ution, maximum bending momen t, and spanwise 
location of the maximum bend ing momen d108l : 
where 
M(x) = Ci sin (x/j) + C2 cos (x/j) + wj2 
Di .2 M max = ( j ') + WJ cos x J 
tan (Xm) = D2 - D i cos (L/j) 
j · Di sin(L/ j) 
j = V£i7P 
D2 - D i cos(L/ j) Ci= -----sin (L/j) 
C2 = Di = Mi - wj2 
D2 = M2 - wj2 
(14.38) 
(14 .39) 
(14.4 0) 
(14.41) 
(14.4 2) 
(14.4 3) 
(14.4 4) 
From a design point of view, most wing struts seem to be set at around 40 
degrees up from horizon tal as seen from the front. If the angle is too flat 
(small) you get huge tension loads in the strut and large pulling foads at 
the side of the fuselage where it at taches. You also get a substantial compressio n load in the internal wing structure inboard of the strut attachment


<!-- p.550 -->

550 Ai rcraf t Desi gn: A Concep tual Approach 
which promotes spanwise buckling. With a more-hor izontal strut, the strut i: 
very long and runs close to the wing, so the strut drag is quite high. But if thi 
strut angle is too steep (vertical), you leave a lot of the wing still cantile verec 
and therefore still heavy. 
4lll1ff Torsion 
Figure 14.41 shows a solid circular shaft in torsion. The applied torque ] 
produces a twisting deformation cp that depends upon the length of the shaft 
As shown at the right of the figure, the torque is resisted by shearing stressethat increase linear ly with distance from the center-if the stresses remair 
within the elast ic limit. 
The shear stresses due to torsion are calculated with Eq. (14 .45) and are a1 
a maximum at the surface of the shaft (r = R). The angular deflec tion iii 
radians is determined from Eq. (14 .46) . These equations also apply to circula1 
tubing under torsion, using the approp riate value of Ip as provided earlier. 
T = Tr/Ip 
cp = TL/Gip 
(1 4.45) 
(14 .46) 
For a noncircular member under torsion, the analysis is generally much 
more complex. Several special cases can be readily solved. A thin-walled , 
closed, cross-s ectional member with cons tant wall th ickness t, total crosssectional area A, and cross- sectional perimeter s has shear stress and 
angular deflection as defined by Eqs. (14 .47) and (14 .48) . 
. 
I . . 
I . . 
I . . 
I . 
. 
I . 
I 
. . 
I 
T = T /2At 
In tern al shea r 
stresses 
Fig. 14 .41 Solid cir cu lar shaf t in torsion . 
(1 4.47) 
(1 4.48)


<!-- p.551 -->

CHAP TER 14 Structu res and Loa ds 551 
Table 14 .7 Tors ion Constants 
--1. 00 0.2 08 0. 14 1 
1 .50 0.231 0. 19 6 
l. 75 0. 239 0.214 
2.00 0.246 0.229 
2.5 0 0. 258 0.2 49 
3.00 0.2 67 0.2 63 
4 0.2 82 0.28 1 
6 0.2 99 0.2 99 
8 0.3 07 0.307 
10 0.31 3 0.31 3 
00 0.333 0.333 
Solid rectangular members can be analyzed with Eqs. (14 .49) and (1 4.50) 
using the values from Table 14. 7, where t is the thickness of the member and 
b is its width. These equations can also be applied to members bent up from 
flat sheet metal by "unwrapping" the member to find the total effective width. 
T T= --abt2 (14.4 9) 
TL 
<P = {3bt3 G (14. 50) 
Analysis of the torsional stresses in a complex shape such as a multicelled 
wing box goes beyond the scope of this book. See [1 08] for a discussion of 
such analysis. 
- Fin ite El emen t Struc tu ral Analy sis 
The structural- analysis methods just described, along with extensive 
handbooks and nomograms, have been used for many years for aircraft structural design. Today these methods are a dying art. Instead, virtually all 
major structural analysis is now performed using finite element comp uter 
programs. Even today's homebuilders have access to finite element programs 
using personal computers that are as powerful as the mainframe computers 
of the 1960s. 
The.fin ite element method (FEM) * is based upon the concept of breaking 
the structure of the aircraft into numerous small "elements," much like the 
*S tructural analysis using FEM is sometimes abbreviated as "FEA." Note that FEA and FEM also 
refer to finite element methods in other fields such as aerodynamics, but if not otherwise specified, 
most working engineers will understand FEM or FEA as structural analysis.


<!-- p.552 -->

552 Ai rc raft Desig n: A Concept ual Appr oa ch 
gridding of the air mass for CFD. Equations describing the structural behavior of these finite elements are prepared using various approximations of the 
end-const raints and deflection shapes for the element. 
The element equations are then linked together using matrix algebra so 
that the entire structure's response to a given external loading condition 
can be determined. The huge size of the matrices used for FEM analysis 
requires comp uters for solution of all but the most trivial cases. 
Figure 14.42 illustrates the more commo nly used finite elements. The aircraft structure must be modeled as a connected collec tion of one or more of 
these finite element shapes. 
Selection of which element type to use is a matter of engineer ing judgment. Unfortunatel y, the selection of the element type can influence the 
results. Also, the selection of the size of the elements requires experience . 
As a general rule, the size of the elements should be reduced anywhere 
that the stress is expected to vary greatly. An example of this would be in 
the vicin ity of a corner. 
Figure 14.43 shows an FEM example in which the major structural 
members of a propfan research aircraft are modeled using the rectangularplate finite element. As is the case for CFD gridding, the modeling of a 
comple x structure for FEM analysis can be very time consu ming. 
Detailed derivat ions of the equations for the various finite element types 
shown in Fig. 14.42 are beyond the scope of this book (see [10 9, ll O] ). A 
simple example, the one-d imensio nal bar, will be developed to illustrate 
the principles involved. l111 l 
Bar or 
bea m 
Solid 
tetra hedr on 
u 
c"' t -c 
Fig. 14 .42 Typica l fin ite eleme nts . 
Rect angular 
plat e 
Solid ring


<!-- p.553 -->

Fo rwa rd 
fuselage 
CHAPTER 14 Structu res and Loa ds 553 
Nacel le 
Aft 
fuse lage 
Fig. 14 .43 Typica l fini te element model (cou rtesy of Lockheed Mortin) . 
Figure 14.4 4 depicts a simple one- dimensional bar element with endloadings P1 and P2 and end- deflections U1 and U2. For a static structural 
analysis, P1 must equal the negative of P2, although this is not true in a 
dynamic analysis. The cross-s ectional area of the bar is shown as A. Note 
that although this example is a one- dimensional case, the deflected posi tion 
is depicted slightly offset for clar ity. 
The strain e is defined earlier in this chapter as the change in length 
divided by the original length L, as shown in Eq. (14 .5 1). The stress <r is 
L 
P, -( c----- ir-------- ---TJr'i 
I 
'---------------------------- - ------ -' 
r---1 I •I 
- Fig. 14 .44 Simp le one-dim ensiona l bar element.


<!-- p.554 -->

554 Air craf t Desi gn: A Concept ual Approach 
defined as the load divided by the cross- sectional area, and Young's modulus 
Ei s defined as the stress divided by the strain. This results in Eq. (1 4.52) . 
or 
s = (u1 - u2)/L 
E = a/E = (P/A)/ [(u1 - u2)/LJ 
EA P = - (u1 - uz) L 
(1 4. 51) 
(1 4. 52) 
(1 4. 53) 
Applying a load P1 yields Eq. (14 .54) . Similar ly, applying a load P2 results 
in Eq. (1 4.55). The change in signs of the deflections in Eq. (1 4.55) is due to 
the assumed direct ions of the two loads as drawn in the figure. 
EA P1 = y (u1 - uz) (1 4. 54) 
EA P2 = L ( -u1 + u2) (14 .5 5) 
Equations (14 .54) and (1 4.55) can be combined into matrix form as 
shown in Eqs. (14 .56) and (14 .57). The K matrix is called the stiffness 
matrix because it relates the amount of deflection to the applied loads. The 
values within the k matrix are called stiffness coefficients. 
The u matrix containing the deflection terms is called the "displace ment 
vector." The P matrix is the force vector. (Letters other than P and u are frequently used for these terms, but for some reason k is almost always used for 
the stiffness matrix.) 
{ P1 } [ EA/L 
P2 - -EA/L 
{P} = [k]{u} 
-EA/L] { u1 } EA/L uz (14. 56) 
(1 4. 57) 
The values E, A, and L are known, so the stiffness matrix is known. By 
inverting the stiffness matrix, the deflections can be found for any loading 
condition. 
This simple example could easily be sol ved by classical structure techniques. The power of FEM is in the ass emblage of numerous finite elements. 
Figure 14.45 shows a two-element assem blage using the one- dimension al 
bar element ju st developed. Two bars of different leng th and cross -sectional 
area are connected. The point where two (or more) finite elements are connected is called a "node" and is distinguished by the fact that at a node, the 
displacements of the connected finite elements are the same. Thus, u2 represents both the displacement of the right end of the first element and the 
displacement of the left end of the second element.


<!-- p.555 -->

CHAPTER 14 Structu res and Loa ds 555 
I L1 ----I-- Lz 
I 
P,-( ® P,Jc
.____
: _......_® 
(j- P3 
H H 
Fig. 14 .45 One-d ime nsional bar FEM ass embly. 
H 
From Eq. (14 .56), the matrix equations for the left- and right- side 
elements can be written as Eqs. (14 .58) and (14 .59) . 
(14.58) 
(14 .59) 
Now the matrices can be assembled by merging the element matric es. 
This is shown in Eq. (14 .60) . Note that the "overlapping" terms at the node 
result from the nodal condition of identical deflection (u2 in this case) . 
These overlapping terms are added in forming the assembled matrix. 
-EAi/L1 (EAi/ L1 + EA2/ L2) -EA2/L2 
(14.6 0) 
This completes the FEM development for this example. The remaining 
work is strictly computation based upon the actual values of the variables 
in a given design problem. For example, Fig. 14.46 shows a two-bar structure 
in which the right side attaches to a wall, loads are as shown, and 
the dime nsional and material values are as indicated. This produces the following: 
(- 2.5 x 107) 
(3.4 x 107) 
(- 9. 2 x 106) 
(- 9.2 °x 106)1 x { :-} 
(9.2 X 106) U3 
(14 .61) 
The 3x 3 stiffness matrix in Eq. (14 .61) can be inverted to find the deflections for any loading. This would first require determining the unknow n 
wall-reaction load P3.


<!-- p.556 -->

556 Aircr aft Desi gn: A Concep tual Appr oach 
12 in. --- ---- 14 in. ____ _.,_, 
A1 =2 8 in. 2 
A2 = 12 in. 2 
H H 
P1 = 400,000 lb P2 = 300,000 lb Aluminum: E = 10.7 x 106 psi 
Fig. 14 .46 FEM example. 
Alterna tively, we can simplify the FEM matrix solu tion by noting that the 
deflection at the wall u3 is zero, so we can eliminate the third row and the 
third column from the matrix. This produces Eq. (1 4.62) with a 2x 2 stiffness 
matrix. 
{Pi } = [ (2.5 x 107) (-2.5 x 10 7)] { u1 } P2 (- 2.5 x 10 7) (3.5 x 10 7) u 2 
[ --:- : --=-j --:- : --=-j] { ;- } = { :- } 
{ 0.0 93 } = { u1 } 
0.0 77 u2 
(1 4. 62) 
(1 4. 63) 
(1 4.6 4) 
In Eq. (1 4.63) we have found the inverse of the reduced k matrix. By 
substituting the actual values of the loadings P, we determine the deflections 
as provided in Eq. (14 .64) . We can then use the deflections of the nodes to 
solve for the strain and stress, as follows: 
El = (0.0 93 -0.0 77) /12 = 0.0013 
E2 = (0.077-0 )/1 4 = 0.0 055 
u1 = 14,267 psi 
u2 = 58,850 psi 
(1 4.6 5) 
(14.6 6) 
(1 4. 67) 
(1 4.6 8) 
This one- dimensional example does not illustrate the compl ications 
caused by three- dimensional geom etry. For this simple example the deflections at the nodes produce identical changes in the length of the bars. 
Were the bars connected at some angle, the identical nodal deflections 
would produce different changes in bar lengths. Matrix direct ion- cosine 
terms must be used to keep track of these three- dimensio nal effects.


<!-- p.557 -->

CHAPTER 14 Structu res and Loa ds 557 
Most finite element analyses use surface elements rather than simple bar 
elements. The triangle element shown in Fig. 14.42 is typical and allows a 
complicated structure to be broken into numerous connected elements. 
These elements are assumed to be connected at the nodes (corners) where 
the deflections are identical. 
Equations are prepared in matrix form describing how each element 
responds to loadings at its nodes. The element stiffness matrices are combined using appropriate direction cosine terms to account for threedimensional geome try, and the combined matrix is inverted to solve for 
the deflections for a given loading. 
For dynamic analysis, mass and damping terms are developed using 
matrix metho ds. These greatly increase the number of inputs required for 
the analysis. 
Fortunately, working structural engineers do not need to develop their 
own FEM program every time they wish to analyze a structure. There are 
numerous FEM programs available, many of them integrated into high-end 
CAD program s. 
The indus try-standard FEM program has long been the NASTRAN 
(NASA Struct ural Analysis) program. NASTRAN handles virtually everything but requires substantial experience to ensure that the results are meaningful. Versions of NASTRAN are linked to or integrated within a number of 
CAD programs and analysis suites. 
What We've Learned 
We've been shown how to do the overall structural arrangement on the 
Dash-One layout, how to define the loads, and the classical methods of structural analysis. Finite elem -nt methods provide better answers late r on. 
Worl d's lar gest ai rcraft as of now-Antono v An-225 Mriya (Dream) (U .S. Air Force pho to) .


<!-- p.558 -->

558 Aircr aft De sign: A Conce ptual Appr oach
