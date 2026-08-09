# Raymer Ch.19 - Sizing and Trade Studies

*Converted from `Daniel P. Raymer - Aircraft Design_ A Conceptual Approach (2018, American Institute of Aeronautics and Astronautics Inc.) - libgen.li.pdf` by `tools/pdf_to_md.py`. Page markers are printed page numbers.*


<!-- p.709 -->

CHAPTER 18 Cost Ana lysis 707 
Equation (18 .14) determines the future value Vn after n years of an initial 
investment of value Vo, given an interest rate r. In Eq. (18.15 ), this is solved 
for the required investment today to yield a given future value. Vo is therefore 
the net present value Vnp as just described. The interest rate r is known as the 
"discount factor" in net-presen t-value calculation s. 
Vn = Vo(l + rt Vn Vo= Vnp = ( ) n l+ r 
(18. 14) 
(18. 15) 
The NPV of an airliner is the total of the net present values of all of the 
yearly oper ating profits during the life of the aircra ft (usually taken to be the 
depreciation period) . The yearly operating profits are the yearly revenues 
minus the DOC and IOC, not including depreciation. Depr eciation is not 
included in NPV calculation because it is the yearly apportionment of the 
purchase price. 
The NPV is determined by estimating the revenues and costs for each 
year of operation, including the effects of the estimated inflation. The 
yearly operating profit is then converted to NPV using Eq. (18.15). Finally, 
the NPV s of all of the years of oper ation are summed. To this is added the 
NPV of the salvage value of the aircraft at the end of its life (typically equal 
to 10% of purchase pric e) . 
The total NPV must be greater than the purchase price of the aircraft, or 
the investment will not return the expected normal rate of return, that is, the 
discount factor r. 
Selection of the appropriate discount factor is critical to the NPV calculation. The selected discount factor should be greater than the interest 
received from extremely safe investments such as government bonds, but 
should be less than the return from risky investments such as volatile 
stocks. The selected disco.unt rate should proba bly be no less than the real 
rate of return on the airline company's stock, which equals the yearly dividends plus the increase in stock value, divided by the stock purchase price. 
Alternatively, the discount factor can be solved for the value for which the 
investment just barely breaks even. The discount factor r for which the NPV 
exactly equals the investment is called the "internal rate of return"; it represents the equivalent interest rate returned by the airline investment. This 
can be compared to the expected rate of return on other investmen ts to 
determine if the new airliner is a good buy. 
What We've Learned 
Cost is the real design measure of merit and, for now, can be estimated 
with statistics.


<!-- p.710 -->

708 Ai rcraft De sign: A Concept ual Appr oach 
Adva nced Taille ss Airli ner Concept, D. Raymer , 201 1 (rendering by A. Ramir ez P.)


<!-- p.711 -->

Sizing and Trade 
Studies 
• Opti mi zation and trade stud ies tel l you how to mak e your air plane bette r. 
• Sizing is the hear t of ai rcraft opti miz ation -potent ial impr ove me nts mu st jus tify 
themse lves by a bet ter sizing result but without violati ng any req uir ements. 
• Class ica l ca rpet plo ts ar e sti ll power ful too ls, but modern MOO methods ar e far 
superior -wh en properly and rea li stica lly emplo yed . 
Introduc tion 
W e have come full circle in the design process. We began with 
a rough conce ptual sketch and a first-or der estimation of the 
T/W and W/S to meet the performance requirements. A 
"quick and dirty" sizing .method was used to estimate the takeoff weight 
and fuel weight required to meet the mission requirements. 
The results of that sizing were used to develop a conceptual design layout 
that incorpor ated considerations for the real world, including landing gear, 
structure, engine installation, etc. The design layout was then analyzed for 
aerodynamics, weights, install ed- engine characteristics, structures, stability, 
performance, and cost. 
The as-drawn aircraft might or might not actually meet all of the performance and mission requirements. The refined estimates for the drags, 
weights, and installed engine characteristics are all somewhat different 
from our earlier crude estimates. Therefore, the selected T / W and W / S 
are proba bly not optimal. The same is true for the aspect ratio, sweep, 
taper ratio, and other geometric parameters. 
Now we are ready to revisit the sizing analysis using our far greater 
knowledge about the aircraft. Refined trade-study methods will allow us to 
determine the size and characteristics of the optimal aircraft, which meets 
709


<!-- p.712 -->

710 Air c raf t Des ign : A Conc eptu al Ap proa ch 
all performance and mission requirements. Results from these trade studies 
will be used to make the Dash- Two drawing, which will be far clo ser to 
correct than the initial layout. 
Derai led Sizing Methods 
Equations (17.1) and (1 7.2) [repeated as Eqs. (19 .1) and (1 9.2)] define the 
sum of the forces on the aircraft in the Xs and Zs direct ions. The resulting 
accelerations on the aircraft are determined as these force summ ations 
divided by the aircraft mass (W/g): 
2-Fx = T cos ( a + <PT) - D - W sin y 
2-Fz = T sin ( a + <PT) + L - W cos y 
W =- CT 
(19 . 1) 
(1 9.2 ) 
(19 .3 ) 
Equation (19 .3) defines the time rate of change in aircraft weight as the 
specific fuel consumption c times the thrust. Equations (1 9.4) and (19 .5) 
determine the equivalent c and thrust for a piston- engine aircraft (see 
Chapter 5): 
v v C = Cpower - = Cbhp -550 
Y/p Y/p 
T = P_YJ_P = _55_o_b_h_p_YJ_P v v 
(1 9.4 ) 
(19. 5) 
These equations are the basis of the highly detail ed sizing programs used 
by the major airframe companies. In these programs the fuel weight is calculated by determining the actual drag as the airplane flies through its mission 
and from that determining the required thrust level and resulting fuel flow. 
The angle of attack and thrust level are varied to give the required total lift 
and the required longitudinal acceler ation depending upon what maneuver 
the aircraft must perform (level cruise, climb, accel erate, turn, etc.). Angle 
of attack and lift are restricted by the maximum lift available. The thrust 
level is restricted to the available thrust obtained from a table of 
installed -engine thrust vs altitude and velocity (or Mach number) . 
To improve the accura cy, the mission is broken into a large number of 
very short segments that can be less than 1 min in duration. The reduction 
in the aircraft weight during each of these short mission segments is determined by calcu lating the actual fuel burned based upon the required 
thrust setting. 
The computer iterates for sized takeoff weight by varying the assumed 
takeoff weight until the ending empty-weight fraction matches the emptyweight fraction determined by the detailed weight estimation. More sophisticated sizing programs will use statistical weights equations to autom atically 
recalculate the allowable empty weight for the sizing variati ons in takeoff 
weight, wing area, thrust, aspect ratio, and other trade parameters.


<!-- p.713 -->

CHAP TE R 19 Sizi ng and Tra de Stud ies 71 1 
Such methods go beyond the scope of this book. Those who take jo bs as 
sizing and performance specialists in major aircra ft companies will find that 
these giant computer programs are accurate enough to satisfy the licensing 
authorities and to prepare flight manua ls, but are difficult to use at the conceptual design level. 
f1 Improved Conc eptual Sizing Methods 
ltlll Revie w of Sizing Method 
For sizin g and trade studies during conceptual desi gn, an improved version 
of the method presented in Chapter 6 is presented. Remember that the aircraft was sized iteratively by assuming a takeoff weight. A statistical method 
was used to determine the empty weight for this assumed takeoff weight. 
The fuel used was determined by brea king the mission into mission segments, numbered from 1 to x. For each mission segment, the change in 
aircraft weight was calculated as either a miss ion-se gment weight fraction 
(Wi/ Wi- 1 ) due to fuel burned, or as a discrete change in weight due to 
payload dropped. 
Starting with the assumed takeoff weight, the aircraft weight was reduced 
for each mission segment either by subtracting the discrete weight or by multiplying by the mission- segment weight fraction. The fuel burned during each 
mission segment was totaled throughout the mis sion to determine the total 
fuel burned. A 6% allowance was added to the mission fuel to acco unt for 
reserve and trapped fuel. 
The aircraft takeoff weight was then calculated by summing the payload, 
crew, fuel, and empty weight. This calculated takeoff weight was compared to 
the assumed takeoff weight . A new assumed takeoff weight was selected 
somewhere between the .two, and the sizing process was iterated toward 
a solution. 
This same sizing process can be employed for sizing the as- drawn aircraft, 
but the method can be impro ved based upon our greater knowledge of 
the design. 
In the initial sizing before the aircraft design layout was prepared, the 
mission fuel was determined using simplified equations and statistical estimates of the aerodynamic proper ties and installed -en gine characte ristics. 
The empty weight was determined from statistical equations based only 
upon the takeoff weight. 
At this later stage in the design process, we can calcula te better estimates 
for the fuel used during each mission segmen t, and we have a better estimate 
of the empty weight based upon a detailed analys is of the as- drawn aircraft. 
These impro ved methods are presented next. 
Many of these methods rely upon calcula ting, by the methods of the 
performa nce chapter, the duration of time to perform the mission 
segment. The fuel burned during a duration of d at a given thrust T and


<!-- p.714 -->

712 Ai rcraf t Desig n: A Concept ual Approach 
specific fuel consumption C is then determined by Eq. (19 .6). The missionsegment fuel fraction is solved for in Eq. (19 .7), where C and (T/W)i are 
the average actual values during mission segment i: 
Wf; = CTd 
wi = 1 - cd(7-) 
Wi- 1 w i 
(19.6 ) 
(1 9.7 ) 
Note that if ( T /W )i remains esse ntially constant during the iteratio ns 
for takeoff weight, the result of Eq. (1 9.7) can be used unchanged for each 
iterat ion. This is the case for "rubber- engine" sizing. 
For "fixed-engine" sizing, Eq. (19 .7) would have to be recalcu lated for 
each iteration step because the T / W for a fixed thrust changes as the 
weight is changed. Altern atively, Eq. (1 9.6) can be used to calcu late the 
actual weight of the fuel burned by that fixed-si ze engine. The fuel burned 
is then treated as a weight drop in the sizing iterat ions. 
(A word of caution: Mission-seg ment weight fractions should range 
between about 0.9 and 1. 0. If a mission-se gment weight fraction is less 
than 0.9, the accuracy should be improved by brea king that mission 
segment into two or more smaller segments. If the mission- segment 
weight fraction is calculated to be greater than 1. 0, you have prob ably used 
the wrong units some where or have forgotten the negative sign on an 
exponent!) 
•at I Engine Start, Warmup, and Taxi 
In the initial sizing method, the mission- segment weight fraction for 
engine start, warmup, and taxi was lumped with the takeoff, and assumed 
to be 0.97 - 0.99. 
A better estimate for the fuel used during engine start, warmup, and taxi 
uses the actual engine characteristics to calculate the fuel burned by the 
engine in a certain number of minutes at some thrust setting. Typically, 
this would be 15 min at idle power. Equation (19 .7) is used to determine 
the resu lting missi on-se gment weight fraction. 
•au Takeoff 
The takeoff distance was broken into segments and calculated in Chapter 
17 . The time duration d of those segments is approxima tely the segment distance divided by the average velo city during the segment. Equation (1 9.7) can 
then be used to calculate the mission- segment weight fraction using the 
appropria te average takeoff thrust and fuel consum ption. 
Som etimes the design requirements can lump together the engine start, 
warmup, taxi, and takeoff into a single require ment based upon some 
amount of time at a given thrust setting. For military combat aircraft this is


<!-- p.715 -->

CHAPTE R 19 Sizi ng and Trade Stud ies 713 
usually 5 min at maximum dry power. For transpor ts and commercial aircraft, 
14 min at ground idle plus 1 min at takeoff thrust have often been specified. 
#111 Climb an d Acce ler ation 
The energy methods of Chapter 17 were used to develop Eq. (17 .97) for 
the mission-se gment weight fraction for a change in altitude and/or veloc ity 
[repeated as Eq. (19 .8)]. The average values of C, V, D, and Ts hould be used. 
A long climb or large change in velocity should be broken into segments 
such that the quantity C/[V (l - D/ T)] is appr oximately constant. 
Wi = exp [ -CA.he ] 
Wi-1 V(l -D/T) A.he= A(h + ;g V2) 
(19.8 ) 
(19.9 ) 
The distance travelled during clim.b is usua lly "credited" to the cruise 
segment that follows, that is, that distance is subtracted from the required 
cruise range. Distance travelled during climb is calculated as average veloc ity 
times the time to climb, which equals A.he/ P5• 
Im) Cruise and Loiter 
In Chapter 17, methods for determining the optimal velocities and altitudes for cruise and loiter were presented, and the Breguet equations for 
cruise and loiter were derived. Solving these for mission- segment weight 
fraction yields Eqs. (19. 10) and (19.1 1), where R is the range and E is the 
endurance time. 
Cruis e: 
Wi [-RC] 
Wi- 1 = exp V /D) (19. 10 ) 
Loiter: 
Wi [-EC] 
Wi- 1 = exp L/D (19. 11 ) 
Equation (19 .10) provides the mission- segment weight fraction for a 
cruise- climb, as discussed in Chapter 17. For a constant-airspeed, constantaltitude cruise, the cruise must be broken into shorter segments and the 
L/D revised as the weight changes. 
If your sizing mission speci fies some headwind, you must increase the 
required cruise range R in the mission- segment weight fraction equation 
by the ratio of velocities (Vairspeed/ Vgroundspeed) while still using the actual 
airspeed for Vi n the equation (see Chapter 17). Loiter is not affected by wind.


