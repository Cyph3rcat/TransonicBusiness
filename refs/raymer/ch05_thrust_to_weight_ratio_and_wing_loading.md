# Raymer Ch.5 - Thrust-to-Weight Ratio and Wing Loading

*Converted from `Daniel P. Raymer - Aircraft Design_ A Conceptual Approach (2018, American Institute of Aeronautics and Astronautics Inc.) - libgen.li.pdf` by `tools/pdf_to_md.py`. Page markers are printed page numbers.*


<!-- p.115 -->

Thrust-to-Weight 
Ratio and Wing 
Loading 
• Engi ne and wing sizes are set by ca lculat ed TOGW and selected values for T / wand W/' s. 
• T/Wa nd W/S have the greatest effect on air craft performance so that we ne ed 
good ini tial va lues before mak ing the first dr awing. 
• These ini tial va lues will be revised lat er by post -lay out ca rpet pl ots and other methods 
of optimizat ion. 
In trod uction 
T he thrus t-to-w eight ratio T /Wa nd the wing loading W/ S are the two 
most impor tant parameters affecting aircraft performance. Their 
optimization forms a major part of the analytical design activities 
conducted after the initial concept layout, but we need T /W and W / S estimates to make that first design. You can't draw the airplane if you don't 
know how big to draw the engine and the wing. 
Methods for defining initial values for T /W and W /S are presen ted in this 
chapter. If proper ly used, these should give results fairly close to the morecorrect values found later. If poor ly-chosen values are used for the first 
layout, the optimized aircraft might be so different that the design must be 
compl etely redone. 
For example, if the wing loading used for the initial layout is very low, 
the wing will be large. The desi gner will have no trouble finding room for 
the landing gear and fuel tanks. If later optimization gives a higher wing 
loading, the res ulting smaller wing may no longer hold the landing gear 
and fuel. They could be put in the fuselage but this would increase the 
wetted area and therefore the drag. The optimization results wouldn't 
apply to this revised design, so it's back to square one. 
115


<!-- p.116 -->

11 6 Air c raft De sign : A Concep tual Appr oa ch 
Wing loading and thrust-to-w eight ratio are close ly interconnected for 
most performance calculat ions. Consider takeoff distance, freque ntly a critical design driver. A requirement for a short takeoff can be met by using a 
large wing (low W/S) with a relatively small engine (low T/W). The small 
engine will cause the aircraft to accelerate slowly, but it only needs to 
reach a moder ate speed to lift off the ground. 
On the other hand, the same takeoff distance could be met with a small 
wing (high W/S) provided that a large engine (high T/W) is also used. In this 
case, the aircraft must reach a high speed to lift off, but the large engine can 
rapidly accel erate the aircraft to that speed. 
Because of this interconnection, it is unwise to rely upon purely historical 
values for bot h wing loading and thrust-to-w eight rat io. The most correct 
method of est imating them would be a simultaneous solu tion. This can be 
done comput ationally, or graphic ally using a method much like the carpet 
plots described in Chapter 19. Unfortunat ely, because we have not yet 
drawn the airplane, the estimates for the aerod ynamic and propulsion 
parameters needed for the various equations are not very accurate. The 
"garbage -in- garbage-ou t" phenomena might make the extra work of a simultaneous solution a waste of time. 
Another option, favored by this author, is to use a quick approximation 
of one of the parameters and then use that value to calcula te the other 
parameter from the performance requirements. This turns the simultaneous 
solution into a few closed-form equat ions. 
In many cases, the critical requirement for wing loading will be the stall 
speed during the approach for landing. Under FAR 23, smaller single- engine 
aircraft must stall at no more than 61 kt {113 km/h} . It is unlikely that any 
other requirement will force the wing to be larger, that is, impose a lower 
wing loading. Because stall speed is independent of engine size, the wing 
loading for such designs can be estimated based upon stall speed alone. The 
calculated wing loading can then be used to determine the T / W required to 
attain the other performance drivers such as takeoff distance or rate of climb. 
For other cases it is best to start with thrust-to-w eight ratio. T / W lends 
itself to a statistical approach being stro ngly correlated with veloc ity and 
also shows less variation within a given class of aircraft. Once an initial 
T / W is chosen, the wing loading W/ S can be direct ly calculated. This 
approach is assumed in the material that follow s. For a design where the 
wing loading can be determined just from the stall speed, do that first, and 
then solve for T /Wi n the equations that follow. 
Th rust-to-We igh t Ratio 
The thrust to weight ratio T / W dire ctly affects the performance of the 
aircraft. An aircraft with a higher T / W will acceler ate more quickly, climb


<!-- p.117 -->

CH APTE R 5 Thru st-to-We ight Ratio and Wing Loading 11 7 
more rapidly, reach a higher maximum speed, and sustain higher turn rates. 
On the other hand, the larger engines are heavier and will con sume more fuel 
throughout the mission, which will drive up the aircraft's takeoff gross weight 
to perform the design mission. 
When designers speak of an aircraft's thrust-to-w eight ratio, they generally refer to the T / W during sea-le vel static (zero-veloc ity), standard- day 
conditions at design takeoff weight and maximum throttle setting. This 
includes afterburner on, if there is one. 
Table 5.1 provides typical values for T / W for jet aircraft. Interest ingly, 
there is a wide variation for commercial transports . The higher values are 
for two-engine airplanes, the lower for four- engine airplanes. This makes 
sense-if you lose an engine on takeoff, you need enough thrust to safely 
climb away. If there is only one engine remaining, it needs a lot of thrust. 
With one engine out, all of the transpor ts have a T / W of around 0.2. 
At takeoff weights, a modern fighter plane approaches a T/W of 1. 0, 
implying that the thrust is nearly equal to the weight. At com bat conditions 
when some fuel has been burned off, these aircraft have T / W values exceeding 1. 0 and are capable of acc elerati ng to supersonic speeds while going 
straight up! 
It is impor tant to avoid con fusing the takeoff T / W with the T / W at 
other con ditions in the following calcu latio ns. During the flight, the 
weight drops as fuel is burned off. The thrust changes at different speeds, 
altitudes, and throttle settings. When a required T / W is calc ulated at 
some flight condition, it must be adjusted back to the original takeoff conditions so that it can be com pared to other required values of T / W and 
ultimately used to define the required engine si-e. These T/W adjustments 
will be discussed later. 
#f !J Props and Powe r Loading 
For an airplane powered by a prope ller, the prop makes thrust so the 
methods for estimating the required T/W can be equally applied. 
However, the engine companies for such airplanes don't sell "thrust, " they 
sell "power." When sele cting the approp riate engine, it is useful to consider 
Table 5. 1 Thrust-to-We igh t Ratio (T /W )* 
Air craft Type 
Jet train er 
Jet fighter (dogf ig hter ) 
Jet fighter (other ) 
Mil ita ry cargo /bomber 
Jet trans port (higher value for fewer engi nes) 
Typical Insta ll ed T / w 
0.4 
0.9 
0.6 
0.25 
0. 25-0 .4 
*In mks units. the th rust force is found as T/Wt im es mass time s g = 9.807.


<!-- p.118 -->

11 8 Airc raft Des ign: A Conceptual Appr oach 
a parameter based upon power, not thrust. While it might make sense to 
define a power-to -weight ratio P/ W as the equivalent to T/W, this is not 
the usual practice. 
For propeller-po wered aircraft, the classica l term to define engine size 
has been a ratio called "power loading." Power loading is the weight of 
the aircraft divided by its engine power W / P, so that it is the inverse of 
the power-to-w eight rati o. It is common early in the design development 
of propeller-po wered airplanes to select a desired power loading based on 
history and experience, and use it to select an engine. 
Power loading has an opposite connot ation from T / W Confusing ly, a 
high power loading indicates a small engine. Power loadings typically range 
from 10-15 lb per horsep ower. An aerobatic aircraft can have a power 
loading of about six. * A few have been built with power loadings as low as 
three including the Pitts Sampson, a one-of -a-k ind airshow performer. 
A propeller- powered aircraft produces thrust via the propeller. The prop 
has an efficiency Y/p defined as the thrust power produced by the propeller 
(thrust times velocity) divided by the actual power provided by the engine. 
Based on this, thrust is calculated as power times prop efficienc y, divided 
by veloc ity. Dividing by weight gives an expression for T / W for propellerpowered aircraft as follows: 
- = (-) (-) = (55-YJp) (-) {fps} (5.1) 
The 550 term in the right-hand version of the equation is a conversion 
factor that must be applied when units of horsepo wer are used. 
Note that this equation includes the term P / W, the power- to-weight ratio 
that is the inverse of power loading W/hp. To avoid confusion when discussing requirements affecting both jet- and propeller-p owered aircraft, 
this book often refers to the power-to -weight ratio rather than power 
loading. Also, to avoid excessi ve verbiage the term "thru st-to-w eight ratio" 
should be understood to apply to propeller-po wered aircraft as well. 
Table 5.2 provides typical values for P/ W for propeller aircraft. It 
also provides the reciproca l values, power loadings, in pounds per horsepower. These values are all at maximum power settings at sea-le vel static 
conditions. 
The metric equivalents in this table are actu ally given as power divided 
by mass (watts per gram). As explained in the Author's Note, a "weight" 
given as kg must be converted to force (Newtons) by multiplying by 
g(= 9. 807 m/s 2). Divide P/ W in watts per gram by 9.807 before using in 
equatio ns. Since Newtons are defined using kg, the resulting value has 
units of kW /N. 
*Power loading is a designer's measure of merit from the earliest days of aviation, historically 
defined in British Imperial units of pounds-per- horsepower and still commonly used that way even 
by otherwise-metric engineers. Multiply it by 1.6 44 to get units of kg/kW.


