# Raymer Ch.3 - Sizing from a Conceptual Sketch

*Converted from `Daniel P. Raymer - Aircraft Design_ A Conceptual Approach (2018, American Institute of Aeronautics and Astronautics Inc.) - libgen.li.pdf` by `tools/pdf_to_md.py`. Page markers are printed page numbers.*


<!-- p.27 -->

( 
-----Sizing from a 
Conceptual 
Sketch 
• "Sizi ng" is the first and most im portant calc ula tion in ai rcraft concep tual design . 
• Sizing finds how big and heavy the air plane must be to atta in the requi red mission 
range car rying the de sign pay load . 
• The drawing is based on the sizing resul ts, which ore used to find the dimensions of 
the engine , wings , tir es, fuel tanks, ta il s, etc. 
In trod uction 
S izing is the most impor tant calculation in aircraft design, more so than 
drag, or stress, or even cost (well, maybe not cost) . Sizing literally 
determines the size of the aircra ft, specifically the weight that the aircraft must be designed to so that it can perform its intended mission carrying 
its intended payload. An airplane that is too small just cannot carry enoug h 
fuel to do its jo b. How do we know? We know by sizing. 
To the rest of the aircraft communi ty-pilots, detail design engineers, 
mechanics, military officers-our process of aircraft sizing seems backwards. 
Most people would assume that we draw a new aircraft design and then 
determine how far it goes. We do it the other way around. We know how 
far it goes. It goes as far as the requiremen ts say it goes. What we do not 
know, and will find out by the sizing calcula tion, is how big to draw it. Its size. 
There are many levels of aircraft sizing procedure. The simplest level just 
adopts past histor y. For example, if you need an immedi ate estimate of the 
takeoff weight of an airplane to replace the Air Force F-15 fighter, use 
44,500 lb. That is the design weight of the F- 15 and is proba bly a fair 
number to start with, if you are in a hurry. 
27


<!-- p.28 -->

28 Air c raf t De si gn: A Conceptual Approa ch 
To get the "right" answer takes several years, many people, and lots of 
money. Desi gn requirements must be rigorous ly analyzed and then used to 
develop a number of candidate designs, each of which must be designed, analyzed, sized, optimized, and redesigned any number of times. The best of our 
candidates, sized to its minimum weight to perform the required mission, 
yields the right answer-we presume. 
Analysis techniques include all manner of compu ter code as well as correlations to wind-t unnel and other tests. Even with this extreme level of 
design sophistication, the actual airplane when flown will never exactly 
match predictions. 
In between these extremes of sizing procedure lie the methods used 
for most conce ptual design activities. As an introduction to the design 
process, this chapter presents a quick sizing method, which will allow you 
to estimate required takeoff weight from a con ceptual sketch and a sizing 
mission. 
The sizing method prese nted in this chapter is most accur ate when used 
for missions that do not include any combat or payload drops. Although 
admit tedly simplified, this method introduces all of the ess ential features of 
the most sophisticated sizing methods used by the major aerospace manufacturers. In a later chapter, the concepts introduced here will be expanded to a 
sizing method capable of handling all types of missions and with greater 
accur acy. 
Takeoff-Weigh t Buildup 
Desi gn takeoff gross weight is the total weight of the aircraft as it begins 
the mission for which it was designed. This is not necess arily the same as 
the maximum takeoff weight. Many military aircraft can be overloaded 
beyond design weight but will suffer a reduced maneu verability. Unless 
spe cifica lly mentioned, takeoff gross weight, or Wo, is assumed to be the 
design weight. 
Desi gn takeoff gross weight can be broken into crew weight, payload (or 
passen ger) weight, fuel weight, and the remaining (or "empt y") weight. The 
empty weight includes the structure, engines, landing gear, fixed equipment, 
avionics, and anything else not consid ered a part of crew, payload, or fuel. 
Equation (3. 1) summarizes the takeoff-weight buildup: 
Wo = Wcrew + Wpayload + Wfuel + Wempty (3 .1) 
The crew and payload weights are both known because they are given in 
the design requirements. The only unkno wns are the fuel weight and empty 
weight. However, they are both dependent on the total aircraft weight. Thus, 
an iterative process must be used for aircraft sizing. 
To simplify the calculation, both fuel and empty weights can be expressed 
as fractions of the total takeoff weight, that is, ( itj/ Wo) and ( We/ W0). Thus,


<!-- p.29 -->

Eq. (3.1) becomes 
CHAPTER 3 Sizi ng from a Con ceptu al Sk etch 29 
Wo = Wcrew + Wpayload + (-) Wo + (;-) Wo (3.2) 
This can be solved for Wo as follows: 
Wo - (-) Wo - (;-) Wo = Wcrew + Wpayload (3.3) 
Wcrew + Wpayload 
Wo = (3.4 ) 1- ( W1/ Wo) - ( We/ Wo) 
Now, Wo can be determined if (Wj / Wo) and (We/ Wo) can be estimated. 
These are described next. 
Em pty-We ight Esti mation 
After the aircraft has been drawn, the actual empty weight will be calculated by estimating and summing the weights of all of the componen ts of the 
aircraft. For now it can be estimated as a fraction (We/Wo) using simpler 
methods. The empty-weight fraction (We/ Wo) can be estimated statistically 
from historical trends as shown in Fig. 3.1, developed by the author from data 
taken from f6l and other sources. Empty-weight fractions vary from about 0.3 
to 0.7 and diminish with increasing total aircraft weight. 
As can be seen, the type of aircraft also has a strong effect, with flying 
boats having the highest empty-weight fractions and long- range military aircraft having the lowest. Flying boats are heavy because they need to carry 
extra weight for what amounts to a boat hull. Notice also that different 
types of aircra ft exhibit different slopes to the trend lines of empty-weight 
fraction vs takeoff weight. 
Table 3.1 presents statistical curve-fit equations for the trends shown in 
Fig. 3.1. Note that these are all exponen tial equations* based upon takeoff 
gross weight (pounds or kilogram s). The exponents are small negative 
numbers, which indicates that the empty-weight fractions decrease with 
increasing takeoff weight, as shown by the trend lines in Fig. 3.1. The differences in exponents for different types of aircraft reflect the different slopes 
of their trend lines and imply that some types of aircraft are more sens itive 
in sizing than others. 
A variable- sweep wing is heavier than a fixed wing and is accounted for at 
this initial stage of design by multiplying the empty-weight fraction as determined from the equations in Table 3.1 by about 1. 04. Crude, but not too far off. 
*More-properly called "Power Equations" being of form [constant times variable raised to a constant power] . A true Exponential Equation is of form [constant times constant raised to a variable 
power] . But the all-im portant constant power, the non- integer "C" term that defines the slo pe on 
Fig. 3.1, is called the "exponent" hence the common verbal transposition.


<!-- p.30 -->

30 Aircr af t Design- A Conceptu al Approach 
c 
0 ·.;::; u 
ro 
.:= 
...., 
..c 
°' 
'iii 
3: 
>c_ 
E 
UJ 
100 
Si zed ta keoff we ight W0 (kg) 
1000 10,000 100,000 
0.8 ----------------------0.7 
0.6 
0.5 
0.4 
100 1000 10 ,000 100,000 
Si zed ta keoff we ight W0 (lb) 
Fig. 3. 1 Em pty-weight fraction trends. 
1, 000,000 
Composi te materials such as graphite -epo xy are replacing aluminum in 
many new designs. There still haven't been eno ugh comp osite aircraft to 
develop good statistical equations just for them, so we usua lly fake it. We'll 
approximate the empty-weight fraction for a compos ite aircraft by multip lying 0.95 times the appropriate statistical empty-weight fraction calculated 
from the table. Later we'll analyze the weights in some detail, and learn if 
this was about right. 
It is possible to improve on these statistical numbers. The round-theworld Rutan Globa lFlyer has an empty weight fraction below 18%, but is 
little more than a flying fuel tank, designed and optimized solely for that 
mission and highly impractical for any normal applicat ion. For really-c razy 
numbers look at launch vehicl es. They often have empty weight fractions 
below 10%! Don' t expect that for an airplane with wings, landing gear, and 
other things that launch vehicles don't need (see Chapter 21). 
While Figure 3.1 and Table 3.1 can be used for initial estimat ion of the 
fracti on (We/W o), it's always better to develop your own trendline. Obtain


<!-- p.31 -->

CHAPTE R 3 Sizing from a Con ceptu al Sk etc h 31 
Table 3.1 Em pty Weight Fraction vs W 0 
We/ Wo = A W1i Kvs Sai lplane -unpo wered 0.8 6 
Sai lplane -powered 0 . 91 
Homebuil t-metal/wood 1 . 1 9 
Homebui lt-c ompos ite 1 . 15 
Gener al aviation -single engine 2 . 36 
Gener al aviation -twin engine 1 . 51 
Agricultural ai rcraft 0 . 74 
Twin turbopr op 0.96 
Flying boat 1 . 09 
Jet train er 1 . 59 
Jet figh ter 2 . 34 
Milita ry cargo /bomber 0 . 93 
Jet transpor t 1. 02 
UAV-Tac Reece & UCAV 1 . 67 
UAV-high al titude 2 . 75 
UAV-sma ll 0 . 97 
{A-metric} c 
{0 . 83} - 0 . 05 
{0 . 88} - 0 . 05 
{ l . ll } - 0 . 09 
{l . 07} - 0.0 9 
{2. 05} - 0 . 18 
{l .4 } - 0 . 10 
{0.72} - 0.Q 3 
{0 . 92} - 0 . 05 
{l . 05} - 0.0 5 
{l . 4 7} - 0 . 10 
{2 . 11 } - 0 . 13 
{0 . 88} - 0.o? 
{0 . 97} - 0 . 06 
{l .4 7} - 0 . 16 
{2. 39} - 0 . 18 
{0 . 93} - 0 .06 
Kvs = variable sweep constant = l .04 if variable sweep = l .00 if fixed sweep 
We and W o data for aircraft similar to your proj ect, plot the data onto Figure 
3.1, and draw a reasonable trendline with slope . similar to those shown. If 
using curve-fit software be careful-it may return a positive exponent 
depending upon the exact data you've fed it. Don't use that result-it isn't 
"real world" and the sizing equation will not converge. Instead force the software to use a negative number 'C' term like those in Table 3.1 and find the 
constant term with the lowest square error. This was actually the case for 
several of the classes of aircraft in Table 3.1. 
Fuel-Fr action Esti mation 
We also need to estima te the fuel available to perform the mission. Simple 
statistical methods will not work-we need to "fly" the aircraft over its 
required mission. Only part of the aircraft's fuel supply is available for performing the mission ("mission fuel"). The other fuel includes "reser ve fuel" 
as required by civil or military design specifications (most ly to allow for 
degradation of engine performance) and also includes "trapped fuel," 
which is the fuel that cannot be pumped out of the tanks. 
The required amount of mission fuel depends upon the mission to be 
flown, the aerod ynamics of the aircraft, and the engine's fuel consum ption. 
The aircraft weight during the mission affects the drag, so that the fuel 
used is a function of the aircraft weight.


<!-- p.32 -->

32 Ai rcraft De sign : A Conc eptual Appr oa ch 
As a first approximation, the fuel used can be consi dered to be propor tional to the aircraft weight, so that the fuel fraction ( WJ / Wo) is approximately independ ent of aircraft weight. Fuel fraction can be estimated based 
on the mission to be flown using approximations of the fuel consum ption 
and aerod ynamics. 
0 (II Mi ssion Profi les 
Typical mission profiles for various types of aircraft are shown in Fig. 3.2. 
The Simple Cruise mission is used for many transport and genera l-aviation 
designs, including hom ebuilts. The aircraft is sized to provide some required 
cruise range. 
For safety you would be wise to carry extra fuel in case your intended 
airport is closed, so a loiter of typically 20-30 min [at 10,000 ft {3048 m}] 
is added. Altern atively, additional range could be included, represent ing 
the distance to the nearest other airport or some fixed number of minutes 
of flight at cruise speed. [The FAA requires 30 min of additional cruise fuel 
for daytime flights under visual flight rules (VFR), and 45 min of fuel at 
night or under instrument cond itions (IFR) .] Under comme rcial IFR regulations, you also need fuel to fly to an alternate airport after loitering and 
attempting to land at your intended destinat ion. 
Takeoff 
Takeoff 
Cruise 
Simple 
cruise 
Cruise out 
Low- level 
strik e 
Takeoff 
Weight dr op 
Cruise 
Commer cial 
tran sport 
Cruise back 
Atte mp t to land 
Cruise out 
Air Weight dr op 
su periority 
Fig. 3.2 Typical mi ssion profi les for sizing .


<!-- p.33 -->

CHAP TER 3 Sizi ng from a Con ceptu al Ske tch 33 
The low-le vel strike mission includes "dash" segments that must be flown 
at just a few hundred feet off the ground. This is to impro ve the survivability 
of the aircraft as it approaches its target. Unfortunately, the aerod ynamic efficiency of an aircraft, expressed as lift-to- drag ratio (L/ D), is greatly reduced 
during low-le vel, hig h-speed flight, as is the engine efficie ncy. The aircraft 
may burn almost as much fuel during the low-level dash segment as it 
burns in the much-longer cruise segment. 
The typical air superio rity mission includes a cruise out, a combat consisting of either a certain number of turns or a certain number of minutes 
at maximum power, a weapons drop, a cruise back, and a loiter. The 
weapons drop refers to the firing of gun and missiles and is often left out 
of the sizing analys is to ensure that the aircraft has enoug h fuel to return 
safely if the weapons are not used. Note that the second cruise segment is 
identical to the first, indica ting that the aircraft must return to its base at 
the end of the mission. 
Many military missions include aerial refueling. The aircraft meets up 
with a tanker aircraft such as an Air Fo-ce KC- 135 and recei ves some quantity of fuel. This enables the aircraft to achieve far more range, but adds to the 
overall oper ating cost because a fleet of tanker aircraft must be dedicated to 
suppor ting the bombers. Analytically, this "rese ts the clock." The onloaded 
fuel brings the aircraft weight up to or even greater than the takeoff 
weight, so that the post-refuel segments are treated as an entire separate 
mission. 
Military missions are specified in MIL-STD-30 13 (previously MIL-C5011 A). Civilian missions are defined by the a.ircraft designers, provided 
that they follow the various requirements defined in the US Feder al Aviation 
Regulations (FARs) and/or European Certification Specifications (CSs). 
In addition to the mission profile, requirements will be established for a 
number of performance parameters such as takeoff distance, maneu verability, and climb rates. These are not addressed in the simplified sizing method 
of this chapter but will be discussed in detail later. 
*If J Mi ssion- Seg ment Weigh t Fractions 
For analysis, the various mission segments, or "legs," are numbered, with 
zero denot ing the start of the mission. Mission leg one is usua lly engine 
warm-up and takeoff for first-order sizing estimat ion. The remaining legs 
are seque ntially numbered. 
For example, in the simple cruise mission the legs could be numbered 
as 1) warm-up and takeoff , 2) climb, 3) cruise, 4) loiter, and 5) land 
(see the example mission at the end of this chapter) . 
In a similar fashion, the aircraft weight at each part of the mission can be 
numbered. Thus, Wo is the beginning weight (takeoff gross weight) . 
For the simple cruise mission, W1 would be the weight at the end of the 
first mission-se gment, which is the warm-up and takeoff. W2 would be the


