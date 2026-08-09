# Raymer Ch.17 - Performance and Flight Mechanics

*Converted from `Daniel P. Raymer - Aircraft Design_ A Conceptual Approach (2018, American Institute of Aeronautics and Astronautics Inc.) - libgen.li.pdf` by `tools/pdf_to_md.py`. Page markers are printed page numbers.*


<!-- p.641 -->

CHAPTER 17 Performance and Fligh t Mech an ics 639 
for example, the rate of climb varies with velocity. What combination of 
velocity and thrust setting will allow an airliner to climb to cruise altitude 
with the least fuel consumption over the total mission ? This chapter will 
address such performance issues. 
For normal aircraft the thrust force is nearly aligned with respect to the 
wind axis under most flight conditions. This is by design. Airplanes are 
most efficient when the engines push, the wings lift, and neither tries to do 
the other's job! This permits simpli fying Eqs. (17.1) and (1 7.2) to the forms 
shown in Eqs. (1 7.6) and (1 7.7) . 
lFx = T - D - W sin y 
lF2 = L - W cos y 
(17 .6) 
(17 .7) 
Here is a word of caution: be espec ially careful with fps (British) units in 
the performance calculat ions. Apply each equat ion to the units of the data 
you are using to be sure that all units cancel, leaving you with the units of 
the desired answer. Be wary of equations involving horsepower. Anytime 
the constant "55 0" appears in an equation, the other units must be converted 
to feet, pounds, and seconds (1 bhp = 550 ft-l b/s). The more logical metric 
system avoids such confusion. Another poten tial source of confusion is 
the specific fuel consumption C, which is usua lly given in units of hours - l 
(actually lb-fuel per hour per lb-thrus t!). This must be divided by 3600 to 
yield seconds -1 . 
Also, see Author's Note on use of metric equivalent units at the beginning 
of the book. Terms involving mass or weight can be confusing, and some of 
the equations having g would not require it with approp riate metric units. 
ilfl1 Steady Leve l Fl igh t 
If the aircraft is flying in unacce lerated level flight, then climb angle y 
equals zero, and the sum of the forces must equal zero. This leads to Eqs. 
(17.8) and (17 .9), the most simple versions of the translational equations of 
motion. They state simply that, in level flight, thrust equals drag and lift 
equals weight. These are expressed using aerod ynamic coefficie nts for the 
analysis that follows. 
T = D = qS( CD0 + KCz) 
L = W = qSCr 
(17 .8 ) 
(17 .9 ) 
(17. 10) 
From Eq. (1 7.9), the velocity in level flight can be expressed as a function 
of wing loading, lift coefficient, and air densi ty [Eq. (17. 10)] .


<!-- p.642 -->

640 Air cr aft Design : A Conceptual Appro ach 
These equations imply that the actual T / W in level flight must be thE 
inverse of the L/D at that flight cond ition [Eq. (17.1 1)]. The T/W and L/L 
in level flight can be expressed in terms of the wing loading and dynamic 
pressure by substituting Eq. (1 7.9) into Eq. (1 7.8), as follows: 
T 1 qCDo (w) ]( 
W = L/D = (W /S) + S q 
Mfljl Minimum Th rust Req uir ed for Leve l Fl ight 
(17.1 1) 
From Eq. (17 .11) it follow s that the condition for minimum thrust at a 
given weight is also the cond ition for maximum L / D. To find the velocity 
at which thrust is minimum and L / D is maximum, the derivat ive with 
respect to veloc ity of Eq. (17 .11) is set to zero. This is shown in Eq. (17 .12) 
and solved in Eq. (17.13 ) for the velocity at which the required thrust is 
minimum and the L/ D is at a maximum. 
o(T /W) = pVCD0 _ W 2K = O 
av w;s s 1 v3 - p 2 
(17 .1 2) 
V min thrust or drag = (17 .1 3) 
- Cr min thrust or drag = y K (17 .14) 
Subst ituting this veloc ity into Eq. (17 .9) yields the lift coefficient for 
minimum drag in level flight [Eq. (17 .14 )]. This optimal lift coeffici ent is 
only dependent upon the aerod ynamic parameters. At any given weight, 
the aircraft can be flown at the optimal lift coefficient for minimum drag 
by varying veloc ity or air dens ity (altit ude). 
If the lift coefficient for minimum drag is subst ituted back into the total 
drag [Eq. (17 .8)], the induced- drag term will equal the zero-lift drag term. 
The total drag at the lift coefficient for minimum drag will then be exactly 
twice the zero-lift drag [Eq. (17 .15 )] . 
Dmin thru.t°' drng - qS [ Cv, + K (ff-)'] - qS( Cv, + Cv, ) (17. 15) 
4fllJ Minimum Powe r Req uir ed for Leve l Fl igh t 
The conditions for minimum thrust and minimum power required are 
not the same. Power is force times velocity, which in steady level flight


<!-- p.643 -->

CHAPTER 17 Perfor manc e and Fligh t Mech an ics 64 1 
equals the drag times the velocity as shown in Eq. (17 .1 6). Substituting the lift 
coefficient in level flight from Eq. (1 7.9) yields Eq. (17.17 ). 
1 
p = DV = qS(CDo + KCz)V = -p V3S(CDo + Kcf) 2 (17 .16) 
1 3 KW2 P = -pV SCD + -2 ° 1 -pVS 2 
The velocity for flight on minimum power is 
obtained by setting the derivative of Eq. (17 .1 7) to 
zero, as shown in Eqs. (17 .18 ) and (17.19 ). Substituting this into Eq. (1 7.9) yields the lift coeffi cient for 
minimum power, Eq. (1 7.20) . Substituting this into 
Eq. (17.8) gives the drag at minimum power required 
[Eq. (17 .21) ]: 
8P 3 2 · KW2 - = -pV SCD - = 0 av 2 ° -pv2s 2 
V min power = 2W /K 
ps y - CLm in power = V 7 
(17. 17) 
When flying at the 
speed for minimum 
drag, the induced 
drag equals the 
parasitic drag. 
(1 7.18 ) 
(17 .1 9) 
(17 .20) 
(17 .21) 
Note that the veloc ity for minimum power required is approxi mately 0.76 
times the velocity for minimum thrust as derived in Eq. (17.13 ). The aircraft is 
flying at a lift coefficient for minimum power, which is about 73% higher than 
the lift coefficient for minimum drag [Eq. (17.14 )]. 
The induced drag at the lift coefficient for minimum power is exactly 
three times the zero -lift drag, so the total drag is four times the zero -lift 
drag [Eq. (17. 21)] . This drag coefficient is twice as high as at minimum 
drag [Eq. (17.1 5)]. 
Remember that at the minimum-po wer cond ition the aircraft is flying 
at a slower speed (reduced dynamic pressure) than at the minimum- drag 
condition. The actual drag increase will thus be less than the factor of 
two indicated by the drag coefficients. The actual drag increase is 2.0 
times the ratio of dynamic pressures (0.76 2), or only 15 .5% higher than 
the total drag at minimum-d rag cond itions. Thus, the L/D when flying 
at the velocity for minimum power required is 1/1. 155 , or 0.866 times 
the maximum L / D.


<!-- p.644 -->