<!-- p.119 -->

CHAPTER 5 Thru st-to-Weight Ratio and Wing Loading 11 9 
Table 5.2 Power-to-We igh t Ratio (P/W) 
Aircraft Type 
Powered sailplane 
Homebu ilt 
Gener al aviation- single engine 
Gener al aviatio n-twin engine 
Agricultur al 
Twin tur boprop 
Flyin g boat 
I I 
hp/lb {Watt /g} 
0.0 4 {0 .07} 
0.0 8 {0 . 13 } 
O.Q7 {0. 12 } 
0. 17 {0 .3} 
0.09 {0 . 15 } 
0.20 {0 .33} 
0. 10 {0 . 16 } 
Note. Divide Watt/g by 9.8 07 before using in ca lculations. 
I t •I 
I It I 
25 
12 
14 
6 
11 
5 
10 
#f D Statis tica l Esti mation of T/ wa nd Powe r Load ing 
If you want your car, or your moto rcycle, or even your airplane to go 
faster, most of us know what to do. 'Buy a bigger engine. This obvious 
relationship can be seen on any plot of aircraft maximum vel ocity vs T / W 
or P/ W. 
Tables 5.3 and 5.4 provide statistical equations based upon maximum 
Mach number or velocity for different classes of aircraft. They are of exponential form, being a constant term times the independent variable (speed) 
raised to a given power. Such equations represent a straight line on log-log 
graph paper. As discussed in Chapter 15, many parameters of interest to 
aircraft designers will fit nicely to this form of equation. 
These equations were developed by the author using data from [6] and 
should be considered valid only within the normal range of maximum 
speeds for each aircraft class. For most airplanes they can be used as a 
credible first estimate for T / W or P / W 
Af JI Th rust Match ing 
A simple calculation of the required T / W during cruise can be done with 
a method called "thrust matchi ng." This comp ares the thrust available during 
Table 5.3 T /Wo vs Mmax 
T/Wo = a M-ax -Jet train er 0. 488 0.7 28 
Jet fig hter ( dogfig hter) 0.648 0.5 94 
Jet fig hter (other ) 0.514 0. 14 1 
Mil itar y cargo /bomber 0.2 44 0.341 
Jet tra nspor t 0.2 67 0.3 63


<!-- p.120 -->

12 0 Ai rcraf t De sign: A Concep tu al Approach 
Table 5.4 P/ W0 vs Vmax kt or {km/h} 
P/ Wo == a-ax= hp/l b{Watt/g} a 
Sailpla ne-powered 0.0 43 {0.07 1 } 
Homebu il t-metal /wood 0.0 05 {0.0 06} 
Homebui lt-com posite 0.0 04 {0.0 05} 
General aviation-s ingle eng ine 0.025 {0.0 36} 
General aviatio n-twin engine 0.0 36 {0.0 48} 
Agricultural ai rcraft 0. 009 {0 .01 O} 
Twin turboprop 0.01 3 {0 .01 6} 
Flying boat 0.0 30 {0.0 43} 
Note.· Divide Watt/g by 9.807 before using in ca lculations. 
0 
0.57 
0.57 
0.22 
0.32 
0.50 
0.5 0 
0.23 
cruise to the estimated aircraft drag. In level unacceler ating flight, the thrust 
must equal the drag. Likewise, the weight must equal the lift (assuming 
that the thrust is aligned with the flight path) . Combining these relat ionships 
indicates that the T/W must equal the inverse of L/ D [Eq. (5.2 )] : 
(-)cruise= ( L / D -cruise 
(5.2) 
L / D can be estimated in a variety of ways including the detailed methods 
discussed in Chapter 12. For the initial estimation of T / W, the method for 
L / D estimation presented in Chapter 3 is adequate. 
Reca ll that this procedure for L / D estimation uses the selected aspect 
ratio and an estimated wetted-a rea ratio (Fig. 3.6) to determine the wetted 
aspect ratio. Figure 3.5 is then used to estimate the maximum L/D. For 
propeller aircra ft, the cruise L / D is the same as the maximum L / D. For jet 
aircraft, the cruise L / D is 86.6% of the maximum L / D. 
This simple method assumes that the aircraft is cruising at approxima tely 
the optimum altitude for the as-yet- unkn own wing loading. It would be 
invalid if the aircraft were forced by the mission requirements to cruise 
at some other altitude such as sea level. The better methods of estimating 
L / D as described later do not have this restrict ion. 
Thrust-to -weight ratio is often determined by a climb requirement rather 
than by cruise conditio ns. This leads to a common problem. The T / W for 
climb can be so large that the engines must be throttl ed way back during 
cruise, and an aircraft engine running at only a fraction of its available power 
during cruise is us ually very inefficient. This is espec ially true for jet engines. 
T / W for a climb requirement can be found from a small adjus tment to 
Eq. (5.2). As derived in Chapter 17, the T/Wfo r climb is the T/Wfo r level 
flight, plus the extra thrust required for the climb gradient, leading to 
Eq. (5.3). The aircraft's vertical velocity during the climb is usua lly specified 
in the design requireme nts or in military or civilian speci fications (see


<!-- p.121 -->

CHAP TER 5 Thru st-to-We igh t Ratio and Wing Loading 12 1 
Appendix F, Table F.2) . Note that the L/ D for climb might be lower than the 
L/ D during cruising flight, especia lly during initial climb when the gear and 
flaps might still be down. 
( T ) 1 Vvertical 
W climb= (L/D)climb + V (5.3) 
One might wonder why the calculation for cruise T /Wi s ever performed. 
Surely if an airplane has enough thrust to climb to a certain altitu de, it has 
enough thrust to cruise there! The reason is simple: most aircraft engines 
cannot be run at maximum power for a long time. The pilot can select 
maximum power for takeoff and climb, but must throttle back to 
"maximum continuous power" for cruising flight. Is it enough? 
There are other criteria that can set the thrus t-to -weight ratio, such as 
takeoff distance and turning performa nce. These are described in the 
next section. 
For initial layout the T / W should be selected as the higher of either the 
statistical value obtained from the appropri ate equation in Tables 5.3 and 
5.4, or the value obtained from the thrust matching as ju st described. The 
calculated T / W values must be adjusted to a consi stent conditi on. This is 
discussed next. 
Af JJ Ratio Resu lts to Takeoff Conditions 
As mentioned above, during the flight the aircraft weight and engine 
thrust will change . A T / W value calculated .at one cond ition such as 
takeoff cannot be direct ly compa red to a T / W calculated during , say, 
cruise. We normally adjust all calculated values of T / W back to the original 
takeoff conditions for compari son. This is done by simple rat ios. 
For example, the thrust-to -weight ratio estimated using Eq. (5.2) is at 
cruise cond itions, not takeoff. The aircraft will have burned off part of its 
fuel before beginning the cruise and will burn off more as the cruise progresses. The airplane weighs less. 
Also, the thrust of the selected engine will be different at the cruise conditions than at sea-le vel, static con ditions . These factors must be con sidered 
to arrive at the required takeoff T / W, used to size the engine. 
During cruise the highest aircraft weight, and hence the worst T / W, 
occurs at the beginning of the crui se. The weight at the beginning of the 
cruise can be found by multip lying together all of the mission- segment 
weight fractions prior to cruise. For the example in Chapter 3, Table 3.2 
gives mission weight fractions for takeoff and climb of 0.970 and 0.985, 
or 0.956 when multip lied together. Multipl ying this value times the cruise 
T / W will ratio the weight back to takeoff conditions, but the thrust change 
must also be considered. 
This is done by finding the ratio between the actual thrust at that flight 
condition (cruise in our example) and the sea-le vel static maximum thrust.


<!-- p.122 -->

12 2 Air c raf t Desig n: A Concep tu al Approach 
Hop efully engine data are available so that the actual values can be used. 
If not, they can be approximated. 
Typic ally, a subsonic, high-by pass-r atio turbofan for a transport aircraft 
will have a cruise thrust of 20-25% of the takeoff thrust, while a low- bypass 
afterburning turbofan or turboj et will have a cruise thrust of 40- 70% of the 
takeoff maximum value (see Fig. 5.1). Appendix E provides thrust and fuel 
cons umption data for several represent ative engines. 
When a prop is being used, the thrust created by that prop must be 
calc ulated for both flight conditions taking into acc ount the engine power 
variati ons and the thrust effects of veloc ity and propeller efficien cy. 
For a piston engine the power varies with the dens ity of the air provided 
to the intake manifold. If the engine is not superc harged, then the power falls 
off with incr easing altitude approxima tely to the dens ity ratio CT. For example, 
an unsupe rcharged engine at 10,000 ft {3,0 48 m} will have about 73% of its 
sea-le vel power. 
To prevent this power decr ease, many piston engines use a superc harger 
to maintain the air provided to the manifold at essentially sea-le vel dens ity up 
to the com pression limit of the superc harger. Above this altitu de, the power 
begins to drop off (see Fig. 5.2). 
If possible, manufacturer's data for power vs altitude should be obtained. 
Piston-po wered aircraft typic ally cruise at about 75% of takeoff power. 
(ft) (m) 
40,000 12,500 
10,0 00 
30,000 
(]) 7500 
"O 
3 
·.;::; 20,000 <i'. 
5000 
10 ,000 
2500 
0 
0 
Typical current-gen eration engi nes 
High BPR 
turbofan 
0.1 0.2 
at Mach = 0.8 
0.3 0.4 
T max dry cruise 
T max takeoff (SLS) 
0.5 
Fig. 5.1 Thrus t lapse at cru ise. 
Low BPR 
afterburning turbofan 
0.6 0.7