<!-- p.716 -->

714 Airc raf t Des ign: A Conceptual Appro ach 
4QO Com bat and Man euver 
Fighter aircraft are sized with a requirement for air-com bat time. This 
can be explic itly stated, such as "5 min at maximum thrust at 30,000 ft 
at 0.9 Mach number." Alterna tively, a certain number of turns at combat 
conditio ns can be specified. In that case, the time to perform the turns is 
determined from the performance methods of Chapter 17. 
Once the combat time is known, Eq. (19.7) can be used. 
MQU Desce nt 
Descent was statistica lly estimated in the initial sizing method , and no 
range credit was taken for the horizontal distance travelled during descent. 
A more accur ate calculation will proba bly yield a small improvement in 
sized takeoff weight. 
v = v(!_) - pV3CDo -2K (w) 
v W 2 (W/S) pV S (19.12) 
Descent is a negative climb, that is, thrust less than the drag. The climb 
equation devel oped in Chapter 17 is repeated as Eq. (19.12), in which Vy is 
vertical velocity or rate of descent. Descent is usua lly flown at cruise velocity 
and idle power setting, unless this produces an extreme descent angle 
(arcsine Vy/V). 
The time to descend is determined from the vertical velocit y, and the 
mission-segment weight fraction is determined from Eq. (19.7). A long 
descent should be broken into segments for greater accuracy. Also, credit 
should be taken for the distance travelled unless the mission requirements 
spe cific ally exclude range credit. 
{The detailed calculation of descent fuel is probably more trouble than it 
is worth for quick studies and student design proje cts. The earlier historical 
method [Eq. (6.22)] is usua lly good enough.} 
MQl:I La nding 
Landing was previously appro ximated by a small Wi/Wi-l fraction 
(0.992 -0.997). This is prob ably good enough even for more refined sizing. 
From obstacle clearance height to full stop takes less than 1 min and is 
usua lly flown at idle power. Even if thrust reversers are emplo yed, the 
impact upon total fuel weight is small because the thrust reversers are operated for only about 10 s. 
If more acc uracy is desired, the fuel for landing can be calcu lated by 
determining the time to land from the distances calculated in Chapter 17, 
using the average velocity for each landing segment. Then Eq. (19.7) can 
be employed.