642 Ai rcr aft Des ign : A Conceptu al Ap proach 
MflH Graph ical Analy sis for Th rust and Power Requir ed 
The analytical optimizations in the last two sections depend upon the 
assumpt ions that the zero-lift drag coefficient is constant with velocity, 
that the drag due to lift follows the parabolic approximation, and that ]( is 
constant with veloc ity. As seen in Chapter 12, these assumptions are not 
very good other than for an aircraft with a high-asp ect- ratio wing that is 
flying at low Mach numbers. 
To determine the actual thrust (or power) required for level flight, the 
aerod ynamic results are plotted vs veloc ity or Mach number and compared 
to the engine data, as shown in Fig. 17.2. Soph isticated computer programs 
for performance and range calculations do this inte rnally, searching for 
the velocit y that gives best resu lts rather than relying upon some simple 
equatio ns. 
For pist on-po wered aircraft, power is virtually cons tant with veloc ity. The 
only power variati on with velocity is due to ram pressure in the intake manifold. For je t aircraft, equivalent power varies widely with velocity but thrust is 
roughly constant with velocit y. 
It is therefore common practice to graph the propulsi ve requirements of 
an aircraft vs velocity (or Mach number) , using thrust for jet aircraft and 
using power for propeller aircraft. These are shown in Fig. 17.2. The power 
5000 
- 4000 
Cl 
0 3000 
..., 
V'I 
2000 2 
.s:::: 
I10 00 
0 
8000 
Q; 6000 
:;: 4000 0 
a.. 
2000 
0 
0 
\ 
' 
' 
...... 
Sta ll 
Min Min power drag req uir ed 
- ..... 
jet range 
Veloci ty 
Max speed 
pi ston-pr op 
100 200 300 400 500 
Velocity 
- 600 700 
Fig. 17 .2 Thrust and power. 
Drag (thrust req uir ed) 
jet th rust available 
Thrust avai lable 
- 2000 HP piston-pr op 
Power req uir ed 
...- Jet th rust powe r 
avail able 
Pist on-pr op 
powe r 
available


<!-- p.645 -->

CHAP TER 17 Performanc e and Flight Me chan ics 643 
required is found by multiplying the drag by the velocity. The equival ent 
thrust for the propeller aircraft is also shown for illustration but is not 
commonly plotted. 
The velocities for minimum thrust and minimum power are shown. 
Note that the minimum-power-required veloc ity is about 86.6% of the 
minimum-thrust-required veloc ity, as predicted in the last section. Also, 
the superio rity of the jet engine for high-speed flight should be clear from 
this illustratio n. 
The excess thrust at full throttle is determined simply by subtracting the 
thrust required from the thrust available. This excess can be used to accelerate or climb, as discussed later. 
Such a plot of thrust or power vs veloc ity is different at each altitude. 
Ifill Range 
The range of an aircraft is its veloc ity multiplied by the amount of time it 
can remain in the air. Time in the air equals the amount of fuel carried 
divided by the rate at which the fuel is burned. This in turn is the required 
thrust multiplied by the specific fuel consum ption. 
Unfortunately, the simple equation implied by the last paragraph is 
complicated by the fact that the aircraft weight drops as fuel is burned. 
This changes the drag, which then changes the thrust required. The 
net result is that the aircraft goes farther, but the calculation is more 
difficult! 
However, the "instanta neous range" derivative can be calculated using the 
simple relationship just described, which is expressed in Eq. (1 7.22) . This 
describes the additional distance the aircraft will travel with the next incremental amount of fuel burned. This can also be expre ssed in terms of the 
L/D and weight, as shown. Instantaneous range is a commo nly used 
measure of merit and is usua lly discussed in units of nautical miles per 
pound of fuel. 
dR V V V(L/D) 
dW - CT - CD -C W (17.2 2) 
(17.2 3) 
Integrating the instant aneous range with respect to the change in aircraft 
weight yields the Breguet range equation [Eq. (1 7.23 )]. This integration 
assumes that the veloc ity, speci fic fuel consumption, and L/ D are approximately constant. 
These assumptions require that the aircra ft hold lift coefficient constant. 
To hold the lift coefficient con stant as the aircraft becomes lighter requires


<!-- p.646 -->

644 Ai rcraf t Desig n: A Conceptu al Appr oach 
reducing the dynamic pressure. Because velocity is also being held constant 
the only way to reduce dynamic pressure is to reduce air dens ity by climbing'. 
This results in a flight path known as the cruise- climb, which has been found 
to offer maximum range. 
Unfortunatel y, the air traffic controllers don't want airplanes to be 
rando mly climbing during their flight. Safe sep aration between airplanes 
is ensured by instructing each plane to fly at a specified speed and altitude. 
Violations of the assigned altitude are dealt with severely. To maximize 
range, the pilot will request per mission to climb several times during the 
flight as fuel is burned off, thus forming the characteristic "stair-step" 
cruise climb. 
It is possi ble to develop a rather messy range equation for the consta nt 
speed-co nstant altitude assumption. However, the Breguet range equation 
can be applied with little loss of accur acy even under these con ditions by 
breaking the cruise legs into several shorter mission- segments, using the 
approp riate L / D values as aircraft weight drops. This is also done for analyzing the stair-step cruise climb, which is represen tative of actual flight 
oper ations. 
There is work in progress to develop an all new computerized air traffic 
control system that would, among other things, allow use of the true cruiseclimb. This would save a lot of fuel. The new system would also reduce the 
actual distances flown by aircraft by allowing them to fly direct ly from 
airport to airport. Aircraft normally follow federal airways, straight lines connecting navigational aid transmitters, which might not dire ctly connect the 
two airports. 
MUJI Range Opti miz ation -Jet 
The Breguet range equation can be applied equally well to jets or propeller aircraft, with the use of Eq. (1 7.4) to determine an equivalent thrust 
specific fuel consumption for the propeller aircraft. However, the conditions 
for maximum range differ for je ts and props because of the effect of velocity 
on thrust for the propeller. 
The terms in the Breguet range equation that do not involve the weight 
change [i.e., (V/C) (L/D)] are known as the "range parameter" and are a 
measure of the cruising performance. For subsonic jet aircraft the specific 
fuel cons umption is approxima tely independen t of veloc ity, and the range 
parameter can be expanded as shown in Eq. (1 7.2 4) . 
Setting the derivative of Eq. (1 7.24) with respect to velocity equal to zero 
yields Eq. (1 7.25), the veloc ity for best range for a jet. The res ulting lift coefficient and drag are given in Eqs. (1 7.26) and (1 7.27). 
V (L) V ( CL ) 
c I> = c cD0 + Kcf 2W/pVS (17. 24)


<!-- p.647 -->

CHAPTER 17 Perf ormance and Fligh t Mech an ics 645 
V best range = 
CL = rc;;;3-; best range V 3K 
( CDo) D best range = qS CDo + 3 
(17 .25) 
(17.2 6) 
(17.2 7) 
Note that the drag coefficient for best range for a jet is 1. 33 times 
the zero-l ift drag coefficient. This is a lower drag coefficient than the drag 
coefficient for best L/ D, which was shown to be 2.0 times the zero-lift coefficient. However, when maximizing range, the aircraft flies at a higher veloc ity 
[31. 6% faster- divide Eq. (1 7.25) by Eq. (17.13 )) . This increases the dynamic 
pressure, which increases the actual drag magnitu de. 
As a result, the actual drag while flying at the veloc ity for best range will 
be higher than the drag at the veloc ity for best L / D. The ratio between the 
drags at the best range velocity and the best L/ D veloc ity is determined as 
the ratio of drag coefficien ts (1 .33/2. 0) multiplied by the ratio of dynamic 
pressures (1.316 2), or about 1.15 4. 
Because drag is in the deno minator of L / D, the L / D at the velocity for 
best range will be found to be 86.6% of the best L/D (1/1. 15 4 = 0.866). 
This result was presented without proof in Chapter 5. 
These range optimization equations were based on the assumption 
that the range parameter ( V / C)(L / D) does not vary with weight as Eq. 
(1 7.23) is integrated, which we attempt to provide by holding a const ant 
lift coefficient during cruise. We do this by climbing, but eventually that 
will change specific fuel cons umption C because it is a function of altitude 
for jet and prop engines. Furthermore, our derivation of Eq. (17 .24) 
implicitly assumed that CDo and ](d o not vary as veloc ity changes when 
we solve for V in Eq. (17 .25), which we also know to be only a rough 
approximation. Thus, Eqs. (1 7.2 5-1 7.27) are not exactly correct in the 
real world. 
A more correct optimum cond ition for range can be found by ex haustively searching throughout the flight envelope at the current aircraft 
weight, looking for the place where the range parameter (V/C)(L/D) is at a 
maximum. This is the method used by the computer programs in the 
major aircraft companies. The same is true for the follo wing loiter optimization methods. 
lflU Range Opti miz atio n-Prop 
Substituting Eq. (1 7.4) into Eq. (17. 23) yields the Breguet range equation 
for propeller-po wered aircraft [Eq. (1 7.28 )) . The veloc ity term seen in the jet


<!-- p.648 -->

646 Air craft Desig n: A Conceptual Approach 
range equation has disappeared. Because all other terms are const ant wiU 
respect to veloc ity, it follo ws that propeller aircraft range will maximize h) 
flying at the speed and lift coefficient for maximum L / D, as was determinec 
with Eqs. (17 .13 ) and (1 7.14 ): 
(1 7.2 s; 
Aff 11 Loit er Endur anc e 
The amount of time an aircraft can remain in the air is simply its fuel 
capacit y divided by the rate of fuel cons umption (thrust multiplied by specific 
fuel consum ption) . The change in weight due to fuel consu mption complicates the equation. 
The "instantaneous endurance" as defined in Eq. (1 7.29) is the amount of 
time the aircraft will remain aloft from the next increment of fuel burned. 
This can be expanded as shown to express instantane ous endurance in 
terms of L / D and weight. 
(17 .29 ) 
E - J:--Tdw- J:c-(-)dw- @(-)t·(-) (17.3 0) 
Equation (1 7.30) integrates for total endurance E. For propeller aircraft, 
the endurance is obtained by using the equivalent C obtained from Eq. (1 7.4) . 
Aff J:I Loit er Opti mi zation -Jet 
For jet aircra ft the only term in the endurance equation that varies with 
velocity is the L/D. Therefore, the endurance for jet aircraft is maximized by 
maximizing the L/D, as determined from Eqs. (17.13 ) and (17. 14). 
AUD Loit er Opti mi zati on-Prop 
Subst ituting Eq. (1 7.4) into Eq. (1 7.30) yields Eq. (17 .31), the endurance 
equation for propeller aircraft. This substituti on introduces a velocity term 
into the loiter endurance equation, so the condition for best prop loite r 
will not simply be the maximum L/D. 
The terms in Eq. (17.31) that vary with velocity are expanded, and the 
derivative with respect to veloc ity is set to zero in Eq. (17 .32) . This eventually 
leads to Eq. (1 7.33), the veloc ity condition for maximum loiter time for a


<!-- p.649 -->

CHAP TE R 17 Performance and Fligh t Mech an ics 647 
propeller aircr aft. 
E -(!:__) ( Y/p ) en ( wi) D Cpower V Wf 
=(!:__) (550YJP)en(wi) D Cbhp V \rj" 
(17 .31) 
(17.3 2) 
(17.3 3) 
This last equation is identical to Eq. (17.19 ), the velocity cond ition for 
minimum power required. The lift coefficient and drag for maximum prop 
endurance are therefore identical to the minim um-po wer results defined 
by E qs. (17.2 0) and (17.21). As was shown, the aircraft flies at a veloc ity 
that is 76% of the veloc ity for best L / D. The L / D when flying at the 
minimum power velocity was shown to be 86.6% of the best L / D. 
4f1Jl•1 Relationsh ip Between Loiter and Cru ise 
In prelimi nary design studies of derivative airc raft, the available loiter 
time of existing aircraft is often needed for evaluation of their usability for 
other missions. There is a simple relationship between range and endurance 
based on the Breguet range and loiter equat ions. l125 l Given a known aircraft 
range and cruise speed, equivalent loiter time can be estimated with reasonable accuracy by 
E {Rcruise} loiter = 1.1 4 -.
Vcrmse 
4flJll Effects of Wind on Cru ise and Loiter 
(17.3 4) 
While the design mission for an aircraft often assumes zero wind, the 
real world is usually not so coop erative. In fact, when you fly east in the 
morning and west in the aftern oon, you often find a strong headwi nd 
both ways! This has a direct effect on the range as calculated in Eq. 
(17. 23). If you have a direct headwind that makes your groundspeed 10% 
lower than in no -wind con ditions, then your range during cruise for a 
certain amount of fuel will be 10% less. If you are sizing to a required 
range, you must increase the required cruise range R in the mission 
segment weight fraction (19. 10) by the ratio of velocities (Vairspeed/


<!-- p.650 -->

648 Ai rcr aft Desig n: A Con ceptu al Approa ch 
Vgroundspeed) while still using the actual airspeed for V in the equation. If 
you have a tailwind, the cruise range is improved. 
Also, the real world usually offers a wind that is neither a headwind nor a 
tailwind. You must solve for the groundspeed along the desired flight direction using the Law of Sines and a wind vector diagram as shown at the bottom 
of Fig. 17.3. Note that the aircraft has its nose poi nted to the left of the desired 
ground track to compensate for the wind. If we define the relative wind angle 
such that a tailwind has angle zero, and a headwind has angle of p radians 
(18 0 deg) , then we can derive the following: 
- Vairspeed sin { 7f - Litailwind - sin - l [V wind (sin Litailwind ) I Vairspeed]} Vgroundspeed - · Li sm tailwind 
(1 7. 35) 
The traditional pilot's "flight computer" solves this equation graphically, 
telling where to poin t the nose and what the resulting groundspeed will be. 
From the calculated groundspeed, the cruise range or the mission segmen t 
weight fraction equation can be adju sted as shown before. Most pilots 
today use a spe cial pocket calculator that does all such calculations 
insta ntly- as long as you type in the correct values. 
The presence of wind also affects the optimal cruising speed for maximizing range. Basic ally, you should fly faster into a headwind so that you 
do not fight it as long, and slower if a tailwind is pushing you forward. 
Unless the wind is very strong, these will only change your airspeed by 
perhaps 5-10 % or so, gaining ju st a few percent in range over the range if 
you flew at the no-wind optimal speed. 
Complicated adjust ments can be made to the range optimiz ation 
equat ions (see [12 6]), but as was alread y discussed, the use of pure equatio ns 
for optimizing for range is not the preferred method anyway. Instead, we use 
a comp uter program that will exhaustively search throughout the flight 
Vairspeed 
vground track 
Vairspeed 7 
·<:-0. 
Lltailwind 0 --l "'' 
Vground track 
Fig. 17 .3 Effects of wind.


<!-- p.651 -->

CHAP TER 17 Performance and Fligh t Me chan ics 649 
envelope at the current aircraft weight, looking for the place where the 
range parameter (V/C)( L/D) is at a maximum. We can adjust the velocity 
v in the range parameter as ju st described and use the same search 
routine to find the best answer for range optimi zation with winds considered. 
Then, calculate the range obtained with the veloc ity adjusted as already 
described. 
The wind has no effect on loiter time or loiter optimization airsp eeds, 
unless somehow the wind speed is greater than your optimum loiter speed 
and you find you are being blown backward! 
fl Steady Cli mbin g and Descending Fl ight 
lflll Climb Equa tions of Motion 
Rate of climb is a vertical velocity, typically expressed in feet or meters 
per minute (which must be converted to feet or meters per second for 
the following calculat ion s). Climb gradient G is the ratio between vertical and horizont al distance traveled. This is approxima tely equal to the vertical climb rate divided by the aircraft velocity or the sine of the climb 
angle y. 
Equations (1 7.6) and (1 7.7) sum the forces depicted in Fig. 17.1 when '}'i s 
not zero. Setting the sum of the forces to zero yields the steady climb Eqs. 
(1 7.36) and (1 7.37). Solving for climb angle in Eq. (1 7.36) produces Eq. 
(1 7.38). For normal climb angles (less than 15 deg), the cosine term is 
approximately one. 
The rate of climb, or vertical veloc ity, is the veloc ity times the sine of the 
climb angle [Eq. (17 .39 )]. 
T =D + Ws in y 
L = W cos 'Y 
. _ 1 ( T - D) . _ 1 ( T cos 'Y) . _ 1 ( T 1 ) 
'Y = sm --W- = sm W - L / D - sm W - L/ D 
Vv = V sin y = V ( T; D) - V ( L: D) 
(17.3 6) 
(17.3 7) 
(17.3 8) 
(17. 39) 
The velocity for steady climbing flight can now be derive d from Eq. 
(17 .37), as shown in Eq. (1 7.40) . 
The thrust-to-w eight ratio is no longer the inverse of the lift-to- drag ratio 
as was the case for level flight. Solving Eq. (1 7.38) for T/Wyields Eq. (17 .41), 
the thrust-to -weight ratio required for a steady climb at angle 'Y· 
V= _2_ ( w) cos 'Y 
pCL S (17.4 0)


<!-- p.652 -->

650 Aircr aft Des ign: A Conceptual Appr oac h 
COS 'Y . rv 1 . 1 V v T / W = -- + sm y = - + sm y = -- + -L/D L/D L/D V 
4fff J Graph ical Method for Best Angle and Rate of Climb 
(17 .41) 
Two climb conditions especia lly concern the aircraft designer: the best 
rate of climb, which provides the maximum vertical velocity Vv, and the 
best angle of climb, which provides a slightly lower vertical velocity but at 
a reduced horizon tal speed, so that the angle of climb is maximized. Therefore, the aircraft gains more altitude for a given horizo ntal distance, important for clearing mountains! 
The most accu rate way to determine best rate and angle of climb is to plot 
the rate of climb vs veloc ity, using Eq. (1 7.39), and the actual thrust and drag 
data as shown in Fig. 17 .4. The best rate of climb is obviously the peak of the 
curve. The best angle of climb is the point of tangency to a line from the 
origin. The angle of climb is the arctangent of the vertical velocity divided 
by the horizo ntal veloc ity at that poi nt. 
4tfP Best Angle and Rate of Climb -Jet 
Analytical optimization of veloc ity for best angle and rate of climb can be 
messy. Graphical analysis is more reliable, but doesn't give an analytical 
feeling for the key variables. 
For a jet aircraft, the thrust is essen tially constant with velocity, so 
Eq. (1 7.38) can be dire ctly maximized for the cond itions for best climb 
angle. Because the T / W term is constant with vel ocity, the velocity for best 
Rate of 
climb -Vv 
/ 
/ 
/ 
/ 
/ 
Best rate of climb 
/----------------- VH = V 
Fig. 17 .4 Graph ica l method for best climb.


<!-- p.653 -->

CHAP TER 17 Perf ormance and Fligh t Mech an ics 65 1 
L/D should be used to maximize climb angle. This velocity was determined 
in Eq. (17.1 3). 
To determine the velocity for best rate of climb of a jet aircraft, Eq. (1 7.39) 
must be maximized. Equatio n (1 7.42) is obtained from Eq. (1 7.39) by expanding the drag term and assuming that 'Y is small enough that lift approximately 
equals weight: 
Vv = v(T; D) = v( -) ---;--)- -- (-) 
8Vv = O = !_ _ 3pV2 CD0 21( (W) 8V W 2( W/S) + pV2 S 
V = W /S [r / W + V(T / W)2 + 12CD0KJ 3pCD0 
(17 .42) 
(17 .43) 
In Eq. (1 7.43), the derivative of the vertical veloc ity with respect to aircraft 
velocity is set to zero and solved for velocity for best climb. 
Note that if the thrust is zero, this equation collapses to the equat ion for 
the velocity for minimum power required [Eq. (17. 19 )], which serves as a 
lower boundary on the solution. The effect of nonzero thrust is a significant 
increase in the velocity for best climb rate with increasing thrust. 
The veloc ity for best climb rate including the effects of thrust might be on 
the order of twice the veloc ity for minimum power. Velocities of 300-500 kt 
are not uncommon for the best climb speed for a jet. The B-70 has a best 
climb speed of 583 kt {10 80 km/ h}. 
This climb optimization will only determine the velocity for the best rate 
of climb at some alti tude. It will not tell you what the complete climb profile 
should be to minimize time to a given altitude. For many supersonic aircraft, 
minimizing total time to climb requires leveling off or even diving as the aircraft accelerates through transonic speeds to minimize the time spent at 
these high- drag cond itions. In a later section, the specific excess power 
method will be presented as a means for determining the climb profile that 
minimizes total time to climb. 
lffll Best Angle and Rate of Climb -Prop 
Equation (17. 44) expresses the climb angle of a propeller aircraft, as 
obtained by subst ituting Eq. (1 7.5) into Eq. (1 7.38). This equation can be 
expanded and the derivative taken with respect to veloc ity: 
'Y = sin- 1 [- --] = sin -1[550: 1Jp --] (17.4 4) 
However, the theoretical optimal velocities obtained with the resulting 
equation tend to be too low for the parabolic drag approximati on to be


<!-- p.654 -->

652 Air c raft De sign : A Conceptual Appro ach 
valid because of the sep aration drag at high angles of attack. Also, the thrust 
no longer follows Eq. (1 7.5), which implies that thrust is infinite at zero airspeed. Even worse, sometimes this equation gives an optimal climb speed 
which is lower than the stall speed! 
If thrust and drag data are available at low speeds, the graphical method 
will produce good results. Most propeller aircraft have a best angle-of -climb 
speed about 85-9 0% of the best rate-of-climb speed. This can be used for an 
initial estimate. 
Best rate of climb for a propeller aircraft is obtained by substitut ing Eq. 
(17 .5) into Eq. (17 .39). This yields Eq. (1 7.45), simply the power available 
minus the power required, divided by aircraft weight. Therefore the best 
rate of climb occurs at the veloc ity for minimum power requir ed, as 
defined in Eq. (17 .19 ): 
. Prip Vv = V sm ')' = -W 
DV 
w 
550 bhp Y/p 
w 
MfUj Time to Climb and Fuel to Climb 
DV 
w (17. 45) 
The time to climb to a given altitude is the change in altitude divided by 
the vertical veloc ity (rate of climb ), as shown in Eq. (17. 46) for an incre mental 
altitude change. Fuel burned is the product of the thrust, speci fic fuel consumption, and time to climb [Eq. (1 7.47) ]. 
dt = dh 
Vv 
dW! = - CTdt 
(17 .46) 
(17 .47) 
The air densit y, aircraft weight, drag, thrust, speci fic fuel consum ption, 
and best climb veloc ity all change during the climb. A good approximation 
over small changes in altitude is that the rate of climb at a given weight 
and const ant- thrust setting and constant velocity will reduce linea rly with 
the altitude. This is shown in Eq. (1 7.48), where the linea r constant a is determined from the rates of climb at any two altitudes h1 and h2 [Eq. (17. 49)]. 
These two altitudes used to determine a should be near the beginning and 
ending altitu des of the climb being analyzed, but need not be exactly the 
same altitudes. 
Vv2 - Vv1 a= ---h2 - h1 
(17.4 8) 
(17.4 9) 
If the climb is broken into short segmen ts (less than 5000 ft {-15 00 m} in 
altitude gain) , the fuel burned will be an insignificant portion of the total aircraft weight and can be ignored in the time integratio n. Subst ituting Eq.


<!-- p.655 -->

CHAP TER 17 Performance and Fligh t Mech ani cs 653 
(17.48) into Eq. (17. 46) and integrating yields Eq. (1 7.50), the time to climb 
from altitude i to altitude i + 1. 
Oddly enoug h, the change in altitude has dropped out of the equation! 
However, the change in altitude is implicit in the change in rate of climb 
Vv due to change in altitude. The fuel burned will then be described by 
Eq. (1 7.5 1). 
(17 .50) 
(17 .51) 
If desired, the accu racy of Eq. (1 7.50) can be improved upon by iteration. 
The rate of climb at the end of the climb segment can be recalculated using 
the reduced aircraft weight obtained by subtracting the fuel burned [Eq. 
(17.51 )) from the original weight. This revised rate of climb can then be 
applied back into Eq. (1 7.50). 
'fl Level Tur nin g Fligh t 
In level turning flight, the lift of the wing is canted so that the horizo ntal 
component of the lift exerts the centripetal force required to turn. The total 
lift on the wing is n times the aircraft weight W, where n is the load factor. 
Because the vertical component of lift must be W, the horizo ntal component 
of lift must be W times the square root of (n2 - 1). The geomet ry of a level 
turn is shown in Fig. 17.5 . 
. W- g- l/J= (W/g)V = V (17 .5 2) 
Turn rate ( d!/J / dt) equals the radial acceleration divided by the veloc ity, as 
shown in Eq. (17 .52). Turn rate is usua lly expres sed in degrees per second. 
Equation (17 .52) yields radians per second, which must be multiplied by 
57.3 to get degrees per second. 
MUii Ins tant aneous Tu rn Rate 
If the aircraft is allowed to slow down during the turn (instanta neous 
turn), the load factor n will be limited only by the maximum lift coefficient 
or structural strength of the aircraft. Figure 17.6 shows these stall and structural limits expressed as turn rate vs veloc ity for a typical fighter aircraft. 
The intersection of the stall limit and the structural limit defines the 
corner speed, which is the veloc ity for maximum instantaneous turn rate. 
For a typical fighter, corner speed is about 300-350 kt {560-650 km/h} . In 
a classical turning dogfight, opponen ts will try to get to their own corner 
speed as quick ly as poss ible.


<!-- p.656 -->

654 Aircr aft Desig n: A Concep tual Approach 
Turn 
axis 
30 
25 
10 
5 
'\V.-t' 
X·>J.'> 
(a.u' 
) o/= turn 
rate 
Fig. 17 .5 Level turn geome try. 
Corner 
-----6 
4 
2 
100 200 300 400 500 600 700 
Veloc ity (kts) 
Fig. 17 .6 Turn rate and corner speed (sa mple data at one al titude ). 
al' 
('\ 
§' ;,.


<!-- p.657 -->

CHAPTER 17 Performanc e and Fligh t Me chan ics 655 
lfll I Sustaine d Tu rn Rate 
In a sustaine d turn, the aircraft is not permitted to slow down or lose altitude during the turn. In a sustained turn the thrust must equal the drag and 
the lift must equal load factor n times the weight. Thus, the maximum load 
factor for sustained turn can be expressed as the product of the 
thrust-to-weight and lift-to-drag ratios [Eq. (17 .53 )], assuming that the 
thrust axis is approxim ately aligned with the flight direct ion. 
To solve for the sustained load factor in terms of the basic aerod ynamic 
coefficients, the drag is expanded using (CL = n W / qS) and set equal to the 
thrust. This leads to Eq. (17.5 4), which defines the maximum available sustained load factor for a given flight condition. 
Note that the drag- due-to- lift factor J( is a function of lift coefficient, as 
described in Chapter 12. Because n is also a function of lift coefficient, iteration is required to solve Eq. (1 7.54). 
n = ( T /W)(L/D) (17.5 3) 
n= q ( T qCDo) J<(W/S) W W/S (17.5 4) 
Equation (17 .53) implies that the sustained-turn load factor can be optimized by flying at the lift coefficient for maximum L/D, which was determined in Eq. (17. 14). Using this lift coefficient and setting lift equal to n 
times W leads to Eq. (1 7.55). This can be readily solved for either velocity 
or wing loading to obtain the maximum sustained- turn load factor. 
- L=n W= qSVK (17.5 5) 
Figure 17.6 shows the .sustained turn- rate envelope. This is derived using 
Eq. (1 7.52) to determine the turn rates provided by the sustained load factors 
available at the various flight conditions. 
lflfl Turn Rate with Vectored Th rust 
Vectored thrust as seen on the VSTOL Harrier fighter can be used to 
maximize turn rate. In the Harrier, the pilot can quickly deflect the nozzles 
downwards during a combat turn, creating almost l-g of extra load factor, 
which increases turn rate as seen in Eq. (17 .52). However, if the nozzles 
are deflected all of the way down, the thrust in the flight directi on 
becomes zero, and the airplane slows down rapidly. Harrier pilots learn to 
use this spari ngly. 
The optimal direction the thrust should be vectored depends upon 
whether instantan eous or sustained turn rate is to be maximized. In a level 
turn with vectored thrust, the load factor times the weight must equal the 
lift plus the contrib ution of the vectored thrust, as shown in Eq. (1 7.56).


<!-- p.658 -->

656 Aircr aft Desi gn: A Concep tual Approach 
The maximum load factor (and turn rate) is obtained by taking the 
derivative with respect to vector angle and setting it to zero [Eq. (17 .5 7)] . 
This yields Eq. (17 .5 8), which states simply that the thrust vecto r for 
maximum instantaneous turn rate should be exactly perpe ndicular to the 
flight direct ion. 
nW = L + Ts in (a + ¢y) (17 .5 6) 
-=- -+- sin ( a +¢y) an a [ L T 
J a¢T a¢T w w (-) cos (a + ¢y) = 0 (17 .5 7) 
¢T = 90 deg - a (17 .5 8) 
Because none of the thrust is prope lling the aircraft forward, it will slow 
down very rapidl y. Harrier pilots in combat have used its 90-deg vectorin g 
capabi lity to generate a high turn rate while decelera ting, causing pursuin g 
pilots to overshoot. When this trick is attempted, opposing pilots learn to 
pull up vertically, then roll over and dive on the now too slow Harrier. 
In a sustained turn with vectored thrust, the drag equals the thrust times 
the cosine of the total thrust angle, so the load factor n is expressed as in Eq. 
(17 .5 9) . Setting the derivative with respect to thrust-v ector angle equal to 
zero [Eq. (1 7.60 )] yields Eq. (17 .61 ) . 
an T (L) -a = -s in (a + ¢y) - =0 ¢T W D 
<f>T =- a 
(17. 59) 
(17.6 0) 
(17 .61 ) 
Equat ion (17 .61 ) surprisi ngly implies that the thrust vector for maximum 
sustained turn rate should be aligned with the flight direction, not vectored 
downwards to increase turning. If the aircraft is at a posi tive angle of 
attack, the thrust should actu ally be vectored upward (relati ve to the fuselage 
axis) to align it with the freestream! However, this calculation ignores the jet 
flap effect that can produce a drag reduction with slight downward deflection 
if the nozzles are located near the wing trailing edge. 
Note that the use of vectored thrust for turn augmentation only works if 
the nozzles are loca ted close to the aircraft center of gravity. Otherwise any 
thrust deflection will create a huge pitching moment that cannot be balanced. 
While the Harrier can deflect its nozzles down by 90 deg or more during 
combat, the F-22 and F-3 5 cannot use thrust vectoring to increase load 
factor in a combat turn. Their vectoring nozzles are at the back of the airplane 
where they provide pitch control but not lift enhancement.


<!-- p.659 -->

CHAP TER 17 Performance and Fligh t Mechanics 657 
Glidin g Fligh t 
MJI Stra ight Gliding Fligh t 
Glid ing flight is similar to climbing flight with the thrust set to zero. 
Equations (1 7.36) and (1 7.37) become Eqs. (1 7.62) and (17.63). The direction 
of the gliding angle y is assumed to be reversed from that used for climb. 
D = Ws in y (17 .62) 
L = Wc os y (17 .63) 
L Wc os y 1 1 (17 .64) ---D Ws in y tan y y 
The lift-to- drag ratio is the inv erse of the tangent of the glide angle 
[Eq. (1 7.64)]. In sailplane terminolog y, the "glide ratio" is the ratio between 
horizontal distance traveled and altitude lost and is equal to the lift-to- drag 
ratio. A high-p erformance sailplane with a glide ratio of 40 will travel over 
seven statute miles for every thousand feef of altitude lost. 
(Cultural note: In sailplane terminolog y, a "sailplane" is an expensive, 
high-performance unpowered aircraft. A "glider" is a crude, low-performance 
unpowered aircraft!) 
To maximize range from a given altitu de, the glide ratio should be maximized. This requires flying at the velocity for maximum L/D as found in Eq. 
(17 .13), repeated below as Eq. (1 7.65). The lift coefficient for maximum Lj D 
is repeated as Eq. (1 7.66). The resulting maximum L/D (glide ratio) is determined from Eq. (17.15 ), as shown in Eq. (17. 67). 
Vmax L/D = (17 .65) 
(17 .66) 
(L) 1 1 D max= 2JCDoJ( = 2 V c;;; 
(17 .67) 
The time a glider can remain in the air is determined by the "sink rate,'' 
the vertical veloc ity Vv, which is negative in this case. Sink rate is the aircraft 
velocity times the sine of the glide angle, as ex pressed in Eq. (1 7.68). 
Vv = V sin y = sin y 
. D CD 
(W) 2c os y 
S pCr 
sm y = - cos y = - cos y L Cr 
(17 .68) 
(17 .69)


<!-- p.660 -->

658 Air craf t Desig n: A Con cept ual Approach 
Vv = 
W2 cos3 yC2 
----D- '"" 
S pCz - (17 .70) 
Equation (1 7.68) contains both sine and cosine terms. In Eq. (1 7.69 ), the 
sine of the glide angle is expressed in cosine terms to allow subst itution into 
Eq. (1 7.68), as shown in Eq. (1 7.7 0) . For typical, small glide angles the cosine 
term can be ignored. 
The lift coefficient for minimum sink rate is solved for by maximi zing the 
term involving CL and CD. This is shown in Eq. (17.71), with the resul t in Eq. 
(1 7.72) . Note that this is also the lift coefficient for minimum power required, 
so the veloci ty can be expressed as in Eq. (17 .73). The L/D at minim um sink 
speed is given by Eq. (1 7.7 4) . 
- Crrninsink == 
V K 
Vmin sink = 2W pS y -:;;c;;; 
(17 .7 1) 
(17 .72) 
(17 .73) 
(17.7 4) 
The veloc ity for minimum sink rate is 76% of the veloc ity for best glide 
ratio. Sailplane pil ots fly at minimum sink speed when they are in "lift" 
(i.e., in an air mass moving upwar d), often circling as described below. 
When the lift "dies," they accel erate to the veloci ty for best glide ratio to 
cover the most ground while looking for the next lift. An instrument called 
a "variometer" tells the sailplane pilots when they are in lift. 
Figure 17.7 shows a graphical represen tation of sink rate for a sailpla ne. 
This is known as a "speed-polar," or "hodograph," and can be used to graphically determine the velocities for minimum sink rate and best glide ratio. 
41Jf J Tur ning Gliding Flight 
When sailplane pilots find lift, they turn in a small circle to stay within the 
lifting air mass. Because of the additional wing lift required to turn, the sailplane will experience higher drag and a greater sink rate. Equation (17 .63) 
must be modified to account for the bank angle <P [Eq. (1 7.75 )]. 
L cos </> = W cos 'Y - W (17. 75)


<!-- p.661 -->

0 10 0 .... 
CHAP TER 17 Performanc e and Fligh t Mech ani cs 659 
20 30 
Veloc ity 
40 50 60 70 
.... .... Minimum sink rate 
80 90 100 
.... .... .... .... .... / Best glide ratio 
2 ------------ .... .... _ / (hig hest l/D) 
3 
6 
7 
8 
,,. - , .... .... 
... ... 
- - ... 
; .... ' 
I 
' ' ' ' 
' ' ' ' ' ' ' ' 
.... - ... ; ' 
Fig. 17 .7 Sail plane sink rate. 
' ' ' ' 
' 
' 
' ' 
' 
' ' 
' ' 
' 
' 
' ' 
' ' 
' ' 
' ' 
\. ' , O" 
60° ' ' 
40" 20" Ba nk angle ¢ 
Turn rate is equal to the centripetal acceleration divided by the vel ocity 
and is also equal to the veloc ity divided by the turn radius [Eq. (17 .76 )). 
This allows the centripetal accel eration to be expressed as the veloc ity 
squared divided by the turn radius [Eq. (1 7.77 )). In Eq. (1 7.78), the turning 
force due to the lateral compo nent of wing lift is equal to the aircraft mass 
times the centripetal acceleration. 
ifr= a/V = V/R 
wv2 Ls in cp = -- = wJn2=I gR 
v2 v2 R- ---- -----g tan cf> -g-Vn2=l 
(17.7 6) 
(17.7 7) 
(17.7 8) 
(17.7 9) 
Equation (1 7.78) can be sol ved for turn radius as expressed in terms of 
either bank angle or load factor [Eq. (1 7.79 )). 
The vertical veloci ty (sink rate) can be determined by substituting Cr 
cos cf> for Cr in Eq. (1 7.70) . This yields Eq. (1 7.80), which is simpl y the previous result divided by the cosi ne of cf>, raised to the 3/2 power. The radius 
of the turn is found by substituting Eq. (1 7.75) into Eq. (1 7.79), as shown


<!-- p.662 -->

660 Ai rc raf t De si gn: A Concep tu al Approach 
in Eq. (1 7. 81): 
1 Vv = --cos 312 <P 
2W R = ----pSCrgs in <P 
(1 7. 80) 
(17 .81) 
Because the <P term in Eq. (1 7.80) does not vary with velocity, the prior 
results for the velocities for best glide ratio and minimum sink rate can 
be applied. 
One unique problem for a slow-flying sailplane in a turn is the variatio n in 
veloc ity across the long span of the wing. The wing on the inside of the turn 
might stall due to the lower veloci ty. This is shown in Fig. 17 .8. The velocity 
across the span varies linear ly with distance from the axis of the turn. Also, 
the bank angle shortens the wing span when seen from above. These 
effects are shown in Eq. (1 7.82): 
V= Vcg[l +- cos </J] (1 7.82 ) 
\/inner = Veg [ 1 -:R COS </J] (17.8 3) 
In Eq. (1 7.83), the veloc ity at the inner wing tip is shown as a function of 
wing span, turn radius, and bank angle. In normal flight this velocity difference is easily corrected with a little aileron to increase the lift coefficient on 
v,"-·- - - - - - - - v -------_vr, 
------ --------- - -------- Tu rn 
axis 
Tu rn 
axis 
Ar-----• I --- -\¢ .,....-----,..--1 U (b/2 )cos cf> Rinner 
I 
Router 
-----+- Y 
R 
Fig. 17 .8 Turn radiu s effect on wing-ti p velocity.


<!-- p.663 -->

CHAP TE R 17 Perfo rmance and Fl ight Me chan ics 66 1 
the inner wing. However, when flying near the stall at even a mode rate bank 
angle, this can reduce the veloc ity of the inner wing tip enough to crea te a 
one-wing stall, which leads to a spin. 
Energy-Man euver abil ity Methods 
.lflll Ener gy Equa tions 
Fighter pilots have always known that management of energ y is critical to 
survival and success. In World War I the experienced pilots always tried to 
enter a dogfight from above. They could then exchange the potent ial 
energy of altitude for the kinetic energy of speed or turn rate. 
Jet-fighter dogfight maneuvers largel y rely upon the exchange of poten tial 
and kinetic energy to attain a posi tional advantage. For example, the "highspeed yo-yo" maneuver is used when overtaking a slower aircraft in a hard 
turn. The attacker pulls up, trading kinetic ene rgy for potential energy and 
slowing to allow a higher turn rate. After turning, the attacker rolls partially 
inverted and pulls down astern of the opponen t, now exchanging potential 
energy back for speed. 
Fighter pilots understand that potential and kinetic energy can be 
exchanged and that the sum of the airc raft energy must be managed to 
attain success. This intuitive measure of goodness can be analytically developed and applied to aircraft design (first defined in [1 27l ). 
E = Wh + - (;) V2 
E 1 2 he = - = h + -V w 2g 
p = dhe = dh + V d V 
Sused dt dt g dt 
(17.8 4) 
(17. 85) 
(17.8 6) 
At any point in time, the total energy of an aircraft (the "ener gy state ") is 
the sum of the potent ial and kinetic energ y, as shown in Eq. (1 7. 84) . Dividing 
by aircraft weight gives the "specific energ y" [Eq. (17 .85 )]. Specific ene rgy has 
units of distance (feet or meters) and is also called the "ener gy height" he 
because it equals the aircraft altitude if the velocity is zero. 
Power is the time rate of energy usage, so the spe cific power (Ps)used can 
be defined as the time rate at which the aircraft is gaining altitude or velocity 
[Eq. (17 .86 )]. Because specific energy has units of distance, speci fic power has 
units of distance per time [( ft/s) or {m/s }] . 
This power being used by the aircraft to gain height or veloc ity has to come 
from somewhere. In the discussions of power required vs power available, it 
was pointed out that the excess power could be used to climb or accelerate. 
This excess power is the excess thrust (T -D) times the veloc ity [Eq. (17 .87 )].


<!-- p.664 -->

662 Aircr aft Desig n: A Concep tual Approach 
The spec ific excess power P is the excess power divided by the weight and 
equals the speci fic power used, as shown in Eq. (17 .88). 
P=V (T-D ) (17.8 7) 
p = V(T -D) = dh + V dV s w dt g dt (17.8 8) 
p = v[I_ -qCDo - n2]( W] s W W/S q S (17 .8 9) 
Drag, and therefore P5, is a function of the aircraft load factor. The higher 
the load factor is, the greater the drag, and thus the less excess power available. Equation (1 7.88) can be expanded in terms of the load factor and the 
aerod ynamic coefficients as shown in Eq. (17 .89). Note that T/W and W/S 
are at the given flight condition, not the takeoff values! 
Specific excess power P5 has the same units as rate of climb . In fact, Eq. 
(1 7.88) is identical to the rate-of-climb equation if the longitudinal acceleration (d V/ dt) is zero. The Ps at a load factor of one is actually the rate of climb 
that would be available if the pilot chose to use all of the excess power for 
climbing at const ant veloc ity. 
When P5 equals zero, the drag of the aircraft exactly equals the thrust, so 
there is no excess power. This does not necess arily mean that the aircraft isn't 
climbing or accelerating. However, if the sum of the energy usage equals zero, 
then the aircraft must be flying level, or climbing and decelerating, or descending and accel erating. 
Equations (17 .88) and (17 .89) assume that the thrust axis is approximately aligned with the flight direction. If this is not the case, the thrust components in the lift and drag directions yield Eq. (17 .90) . 
p = 
v{T cos(a + 
<f>r) _q CDo - n2K [W - Tsin(a+ </> )]} (17 .90) s W W/S WqS 
r 
4flf J Ps Pl ots 
For any given altitude, P5 can be calculated using Eq. (17. 89) for varying 
Mach numbers and load factors once the aerod ynamic coefficients and 
installed thrust data are ava ilable. Design specifications for a new fighter 
will have a large number of "must meet or exceed" P5 points, such as 
P5 = 0 at n = 5 at Mach 0.9 at 30,000 ft {914 4 m}. 
P5 values are calculated and plotted against Mach number as shown in 
Fig. 17.9 for a number of altitudes. Computers are especi ally handy for this 
"number crunching." 
From the P5 charts at the various altitudes (Fig. 17 .9), several additional 
charts can be prepared by cross-plot ting.


<!-- p.665 -->

u 
500 
400 
300 
200 
- 100 
.!;:'. 
' 
0 
-10 0 
-200 
-300 
CHAPTER 17 Performanc e and Fligh t Me chani cs 663 
(Typical value s) 
n 
7 
-400 +---+--t-'--t--f---+-' ---tf---+----t--t---t-+ 0 0.2 0.4 0.6 0.8 1.0 1.2 1. 4 1.6 1.8 2.0 2.2 
Mach numb er 
Fig. 17 . 9 P5 vs Mach numb er and load facto r. 
The level turn rate can be determined for the various load factors at a 
given altitude and Mach number and plotted vs P5 (Fig. 17. 10). This is compared to the data for a threat aircraft at that altitude and Mach number. With 
an equivalent P5 at a higher turn rate, the new fighter would always be able to 
turn inside the opponent without losi ng relative energy. A turn- rate advantage of 2 deg/ s is considered significant. 
600 Altitude = 30,000 ft (91 44 m} 
400 Mach = 0.9 
..... 
..... 
200 ' 
, . 
' 
0 
' Adva nced 
u -200 ' 
dogf ig hter QJ ' V\ 
' \ .!;:'. -400 ' \ ..... 
Cl..,- \ E 
-600 \ = 
\ "' ..... 
-800 Th reat \ 
V'l 
ai rcraft \ 
-1000 \ 
\ 
-12 00 
-14 00 0 5 10 15 20 25 
Turn rate if (deg /s) 
Fig. 17 .1 0 Turn rate vs P, .


<!-- p.666 -->

664 Air craf t De sign: A Concep tual Appr oa ch 
(Typica l) n= l 
50 
40 
10 
0 +--+-'---1------"L__JL---'-l--____, f--'----'1----+ ----+---+---+- 0 0.2 0.4 0.6 0.8 1.0 1.2 1. 4 1.6 1.8 2.0 
Mach numb er 
Fig. 17 .1 1 Ps = 0 cont ours. 
In Fig. 17 .11, P5 = 0 contours are plotted for different load factors on a 
Mach number vs altitude chart. This is a major tool for the evaluation of 
new fighters and permits comparisons between two aircraft for all Mach 
numbers and altitudes on one chart. To win a protracted dogfight, an aircraft 
should have P5 = 0 contours that envelop those of an oppo nent. 
In Fig. 17. 12 , contour lines of constant P5 at a given load factor are plotted 
onto a Mach number vs altitude chart. A separate chart is prepared for each 
load factor. The chart for load factor equals one is espe cially important 
because it provides the rate of climb and the aircraft ceiling, and because it 
is used to determine an optimal climb trajectory. 
MUfl Minim um Time- to-Clim b Trajec tory 
Figure 17 .13 is a plot of energy height vs Mach number and altitude. This 
is merely a graphical represe ntation of Eq. (1 7.85) and has nothing to do with 
the particulars of any one aircraft. An F-16 or a Boei ng 747 would have an 
energy height of 42,447 ft {1 2,938 m} if flying at Mach 0.9 at 30,000 ft 
{914 4 m}. 
dt = 
dhe 
Ps (17.9 1) 
(17. 92)


<!-- p.667 -->

.t'. "' 
0 
' 
Q) 
" 
·;::; 
<i'. 
50 
40 
30 
20 
10 
CHAP TER 17 Performance and Flight Mech ani cs 665 
(Typica l) P5 value s, n = 5 
-400 
O+--+--'+'--'+--'---t---+--'-+----+----+----+---+0 0 .2 0.4 0.6 0.8 1.0 1 .2 1.4 1.6 1.8 2 .0 
Mach numb er 
Fig. 17 .12 Ps contour s, cons tant load facto r. 
Equation (1 7.86) can be rearranged into Eq. (1 7. 91), which expresses 
the incremental time to change energy height he as the change in energy 
height divided by the Ps at that flight cond ition. This is then integrated in 
Eq. (1 7.92) for the time to change energy height. 
' 
Q) 
" 
:::> 
50 
40 
·E 20 
<i'. 
10 
Ener gy heig ht: he = h + - V2 
60 70 80 90 100 120 1 40 1 60 
\ 
0 0 .2 0.4 0.6 0.8 1.0 1 .2 1.4 1.6 1.8 2 .0 2.2 2.4 2.6 2.8 
Mach numb er 
Fig. 17 .13 Li nes of cons tant ener gy heigh t.


<!-- p.668 -->

666 Air craf t Desi gn: A Concep tu al Approach 
Equa tion (1 7.92) shows that the time to change energy height is minimized if the Ps is maximized at each energy height. This occurs at those 
points on the Mach number vs altitude plot of l-g Ps (Fig. 17. 12) where 
the P5 curve is exactly tangent to an energy-hei ght curve (Fig. 17.13 ). 
In Fig. 17. 14, the l-g Ps curves for a typical high thrust fighter are superimposed on the he curves of Fig. 17.13. The traject ory for minimum time to 
climb is shown as passing through the dots represent ing the points where the 
Ps curves are tangent to he curves. These points can also be found by starting 
at the top of each energy height he curve and following it down to sea level, 
noting the altitude where the highest value of Ps is found. This techn ique is 
easiest for programm ing and automatic ally accounts for oddly shaped p5 
curves as in the next example. 
For a high thrust fighter, the minimum time to climb is obtained by 
staying low and accelerating to transonic speeds, then pitching up into a 
steep climb at approximately constant indicated airspeed (i.e., dynamic 
pressur e), as shown by the optimal trajector y. This is ess entially the strategy 
followed by record-s etting jets like the F- 15 Streak Eagle. 
Figure 17.15 shows l-g P5 curves typical for a supersonic transport (SS T) 
or a 19 60s era jet fighter. These aircraft have significan tly less thrust than the 
previous example and suffer a "thrust pinch" at transonic speeds in which the 
thrust minus drag reduces to almost zero. This causes the Ps contours to 
form "bubbles." 
50 
40 
.;::'. 
'6 30 
' 
CJ.) 
"O 
3 
- 20 
10 
(Ps contou rs for n = 1) 
100 
Tangent to 
Ps and constant 
ener gy height 
cu rves 
Con sta nt ener gy 
height cu rves 
120 
o-------L:::J.'..__L_J.__L_LL_LJ___l,_J_JI--- 0 0.2 0.4 0.6 0.8 1. 0 1.2 1. 4 1. 6 1.8 2.0 2.2 2.4 2.6 2.8 
Mach numb er 
Fig. 17 .14 Minimum time -to-climb trajectory, hig h-thrust figh ter.


<!-- p.669 -->

50 
40 
"' 
0 30 
Q) 
-0 
:i .. 
20 -;; 
<{ 
10 
CHAPTE R 17 Performance and Fligh t Mechan ics 667 
(Ps cont our s for n = 1) 
0.2 0.4 0.6 0.8 1.0 1.2 1. 4 1.6 1.8 2.0 2.2 2.4 2.6 
Mach numb er 
Objective: 
Mach 2.0 
at 45,000 ft 
Tangent to 
Ps and constant 
energy height 
cu rves 
Fig. 17 .15 Minimum tim e-to-climb. SST or low-thrust figh ter. 
The minimum time -to- climb trajector y requires "jumping" from one 
bubble to the lower, higher-speed one. This is done by diving along a line 
of constant energy height tangent to a Ps lines of the same numerical value 
for both bubbles, as shown in Fig. 17.15. 
Note that Fig. 17 .15 requires diving through Mach 1. 0 to minimize time 
to climb for this aircraft. This was common in earlier jets, and makes sense 
intuitively. Because thrust minus drag is nearly zero at transonic speeds, 
acceleration will be slow, and the aircraft will spend a lot of time in transonic 
accelera tion. Diving reduces this time. The altitude lost is easily regained at 
higher speeds where the drag is less. This is exactly what the Concorde did, 
not because it was incapable of going supersonic in level flight, but because it 
was more fuel efficient to do it this way. 
This method minimizes time to climb with no constraint on ending velocity. To climb to a given altitude with a specified ending velocity, the 
optimal trajectory is flown until the aircraft reaches the energy-he ight 
curve of the desired ending conditio n. Then that ene rgy-height curve is followed to the ending altitude and velocity, by either climbing or diving. 
!::..he t1 -2 - ( ) Ps average 
(17.9 3) 
The actual time to climb is determined by numerica lly integrating along 
the optimal trajectory using Eq. (1 7.92). The time to change energy height is 
approximately expressed in Eq. (17 .93) as the change in energy height divided


<!-- p.670 -->

668 Aircr aft Des ign: A Conceptual Appr oach 
by the average Ps during the change. As always, accur acy is impro ved with 
smaller integration steps. 
Note that the time to follow lines of constant energy height is usual ly negligible for a first-order analysis. 
Aflll Minimum Fuel- to-Climb Traj ecto ry 
The energy equations can be modified to determine the climb trajectory 
that minimizes fuel consu mption. The fuel spec ific energy ls is define d as the 
change in specific energy per change in fuel weight. This is shown in Eq. 
(1 7.9 4) to equal the Ps divided by the fuel flow, which is the thrust times 
the specific fuel consum ption. 
Like P5, the ls values can be calculated and plotted vs Mach num ber for 
each altitude and then cross -pl otted as contour lines on a Mach number vs 
altitude chart, as shown in Fig. 17.16 . 
fs _ dhe _ dhe/dt _ !.!___ s - dW! - dWf /dt -CT 
Jhe2 1 
w./i-2 = ,dhe he1 JS 
(17 .94) 
(17 .95 ) 
In Eq. (1 7.95), Eq. (1 7.9 4) is rearranged and integrated to yield the change 
in fuel weight for a change in ener gy height he. Note that this is minimized 
.::: 
0 
' 
<Ii 
"O 
:;:; 
<( 
50 
40 
30 
20 
10 
dh Line of cons tant;; = d 
Cruise objectiv e - wf 
Mach 0.9 at 45,000 ft {1 3,716 m} Su per sonic 
objective: 
Mach 2.0 at 
45,000 ft {1 3,71 6 m} 
Tangent to 
"l--..f----1--_ fs and constant 
12 0 
ener gy height 
cu rves 
0 .J-----'--....__,_ -=--'""-'-'"'---" '--__.__,___,+----JL-+'---'-'--'--'-............ '---+0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6 2.8 
Mach numb er 
Fig. 17 .16 Minimum fuel to climb.


<!-- p.671 -->

CH APTE R 17 Performanc e and Flight Mech ani cs 669 
when fs is maximized for each energy height. This implies that the 
minimum-fuel-to -climb trajector y passes through those points for which fs 
contours are exactly tangent to the he contours. This is shown in Fig. 
17 .1 5, which greatly resembles the chart used to determine the minimumtime-to-climb trajectory. 
D.he 
wf1-2 -f l' ) vs average (17.96) 
The fuel consumed during the climb is determined by numeric ally 
integrating along the minimum-fuel trajectory, using Eq. (17.96) as an 
approximation . 
jkf.J Ener gy Method for Mi ssion- Seg ment Weigh t Frac tion 
Equation (17.97) is an expression of the missi on-se gment weight fraction 
for any flight maneuver involving an inaease in energy height. This can be 
used for climbs or accelerations or combinations of the two. Remember 
that the mi ssion-se gment weight fraction expresses the total aircraft weight 
at the end of the mission segment divided by the total aircraft weight at 
the beginning of the mission segment. This is used for sizing as discussed 
in earlier chapters . 
Wi [ -CD.he ] [ -CD.he ] 
Wi- 1 = exp V(l -D/T) = exp V{l - [l/(T/W)(L/D)]} (l7·97) 
Unfortunately, a maneuver involving a reduction in energy height cannot 
put fuel back in the tanks, as would be implied by putting a negative value for 
the change in he into Eq. (17.97)! 
Operating En velope 
The aircraft "oper ating envel ope" or "flight envelope" maps the combinations of altitude and veloc ity that the aircraft has been designed to attain 
and withstand. The "level-flight oper ating envelope" has the further restriction that the aircraft be capable of steady level flight. 
The operating envelope for a typical fighter is shown in Fig. 17.17. Fighter 
operating envelopes are the most complica ted and contain all of the elements 
of the oper ating envelopes of other classes of aircraft. 
The level- flight operating envelope is determined from the Ps = 0 and 
stall limit lines. The Ps = 0 limit is usually shown for both maximum 
thrust and for military (nona fterburning) thrust. Because the Ps = 0 and 
stall lines vary with aircraft weight, some assumption about aircraft weight 
must be made. Typically, the operating envelope is calculated at takeoff 
weight, cruise weight, or combat weight.


<!-- p.672 -->

670 Ai rcraf t Des ign: A Con ceptu al Approach 
.:= 
M 
0 
QJ 
""Cl 
.=:! 
·::;: 
60 
Pi lot ejection 
al titude limi t 50 - - - -{ = 15 ,240 m} 
40 Engine 
relight limi t 
30 
20 
·'!:: 
ff 
;::::: 
10 3 
V) 
Absol ute cei ling 
----.,,,.. ..... _-_ - - - - -..... ' +-' 
,,, ,,- "' ....- ....- Service cei ling ', ' .-:::.- ""'--- - - - - - - - - 6_ / 
1' E I .,,,.. - - - ..... ..... 
' 
\ 
\ 
I 
C::, I 
2 1 S 1 
- I -- I 
t I 
a' I 
11 I 
-.,'' I 
..., I 
.5' I - I -(;<.; /0 .;§e, 
§ I <;<; ,_e, .§ 1 Q 
,if I 
- I 
CY I 
I. 
0 0 0.2 0.4 0.6 0.8 1.0 1. 2 1. 4 1.6 1. 8 2.0 2.2 
Mach numb er 
Fig. 17 .17 Oper ating envelope. 
The "absolu te ceiling" is determined by the highest altitude at which 
Ps = 0. Som e small rate-of -climb capabi lity (i.e., Ps) is required at the 
"ser vice ceilin g." F ARs require 100 fpm {30.5 mpm} for propeller aircraft 
and 500 fpm {15 2 mpm} for jets. Military specifica tions require 100 fpm 
{30.5 mpm} at the service ceiling (300 fpm {91 mpm} for U.S. Navy). 
For some jet aircraft, the limitation on usable ceiling is the pilot. The odds 
of surviving an ejection above 50,0 00 ft {1 5,2 40 m} are rather small without 
an astronaut-t ype pressu re suit or some type of capsule. This limits the 
usable ceiling as shown. 
Another limitation to the level flight envelope of many jet aircraft is the 
low-q engine operating limit. At low velocities and high altitudes there might 
not be enou gh air available to restart the engine in the event of a flameou t. It 
might also be impossible to oper ate or light the afterburner. These limits are 
provided by the engine manufacturer. 
The remaining limits shown in Fig. 17.17 are structural. The externalflow dynamic press ure q as defined in Eq. (1 7.98) has a direct impact upon 
the structural loads. A maximum q limit is specified in the design requirements and used by the structural designers for stress analysis. Typical 
fighter aircraft have a q limit of 18 00-2200 psf {86- 105 kN/m 2}. This correspon ds to transonic speeds at sea level. 
1 2 2 q = - Pco V co = 0. 7 PstaticM 2 (17. 98) 
(17. 99)


<!-- p.673 -->

CHAPTE R 17 Performanc e and Flight Mech ani cs 67 1 
The airload pressures exerted within the inlet duct are greater than 
the freestream pressures because the inlet slows the air down (typically 
to about Mach 0.4-0.5 at the engine front fac e). The total pressure of 
the oncoming air is determined from Eq. (1 7.99), using the static atmospheric press ure at that altitude from the Standard Atmosphere Table in 
Appendix B. 
The total pressure within the duct equals the outside total pressure times 
the inlet-duct pressure recovery, as discussed in Chapter 13 . Equation (1 7.99) 
is used again for the flow within the duct and solved for the static pressure at 
the Mach number at the engine front face. This is the maximum wall 
pressure exerted within the inlet duct and can eas ily be three times the 
outside dynamic pressure. As shown in Fig. 17.17, the inlet -duct pressure 
limit does not follow the same slope as the dynamic-pressure limit. 
The remaining operating envelope limit is the tempe rature limit due to 
skin aerodynamic heating. This depends upon the selected structural 
materials. A design chart for skin temper ature vs Mach number and altitude 
was presented in Chapter 14. 
r;J Takeoff Ana lysis 
An empirical chart for determining takeoff distance was presented in 
Chapter 5. Later in the design process, a more detailed analysis breaks the 
takeoff into segments for more accu rate analysis. 
Figure 17. 18 illustrates the segments of the takeoff analysis. The ground 
roll includes two parts, the level ground roll and the ground roll during 
Start 
V= O 
R 
Begin to 
rotate Takeoff 
V = VTO 
I 
- sG- 1- sR-1- Sm --1- sc--Rotate Transition to . 
- Total ground roll - climb Cltmb 
Total takeoff dis tanc e 
Fig. 17 .18 Takeoff ana lysis.


<!-- p.674 -->

672 Air c raft Des ign: A Concep tual Appr oa ch 
rotation to the angle of attack for liftoff. After rotation, the aircraft follows an 
approxim ately circular arc ("transition") until it reaches the climb angle. 
MU:ll Ground Roll 
During the ground roll, the forces on the aircraft are the thrust, drag, and 
rolling friction of the wheels, this last being expressed as a rolling-fr iction 
coefficient µ times the weight on the wheels (W - L). A typical µ value for 
rolling resistance on a hard runway is 0.03. Values for various runway surfaces are presented in Table 17.1. 
The resu lting acceleration of the aircra ft, as expressed by Eq. (17.10 0), can 
be expanded in terms of the aerod ynamic coefficients. This requires evaluating the lift and drag of the aircra ft in ground effect and with landin g gear 
down and flaps in the takeoff posi tion, as discussed in Chapter 12. The lift 
coefficient is based on the wing angle of attack on the ground (measured 
to the zero lift angle) and is typically less than 0.1 unless large takeoff flaps 
are deployed. 
a= l:_ [T -D - µ( W - L)J 
w 
= g [ ( - - µ) + 2; 15 ( -cD0 - KCz + µCr) v2 J 
JV! V 1 JV! 1 2 
SG = -dV = - -d( V ) 
Vi a 2V; a 
(17 .1 00) 
(17.1 01) 
The ground-roll distance is determined by integrating velocity 
divided by acceleration, as shown in Eq. (17.101). Note the mathematical 
trick that simplifies the integration by integrating with respect to V2 
instead of V. 
Table 17 .1 Ground Rollin g Resistance 
Dry concr ete/asphalt 
Wet concr ete/asphalt 
Icy concr ete/asphalt O.D 2 
Hor d tur f 0.05 
Firm dirt 0.04 
Soft tur f O.D? 
Wet gross 0.08 
0. 15 -0 .3 
0.06-0 . 10 
0.4 
0.3 
0.2 
0.2


<!-- p.675 -->

CHAPTER 17 Performance and Fligh t Mech an ics 673 
The takeoff velocity must be no less than 1.1 times the stall speed, which 
is found by setting maximum lift at stall speed equal to weight and solving for 
stall speed. The maximum lift coefficient is with the flaps in the takeoff position. Remembe r that landing-gear geometry can limit maximum angle of 
attack (and hence lift coefficient) for takeoff and landing. 
Equation (17.101) is integrated for ground-roll distance from Vinitial to 
Vfinal in Eq. (17 .102), where the terms Ky and KA are defined in Eqs. 
(17 .103) and (17.10 4). Ky contains the thrust terms and KA contains the 
aerodynamic terms. 
s -- JV! d(V2) - (-l-)en(Ky+KAV}) G -2g V; Ky+ KA V2 - 2gKA Ky+ KA v? (17. 10 2) 
Ky= (-) -JL (17. 103) 
KA = 2(: /S) (JLCL -CD0 -KC]'J (17. 104) 
Equation (17. 102) integrates ground roll from any initial velocity to any 
final velocity. For takeoff, the initial veloc ity is zero, and the final velocit y 
is VTO· Because the thrust actually varies some what during the ground 
roll, an averaged thrust value must be used. Because we integrate with 
respect to velocity squared, the averaged thrust to use is the thrust at 
abo ut 70% (1/ .J2) of VTO· 
For greater accuracy, the ground roll can be broken into smaller segments and integrated using the averaged thrust for each segment in 
Eq. (17. 102). The averaged thrust is the thrust at 70% of the velocit y 
increase for that segment. Also, K can be reduced due to ground effect 
(Chapter 12). 
The time to rotate to liftoff attitude depends mostly on the pilot. 
Maximum elevator deflection is rarely employed. A typical assumption for 
large aircraft is that rotation takes 3 s. The acceleration is assumed to be negligible over that short time interval, so the rotation ground-roll distance SR is 
approximated by three times VTO· For small aircraft the rotational time is on 
the order of 1 s, and SR = VTO· 
IU:f I Tran sition 
During the transition from the moment of takeoff to a stabilized climb 
angle, the aircraft follows a path that approximates a circular arc. During this 
time, it also accele rates from takeoff speed (1.1 Vstan) to climb speed (1 .2 Vstau). 
The average velocity during transition is therefore about 1.15 Vstall· The 
average lift coefficient during transition can be assumed to be about 90% of 
the maximum lift coefficient with takeoff flaps. The average vertical


<!-- p.676 -->

674 Ai rcraf t Des ign: A Con ceptu al Appr oach 
acceleration in terms of load factor can then be found from Eq. (17.10 5) : 
1 2 L 2 pS(0.9 CrmaJ (1.15 Vstall) n = - = = 1. 2 \V 1 2 2 pSCrmax Vstall 
v2 n = 1. 0 + TR = 1. 2 Rg 
VfR R= --g(n - 1) 
VfR 
0.2 g 
(17 . 105) 
(17 . 106) 
(17 .1 07) 
The vertical load factor must also equal 1.0 plus the centripetal acceleration required to cause the aircraft to follow the circular transition arc. This is 
shown in Eq. (17.10 6) and solved for the radius of the transition arc in 
Eq. (17.10 7). 
The climb angle y at the end of the transition is determined from 
Eq. (17.10 8). The climb angle is equal to the included angle of the transition arc (see Fig. 17.18 ), so the horizo ntal distance traveled during transition can be determined from Eq. (17. 109). The altitude gained during 
transition is determined from the geom etry of Fig. 17.18 to be as indicated 
in Eq. (17.10 8). 
. T -D ,,.._, T 1 sm 'Yc!imb = -W = \V - L/D 
STR = Rsin 'Yc!imb = R(T;D) - R(- - L;D) 
hTR = R( l - cos 'Yc!imb) 
(17. 108 ) 
(17. 109) 
(17.1 10} 
If the obstacle height is cleared before the end of the transition segment, 
then Eq. (17 .111 ) is used to determine the transition distance. 
(17. 111 ) 
MU:fl Climb 
Finally, the horizo ntal distance travelled during the climb to clear the 
obstacle height is found from Eq. (17 .112 ). The required obstacle clea rance 
is 50 ft {1 5.24 m} for military and small civil aircraft and 35 ft {10 .7 m} for 
commerci al aircraft. 
Sc = hobstacle - hTR tan 'Yc!imb 
If the obstacle height was cleared during transition, then Sc is zero. 
(17. 112 )


<!-- p.677 -->

CHAPTER 17 Perf ormance and Flight Mechan ics 675 
111:11 Ba la nced Field Len gth 
The balanced field length (discussed in Chapter 5) is the total takeoff distance including obstacle clearance when an engine fails at "decision speed" 
Vi, the speed at which, upon an engine failure, the aircraft can either 
brake to a halt or continue the takeoff in the same total distance. If the 
engine fails before decision speed, the pilot can eas ily brake to a halt. If the 
engine fails after decision speed, the pilot must continue the takeoff. 
An empi rical method for balanced field-len gth estimation was presented 
in Chapter 5. A more detailed equation, as developed in[4o] , takes this form: 
0.8 63 ( W /S ) ( 1 ) BFL = l + 2.3 G C . + hobstacle T /W _ U + 2.7 
pg Lc1imb av 
( 655 ) 
+ Jet: 
[5 + BPR] Tav = 0.75 T takeoff 4 + BPR 
static 
Prop: 
where 
1 
T = 5 75 bh [(p/ PsdNeD-l 3 
B . p bhp 
BFL = balanced field length (ft) 
G = Yclimb - Ymin 
Yclimb = arcsine [( T-D)/ W], 1 - engine-ou t, climb speed 
Ymin = 0.024 2- engine; 0.027 3-en gine; 0.030 4-en gine 
CLc1imb = CL at climb speed (1. 2 Vstall) 
hobstacle = 35 ft comm ercial, 50 ft military 
U = 0.01 CLmax + 0.02 for flaps in takeoff position BPR = bypass ratio 
bhp = engine brake horsepo wer 
Ne = number of engines 
Dp = propeller diameter (ft) 
(17. 1 13) 
(17. 1 14) 
(17. 1 15) 
For a more accur ate determination of the balanced field length, the 
takeoff roll should be integrated with an engine failure at an assumed Vi 
and compared with a braking analysis at that Vi using the methods in the 
next secti on. The assumed Vi should be iterated until the total takeoff distance including a 35-ft -obstacle clearance equals the total distance 
with braking.


<!-- p.678 -->

616 Ai rcraft Des ign: A Concep tual Appr oach 
It is usu ally assumed that the pilot waits 1 s before recog nizing the engine 
failure and applying the brakes. The use of reverse thrust is not permitted for 
the balanced field-len gth calcu latio ns. To permit posit ive rate of climb after 
engine failure, the pilot will not take off at minimum flight speed where the 
drag due to lift is excessi ve. Instead, takeoff will be delayed until a higher 
speed, which is calculated to minimize balanced field length. This might be 
20-40% higher than minimum takeoff speed. 
As discussed in Chapter 5, there is a special field-l ength requirem ent for 
FAR 25 certified aircraft called "FAR takeoff field lengt h." This has a 35-ft 
{10 .7 -m} obstacle clearance requirement and requires that the aircr aft meet 
the worst of either balanced field length as described or a value of 15% greater 
than the all- engine s-op erating obstacle clearance takeoff distance. FAR 23 
certified aircraft do not have to meet this double -trouble requirement. 
- 17 .9 Landing Ana lysis 
Landing is much like taking off, only backward ! Figure 17.19 illustrate s 
the landing analysis, which contains virtually the same elements as the 
takeoff. Note that the aircraft weight for landing analysis is specified in the 
design requirements and ranges from the takeoff value to about 85% of 
takeoff weight. Landing weight is not the end- of-mission weight because 
this would require dumping large amounts of fuel to land immed iately 
after takeoff in the event of an emergency. 
AUii Appr oach 
The approach begins with obstacle clearance over a 50-ft {15. 24-m} 
object. Approach speed Va is 1.3 Vstall (1. 2 Vstall for military) . The steepest 
.... .... R 
.... 
raj' Touch 
-- -- - .... down Brakes 
', V= Vrnappli ed 
f ' ..: = VF I I 
v = 0 
JiF - f -- -----Appr oach di sta nce Flar e Free Braking dis tance 
Sa 1- SF --FR·j-ssdis tance roll 
- Ground roll Tota l landing dis tance 
Fig. 17 .19 Landing ana lysis.


<!-- p.679 -->

CHAP TER 17 Perfo rmance and Fligh t Mech an ics 677 
approach angle can be calculated from Eq. (17 .108), with idle thrust and drag 
with full flaps deflected. 
For transport aircraft the approach angle should be no steeper than 3 deg 
(0.052 rad), which might require more than idle thrust. Approach distance is 
determined from Eq. (17.1 12) using the flare height hf' 
jfUJ Flar e 
Flare is the reverse of takeoff transition and also approximates a circular 
path. The plane transitions from descent at a stable approach angle, bring ing 
up the nose and slowing down until the airplane touches down with vertical 
velocity reduced to near zero. 
Touchdown speed VTD is 1.15 Vstall (1.1 Vstall for military) . The aircra ft 
decelerates from Va to VTD during the flare. The average veloc ity during the 
flare "j- is therefore 1. 23 Vstall (1.15 Vstall for military) . The radius of the flare 
circular arc is found by Eq. (17. 107) using "f', and where n = 1. 2 for a 
typical aircraft. 
The flare height can now be found from Eq. (17.1 10), and the horizo ntal 
distance during flare can be found from Eq. (17. 109). 
Although the deceler ation from Va to VTD would imply additional ener gy 
and thus additional distance, this is negligible because the pilot usuall y pulls 
off all remaining approach power when the flare is begun. 
lflfl Ground Roll 
After touc hdown, the aircraft rolls free for several seconds before the pilot 
applies the brakes. The distance is VTD times the assumed delay (1-3 s). 
The braking distance is determined by the same equation used for takeoff 
ground roll [Eq. (17.10 2)}. The initial veloci ty is VyD, and the final velocity 
is zero. 
The thrust term is the idle thrust. If a jet aircraft is equipped with thrust 
reversers, the thrust will be a negative value approxima tely equal to 40 or 50% 
of maximum forward thrust. However, the F ARs do not permit use of thrust 
reversing in meeting the certification requirements; what if they fail just when 
you need them? Thrust reversers are added to airplanes for safety and to save 
on brake wear, not to meet FAA certification requirements. 
Thrust reversers cannot be oper ated at very slow speeds because of reingestion of the exhaust gases. Thrust reverser "cutoff speed" is determined by 
the engine manufacturer and is typically about 50 kt [(85 ft/s) or {93 km/h }} . 
The ground roll must be broken into two segments using Eq. (17. 102) and the 
appropriate values for thrust (negative above cutoff spee d, pos itive idle thrust 
below cutoff speed) . 
Reversible propellers produce a reverse thrust of about 40% of static 
forward thrust (60% for turboprops) and can be used throughout the 
landing roll.


<!-- p.680 -->

678 Aircraf t Design : A Concep tual Approach 
The drag term can include the additional drag of spoilers, speed brake s, or 
drogue chutes. Drogue chutes have drag coefficient of about 1. 4 times the 
inflated frontal area, divided by the wing reference area. 
The rolling resistance will be greatly increased by the application of the 
brakes. Typical µ, values for a hard runway surface are about 0.5 for civil 
and 0.3 for military aircraft. Values for various surfaces are provid ed in 
Table 17. 1. 
The FAA requires that an additional two-thirds be added to the total 
landing distance of commercial aircraft to allow for pilot technique. Thus 
the "FAR field length" is equal to 1. 666 times the sum of the approa ch, 
flare, and total ground roll. 
MUii Effect of Wind on Takeoff & Land ing 
The effects of wind on takeoff and landing distances are difficult to model 
with a simple equatio n. During takeoff , the increased wind velocity increase s 
drag thus reducing acceleration, but the aircraft can take off at a lower 
ground speed so the net effect is a shorter takeoff distance. Transition and 
climb distances are reduced because, relative to the static ground, the aircraft 
is climbing more steeply. On landi ng, the rollout distance is reduced because 
of the slower approach and touch down ground speed, plus the increased aircraft drag after touchdown. 
As a very rough approximation for the effect of winds on takeoff and 
landing, each of the segment distances calculated above can be ratioed for 
winds. Find the square -root-a veraged veloc ity for each segment (0.29 times 
the initial speed plus 0.71 times the final speed) . The adjustment ratio is 
that value, divided by that value plus the wind speed. A time- domain 
3-DOF simulation is proba bly needed to get a good answer. 
The above assumes that the pilot is taking off or landing while facing into 
the wind. If for some reason a downwind takeoff or landing is attempted, all 
distances increase dramatically. Don't do that. 
4U'lj Un powe red La ndi ngs 
For an airliner-t ype landing, a mode rate power setting is used during the 
landing approach to keep the approach angle at no more than 3 degrees. If 
the power is pulled off compl etely, the approach angle is steeper. Even if 
the engine is shut down compl etely or is nonexistent as for a sailplane, the 
steeper approach angle isn't a problem-for a normal airplane 
For a high-drag vehicle such as a fighter with an engine flame-out or a 
Space Shutt le- like reent ry vehicle, the approach angle can be extremely 
steep. This may pose a severe enough problem that substantial vehicle aerodynamic redesign is required, such as a larger wing, higher aspect ratio, or 
increased fuselage fineness ratio.


<!-- p.681 -->

CHAP TER 17 Performance and Flight Mec hani cs 679 
The problem is that as an unpowered aircraft flares for landing, it must 
not run out of airspeed before a safe touchdown can be accomplished. If it 
has high drag and no thrust, it approaches the airfield at a steep descent 
angle as calculated using Eq. (17. 108). 
During the flare it increases angle of attack to level out its velocity vector 
and cut its sink rate to the value that the landing gear can safely handle. It 
needs to hold that safe sink rate for about 5 to 15 seco nds while waiting 
for the wheels to "find the groun d." But with no thrust and high drag the aircraft is slowing down rapidly. It might stall before touc hdown. 
The only solution, other than adding thrust or assu ming stronger landing 
gear, is to improve the L/D during pullup. This requires redesign. Diving to 
build up speed before the flare doesn't help, because that results in a steeper 
desce nt angle. 
if1I1J Other Figh ter Performa nce Measur es of Merit 
The standard measures of merit foF fighter aircraft including turn rate, 
corner speed, load factor, and speci fic excess power P5 do not compl etely distinguish between a good and a not- so-g ood fighter. For example, two fighters 
with exactly the same turn rate vs P5 will be widely different in comba t effectiveness if one aircraft has unpredic table and unco ntrollable behavior at high 
angle of attack. There is now great interest in defining new fighter measures 
of merit that can account for such differences. 
There are several key deficiencies in current measures of merit. First, they 
focus on steady-state performance abilities, whereas a real dogfight is characterized by continuous change in aircraft state. In the high-s peed yo-yo discussed earlier, the aircraft quickly pitches up, then rolls and turns at 
approximately corner speed for a few secon ds, then rolls to almost inverted 
flight, pitches up (down) again, and then rolls out and dives. 
While turn rate at corner speed is impor tant, the ability to rapidly execute 
these changes in state is also very impor tant. Furthermore, these changes of 
state are usually being executed simultaneous ly such as pitching and rolling 
at the same time (known affectio nately as "yank and bank "). 
Another deficiency is that the current measures of merit are oriented 
around the classical gun attack in which a tail chase with your oppon ent in 
front is the desired outcome. Modern missiles are so good that in comba t 
the first aircraft to point its nose at the opponent will win, regardless of 
energy state. Modern missiles have such good "off-bore sight" capability 
that even nose-poi nting might become irreleva nt- simply "see-a nd-shoot"! 
It must be remembered, however, that missiles are expensi ve and that 
each fighter can only carry a few of them. Future fighters must also have 
good classical dogfighting abilities, but maybe not quite as good as the fighters of old. This is true of the F-35, which has both amazing missiles and a synthetic vision system to help the pilot see- and-shoot. The tradeoff -reduced 
dogfight maneuverability, which is often criticized by "armchair aviators."


<!-- p.682 -->

680 Ai rcraf t Des ign: A Concep tu al Approach 
Classical fighter measures of merit also fail to address the impo rtance of 
what is called "decoupled energy management" to permit nonstan dard 
fighter maneuv ers. "Cou pled energy management" refers to maneuv ers in 
which potential and kinetic energy are exchanged. In the high-speed yo-yo, 
kinetic ener gy is exchanged for potential energy in the initial climb, and 
the pote ntial energy is then exchanged back for kinetic energy after the 
turn. This makes the aircraft predicta ble. 
In decoupled energ y management, the potential and kinetic energy are 
changed independen tly. For example, speed can be reduced rapidly and 
without gaining altitude by using large speed brakes and/or in-flight thrust 
reversing. 
Figure 17 .20 shows the "ener gy management envelope" measure of merit. 
In this extended version of energy maneu verabilit y, the maximum and 
minimum (most negative) P5 values obtainable are plot ted vs turn rate. If 
suitable controls over thrust and drag are available, the pilot can manage 
his energy state by sel ecting any Ps level within the envelope at a given 
turn rate . In the traditional evaluation of Fig. 17. 10, only the maximum P5 
obtainable is considered. 
Note from Fig. 17 .20 that an aircraft controllable after the stall has the 
option of developing a tremendous drag force for reduction of energy 
state. Under certain combat co nditions this can be used to force the 
opponent to overshoot. 
Also, turn rate is inversely prop ortional to velocit y. If an aircraft can be 
momen tarily slowed to extremel y low speeds, well below stall, the turn 
PS 
Max imum drag 
- - - - In -flight - -..... ....._ 
reverse th rust ' , 
' 
' 
' 
' 
Fig. 17 .20 Ene rgy ma nagement envelope. 
clmax 
at sta ll


<!-- p.683 -->

Roll rate 
CH APTE R 17 Performa nce and Fligh t Mec hanics 68 1 
Ideal air craft-no red uction in roll rate 
Ai rcraft A-good 
Ai rcraft B-poor 
Ai rcraft C-bad 
(roll reversa l) 
Fig. 17 .21 Loaded roll comparison . 
rate can greatly exceed that in conventJonal flight. This may allow a missile 
first-shot oppor tunity. This poststall maneuvering [128l was successfu lly 
employed on the X-31 test airc raft, the only X-plane to put on an aerial 
display at the Paris Air Show. 
The "loaded roll" measure of merit deals with the effect of angle of attack 
on roll performance. A number of existing fighters lose their roll ability at 
high load factors due to aeroel astic effects, adverse yaw, and aileron flow separation. An aircraft sluggish in roll during a high-g turn will be at a clear disadvantage. Figure 17.21 illustrates this comparison for a "good" aircraft, a 
"fair" aircraft, and an aircraft that experiences complete roll reversal. 
Reference [12 9] defines a number of alternative fighter measures of 
merit. 
AUl•ll Su perma neu ver and Poststa ll Maneu ver 
Fighter capabilities variously called postst all maneu ver (PSM), enhanced 
fighter maneuver, and supermaneu ver offer substantial advantages in 
close-in combat. With the successful flight test of the X-31, and the 
YF-22s demonst ration of 60-deg angle- of-attack operation, these capabilities 
have finally come of age. A supermaneuver capabili ty allows a fighter to point 
its nose at an oppon ent more rapidly, getting the first missile shot in a 
"face-to -face" dogfight. This is attained primarily by the combination of 
thrust-induced turning and dynamic turning, usually involving high angles 
of attack as described next. 
Contrary to science- fiction movies, a rocket can turn in space only by 
thrusting in a direction perpen dicular to the flight path (Fig. 17.22). This produces a turn load factor n that is the compon ent of thrust perpendicular to 
the flight path, divided by the weight of the vehicl e. Turn rate can then be 
expressed simply as equa l to (gn/V) .


<!-- p.684 -->

682 Air craf t Desi gn: A Conceptual Approach 
(No gravit y) 
30 \jl = Radial accel/ V=g (T !W)I V=gn/V 
I 
200 400 
Veloci ty 
600 
Flight path I 
- -Fig. 17 .22 Thrust-ind uced tur ning. 
Note that at zero velocit y, turn rate seems to go to infinity! While limited 
by pitch rate capab ility, a rocket could attain extremely high turn rates if it 
slowed to a very low speed. 
An aircraft can also turn using thrust, provided that its thrust can be 
angled to have a substan tial compone nt perpendicular to the flight path. 
This can be done in three ways. 
Figure 17 .23 shows one way to direct the aircraft thrust perpendi cular to 
the flight path, namely, by providing thrust-vectoring nozzles at or near the 
aircraft center of gravity. This allows the pilot to vector thrust at will, without 
concern for thrust-produced pitching moments . Such vecto ring is available 
on the Harrier and is proposed for the Revers e-Ins tallat ion Vectored 
Engine Thrust (RIVET) VSTOL concept. l130l 
For such a design, the turn- rate plot and the vectored thrust- induced 
turn- rate plot are essen tially summed. The wing can be kept at the angle 
of attack for maximum lift, while the nozzles are directed approxi mately 
30 
200 400 
No-gr avity turn 
Fig. 17 .23 Thrust vectoring at e.g. 
600 
Veloc ity


<!-- p.685 -->

CHAP TER 17 Performan ce and Fl ight Mech an ics 683 
perpendicular to the flight path for maximum instantaneous turn rate as 
proven in Eq. (1 7.57). 
Note that the wing stall limit line of Fig. 17.23 goes to zero rather than the 
level-flight stall speed. This indicates that we are mome ntarily ignoring 
gravity, going to a 90- deg bank to maximize instantaneous turn rate. 
Obviously, this can only be done for a few secon ds! 
Another option for vectoring the thrust perpendicular to the flight path is 
the addition of a thrust-vectored nozzle at the rear, as on the F-22. However, 
the F-22 nozzles cannot be used for thrust-induced turning because the 
downward vecto ring of thrust produces a large nose- down pitching 
moment. To be useful for thrust-induced turning, this pitching moment 
must be balanced by some nose-up momen t, which can be attained by the 
addition of a large canard as seen on the F- 15 STOL/ Maneuver demonstrator, and an early Lockheed JSF design concept. 
This approach, the aft-nozzle -plus- canard, allows the aircraft to retain 
the full turning ability due to wing lift, plus the additional vectored thrustinduced turning, down to the speed at which the canard stalls (Fig. 17.2 4). 
However, the large canard adds weight and drag. 
In the third option, the aircraft acts like a rocket, pointing its fuselage at a 
very high angle to the flight path (Fig. 17 .25) . The aircraft angle of attack is 
well past the stall angle (i.e., post stall maneuvering) . This clearly requires 
that the aircraft not just have flying abilities at poststall angles, but that it 
also retain good controllabil ity and accept able air quality into the inlet 
duct so that the engine continues running. 
This post stall thrust-induced turning, used by X-3 1, has several problems. It is difficult for the pilots because the airplane is flying in a direction 
downward through the floorboards! The pilot is blind in the direction of 
flight. A roll about the velocity vector looks like a yaw to the pilot, so disorientation is very pos sible: 
200 400 
No-gr avity turn 
Fig. 17 .2 4 Aft nozz le plus canar d . 
600 
Velocity


<!-- p.686 -->

684 Ai rcraf t Des ign: A Conc ept ual Approach 
30 
/ 
\ / ·- \ 
/ "- "'-./-,, ,,,.. / c,'<J .......... 
/. /.,-°> ><- - . / -../' ----- Thrust-i nduc ed turning / "_../" -- - --200 400 
No-grav ity tu rn 
600 
Veloci ty 
Fig. 17 .25 Fuselage poin ting. 
Also, flight into the post stall region means just that-the wing is stalled, 
and hence is producing only a fraction of its maximum lift. However, if velocity is slow enough, the jet thrust alone ensures that turn rate will be high 
anyway. 
In any case the drag at extreme angle of attack will be very high, and the 
thrust compone nt in the flight direction very small, so that the aircraft will 
---- ---- - Dece ler ate Fig. 17 .26 X-3 1 Sup ermaneu ver.