<!-- p.123 -->

QI 
"'tJ 
::l 
+-' 
·;:; 
;;; 
::l 
V1 
V1 
QI 
(ft) 
20,000 
15 ,000 
10 ,000 
5000 
(m) 
5000 
2500 
CHAP TER 5 Thru st-to-We ight Ratio and Wing Loading 12 3 
T0-360 
(Turbo charged) 
50 
0 -----------,--'----->, -LL..--(kW) 
(hp) 0 50 100 150 200 
Power 
Fig. 5.2 Piston engine power variation with al titude. 
250 
For a turbine-po wered, propeller-dr iven (turboprop) aircraft, the power 
available increases somewhat with increasing speed, but the thrust drops 
off anyway due to the veloc ity effect on the propeller [Eq. (5 .1)] . 
With a turboprop, there is an additiona l, residua l thrust contribution 
from the turbine exhaust. It is custo mary to convert this thrust to its horsepower equivalent and add it to the actual horsep ower, creating an "equi valent 
shaft horsep ower" (esh p). For a typical turboprop engine installati on, the 
cruise eshp is about 60-80% of the takeoff value. 
The required T / W can then be adju sted from cruise to takeoff cond itions 
using Eq. (5. 4). Note that the takeoff thrust value is in the numerator, not in 
the denomina tor as was the case for the weight adjustment. After adjustment, 
the higher value of T / W is selected from statistical and thrust matching 
calculations and used for engine sizing. For a propell er-po wered aircr aft 
the required P/W can be found from this result by solving in Eq. (5. 1). 
( T) ( T) ( Wcruise) (Ttakeoff) (5.4 ) W takeoff= W cruise Wtakeoff Tcruise 
EJ Wing Load in g 
MUI w;s Overvie w 
The wing loading W / S is the weight of the aircraft divided by the area of 
the reference wing. Wing loading affects stall speed, climb rate, takeoff and


<!-- p.124 -->

12 4 Air craft Design : A Con ceptua l Appr oach 
landing distances, and turn performance. The wing loading determines the 
design lift coefficient and impacts drag through its effect upon wetted area 
and wing span. 
Wing loading has a big effect upon sized aircraft takeoff gross weight. 
This is another "backwar ds" parameter-if the wing loading is reduced, the 
wing is larger. This usually improves performance, but the additional drag 
and empty weight due to the larger wing will increase the takeoff gross 
weight to perform the mission. The leverage effect of the sizing equation 
will require a more-t han-propor tional weight increase when factors such 
as drag and empty weight are increased. Table 5.5 provides represe ntative 
wing loadings. 
Recall that the reference wing used for W / S is the simplified trapezoida l 
shape that extends all of the way to the aircraft centerline, including the portions covered by the fuselage. When proper ly calcula ting the lift (Chapter 12), 
this area must be adju sted using the "exposed" wing area, which is the actual 
planform area of the wing after removal of the portions covered by the fuselage. For W / S, though, the reference area is used. 
For performance calculations the weight term in W / S must be the actual 
weight of the aircraft at that time. When calculating performance for a known 
aircraft weight, the wing loading is reduced from the takeoff value to take into 
account the fuel that has been burned by that time. 
However, when solving for the required W / S at various points in the 
mission, the answer will be wing loading at the actual weight at that time. 
For compa rison purposes when sele cting the aircraft's wing loading, all 
W / S values must be converted to an equivalent condition, namely, takeoff 
weight. Therefore, the calculated W / S values must be ratioed up to the 
takeoff value. This is easily confused. This adjustment is made by multip lying W / S times a ratio found by multipl ying toget her the mission- segment 
weight fractions. 
Table 5.5 Wing Loading* 
-B·i!J·11¢tmilrHis torical Trends 
Sa il plane 6 {30} 
Homebu ilt 11 {54} 
Gener al aviation- single engine 17 {83} 
Gener al aviation -twin eng ine 26 { 12 7} 
Twin turbopr op 40 {1 95} 
Jet trai ner 50 {244} 
Jet fig hter 70 {342} 
Jet transpor t/bom ber 12 0 {586 } 
*In mks un its, mul tiply metric value s ti mes g = 9.807 to use in equations.


<!-- p.125 -->

CHAP TE R 5 Thru st-to-W eigh t Ratio and Wing Loading 12 5 
Ultimately the wing loading and the thrust-to -weight ratio must be optimized together. Such optimization methods are presented in Chapter 19 
using aerodynamic, weight, and propu lsion data calculated from the initial 
design layout. The remainder of this chapter provides methods for initially 
estimating the wing loading to meet various requirements. These allow the 
designer to begin the layout with some assurance that the design will not 
require a comp lete revision after the initial aircraft layout is completed 
and analyzed. 
This material genera lly assumes that an initial estimate of T / W has been 
made using the methods presented in the last section. Most of the equations 
could be solved for T / W if the wing loading is defined by some extreme 
requirement such as a low stall speed. 
These methods estimate the wing loading required for various performance condit ions. To ensure that the wing provides enough lift in all circumstances, the designer should select the lowest of the estimated wing loadings. 
If an unreaso nably low wing loading value is driven by only one of these 
performance conditions, the designer should consider another way to meet 
that condition . 
For example, if the wing loading required to meet a stall speed requir ement is well below all other requirements, it might be better to equip the 
aircraft with a high-lift flap system. If takeoff distance or- rate of climb 
requires a very low wing loading, perhaps the thrust-to -weight ratio should 
be increased. 
Ajf J Stall Speed 
The stall speed of an aircraft is directly determined by the wing loading 
and the maximum lift coefficient. Stall speed is a major contributor to 
flying safety, with a substantial number of fatal accidents each year due to 
"failure to maintain flying speed." Also, the approach speed, which is the 
most impor tant factor in landing distance and also contributes to posttouchdown accidents, is defined by the stall speed. 
Civil and military design speci fications establish maximum allowable stall 
speeds for various classes of aircraft. In some cases the stall speed is explici tly 
stated. FAR 23 says that certified aircraft under 12,500 lb TOGW {5 ,670 kg} 
must stall at no more than 61 kt {113 km/h} unless they are multi -engined 
and meet certain climb requirements (see Appen dix F). While not stated in 
any design spe cifications, a stall speed of about 50 kt would be cons idered 
the upper limit for a civilian trainer or other aircraft to be operated by 
low-time pilots. 
Sometimes the stall speed is indire ctly set from the required approach 
speed. This must be a certain multiple of the stall speed to give a factor of 
safety in case of rearward gust or wind shear. For civil applic ations, the 
approach speed must be at least 1.3 times the stall speed. For military 
applications, the multiple must be at least 1. 2. Appr oach speed might be