<!-- p.34 -->

34 Air craft Desig n: A Conceptu al Ap proa ch 
aircraft weight at the end of the climb. W3 would be the weight after cruise, 
and W4 after loiter. Finally, Ws would be the weight at the end of the landing 
segment, which is also the end of the total mission. 
During each mission segment, the aircraft loses weight by burning fuel. 
(Remember that our simple sizing method doesn't per mit missions involving 
a payload drop.) The aircraft weight at the end of a mission segment divided 
by its weight at the beginning of that segment is called the "mission segment 
weight fraction." This will be the basis for estimating the required fuel fraction for initial sizing. 
For any mission segment i, the mission segment weight fraction can be 
expressed as (Wi/Wi-1). If these weight fractions can be estimated for all 
of the mission legs, they can be multiplied together to find the ratio of the 
aircraft weight at the end of the total mission, Wx (assuming x segments 
altogether) divided by the initial weight Wo. This ratio Wx/Wo can then be 
used to calculate the total fuel fraction required. 
These mission- segment weight fractions can be estimated by a variety of 
methods. For our simplified form of initial sizing, the types of mission leg will 
be limited to warm-up and takeoff , climb, cruise, loiter, and land. As mentioned earlier, mission legs involving comba t, payload drop, and refuel are 
not permitted in this simplified sizing method but will be discussed in a 
later chapter. 
The warm-up, takeoff, and landing weight fractions can be estimated historic ally. Table 3.2 gives typical historical values for initial sizing. These 
values can vary somewhat depend ing on aircraft type, but the averaged 
values given in the table are reasona ble for initial sizing. 
In our simple sizing method we ignore descen t, assuming that the cruise 
ends with a descent and that the distance traveled during descent is part of 
the cruise range . 
Cruis e-s egment mission weight fractions can be found using the Breguet 
range equation (derived in Chapter 17): 
or 
Wi -RC 
-- = exp Wi-l V(L/D) 
Table 3.2 His torica l Mi ssio n-Seg ment Weight Fractions 
Mission Segment 
Warmup and takeoff 
Climb 
Landing 
(W;/W ;-1) 
0.970 
0.985 
0.9 95 
(3 .5) 
(3.6 )


