# Raymer Ch.6 - Initial Sizing

*Converted from `Daniel P. Raymer - Aircraft Design_ A Conceptual Approach (2018, American Institute of Aeronautics and Astronautics Inc.) - libgen.li.pdf` by `tools/pdf_to_md.py`. Page markers are printed page numbers.*


<!-- p.145 -->

Initial Sizing 
• A bette r method of sizi ng offers mor e accur acy and al lows for certa in co mple xities 
in clud ing "fix ed-s ize" vs "r ubb er" engin e, and al so a we ight drop. 
• This method steps thr ough the mis sion to find fuel burn, making it too la borious for 
hand ca lculations. 
• We can then size the fuse lage and ta ils. 
In trod uction 
A ircraft sizing determines the takeoff gross weight and fuel weight 
required for an aircraft to perform its design mission. Sizing is the 
single most impor tant calculation for aircraft design. It is an essential tool for initial design layout and for analyzing and optimizing the aircraft 
after that first design layout is completed. 
Sizing seems "backward s" to the unini tiated. People assume that we 
designers draw a nice aircraft concept and then analyze how far it goes. 
That is wrong. We do the opposi te. We know how far it goes-it must 
meet the required range. What we don't know is how big the airplane has 
to be to go that far. Sizing gives us that critical answer and allows us to 
then determine the engine size, the sizes of the wings and tails, and even 
the sizes of landing gear, fuel tanks, and other aircraft systems used to 
make the design layout. 
Sizing was introduced in Chapter 3, in which a quick method based upon 
minimal information about the design was used to estimate the sizing parameters. This chapter prese nts a more refined method capable of dealing 
with most types of aircraft- sizing problems. It is suitable for pre- layout calculations and also is good eno ugh for the refined sizing calculations made 
after the initial design drawing is made. 
One disad vantage, though, is that this method is more complica ted and 
probabl y too time cons uming for hand calculat ion. Luckily, it is quite easy 
14 5


<!-- p.146 -->

14 6 Air c raft De sign: A Concept ual Appr oa c h 
to code. A free Basic sour ce code file of such a computer program can be 
found on the author's website, www.aircraftdesign .com. 
"Rubber " vs "F ixed -Size" Engi nes 
An aircraft can be sized using an existing engine or a new-design engine. 
The existing engine is obviously fixed in size and thrust, so it is referred to as 
a "fixed-size- engine" or, confusing ly, a "fixed-engine" ("fixed" refers to the 
engine size, not to how it is attach ed!). 
The alternative, an all-new engine, can be designed to any size and thrust 
required. It is often called a "rubber engine" because it can be "stretched" 
during the sizing process to provide any required amount of thrust. The 
engine companies would be happy to create a new engine at any size you 
desire, as long as someb ody pays for it. 
The use of a rubber or a fixed-size engine actually changes the sizing 
process a bit. The rubber engine can be scaled to any thrust so that the 
thrust-to -weight ratio can be held to some desired value even as the aircraft 
weight is varied. The rubber- engine sizing approach allows the designer to 
size the aircraft to meet both performance and range goals, by solving for 
takeoff gross weight while holding the thrust-to-w eight ratio required to 
meet the performance objectives. As the weight varies, the rubber engine is 
scaled up or down as required. 
This is not possible for fixed-en gine aircraft sizing. For a particular existing engine, you cannot always meet both range and performance requirements. If you size the aircraft up in weight eno ugh to meet the range 
requirement, it may be too heavy to meet performance requirements with 
that engine. So when a fixed-size engine is used, either the mission range 
or the performance of the aircraft must become a "fallout" parameter. 
Methods for both types of sizing are discussed below. 
Rubber- engine sizing is used during the early stages of an aircraft proj ect 
that is sufficiently impor tant to warrant the development of an all new 
engine. This is gene rally the case for a major military fighter or bomber 
program and is sometimes the case for a commercial transpor t proj ect 
such as the SST. 
In such design projects, the designer will use a rubber engine in the 
early stages of design and then, with the customer, tell the engine comp any 
what characteristics the new engine should have. When the engine company finalizes the design for the new engine, it becomes fixed in size and 
thrust. The aircraft concept will then be finalized around this now-fixed 
engine. 
Developing a new jet engine will cost billions of dollars, and even a piston 
engine is very expensi ve to bring to market. Most aircraft proj ects do not rate 
development of a new engine, so they must rely on selecting the best of the 
existing engines. However, even projects that must use an existing engine 
may begin with a rubber-en gine design studies to determine what


<!-- p.147 -->