<!-- p.126 -->

12 6 Air cr aft De sign : A Concept ual Approach 
explicit ly stated in the design requirements, or it might be selected based 
upon previous aircraft. Then the required stall speed is found by division 
by 1. 3 or 1. 2. 
The wing loading required to meet a certain stall speed requirement 
can be found from the simple fact that lift must equal weight. Equa tion 
(5.5) expands this out, noting that at the stall speed the aircraft is at 
maximum lift coefficient. Dividing both sides by wing area S gives Eq. (5.6) 
the required wing loading to attain a given stall speed with a certain 
maximum lift coefficient. 
(5 .5) 
1 2 w Is = 2 p vstall c Lmax (5.6 ) 
In this equation the air density p is typically the sea-le vel standard value of 
0.00238 slugs/ft 3 {l. 23 kg/m3}. Sometimes the 5000-ft-a ltitude {1 524 m} 
hot- day value of 0.0 0189 {0.97 4} is used to ensure that the airplane can be 
flown into Denver during summer. 
The remaining unkno wn, the maximum lift coefficient, is very impor tant 
to aircraft design. It often sets the wing size, but can be very difficult to estimate. Maximum lift coef ficient depends upon the wing geomet ry, airfoil 
shape, flap geom etry and span, leading-edge slot or slat geomet ry, Reynolds 
number, surface texture, and interfer ence from other parts of the aircraft 
such as the fuselage, nacelles, or pylons. The trim force provided by the horizontal tail will increase or reduce the maximum lift, depending upon the 
direction of the trim force. If the propwash or jetwash impinges upon the 
wing or the flaps, it will also have a major influence upon maximum lift 
during power-on cond itions. 
Below are a few quick methods for its estimat ion. Better methods are 
given in Chapter 12 , but the "real" answer takes a lot of work by a competent 
aerod ynamics staff. Methods include comp utational fluid dynamics, historical comparisons, wind-tunnel test, and a bit of edu cated guess work, but you 
are never sur e of the maximum lift coefficient until the airplane flies. If the 
airplane stalls at the speed you predicted, your estimate was good. If not, 
fix it-a common occur rence. 
Typical maximum lift coefficient values range from about 1. 2 to 1.5 for a 
plain wing with no flaps to as much as 5.0 for a wing with large flaps 
immersed in the propwash or jetwash. For a wing of fairly high aspect ratio 
(over about 5), the no-f laps maximum lift coefficient will be approxim ately 
90% of the airfoil maximum lift coefficient (see Appe ndix D for typical 
values) . If the wing is swept, maximum lift is reduced by the cosine of the 
sweep angle [Eq. (5.7 )]. 
Cr = 0.9 Cn cos Ao 25c max -tmax · (5.7 )


<!-- p.127 -->

CHA PTE R 5 Thrus t-to-We ight Ratio and Wing Load ing 12 7 
"Normal" aircraft with flaps on the inner part of the wing will reach a lift 
coefficient of about 1. 6-2.0. A commerc ial transport aircraft with flaps and 
slats (leading-edge flaps with slots to improve airflow) might see a 
maximum lift coefficient of about 2.4. The maximum lift coeffi cient for an 
aircraft designed with huge flaps, slots, and other tricks used for short 
takeoff and landing (STOL) applications can reach around 3.0. 
Figure 5.3 provides maximum-lift trends vs sweep angle for several 
classes of aircraft. This old Boeing chart approximates the maximum lift 
fairly well if the wing flaps are designed the way Boeing would do it-whatever that means! As a first estimate done before the aircraft layout is done, it 
is not too bad. A better method in Chapter 12 takes into account your 
design's flap geomet ry. 
Most aircraft use different flap settings for takeoff and landing. During 
landing the flaps will be deployed the maximum amount to provide the 
greatest lift and drag. However, for takeoff the maximum flap angle would 
probably cause more drag than desirable for rapid accelerat ion and climb, 
so the flaps will be depl oyed to only about half the maximum angle. This 
typically results in a takeoff maximum lift coefficient that is about 80% that 
of the landing value. Gen eral aviation aircraft often take off without any 
flaps, so the takeoff maximum lift coefficient is the easily calculated "clean 
wing" value. 
4.0 
e cJ 2.0 
1.0 
Wings of moderate aspecfratio (4-8) 
Triple slotted flap and slat Double slotted flap and slat 
Flower flap Slotted flap Plain flap No flap 
Double slotted flap 
0 ------------------------0 10 20 30 
Sweep Ae,14 
40 
Fig. 5.3 Maxi mum li ft coefficient. 
50 60


<!-- p.128 -->

12 8 Air cr aft Desig n: A Conceptual Approach 
*#fl Takeoff Dis tance 
Be careful when somebod y says "the takeoff distance is .... " There are 
actually three very different numbers that are referred to as takeoff distance. 
The "ground roll" is the actual distance traveled before the wheels leave the 
ground. But what if there is a tree at the end of the runway? 
The "ob stacle clearance distance" is the distance required from brake 
release until the aircraft has reached some speci fied altitude. This is usually 
50 ft {15. 24 m} for militar y and most civil aircraft, but only 35 ft {10 .7 m} 
for jet com mercial aircraft. 
The (possi bly apocr yphal) reason offered for the 50-ft obstacle is that it 
was the height of a tree at the end of an early Army Air Corps base in 
Texas. The tree is long gone, but the requirement remains. The 35-ft requirement for jet com mercial aircraft was apparently negotiated in the early days 
of jet transpor ts because they simply couldn't meet the 50-ft requirement 
without a substantial pena lty. 
Norma lly the liftoff speed for takeoff ground roll or obstacle clearance 
distance is 1.1 times the stall speed. This provides a margin of safety for 
sudden gusts and ensures adequate flow over the control surfaces. 
The "balanced field leng th" (BFL) is the leng th of the airfield required for 
safety in the event of an engine failure at the worst possible time in a multiengine aircraft. When the aircraft has ju st begun its ground roll, the pilot 
would have no trouble stopping it safely if one engine were to fail. As the 
speed increases, more distance would be required to stop after an engine 
failure. If the aircraft is near ly at liftoff speed and an engine fails, the pilot 
would be unable to stop safely and instead would continue the takeoff on 
the remaining engines. 
The speed at which the distance to stop after an engine failure exactly 
equals the distance to continue the takeoff on the remaining engines is 
called the "decision speed." The balanced field length is the length required 
to take off and clear the specified obstacle when one engine fails exactly at 
decision speed. Note that use of reversed thrust is not permitted for calculation of balanced field length. 
The Federal Aviation Administration specifies a field leng th requirement 
for FAR 25 certified aircraft called "FAR takeoff field lengt h." This has a 35-ft 
{10 .7-m} obstacle clearance requirement and requires that the aircraft meet 
the worst of either balanced field length as just described, or a value of 15 % 
greater than the all-engines -op erating obstacle clearance takeoff dista nce. 
FAR 23 certified aircraft are not required to meet a balanced field length 
requirement. See Appen dix F for more information about FAR requiremen ts 
or obtain the full FARs (available online ). 
For military aircraft the balanced field length retains the 50-ft {15 .24-m} 
obstacle clearance requirement. 
Both the wing loading and the thrust-to-w eight ratio contribute to the 
takeoff distance. The following equations assume that the thrust-to -weight


<!-- p.129 -->