<!-- p.717 -->

CHAPTER 19 Sizi ng and Tra de Stu di es 715 
#lfl Em pty-We ight Esti mation and Refi ne d Sizing 
Previously, the empty weight was estimated statistic ally using the takeoff 
weight. Now that we have a design layout, the methods of Chapter 15 can 
be used to calculate the empty weight for the as-d rawn aircraft by a detailed 
estimation of the weight of each major compon ent of the aircraft. 
During the first refined sizing iteration, the assumed takeoff weight is the 
as-drawn takeoff weight. The empty weight is the as- drawn empty weight. 
The fuel required is calculated using the refined methods just prese nted, 
plus an allowance for reser ve and trapped fuel (6%). 
Unless the designer has been very lucky, the takeoff weight calculated 
from the refined estimate of fuel burned and the as- drawn empty weight 
will not equal the as- drawn takeoff weight. The as- drawn takeoff weight 
was based upon initial sizing with limited information about the aircraft 
and cannot be expected to be very accurate. 
Because the calculated takeoff weight does not equal the as- drawn takeoff 
weight, the designer must iterate by ::issum ing a new takeoff weight. The 
empty weight must then be determined for the new assumed takeoff weight. 
It would be pos sible to go back to the detailed weight equations of 
Chapter 15 and recalculate the empty weight by summing the compo nent 
weights. Without the aid of a sophisticated comp uter program, however, 
the time involved would be prohibitive if this were done for each step of 
the sizing iteration. 
An approximate noncom puterized method relies upon the statistical data 
from Chapter 3 to adjust the as- drawn empty weight based upon the new 
assumed takeoff weight. Remember that Fig. 3.1 showed the trend of the 
empty weight ratio We/Wo decreasing with increasing takeoff weight. A 
good approximation for the new empty weight would be found by adjusting 
the as-d rawn empty weight ratio along the slope shown in Fig. 3.1 for that 
class of aircraft. The empty weight for the new assumed takeoff weight can 
therefore be estimated by adjusting the as- drawn empty weight for the new 
takeoff weight, as shown in Eq. (19.13). The value of C (not to be confused 
with SFC) represents the slope of the empty-weight-ratio trend line and is 
taken from Table 3.1. 
[ w, ] l+c 
w:- w: 0 e - easdrawn w; 
Oas drawn 
(19. 13) 
The value c typically equals (- 0.1), so (1 + c) equals about 0.9. This indicates that the empty weight as a fraction of takeoff weight will reduce as the 
assumed takeoff weight is increased. 
A statistical value of c (such as - 0.1) can be used, or c can be ca lculated 
from your aircraft concept. Make an arbitrary change in Wo, say a 10% 
increase, and recalculate We with all effects considered. These include 
changes in wing and tail areas, increased fuselage size, heavier landing


<!-- p.718 -->

716 Ai rcraf t Desig n: A Concept ual Approach 
gear, and larger engine. Then, with the new values as Wo and We, solve for c 
in Eq. (19.13 ). 
At this poi nt, sufficient information is available to size the aircraft using 
the sizing method of Chapter 6 with the improved estimates for fuel burned 
and empty weight. 
If the res ulting sized- aircraft weight substant ially differs from the 
as- drawn weight, the results shou ld be considered suspicious and the aircraft 
redrawn, reana lyzed, and resized. "Substantially different" is a matter of 
opinion, but this author gets nervous at a takeoff-weight diff erence greater 
than about 30% of the as- drawn weight. 
4wl•1 Photo-Sca le Problem 
The process of sizing scales the airplane up or down until it can do the 
design mission. As this scaling occurs, there is a poten tial problem: the 
scaling can change the values of the aerod ynamics, propulsion, and weights 
parameters estimated from the drawing. The empty weight will definitely 
change and, as already discussed, even the ratio of empty weight to gross 
weight will vary. This was shown back in Fig. 3.1 and is the reason that 
Eq. (1 9.3) is used. This usua lly works just fine. 
The propulsion parameters might or might not change. If an actual 
(fixed- size) engine is being used, the propulsion won't change at all except 
perhaps some microscopic variation in the propulsion-r elated drags. If a 
rubber engine is being used, it can be scaled up or down to keep T / W the 
same. The speci fic fuel consum ption would remain the same, so propu lsion 
isn't really a problem either way. 
The aerod ynamic coefficients are nondimensiona lized based on the wing 
area. As the entire design is sca led up or down, the reference wing area 
scales too. The most impor tant parameters for drag analysis are the wetted 
area and maximum cross-s ection area. If the airplane is scaled photog raphically, these areas will scale by the same ratio as the reference area. This means 
that, to a good first approximation, the aerod ynamic coefficients calcula ted 
for the drawing can be used without change, provided that the sizing calculations stay close to the baseline TOGW , say 10 - 20%. 
Som etimes, though, the sizing calculations move far from the baseline 
TOGW . This can introduce sizing errors due to photo -scale problem s. 
First, no design really photo -sc ales because of the infamous square-cube 
law. If the TOGW is halved, the wing area should be halved also, to keep 
the same W / S. This is a photo- scale by a length factor of the square root 
of (1/ 2). If that is applied to the whole airplane, the internal volume is 
found from the cube of the length scaling, that is, a factor of (1 /2) raise d 
to the 3/2 power, or 0.35 4. But the weight was only halved, so the aircraft 
doesn't have enough internal volume. To keep a reason able volume tric 
dens ity, something will have to be larger than the phot o-sca le would 
produce, probably the fuselage.