<!-- p.35 -->

CHAPTER 3 Sizi ng from a Con ceptu al Sk etc h 35 
where 
R = range (ft or m) 
C = specific fuel consu mption (see following section) 
V = velocity (ft/s or m/s) 
L/ D = lift-to- drag ratio 
Loiter weight fractions are found from the endurance equation (also 
derived in Chapter 17): 
or 
Wi -EC -- = exp --Wi-1 L/D 
where E = endurance or loiter time. . 
(3 .7 ) 
(3.8 ) 
(Note: It is very important to use cons istent units! Convert all values to 
feet-lb -s, or to m-k-s. Also note that C and L/ D vary with speed and altitude. 
Furthermore, C varies with throttle setting, and L / D varies with aircraft 
weight. These will be discussed in detail in later chapte rs.) 
*lfl Specific Fuel Consu mption 
Specific fuel consumption (SFC or simply C) is the rate of fuel consumption divided by the resulting thrust. For jet engines, specific fuel consumption 
is measured in fuel mass flow per hour per unit thrust force. In British {fps} 
units, SFC is in pou nds of fuel per hour, per pound of thrust. We sometimes 
"cancel" the pounds and say "per hour" (1 /h) as the units-but it is just a joke! 
In metric terms we use the more reasonable mg/Ns. Figure 3.3 shows trend 
lines of SFC vs Mach number. 
Propeller engine SFC is norma lly given as Cbhp' the pounds of fuel per 
hour to produce one horsepo wer at the propeller shaft (or one brake horsepower: bhp = 550 ft-lb/s). In metric, power SFC is given in mg/W-s (mg/J, 
or in µ,g/J to make "nice" numbers) . 
A propeller thrust SFC equivalent to the jet-engine SFC can be calculated. 
The engine produces thrust via the propeller, which has an efficiency 1/p 
defined as thrust power produced by the propeller (thrust times veloc ity) 
divided by the engine power provided to the propeller [Eq. (3.9 )]. The 550 
term converts horsep ower to power in British units and assumes that V is 
in feet per second. 
TV TV 7/p = p- = 550 hp {fps} (3 .9)