CHAPTE R 5 Thru st-to-We igh t Ratio and Wing Loading 12 9 
ratio has been selected and can be used to determine the required wing 
loading to attain some required takeoff distan ce. However, the equations 
could be solved for T / W if the wing loading is known. 
Other factors contributing to the takeoff distance are the aircraft's aero dynamic drag and rolling resista nce. Aerod ynamic drag on the ground 
depends largely upon pilot techniq ue. For example, if the pilot rotates (lifts 
the nose) too early, the extra drag can prevent the aircraft from accelerating 
to takeoff speed. This was a frequent cause of acciden ts in early jets, which 
were underpowered by today's standar ds. 
The aircraft's rolling resistance µ, is determined by the type of runway 
surface and by the type, number, inflation pressure, and arrangement of 
the tires . A thin, high-pressur e tire oper ated over a soft dirt runway will 
have so much rolling resistance that the aircraft might be unable to move. 
A large, low-pressure tire can oper ate over a softer runway surface but will 
have more aerodynamic drag if not retracted, or will take up more room if 
retracted. Values of µ, for different runway surfaces are provided in the 
detailed takeoff analysis in Chapter 17. , 
In later stages of analysis, the takeoff distance will be calculated by integrating the accelerations throughout the takeoff, cons idering the variat ions in 
thrust, rolling resistance, weight, drag, and lift. For initial estimation of the 
required wing loa ding, a statistical approach for estimation of takeoff distance can be used. 
Figure 5.4, based upon data from, [13 ,i4] perm its estimation of the takeoff 
ground roll, takeoff distance to clear a 50-ft {15 .24-m} obstacle, and FAR or 
balanced field length over a 35-ft {1 0.7 -m} obs-acle. For a military multiengined aircraft, the balanced field length over a 50-ft {15. 24-m} obstacle is 
approximately 5% greater than the FAR 35-ft {10 .7-m} clearance balanced 
field value. 
Note that a twin-en gine aircraft has a greater balanced field length than a 
three- or four- engine aircraft with the same total thrust. This occurs because 
the twin-en gine aircraft loses half of its thrust from a single engine failure, 
whereas the three- and four-en gine aircraft lose a smaller percen tage of 
their total thrust from a single engine failure. Because of this, we usually 
design twin- engine aircraft with a higher total T/W 
The takeoff parameter (TOP) of Fig. 5.4 is the takeoff wing loading 
divided by the product of the densi ty ratio <r, takeoff lift coefficie nt, and 
takeoff thrust-to-w eight (or power-to -weight) ratio . The dens ity ratio is 
simply the air density p at the takeoff altitude divided by the sea- level dens ity. 
For the jet and propeller lines, the takeoff lift coefficient is the actual 
lift coefficient at takeoff, not the maximum lift. The aircraft takes off at 
about 1.1 times the stall speed so that the takeoff lift coefficient is the 
maximum takeoff lift coefficient divided by 1.21 (1.1 squared) . However, 
takeoff (and landing) lift coefficient can also be limited by the maximum 
tail-down angle permitted by the landing gear (typically not more than 
15 deg) .


<!-- p.130 -->

13 0 Ai rcraf t Des ign: A Conceptual Appr oach 
2 
0 
::: 
Q) u 
c 
2 
.!!! 
-0 
ti:: 
0 
Q) ..:£ 
12 
11 
10 
9 
8 
7 
6 
5 
4 
3 
2 
1 
0 
0 
FAR ta keoff 
100 200 300 400 500 
Takeoffparameter: WIS or __ w:_;s __ 
<JCLrn T/W <JCLrn BHP/W 
Fig. 5.4 Takeoff dis tance esti mation (fps un its) . 
600 
For the FAR takeoff lines, the takeoff lift coefficient is the maximum lift 
coefficient at takeoff cond itions as used for stall calcula tion. 
To determine the required wing loading to meet a given takeoff distance requirem ent, the takeoff parameter is obtained from Fig. 5.4. Then 
the following expressions give the maximum allowable wing loading for 
the given takeoff distan ce: 
Prop: 
(W/S) = (TOP) uCrrn(hp/W) (5.8 ) 
Jet: 
(W/S) = (TOP) uCrrn(T/W) (5.9 ) 
*#fl Catapul t Takeoff 
"Real" naval aircraft must be capable of oper ation from an aircraft carrier. 
While some early aircraft simply flew off the carrier's flat deck, this was 
dangerous and inapprop riate for larger aircraft with longer takeoff distan ces. 
Early catap ults used compressed air, hydraulic pistons, rockets, or even


<!-- p.131 -->

CHAPTER 5 Thrus t-to-We ight Ratio and Wing Load ing 131 
explosive charges, with varying success. In the period right after WWII, the 
modern steam catapult was devel oped. 
Steam-ope rated catapults are reliable and provide a smooth and predictable accele ratio n. They produce a force on the aircraft depend ing on 
the steam pressure used, which is adjustable just before launch to avoid 
over-acceler ating a lightweight aircraft. At the limit of aircraft weight, a 
lighter aircraft can be accelerated to a higher speed by the catapult than 
a heavier one. Figure 5.5 dep icts the velocities attainable as a function of 
aircraft weight for three catap ults in use by the U.S. Navy. 
For a catapult takeoff, the airspeed as the aircraft leaves the catapult must 
exceed the stall speed by 10%. Airspeed is the sum of the catapult end speed 
Vend and the wind-o ver- deck of the carrier V wod' plus the veloc ity added by 
the engine's thrust, typically 3-10 kt, or 5-18 km/h. 
For aircraft launch operations the carrier will be turned into the wind, 
which will produce a wind-ov er- deck on the order of 20-4 0 kt. However, 
the design spe cifications for a Navy aircraft freque ntly require launch capabilities with zero wind-ov er- deck or even a negative value, to enable aircraft 
launch while at anchor. Once the end . speed is known, the maximum wing 
loading is defined by 
(W) 1 ( V: V: Li V. ) 2 (Crrn.Jtakeoff 
S = 2 P end + wod + thrust l 21 takeoff 
· 
(5. 10) 
where p = 0.002 19 slug/ft 3 {1.13 kg/m3} tropic-! day. 
Vl ..., 
0 
c 
-0 
Q) 
Q) 
Q. 
V\ 
-0 
c 
Q) 
..., 
:::J 
Q. 
"' 
u 
150 
100 
50 
Catapult type C-1 1 C-7 C-13 
l 
0 -----------------------0 20 40 60 
Maximum TOGW (103 lb) 
Fig. 5.5 Cata pult end spee ds. 
80 100


<!-- p.132 -->

13 2 Ai rcr aft Design: A Concept ual Ap proach 
Some times the takeoff stall margin in this equation is defined not as a 
veloci ty margin of 10 %, but as a lift coefficient margin of 15%. This action 
changes the 1.21 term to a value of 1.18. 
A new system has been in development for some years as an alternative to 
steam catapults, called Ele ctroMagnetic Aircraft Launch System (EMALS ). 
This uses a linear induction motor to acceler ate the aircraft. Benefits 
include reduced stress on the airplane due to more consistent acceleration, 
lower system weight, and purpor tedly reduced maintenance and total 
system cost. It also uses far less fresh water than a steam system, reducing 
des alination demands placed upon the ship. 
A subtle advantage is that the EMALS can be "dialed down" to accommodate small UAVs, ever-more impor tant for Naval aviation. Traditional steam 
catapults cannot do this, and their launch force would tear such VA Vs apart. 
EMALS uses more ele ctric ity than even a nuclear aircraft carrier can 
provide, so the system must store ener gy before use. Current designs use 
rotating disk alternators for this storage, charging them in about 45 seconds. 
EMALS has had sub stantial developme ntal problems and cost overruns, 
but recent sea trials seem to have been successful. It is used exclusi vely in the 
new Ford- class aircraft carriers, of which one has been commissioned 
(the Gerald Ford) and three more are authorized. Retrofitting EMALS to 
the more-num erous Nimit z-c lass carriers was proposed but rejected, so 
steam launch will be continue to be used for the foreseeable future. 
The EMALS designed for the Ford-class carriers can launch even heavier 
aircraft than legacy steam catapults, so the graphs above can be used to set an 
upper limit on aircraft design characterist ics. 
*HJ La nding Di stance 
There are a number of different values referred to as the "landing dista nce." 
"Landing ground roll" is the actual distance the aircraft travels from the time 
the wheels first touch to the time the aircraft comes to a complete stop. 
The "FAR 23 landing field length" includes clearing a 50-ft {15 .24-m} 
obstacle while the aircraft is still at approach speed and on the approach 
glidep ath (nor mally 3 deg) . After crossing the obstacle, the pilot slows the 
aircraft to the touchdown speed of typically 1.15 times the stall speed. The 
obsta cle-cle arance distance roughly doubles the ground- roll distance alone. 
The "FAR 25 landing field leng th" includes the 50-ft {15 .24-m} obstacle 
clearance at approach speed and also adds an arbit rary two-thirds to the 
total distance to allow a safety margin. The landing distance definition for 
military aircraft is norma lly specified in a request for proposal (RFP), but 
typically resembles the FAR 23 definit ion. 
Landing distance is largely determined by wing lo ading. Wing loading 
affects the approach speed, which must be a certain multiple of stall speed 
(1.3 for civil aircraft, 1.2 for milit ary aircraft) . Approach speed determines 
the touchdown speed, which in turn defines the kinetic energy that must


<!-- p.133 -->