<!-- p.719 -->

CHAPTER 19 Sizing and Tra de Stu di es 717 
Even worse, sometimes it just isn't possi ble to make the fuselage any 
smaller than its baseline size. In a recent parametric study of future airliners, 
the aggressive application of future technologies resulted in some concepts in 
which the sizing results scaled the airplane down by 50% in TOGW. [12l While 
wings and tails and nacelles could scale acco rdingly, what about the passenger compartme nt? It still has to hold the pass engers, crew, cargo, galleys, and 
toilets. None of those get smaller just because the sizing calculation says 
TO GW is reduced. The net effect is that as the aircra ft scales down in 
TOGW, the drag coefficient will actually increase. The unchanged fuselage 
drag value is referenced to the now smaller wing area. 
This is proper ly handled by redrawing the airplane for each "guess" of 
TOGW in the sizing process. Sophisticated sizing programs do just this 
internally, but for quick calculat ions, a reaso nable appr oximation is desired. 
Equation (19 .14) adjusts the parasitic drag coefficient for the perce ntage 
of wetted area that will not phot o-s cale (X), most likely the fuselage. For 
example, if the sizing calculation scales to 50% of TOGW, and 35% of the 
as-drawn wetted area will not phot o-sc ale, then a parasitic drag coefficient 
of 100 counts (0.0 100) will increase to 120 counts. 
CDo CDo = (1 - X)CDo + x 0 666 (Wo/Wo-asdrawn) · 
(19. 14) 
The square -cube and smallest-fus elage problems also affect the empty 
weight scaling. For the previous future transport study, a detailed analysis 
found that because the fuselage could not be scaled down any further, the 
empty weight did not reduce nearly as much as expected when the sizing 
process reduced the TOGW. Referring back to Fig. 3.1, this amounts to a 
much steeper slope. Table 3.1 gives the exponent for the empty weight fraction as - 0.06 for a typical transport. When the photo -sca le problem is fixed, 
this changes to - 0.3 1, a huge diff erence. 
For most desi gn efforts, and cer tainly for student projects, the photo -sca le 
problem can be ignored. The effect is usually seen only in extreme trade 
studies, or when the initial sizing was so far off that you almost have to 
start over anyway. 
Classic Opti miz ation -Sizing Matrix and Ca rpet Plots 
MQll Im proving the Dash- One 
The sizing proced ure ensures that the as- drawn aircra ft, proper ly scaled 
to the sized takeoff weight, will meet the required mission range. However, 
there is no assurance that it will still meet its performance requireme nts or 
that it represents the best possi ble combination of desi gn parameters . 
Prior to making the design layout, various design parameters were 
selected based on quick calculations or historica l trend lines. These include 
thrust-to- weight ratio and wing loading, the wing parameters such as aspect


<!-- p.720 -->

718 Air craft Desig n: A Concept ual Appr oach 
ratio and sweep, and the fuselage fineness ratio and others. Optimal values for 
all of those parameters can now be found, as a part of a process that include s 
finding the lightest and cheapest airplane while ens uring that performa nce 
requirements are met. 
It would be poss ible to take the as-dr awn airplane and simpl y adjust 
its T / W, W/ S, and other parameters until all perfo rmance requir ements 
are met. This "hit or miss" method would be time consuming and would 
not guarantee that the best airplane was found. Inst ead, optim ization 
methods are employed. 
The Kuhn - Tucker Theorem of 19 50 is widely used in the proofs of 
analytical optimization methods. Fundamenta lly, it says that at the 
optimum the only direction you can move to improve the objective function 
is one that will violate one or more const raints . This is the essence of aircraft 
optimization methods, which long predate Kuhn -Tucker. We airplane 
designers are always looking for the lightest airplane and finding that we 
are blocked by performance con straint lines. 
Classic aircraft optimizat ion methods are parametric. To find the 
optimum, we change a few parameters and see what happens. For the 
chosen changes in parameter, such as T / W and W / S, we calculate the 
effect upon sized takeoff gross weight, performance, and cost. In the classic 
methods, raw parametric data are then "massaged" into a graphical presentation so that the optimum can be found. Advanced optimization methods 
do it differently, but the result is the same. 
There are many aircraft design parameters that can be optimized by such 
methods. Trade studies categories are discussed later. 
4Qf J Sizing Matrix Plo t 
The classic two-variable aircraft optimization method is called a "carpet 
plot." There are actually two versions of this, based on the same analysis 
but displa yed in slightly different graphica l formats. For either format, two 
selected variables are parametr ically varied and used to calcul ate aircraft 
sizing and performance, creating a matrix of analysis results. A graphical 
method then allows selec ting the optimal values of the two variables. 
For aircraft design optimization, the main two variables in the optimization are usually the thrust-to-w eight ratio T/W and wing loading W/S. 
Other possi bilities are discussed belo w. 
The carpet plot begins with a paramet ric sizing matrix as shown in 
Fig. 19.1. The thrust-to -weight ratio T /Wa nd wing loading W/ S are arbitrarily varied from the as- drawn bas eline values, typically by plus and minus 20%. 
Each combination of T /W and W / S produces a different airplane, with different aerodynamics, propulsion, and weights. These different airplanes are separately sized to determine the takeoff weight of each to perform the design 
mission.


<!-- p.721 -->

T/W= l . I 
T /W= I. 0 
T/W = 0.9 
WIS= 50( lb/ftl) 
Ll 
Wo = 56,000 lb 
P, = 700 fps 
(M0.9, 30k ft, 5g's) 
s,o = 340 ft 
a= 46 s 
L±. 
W0 = 48,500 lb 
P, = 430 fps 
s,o = 450 ft 
a= 50.5 s 
W0 = 44,000 lb 
Lz. 
P., = 14 0 fps 
s,() 670 ft 
a= 56 s 
CHAP TER 19 Sizing and Trade Stu di es 719 
W/S=6 0 WIS=7 0 
u 
W0 = 46,000 lb Ll. W0 = 49,000 lb 
Ps = 330 fps P, = 30 fps 
s,o = 430 ft s,o = 660 ft 
II= 42 S a= 39 s 
Resized base li ne Ll. L2. 
W0 = 43,700 lb W0 = 42,000 lb 
P, = 30 fps Ps = -19 0 fps 
s,o = 595 ft 
s,o = 800 ft 
a= 45 s 
a =4 7 s 
W0 = 39,000 lb 
LI. W0 = 36,0 00 lb L2. 
P, = -230 fps P., = - 320 fps 
s,o = 810 ft s/o = 10 10 ft 
a= 53 s a= 51 s 
Require: P, :?0 at M0.9, 30 k ft {914 4 m}, 5g' s 
s,o <;; 500 fl { 15 2 Ill) 
a 50 s from M0.9 to Ml .5 
Fig. 19 .1 Sizing matrix. 
They are also separa tely analyzed for performance. If the T /W and W / S 
variations are wide enough, at least one of the aircraft will meet all performance requirements, although it will proba bly be the heaviest airplane when 
sized to perform the mission. 
Figure 19.1 shows trade study data for a small fighter. Nine T/W- W/S 
variations of the aircraft have been sized and analyzed for takeoff distance 
Ps and acce leration time. Performance requirements for this example are a 
takeoff distance under SOO ft {152 m}, zero Ps at Mach 0.9 and 5g at 
30,000 ft {914 4 m}, and an acceleration time under 50 s from Mach 0.9 -1 .5. 
From the data in the matrix, it can be seen that the as- drawn baseline 
(number 5) exceeds the requireme nts except for takeoff distance. Number 
3 exceeds all requirements but is very heavy. Numbers 4, 7, 8, and 9 are 
deficient in some requirement but lighter in weight. The question is: 
"What combination of T/W and W/S will meet all of the requirements at 
a minimum weight?" 
Optimization of T /W and W/ S requires cross plot ting the sizing matrix 
data, as shown in Fig. 19.2. For each value of thrust-to -weight ratio, the sized 
takeoff gross weight P5 and takeoff distance are plotted vs wing loading. The 
data points from the sizing matrix in Fig. 19. 1 are shown as numbered black 
dots. (The acceleration data points were plotted in a similar fashion, but not 
shown.) 
From the takeoff-weight graphs in Fig. 19 .2, the wing loadings corresponding to regular ly spaced arbitrary gross weights are determined. For


<!-- p.722 -->

Takeoff wei ght 
W0 (1 000 lb) 
60 1 
50
11--! __ _ :
__ 3 
- 40 
30 ---+--- ' 1 
0 50 ....; 
11 6 
- 40 ---- t ------------- w 
i 
Ps at M. 9, 30,000 ft 5 g's 
Ps (1 00 fps) 
1 
6 
4 
2 
al -3 
-2 
6 ' 4 
4 
2 
I ---------''\'\ 0 l"" "" "" '-'f ----2 
6 
4 
i 
d 7 8 9 11 
----- I_ _________ _ t - ------ f 
- - \\\ _'.' \\\\ \ 
-2 
50 60 70 
WIS 
50 60 
WIS 
70 
Fig. 19 .2 Sizing matrix crossp lots . 
s (1 00 ft) 
10 
8 
6 
Takeoff dis tance 
3 
-FT": 
10 6 
8 
6 -,,,,, ,, , 
4 
2 
0 
10 
8 
6 
4 
2 
0 50 60 
WIS 
9 
70 
..... 
N 
0 
? 
0 
0 
<t> 
(J) 
<O" 
::; 
)> 
0 
0 
::; 
0 
<t> 
"O .... 
c 
Q 
)> 
"O 
"O 
0 
Q 
0 
:r