CHAPTE R 6 Ini tial Sizing 14 7 
characteristics to look for in the eventual selection of an existing engine. 
Sometimes we "rubberize" an actual engine to learn more about engine 
options before we lock in a choice. 
Rubber -En gin e Sizing 
Mii Revi ew of Sizing 
Chapter 3 presented a quick method of sizing an aircraft using a configuration sketch and the selected aspect ratio. From this information an 
estimate of the maximum L/D was graphic ally obtained. Using approximations of the specific fuel cons umption, the changes in weight due to the 
fuel burned during cruise and loiter mission segmen ts were estimated, 
expressed as the mission- segment weight fraction Wi/ Wi-1· Using these 
fractions and the approximate fractions for takeoff, climb, and landing that 
were provided in Table 3.2, the total mission weight fraction Wx/ Wo 
was estimated. 
For different classes of aircraft, statistical equations for the aircraft 
empty-weight fraction were provided in Table 3.1. Then, the takeoff weight 
was calculated using Eq. (3.4), repeated below as Eq. (6. 1). 
Because the empty weight was calculated using a guess of the takeoff 
weight, it was necess ary to iterate toward a solution. This was done by calculating the empty-weight fraction from an initial guess of the takeoff weight 
and using Eq. (6. 1) to calcul ate the resulting takeoff weight. If the calcula ted 
takeoff weight did not equal the initial guess, a new guess was made somewhere between the two. 
· 
where 
- = 1. 06(1- -) 
(6 .1) 
(6.2) 
Equation (6.2) assumes that the aircraft's change in weight during the 
mission is entirely fuel burn so that this method is limited to missions that 
do not have a sudden weight change, such as a payload drop. Also, buried 
in the math is the assumption that T / W is being held constant, so it isn't 
very accurate when used for fixed-engine sizing. 
+.If J Refi ned Sizing Eq uation 
A better but somewhat more laborious sizing method can be derived. As 
with the method in Chapter 3, the design takeoff gross weight is first 
expressed as the sum of the crew weight, payload weight, fuel weight, and 
empty weight. This is shown in Eq. (6.3), which resembles Eq. (3 .1) except


<!-- p.148 -->

14 8 Aircr aft De sign: A Concep tu al Approach 
that the payload now permits both fixed and dropped payloads. The empty 
weight is again expressed as an empty-weight fraction [Eq. (6.4 )], but the 
fuel weight will be determined by "stepping" through the mission and calculating the fuel burned during each mission segment. 
or 
Wo = Wcrew + Wfixed payload + Wdropped payload 
+ Wfuel + Wempty 
Wo = Wcrew + Wfixed payload + Wdropped payload 
+ Wfuel + (;-) Wo 
(6.3) 
(6.4 ) 
As before, an initial guess of the takeoff weight is used to determine a calculated takeoff weight, and the solution is iterated until the two are approximately equal to within a few percent. Refined methods for determining the 
empty-weight fraction and the fuel used are discussed in the following 
sections. 
*·m Emp ty-Weigh t Fraction 
Even in this improved sizing method, the empty-weight fraction must be 
estimated statistic ally for pre-la yout calculat ions. The simple equations in 
Table 3.1 could be applied. These used only a single independent variable 
Wo to predict the empty weight fraction, but if the equations are calibrated 
using data from recent airplanes that are similar to the new airplane being 
designed, this may be the best possible estimate at this time. 
Another approach is to develop statistical equations using additional 
independent variables. Tables 6.1 and 6.2 were prepared using data from f6l 
to provide empty-weight equations based on aspect ratio, thrust-to -weight 
(or horsepo wer-to -weight) ratio, wing loadi ng, maximum speed, and, 
of course, takeoff gross weight Wo. These additional variables result in a 
Table 6. 1 Em pty Weight Frac tion vs W0, A, T /W 0, W0/S, and Mmax 
__ ............ 
Jet train er 0 4.28 - 0. 10 0. 10 0.20 - 0.24 0.1 1 
Jet fig hter - 0.02 2 . 16 - 0, 10 0.2 0 0.0 4 - 0. 10 0.08 
Mil ita ry ca rgo/bomber om 1. 71 -0 . 10 0. 10 0.06 -0 . 10 0.05 
Jet tra nspor t 0.32 0.6 6 -0 .13 0.30 0.06 - 0.05 0.05 
Kvs = variable sweep cons tant = 1. 04 if variable sweep and 1. 00 if fixed swee p.


<!-- p.149 -->

CHAP TER 6 Ini tial Sizi ng 14 9 
Table 6.2 Em pty Weigh t Fraction vs Wo, A, hp/W o, Wo/S, and V max (kt) 
_ .......... .. 
Sail plane-unpowered 
Sailpl ane -powered 
Home buil t-metal /wood 
Homebui lt-co mp osite 
Genera l aviation- sin gle 
engi ne 
Gener al aviatio n-twin 
engi ne 
Agric ultural ai rcraft 
Twin turbop rop 
Flyi ng boat 
0 0.7 6 - 0.05 0. 14 0 - 0.30 0.0 6 
0 1 .21 -0 .04 0. 14 0. 19 - 0.20 0.05 
0 0. 71 - 0. 10 0.05 0. 10 -0 .05 0.1 7 
0 0.69 - 0. 10 0.05 0. 10 - 0.05 0. 17 
-0 .25 1 . 18 -0 .20 0.0 8 0.0 5 - 0.05 0.27 
-0 .90 1. 36 - 0. 10 0.0 8 0.05 -0 .05 0.20 
0 l .67 - 0. 14 O.D? 0. 10 - 0. 10 0.1 1 
0.37 O.Q 9 -0 .06 0.08 0.0 8 - 0.05 0.3 0 
0 0.42 - 0.01 0. 10 0.05 -0 .12 0. 18 
better statistical fit, with only about half the standard deviation of the 
equations in Table 3.1. 
Still, these equations are only suitable for use before the airplane layout 
is made, and they are not appropr iate for design trade studies. After the 
layout is completed, the compon ent weight buildup methods in Chapter 15 
are used to calculate the weight of the baseline and to perform trade 
studies to optimize the design. 
Mfll Fuel Weight 
The remaining unknown in Eq. ( 6.4) is the fuel weight. Previously this was 
estimated as a fuel fraction by determining the ratio between the weight at 
the end of the mission and the takeoff weight Wx/ Wo. Because the only 
weight loss during the mission was due to fuel usage, the fuel fraction was 
found simply as (1 - Wx/Wo). 
This impro ved mission allows a weight drop, so it is necessa ry to calc ulate 
the weight of the fuel burned during every mission leg and sum for the total 
mission fuel. This isn't as difficult as it sounds and is based on the same 
mission- segment weight fractions Wi/ Wi-l that were calculated in the 
Chapter 3 method. The difference is that rather than multiplying them all 
together they are used one at a time to determine fuel burn in each segment. 
The missio n-s egment weight fractions Wi/ Wi- l are calculated as before 
for all mission segmen ts other than those that are weight drops. For each 
mission segment, the fuel burned is then equal to 
wfi = (1 - wi ) wi- 1 Wi- 1 
(6.5)