CHAPTER 5 Thru st-to-We ight Ratio and Wing Loading 13 3 
be dissipated to bring the aircraft to a halt. The kinetic energy, and hence the 
stopping distance, varies as the square of the touch down speed. 
In fact, a reasonable first guess of the total landing distance in feet, including obstacle clearance, is approximately 0.3 times the square of the approach 
speed in knots. f 14l This is approxim ately true for FAR 23 and military aircraft 
without thrust reversers and FAR 25 aircraft with thrust reversers. While the 
FAR 25 aircraft have the additional requirement of a two-thirds distance 
increase, the thrust reversers used on most FAR 25 aircraft shorten the 
landing distance by about the same amount. 
Equation (5.11) provides a better approximation of the landing distance, 
which can be used to estimate the maximum landing wing loading. The first 
term represents the ground roll to absorb the kinetic energy at touc hdown 
speed. The const ant term Sa represents the obstacle- clearance dista nce. 
where 
Standing = 80 ( -) ( CTC-max) + Sa {ft} 
= 5(-) (CT--maJ + Sa {m} 
CT = density ratio = P!anding/ Psea-level standard day 
(5.11) 
(CT= 1. 0 for sea-le vel standard day; CT= 0.79 4 for hot day at 5000 ft) 
Sa = 1000 ft {305 m} for airliner-t ype, 3- deg glideslope 
= 600 ft {18 3 m} for general-a viation-t ype· power-off approach 
= 450 ft {13 7 m} for STOL, 7-d eg glideslope 
For landing calculations with thrust reversers or reversible-pi tch propellers, multiply the ground portion of the landing [first term in Eq. (5. 11 )) 
by 0.66. However, FAR and other requirem ents often specify that thrust 
reversers cannot be used to meet landing specifications for a simple 
reason-they may break, right when you need them the most. 
For commercial (FAR 25) aircraft, multiply the total landing distance 
calculated with Eq. (5 .11) by 1. 67 to provide the required safety margin. 
The landing wing loading must be converted to takeoff conditions 
by dividing by the ratio of landing weight to takeoff weight. This ratio is 
usually not based upon the calculated end-of -mission weight, but is instead 
is based upon some arbitrary landing weight as speci fied in the design 
requirements. 
For most propeller-p owered aircraft and jet trainers, the aircraft must 
meet its landing requirement at or near the design takeoff weight, so the 
ratio is about 1. 0. For most jet aircraft, the landing is typically calculated at 
about 85% of takeoff weight. Military design requirements will freque ntly 
specify full payload and some percent of fuel remaining (usua lly 50%) for 
the landing.


<!-- p.134 -->

13 4 Air c raft Desi gn: A Concep tual Approach 
*#U Arrested Land ing 
Aircraft that land on Navy aircraft carriers are stopped by a cable-andbrake arrangement called "arresting gear." One of several cables strung 
across the flight deck is caught by a hook attached to the rear of the aircraft. 
The cable is attached at both ends to drum mechanisms, which exert a drag 
upon the cable as it is pulled by the aircraft, thus stopping it in a very 
short distance. 
For carrier-based aircraft, the approach speed (1.2 times the stall speed) is 
the same as the touchdo wn speed. Carrier pilots do not flare and slow down 
for landing. Instead, they are taught to fly the aircraft right into the deck, 
relying upon the arresting gear to stop the aircraft. By using this technique, 
the aircraft has enough speed to go around if the cables are missed. 
The landing weight limits for three standard arresting gears are depicted 
in Fig. 5.6. This figure can be used to determine the allowable approach 
speed based upon a first guess of the landing weight. The approach speed 
divided by 1. 2 defines the stall speed, which can then be used to estimate 
the wing loading. 
*#ff Wing Load ing for Cruise 
We could use the wing loading that maximizes range during cruise, but 
there is a problem. The wing loading for best cruise range is us ually much 
higher than that required for stall speed or other performance const raints . 
You ju st can't safely fly with such a small wing. Nevertheless, it is instruc tive 
to learn what W / S the airplane would like to have for cruise. This calculation 
Vl 
0 
15 0 
- 100 
"Cl 
QJ 
QJ 
a. 
Vl 
...., 
c 
QJ 
E 
- 50 
ro 
C'l 
c 
w 
Mark 7 arresting gear 
0 ---------------------0 20 40 60 80 100 
Maximum landing weight (10 3 lb) 
Fig. 5.6 Arresting gear weight limi ts.


<!-- p.135 -->

CHAPTE R 5 Thrus t-to-We ight Ratio and Wing Load ing 13 5 
might even encou rage us to use more sophisticated flaps to get more lift from 
a smaller and more optimal wing. 
To make this calculation, we must bring in the use of two aerod ynamic 
coefficien ts, CDo and e. CDo is the zero-lift drag coefficient and is approximately 0.015 for a jet aircraft, 0.02 for a clean propeller aircraft, and 0.03 for a 
dirty, fixed-gear propeller aircraft. 
The Oswald span efficiency factor e is a measure of drag due to lift efficienc y. During cruise, e is approximately 0.6 to 0.8 for a fighter and 0.8 for 
other aircraft. These coefficie nts are extensively discussed in Chapter 12 
along with methods for their estimat ion. The derivations of the equations 
used below are provided in Chapter 17. 
A propeller-po wered aircraft loses thrust as its speed goes up, so that it 
gets the maximum range when flying right at the speed for best L/D. The 
speed for best Lj D can be shown to result in the parasite drag equaling 
the induced drag (see Chapter 17). Therefore, to maximize range, a propeller 
aircraft should fly such that 
. c2 qSCD0 = qS -L 1TAe (5. 12) 
During cruise, the lift equals the weight, so the lift coefficient equals the 
wing loading divided by the dynamic pressure. Substitution into Eq. (5.12) 
allows solution for the required wing loading to maximize L / D for a given 
flight condition. This result [Eq. (5.13)) is the wing loading for maximum 
range for a propeller-p owered aircraft. 
Maximum prop range: 
(5 .1 3) 
As the aircraft cruises, its weight reduces due to the fuel burned, so the 
wing loading also reduces during cruise. Optimizing the cruise efficiency 
while the wing loading is steadily declining requires reducing the dynamic 
pressure by the same percent [see Eq. (5.13)] . This can be done by reducing 
velocity, which is undesirable, or by climbing to obtain a lower air dens ity. 
This range optimizing technique is kn own as a cruise-climb. 
A jet aircraft maximizes range at a higher speed than the speed for best 
L / D. Its thrust isn't much affected by the greater speed; in fact, it might be 
improved. At this higher speed the Lj D is slightly reduced from the best 
value, but because the airplane is going faster, it gets more range for the 
fuel used. This is mathematic ally derived in Chapter 17. 
When flying at this greater speed, the parasi te drag of the jet is three 
times the induced drag. Equating these yields the following formula for 
wing-lo ading selection for range optimization of jet aircraft: 
Maximum jet range: 
(5. 14)


<!-- p.136 -->

13 6 Aircr aft Desig n: A Concept ual Approach 
*#f:I Wing Load ing for Loiter En dur anc e 
Most aircraft will have some loiter requirement during the m1ss10n, 
typically 20 min of loiter before landing. Unless the loiter requirement is a 
substantial fraction of the total mission duration, it is better to optimize 
the wing loading for cruise. Still, it is worth doing a simple calculation ju st 
to see what wing loading would be desirable. 
Patrol aircraft such as the ASW design example of Chapter 3 are sometimes more concerned with time on station than with cruise efficienc y. 
Other aircraft that can be more optimized for loiter are airborne command 
post s and intelli gence- gathering aircraft, or the long-en durance UA Vs used 
for various mission these days. 
For an aircraft that is optimized for loiter, the wing loading should be 
selected to provide a high L/D. For jet aircraft, the best loiter occurs at 
maximum L/D, so Eq. (5.13), repeated as Eq. (5.1 5), should be used. For a 
propeller-p owered aircraft, loiter is optimized when the induced drag is 
three times the parasi te drag, which yields Eq. (5.16). This also provides 
the wing loading for minimum power required and is derived in Chapter 17. 
Maximum jet loiter: 
W/S = qy'TrAeCD0 (5 .15 ) 
Maximum prop loiter: 
(5 . 16) 
These equations assume that the loiter veloc ity and altitude are known. If 
the loiter altitude is not speci fied, it should be selected for best speci fic fuel 
consu mption at the loiter power setting. This is typically 30,000-4 0,000 ft 
{app roxima tely 10 ,000 m} for a jet and the limit altitude for the turboc harger 
for a piston- propeller aircraft. For a non- turboch arged engine, best loiter 
occurs at sea level. 
Usually, the loiter veloc ity is not specified. Instead, the designer must 
determine the best loiter velocity and select the wing loading according ly. 
This requires cross plotting of wing loadings with the resulting L/ D and 
speci fic fuel consumption for various velocities and altitudes. Such a procedure is too comple x for initial design purposes. 
For initial design purposes, it can be assumed that the best loiter velocity 
will be about 15 0-200 kt {about 325 km/h} for turboprops and jets and about 
80- 120 kt {abou t 180 km/h} for propeller-po wered aircraft. If altitude is not 
spec ified, the altitude for best fuel consum ption should be selected. 
The wing loading estimated from Eqs. (5.15) or (5.16) is the average 
during the loiter. This loa ding must be converted to takeoff cond itions by 
dividing the loiter wing loading by the ratio of the average loiter weight to 
the takeoff weight. In the absence of better information, this ratio can be 
assumed to be about 0.85.


<!-- p.137 -->

CHAP TER 5 Thru st-to-We ight Ratio and Wing Loadin g 13 7 
Remember that Eqs. (5. 15) and (5. 16 ) are to be used for designing an 
aircraft optimized sole ly for loiter. Optimizing for loiter alone is very rare 
in aircraft design. For most aircraft, the wing loading will be selected for 
best cruise or other requirements, and the loiter cap abilities will be a secondary consi deratio n. 
AIU Ins tantane ous Tur n 
An aircraft designed for air-to- air dogfighting must be capable of high 
turn rates. Turn rate will determine the outcome of a dogfight if the aircraft 
and pilots are evenly matched otherwise. When air-to- air missiles are in use, 
the first aircraft to turn toward the other aircraft enough to launch a missile 
will prob ably win. In a guns- only do gfight, the aircraft with the higher turn 
rate will be able to maneuver behind the other to "take the shot." A turn 
rate superior ity of 2 deg per second is usually considered significant. 
There are two different turn rates we care about. The "sust ained" turn 
rate for some flight condition is the tu-n rate at which the thrust of the aircraft is sufficient to maintain velocity and altitude in the turn. In other words, 
the thrust equals the drag for a sustained turn. 
If the aircraft turns at a quicker rate, the drag becomes greater than the 
available thrust, so the aircraft begins to slow down or lose altitude. The 
"instant aneous" turn rate is the highest turn rate possi ble, ignoring the fact 
that the aircraft will slow down or lose altitu de. Maximum instantaneous 
turn is set either by wing stall or by the aircraft's structural limit. 
The "load factor," or "g-lo ading, " during a tu_rn is the acceleration due to 
lift expressed as a multiple of the standard acceleration due to gravity 
(g = 32.2 ft/s 2 = 9.8 m/s 2). Load factor n is equal to the lift divided by the 
aircraft's weight. 
Level, unturning flight implies a load factor of one (n = 1). In a level 
turn, the wing must provide 1-g lift in the vertical direction to hold up the 
aircraft, so that the remaining g available to turn the aircraft in the horizon tal 
direction are equal to the square root of n squared minus 1 (see Fig. 17. 4). 
Thus, the radial acceleration in a level turn is g times the square root of 
(n2-1). 
Turn rate is equal to the radial accele ration divided by the veloc ity. For a 
level turn, this results in the well-kno wn turn rate equation [Eq. (5. 17)] . This 
gives turn rate in radians per second, which must be multiplied by 57.3 to 
obtain degrees per second: 
where 
. g- !f;= -v (5. 17) 
(5 .1 8)


<!-- p.138 -->

13 8 Air craft Desi gn: A Conceptual Approach 
Instant aneous turn rate is limited only by the usable maximum lift, up to 
the speed at which the maximum lift exceeds the load- carrying capabil ity of 
the wing structure. Fighter aircraft were previously designed to a maximum 
(limit) load factor of 7.33 g at combat weight. Newer fighters use 8 g. 
The speed at which the maximum lift available exactly equals the 
allowable load factor is called the "corner speed" and provides the 
maximum turn rate for that aircraft at that altit ude. In a dogfight, pilots 
try to get to corner speed as quickly as possible as it provides the best 
turn rate. Typically, a modern fighter has a corner speed of about 300350 kt {550-650 km/h} indicated airspeed (i.e., dynamic pressure) regardless of altitu de. 
Design specifications will usually require some maximum turn rate at 
some flight cond ition. Equa tion (5. 17 ) can be solved for the load factor at 
the specified turn rate as follows: 
- n= y- g) +1 (5 .19 ) 
If this value of load factor is greater than the ultimate load factor specified 
in the design requirements, somebody has made a mistake. The required 
wing loading can be solved for in Eq. (5. 18 ) as follows: 
W qCLmax S n 
(5. 20) 
The only unkn own is the maximum lift coefficient at combat conditions. This is not the same as the maximum lift coefficient for landing. 
During comba t, use of full flap settings is not pos sible. Also, there is a 
Mach number effect that reduces maximum lift at higher speeds. Frequent ly, 
the combat maximum usable lift will be limited by buffeting or controllability 
consi derat ions. 
For initial design purposes, a combat maximum lift coefficient of about 
0.6-0.8 should be assumed for a fighter with only a simple trailing-ed ge 
flap for combat. For a fighter with a complex system of le ading- and 
traili ng-edge flaps that can be deployed during combat, a maximum usable 
lift coefficient of about 1. 0- 1.5 is attainable. Chapter 12 provides better 
methods of estimating the maximum lift coefficient. 
The res ulting wing loa ding must be divided by the ratio of combat weight 
to takeoff weight to obtain the required takeoff wing loading. Luckily high-g 
combat is only done at a reduced combat weight, not at takeoff weight. 
Otherwise the weight pena lty would be extreme. 
If not otherwise spe cified, it can be assumed that combat weight is the 
takeoff weight with any external fuel tanks dropped and 50% of the internal 
fuel gone. This is app roxim ately 0.85 times the takeoff weight for most 
fighters.