<!-- p.723 -->

CHAP TER 19 Sizi ng and Tra de Stu die s 72 1 
this example, gross weights at 5000-lb increments were selected. For these 
arbitrary weight increments, the correspo nding W / S values are shown as 
circles on Fig. 19. 2. 
The W / S and T / W values for the arbitrary gross-w eight increme nts are 
transferred to a T/W- W/S graph as shown in Fig. 19 .3. Smoot h curves 
are drawn connecting the various points that have the same gross weight 
to produce lines of constant-size takeoff gross weight (Fig. 19 .3). From 
these curves one can readily determine the sized takeoff weight for variations 
of the aircraft with any comb ination of T /W and W / S. 
Next, the W / S values that exactly meet the various performance requirements are obtained from the performance plots for different T / W values 
(right side of Fig. 19 .2) . These values are again shown as circl es. 
These combinations of W/S and T/W that exactly meet a performance 
requirement are transferred to the T / W - W / S graph and connected by 
smooth curves, as shown in Fig. 19 .4. Shading is used to indicate which 
side of these "constraint lines" the desired answer must avoid. 
The desired solution is the lightest aircraft that meets all performance 
requirements. The optimum combination of T / W and W / S is found by 
inspection, as shown in Fig. 19 .4, and usua lly will be located where two 
constraint lines cross. 
This example showed only a 3 x 3 sizing matrix. For better accur acy, 
5 x 5 and larger sizing matrices are used at the major aircraft companies 
but require more work. 
45 K 
1.10 
1. 05 
- ::--- 1. 00 
h 
40 K 
0.95 
40 K 0.9 +-----<. ,_-------< ---------------45 50 55 60 
WIS 
65 
Fig. 19 .3 Sizing matrix plo t (conti nue d) . 
70 75


<!-- p.724 -->