<!-- p.36 -->

36 Ai rcraft Design : A Conceptual Appr oach 
u 
u.. 
Vl 
..._, 
c 
CL> 
- 1 
:J 
CT LLJ 
60 
"' 
z 
40 0, 
E 
20 
o -------------------- o 
0 2 3 4 5 
Mach numb er 
Fig. 3.3 Specific fuel cons ump tion trends (at typical cruise al titude s) . 
Equation (3. 10) shows the derivation of the equivalent-t hrust SFC for 
a prope ller- driven aircraft. Note that for a propeller aircraft, the thrust and 
the SFC are a function of the flight velocity. For a typical aircraft with a 
propeller efficie ncy of about 0.8, 1 hp equals one pound of thrust at about 
440 ft/s, or about 260 kt {484 km/h} . 
W1/time V V C = = Cpower - = Cbhp --thrust Y'/ P 550 Y'/ P 
{fps} (3. 10) 
Table 3.3 provides typical SFC values for jet engines, while Table 3.4 
provides typical Cbhp values for propeller engines. Typically, one can 
assume hp = 0.8 except for a fixed-pi tch propeller during loiter, where 
Y'/p = 0.7. These can be used for rough initial sizing. In later chapters more 
detailed proced ures for calcula ting these values, which change as a function 
of altitude, velocity, and power setting, will be presented. 
Table 3.3 Specific Fuel Consu mption, c 
Typical Jet SFCs: l /hr {m g/N s} Cru ise Loiter 
Pur e turbojet 
Low-bypass turbofa n 
Hig h-bypass turbof an 
0.9 {25 .5} 
0.8 {22 .7} 
0.5 {1 4. l } 
0.8 {22 .7 } 
0.7 {1 9.8} 
0.4 {1 1 .3}


<!-- p.37 -->