<!-- p.139 -->

CHAP TER 5 Thru st-to-We ight Ratio and Wing Loading 13 9 
I Jll1I Sustain ed Turn 
The sustained turn rate is also impor tant for success in combat. If two aircraft pass each other in opposite directions, it will take them about 10 s to 
complete 18 0-d eg turns back towards the other. If one of the aircraft slows 
down below corner speed during this time, it will be at a turn- rate disad vantage to the other, which could prove fatal. 
Sustained turn rate is usua lly expressed in terms of the maximum load 
factor at some flight cond ition that the aircraft can sustain without slowing 
or losing altitude. For example, the abilit y for sustaining 4 or 5 g at 0.9 
Mach number at 30,000 ft {9 144 m} is freque ntly specified. Equations 
(5.17 ) or (5. 19 ) can be used to relate turn rate to load factor. 
If speed is to be maintained, the thrust must equal the drag (assum ing 
that the thrust axis is approxi mately aligned with the flight directio n). The 
lift must equal the weight times the load factor, so we can write: 
n = (T /W)(L/D) (5.21) 
Load factor in a sustained turn is maximized by maximizing the T / W 
and L/ D. The highest L/ D occ urs when the induced drag equals the parasite 
drag, as expressed by Eq. (5. 12). During a turn, the lift equals the weight times 
n, so the lift coefficient equals the wing loading times n divided by the 
dynamic pressure. Subst itution into Eq. (5.12 ) yields 
W/S = Cf._ ,/rrAeCDo 
n 
(5.2 2) 
This equation gives the wing loading that maximizes the sustained turn 
rate at a given flight condition. Note that if n equals one, Eq. (5.22) is the 
same as Eq. (5.13), the wing loading for best L/D in level flight. 
Equation (5.22) estimates the wing loading that maximi zes the sustained 
turn rate regard less of thrust available. This equation will freque ntly give ridiculously low values of wing loading that will provide the required sustained 
turn rate using only a fraction of the available thrust. 
The wing loading to exactly attain a required sustained load factor n using 
all of the available thrust can be determined by equating the thrust and drag, 
and using the fact that since lift equals weight times n, the lift coefficient 
during maneuver equals the wing loading times n, divided by the dynamic 
pressure. This yields Eq. (5.23) : 
or 
( c2) n2w2 T = qSCDo + qS 1Tle 
= qSCDo + qS7TAe 
T qCD0 W ( n2 ) 
- - -- + - -w - W/S S q1TAe 
(5.2 3) 
(5.2 4)


<!-- p.140 -->