<!-- p.150 -->

15 0 Airc raf t Des ign: A Conceptual Appr oa ch 
The total mission fuel \tf.n then is equal to 
x 
w1m = 'L wf; (6.6 ) 
1 
The proced ure is simple: start with the initial guess of takeoff gross weight 
Wo and use it as Wi in Eq. (6.5). Apply the mission- segment weight fractions 
(Wi/ Wi -1) for the first mission segment, probably takeoff, and determine the 
fuel burned during that segment. Subtract this from Wi to find the weight 
at the beginning of the next segmen t, which becomes the next Wi. Continue 
this process until the end of the mission, adding up the fuel used for each 
segment. If there is a weight drop segment, simply reduce the next Wi by 
the dropped amount and continue. 
The total aircraft fuel includes the mission fuel as well as an allowance for 
reser ve and trapped fuel. This reser ve fuel allowance is usua lly 5% and 
accounts for an engine with poorer-than-no minal fuel consumption. An 
additiona l allowance of 1 % for trapped (i.e., unusable) fuel is typical. Thus, 
the total aircraft fuel is 
(6. 7) 
Methods for estimating the miss ion-se gment weight fractions are presented next. These are a comb ination of analytical and statistical methods, 
improved from the methods used in Chapter 3. Chapter 19 offers even 
better methods, but they are more suitable for analyzing the aircraft after 
that first layout has been made. 
*·ff J Engine Start, Tax i, and Takeoff 
As before, the miss ion-s egment weight fraction for engine start, taxi, and 
takeoff is estimated historic ally at this poin t. A reasonable estimate is 
W'f/ Wi- l = 0.9 7 - 0.9 9 (6.8) 
Previously a fraction of 0.985 was suggested for climb. From data in[1 6l , 
the weight fraction for an aircraft climbing and acceler ating to cruise altitude 
and Mach number M (starting at Mach 0.1) can be approximated as follow s: 
Subsonic: 
Wi/ Wi- l = 1. 0065 - 0. 0325 M (6. 9) 
Supersonic: 
W'f/ Wi-l = 0.991 - 0. 007M - 0.01 M2 (6. 10)


<!-- p.151 -->

CHAPTER 6 Ini ti al Sizi ng 15 1 
For an acceleration beginning at other than Mach 0.1, the weight fraction 
calculated by Eqs. (6.9) or (6. 10) for the given ending Mach number should be 
divided by the weight fraction calculated for the beginning Mach number 
using Eqs. (6.9) or (6. 10). 
For example, acceleration from Mach 0.1 -0.8 requires a weight fraction 
of about 0.9805, whereas acceler ation from Mach 0. 1-2.0 requires a weight 
fraction of 0.937. To accel erate from Mach 0.8-2.0 would require a weight 
fraction of (0.937 /0.9805) or 0.956. 
A complica ted but far superior method is derived in Chapter 17. 
Mfl Cruise 
Equation (3.6), repeated next as Eq. (6.1 1), is derived from the Breguet 
range equation for cruise as derived in Chapter 17. For propeller aircraft, 
the specific fuel consu mption C is calculated from the propeller speci fic 
fuel consumption Cp or Cbhp using Eq. (3.10). Substitution of Eq. (3.10 ) 
into Eq. (6.11) yields Eq. (6. 12). 
Jet: 
Prop: 
Wi -RC 
-- =e xp Wi-l V(L/D) (6.11 ) 
Wi [-RCpower] [ -RCbhp l 
Wi- l = exp YJp (L/D) = exp 550 YJp (L/D) {fps} (6 ·1 2) 
where 
R = range 
C = specific fuel consum ption 
V = velocity 
L/ D = lift-to- drag ratio 
Y/p = propeller efficiency 
During cruise and loiter, the lift equals the weight, so that the L / D can be 
expressed as the inverse of the drag divided by the weight: 
L 1 
D qCn0 + W _l_ 
W /S S q-rrAe 
(6 .1 3) 
Note that the wing loading used in Eq. (6. 13 ) and subsequent weight 
fraction equations is the actual wing loading at the cond ition being evaluated, 
not the takeoff wing loading.


<!-- p.152 -->

15 2 Air c raft Desi gn: A Conc eptu al Appr oa ch 
+.ff:J Loiter 
Repea ting Eq. (3.8), the weight fraction for a loiter mission segment is 
Jet: 
Wi -EC -- =e xp --Wi-1 L/D 
where E = endurance or loiter time. 
(6. 14) 
(Note -watch the units !) Subst itution of Eq. (3. 10) into Eq. (6. 14) yields 
the following: 
Prop: 
Wi [-EVCpower] [ -EVCbhp l 
Wi-1 = exp YJp (L/D) =e xp 550 rip (L/D) {fps} 
*·fP Known -Ti me Fuel Bur n and Com bat 
(6 .1 5) 
Some mission segments can be modeled simply by turning on the engine 
and running it for a certain leng th of time. Such a mission segment could be 
called a "known-time fuel burn" and can be used for combat as well as engine 
warm-up, taxi, and sometimes descent. 
For a fixed-size engine, the weight of the fuel burned in a known-time fuel 
burn is simply found from the definition of speci fic fuel cons umption, that is, 
the product of thrust, specific fuel consu mption, and duration of the combat. 
Dividing by weight yields a mission- segment weight fraction suitable for a 
rubber engine where T /Wi s held const ant, namely, 
Wi/Wi-1 = 1 - C( T / W) (d) (6 .1 6) 
Note that the T/W is defined by the thrust and weight during that 
segment weight, not at takeoff conditions. Watch the units, espec ially the 
time unit. Whether seconds, minutes, or hours, the time unit must match 
the units of speci fic fuel consumption. 
A com bat mission segment is normally spe cified as either a given time 
duration d at maximum thrust (typica lly d = 3 min) , or as a certain 
number of combat turns at some altitu de and Mach number. 
If the combat is defined by some number of turns, the duration of combat 
d must be calculated. The time to compl ete x turns is the total number of 
radians to turn divided by the turn rate. When combined with Eq. (5. 17 ), 
this yields 
d = 2m: = 27T VX 
- gJn2 -1 
(6. 17 ) 
The load factor n for a sustained com bat turn is found by assuming that 
the thrust angle is approximately aligned with the flight direction, so the


<!-- p.153 -->

CH APTE R 6 Ini tial Sizi ng 15 3 
thrust must equal the drag. The lift must equal the weight times the load 
factor n, which yields 
n = (T /W) (L/D) (6.18) 
This is subj ect to the constraints of maximum structural load factor 
[Eq. (6. 19)] and maximum available lift [Eq. (6.20 )] . 
n - nmax 
< qCLmax n 
--- W/S 
(6 .19 ) 
(6.2 0) 
The lift-to- drag ratio is found by including the load factor term in 
Eq. (6. 13), which results in Eq. (6.21). The changes to the wing's Oswald 
span efficiency factor e at combat conditions discussed in the last chapter 
should be used in Eq. (6.2 1). 
L 1 
D CD0 • n(W /S) q n(W /S) + q7rAe 
lfll11 Desce nt for Landing 
(6 .21) 
Descent can be estimated by calculating the time it takes to descend, then 
applying the known-time fuel burn equation. For initial sizing, it is usually 
estimated historic ally: 
Wi/ Wi-1 = 0. 990 to 0.9 95 (6. 22) 
0111 Landing and Taxi Back 
Again, a historical app roximation is used for now: 
Wi/ Wi-1 = 0. 992 to 0.9 97 (6. 23) 
Alf J Summar y of Refi ned Sizing Method 
The design and sizing method presen ted so far is summarized in 
Figure 6.1. From the design objectives and sizing mission, the wing geomet ry 
parameters are selected. A con ceptual sketch or rough layout is used to estimate the wetted- area ratio, from which CDo is estimated. Initial values for 
thrust-to-w eight (or horsepo wer-to -weight) ratio and wing loading are 
defined, then missi on-se gment weight fractions are estimated for each leg 
of the design mission. 
The iterati on for takeoff gross weight Wo begins with an initial guess of 
Wo. For each mission leg, the aircraft weight is reduced by either the 
weight of fuel burned or the payload weight drop ped. The total fuel 
burned is summed throughout the mission. Equations (6.7) and (6. 4) are


<!-- p.154 -->

15 4 Air craft De sign : A Conceptual Approac h 
Sketch or initial layout 
1 
Swe/Sref 
and CDO 
Engine SFCs 
w W.e equation 0 
-I 
-I 
-------1------------I 
-I 
Fig. 6. 1 
Design objectives I- Wing geometry selection and "e" estimate 
I- T!Wand WIS 
t 
- for each 
wi-1 mission segment 
t 
W0guess 
t Iterate W5foreach for mission segment solution 
t 
W0 calcula ted 
Refined sizing method . 
Sizing mission 
then used, along with a statistical empty weight fraction estimation, to arrive 
at a calculated value of Wo. 
If this does not equal the guessed value for Wo, a new guess for Wo is 
selected. Experience indicates that the solution will converge most rapid ly 
if the new guess for Wo is about three-four ths of the way from the initial 
guess to the calculated W o value. 
This pro cedure is less complica ted than it sounds! Examples can be found 
in Chapter 23. 
Fi xed-Engine Sizing 
The confusing title of this subsection is a shortened version of the actual 
process name, "fixed-si ze engine aircraft sizing." The aircraft sizing procedure when a fixed-size engine is emplo yed is basica lly similar to that for 
rubber-en gine sizing, with the adjustmen ts to the mission segment weight 
fraction calculations as described above. 
However, the fixed-size engine assumption often causes a problem. The 
aircraft cannot make the mission range, but if you increase TOGW to add 
fuel, now it cannot meet a performance requirement such as takeoff distance 
or engine -ou t rate of climb. 
There are then two basic choices: insist upon mission range which means 
that performance must be secon dary, or insist upon performance and see 
what you get for range. You cannot guarantee both range and performance, 
unless you're willing to buy a bigger engine.


<!-- p.155 -->

CH APTE R 6 Ini tial Sizing 15 5 
Jllll Mi ssion Range Mu st Be Met 
If the mission range requirement must be met no matter what, then the 
aircraft performance cannot be assured during the sizing process. The takeoff 
gross weight will be set by fuel requirements. At that weight, the fixed-si ze 
engine might not provide the thrust-to -weight ratio needed for performance 
consideration s. 
In this case the takeoff gross weight can be solved by iterati on of Eq. (6.4) 
as for the rubber-en gine case, with one major except ion. Since the thrust 
cannot change, the thrust-to -weight ratio will vary as the aircraft weight 
varies during the sizing iterati ons. 
Equation (6. 16 ) for known-time fuel burn mission segmen ts (com bat, 
takeoff, desc ent) assumes a speci fic T / W during comb at, so it cannot be 
used. Instead, the fuel burned by a fix ed-size engine over a particular 
amount of time is directly calculated as simply the thrust times the speci fic 
fuel consumption times duration d: 
(6. 24) 
Fuel weight calculated by Eq. (6.2 4) is then used in the iterati ons to solve 
Eq. (6.4), being subtracted from the vehicle weight at that point in the mission 
and added to the running total of fuel burned. 
Once the takeoff gross weight is determined, the resulting thrustto-weight ratio is calculated and used to determine the actual aircraft 
performance. 
#.Jf J Performanc e Mus t Be Met 
If the aircraft performance such as takeoff distance, rate of climb, or turn 
rate simply must be met, then the range must be allowed to vary. This makes 
the sizing process very simple. The required thrust-to -weight ratio T /W is 
determined by the methods of the last chapter to provide all required performance capabilities, using the known characteristics of the selected 
engine. Then the takeoff gross weight is trivially found as the total engine 
takeoff thrust divided by the required takeoff thrust-to -weight ratio. 
W, _ NTpere ngine o - (T/ W) (6 .2 5) 
where N = number of engines. 
With the takeoff weight known, the range capabilit y can be determined 
from Eq. (6.4) using a modified iteration techniq ue. The known takeoff 
weight is repe atedly used as the "guess" Wo, and the range for one or more 
cruise legs is varied until the calculated Wo equals the known W0. 
This technique can also be used to vary mission parameters other than 
range. For example, a research aircra ft could be sized for a certain radius


<!-- p.156 -->

15 6 Aircr aft De sign : A Conceptual Appr oach 
(range out and back) with the number of minutes of test time as the 
variable parameter. 
For either method, if you wish to meet both range and performanc e 
requirements then you'll have to change the design. Consider a differen t 
engine, or more engines, or some other subst antial change to your desig n 
approach. Or, try to change the requirements. One possi bility is to reduce 
the pay load, but remember that payload is usually the reason for buildin g 
the aircraft in the first place! 
Desi gners sometimes skip the sizing process detailed above. Instead they 
start by selecting an existing engine, usua lly because of cost or availability . 
This engine is chosen to be about the right thrust or power for a "typical" 
airplane of that class. Next, they estimate the T/ W or P/ W needed to meet 
performance requireme nts, using methods as described above. Equation 
(6.25) is used to estimate TOGW , then the layout is made. 
From here on, this process is the same as the "performance must be met" 
process described above. Range is found after-the-fact. If range doesn't meet 
the stated desi gn mission range, the design must be modified or the requirements must be changed. Or, perhaps that engine isn't really the right one for 
this project. 
This method is common for battery-ele ctric aircr aft, as described in 
Chapter 10. 
Geo metry Sizing 
Once the takeoff gross weight has been calcula ted, the physical geomet ry 
of the fuselage, wing, and tails can be considered. For some aircraft, the 
fuselage size is determined strictly by the payload it must carry. A passe nger 
aircraft devotes most of its leng th to the passe nger compartment. Given the 
number of passen gers and the number of seats across, the fuselage length and 
diameter are esse ntially determ ined. 
For other types of aircra ft, the final leng th evolves as the design is 
prepared, including cons iderations for packaging internal compo nents, 
aerod ynamic "sleekne ss," ease of manufacture, and other consid erations as 
discussed in later chapters . For initial guidance during fuselage layout, 
Table 6.3 provides statistical equations for fuselage length developed from 
data provided in [6l . These are based sole ly upon takeoff gross weight and 
give remar kably good correlations to most existing aircraft. However, they 
should be considered no more than an initial starting poi nt. 
Proper fuselage layout includes definition of the fuselage fineness ratio. 
This is the ratio between the fuselage length and its maximum diameter.


<!-- p.157 -->

CHAP TER 6 Ini tial Sizi ng 15 7 
Table 6.3 Fuselage Length vs w 0 (lb or {kg}) 
Leng th = a- (ft or {m} ) 
Sailpla ne-un powered 0. 86 {0. 383} 
Sailplane -powered 0.71 {0 .316 } 
Homebu i It-me ta I /wood 3.6 8 { 1 .35} 
Homebui lt-com posite 3.5 0 {1 .28} 
General aviation- single engine 4.37 { 1. 6} 
Gener al aviation -twin engine 0.8 6 {0 .366} 
Agricultur al ai rcraf t 4.0 4 { 1. 48} 
Twin tu rboprop 0.37 {O. 16 9} 
Flying boat 1 .05 {0.439} 
Jet train er 0. 79 {0.3 33} 
Jet fighter 0 .93 {0.3 89} 
Mil ita ry cargo /bomber 0.23 {0 . 10 4} 
Jet transpor t 0.67 {0.287 } 
0.48 
0.48 
0.23 
0.23 
0.23 
0.4 2 
0.23 
0.51 
0.40 
0.41 
0.39 
0.5 0 
0.4 3 
If the fuselage cross section is not a circle, an equivalent diameter is calculated from the cross-s ectional area. 
Numerous design books such as the classic Hoerner Fluid Dynamic Drag[9] indicate that drag is minimized with a fineness ratio of around 
three. This is an odd conclusion because few succes sful designs actually 
use such a low fineness ratio. 
Like so many things, the best answer depends upon the assumptions. If 
it is assumed that the fuselage must have a diameter no less than a certain 
value, then three really is the best answer. This would be the case for a 
design where there is a speci fic layout requirement that forces a certain 
cross-se ction area, such as side-b y-side seating for two people. 
However, a fineness ratio of three might not provide a long enoug h tail 
moment arm. This can be so lved by using extra-l arge tails, or a tail boom 
that creates the streamlined "tadp ole" shape characteristic of many sailplanes 
and other small airplanes can be added. 
For a larger aircraft where the internal compon ents can be rearranged 
as desired, there proba bly isn't a firm requirement for a certain crosssection area. When fuselage fineness ratio is increased, the diameter can be 
reduced propor tiona lly keef ing the total volume the same. A recent analytical optimization study[1 7 found that if volume is held constant then 
the optimum fineness ratio for subsonic aircra ft is somewhere between 6 
and 8. Interest ingly enough, this matches the fineness ratios of most successful airship s. 
These values are suitable for subsonic aircraft. Supersonic drag is typically 
minimized by a fineness ratio of about 14, but that is very design dependent 
and can range from 10 to 15 or more.


<!-- p.158 -->

15 8 Air cr aft Des ign: A Con ce ptu al Approach 
When making the actual design layout, the various real-w orld const raint s 
such as cockpit and payload shape must take prio rity. For most design efforts 
the realities of pack aging the internal compo nents will ultimately establish 
the fuselage length and diameter-but it is good to know the optimal fineness 
ratio as a layout goal. 
The actual wing size can now be determined simply as the takeoff gross 
weight divided by the takeoff wing loading. Remember that this is the reference area of the trapezoi dal wing and includes the area extending into the 
aircraft centerline. 
Now that wing area is known, the equations of Chapter 4 can be used to 
lay out the trapezoidal wing. Loca ting it proper ly in the aircraft will be discussed in Chapter 7. 
+.JU Tail Volume Coeff icient 
For the initial layout, a historical approach is used for the estimation of 
tail size. The effectiveness of a tail in genera ting a moment about the 
center of gravity is propor tional to the force (i.e., lift) produced by the tail 
and to the tail moment arm. 
The prim ary purpose of a tail is to counter the momen ts produced by the 
wing. Thus, it would be expected that the tail size would be in some way 
related to the wing size. In fact, there is a dire ctly propor tional relationship 
between the two, as can be determined by examining the moment equations 
prese nted in Chapter 16. Therefore, the tail area divided by the wing area 
should show some consistent relationship for different aircraft, if the 
effects of tail moment arm could be accounted for. 
The force due to tail lift is propor tional to the tail area. Thus, the tail 
effectiveness is propor tional to the tail area times the tail moment arm. 
This product has units of volume, which leads to the "tail volume coefficie nt" 
method for initial estimation of tail size. 
Rendering this parameter nondimensional requires dividing by some 
quant ity with units of length. For a vertical tail, the wing yawing momen ts 
that must be countered are most direct ly related to the wing span bw. 
This leads to the "vertical tail volume coefficient," as defined by Eq. (6.26). 
For a horizo ntal tail or canard, the pitching mome nts that must be coun tered 
are most direct ly related to the wing mean chord Cw. This leads to the 
"horizo ntal tail volume coefficie nt," as shown by Eq. (6.27). 
LvTSvT cvT = 
bwSw (6. 26) 
(6. 27)


<!-- p.159 -->

CH APTER 6 Ini tial Siz ing 15 9 
Note that the moment arm L is common ly approximated as the distance from the tail quarter- chord (i.e., 25% of the mean chord length 
measured back from the leading edge of the mean chord) to the wing 
quarter-chord. 
The definition of tail moment arm is shown in Fig. 6.2, along with the 
definitions of tail area. Obser ve that the horizont al tail area is commonly 
measured to the aircraft centerline, whereas a canard's area is commonly 
considered to include only the exposed area. If twin vertical tails are used, 
the vertical tail area is the sum of the two. 
Table 6.4 provides typical values for volume coefficients for different 
classes of aircraft. These values (conser vative averages based upon data 
in[6, l8] ) are used in Eqs. (6.28) or (6.29) to calculate tail area. (Inciden tally)18l 
compiles a tremendous amount of aircra ft data and is highly recommended 
for every designer's library.) 
cvTbwSw SvT = ----LvT 
SHT = 
cHTCwSw 
LHT 
(6.2 8) 
(6.2 9) 
To calcul ate tail size, the moment arm must be estimated. This can be 
approximated at this stage of design by a percent of the fuselage length as 
estimated earlier. 
Tail volume coefficient method 
Sw =wing area 
bw =wing area c w= wing mean chord 
Fig. 6.2 Ini tial tail sizi ng .


<!-- p.160 -->

16 0 Air c raft De si gn: A Conceptual Appr oach 
Table 6.4 Toil Volume Coefficient 
Typical Valu es 
Horiz ontal cHT 
Sailplane 0.50 
Homebuilt 0.50 0.0 4 
Gener al aviation- single engine 0.7 0 0.04 
General aviation -twin engine 0.80 0.07 
Agricul tural 0.50 0.04 
Twin turboprop 0.90 0.08 
Flying boot 0.7 0 0.0 6 
Jet trainer 0. 70 0.06 
Jet fig hter 0.40 0.07 -0. 12 * 
Mil ita ry cargo /bom ber 1 .00 0.08 
Jet tra nspor t 1. 00 0.09 
*L ong fus elage with high wing loading needs lar ger value. 
For an aircraft with a front- mounted propeller engine, the tail arm is 
about 60% of the fuselage length. For an aircraft with the engines on the 
wings, the tail arm is about 50-55% of the fuse lage length. For aft-m ounted 
engines the tail arm is about 45-50% of the fuselage length. A sailplane has a 
tail moment arm of about 65% of the fuselage length. 
For an all- moving tail, the volume coefficient can be reduced by about 
10- 15 %. For a "T-t ail, " the vertical- tail volume coefficient can be reduced 
by approxim ately 5% due to the end-pl ate effect, and the horizo ntal tail 
volume coefficient can be reduced by about 5% due to the clean air seen 
by the horizontal. Simil arly, the horizo ntal tail volume coefficient for an 
"H-t ail" can be reduced by about 5%. 
For an aircraft that uses a "V-tai l," the required horizo ntal and vertical tail 
sizes should be estimated as before. Then the V surfaces should be sized to 
provide the same total surface area flO] as required for conventional tails. 
The tail dihed ral angle should be set to the arctangent of the square root 
of the ratio between the required vertical and horizo ntal tail areas. This 
should be near 45 deg. 
The horiz ontal tail volume coefficient for an aircraft with a contr ol-t ype 
canard is approximately 0.1, based upon the relatively few aircraft of this type 
that have flown. For canard aircraft there is a much wider variation in the tail 
moment arm. Typically, the canard aircraft will have a moment arm of about 
30-50% of the fuselage length. 
For a lifting canard aircraft, the volume coefficient method isn't applicable. Instead, an area split must be selected by the designer. The required 
total wing area is then allocated according ly. Typically, the area split alloca tes 
about 25% to the canard and 75% to the wing, although there can be wide 
variati on. A 50-50 split produces a tandem -wing aircraft.


<!-- p.161 -->

CHAPTE R 6 Ini tial Sizing 161 
For an airplane with a computerized "active" flight control system, the 
statistically estimated tail areas can be reduced by approximately 10% provided that trim, engin e-ou t, and nose wheel liftoff requirements can be met. 
These are discussed in Chapter 16. 
Contr ol- Surf ace Sizin g 
The primar y control surfaces are the ailerons (roll) , elevator (pitch) , and 
rudder (yaw). Final sizing of these surfaces is based upon dynamic analysis of 
control effectiveness, including structural bending and control-s ystem 
effects. For initial design, the following guidelines are offered. 
The required aileron area can be estimated from Fig. 6.3, an updated 
version of a figure from f19 l . In span, the ailerons typically extend from 
about 50% to about 90% of the span. In some aircraft, the ailerons extend 
all the way out to the wing tips. This extra 10% provides little control effectiveness due to the vortex flow at the wing tips, but can provide a location for 
an aileron mass balance (see the follo'"".ing) . 
Wing flaps occu py the part of the wing span inbo ard of the ailerons . If a 
large maximum lift coefficient is required, the flap span should be as large as 
possible. One way of acco mplishing this is through the use of spoi lers rather 
than ailero ns. Spoi lers are plates loca ted forward of the flaps on the top of the 
wing, typically aft of the maximum thickness point. Spoilers are deflected 
upward into the slipstream to reduce the wing's lift. Deplo ying the spoiler 
on one wing will cause a large rolling moment. 
1.0 
0.8 
c 
"' 
Cl. 
V1 
°' 0.6 c 
·----. 
c 
"' 
Cl. 
V1 
c 0.4 
0 
j! 
- guidelines 
0.2 
0 
0.10 0.15 0.20 0.25 0.30 0.35 
Aileron chord/wing chord 
Fig. 6.3 Ailer on gui deli nes.


<!-- p.162 -->

16 2 Ai rcraft De sign: A Conceptu al Appr oach 
Spoi lers are common ly used on jet trans ports to augment roll control at 
low speed and can also be used to reduce lift and add drag during the landing 
rollout. However, because spoi lers have very nonlinea r response characteristics, they are difficult to implement for roll control when using a manua l 
flight control system. 
High-speed aircraft can experience a phenomenon known as "ailero n 
reversal" in which the air loads placed upon a deflected aileron are so great 
that the wing itself is twisted. At some speed, the wing might twist so much 
that the rolling moment produced by the twist will exceed the rolling 
moment produced by the aileron, causing the aircraft to roll the wrong way. 
To avoid this, many transport je ts use an auxiliary, inboard aileron for 
high-speed roll cont rol. Spoilers can also be used for this purpose. Several 
military fighters rely upon "rolling tails" (horizo ntal tails capable of bein g 
deflected nons ymmetricall y) to achieve the same result. 
Elevators and rudders gener ally begin at the side of the fuselage and 
extend to the tip of the tail or to about 90% of the tail span. High-speed 
aircraft some times use rudders of large chord that only extend to about 
50% of the span. This avoids a rudder effectiveness problem similar to aileron 
revers al. Guidelines for prelimi nary control surface sizing are offered in 
Table 6.5. 
Control surfaces are usua lly tap ered in chord by the same ratio as the 
wing or tail surface so that the control surface maintains a const ant 
percent chord (Fig. 6.4) . This allows spars to be straig ht-tapered rather 
than curved. Ailerons and flaps are typically about 15- 25% of the wing 
chord. Rudder s and elevato rs are typically about 25-5 0% of the tail chord. 
Control- surface "flutter, " a rapid osci llation of the surface caused by the 
airloads, can tear off the control surface or even the whole wing. Flutter tendencies are minimized by using mass balancing and aerod ynamic balancing. 
Flutter is discussed in more detail in Chapter 8. 
Mass balancing refers to the addition of weight forward of the controlsurface hinge line to counterbalance the weight of the control surface aft 
Table 6.5 Control Sur face Sizing Guidel in es 
Ai rcraft 
Fig hter / attack 
Jet transpor t 
Jet train er 
Biz jet 
GA single 
GA !win 
Sailplane 
I I 
0.30* 
o.25 t 
0.35 
0.32 t 
0.45 
0.36 
0.43 
Rudder Cr/C 
0.30 
0.3 2 
0.35 
0.30 
0.40 
0.46 
0.4 0 
*Su per sonic usually all -moving ta il without separ ate ele vato r. 
t Often all -moving plus ele vato r.


<!-- p.163 -->

Wing or ta il 
CHAPTE R 6 Ini ti al Sizi ng 16 3 
' , \ \ 
' ' I 
' ' I 
' 
. 
', \ 't '' \ ' 
' \ \ 
' , \ \ 
' '. ' 
' , , 
',:- Ap ex 
Fig. 6.4 Consta nt-per cent chor d control sur face . 
of the hinge line. This greatly reduces flutter tendencies. To minimize the 
weight penal ty, the balance weight should be located as far forward as possible. Some aircraft mount the balance weight on a boom flush to the wing tip. 
Others bury the mass balance within the wing, mounted on a boom attached 
to the control surface. 
An aerodynamic balance is a portion of the control surface in front of the 
hinge line. This lessens the control force required to deflect the surface and 
helps to reduce flutter tendencies. 
The aerod ynamic balance can be a notched part of the control surface 
(Fig. 6.Sa), an overhung portion of the control surface (Fig. 6. Sb), or a combination of the two. The notched balance is not suitable for ailerons or for 
any surface in high-speed flight. The hinge axis should be no farther aft 
than about 20% of the average chord of the control surface. 
An old naval architects' approximation for balanced rudders can be used 
for a first layout of the hinge line of a balanced control surface, as follows: 
break the control surface into spanwise strip s. For a movable surface trailing 
a fixed surface, assume the center of pressure is at 0.33 of the movable chord 
length. For a movable surface in the freestream, as in the top of the rudder 
in Fig. 6.5, assume that the center of pressure is at 0.20 of the chord 
length. Add up the centers of pressure, weighted by the areas, to find an 
overall center of pressure and make sure that the hinge line is well ahead 
of it. Then, don't trust the result-use a more sophisticated analysis 
method as soon as possible.


<!-- p.164 -->

16 4 Ai rcraf t Design : A Conceptu al Ap proach 
a) b) Hi ngeline 
Notched or "ho rn" 
aer odyn amic bala nce 
Overh ung aer odyn amic ba lanc e 
Fig. 6.5 Aerody namic balan ce. 
The horizo ntal tail for a manually controlled aircraft is usually configured 
such that the elevator will have a hinge line perpen dicular to the aircraft centerline. This configuration permi ts connecting the left-and right-hand elevator surfaces with a torque tube, which reduces elevator flutter tendencies. 
Some aircraft have no separate elevator. Instead, the entire horizont al 
tail is moun ted on a spindle to provide variable tail incidence. This provides 
outstanding "elevator" effectiveness but is somewhat heavy. Some generalaviation aircraft use such an all- moving tail, but it is most common for supersonic aircra ft, where it can be used to trim the rearward shift in aerod ynamic 
center that occurs at supersonic speeds. 
A few aircra ft such as the F-23, SR-7 1, and North American F-10 7 have 
used all-mo ving vertical tails to increase control authority. 
What We've Lea rned 
We now know a better way to perform aircraft sizing and useful initial 
methods for sizing the fusela ge, tails, and control surfaces.