722 Airc raf t Desig n: A Concep tua l Approach 
1.10 
1. 05 
- 1. 00 
h 
0.95 
0.9 +--l >-----.----.lfl-----r----(J----. ----.-----,..;:r-------. 
45 50 55 60 
WIS 
65 
Fig. 19 .4 Sizing matrix plo t (concluded). 
4Qff Carpet Plo t 
70 75 
Another format for the sizing matrix optimization actually looks like a 
carpet, at least according to some people. This carpet plot is based upon 
superimposing the takeoff weight plots from Fig. 19 .2. 
In Fig. 19.5, the upper-left illustration from Fig. 19.2 is repeated showing a 
plot of sized takeoff gross weight Wo vs W/S for a T/W of 1.1. The points 
labeled l, 2, and 3-d ata points from the matrix (Fig. 19 .1)- represent 
wing loadings of 50, 60, and 70 psf {244, 293, and 342 kg/m2}. 
The next illustration of Fig. 19.5 superim poses the next Wo vs W/S plot 
from Fig. 19.2. This plot represen ts a T / W of 1. 0. The data points labeled 4, 5, 
and 6 again represent wing loadings of 50, 60, and 70. 
To avoid clutter, the horizontal axis has been shifted to the left some 
arbitrary distance. This shifting of the axis is crucial to the development of 
the carpet-plot format. 
In the lower illustration of Fig. 19.5, the third curve of Wo vs W/S has 
been added, again shifting the horizo ntal axis the same increment. The 
points labeled 7, 8, and 9 again represent wing loadings of 50, 60, and 70. 
Now these regular ly spaced wing-lo ading points on the three curves can 
be conne cted, as shown. The resu lting curves are said to resemble a carpet, 
hence the name. The horizo ntal axis can be removed from the carpet plot 
because one can now read wing loadings by interp olating between the curves.


<!-- p.725 -->

W0 (1 000 lb) 
60 1 
50 
40 
30 50 
TIW= 1.1 
60 70 
WIS 
CHAP TER 19 Sizi ng and Trade Stu di es 723 
W0 (1 000 lb) Shif ted sca le 
for next TIW 60 1 
50 
40 
30 -: 50 
50 
60 
60 
70 WIS for 1, 2, 3 
WIS for 4, 5, 6 70 
W0(10 00 1b) WIS=5 0 60 
50 
40 
30 
Fig. 19 .5 Carpet plo t format (sa me resu lts!). 
In Fig. 19 .6, the wing loadings that exactly meet the takeoff P5 and acceleration requirements (from Fig. 19.2) have been plotted onto the carpet plot 
and connected with con straint lines. The optimal aircra ft is found by inspection as the lowest point on the carpet plot that meets all constraints. This 
usually occurs at the intersection of two cons traint curves. 
It is possi ble to create sizing plots in which the measure of merit is cost 
rather than weight. The plotting proced ure is the same except that cost values 
are used rather than weight values in the development of the sizing plot. 
60 
50 
40 
30 
WIS=5 0 
Fig. 19 .6 Comple ted carpet plot. 
TIW= 1.1 
TIW= l. O


<!-- p.726 -->

724 Air cr aft Desig n: A Con cept ual Approach 
However, for most aircraft types the minimization of weight will also minimize cost for a given design concept. 
Trade Studie s 
MP,jl Trade Study Categorie s 
Trade studies produce the answers to design questions beginning with 
"What if ... ?" Proper selection and execution of the trade studies is as 
impor tant in aircraft design as a good configurat ion layout or a correct 
sizing analysis. Only through the trade studies will the true optimum 
aircraft emerge. 
The "grand daddy" of all trade studies is the T / W - W / S carpet plot . This 
is such an integral part of aircraft analysis that it is not usually even thought of 
as a trade study. A T / W - W / S carpet plot in good measure determines the 
minimum -weight aircraft that meets all performance requirements. 
Table 19.1 shows a number of the trade studies common ly cond ucted in 
aircraft design. These are loos ely organized into design trades, requirements 
trades, and growth sensi tivities. 
Des ign trades reduce the weight and cost of the aircraft to meet a given 
set of mission and performance requirements . These include wing-geome try 
and propulsion variati ons as well as configurat ion arrangement trade s. 
Table 19 . l Typical Trade Studie s 
Design trades 
T/ Wa nd W/S 
A, A 
t/c, A 
Air foil shape and camber 
High -lif t devices 
Fuselage finene ss ratio 
BPR , OPR, TIT, etc . 
Prope ll er dia meter 
Materials 
Configur ation 
Toil type 
Variable sweep 
Numb er and type of engi nes 
Maint ainabil ity featu res 
Obser vable s 
Passenger ar rangement 
Adva nced tech nologies 
• 1 11 • 
Range / payload / passenger s 
Loiter time 
Speed 
Tu rn-rate, P5, nmax 
Runway length 
Tim e-to-climb 
Signatur e level 
Desig n-to-cost 
Growth Sensitivit ies 
Dead weight 
C v0 
K 
CDwave 
clmax 
Thrust 
SFC 
Fuel pric e


<!-- p.727 -->

CHAPTER 19 Sizi ng and Tra de Stu die s 725 
Requirements trades determine the sensiti vity of the aircraft to changes in 
the design requirements. If one require ment forces a large increase in weight 
or cost, the customer can relax it. 
Growth-sens itivity trade studies determine how much the aircraft weight 
will be impacted if various parameters such as drag or specific fuel consumption should increase. These are typically presented in a single graph, with percentage change of the various parameters on the horizontal axis and 
percentage change in takeoff weight on the vertical axis. 
An important but misundersto od growth-sen sitivity trade study is called 
"Dead Weight." This is a catch-all phrase for "the airplane empty weight 
might increase by X pound s." It might come about because the structure is 
heavier, or the tires need to be made larger, or more avionics was added to 
the design. Perhaps a new technol ogy turned out to be heavier when it 
went from labora tory to reality (like, every time). Perhaps the airplane was 
out of balance and some ballast had to be added. 
We use the concept of dead weight in trade studies to calculate how sensitive the design will be to any weight in-rease that may happen later in development. When the actual aircra ft is finished and put up on scales, there is no 
dead weight! But there may be additional weight due to problems like those 
mentioned above . During conc eptual design, our Dead Weight trade studies 
have hopefully warned us their impact even before they happen. And hopefully, that weight isn't too much. 
Be aware of an impor tant cons ideration in all of these trade studies: the 
realism factor. There is an unfortunate tendency to minimize redesign 
effort, espe cially for yet another boring trade study! If asked to study the 
impact of carrying two more internal missiles, the designer might find a 
way to "stuff them in" wi thout changing the external lines of the aircraft. 
This might complet ely invalidate the results of the trade study. If there 
were sufficient room in the base line to fit two more missiles interna lly, 
then the baseline was po.orly designed. If the baseline was alread y "tight," 
then the revised layout must be a fake! 
The best way to avoid such problems is to insist that all redesigned 
layouts used for trade studies be checked to maintain the same internal 
density as the baseline, calculated as takeoff weight divided by internal 
volume. The various "customer" organizations, especi ally Naval Air 
Systems Command, had graphs showing what a reasonable volumetric 
density would be for various aircraft types. If your design didn't fall within 
the historical trend line, they declared that your design wouldn't workbut they wouldn't show you the magic graph! 
A more-so phisticated approach called "Net Des ign Volume" was dev eloped by this author to ensure that each trade -st udy-modified aircraft 
design will have sufficient internal volume to hold the payload, fuel, and 
other internal components. Suitable for computerized aircraft optimiza tion 
methods, it takes few additional inputs beyond those already needed for 
the aircraft analysis used by such methods. l137l


<!-- p.728 -->

726 Airc raf t Desi gn: A Concep tual Approach 
The T / W- W/ S carpet plot is described above as the "granddad dy" of all 
trade studies. When doing trade studies of other variables as shown in 
Table 19. 1, each paramet ric variation of those other variables should be 
calculated using a complete T/W- W/S carpet plot for each data point. 
Other wise, the answers aren't belie vable because the initial values of 
T/Wand W/S might be forcing the answer to a non-o ptimal direction. 
For example, to determine the optimal aspect ratio the designe r might 
parametrically vary the baseline aspect ratio up and down 20%. For each 
aspect ratio, a T / W- W / S carpet plot would be used to determ ine the 
minimum-w eight airplane. These minimum weights would then be plotted 
vs aspect ratio to find the best aspect ratio. 
If the designer wished to optimize for, say, aspect ratio and sweep, a 
matrix of parametric variati ons of these would have to be define d. At a 
minimum, this would consist of three variations of each, or a total of nine 
variations. For each variation, a T/W- W/S carpet plot optimization would 
be done, each with nine variat ions of T /Wa nd W / S, to find the best possib le 
aircraft for the specified combination of aspect ratio and sweep. 
These nine resulting "bests" would be used to make an aspect- ratio-s weep 
carpet plot to finally find the "best best." Notice that 9 x 9, or 81 parametri c 
variations of the aircraft, would have to be defined and analyzed as to aero dynamics, propulsion, weights, sizing, and mission performance. This allows 
a "mult ivariable optimization" of aspect ratio, sweep, T / W, and W/ S. What a 
lot of work! 
But what about taper ratio? And t/ c? And fineness ratio, and bypass ratio, 
and ... ? 
Mtlfj Mu ltivar iable/Mu ltid isci plin ary Design Opti mi zation 
As this example shows, the workload for multivariable optimization trade 
studies will rapid ly exceed manual capabilit ies. To optimize T / W, W / S, 
aspect ratio, taper ratio, sweep, and thickness (the basic set of design parameters) requires a minimum of 36, or 729 data points (56, or 15 ,625 data 
points would be better) . Each data point represents a different airplane and 
requires full analysis for aerod ynamics, propulsion, weights, sizin g, and performance. Also, you need a technique to find the best aircraft by interpola ting 
between those 729 cases. How do you draw a six- dimensional carpet plot? 
To truly optimize an airc raft, even more design parameters from 
Table 19.1 such as fuselage fineness ratio and engine bypass ratio or propelle r 
diameter should be included in a simultan eous optimization. In fact, one 
could attempt to simultaneo usly optimize all of these and many more and 
also have the compu ter optimally change the actual shape of the design 
including wing planform breaks, nacelle locations, and tail locations, and 
perhaps optimize the airfoils and the APU installation at the same time. 
Such "everything optimization" is neither feasible nor desirable. After a 
certain point, excessi ve time spent on defining, execu ting, and understan ding


<!-- p.729 -->

CHAP TER 19 Sizi ng and Trade Stu di es 727 
an optimization method or computer program is just time taken away from 
other pressi ng design tasks. 
All optimization methods must revolve around one or more measures of 
merit, which implies that we know exactly how the aircraft will be op erated. 
In the histor y of aviation, there has prob ably never been a case of an aircraft 
flying its "design mission," that is, the exact same mission that was used for 
sizing and optimization during its concept ual design. Even if a pilot looked up 
the original desi gn mission and tried to duplicate it in flight, it could not be 
done unless the pilot could find a perfect standard day and happened to have 
a perfect, nominal engine and an aircraft whose design was not changed or 
compromised during development. 
Even more impor tant, most aircra ft are converted to missions that were 
never anticip ated during their design. The F-4, one of the most successful 
fighters of all time, was designed for a supersonic, deck-la unched interc eption missio n totally unrelated to its widesp read use as a multirole fighterbomber. The F- 16, in use around the world, was concei ved, sized, and optimized as a lightweight dogfighter with tt"ie designers ' battle cry "not a pound 
for air-to-g round." It is now the U.S. Air Force's main ground- attack fighter 
(but is still a potent air-to- air machin e) . 
Another problem is that aircraft optimization is, by definition, making 
changes to the shape of the aircraft. After wading through almost 800 
pages of aircraft desi gn methods emp hasizing the actual conceptual layout, 
the reader should now scream, "but how does the compu ter know if the 
landing gear fits, and the radar fits, and the pass engers fit, and the fuel 
tanks are big enough, and the overnose vision angle is still correct, and ... . " 
Of course, each of these and many more could be programmed into the 
optimizer, but the time to develop all the inputs for such an optimization 
model must be consi dered against the time const raints of concept ual 
design. The Net Design Volume approach mentioned above is a reasonable 
approximation to mainta ining volumetric realism during an optimization, 
but it isn't per fect and doesn't fully cap ture the geom etric change s. 
There is another, very human problem to con sider. Once a timeconsuming optimization model is developed for a certain design approach, 
there will be an understandable reluctance to look at totally different 
design app roaches that are not represented by the model. If a certain trade 
study would be very difficult to model and opt imize with the tools in use, 
it is easy to convince oneself that it "proba bly won't work anyway." This 
could serve as a dampener on the essence of aircraft concep tual design. 
However, if we are careful to use opt imization in a balanced fashion, with 
experienced designers always "in the loop," it can be a very powerful tool 
for improving our design. In this author's opinion, it is best used when 
based on analysis of a realistic and complete aircraft conceptual design 
layout and when its goal is to quickly tell the aircraft designer how to 
change the design layout to make it better and is used in the next design iteration as only one of many "inputs," as described in Chapter 2.


<!-- p.730 -->

728 Ai rc raft Desi gn: A Conceptu al Appr oach 
There are many mathematical techniques for multivariable optimi zation 
including the repet itive use of carpet plots as already described. Better, thmultivariable parametric data as alread y discussed can be fit to an approximating multidim ensional surface equation called a "response surface," 
which can then be mathematically or numerica lly solved for an optim um. 
A concept called "Latin squares" was used at a number of companies 
including Boeing. It can be viewed as a mathematical approximation for redu cing the number of data points needed to be calculated and is related to the 
"Design of Experiments" method. Esse ntially, Latin squares tells you which 
data poi nts to skip and how to approximate the results that the skipped 
points would have provided. It is analogous to the old sizing expert's tricksurpris ingly good-of drawing a family of curves from five data poi nts. 
Another technique for multivariable optimization uses a "finite difference" 
approach. Small parametr ic changes are made to the aircraft one at a time, and 
the change in the measur e of merit (such as sized takeoff weight) is used 
to define a slope (first derivative) of the "system response" to a change in 
that variab le. These derivatives are then used to predict the optimum solution, 
and iteration is used to drive out the obvious linearization errors. 
This author has had good results with exhaustive searching by a simple 
gradient method to simultaneously optimize an aircraft for the six basic 
design parameters just described J138l Each variable is paramet rically varied 
by plus and minus some selected "step size, " and the resulting aircraft are 
all analyzed for aerod ynamics, weights, sizing, cost, and performance. The 
"best" variant, that with the lowest value of the selected measure of merit, 
which also meets all performance requirements, is remembered and, when 
all parametric variati ons about the initial baseline are exhausted, becomes 
the center point baseline for the next iteration loop. This continues until 
no better variant is found, then the stepping distance is shortened and the 
process repeated until some desired level of resolution is obtained. 
Multidisciplina ry design optimization (MDO) carries multivariable 
optimizat ion to the next stage: the optimization of systems across widely 
different functional areas. J. Sobieski of NASA Langley Resea rch Center 
defines MDO as "a methodolo gy for design of comple x engineering systems 
that are governed by mutually interacting physical phenom ena and made up 
of distinct interacting subsy stems" and goes on to explain MDO as suitable 
for systems for which "in their design, everything influences everything 
else". l138l 
That is, in fact, a pretty good description of aircraft conc eptual design, 
and the various multivariable optimizations just des cribed can be viewed 
as MDO-e ven the simple sizing carpet plots that, after all, optimize over 
disp arate disciplines of aero dynamics, weights, propulsion, sizing, and 
performance. 
MDO, though, seeks to carry the level of analysis to a much higher level 
without losing the interconnec tivity of the different functional areas. Ideal 
for engineering systems for which no single mathematical model is possible,


<!-- p.731 -->

CHAPTER 1 9 Sizing and Trade Stu di es 729 
it permits assembling mathematical models from different functional disciplines such as aerodynamics and structures and then deriving system 
optimizations. 
MDO methods include the finite difference technique just discussed, as 
well as more exotic techniq ues. The Implicit Function Theorem method 
differentiates the various governing equations to obtain sens itivity equat ions. 
These are used to set up simultaneous linear algebraic equatio ns, which are 
then solved for an optimal solu tion. 
"Decompo sition" works by partitioning a large engineer ing design optimization probl em into a number of smaller, solvable problems ("submodu les") . 
During execution of the optimizer, top-le vel routines pass data between the 
submodules in a structured manner that retains their coupling and accommodates the defined system constraints. For example, a wing analysis 
decomposition might have an aerod ynamics module that knows how to calculate drag and airloads if it knows the wing shape, and a structures module 
that knows how to calculate weight and structural deflections if it knows the 
airloads. Each executes separ ately, passiRg their results to the other until they 
converge at an optimum for the measure of merit such as weight or drag, or a 
blended bit of both. 
The "response surface" method addre sses the problem of excessi ve calculation to find the optimum by fitting a mathematical surface to a collection 
of parametric design variations. Actually, the classic aircraft design carpet 
plot described above is a graphic ally fit response surface but limited to 
three dimensions (two variables and the measure of merit) . 
The mathematical response surface (RS) method permits far more variables and is a leading tool of MDO resea rchers and aircra ft designers alike. 
In addition to the large reduction in the number of full design evaluations 
that must be calculated, RS has a further advantage of naturally smo othing 
out numerical noise resµlting from the parametric analysis. Be careful, 
though-if the equation form of the RS is lower than third degree, any 
reflexes in the actual surface will be smoot hed over and the answer will be 
wrong. Fourth or fifth degree would be even better, but the calculation 
time goes up dramatically. 
Another benefit of the response surface method is that the design points 
are selected and evaluated external to, and prior to, the optimizat ion. This 
makes it pos sible to select design points and have real engineers working 
offline do the design and analysis work to calculate the system-le vel response 
to changes in the design variables. One company goes so far as to have 
designers prepare initial layouts of dozens of different aircra ft concepts spanning the range of parametric design variables. These are then analyzed, fit to a 
response surface, and an optimum is determined. 
The "genetic algorithm" approach works by applying a process of "survival of the fittest." While Darwin is not norma lly asso ciated with aircraft 
design, the modeling of aircraft characteristics as "genes" of design variab les 
shows much promise. The design variables are coded into binary strings such


<!-- p.732 -->

730 Ai rcraf t Desig n: A Conceptual Appr oach 
that a collection of 1 s and 0 s defines a particular aircr aft, at least as regards 
the design variables being optimized. f139•140l 
Rather than starting with a single "baseline" design and trying to improve 
upon it, the genetic algorithm starts with a number of random colle ctions of 
1 s and 0 s defining some initial "popu lation" of designs. Those are analyzed 
and evaluated as to "fitness, " based on the measure (s) of merit, and the most 
fit are most likely to be permitted to "reprod uce. " Reproduction occurs 
by breaking apart genes and combining them random ly with other s. The 
"child" might be able to say, "I got my large engine from my father, and 
my area ruling from my mother. " The next generation is evaluated as to 
fitness, and the process continues until the population all resembl e each 
other. This is presumed to represent an optimum (but occasion ally it 
doesn't-t he subje ct of much research today) . 
A detailed overview of MDO methods and espe cially genetic algorithms 
as applied to aircraft concep tual design optimization can be found in 
Raymer. [141] This also includes a discussion of the variables and const raints 
most suitable and useful to aircraft conce ptual design proj ects and methods 
for automatically revising the vehicle geom etry to enhance realism of the 
optimization results. 
AUD Cost as the Measur e of Merit 
It has been assumed in the previous discussion that the measure of mer it 
for trade studies and optimization is the sized takeoff gross weight. In an 
actual design comp etition or sale, cost will probably be the final deciding criteria. Using weight as the measure of merit is usually a good appr oximation to 
minimizing acquisition cost because cost is so stro ngly driven by the weight 
(especially empty weight) for a given design approach. However, if you are 
doing trade studies of alternative technologies, engines, avionics, manufacturing methods, or similar items, then weight is a poor approximation to 
cost. Also, life- cycle cost is largely driven by fuel costs, which might not be 
minimized by finding the minimum weight airplane. A higher-aspec t-ratio 
wing is heavier but saves fuel. If you are designing a commer cial transport, 
the airlines will be more interested in their return on investment and even 
the net present value, as explained in Chapter 18. 
It is a fairly simple matter to use purchase price, fuel cost, ope rating cost, 
life-cycle cost, return on investment, or net present value as the meas ure of 
merit for carpet plots. Estimate the desired cost value for each parametric 
design variation from its sized empty weight, and use the cost rather than 
weight on the carpet plot. The same can be done with multivariable optimizers and even with MDO. 
Estim ating cost from changes in sized weight can be readily done with the 
DAPCA cost model described earlier, where empty weight is a key analysis 
input. Other costs items such as avionics acquisition will be insens itive to aircraft sized weight and must be estimated in some other manner. The fuel


<!-- p.733 -->

CHAPTER 19 Sizi ng and Trade Stu di es 731 
carried by the sized aircraft can be used to ratio fuel usage for operations 
costing. 
It is more difficult to use cost as estimated by the detailed WBS methods 
described in Chapter 18. The relationsh ip between sized aircraft weight and 
the number of hours to perform the various tasks is not clear or easy to 
define, and the number of inputs and assumptions overwhelms the optimization proce ss. For these reasons, most comp anies use DAPCA or an in-house 
equivalent for concep tual design trade studies and optimizat ions, then use a 
detailed WBS method for the final contract pricing. 
As was stressed in Chapters 2 and 3, a key part of the early conceptual 
design process is the desi gn of the requirements . The aircraft designers 
work with the intended customers to understand the requirements and to 
change them as required to provide the best combination of aircraft capabilities and cost. Sometimes, the cost part is clear. The customer simply doesn't 
have the ability to pay more than a certain amount. 
"Design-to- cost" is the term historica lly used to descr ibe a desi gn process 
wherein a cost target cannot be exceed-d. A more recent term, "cost as an 
independent variable," or CAIV, says it more strong ly: the plane has to 
cost "X"- now tell me what you can give me for that! 
CAIV forces early cost-based trade studies of requirements, technologies, 
and concepts. At its simplest, a CAIV study could involve a parametric variation of mission range, calculating sized takeoff weight and hence acquisition 
cost. From the cost the customer will pay, we can read off the range of the 
aircraft he or she can afford (Fig. 19.7). 
32000 
31000 
V> 
30000 Q] 
.0. 
QJ 29000 Vl 
"' 
.r: 
:= 
:::> 
28000 CL 
27000 
26000 300 400 500 
Range 
j. 
Fig. 19 .7 Cost-d riven range trade. 
600 700


<!-- p.734 -->

732 Aircr aft Desig n: A Con ceptu al Appr oach 
CAIV goes far beyond that, though, following throughout the desig n and 
development cycle and perme ating all design decisions. The cost impact of 
any change, whether to fix a problem or to add a new capabili ty, is assessed 
and used to bound the options. Management and the technical staff commit 
to keeping within the cost bounds and driving cost downwards at every 
chance. Finally, the customers commit to work with the contract ors to 
keep costs down rather than ass uming a traditional adversarial role. 
Hop efully you never run across the sort of customer who sets an ambitious set of firm design-to requiremen ts and then says, "and the plane has 
to cost no more than X." 
NASA X-Wi ng hybrid helic opter (NASA pho to) . 
What We've Lea rned 
Optimization is a cruci al part of aircraft design that can tell us how to make 
the Dash- Two better. Classical carpet plots are a useful tool, and modern 
MDO methods, with real-world const raints, are even better.