CHAPTER 3 Sizing from a Con ceptu al Sk etc h 37 
Table 3.4 Propell er-Specific Fuel Cons ump tio n, Cbhp 
-Propel ler: C = Cpower V/71µ = Cbhp V/( 55071µ) 
Typi cal cbhp: lb /hr/bhp {mg /W-s} 
Piston-prop (fixed pit ch) 
Pisto n-prop (variable pitch) 
Turb oprop 
#Ill L/D Estimation 
-0.4 {0 .068} 
0.4 {0 .068} 
0.5 {0. 085} 
0.5 {0. 085} 
0.5 {0. 085} 
0.6 {0 .101} 
The remaining unknown in both range and loiter equations is the 
L/ D, or lift- to- drag ratio, which is a measure of the design's overall aero dynamic efficienc y. Unlike the parameters just estimated, the L/ D is 
highly dependent upon the configuration arrangement. At subsonic 
speeds L / D is most directly affected by two aspects of the design: wing 
span and wetted area. 
In level flight, the lift is known, It must equa l the aircraft weight. Thus, 
L/D is solely dependent upon drag. 
The drag at subsonic speeds is composed of two parts. Induced drag is 
the drag caused by the generation of lift. This is prim arily a function of the 
wing span. 
Zero- lift, or "parasite" drag is the drag that is not related to lift. This is 
primarily skin-friction drag, and as such is direct ly propor tional to the 
total surface area of the aircraft exposed ("wetted ") to the air. 
The aspect ratio of the wing has historic ally been used as the primary 
indicator of wing efficie ncy. Aspect ratio is defined as the square of the 
wing span divided by the wing reference area. For a rectangular wing the 
aspect ratio is simply the span divided by chord. 
Aspect ratios range from under 1 for reentry lifting bodies to over 30 for 
sailplanes. Typical values range between 3 and 8. For initial design purposes, 
aspect ratio can be selected from historical data. For final determination of 
the best aspect ratio, a trade study as discussed in Chapter 19 should 
be conducted. 
Aspect ratio could be used to estimate subsonic lift-to- drag ratio but for 
one major problem. L/D depends upon both the induced and parasitic drags. 
The induced drag depends largely upon the wing span, as defined by aspect 
ratio. The parasite drag depends on the aircraft's total wetted area, not just 
the wing area as expressed by aspect ratio. Two airplanes with similar span 
and total wetted area will have a similar lift- to- drag ratio, even if they look 
compl etely different and their aspect ratios are dissimilar. 
Figure 3.4 shows two widely different aircraft concepts, developed to 
illustrate this. Both are large airliners. (Data are metric, but actual 
numbers don't matter here .) By design, both have exactly the same wing 
span and the same total internal volume. The aspect ratio of the delta


<!-- p.38 -->

38 Air craf t Des ign: A Conceptual Approach 
s,.r 
swetted 
Span 
Swe/Srer 
Aspect ratio 
Wetted asp ect ratio 
L/Dmax 
In ternal volume 
Conv entional 
393 
244 1 
55 
6.2 
7.7 
1. 2 
15 
210 0 
Fig. 3.4 Does aspect ratio predic t drag? 
Delta wina 
10 00 
215 6 
55 
2.2 
3 
1 .4 
16 
210 0 
wing is lower, not because of a reduced span, but because of an increased 
chord length. 
The conventional design has an aspect ratio typical for Boeing and Airbus 
airliners, and attains a typical L/ Dmax of 15. The delta design has an aspect 
ratio of only 3, yet it attains the same L / D-e ven better .* 
The explanation for this curious outcome lies in the actual drivers of L / D. 
Both aircraft have about the same wing span, and both have about the same 
wetted areas, so both have about the same L/ D. The aspect ratio of the conventional design is higher not because of a greater wing span, but because of a 
smaller wing area. However, this reduced wing area is offset by the wetted 
area of the fuselage, nacelles, and tails. 
This is illustrated by the ratios of wetted area to wing reference area 
(Swet/Sref). While the delta design has a total wetted area of just over two 
times the wing area, the conventional design has a wetted area of over six 
times the wing area. 
This wetted-area ratio can be used, along with aspect ratio, for an early 
estimate of L/D. Figure 3.6 shows a spectrum of design approaches and 
the result ing wetted-area ratios. 
L / D depends primar ily on the wing span and the wetted area. This 
suggests a new parameter, the wetted aspect ratio, which is defined as the 
* Earlier editions showed the B-47 and Avro Vulcan to illustrate this effect. These notional designs 
show it better because they have exactly the same span and volume. Design and calculations were 
done in RDS-P rofessional, with rendering in RhinoCAD.


<!-- p.39 -->

CHAP TER 3 Sizi ng from a Con ceptu al Sk etc h 39 
wing span squared divided by the total aircraft wetted area [Eq. (3 .11)]. This is 
very similar to the aspect ratio except that it considers total wetted area 
instead of wing reference area. Because the wing geomet ric aspect ratio is 
the square of wing span divided by wing reference area, the wetted aspect 
ratio can be found to equal the wing geometric aspect ratio divided by the 
wetted-area ratio (Swet/Sref) as defined above. 
b2 A Awetted = ---= -----Swetted ( Swet/ Sref) (3 .11 ) 
Figure 3.5 plots maximum L/D for a number of aircraft vs the wetted 
aspect ratio and shows clear trend lines for jet, prop, and fixed- gear prop aircraft. These historical data are surprisin gly useful as an early L / D predictor, 
and for double- checking the results obtained from detailed aerod ynamic 
calculat ions. 
The trend lines of Fig. 3.5 could be extended far to the right for 
high-aspect- ratio designs. The Globa l Hawk has a wetted aspect ratio of 
6.8 and attains an L/ Dmax of over 35. High-performance sailplanes have 
wetted aspect ratios as high as 12 and see a maximum L/D of 50 or more. 
20 
18 
16 
14 
- 12 
E 
-...] 10 
8 
6 
4 
2 
0 
Blue 
Jets at Mach 1. 15 
(poor correl ation) 
0.2 0.4 0.6 0.8 1.0 1.2 1.4 1.6 1.8 2.0 2.2 2 .4 
Wetted asp ect ratio = b21Swet = A/(SwetfSref) 
Fig. 3.5 Maxi mum li ft-to-d rag ra tio trends.


<!-- p.40 -->

40 Ai rc raft Desig n: A Concept ual Appr oach 
Empirical values to extend this graph are (5,32) and (1 0,45), based on a 
number of sailplanes and high aspect ratio UAVs. 
There is an equivalent technique going back at least to the 1940s that 
plots L / D vs the square root of wetted aspect ratio. The term "wetted 
aspect ratio" was not in use back then, so the horizon tal axis is given as 
sqrt[A/(Swet/Sref)]. This format is useful because the data become fairly 
linear, but the plot ting in Fig. 3.5 is more relevant to the actual physics of 
drag. Either format should give the same answer. 
The line arity of the data makes a usefu l equation for predicting L / Dmax 
[Eq. (3. 12 )], or you can direct ly use Fig. 3.5. 
where 
L A --= K10 J Awetted = K10 
Dmax ( Swet/ Sref) 
Kw = 15 .5 for civil jets 
8 
2 
14 for military jets 
11 for retractable prop aircraft 
9 for nonretractable prop aircraft 
13 for high-a spect- ratio aircraft 
15 for sailplanes 
Avro Vu lcan 
* Including ca nar d ar ea 
Fig. 3.6 Wetted area ratios. 
Boei ng 747 
(3 .12 )


<!-- p.41 -->

CH APTE R 3 Sizi ng from a Conc eptu al Sk etc h 41 
How do you estimate wetted aspect ratio before you've made the configuration design layout? Aspect ratio is something that you select (see 
Chapter 4). Wetted area ratio can be "eyeball" estimated from the 
sketch, using Fig. 3.6 for guida nce. The wetted aspect ratio can then 
be calculated as the wing aspect ratio divided by the wetted-area ratio. 
Equation (3.12 ) or Fig. 3.5 can then be used to estima te the maximum 
L/D. 
Drag varies with altitude and veloc ity. For any altitude there is a velocity 
that maximizes L/ D. To maximize cruise or loiter efficiency, the aircraft 
should fly at approxima tely the velocity for maximum L/D. 
For reasons that will be derived later, the most efficient loiter for a jet aircraft occurs exactly at the veloc ity for maximum L / D, but the most efficient 
loiter speed for a propeller aircraft occurs at a slower veloc ity that yields an 
L/D of 86.6% of the maximum L/D. 
Similarly, the most efficient cruise velocity for a propeller aircraft occurs 
at the velocity yielding maximum L / D, whereas the most efficient cruise 
for a jet aircraft occurs at a slightly ,higher velocit y yielding an L/ D of 
86.6% of the maximum L / D: 
- Cruise Loiter 
Jet 0.86 6 L/Dmax L/Dmax 
Prop L / Dmax 0.866 L / Dmax 
For initial slZlng, these percent ages can · be multiplied times the 
maximum L/D as estimated using Fig. 3.5 to determine the L/D for cruise 
and loiter. 
*ff.J Fuel-Fr acti on Esti mation 
Using historical values from Table 3.2 and the equations for cruise and 
loiter segments, the mission- segment weight fractions can now be estimated. 
By multiplying them together, the total mission weight fraction Wx/ Wo can 
be calculated. 
Because this simplified sizing method does not allow mission segments 
involving payload drops, all weight lost during the mission must be due to 
fuel usage. The mission fuel fraction must therefore 
be equal to (1 - Wx/ Wo). If you assume, typically, a 
6% allowance for reser ve and trapped fuel, the total 
fuel fraction can be estimated as in Eq. (3.13 ): 
Sizing: the most 
important 
calculation in 
aircraft design. 
(3 .1 3)