14 0 Aircr aft Des ign : A Conceptual Appro ach 
Equation (5. 24) can be solved for W/S to yield the wing loading that 
exactly attains a required sustained load factor n [Eq. (5.25 )]. Also, Eq. 
(5.2 4) can be used later to recheck the T /Wa fter the wing loading is selected. 
w (T/W) ± V(T/W)2 - (4n2CD0/7TAe ) 
S 2n2 /q7rAe (5. 25) 
The thrust-to -weight ratio for this calculation is at combat cond itions, so 
the takeoff T / W must be adjusted to combat conditions by dividing by the 
ratio between combat and takeoff weight and by multipl ying by the ratio 
between combat thrust and takeoff thrust. 
If the term within the square root in Eq. (5.25) becomes negative, there is 
no solution. This implies that, at a given load factor, the following must be 
satisfied regardless of the wing loading: 
T lfiDo -> 2n --w - 7rAe (5. 26) 
It is very impor tant to realize in these calculations that the efficiency 
factor e is itself a function of the lift coefficient at which the aircraft is operating. This is due to the separation effects at higher lift coefficients that 
increase drag above the parabolic drag polar values. At high angles of 
attack the effective e value can be reduced by 30% or more. 
Unfortunately, the previous equati ons for turning flight are very sensit ive 
to the e value. If these equations yield W / S values far from historical values, 
the e value is prob ably unrealistic, and the calculated W / S values should be 
ignored. Methods in Chapter 12 will better account for the sep aration effects. 
4@11 Climb and Glide 
Append ix F cites numerous climb requirements for FAR or military aircraft. These specify rate of climb for various combinations of factors such as 
engine-out, landing-gear position, and flap settings. While the details might 
vary, the method for sele cting a wing loading to satisfy such requirements is 
the same. 
Rate of climb is a vertical velocity, typically expressed in feet-per- minute 
(which must be converted to feet-per- second for the foll owing calculatio ns) . 
Climb gradient G is the ratio between vertical and horizo ntal distance 
traveled. As will be shown in Chapter 17 , at normal climb angles the climb 
gradient equals the excess thrust divided by the weight, that is, 
or 
G= (T -D)/W 
D T 
-= -- G w w 
(5 .27) 
(5. 28)


<!-- p.141 -->

CHAP TER 5 Thru st-to-We ight Ratio and Wing Loading 141 
D/ W can also be expressed as in Eq. (5.29), where in the final expression the 
lift coefficient is replaced by W / qS. 
D qSCD0 + qS(C'ffrrAe) qCDo W 1 -= = -- + - --w W WjS S q7TAe (5.2 9) 
Equating Eqs. (5.28) with (5.29) and solving for wing loading yields: 
W [(T/ W) - G] ± V[(T/ W) - G]2 - (4CD0 /1TAe) 
S 2jq1TAe (5.3 0) 
T / W must be relevant to the flight conditions and weight under consideration. The resulting W / S must then be ratioed to a takeoff-weight value. 
The term within the square root symbol in Eq. (5.30) cannot go below 
zero, so the following must be true regardless of the wing loading: 
!__ >G -t- 2 {C;;; w - V -;Ae (5 .31) 
This equation says that no matter how "clean" your design is, the T/W 
must be greater than the desired climb gradient. A subtle implication of 
this equation is that a very clean aircraft that cruises at a high speed 
despite a very low T / W will prob ably climb poorly. A 200-mph airplane 
that flies on 20 hp can't be expected to climb as well as an airplane that 
requires 200 hp to reach 200 mph (unless the latter weighs 10 times as much) . 
CDo and e values for some of the climb conditions speci fied in Appen dix F 
must include the effects of flaps and landing gear. Chapter 12 will provide 
methods for estimating these effects, but, for now, approximations can 
be used. 
For takeoff flap settings, CDo will increase by about 0.02 and e will 
decrease about 5%. For landing flap settings, CDo will increase by about 
0.07, and e will decrease by about 10% relative to the no-f lap value. Retractable landing gear in the down position will increase CDo by about 0.02. l15l 
Sometimes the rate of climb must also be calculated with one engine 
wind-milling or stopped. The thrust loss due to a "dead" engine can be 
accounted for in the T / W. For example, if a three-engine aircraft loses one 
engine, the T / W becomes two-thirds of the original T / W. 
The drag increase due to a windmilling or stopped engine will further 
reduce the climb rate. Chapter 12 provides methods for estimating this 
drag. For rough initial analysis, however, it can proba bly be ignored. 
Equation (5.30) can also be used to establish the wing loading required to 
attain some specified glide angle, by setting T / W to zero and using a negative 
value of G (i.e., a glide is a climb in the negative direct ion) . If a particular sink 
rate must be attained, the value of G to use is the sink rate divided by the 
forward velocity. Make sure that both are in the same units.


<!-- p.142 -->

14 2 Air c raft De sign: A Concep tu al Approach 
4Jlf J Maximum Ce il ing 
Equation (5.30) can be used to calculate the wing loading to attain some 
maximum ceiling, given the T /Wa t those cond itio ns. The climb gradient G 
can be set to zero to represent level flight at the desired altitu de. Freque ntly, a 
small residual climb capabilit y, such as 100 ft/min {30.5 m/min} is required 
at the usable maximum ceiling (called the "service" ceiling) . This can be 
included in Eq. (5 .30) by first solving for the climb gradient G (climb rate 
divided by forward veloc ity). 
For a high- altitude aircraft such as an atmospheric research or reconnaissance plane, the low dynamic pressure available can determine the minimum 
pos sible wing loading. For example, at 100,000 ft {30 ,480 m} and 0.8 Mach 
number, the dynamic pressure is only 10 psf {0.5 kN/m 2}. Equation (5.13 ) 
[repeated below as Eq. (5.32)] can be used to determine the wing loading 
for minimum power: 
(5. 32) 
This might suggest a wing loading so low as to be impractical, so should 
be compared with the wing loading required to fly at a given lift coefficient, 
that is, 
W/S =q CL (5. 33) 
For efficiency during high- altitude cruise, the lift coefficient should be 
near the airfoil design lift coefficient. For a typical airfoil, this is about 0.5. 
For a high- altitude aircraft, new high-lift airfoils with design lift coefficie nts 
on the order of 0.9 5-1. 0 can be used. 
Sele ction of Th rust to Weigh t and Wing Loading 
In the method presented here, an initial estima te of the thrust-to -weight 
(or power-to-w eight) ratio is made and then used to calcula te the required 
wing loading to meet various performance requirements. From these wing 
loadings, the lowest value should be selected to ensure that the wing is 
large enough for all flight conditions. Don't forget to convert all wing loadings to takeoff conditions prior to comparisons. 
A low wing loading makes a bigger wing which will always increase aircraft weight and cost. If a very low wing loading is driven by only one of 
the requireme nts, it might make sense to reconsider that requirement. Alternatively, this may point to a change in the design itself, perhaps adding more 
sophisticated flaps as a way to allow a higher wing loading. 
Also, keep in mind that the optimal wing load ings calculated by Eqs. 
(5.13-5.16 ), (5.22), and (5.32) are aerod ynamic optimizations, not firm 
requirements. If these drive the wing loading to ridiculo usly low values, 
they can be ignored.


<!-- p.143 -->

CHAPTE R 5 Thru st-to-We igh t Ratio and Wing Loading 14 3 
When the best compromise for wing loading has been selected, the 
thrust-to -weight ratio should be rechecked to ensure that all requirements 
are still met. The equations in the last section that use T / W should be 
recalculated with the selected W/S and T/W. 
Sometimes a particular requirement such as stall speed will force an 
obviously low value of wing loading, all by itself. This can be calculated 
first and then used in these same equations to solve for T / W. Otherwise, 
the proced ure is the same. 
It is also possi ble to select initial values for W / S and T / W by carpet plot 
or another optimization method (see Chapter 19). This is done using prelayout estimates of the various coefficien ts and weights, so this author 
believes that the time spent usually isn't worth it. Push to a Dash-One 
layout as quickly as possible, then optimize from its geomet ry. But if a 
good pre- layout optimization tool is alread y available for the class of aircraft 
you are designing, then feel free to use it. But don't belie ve it until you've 
redone the optimization using parameters taken from the real design layout. 
In any case, these selected values o( W / S and T /W are used only for the 
initial design layout. Once it is completed, a detailed optimization of those 
parameters will be done and the design will be revised according ly. The 
initial values are just to get the design started and are never used again. 
What We've Lea rned 
We've learned how to select reason able initial values for the thrust-to-weight 
ratio and wing loading, key parameters for attaining the required performance.


<!-- p.144 -->

14 4 Airc raft Desi gn: A Concep tu al Approach 
Photo cred it: D. Raymer. 
Saab 270 "Lilldraken"