<!-- p.42 -->

42 Air craf t De si gn: A Conceptual Appr oach 
Takeoff-We igh t Ca lcula tion 
Using the fuel fraction found with Eq. (3.13) and the statistical emptyweight equation selected from Table 3.1, the takeoff gross weight can be 
found iteratively from Eq. (3.4). This is done by guessing the takeoff 
gross weight, calculating the statistical empty-weight fraction, and then calculating the takeoff gross weight. If the result doesn't match the guess 
value, a value between the two is used as the next guess. This will 
usua lly converge in just a few iteratio ns. This first-order sizing process is 
diagrammed in Fig. 3.7. 
Design Example: ASW Ai rcraft 
As a design and sizing example, Fig. 3.8 illustrates the mission require ment for a hypothetical antisubmarine warfare (ASW) aircraft. The key 
requirement is the abili ty to loiter for 3 hr at a distance of 15 00 n miles 
{2778 km} from the takeoff point. While loitering on- station, this type of aircraft uses sop histicated electronic equipment to detect and track submarines. 
For the sizing example, this equipment is assumed to weigh 10,000 lb 
{4536 kg} . Also, a four-man crew is required, totaling 800 lb {363 kg} . The 
aircraft must cruise at 0.6 Mach number. 
Desi gn objectives & sizing mi ssion 
Aspect ratio selection 
Engine SFC data 
W0 gu ess 
--.. ... W.el
•
W.
•0•e-q u•a-ti.on----•-----W,
•0•eq•u•a•tion 
.. _.J Iterate 
No weig ht dr ops permit ted 
Assu mes "rubber engi ne" Calcu lated W0 & Wtuel 
Fig. 3.7 Fi rst-order design method .


<!-- p.43 -->

Warm up & ta keoff 
CHAPTER 3 Sizi ng from a Con ceptu al Sk etc h 43 
Crew weight = 800 lb 
Avionic s payload = 10 ,000 lb 
Fig. 3.8 Sa mple mi ssion profi le. 
7 
mf I Conc eptual Sketche s 
Figure 3.9 shows four conceptual approaches consi dered by the designer 
in response to these mission requirements. Concept one is the conventional 
approach, look ing much like the Lockheed S-3A that curre ntly performs a 
similar mission. The low horizo ntal tail posi tion shown in solid line 
would offer the lightest structure, but may place the tail in the exhaust 
stream of the engines, so other positions for t-e horizo ntal tail are shown 
in dotted lines. 
The second concept is much like the first except for the engine loca tion. 
Here the engines are shown mounted over the wing. This provides extra lift 
1- Conventi onal 2-0ver -wi ng nacelles 
0 
3-Ca na rd, low wing 4-Ca nar d, high wing 
Fig. 3.9 ASW concept sketches .


<!-- p.44 -->

44 Airc raft De sign : A Conceptual Approach 
due to the exhaust over the wings and also provides greater ground clearance 
for the engines, which reduces the tendency of the jet engines to suck up 
debris. The disadvantage of this concept is the difficu lty in reaching the 
engines for maintenance work. Also, wing top engines often suffer from 
interference drag. 
Conce pts three and four explore the canarded approach. Canards offer 
the potential for reduced trim drag and may provide a wider allowable 
range for the center of gravity. However, it is often difficult to put large 
flaps on the wing, so the wing must be oversized. 
In concept three, the wing is low and the engines are mounted over the 
wing as in concept two. This would allow the main landing gear to be 
stowed in the wing root, probably saving some weight and drag. In concept 
four, the wing is high with the engines mounted below. This last approach 
offers better access to the engines. 
The designer would be wise to take all four of these concepts, and maybe 
a few more, on to the next step of initial sizing and subseq uent design 
layout. For this textbook example, only the last approach will be illustrated. 
Figure 3.10 is a conc eptual sketch prepared, in more detail, for the selected 
conce pt. Note the locations indicated for the landing-gear stowage, crew 
station, and fuel tanks. 
This points out a common problem with canard aircra ft, the fuel tank 
loca tions. The fuel tanks should be placed so that the fuel is evenly distributed about the aircraft center of gravity (est imated loca tion shown by the circle 
with two quarters shaded) . This is necessa ry so that the aircraft when loaded 
Fig. 3. 10 Comple ted ASW sketch.


<!-- p.45 -->

CHAP TER 3 Sizi ng from a Conc eptu al Sk etc h 45 
has nearly the same center of gravity as when its fuel is almost gone. However, 
the wing is located aft of the center of gravity whenever a canard is used, so 
that the fuel loca ted in the wing is also aft of the center of gravity. 
One so lution to this problem would be to add fuel tanks in the fusel age, 
forward of the center of gravity. This would increase the risk of fire in the 
fuselage during an accident and is forbidden in commercial aircraft. 
Although this example is a military aircraft, fire saf ety should always be 
considered. 
Another solution, shown on the sketch, is to add a wing strake full of fuel. 
This solution is seen on the Beech Starship among others. The strakes do add 
to the aircraft wetted area, which reduces cruise aerodynamic efficiency. 
This example serves to illustrate an important principle of aircraft 
design- there is no such thing as a free lunch! All aircraft design entails a 
series of tradeoffs. The canard offers lower trim drag, but may requir e a 
larger wing and a greater wetted area. The only way to determine whether 
a canard is a good idea for this or any aircraft is to design several aircraft, 
one with and one without a canard. T_his type of trade study comprises the 
majority of the design effort during the conce ptual design process. 
*UI L/D Esti mation 
For initial sizing of the fourth conce pt, a wing aspect ratio of 10 was 
selected. With the area of the wing and canard both included, this is equivalent to a combined aspect ratio of about 7. 
Comparing the sketch of Fig. 3.10 to the e-amples of Fig. 3.6, it would 
appear that the wetted area ratio (Swet/Sref) is about 5.5. This yields a 
wetted aspect ratio of 1. 27 (i.e., 7 /5.5). 
For a wetted aspect ratio of 1. 27, Fig. 3.5 indicates that a maximum 
lift-to-d rag ratio of about 16 would be expected. This value, obtained from 
an initial sketch and the selected aspect ratio, can now be used for 
initial sizing. 
Because this is a jet aircra ft, the maximum L/D is used for loiter calculations. For cruise, a value of 0.866 times the maximum L/D, or about 
13 .9, is used. 
*QI Takeoff-We igh t Sizing 
From Table 3.3, initial values for SFC are obtained. For a subsonic aircraft 
the best SFC values are obtained with high-by pass turbofans, which have 
typical values of about 0.5 for cruise and 0.4 for loiter. 
Table 3.1 does not provide an equation for statistically estimating the 
empty weight fraction of an antisubmarine aircraft. However, such an aircraft 
is basica lly designed for subsonic cruise efficienc y so that the equation for 
military cargo /bomber can be used. The extensive ASW avionics would 
not be included in that equation, so it is treated as a separate payload weight.


<!-- p.46 -->

46 Air craf t Desig n: A Concept ual Appr oach 
Box 3. 1 ASW Sizing Calcu lations 
Mission-S egment Weight Fractions (British Units) 
1. Warmup and takeoff 
2. Climb 
3. Cruise 
Wi/Wo = 0.97 
W2/W1 = 0.985 
R = 15 00 nmi. = 9, 11 4,000 ft 
C = 0.5 I/hr = 0.000 1389 1/s 
(Table 3.2) 
(Table 3.2) 
V = 0.6 M x (994.8 ft/s) = 5 96.9 ft/s 
L/D = 16 x 0.866 = 13.9 
W3/ W2 = e{ -RC/VL/D} = e- 0.1 53 = 0.858 
4. Loiter E = 3 hr = 10,800 s 
C = 0.4 1/hr = 0.0001 111 1/s 
L/D = 16 
W4/ W3 = e{- EC/L/D} = e- 0.075 = 0.9277 
5. Cruise (same as 3) 
6. Loiter 
7. Land 
W5/W4 = 0.858 
E = t hr = 1200 s 
C = 0.0001111 1/s 
L/D = 16 
W6/ W 5 = e- 0.008 3 = 0. 9917 
W?/ W6 = 0.995 (Table 3.2) 
W?/Wo = (0.97)(0.985) (0. 858) (0.9277) (0.858) (0.9917) (0.995) = 0.6 441 
W1/Wo = 1. 06 (1 - 0.6441) = 0.3773 
We/Wo = 0.93 wo0·07 (Ta ble 3.1) 
Wo = 
10,800 
We 1 - 0. 3773 --Wo 
llmil111lllllm50,000 0.43 6 1 
60.000 0.43 05 
56,000 0.4 326 
56,500 0.4324 
56,700 0.4 322 
21 .803 
25,832 
24.227 
24.428 
24, 508 
W0, calcu lated 
57.863 
56, 19 8 
56,81 4 
56,733 
56, 702 
Box 3.1 gives the calculations for sizing this exampl e. Note the effort to 
ensure cons istent dimensions, including the conversion of cruise velocity 
(Mach 0.6) to ft/ s by assuming a typical cruise altitude of 30,0 00 ft 
{914 4 m}. At this altitude the speed of sound is 994.8 ft/s {303.2 m/s} (see 
Appe ndix B). 
The calculations in Box 3.1 indicate a takeoff gross weight of 56,702 lb 
{25,720 kg} . Although these calculations are based upon crude estimates of 
aerod ynamics, weights, and propulsion parameters, the actual takeoff gross 
weight of the Lockheed S-3 A, as quoted in[6l , is 52,539 lb {23, 831 kg} .


<!-- p.47 -->

-0 
2 
::> 
u 
-;;; u 
; 
55,000 
50,000 
45,000 
CHAPTER 3 Sizi ng from a Conc ep tu al Sk etc h 47 
Sizing gr aphans wer is 
at inter sec tion 
y 40,000 -+"'--------,------------,-----.-------1 
40,000 45,000 50,000 
W0 gu ess 
55,0 00 
Fig. 3.1 1 Graphical sizing method for ASW example. 
60,000 
While strict accuracy should not be expected, this simple sizing method will 
usually yield an answer in the "right ballpark." 
Figure 3. 11 illustrates an alternative way to size the aircraft, by a graphical 
method. Here a number of guesses of Wo that bound the likely solution have 
been made. Rather than attempt to iterate to the correct answer as just done, 
we simply graph these answers with Wo guess OJ! the horizontal axis and Wo 
calculated on the vertical axis. A 45-d eg line from the origin represents where 
the guess equals the calculated value, so that the intersection of this line with 
the line of the answers is the solution. 
An Excel ™ spreadsheet of this sizing example illustrating both methods 
is available at the author's website, www.aircraft desig n.com. 
#Uj Trade Stud ies 
An impo rtant part of concept ual design is the evaluation and refinement, 
with the customer, of the design requirements. In the ASW design example, the required range of 15 00 n miles (each way) is prob ably less than the 
customer would really like. A range trade can be ca lcula ted to determine 
the increase in design takeoff gross weight if the required range is increased. 
This is done by recalcula ting the weight fractions for the cruise mission 
segments, using arbitrarily selected ranges. For example, instead of the required 15 00 n miles, we will calculate the cruise weight fractions using 1000 
and 2000 n miles and will size the aircraft separately for each of those ranges. 
These calculations are shown in Box 3.2, and the results are plotted in Fig. 3.12. 
In a similar fashion, a "payload trade" can be made. The missi on-se gment 
weight fractions and fuel fraction are unchanged, but the numerator of the


<!-- p.48 -->

48 Air c raf t Design: A Concep tual Appro ach 
Box 3.2 Ra nge Trade 
1000 n miles Range 
W3/W2 = Ws/W4 = e-o.io 2o = 0 .9030 
W?f Wo = 0.71 32 
Wf /Wo = 1.0 6 (1 - 0.71 32) = 0 .3040 
10,800 Wo = ------We 1- 0.3040 - ., •. !i!Jijiiifi 
50,000 0.436 1 
40,000 
42 ,000 
42,400 
42,370 
2000 n miles Range 
0. 4429 
0.44 14 
0.4 41 1 
0.44 12 
Wo 
21 ,8 03 
17 ,71 7 
18 ,5 40 
18 ,7 04 
18 ,692 
W0, calcu lated 
41 ,544 
42,670 
42, 41 7 
42, 369 
42,372 
W3/ W2 = W5/ W4 = e-0·2040 = 0.815 4 
W7 I Wo = 0.5 816 
W1/ Wo = 0 .4435 
10,800 Wo = ------ We 1- 0.4435 - -Wo 
•i•!i[i{j 
50,000 
80,000 
80,200 
80,2 10 
80,2 18 
0.436 1 
0.4220 
0.4 219 
0.42 19 
0.4 219 
21 ,8 03 
33,756 
33,835 
33,839 
33,842 
W0, calcul ated 
89, 671 
80,265 
80,22 1 
80,2 19 
80,2 17 
sizing equation (3.4) is paramet rically varied by assuming different payload 
weights . The given payload requirement is 10 ,000 lb of avionics equipment. 
Box 3.3 shows the sizing calculations assuming payload weights of 5000 
and 20,000 lb. The results are plotted in Fig. 3.13. 
The statistical empty-weight equation used here for sizing was based 
upon existing military cargo and bomber aircraft, wh ich are all of aluminum


<!-- p.49 -->

CHAPT E R 3 Sizi ng from a Con ceptu al Sk etc h 49 
70,000 
- 60,000 
50,000 
40,000 +----------------------< 
1000 1200 1400 1600 
Range 
Fig. 3. 12 Range trade. 
Box 3.3 Payload Trade 
5800 
Payload = 5000 lb; Wo = 
We 1 -0. 3773 -Wo 
18 00 
M\M!i!i{jiifid W0, calcula ted 
50,000 0.43 61 21 ,803 
14 ,397 32,00 0 
33,000 
33,300 
33,320 
0.4499 
0. 4489 1 4,81 5 
0. 4487 14 ,940 
0.4486 14 , 949 
15 ,80 0 
Payload = 15 ,000 lb; Wo = 
We 1- 0. 3773 -Wo 
31 ,07 4 
33,563 
33,376 
33,3 21 
33,31 8 
W0, calcula ted 
84,651 
75,000 0.4 239 3 1 ,790 79,456 
78,000 0.4227 32,97 1 78, 994 
78,800 0.4 224 33,285 78, 875 
78,865 0.4224 33, 31 1 78,866 
2000


<!-- p.50 -->

50 Ai rc raf t De sign : A Conceptual Approach 
80,000 --------------------60,000 
40,000 
20,000 +--------------------__, 
5000 7000 9000 11 ,000 13 ,000 15 ,000 
Payload 
Fig. 3. 13 Payload trade. 
construction. The preceding takeoff gross weight calculations have thus 
implic itly assumed that the new aircraft would also be built of aluminum. 
To determine the effect of building the aircraft out of composite 
materials, the designer must adjust the empty-weight equat ion. As already 
mentioned, this can be approximated in the early stages of design by 
taking 95% of the empty-weight fraction obtained for a metal aircraft. The 
calculations for resizing the aircraft using compo site materials are shown 
in Box 3.4. 
Box 3.4 Com posite Materi al Trade 
We/ Wo = (0.95) (0.93 W0-0·07) = 0.88 35 w0-0·07 
10,800 Wo = 
We 1- 0.3773 --Wo 
MJM!i!@jiiifi 
50, 000 0.414 3 
51 ,000 0.41 37 
51 ,5 00 0.41 34 
51, 550 0.413 4 
20,7 13 
21 ,098 
21 ,291 
21 ,31 0 
51, 585 0. 413 4 21 ,323 
W0, calcu lated 
51, 81 0 
51 ,668 
51 ,598 
51 ,59 1 
51 ,587


<!-- p.51 -->

CHAPTER 3 Sizi ng fro m a Con ceptu al Sk etc h 51 
The use of compo site materials reduces the takeoff gross weight from 
56,7 02 lb {25,720 kg} to only 51 ,585 lb {23,399 kg} , yet the aircraft can still 
perform the same mission. This is a 9% takeoff -weight savings, resulting 
from only a 5% empt y-weight saving. 
This result sounds erroneous, but is actu ally typical of the "leverage" 
effect of the sizing equatio n. Unfortunately, this works both ways. If the 
empty weight creeps up during the detail -design process, it will require a 
more-t han-propor tional increase in takeoff gross weight to maintain the 
capabi lity to perform the sizing mission. Thus, it is crucial that realistic estimates of empty weight be used during ea rly conce ptual des ign, and that the 
weight be strict ly controlled during later stages of design. 
There are many trade studies that could be conducted other than range, 
payload , and material. Methods for trade studies are discussed in detail in 
Chapte r 19. 
The remainder of the book presen ts better methods for design, analysis, 
sizing, and trade studies, building on the concepts just given. In this chapter a 
conceptual sketch was made, but no guidance was provided as to how to 
make the sketch or why different features may be good or bad. Following 
chapters address these issues and illustrate how to develop a complete threeview drawing for analysis. Then more so phisticated methods of analys is, 
sizing, and trade studies will be pr ovided. 
What We've Lear ned 
We've learned a quick way to perform initial sizing and a param etric way to do 
trade studie s.


<!-- p.52 -->

52 Airc raft De si gn· A Concept ual Approa ch
