# Raymer Ch.10 - Propulsion and Fuel System Integration

*Converted from `Daniel P. Raymer - Aircraft Design_ A Conceptual Approach (2018, American Institute of Aeronautics and Astronautics Inc.) - libgen.li.pdf` by `tools/pdf_to_md.py`. Page markers are printed page numbers.*


<!-- p.275 -->

Propulsion and 
Fuel System 
Integration 
• Propulsion mu st be done ri ght on that first lay out or the des ign doe sn' t rea ll y work, 
the calcul ated th rust and drag are proba bly wrong, and the ai rcraft weight will lik ely 
go up. 
• Consid erati ons: engine size. locati on, and geom etry, motor mount s. air int ake 
location and size. prop el ler diame te r. and fuel ta nk loca tion and volum e. 
• These ar e exciti ng time s for air craf t propulsion with the em ergen ce of 
envir on mental ly-fri end ly fu els for tr aditional engi nes, ·and the potent ial for alt ernativ e 
pro pulsion methods in clud ing hydrog en, nu clear , and mor e. 
In troduc tion 
G liders are fun, but they aren't very useful. Practical airplanes need 
thrust, and providing that thrust has a large effect on the aircraft 
conc eptual design layout. Whatever the type, the engine will be 
one of the largest single items in weight and size. Along with its assoc iated 
hardware, the integrat ion of the engine will drive the configuration arrangement more than almost anything else. 
To develop the propulsion system layout, the dimensions and installation 
require ments of the engine must be known. The geometry of its supporting 
equipment (inlet ducts, nozzles, propellers) must be obtained or calculated. 
Decisions must be made as to the location and arrangement of the engine 
and its inlet duct or propeller. The fuel system must be defined, especially 
the fuel tanks that carry such a large fraction of the total aircraft weight. 
This chapter treats the integration and layout of the propulsion system 
into the overall vehicle design, and includes discussions of alternative fuels 
and more. The actual calculation of installed propulsion performance is 
275


<!-- p.276 -->

276 Airc raft De sign: A Con cept ual Approach 
covered in Chapter 13. Ele ctric aircraft technolog y, design, and analysis is 
presented in Chapter 20. 
Propu lsion Overvie w and Sel ection 
Most forms of aircraft propulsion work by taking an oncoming massflow 
of air and acce lerating it to the rear. The actual thrust comes from mome ntum transfer-air backwards, airplane forward s. The various forms of 
propulsion differ in how they make this happen. Propellers use blades that 
act like little rotating wings, with downwash pushing the air to the rear. 
The power to spin the propeller usually comes from a fuel-bur ning engine 
or an electric motor. Jet engines take in the air, raise its pressure, then use 
the geom etry of a nozzle to get it to accel erate to the rear. For jets it is 
usually the com bustion of a fuel that powers the pressure rise, but not always. 
Only rockets are really different. They too get thrust from momentu m 
transfer but they don't take in an oncom ing mass of air. Instead they carry 
their own reaction mass, usually as the fuel that they burn to power that 
mass out the rear. This makes them analytically strange -see Chapter 21. 
Figure 10.l illustrates the major options for fuel-based aircraft propulsion. These all oper ate by compressing outside air, mixing it with fuel, 
burning the mixture, and extracting energy from the resulting high-pres sure 
hot gases. In a piston- prop, these steps are done intermittently in the 
cylinders via the recipro cating pistons. In a turbine engine, these steps are 
done continuo usly, but in three distinct parts of the engine. The followin g 
subsections describe these in more detail. 
Pist on-pr op 
Tu rboprop 
Bur ner 
Com prs
s
....,
or
-;:,
/
::----.....:/
_
T
_
u rbi ne 
Centrif ugal tu rb ojet 
Bypass air 
Tu rbof an 
Bur ner 
Co mpr essor I Turbine 
I I 
Axi al -fl ow tu rbojet 
Fuel spr ay Flam eho lde rs 
ba rs 
Tu rbo jet 
or 
tu rbofan 
Afterburner 
Fig. 10 .1 Propulsion system options.


<!-- p.277 -->

CH APT ER 1 O Prop ul sion and Fuel Syste m In teg rati on 277 
1J1f JI Pis ton-Pr op 
Pisto n-prop engines have two advantages . They are cheap, and they have 
the lowest fuel consumption at lower speeds. However, piston engines are 
heavy and produce a lot of noise and vibration. Also, the propeller by its 
very nature produces less and less thrust as velocity increases. 
The piston-prop was the first form of aircraft propulsion. While experiments had been made with electric motors and steam engines, the Wright 
Brothers and all the other earlier aviation pioneers relied upon the gasoline 
internal combustion engine to make power and a propeller to turn that 
power into thrust. 
Actually, the propeller turns shaft power into thrust power, namel y, the 
product of thrust force and veloc ity. Because no propeller is perfect, some 
of that shaft power is "lost" along the way, typically 20%. We define propeller 
efficiency Y/p as the thrust power obtained divided by the engine power used, 
typically 80%. Thrust is then found as power times prop efficie ncy, divided 
by velocity. 
While the Wrights' engine wasn't very good, their propeller was amazing. 
They had expected to apply ship propeller theory to the design of an airplane 
propeller but discovered that there wasn't such a theory. So, they developed 
their own, a modified strip theor y not too different from one used today. This 
allowed them to design a propeller that was twice as efficient as all others, 
with an efficiency of about 60%. Twice the efficie ncy means twice the 
thrust per horsepower-a signi ficant advantage ! 
The continuing evolution of the piston engipe, producing better power 
to weight, lower fuel cons umption, less drag, more thrust, and greater 
reliability, was a major driver in the advancement of the aircraft. By the 
dawn of the jet era, a 5500-hp {4100-k W} pisto n-prop engine was in development. Today piston-props are mainly limited to light airplanes and some 
agricultural aircraft. 
Why is it that piston-props sudd enly fell out of favor for all but the 
slowest aircraft? Physics. When an airplane goes faster the shaft power 
put out by a piston engine stays the same, so the thrust power output by 
the propeller must stay the same. But thrust power is thrust times veloc ity, 
so as the velocity goes up, the thrust must go down. This has nothing to 
do with propeller efficienc y-even a perfectly efficient propeller would 
produce less thrust at higher speeds. Jets don't have this problem. 
ll1f IJ Tu rboj et 
The turbine engine consi sts of a compressor, a burner, and a turbine. 
These separately perform the three functions of the recipro cating piston in 
a piston engin e. 
The compressor takes the air delivered by the inlet system and compresses it to many times atmospheric pressure. This compressed air passes


<!-- p.278 -->

278 Ai rcraf t Des ign: A Concep tual Approach 
to the burner, where fuel is injected and mixed with the air and the resultin g 
mixture ignited. 
The hot gases could be imme diately expelled out of the rear to provide 
thrust but are first passed through a turbine to extract enough mechani cal 
power to drive the compressor. It is interesting to note that one early jet 
engine used a sep arate piston engine to drive the compressor. 
There are two types of compressors. The cent rifugal compressor relies 
upon cent rifugal force to "fling" the air into an increasin gly narrow channe l, 
which raises the pressure. In contrast, an axial compressor relies upon blade 
aero dynamics to force the air into an increas ingly narrow channel. An axial 
compressor typically has about six to ten stages, each of which consists of a 
rotor (i.e., rotating) disk of blades and a stator (i.e., stationar y) disk of blades. 
The rotors tend to swirl the air, so the stators are used to remove the swirl. 
The axial compressor, relying upon blade aerod ynamics, is intolerant to 
distortions in the incoming air such as swirl or pressure variations. These distortions can stall the blades, causing a loss of compression and a possible 
engine flame- out. 
The cent rifugal compressor is much more forgiving of inlet distor tion, 
but causes the engine to have a substantially higher frontal area, which 
increases aircraft drag. Also, a centrifugal compressor cannot provide as 
great a pressure increase (pressure ratio) as an axial compressor. Several 
smaller turbine engines use a centrifugal compressor behind an axial compressor to attempt to get the best of both types. 
Ml1f JI Tu rboprops and Tu rbofans 
A pure turboj et engine isn't very efficient, espec ially at lower speeds, 
because its exhaust is too small and too fast. As will be theoretic ally 
derived in Chapter 13 , aircraft propulsion is most ef ficient when the power 
of the engine is applied to a large cross-s ection area of the outside air, accelerating it by ju st a small amount. It is for this reason that helicopt ers have 
such huge rotors -they literally get more thrust for the power expended. 
To improve the efficiency of the pure turboj et engine, an addit iona l turbine can be added to extract mechanical power from the exhaust gases. This 
mechanical power can then be applied to acce lerate additional outside air. 
For a turboprop engine, the outside air is acceler ated by a conventional 
propeller. A propeller has greater diameter than other forms of aircraft propulsion so that it is inhe rently more efficient at creating thrust at lower 
speeds. Turboprops are still widely used for co mmuter and business aviation 
and are being seen even in small general aviation airplanes. 
For commercial airc raft, the turboprop fell out of favor with the dawn of 
the je t age and the passengers' newfound expectation of transonic speeds. 
Recent developments might bring them back. The "prop -fan" or "undu cted 
fan" is esse ntially a turboprop with an advanced aerod ynamics propeller 
capable of near-sonic speeds. These were succes sfully flight tested in the


<!-- p.279 -->

CHAP TER 1 O Prop ulsion and Fuel System In teg rati on 279 
1980s but did not find application, mostly due to noise and the lingering 
perception that they were "just" propellers. 
The latest variant called an "open rotor" has "propellers" that look and 
act more like the fan rotors at the front of a turbofan engine. Indications 
are that an open rotor engine will offer a 10-3 0% impro vement in SFC 
compared to a turbofan, but suffer a 10-d b increase in noise. Ongoing development work is addressing the issues of weight, comple xity, and noise. 
If success ful, open rotor engines could be seen on the next generation of 
new airlin ers. 
For the turbofan engine, the mechanical power taken from the exhaust 
gases by a turbine is applied to a ducted fan of one or more stages. This 
accelerates additional air, which improves efficienc y as described above. 
For most turbofans, the acceler ated fan air is split, with part of the air 
being "bypassed" around the engine to exit unburned, while the rest is 
ducted into the main part of the engine for further compression and 
burning. In effect, this acts like supercharging the "core," the turboj et 
engine that resides inside every turbofa_n engine. 
The key parameter for turbofan engines is the "bypass ratio," which is the 
mass-flow ratio of the bypassed air, to the air that goes into the core of the 
engine. Bypass ratios normally range from as high as 12 to as low as 0.25 
(the so- called leaky turboj et) . 
To improve efficiency even further, "ultra-high-by pass- ratio" turbofans 
are being studied, with bypass ratios as high as 20. Note that the open rotor 
engine described above has the equivalent of a bypass ratio of 30 or more. 
Another benefit of the turbofan engine is µoise reduction. The duct 
around the fan suppresses its noise, and the reduced exit veloc ity of the 
fan air vs a pure turboj et means that the noise- generating shear layers have 
reduced strength. 
The turbofan engine offers better efficie ncy than a turboj et at subson ic 
speeds, but at supersonic and higher speeds the drag of the fan increases 
so that the net benefit reduces. Aircraft designed for efficient oper ation at 
speeds over Mach 2 are likely to have pure turboj ets. 
ll1f JI Afterburner {Reh eat} 
The ideal turbine engine would inject enough fuel to completely combust 
all of the compressed air, producing maximum thrust for a given engine size. 
Unfortunately, this "stoichiometric" air/fuel mixture ratio of about 15 to 1 
produces temperatures far greater than the capabilities of known materials 
and would therefore burn up the turbine blades. 
To lower the temper ature seen by the turbine blades, excess air is used. 
Currently engines are limited to a turbine tempera ture of about 200025000F {1 100- 1400° C}, which requires an air /fuel mixture ratio of about 
60 to 1. Thus, only about a quarter of the captured and compressed air is 
actually used for combustio n. The exhaust is 75% unused hot air.


<!-- p.280 -->

280 Aircr aft Desig n: A Concep tu al Approa ch 
If fuel is injected into this largely un-c ombu sted hot air, it will mix and 
burn. This will raise the thrust as much as a factor of two and is known 
as "afterburning" ("reheat" in the United Kingdom) . Unfortunate ly, 
afterburning is inefficient in terms of fuel usage because the burnin g is 
done at a lower pressure and the oxygen has already been partially deple ted. 
The fuel flow required to produce a pound of thrust in afterburner is appr oximately double that used to produce a pound of thrust during normal 
engine operat ions. 
Because of the high temperatures produced, afterburning must be done 
downstream of the turbine. Also, it is us ually necessa ry to divert part of 
the compressor air to cool the walls of the afterburner and nozzles. Addition 
of an afterburner will approximately double the leng th of a turboj et or turbo fan engine, but only add 20-40% to the weight because it is mostly hollo w. 
Ml1f Jj Ramjets and Scra m jets 
If the aircraft is traveling fast enough, the inlet duct alone will compress 
the air enoug h to burn when fuel is added. This is the principle of a "ramj et." 
While they will run at Mach 0.5 or below, it isn't until they reach roughly 
Mach 3 that they become comp etitive with turboj ets in terms of efficienc y. 
The first ramjet-p owered aircraft was probably the French Leduc 0.10 , 
built by Breguet Aviation and flown in 1949. After being dropped from a 
mothership (ramj ets can't be used for takeoff), it reached Mach 0.85. Its 
most interesting feature was that the inlet had a giant con ical spike in the 
center, and the pilot sat inside the spike ! 
The Nord 15 00 Griffon, also French, had a turbojet for takeoff but 
switched to ramjet power in flight, reaching Mach 2.19 in 19 58. 
A "scram jet" is a ramjet that operates with supersonic internal flow. This 
reduces the mass ive drag asso ciated with slowing the flow, but requires 
fuel mixing and combustion in a supersonic flow-not easy! Scramjets are 
suitable only for oper ation above Mach 5 or 6. Scramjets were successfu lly 
tested in the X-43 and X-51 unmanned research aircraft, but the longest 
powered flight time was just over two minutes. 
Ramjets and scramjets require some other form of propulsion for takeoff 
and accele ration to the high Mach numbers where they oper ate. This is 
typically a traditional turboj et engine or a solid rocket boos ter. The scramjet 
research aircraft both used rocket boo sters many times larger than the test 
vehicle to acce lerate to hypersonic speeds. 
411f II Propu lsion Syste m Sele ction 
The selection of the type of propulsion system- piston-prop, turbop rop, 
turbofan, turboj et, ramjet-will usua lly be obvious from the design requirements. Aircraft maximum speed limits the choices, as shown in Fig. 10.2 . 
In most cases there is no reason to select a propulsion system other than


<!-- p.281 -->

CHAPTER 10 Prop ul sion and Fuel System In teg ration 281 
(Typ ical applic ations) 
Ram jet 
- f----------------:::0- After burning turb ojet 
O'l 
-- 1-----------,7" Afterburning lo w-bypa ss-ratio tu rbofa n 
"' 
b 1------- Low- bypa ss-ratio tu rbofa n 
c: 
1-------, High -bypass-ratio tu rbofa n 
0 
Propf an 
Pi sto n-pr op 
2 3 4 5 
Design Mach -umb er 
Fig. 10 .2 Propulsion system speed limi ts. 
6 
Roc ket 
? Scr amjet 
the lowest on the chart for the design Mach number. Fuel-consum ption 
trends have been shown in Fig. 3.3. 
The choice between a piston-pr op and a turboprop can depend upon 
several additional factors. The turboprop uses -ore fuel than a piston prop 
of the same power, but is subs tantially lighter and more reliable. Also, turboprops are usually quieter. For these reasons turbine engines have largel y 
replaced piston engines for helicopters, business twins, and shor t-range 
comm uter airplanes regard less of design speed. However, piston-props are 
substantially cheaper and will likel y remain the default choice for light 
aircraft for a long time. 
Electric propulsion is finally becoming practica l although it is still far 
from compet itive with fuel-based propulsion due to the weight of the 
power supply. To date, electric power has been applied mostly to propellers 
because they provide more thrust per unit power, but elec tric fans are also in 
use. Electric propulsion is discussed in Chapter 20. 
Jet-En gin e In teg ration 
Integrati on of a jet engine into an aircraft conc eptual design is very complicated. There are many calculations that must be made prior to the design 
layout, especia lly of the required thrust level (to pick or scale the engine) and 
the size of the inlet duct. The design layout must depict the engine proper ly 
with reasonable allowances for clearance for cool ing air flowing around


<!-- p.282 -->

. 
, , 
282 Ai rc ra ft De sign : A Conceptual Appro ach 
\,'i 
Hydraulic Pump 
Fig. 10 .3 RM6 engine ins tal lation of SAAB Draken (courtesy of SAAB Aircraft) . 
the engine and for access to and removal of the engine. Engine controls 
and fuel lines must be considered, and engine- driven accessories must be 
depicted if there is any question about their fitting into the design. 
There must be strong aircraft structure at the loca tions of the engine 
motor mounts. These can be found on the engine company's installation 
drawing. For commercial engines these are typically on the top, one toward 
the front, and one toward the back. For military engines there are typically 
one on the top toward the front and one on each side somewhere in the 
middle of the engine, or vice versa. 
Figure 10.3 depi cts a jet-en gine installation including inlet ducts, a 
remotely moun ted nozzle (to better balance this particular desig n), control 
lines, fuel lines and fuel system compo nents, and various engine- driven 
accessories such as hydraulic pumps and electrical gener ators . Note the 
clearance around the engine for cooling airflow and the use of ring frame 
wing carrythrough structure. 
Ml1fll Engine Dimen sions 
If the aircraft is designed using an existing, off-the-sh elf engine, the dimensions are obtained from the manufacturer. If a "rubber" engine is being used, 
the dimensions for the engine must be obtained by scaling from some 
nominal engine size by whatever scale factor is required to provide the 
desired thrust. The nominal engine can be obtained by several methods. 
In the major aircraft companies, designers can obtain estimated data for 
hypothetical rubber engines from the engine companies. These data are presented for a nominal engine size, and precise scaling laws are provided. 
Append ix E provides data for several hypothetical advanced engines. 
Better yet, engine companies sometimes provide a "parametric cycle 
deck, " a com puter program that will provide performance and dimensional 
data for an arbitrary advanced- technolog y engine based upon inputs such


<!-- p.283 -->

CH APTER 10 Prop ulsion and Fuel System In teg rati on 283 
as bypass ratio, overall pressure ratio, and turbine- inlet temperature. This 
kind of program, which provides great flexibility for early trade studies, 
goes beyond the scope of this book. 
Another method for defining a nominal engine assumes that the new 
engine will be a scaled version of an existing one, perhaps with some performance improvement due to the use of newer technologies. For example, 
in designing a new fighter one could start with the dimensions and performance charts of the P& W F-10 0 turbofan, which powers the F- 15 and F-16. 
To approxima te the improvements due to advanced technologies, 
one could assume, say, a 10 or 20% reduction in fuel consu mption and a 
similar reduction in weight. This would reflect the better materials, higher 
operating temperatures, and more efficient compressor s and turbines that 
could be built today. 
Figure 10. 4 illustrates the dimensions that must be scaled from the 
nominal engine . The scale factor SF is the ratio between the required 
thrust and the actual thrust of the nominal engine. Equations (10 .1-10 .3) 
show how le ngth, diameter, and weight vary with the scale factor for the 
typical jet engine. 
L = Lactua1 (SF) 0·4 
D = Dactuai (SF) 0.5 
W = Wactual (SF) 
1 . 1 
(10.1) 
(1 0.2) 
(10.3 ) 
Although statistically derived, these equations make intuitive sense. 
Thrust is roughly prop ortional to the mass flow of air used by the engine, 
which is related to the cross -se ctional area of the engine. Because area is 
Length (L) 
Scale fact or: SF = TrequireiTactual 
Fig. 10 .4 Engine scaling.


<!-- p.284 -->

284 Ai rcraf t Desi gn: A Conceptual Appr oach 
propor tional to the square of the diameter, it follow s that the diameter shoul d 
be propor tiona l to the square root of the thrust scale- factor. 
Note the engine-accessories package beneath the engine. The accessories 
include fuel pumps, oil pumps, power-takeoff gearboxes, and engine control 
boxes. The loca tion and size of the accessor y package vary widely for different 
types of engines. In the absence of a drawing, the accessor y package can be 
assumed to extend below the engine to a radius of about 20-4 0% greate r 
than the engine radius. On some engines these accessor ies have been 
loca ted in the compressor spinner or other places. 
If a parametric deck is unavailabl e, and no existing engines come close 
eno ugh to the desired characteristics to be rubberized and updated as just 
described, then a parametric statistical approach can be used to define the 
nominal engine. 
Equat ions (1 0.4- 10 .15 ) define two first-order statistical jet-engine models 
based upon data from [6l . One model is for subsonic nonafterburning engine s 
such as found on comme rcial transports and covers a bypass- ratio range 
from zero to about six. The other model is for afterburning engines for 
supersonic fighters and bombers (M < 2.5) and includes bypass ratios 
from zero to ju st under one. 
Nonafterburning engines: 
W = O .OS4T ue(-0.045 BPR) (lb) = 14.7 yl.le(-0 .045 BPR) 
L = 0.1 8S T 0·4M0·2 (ft) = 0.4 9T 0·4M0·2 
D = 0.0 33 y o.Se(0.04 BPR) (ft) = O.l S TO.Se(0.04 BPR) 
{kg} (1 0.4) 
{m} (10.5) 
{m} (10 .6) 
SFCmax T = 0.6 7e(-O .l2 BPR) (l/h r) = 19 e(-O. l2 BPR) {mg/N s} (10 .7 ) 
Tcruise = 0.60T 0.9 e(0.02 BPR) (lb) = 0.3 5T 0.9 e(0.02 BPR) {kN} (10.8 ) 
SFCcruise = 0.88 e(-O.OS BPR) (1/ hr) = 25e(-O .OS BPR) {mg/Ns} (10.9 ) 
Afterburning engines: 
W = 0_063 TuM0.25e(-0.81 BPR) (lb)= ll . l Tl. lM0.25e(-0.81 BPR) {kg} ( lO. lO) 
L = 0.25 S T0·4M0·2 (ft)= 0.68 T0 4M0· 2 {m} (1 0.11 ) 
D = 0.0 24 T 0.5e(o.o4 BPR) (ft)= O. l 1 T0.5 e(o.o4 BPR) {m} (1 0.12 ) 
SFCmax T = 2. le(-O l2 BPR) (l/hr) = 6 0e(-O.l2 BPR) {mg/N s} ( 10 .13 ) 
Tcruise = 2_4y 0.74e(00 23 BPR) (lb)= 0.5 9 T 0.74e(0.023 BPR) {kN} (l0. l4) 
SFCcruise = l .04 e(-0.186 BPR) (l/hr) = 30e(-0.186 BPR) {mg/N s} (10 .15 )


<!-- p.285 -->

where 
CHAP TER 1 O Propulsion and Fuel System In teg rati on 285 
W = weight (lb) or {kg} 
T = takeoff thrust (lb) or {kN} 
BPR = bypass ratio 
M = max Mach number 
and cruis e is at appro ximately 36, 000 ft {11, 000 m} and 0.9M. 
These equations represent a very unso phisticated model for initial estimation of engine dimensions. They should not be applied beyond the given 
bypass ratio and speed ranges. Also, these equations represent toda y's state 
of the art. Improvement factors should be applied to approximate future 
engines. For a next-generation engine this author recommends, as a crude 
approximation, a 20% reduction in SFC, weight, and length for a given 
maximum thrust. 
Reference [42] is recommended for the theory and practice of jetengine design. 
Iliff J Inle t Geom etry 
Turbo jet and turbofan engines can only operate efficiently if the air entering them is slowed to a speed of about Mach 0.4-0. 5. This keeps the tip speed 
of the compressor blades below sonic. Thus, the main job of an inlet duct is 
to take the oncoming massflow of air, slow it down, and smoot hly pass it to 
the jet engine. 
However, the total pressure in the onc oming air must be maintained as it 
passes into and through the inlet duct. As the air slows down and thus loses 
dynamic pressure, its static pressure must go up accordin gly so that the 
nozzle can use it to accelera te the exhaust back to the aircraft's speed. 
Thrust comes from an exhaust veloc ity greater than the aircraft speed. 
If total pressure is lost by the inlet duct then engine power must be wasted 
to make up for it, just to get the air back to its original speed. Roughly 
speaking, a 10% reduction in inlet press ure recovery (total pressure delivered to the engine divided by frees tream total pressure) will reduce thrust 
by about 13%. 
Thus, it is extremely impor tant that the airflow into and inside the inlet 
duct be slowed down in a manner that, as veloci ty is reduced, increases the 
static pressure. Slowing down the air inside a duct by expanding the crosssectional area of the duct is a "good way" because it raises static pressure 
to hold total pressure cons tant. Slowing down the air by skin friction along 
the sides is a "bad way" -the static pressure isn't raised. 
So, the installed performance of a jet engine greatly depends upon the 
design of the air induction (inlet) system. The type and geomet ry of the 
inlet and inlet duct will determine the pressure loss and distortion of 
the air supplied to the engine, which will affect the installed thrust and fuel 
consumption. Also, the inlet's external geomet ry including the cowl and 
boundary-layer diverter will influence the aircraft drag.


<!-- p.286 -->

286 Ai rcraf t Desig n: A Conc eptu al Appr oach 
a) NA CA fl ush in let 
1] 
b) Conical or spik e or ro und in let 
© 
Half round {2j Quar ter ro und LLJ 
c) Pitot or normal sho ck in let d) 2-D ra mp in let 
Fig. 10 .5 In let types. 
There are four basic types of inlets, as shown in Fig. 10.5. The NACA 
flush inlet was used by several early jet aircraft but is rarely seen today for 
aircraft propulsion systems because of its poor pressure recovery. At the 
subso nic speeds for which the NACA inlet is suitable, a pitot-t ype inlet 
will have virtually 100% pressure rec overy vs about 90% for a well-desi gned 
NACA inlet. However, the NACA inlet tends to reduce aircraft wetted 
area and weight if the engine is in the fuselage. 
The NACA inlet is often used for applications in which pressure reco very 
is less impor tant, such as the intakes for cooling air or for turbine-p owered 
auxiliary power units. The BD-5J, a jet version of the BD-5 homebuilt, 
used the NACA inlet probably to minimize the redesign effort. NACA 
flush inlets are seen on Ferraris and other spor ts cars -are they for efficient 
pressure reco very or for style? 
Figure 10.6 and Table 10.1 provide dimensions for laying out a good 
NACA flush inlet. This inlet will provide as high as 92% pressu re recovery 
when oper ating at a mass flow ratio of 0.5 (i.e., air mass flow through inlet 
is 0.5 times the mass flow through the same cross -se ctional area in the 
freestrea m) . 
The commo nly used "pitot inlet" is simply a forward-facing hole. It works 
very well subsonica lly and fairly well at low supersonic speeds. It is also called 
a "normal shock inlet" when used for supersonic flight ("normal" meaning 
perpendicular in this case) . Figure 10.7 gives design guidance for pitot* inlets. 
*Named for French hydraulic engineer Henri Pitot, who invented the "pitot tube" to measure flow 
velocities in the river Seine back in 17 32. Pronounce it [pee' toe] and you'll be close to the original.


<!-- p.287 -->

CHA PTE R 10 Propulsion and Fuel System In teg ration 287 
The cowl lip radius of an inlet has a major influence upon engine performance and aircraft drag. For subsonic jets, the lip radius ranges from 
6-10% of the inlet radius. A large lip radius tends to minimize distortion, 
especially at high angles of attack and sideslip. Also, a large lip radius will 
readily accom modate the additional air required for takeoff thrust, when 
the ram air effect is small. However, a large lip radius will produce greater 
drag from its blunt front. 
As the speed of sound is approached, shock-sep arated flow on the outside 
of the inlet increases the drag even more. At supersonic speeds the cowl lip 
should be nearly sharp, but there must be some compromise for subsonic 
flight. Supersonic jet inlets typically have a lip radius of about 3-5% of the 
inlet front face radius. 
To minimize distortion the lip radius on a subsonic inlet is freque ntly 
greater on the inside than the outside, with perhaps an 8% inner radius 
and a 4% outer radius. Also, a number of aircraft have a lip radius on the 
lower part of the inlet up to 50% greater than that on the upper lip. This 
reduces the effects of angle of attack during takeoff and landing. 
Normally, the plane of the inlet front face should be perpen dicular to the 
local flow direction during cruise. For the higher angles of attack during 
takeoff and landing, it might be desirable to angle the inlet front face downwards a bit so that the projec ted frontal area of the inlet isn't reduced just 
when you need airflow the most. This is seen on many airliners. 
Even at supersonic speeds, the airflow must be slowed to about Mach 
0.4-0.5 by the time it reaches the engine. The airflow inside the inlet duct 
will be subsonic so that the external geom etry ,of the inlet must slow the 
flow 
Rou nde d 
cowl lip 
Ramp fl oor 
- r --t 
) 7 deg t 
Cap tur e 
ar ea 
Fig. 10 .6 Fl ush inle t geometry.


<!-- p.288 -->

288 Air craft Desig n: A Conceptual Appr oach 
Table 10 .1 Flush Inle t Wall Geometr y 
1. 0 0.083 
0.9 0. 16 0 
0.8 0.236 
0.7 0. 31 3 
0.6 0.389 
0.5 0.466 
0.4 0. 61 4 
0.3 0. 766 
0.2 0.916 
0. 1 0. 996 
0.0 1 .000 
air from supersonic speeds to subsonic speeds. The physics of supersonic 
flow tells us that this occurs through a "nor mal, " that is, perpendicular shock . 
Thus, the forward-facing hole of a pitot inlet will automatic ally create a 
normal shock ju st in front of itself. This slows the air down to subso nic 
speeds whereupon it enters the inlet duct and sl ows down some more as it 
1 
Ca ptur e 
ar ea 
J 
m 
:J 
<!:> 
::;· 
rt> 
a 
al' 
('\ 
rt> 
Fig. 10 .7 Pilot (nor mal sho ck) inle t layout.


<!-- p.289 -->

CHAP TER 1 O Pro pulsion and Fuel System In teg ration 289 
proceeds to the engine. Unfortunately, the physics also tells us that some of 
the airflow's total pressure is lost going through the shock. 
The exit Mach number and loss of total pressure can be found in shock 
tables. (These were printed in earlier editions of this book but are now readi ly 
found on the internet.) At fairly low Mach numbers the loss is minisculeonly a tenth of a percent at Mach 1.1. With higher Mach numbers the 
normal shock is a lot stronger, and the total pressure loss becomes 
extreme. At Mach 2, the loss is 28%, yielding a thrust loss of perhaps 35% 
or more. This is unacceptable and is the reason why the normal-shock 
inlet is rarely used for prolonged oper ation above Mach 1. 4. 
Luckily, there is an altern ative. If we can slow the air down to about 
Mach 1.1 or so before a normal shock is seen, the losses will be reduced. 
We do this by first passing the air through an angled shock, created by 
turning the airflow. An angled, or "oblique," shock takes the air at the freestream superson ic Mach number and slows it to a lower, but still supersonic 
Mach number. Then we pass the air throug h the final normal shock, slowing 
it to subsonic speeds. . 
There is a total pressure loss through an oblique shock too, but if proper ly 
designed, the sum of the losses through the oblique and the final normal 
shock will be less than the huge loss through a single normal shock. This 
basic strategy is the essence of supersonic inlet design. 
We can turn the flow to crea te an oblique shock in several ways. A 
flat plate at an angle to the flow will do it, creating a shock that starts at 
the beginning of the plate and extends upwards at an angle found in the 
shock tables (see NACA TR 11 35 [431 ). This wedge d-shaped inlet is called a 
"two-dimensio nal ramp" inlet. 
We can also turn the flow using a cone. The conical inlet is also called a 
spike, round, or axisymmetric inlet, and can be a complete cone as on the 
SR- 71 or a partial one like the quarter-cone inlet spike on the FB-111 . 
The speed reduction and pressure recovery through an oblique shock 
depends upon the angle of the wedge or cone used to establish the shock. 
For example, a 10-d eg wedge in Mach 2 flow creates an oblique shock 
at 39 deg that reduces the flow speed to Mach 1. 66 (see NACA TR 11 35). 
This gives a pressure loss of only 1. 4% (i.e., pressure recovery of 98.6%) . 
If the Mach 1. 66 air downstream of this oblique shock is then run into a 
normal shock inlet, it will slow to Mach 0.65, with a pressure recovery of 
87.2%. The total pressure recovery from Mach 2 to subsonic speed is 98.6 
times 87.2, or 86%. Thus, use of an oblique shock before the normal shock 
has improved pressure recovery for this example Mach 2 inlet from 72 to 
86%. (Note that this simple example is far from optimal. A well- designed 
Mach 2 inlet with one oblique shock will approach a 95% pressure recovery.) 
Such an external -compression inlet system is shown in Fig. 10.8. The 
previous example is a two-shock system, one external and one normal. At 
a higher speed, the single oblique shock cannot efficiently slow the flow 
enough, so we simply add another oblique shock. The greater the number


<!-- p.290 -->

290 Ai rcraft Desig n: A Conceptu al Appr oach 
Normal shock External compr ession 
c---=--c:::::::::: __ _ 
lsent ropic 
Fig. 10 .8 Super sonic inle ts-exte rnal shocks. 
2 shock 
3 shock 
4 shock 
of oblique shocks emplo yed, the better the pressure recovery espec ially at 
higher Mach numbers. 
The theoretical ideal is the isentropic ramp inlet, which correspo nds to 
infinit ely many oblique shocks and produces a pressure recovery of 100% 
(ignoring friction losses) . The pure isentropic ramp inlet works proper ly at 
only its design Mach number and is seen only rarely except on "one-s peed" 
drones such as the Lockheed D-21, which uses an isentropic cone optimized 
to its cruise speed. However, isen tropic ramps are freque ntly used in combination with flat wedge ramps, such as on the Concor de SST. 
There is a problem with the use of oblique shocks to slow the air down. 
At any given Mach number, there is a shock angle that gives the best pressu re 
recovery. At different Mach numbers we need a different shock angle, which 
is only obtained by changing the angle of the ramp or cone. It is fairly easy to 
change a ramp angle-just mount the plate using a pivot at the front and 
attach an actuator to the rear. However, it is nearly impossi ble to change a 
cone angle! While aircraft such as the SR- 71 mechanize the cone to move 
in and out, none have succeeded in mechanizing a change in cone angle. 
This is why, even though the conical inlet is typically lighter and has 
slightly better pressure recovery (1 .5%), it is rarely emplo yed except on 
high-speed aircraft that are ruthlessly optimized to a single Mach number .


<!-- p.291 -->

CHAP TER 10 Prop ulsion and Fuel System In teg rati on 29 1 
Perhaps the use of morphing technolog y might some day per mit variable 
cone angle inlets. 
Figure 10.9 illustrates a typical three-s hock external -compr ession inlet. 
This illustration could be a side view of a two-dimensional inlet or a 
section view through a spike inlet. Note that the second ramp has a variable 
angle and can collapse to make a larger duct open ing for subsonic flight. 
Some form of boun dary-layer bleed is required on the ramp to prevent 
shock-induced sep aration on the ramp . The bled air is us ually dumped overboard out a rearward -facing hole above the inlet duct. 
Not shown are suck-in (or blow-in) and bypass doors in the diffuser 
section that might be required to provide extra air to the engine for takeoff 
or get rid of excess air during high-speed operation. 
For initial layout, the overall length of the external por tion of the inlet can 
be estimated by assuming an initial ramp angle (10 -20 deg) and determining 
the shock angle for the design Mach number using shock charts such as in 
NACA TR 11 35. The cowl lip should be placed ju st aft of the shock. The 
throat area should be about 70-80% of the engine front-face area. 
There is a fundame ntal speed limitation on external compression inlets 
due to the flow turning angle intro duced by the shocks. A wedge turns the 
flow parallel to the wedge angle, while a cone turns the flow to an angle 
slightly less than the cone angle. 
At speeds app roaching Mach 3, the inlet's oblique shocks will intro duce 
a total flow turning of about 40 deg. The air that doesn't go "down the hole" 
has also been turned and must be turned back to the freestream direction 
by attachment to the outside cowl lip. This might not be pos sible, resulting 
in cowl lip flow sep aration and a huge increase in drag. 
A different form of inlet system introduces no outside flow turning: 
the internal compression inlet, as shown in Fig. 10. 10. This uses a pair of 
inward-facing ramps to produce oblique shocks in the front part of the 
2-D external compr ession 
--------:::::;.--....- c;::::::::::::= t 
Cowl lip t y Throat bleed sots 
Th roat 
Cap tur e ar ea Varia ble ra mp 
j F;>ed ; o ;t\ rn mp 
-::::_"":;'.:------000000_ ,- Sub sonic 
position 
Fig. 10 .9 Variable inle t geome try. 
\ Exit for 
thr oat ble ed air


<!-- p.292 -->

292 Airc raft Des ign: A Concep tu al Ap proach 
In ternal sh ocks 
Mi xed isentropic 
Mi xed com pr ession 
3 shock 
5 shock 
Fig. 10 .10 Super sonic inle ts-i nter nal and mi xed . 
intake . These shocks cross, causing the air to pass through two oblique 
shocks before reaching the nor mal shock. 
This form of shock system can be very efficient when oper ating proper ly 
at its design Mach number. However, this inlet must be "start ed. " If it is 
simply placed into supersonic flow, a normal shock will form across its 
front. To start the inlet and produce the efficient shock structure shown in 
Fig. 10. 10, it is necess ary to "suck" the normal shock down to the throat by 
opening door s downstre am. Once formed, the desired shock structure is 
unstable. Any deviation in flow condition, such as temper ature, pressure, 
or angle of attack, can cause an "unstart" in which the normal shock pops 
out of the duct. This can stall the engine. 
The "mixed compression inlet" as shown in Fig. 10.10 uses both external 
and internal compression to provide high efficiency over a wide Mach 
number range, with an acceptable amount of external flow turning. Typically, 
one or more external oblique shocks will feed a single internal oblique shock, 
followed by a final normal shock. 
Such an inlet has been used for most aircraft designed to fly above 
Mach 2.5, including the B-70, which has a two-dimensiona l mixed compression inlet (Fig. 10 .11 ) and the SR-71, which has an axisymmetric inlet .


<!-- p.293 -->

CHAPTE R 1 O Propu lsion and Fuel System In teg rati on 293 
Unstart remains a problem for this type of inlet and caused at least one 
fatal crash in the SR-7 1. Automa tically open ing doors are used to co ntrol 
unstart. 
Mixed-com pression inlets are complex and can be defined only by 
detailed propulsion analysis beyond the scope of this book. Reference [44] 
is recommended. The rules of thumb just provided for the dimensions 
of external-compression inlets give a reasonable first approximation for 
mixed-com pression inlets. 
The "diffuser" is the interior portion of an inlet where the subson ic flow 
is further slowed down to the speed required by the engine. Thus, a diffuser is 
increasin g in cross-s ectional area from front to back. 
The required length of a diffuser depends upon the applicat ion. For 
a subsonic aircraft such as a commercial transpor t, the diffuser should be 
as short as possi ble without exceeding an internal angle of about 10 deg. 
Typically, this produces a pitot inlet with a length about equal to its frontface diameter. 
For a supersonic application, the theoretical diffuser length for maximum 
efficiency is about eight times the diameter. Lengths longer than eight times 
the diameter are permissible but have internal friction losses as well as an 
additional weight penalty. 
A supersonic diffuser shor ter than about four times the diameter can 
produce some internal flow sepa ration, but the weight savings can exceed 
the engine performance penalty. Diffusers as short as two times the diameter 
have been used with axisymmetric spike inlets. 
For a long diffuser it is impor tant to verify that the cross-sec tional area of 
the flow path is smo othly increasing from the inlet front face back to the 
engine. This verific ation is done with a vo lume- distribution plot of the 
inlet duct, constructed in the same fashion as the aircraft volume plot 
shown in Fig. 7.38. An example of a smooth, long fighter diffuser is shown 
in Fig. 10.12 , from the North American F-X proposal. 
Fig. 10 .1 1 B-70 inle t shock system.


<!-- p.294 -->

294 Air c raf t Des ign: A Conceptual Appr oach 
Fig. 10 .1 2 Typical fig hter inle t di ffuser. 
5TA SlO 
This is always a struggle for the con figurati on designer. When the desig n 
gets "tight, " the other groups look with lust on the inlet duct. They want to 
solve some problem by pushing their compo nents into that "empt y air. " 
Don't let them do it! And yes I mean you, landing- gear group ... 
To reduce airflow distortion, some aircraft use a diffuser that is oversized 
by about 5%. This "pinches" the flow down to the engine front-face diameter in a very shor t distance just before the engine, squeezing out the 
distortio n. 
Figure 10 .13 is a rule- of-thumb inlet selection criteria based upon design 
Mach number. Estimated pressure recoveries of various inlets are provided 
in Chapter 13. 
.... >. 
Vl .... 
0 · u g1 a. · - E 
- 0 QI u 
ti "O 
c c - "' 
Mi xed com pr ession .... L"--------> 
{ 
Exte rna l 
com pression 
in lets 
/ 7 
.... .c;...._ __ __,,.7 3 shock 
/ -""'------"'?' 2 shock 
__________ _,./ Pitot (normal shock ) 
1------,,/ NA CA fl ush 
0 2 
Des ign Mach numb er 
Fig. 10 .13 Inle t applicabil ity. 
4 shock 
3


<!-- p.295 -->

CHAP TER 10 Propulsion and Fuel System In teg rati on 295 
l'•f P In let Location 
The inlet location can have almost as great an effect on engine performance as the inlet geomet ry. If the inlet is loca ted where it can ingest a 
vortex off the fuselage or a sepa rated wake from a wing, the resu lting inletflow distortion can stall the engine. The F- 111 had tremendous problems 
with its inlets, which were tucked up under the intersection of the wing 
and fuselage. The A-10 required a fixed slot on the inboard wing leading 
edge to cure a wake-ingestion problem. 
Figure 10.14 illustrates the various options for inlet loca tion for buried 
engine installat ions. The nose loca tion offers the inlet a completel y clean 
airflow and was used in most early fighters including the F-86 and MiG 21 
as a way of ensuring that the fuselage would not cause distortion problems. 
However, the nose inlet requires a very long internal duct, which is heavy, has 
high loss es, and occupies much of the fuselage volume. 
The chin inlet as seen on the F- 16 has most of the advantages of the nose 
inlet but a shorter duct length. The chiH inlet is especia lly good at high angle 
of attack because the fuselage forebod y helps to turn the flow into it. 
The location of the nose landing gear is a problem. If it is placed forward 
of the chin inlet, it would block and distort the flow, and also the nose wheel 
would tend to throw water and rocks into the inlet. Instead, it is usua lly 
p --g erdl. 
c 
' --, .----0 Nose Chin Side 
- - r::l] -z F"""c 
c:: 
J:, - ,- --Armpit Ove r-fuselage Over-wi ng 
e= .........__ :J -(3 _____ 4 -CR ;::9 
Over-f uselage 
(ta il root) 
:::J - Wi ng root Wi ng le ading edge 
Fig. 10 .14 Inle t locat ions-b urie d engi nes.


<!-- p.296 -->

296 Ai rcraf t Desig n: A Conc eptu al Appr oach 
placed immed iately behind the inlet, which requires that the cowl be deep 
enough to hold the retracted gear, which can increase cowl drag. Also, the 
cowl must be strong enou gh to carry the nose -gear loads. 
If two engines are used, twin inlets can be placed in the chin position with 
the nose wheel located between them. This was used on the North American 
Rockwell prop osal for the F- 15 and is seen on the Sukhoi Su-27. 
Another problem with the chin inlet is foreign-ob ject ingestion by 
suction. As a rule of thumb, all inlets should be located a height above 
the runway equal to at least 80% of the inlet's height if using a low-bypassratio engine and at least 50% of the inlet's height for a high- bypass- ratio 
engine. 
Side- moun ted inlets are very common, espec ially for aircraft with twin 
engines in the fuselage. Side inlets provide shor t ducts and relatively clean 
air. Side-mou nted inlets can have problems at high angles of attack due to 
the vortex shed off the lower corner of the forebod y. This is especia lly 
severe if the forward fuselage has a fairly square shape. 
If side-mo unted inlets are used with a single engine, a split duct must be 
used. Split ducts are prone to a pressure instab ility that can stall the engine. 
To minimize this risk, it is best to keep the two halves of the duct separate all 
of the way to the engine front face, although several aircraft have flown with 
the duct halves rejoined well forward of the engine. 
A side inlet at the intersection of the fuselage and a high wing is called an 
"armpit" inlet. It is risky! The combined boun dary layers of the forebody 
and wing can produce a boun dary layer in the wing-fusela ge corner that is 
too thick to remove. (Bou ndary-la yer removal is discussed later.) This type 
of inlet is especially prone to distortion at angle of attack and sideslip. In 
many cases, however, the armpit inlet does offer a very short internal duct. 
An over-fus elage inlet is much like an inverted chin inlet and has a short 
duct length but without the problems of nosewheel locatio n. This was used 
on the unusual F- 10 7. The upper-fuse lage inlet is poor at high angle of 
attack because the forebod y blanks the airflow, althoug h careful forebod y 
design can create vortices tailored to guide the flow into the inlet. Also, 
pilots might fear that they will sucked down the inlet if forced to bail 
out manu ally. 
Placed over the wing and near the fuselage, an inlet enco unters problems 
similar to those of an inverted- armpit inlet. It also suffers at angle of attack. 
An inlet above the aft fuselage for a buried engine is used on the L- 1011 
and B-727, with the inlet located at the root of the vertical tail. This arrangement allows the engine exhaust to be placed at the rear of the fuselage, which 
tends to reduce fuselage separation and drag. The buried engine with a tail 
inlet must use an "S-duct." This requires careful design to avoid internal separation. Also, the inlet should be well above the fuselage to avoid ingesting 
the thick boun dary layer. 
Inlets set into the wing leading edge can reduce the total aircraft wetted 
area by elimin ating the need for a separate inlet cowl. However, these inlets


<!-- p.297 -->

CHAPTE R 1 O Pro pulsion and Fuel System In tegr ation 297 
can disturb the flow over the wing and increase its weight. The wing-root 
position may also ingest disturbed air off the fuselage. 
A podded engine has higher wetted area than a buried engine but offers 
substantial advantages that have made it standard for commercia l and 
business jets. Podded engines place the inlet away from the fuselage, providing undistur bed air with a very short inlet duct. Podded engines produce less 
noise in the cabin because the engine and exhaust are away from the fuselage. 
Podded engines are usually easier to get to for mainte nance. Most are 
mounted on pylons, but they can also be mounted confor mal to the wing 
or fuselage. Various options are shown in Fig. 10. 15. 
The wing-mounted podded engine is the most common ly used engine 
installation for jet transports. The engines are accessible from the gro und 
and well away from the cabin. The weight of the engines out along the 
wing provides a "span- loading" effect, which helps reduce wing weight. 
The jet exhaust can be directed downward by flaps which greatly increases 
lift for short takeoff. 
On the negative side, the presence -of pods and pylons can disturb the 
airflow on the wing, increasing drag and reducing lift. To minimize this, 
the pylons should not extend above and around the wing leading edge, as 
was seen on one early jet transport. 
On the basis of years of wind-tunnel study, design charts for pylonmounted engines have been prepared that minimize the interference effects 
of the nacelle pod on the wing. As a classical rule of thumb, the inlet for a 
wing-mounted podded engine should be located approxima tely two inlet 
diameters forward and one inlet diameter below the wing leading edge. 
However, modern compu tational fluid dynamic (CFD) methods now allow 
Und er-wing 
Tail 
Over-wi ng 
Ove r-fu selage 
Fig. 10 .15 In let locations -podded engi nes . 
Aft-fu selage 
Wingtip


<!-- p.298 -->

298 Aircraf t Design: A Conceptual Approach 
designing a wi ng-m ounted nacelle much closer to the wing, or even conformal to the wing, without incurring subst antial drag increase due to interference. This will be further discussed in Chapter 12. 
The wing-mou nted nacelle should be angled nose down by about 2-4 deg 
and canted nose inward about 2 deg to align it to the local flow under 
the wing. 
To reduce foreig n-ob ject ingestion by suction, the inlet of a high- bypass 
engine should be loca ted about half a diameter above the ground. This 
requirement increases the required landing-gear height of the under-w ing 
arrangement. 
The over-wing podded nacelle reduces the landing-gear height and 
reduces noise on the ground but is difficult to get to for maintenance. The 
inlets can be forward of the wing to minimize distortion, or above it. If an 
over-wing nacelle is conformal to the wing, the exhaust can be directed 
over the top of flaps, which, through Coanda effect, turn the flow downward 
for increased lift. 
The other standard engine installation for je t transpor ts is the aft-fuse lage 
mount, usua lly with a T-t ail. This eliminates the wing-in terference effects of 
wing-mou nted engines and allows a short landing gear. However, it increases 
the cabin noise at the rear of the aircraft. 
Also, aft-mo unting of the engines tends to move the center of gravity 
aft, which requires shifting the entire fuselage forward relative to the 
wing. This shortens the tail moment arm and increases the amount of 
fuselage forward of the wing, and that necessi tates a larger vertical and 
horizo ntal tail. 
To align the aft nacelle with the loca l flow, a nose-up pitch of 2-4 deg and 
a nose outward cant of 2 deg are recommended. 
The Illyushin Il-76 uses four aft-podded engines in two twin-en gine 
pods. The B- 727 and Hawker-S iddeley Trident combine aft-fus elage 
podded engines with a buried engine using an inlet over the tail. 
The DC- 10 combines wing- mounted engine pods with a tail-mo unted 
podded engine. This is similar to the tail-mounted inlet for a buried engine 
like the L- 1011, but eliminates the need for an S-duct. However, this arrangement increases the tail weight and doesn't have the fuse lage drag-reduction 
effect. All told, the two installati ons are probably equivalent. 
The supersonic Tupole v Tu-22 (Blinder) uses twin engines, pod- moun ted 
on the tail, but this arrangement has not been seen on later Soviet supersonic 
designs. 
The over-fuse lage podded engine has been used only rarely, such as to 
add a jet engine to the turboprop Rockwell OV- 10. Access and cabin noise 
are undesir able for this install ation. 
The wing-tip -mounted engine has an obvious engine-out controlla bility 
problem. It was used on the Soviet supersonic Myasishche v M-52 
(Bo under) , which also had under-w ing engine pods.


<!-- p.299 -->

CHAPTE R 10 Propulsion and Fuel System In teg ration 299 
#RI Captu re-Area Calcu lation 
In a jet propulsion system, the engine is the boss. It takes the amount of 
air it wants, not what the inlet wants to give it. If the inlet is providing more 
air than the engine wants, the inlet is forced to spill the excess out the front. 
If the inlet is not providing what the engine needs, it attempts to suck in the 
extra air required, and failing that, the engine thrust drops way down, maybe 
to zero. 
The capture area of an inlet is the cross- section area of the inlet front 
face, measured in the flow direction to the front-most part of the lip. 
Capture area is pure geomet ry, defined on the configuration layout. It is 
not the same as the freestream cross -se ction area of the air that is captured 
by the engine because in subsonic flight the flow spreads out as it approaches 
the inlet (Fig. 10.16). 
Capture area is impor tant. If it isn't correct, the engine might be starved 
for air espec ially at low speeds, or it might have excessi ve aerod ynamic drag. 
Not only must capture area be sized to provide sufficient air to the engine at 
all aircraft speeds, but for many aircraft the capture area must also provide 
"secondary air" for cooling and environmen tal control and also provide for 
the bounda ry-layer air that is bled off the inlet ramps and thrown overboard. 
Capture- area sizing has a large effect on drag, espec ially at supersonic 
speeds. If it is sized too large, the calcula ted drag values will be lower than 
they should be because any air that goes "down the hole" doesn't get 
pushed aside by the airplane. A modest mistake in oversizing the capture 
area can produce an estimated supersonic waye drag that is 20% lower 
than the corrected value! Later this can lead to a proj ect manager's worse 
nightmare: the propulsion group fixes the capture area, and the airplane no 
longer meets its performance goals! 
t 
In let 
mass flow 
ar ea 
(A=) 
t t Capt ur e 
ar ea Engine fro nt 
(Ac) 
Fig. 10 .16 Sub son ic inle t captur e area . 
face


<!-- p.300 -->

300 Ai rcraf t Des ign: A Concep tu a l Approach 
0 
sq ft 
lb per s 
0.0360 
0.03 40 
- 0.0320 
Vl 
"' 
E 
-..._ 
m o.o3oo 
"' 
E. 0.0280 
"' 
u 
0.0260 
r 
sq m 
kg per s 
0.00 75 
0.00 70 
0.00 65 
0.00 60 
0.005 5 
0. 0240 '------------------------- 0.005 0 
0.000 0. 500 1. 000 1. 500 2.0 00 2. 500 
Design Mach numb er 
Fig. 10 .1 7 Prelimin ary captur e area sizi ng . 
3.000 
So, the initial design layout must include a good estimate of the capture 
area. The actual calculations are described below and aren't too labo rious, 
but a quick statistical method gives a pretty good resu lt. Figure 10.17 estimates the required inlet capture area for subsonic and supersonic inlets, 
including approp riate amounts of bleed and secondary airflows. This estimation is based upon the design Mach number and the engine mass flow, 
normally obtained in the manufacturer's engine data. 
To determine the required capture area, the engine's mass flow is multiplied by the value read from Fig. 10.17. If mass flow is not known, it can be 
estimated as 26 times the square of the engine front-face diameter in feet 
{12 7 times meters squar ed} . If engine front face diameter is not known, it 
can be estimated as 80% of maximum diameter. 
As can be seen on the graph, the largest capture area is usua lly required 
at the highest Mach number. Sometimes, though, takeoff requiremen ts 
are even worse. If so, consider using auxiliary suck-in (or blow- in) doors 
during takeoff . 
A better method for calculating capture area for a subsonic inlet starts 
with the geome try of Fig. 10. 16 . Note the capture area shown by dotted 
lines and the flow streamlines expanding as they approach the inlet. 
A typical subsonic jet inlet is sized for cruise at about Mach 0.8 -0.9, and 
the inlet system must slow the air to about Mach 0.4 for turbofan engines . 
Because this is subsonic flow, the internal inlet duct does not need to do 
all of the work itself. The pressures created by the inlet cause the airflow 
to slow and expand as it approaches the inlet. We can actually control how


<!-- p.301 -->

CHAP TER 10 Propulsion and Fuel System In teg rati on 30 1 
much flow slowing takes place outside by proper ly selecting the capture 
area-a larger capture area causes more of the slowing to take place outside. 
We set this by defining the Mach number desired at the inlet front face, 
normally at halfway between the freestream value and that required at the 
engine front face. Then we can use the well-k nown isentropic compressible 
flow relationship [Eq. (10 .17)], which calculates a ratio between actual area 
and A*, the area that would give exactly sonic flow. This equation is used 
twice, once at the engine front face and once at the inlet front face (which 
is also the throat for a subsonic inlet) . Then the ratio of those results multiplied by the engine front face area gives us the capture area. 
Athroat (A/A* )throat ---Aengine (A/ A*) engine 
- = ]_ (1 + 0.2 M2) 3 
A* M 1.2 
where A* is the area of the same flow at sonic speed. 
(10. 16) 
(10. 17) 
For example, assume an engine that needs its air delivered at Mach 0.4. 
For a cruise speed of Mach 0.8, we might set the Mach number at the inlet 
front face to half the difference, that is, Mach 0.6. The air is slowed from 
M0.8 to M0.6 outside the inlet and from M0.6 to M0.4 inside the inlet duct. 
Equations (1 0. 16 ) and (10.17 ) give the ratio between throat area and 
engine front-face area as 1.188/1 .59, or 0.75 (for this example) . Taking the 
square root gives a diameter ratio of about 0.88, which is reasonable. Note 
that a subsonic inlet generally does not require bleed air because secon dary 
air is obtained from small NACA flush inlets in most subsonic aircraft. 
Equations (10 .16 ) and (10. 17) can also be used to determine the capture 
area for a supersonic pitot inlet. In supersonic flight the airplane is traveling 
faster than the pressures from the inlet, so the air doesn't slow down and 
expand in front of the inlet. Instead, the slowing down occurs through the 
normal shock and then inside the duct. From the flight Mach number, the 
subsonic Mach number behind the shock is found in shock tables such as 
NACA TR 11 35. Then those equations are used to find the area ratio from 
throat to engine front face. Note that this does not include any bleed or 
secondary airflows, which are discussed next. 
The geome try for a supersonic ramp inlet is shown in Fig. 10.18. The 
capture area is defined as the cross-s ection area of the inlet front face, 
measured in the flow direct ion to the front-most part of the cowl lip and 
the start of the ramp. For a coni cal inlet this geom etry is revolved around 
the bottom-m ost line, and the capture area is defined by the cowl lips and 
includes the frontal area of the cone. 
Capture- area sizing for a supersonic ramp or cone inlet is based upon 
manufacturer's data for engine mass flow, plus statistical approximations 
for bleed and seco ndary airflows. As a reminder for the discussion that


<!-- p.302 -->

302 Ai rcraf t Des ign: A Concep tual Appr oa ch 
Design case: sh ock-on-cowl 
Negligible com pr ession 
ra mp spillage 
M = Mdesign / r- Bypass door closed 
"f -------}------- --- - - - . 
c:::= o"E:II -------sed 
(A,= A-) -E 
, - - ! :: i::::: l::::t::::- ,-----, -·- - --- j ------ - -- r --. -- ".:tt.....
-s
-econdar y 
A-s A Th roat air flow (S) 
-s 
bleed (B) 
Fig. 10 .18 Su personic inle t capture area-on des ign. 
follows, airflow is defined by mass flow. Mass flow is related to flow conditions by Eq. (10.18). A word of caution-u sers of British Impe rial units 
(fps) some times multiply mass flow times g (32.2 ft/s 2) to obtain mass flow 
in pounds- mass per ft2, rather than the more-cor rect slugs per ft2. 
m=p VA (10. 18 ) 
The inlet of Fig. 10. 18 is shown at the des ign cond ition, known as 
"shock- on- cowl." At this Mach number and ramp angle, the initial oblique 
shock is almost touching the cowl lip. If the auxili ary doors are shut and 
the shock is on cowl, the geom etric capture area of a prop erly designed 
inlet at the design cond ition provides exactly the right amount of air for 
the engine, bleed , and seco ndary flow. 
Usually the design cond ition is chosen as a Mach number about 0.1 -0.2 
above the aircraft's maximum speed, giving a safety margin for speed 
overshoot and engine mass -flow fluctuatio ns. 
If the total mass flow required by the engine, bleed, and seco ndary flow is 
known, then Eq. (10.18) can be solved for the required cross-sec tional area 
upstream of the inlet (at "infini ty") using the freestream values for dens ity 
and veloc ity. This calculated area is iden tical to the capture area in the 
design cond ition (shoc k-on- cowl) because all of the air in the capture area 
is going into the inlet. 
The required engine mass flow is provided by the engine manufacturer and is a function of the Mach number, altitude, and throttle setting 
(percent power) . Usually the manufacturer's data should be increased by 
3% to allow for manufact uring tolerances. 
The seco ndary airflow requirements are accurat ely determined by an 
evaluation of the aircraft's subs ystems such as environmen tal control. For 
initial capture -area estimation, Table 10.2 (from [45l ) provides sec ondary 
airflow as a fraction of engine mass flow.


<!-- p.303 -->

CHAP TER 1 O Propu lsion and Fuel System In teg ration 303 
Table 10 .2 Secondar y Airflow (Typical) 145J 
sySiem rhs/the 
Eng ine 
Nac elle coolin g 
Oil cooling 
Ejector nozzle air 
Hydraulic system cooling 
0-0 .04 
0-0 .01 
0.0 4-0 .20 
0-0.01 
0.0 2-0.05 Environmen tal control system cooling air (if taken from inle t) 
Typical Totals 
Figh ter 
Transp ort 
0.20 
0.03 
Inlet boun dary-layer bleed should also be determined analytically, but 
can be approximated using Fig. 10 .19 , taken from [46l . This estima tes the 
required extra capture area for bleed as a percent of the capture area required 
for the engine and seco ndary airflow. 
The capture area is therefore determined as in Eq. (10 .1 9), using 
Table 10.2 and Fig. 10.19 . 
0.20 
0.18 
0.16 
0.14 
0.12 
\,.) 
- "< 0. 10 
""' 
0.08 
0.06 
0.04 
0.02 
0 
1.0 
Acapture = 
[rhe( l + rhs/rhe)] (l + As) 
gp00 Voo Ac (10. 19 ) 
Mi xed com pression in le ts 
2.0 
(por ous bleed) 
ble ed Externa l . 
compr ess ion 
Slo t} 
Por ous inle ts 
bleed 
3.0 
Mach nu mber 
Fig. 10 .19 Typical bou ndary -layer ble ed area . 
4.0


<!-- p.304 -->

304 Aircr aft Desi gn: A Concep tual Approach 
Figure 10.18 shows the inlet oper ating at its des ign condition, shockon-co wl, where the geometric capture area equals the freestream area of 
the air actually taken into the inlet and used. If the freestream Mach 
number is reduced, the oblique shock angle is reduced moving the oblique 
shock in front of the cowl, as shown in Fig. 10 .20a. 
Because the airflow is parallel to the ramp, the freestream cross- sectional 
area of the air that actually goes into the inlet is reduced. Part of the air 
defined by the geometric capture area is now spilled after being compressed. 
This represents wasted work and increased drag compared to the case of 
shoc k-on- cowl. 
If the mass flow demand exactly equals the mass flow shown goin g into 
the inlet in Fig. 10 .20a (i.e., capture area less compression- ramp spillage), 
then the engine and inlet duct are still "matc hed, " and the normal shock 
will be at the cowl lip, as shown in Fig. 10 .20a. 
However, the engine demand is usua lly reduced at a slower speed. 
The excess air is simply rejected by the inlet, as shown in Fig. 10.2 0b. 
(Remember , the engine is the boss!) This pushes the normal shock forward 
of the inlet and creates a much larger spillage drag than for the matched 
condition. 
Two approaches to move the normal shock back to the cowl lip are 
shown in Figs. 10.2 0c and 10.2 0d. By opening a bypass door in the diffuser 
section, the excess air can be taken into the inlet and thrown away before 
(Ble ed and sec ondar y ai rflows not shown) 
a) b) 
M < Mdesign Co mpr ession 
1t:::z-t:51'9' 
c) 
t Matched critica l 
A-E+S+B 
A-E+S+B 
oper ation 
Co mpr ession 
Bypass 
Critica l oper ation 
using bypass 
A-E+S+B 
d) 
Fig. 10 .20 Off-de sign inle t oper ati on. 
Su bcritica l operation, 
no bypass 
Critica l operation 
using mo va ble lip


<!-- p.305 -->

CHAPTER 1 O Propuls ion and Fuel System Int eg rati on 305 
reaching the engine. While an inlet bypass will create some additional drag, 
the total is reduced com pared with the case in Fig. 10.20b. 
(Do not con fuse inlet bypass air with the engine bypass air. Inlet bypass 
air is dumped out of the inlet before it reaches the engine and is therefore 
not a contributor to thrust. Engine bypass air is exited after being accele rated 
by the com pressor, and does contribute to thrust.) 
Another appro ach for returning the normal shock to the inlet lip is 
to move the cowl lip down, reducing the capture area as shown in 
Fig. 10.20d. * This also permi ts opening the "hole" for better airflow during 
takeoff and is seen on numerous airplanes such as the Eurofi ghter / 
Typhoon. However, it is com plex and heavy to mec hanize and virtually 
impossible for an axisymmetric inlet. 
It would also be possible to transl ate the ramp or spike fore and aft to 
maintain shock-on-co wl at different Mach numbers. However, the spike 
translation used on the SR- 71 is not for this, but to chan ge the throat area. 
The ratio between the airflow actually going into the inlet and the total 
possible airflow (i.e., the airflow of th_e capture area) is called the "capture 
area ratio" or "inlet mass flow ratio." The total mass flow actually going into 
the inlet is the mass flow required for the engine plus seco ndary airflow plus 
bleed airflow plus inlet bypass air, if any. 
Capture -area ratio is calc ulated by determining the required mass flow 
and dividing by the mass flow through the capture area far upstream 
[Eq. (1 0.20 )]. Note that capture -area ratio is gener ally critical for conditions 
in which the inlet bypass doors are closed (no bypass mass flow) . 
Aao me + ms + ms1 + mbypass 
Ac gpao VaoAc (10.2 0) 
In subsonic flow the capture- area ratio can be greater than, equal to, or 
less than 1. In supersonic flow, it can only be equal to or less than 1. 
Iliff 1 Bou ndar y-Layer Diverter 
Any object moving through the air will build up a bounda ry layer on its 
surface. In the last section, bounda ry-layer bleed was included in the capturearea calc ulatio n. Bleed is used to remove the low- ener gy boun dary-layer air 
from the com pression ramps to prevent shock- induced separation. 
The aircraft's forebod y builds up its own boundar y layer. If this 
low-energy, turbulent air is allowed to enter the engine, it will reduce 
engine performan ce and at supersonic speeds and might even prevent 
proper inlet operation. Unless the aircraft's inlets are very near the nose 
(within two to four inlet diamet ers), some form of boun dary-layer removal 
should be used just in front of the inlet. 
*D on't be confused. These sketches are upside down compared to the inlets in most actual 
airplanes such as the F-15, so "down" is actually "up"!


<!-- p.306 -->

306 Ai rcraf t Desi gn: A Concep tu al Approach 
The four major varieties of boun dary- layer diverter are shown in 
Fig. 10.2 1. The step diverter is suitable only for subsonic aircraft and relies 
upon the boun dary layer itself for oper ation. The boun dary layer cons ists 
of low- ener gy air, compa red to the air outside of the boundar y layer. 
The step diverter works by forcing the bound ary-layer air to either climb 
the step, pushing aside high-en ergy air outside the bou ndary layer, or to 
follow the step, pushing aside other boun dary-layer air that is of lower 
energy. If the step diverter is prop erly shaped, the latter option prevail s. 
The step diverter should have an airfo il-like shape that is faired smoothly 
to the nacelle. The diverter should extend about one inlet diameter forward 
of the inlet and should have a depth equal to roughly 2-4% of the forebod y 
length ahead of the inlet. 
The boun dary-layer bypass duct (simply a separate inlet duct) admits the 
boun dary- layer air and ducts it to an aft-facing hole. The internal duct shape 
should expand roughly 30% from intake to exit to compensa te for the internal 
friction losses. 
The suction form of bound ary-layer diverter is similar. The bounda rylayer air is remo ved by suction through holes or slot s just forward of the 
inlet and ducted to an aft-facing hole. This type of diverter does not 
bene fit from the ram impact of the bou ndary-layer air and therefore does 
not work as well. 
The channel diverter (Fig. 10.22) is the most common bound ary-layer 
diverter for supersonic aircraft. It provides the best performance and the 
least weight in most cases. The inlet front face is loca ted some distance 
away from the fuselage, with a "splitter plate" to ensure that the boundarylayer air does not get into the inlet. The bound ary-layer air is caught 
between the spli tter plate and the fuselage and pushed out of the resulting 
Step 
di verte r 
Bounda rylayer suc tion 
Chann el- type 
bou ndar y layer di verter 
Fig. 10 .21 Boundar y-layer rem oval.


<!-- p.307 -->

CHAP TER 1 O Prop ul sion and Fuel System In teg ration 307 
Spl itte r -pla te 
Inle t 
capt ur e 
ar ea 
I 
g_ 
Bounda ry-l ayer 
di verter ar ea 
Fig. 10 .22 Boundar y-layer div erter. 
channel by the diverter ramps. The diverter ramps should have an angle of no 
more than about 30 deg. 
The required depth of a boun dary-layer diverter depends on the depth of 
the boun dary layer itself. This cannot be easily calculated. The classic 
boundary-layer equations assume a flat plate, which is unlike a fuselage forebody. The three- dimensional effects of a real forebod y tend to reduce 
boundary-layer buildup compared to a flat plate. 
A very good rule of thumb for the required thick ness of a boun dary-layer 
diverter is that it should be between 1 and 3% of the fusel age length in 
front of the inlet, with the larger number for fighters that go to high angle 
of attack. 
As will be discussed in Chapter 12, the drag of a bound ary-layer diverter 
depends upon its frontal area. During con ceptual layout, the fuselage 
and inlet should be designed to minimize this area, shown shaded in 
Fig. 10.22. 
41•m Nozz le Integ ration 
The fundame ntal problem in jet-en gine nozzle design is the misma tch 
in desired exit areas at different speeds, altitudes, and thrust settings. The 
engine can be viewed as a producer of high-pressure subsonic gases. The 
nozzle accel erates those gases to the desired exit speed, which is controlled 
by the exit area.


<!-- p.308 -->

308 Air craft De sign : A Concep tu al Approach 
The nozzle must converge to acce lerate the exhaust gases to a high 
subsonic exit speed. If the desired exit speed is supersonic, a convergin gdiverging nozzle is require d. 
The exit area to obtain a desired exhaust velocity depends upon the 
engine mass flow (i.e., percent power) . This is espe cially a problem with afterburning engines in which the desired exit area for supersonic afterburnin g 
operation can be three times the desired area for subsonic, part-thru st 
operation. 
Typical nozzles are shown in Fig. 10.23. In the past, the nozzle of a jet 
engine was considered an integral part of the engine, to be installed on the 
aircraft without question or change. This is still the case for subsonic commercial aircraft but is changing for supersonic militar y aircraft due to the 
emergence of two-dimensio nal and other advanced nozzles. 
The fixed convergent nozzle is almost univers ally used for subso nic 
comm ercial turb ojet and turbofan engines. The nozzle exit area is selected for cruise efficienc y, resulting in a slight loss of performance at 
lower speeds. However, the simplicity and weight reduction of the fixed 
nozzle more than makes up for the performance loss in most subson ic 
applicat ions. 
For an aircraft that occasio nally flies at high-subsonic to low-sup ersonic 
speeds, a variable- area convergent nozzle allows a better match between lowspeed, part-thrust operation and the maximum speed and thrust conditions. 
Fixed Variable Conver ging Transl ating 
converg ent conv er gent iris plug 
-- -' -> - - -/;:::·- · 
Ejecto r 
Conver ging -d iver ging 
ejector 2-D vect oring 
I- ]t,,,,:·------> 
/ : 
........ : 
---,: ----2:, 
'------y--J 
Cir cle- to-sq uar e 
adap ter 
Fig. 10 .23 Types of nozzles. 
Single 
expa nsion 
ra mp (SERN) 
'------y--J 
Cir cl e-to-sq uar e 
adap ter


<!-- p.309 -->

CHAP TER 10 Propu lsion and Fuel System In teg ration 309 
The nozzle shown has a fixed outer surface, which causes a "base" area when 
the nozzle inside is in the closed posi tion. 
Such a nozzle was used on many early transonic fighters but is not 
typically used today. Instead, the convergent-iris nozzle is used to vary the 
area of a convergent nozzle with out introducing a base area. 
Another means to vary the exit area of a convergent nozzle is the translating plug. This was used on the engine for the Me- 262, the first jet to be 
employed in combat in substantial numbers. The plug slides aft to decrease 
exit area. 
The ejector nozzle takes engine bypass air that has been used to cool the 
afterburner and ejects it into the exhaust air, thus cooling the nozzle as well. 
The variable-geo metry converge nt-di vergent ejector nozzle is common ly 
used in supersonic jet aircraft. It allows varying the nozzle exit area for 
maximum engine performance throughout the flight envelope. The most 
advanced versions can also independe ntly vary the throat area. 
If an existing engine is used in the design, or if a hypothetical engine data 
package has been obtained from an eng_ine company, the nozzle areas will be 
provided for the design flight regime. If not, the nozzle areas must be 
estimated because they have a substantial effect upon the calculated aircraft 
wave drag and boat-t ail drag. 
For initial design layout, a reasonable approximation can be made based 
upon the estimated capture area. For a subsonic convergent nozz le or a 
convergent-di vergent nozzle in the closed position, the required exit area 
is approximately 0.5-0.7 times the capture area. For maximum supersonic 
afterburning operation, the required exit area is about 1. 2- 1. 6 times the 
capture area. 
As mentioned, nozzle arrangement can have a substantial effect on 
boat-tail drag. This is the drag caused by the separation on the outside of 
the nozzle and aft fuselage. To reduce boat-t ail drag to acceptable levels, 
the closure angles on the aft fuselage should be kept below 15 deg, and the 
angles outside of the nozzle should be kept below 20 deg in the nozzleclosed posi tion. 
Jet engines mounted next to each other produce an interference effect 
that reduces net thrust. To minimize this, the nozzles should be sepa rated 
by about one to two times their maximum exit diameter. The area between 
them should taper down like the back of an airfoil, terminating ju st before 
the nozzles. However, this arrangement increases weight and wetted area 
so many fighters have twin engines mounted right next to each other 
despite the increased interference. 
Al•ffl Engine Cooling Provisions 
A critical problem in the design integration of a jet engine is the heat put 
out by an operating engine and the need for engine bay cool ing. Many aircraft 
such as the F-22 have their aft fuselage built mostly of titanium because


<!-- p.310 -->

31 0 Air craf t Des ign: A Conceptual Approa ch 
the temp eratures around the engines are too high for aluminum or most 
composite materia ls. Even the B- 70, which was fabricated largely of hightemperature stainless steel, needed an elabo rate system of cooling aroun d 
the six engines, as shown in Fig. 10.2 4. At the top of the figure is the operatio n 
at low speeds, when inlet duct bypass air, inlet bounda ry-layer bleed air, and 
addit ional air taken in by ground cooling doors are all used for coolin g. 
As can be seen, a cooling shroud surrounds each engine to prevent excess 
heat from getting to the aircraft structure. 
At the bottom of Fig. 10 .24, the norma l operational mode up to Mach 3.0 
is shown. Cooling air is taken from the inlet, just upstream of the engin e, 
and used along with air taken from the bound ary layer bleed. At all speeds, 
part of the cooling air is ejected through the engine nozzle, and part is 
allowed to exit to the rear around the engines. 
During concept ual design, some allowan ce for engine cooling should be 
made based on similar aircraft. Do not "shrink-wrap" the aircraft's outside 
skin around the engin e. You must provide room for cooling and possibly 
an engine shroud, along with clearance for the engine and structural depth 
for the fuselage or nacelle around the engine. 
Bypass 
doors 
Fig. 10 .2 4 B-70 eng ine coolin g provisions.


<!-- p.311 -->

CHAPTE R 10 Prop uls ion and Fuel System In teg ration 31 1 
Propel ler -Engine In tegration 
M•f 11 Prope ll er Sizing 
The actual details of the propeller design such as the blade shape and 
twist are not required to lay out a propeller-engine aircraft. These come 
later. However, the diameter of the prop eller, the dimensions of the 
engine, and the cooling air intake and exit must be determined for the 
initial configuratio n design. 
Generally spea king, the larger the propeller diamet er, the more efficient 
the propeller will be. The old rule of thumb was "keep it as long as possi ble, 
as long as possible." Countering this, an overly long propeller will be heavy, 
will increase the loads on the motor mounts, and might require longer 
landing gear. The main limitation on propeller diameter is the propeller tip 
speed, which should be kept well below sonic speed. 
The tip of a propeller follow s a helical path through the air. Tip speed is 
the vector sum of the rotational speed [Eq. (10.21)] and the aircraft's forward 
speed as defined in Eq. (10 .22): 
where 
(Viip)static = 7TnD 
n = rotational rate obtained from engine data 
D = diameter 
(10.21) 
(10.2 2) 
[Watch the units! Rotation rate is no rmally given as revolutions per minute 
(rpm) and must be converted to revolutions per second by dividing by 60.] 
To avoid shocks on the tips during high -speed flight, the calcula ted tip 
speed should be less than the critical Mach number of the propeller airfoil. 
This is approximated in the follo wing rule of thumb: 
At sea level the helical tip speed of a metal prop eller should not exceed 
950 fps {290 m/s}. A wooden propeller, which must be thicker, should be 
kept below 850 fps {260 m/s}. If noise is of concern, the upper limit for 
metal or wood should be about 700 fps {2 13 m/s} during takeoff. The appropriate speed limitation is factored into Eq. (1 0.22) and then Eq. (10 .21) to 
determine allowable diameter. 
Because of weight and configuration arrangement cons idera tions, propeller diameter might be even less than the value calculated based on tip speed. 
This can be approximated with a statistica l approach [Eq. (10 .23 )], which 
estimates propeller diameter as a function of horsepo wer or kilowatts. The 
propeller diameters obtained from these equations should be compared to 
the maximum diameters obtained from tipspeed considerations and the 
smaller of the two values used for initial layout. 
(10.2 3)


<!-- p.312 -->

312 Ai rc raf t De sign: A Concept ual Approach 
Where 
2 1 .7 
3 1 .6 
4+ 1. 5 
Power un its hp 
Diame ter un its ft 
0. 56 
0.5 2 
0.49 
kW 
m 
Method modif ied from 1471 , with spe cial thank s to D. Gerren 
for ai rcraft data colle ction to up date these equations. 
As forward veloc ity increases, the angle of attack seen by the blades of a 
fixed- pitch propeller will decrease. This limits the thrust obtained at higher 
speeds. If the fixed pitch is increased, the blades will tend to stall at low 
speeds, which reduces low- speed thrust. A fix ed-pi tch propeller is called a 
"cruise prop" or "climb prop" depending upon the flight regime the designer 
has decided to emphasize. 
A variable- pitch propeller can be used to impro ve thrust across a broad 
speed range. A controlla ble-pi tch propeller has its pitch direct ly controlled 
by the pilot through a lever alongside the throttle. A constan t-speed propeller is automa tically controlled in pitch to maintain the engine at its 
optimal rpm. 
Most aircraft prope llers have a "spinn er, " a cone- or bullet-sh aped 
fairing at the hub, The inner part of the propeller contributes very little to 
the thrust. A spinner pushes the air out to where the propeller is more efficient. Also, a spinner streamlines the nacelle. Ide ally, the spinner should 
cover the propeller out to about 25% of the radius, although most spin ners 
are not that large, 
To further streamline the nacelle, some aircraft designers use a prop 
extension, a short shaft that loca tes the propeller 2-4 in. {5- 10 cm} farther 
forward (or aft) of the engine. If the propeller is located much farther away 
from the engine, a complicated drive shaft with a sep arate bearing supp ort 
for the propeller must be used. This type of installation was used in the 
P-39, which had a piston engine behind the cockpit and a drive shaft to 
the forward-mo unted propeller. Similarly, the BD- 5 had a drive shaft to a 
rear-moun ted pusher propeller, Such drive shafts are prone to vibration 
and torsio nal excitation and are often heavier and less reliable than the 
designer anticipated. Even Lockheed has had problems with drive shafts the one used to spin the lift fan in the F-35B required a comp lete redes ign, 
and wound up much heavier than origi nally expected, 
Surprisin gly, the number of propeller blades does not have to be speci fied 
for the initial configuration layout, although it will have to be chosen before 
detailed thrust calculations (Chapter 13). In general, the fewer the blades, the 
better the efficiency if diameter is the same. The more blades used, the more


<!-- p.313 -->

CHAPTE R 10 Propulsion and Fuel System In tegr ation 31 3 
each blade is affected by the downwash and tip vortices of the preceding 
blade. This is similar to the inefficiencies experienced by the wings of 
a biplane. 
And yes, a single-b laded propeller is poss ible and in fact, is optimal! 
Model airplanes use single bladed props for record- setting flights including 
maximum speed and longest rubber-po wered endurance. Vibrat ion problems 
usually preclude their use for larger aircraft, even if the blade is coun terweighted. 
The reason for using more than two blades is that the propeller needs to 
have enough blade area to absorb the engine's power. Increasing diameter 
would be a more efficient way to increase blade area, but brings about problems including high tip speeds, increased weight, and ground clearance 
problems. 
Some new propeller designs use gearboxes to slow the prop down which, 
in addition to lowering tip speed, also reduces blade-to- blade interference. 
One seven-b laded design by German company MT- Propellers, now in flight 
test and driven by a PT6A turboprop, _ produces better takeoff performance 
with reduced prop noise. 
ll1Jf J Prope ll er Location 
The common propeller loca tions are shown in Fig. 10.25. The two main 
options are propeller in front, a "tractor" inst allation, or propeller in the rear, 
a "pusher ." The choice of tractor versus pusher has a huge effect on the subsequent aircraft design, so it must be consi dered carefu lly. Better yet, try both 
approaches and study the relative benefits of the two very different designs 
that will be produced. 
The Wright Flyer was a pusher. This let them use a canard tail arrangement which gave more- assured pitch control, and also avoided blowing air 
over the pilot. Several other early designs like those of Glenn Curtiss and 
Alberto Santos Dumon t were also pushers. Despi te this promising start for 
pushers, the tractor location has been standard for most of the histor y 
of aviation. 
The tractor propeller loca tion puts the heavy engine up front. This 
usually shortens the forebod y allowing a smaller tail area and impro ved 
stability. The tractor loca tion also provides a ready source of cooling 
air and places the propeller in undisturbed air. It is superior for pilot 
protection during a crash since the heavy motor clears a path through 
the trees. 
The pusher loca tion does have some advantages and has been used on a 
number of more-recent designs. Most important, it can reduce aircraft 
skin-fricti on drag because the pusher loca tion allows the aircraft to fly in 
undisturbed air. With a tractor propeller the aircraft flies in the turbulence 
from the propeller wake.


<!-- p.314 -->

314 Ai rcraf t Desig n: A Concep tual Approach 
Fuselage 
Wing 
Pod 
Tra ctor 
t=cf?s-=l-!J 
- D e?YJ 
Fig. 10 .25 Prop eller location matrix. 
The fuselage-moun ted pusher propeller can allow a reduction in aircraft 
wetted area by shor tening the fuselage. The inflow caused by the prop eller 
allows a much steeper fuselage closure angle without flow sep aration than 
otherwise possible. The canard-pusher combination is espe cially favorable 
because the canard requires a shor ter tail arm than the aft tail. 
The pusher propeller reduces cabin noise because the engine exhaust is 
pointed away from the cabin, and the windscreen is not buffeted by propwash. The pusher arrangement usua lly improves the pilot's outside vision, 
and reduces the very real danger from fire, smoke, and C02. 
However, the pusher configuration suffers several disadvantages. The 
propeller has reduced efficiency because it is forced to work with disturbed 
airflow off the fuselage, wing, and tails. It usually moves the center of 
gravity to the rear so the tails need to be larger. 
The pusher propeller might require longer landing gear. With an aft 
loca tion, the propeller will dip closer to the runway as the nose is lifted for 
takeoff. The propeller should have at least 9 in. {23 cm} of clearance in 
all attitudes. 
The aft-mounted propeller is also more likely to be damaged by rocks 
thrown up by the wheels. A pus her loca tion for a turboprop propeller can 
create problems due to the engine exhaust impinging upon the propeller.


<!-- p.315 -->

CHAPTE R l O Propulsion and Fuel Syste m In teg ration 31 5 
The Cessna Skymaster and Rutan Defiant use a combination of pusher 
and tractor engines on the fuselage to eliminate engine- out yawing 
moments. This "push-pu ll" arrangement, also seen in several unmanned aircraft, is safer in the event of an engine failure during takeoff but in some ways 
combines the problems of both designs. The fuselage is flying in pro pwash, 
and the aft propeller is flying in bad air from the fuselage. The people 
inside get noise and vibrati ons from both end! 
Most multi-engine aircraft have the engines out on the wings . This reduces 
wing structural weight through a span-loa ding effect, and reduces fuselage 
drag by removing the fuselage from the prope ller wake. There are engineout controllabili ty problems that are usua lly solved by an increase in the 
size of the rudder and vertical tail. Even then, the pilots must undergo 
special training to ensure that they maintain control. Sadly, sometimes 
they don' t. 
Care must be taken during design layout to ensure that the crew and 
passenger compa rtment is not located within ± 5 deg of the propeller disk, 
in case a blade is thrown through the fuselage. For noise reasons it's good 
to keep the propeller away from the fuselage as much as possible. 
With the propellers on the wing, the landing gear has to be extra-long to 
ensure that the props don't strike the ground. Some times the propeller is 
located above the plane of the wing to reduce the landing- gear height. This 
must be done with caution because it causes interference between the 
wing and propeller and increases drag. 
Almost all wing-mounted engines use a tractor propeller arrangement. 
The few examples of the wing-mounted pusher include the Beech Starship 
and Convair B-36. This arrangement tends to lengthen the forebod y and 
requires a very long landing gear. Also, the propeller is half in the wake 
from under the wing and half in the wake from over the wing. The turbulence 
and pressure differences between these two wakes can cause the propeller to 
lose efficienc y and produce vibrati ons. This is minimized by loca ting the 
propeller as far as possible behind the wing, but that makes the landing 
gear problem even worse. 
Upper-fuse lage pods and tail -mo unted pods are used mostly for seaplane 
and amphibian designs. These need a huge clearance between the water and 
the propeller (minimum of 18 in. {46 cm}, prefer ably one propeller diameter, 
but more is even better) . The high thrust line can cause undesir able control 
characteristics in which application of power for an emergency go-around 
produces a nose- down pitching momen t. In fact, it may be difficult to raise 
the nose for takeoff if careful calculations aren't performed during the 
design process. 
There have been some oddball propeller locat ions. The V-22 and the 
Vought V- 173 [17 1 l both have their propellers on the wingtips, but for different reasons. Some designs have their propellers on articulated pylons and 
struts, such as the Advanced Tactics Barracuda which converts to a quadc opter for vertical takeoff. Other designs have their propellers in rings which are


<!-- p.316 -->

316 Ai rc raf t Desig n: A Con ceptu al Appro ach 
buried in the wings for vertical flight, then pivot out of the wings for forward 
flight. These are all spec ial arrangements for special purposes, and need to be 
studied in great detail to determine if they are worth the bother. 
Ml1Jfl Duc ted Fans 
Ducted fans are commonplace for model airplanes but, other than a few 
speci alty applications, are uncommon for full- size aircraft. They have their 
enthusiastic supporters who always wonder "why" but never like the 
answer-we don't use ducted fans because when you use them, you usually 
get an airplane with less capabilit y. 
The reason is simple physics, mentioned before and derived in Chapter 13. 
Aircraft propulsion is more efficient when the mechanical power of the 
engine is used to accel erate a larger cross -se ction area of the air. Althoug h a 
ducted fan is more ef ficient than an equal diameter prope ller, it is rare for a 
ducted fan to actually have the same diameter. If it did, the extra weight and 
high-speed drag of the duct would obli terate the expected bene fit. 
Ducted fans are more efficient than an equal diameter propeller for 
several reasons. At low speeds especia lly, the air inflow in front of the duct 
means that the fan is actually acce lerating a greater cross-sec tion area of 
air than the area of the fan itself. In effect, the duct increases the fan diameter . 
There is also pressure thrust from the flow accelerating around the inlet lips 
as it is pulled into the duct. 
Another reason for improved efficiency is that the duct wall helps the 
fan in the same way that an endplate helps a wing, preventing the loss of 
"lift" towards the blade tip and also preventing the tip vortices that prop eller 
blades, like wings, experience. The duct also allows the designer to control 
the veloc ity of the air entering the fan, by changing duct diameter as discussed above for je t inlet ducts. 
But despite this, for most aircraft design applications the ducted fan 
cannot have the same diameter as a propeller due to weight and drag considerations, so it doesn't see a gain in thrust ef ficienc y. For high-speed 
flight, the ducted fan design suffers from the drag of the duct, which more 
than cou nters the efficiency improvement of the fan. 
Typical calculations might indica te a propeller by itself getting an efficienc y of 80% at its design condition. This could increase to perhaps 90% 
when enclosed in a proper ly-designed duct. However, when the forwardflight drag of the duct is included the net efficiency may drop to 60 or 70% . 
For a ducted fan to work well, the gap between fan and duct must be 
miniscule. Otherwise the higher pressure behind the fan will "leak" forward 
through the gap. This requires good dimensiona l control in fabrication , 
and also the duct structure must be strong enoug h and stiff enough so that 
flexing into the rotating fan does not occur. Simil arly, the blades thems elves 
must be stiff and not bend or stretch under rotational loads.


<!-- p.317 -->

CH APTE R 10 Propulsion and Fuel Syste m In teg ration 317 
Another consid eration is that, like a jet engine, the ducted fan will suffer if 
there is distortion in the inlet flow, or if it has a thick bou ndary layer. Try 
to avoid configurations where the duct takes in air that has alread y travelled 
the length of the fuselage or includes the air from the wing root. 
Ducted fans get the greatest thrust benefit at zero speed, so they are 
especially useful for vertical takeoff aircraft. Using ducted fans rather than 
propellers or helicopter rotors allows a reduced diameter and might make 
it easier to pivot the thrust for forward flight. At equal diameter, a ducted 
fan has perhaps 30% more static thrust (lift) but as mentioned, can rarely 
have that equal diameter. An empirical approximation for the static lifting 
capability of a well-designed ducted fan is: 
where 
W = weight (lbs or kg) 
P = power (hp or kW) 
W/P = K (P/A)-·35 
A = Duct total internal cross-s ection area at fan (sqft or sqm) 
]( = 15 .4 in fps, 19 .4 in mks 
(10.2 4) 
Remember that this excellent static thrust drops off rapidly in forward 
flight. A detailed analysis is required to estimate this. 
Perhaps the best reasons for using ducted fans are the practical ones. 
A ducted fan is much quieter than an open propeller as long as the tip 
speeds are kept low. A ducted fan is also safer. Accidents involving people and 
spinning propellers are still too common. Even with a small net pena lty, a 
quieter, safer general aviation airplane would be a good thing. 
Ducted fans typically allow higher rotation rates because the fan has less 
diameter than the equival ent thrust propeller and the veloc ity inside the duct 
is lower than the freestream. This may permit the use of high-rpm motors 
without the need for heavy reduction gearing. This is espe cially beneficial 
for two-stroke gasoline engines, Wankel engines, and electric motors, all 
of which tend to operate at higher rpm than traditional four- stroke aircraft 
engines. 
A recurring idea is to place a large ducted fan at the rear of an airplane 
and use it for the tail group as well. While it is always beneficial to get one 
part of an airplane to serve two functions, it seems that the duct ring never 
provides enough stability. To make it work, the duct might need to be 
augmented with additional tail surfaces as in this interesting design 
concept by NASA's Andrew Hahn (Fig. 10 .26) J48l 
So why do we see so many ducted fans in model airplanes? Partly this is 
because model airplanes fly at low speeds compared to real airplanes, where 
the thrust benefit of a ducted fan is most pronounced. Model airplanes tend 
to use engines that operate at high RPMs. Another reason is that rea l turbojet 
engines of model size are expensi ve, and nobody wants to hang a propeller on 
the front of their beautiful subscale F-86!


<!-- p.318 -->

318 Ai rcraft Des ign: A Concept ual Approach 
Fig. 10 .2 6 NASA "Tail lon" duc ted-fan gener al aviation concept (image from NASA Langle y 
Resea rch Center . no copy right is asser ted). 
Ducted-fan design and power matching are complica ted subjects. A good 
classica l treatment can be found in Ki.ichemann and Weber. l49l A moremodern treatment is found in Hollman. f 5°l 
Ml•JCI Engine Type and Size 
There are many types of propeller powerplant in use. The Wright Brothers were unable to purchase a suitable engine, so they designed their own, a 
four cylinder in-line engine. While crude even by the standards of the day-it 
had no carburetor, and the cooling water did not circulate-it did have an 
innovative aluminum crankcase, and it put out ju st enough power to fly. 
By the time of World War I, the radial cylinder arrangement was widely 
used. It provides better cooling for a high power piston engine and is also 
shor ter. In-line and radial engines were common up to the 19 50s, but are 
rare today in the West. In former Soviet-bloc countries, large radial 
engines are still in production for agricultural, utilit y, and aeroba tic aircr aft. 
The horizo ntally opposed piston engine is most widely used for gener alaviation aircraft, offering low frontal area and, with suitable cowling des ign, 
acceptable cool ing. With proper maintenance, the reliab ility of such engines 
is almost magical. Norma lly they burn speci al aviation grades of gasoline, but


<!-- p.319 -->

CHAPTE R 10 Propulsio n and Fuel System In teg rati on 319 
a simple conversion allows many of them to burn the cheaper automo tive 
grades. 
Be aware that many piston engines have two power ratings- maximum 
power, and maximum continuous power. As for your automobile, you 
don't want to push the throttle all the way in and leave it there for several 
hours! If an aircraft engine does have a maximum continuous power limit 
it probably produces about 5-8% less power than the maximum setting. 
This must be taken into account for cruise calculations especia lly. 
While the general aviation piston- prop aircraft will continue to rely on 
the horizontally opposed engine for many years to come, there are some 
exciting new developments under way, many driven by the market for homebuilt aircraft. These include automo tive engine conversions, new radial 
engines, two-stroke gasoline and diesel engines, Wankel engines both new 
and auto conversions, and even turboprops designed just for this market. 
The turboprop is a jet engine where an extra turbine has been added 
to extract mechanical power from the exhaust. This power is applied to a 
propeller, creating more thrust than the jet engine alone could provide. At 
higher speeds the thrust loss experienced by all propellers limits its efficie ncy, 
so turboprops are most suitable for airplanes that fly at under 400 kt. Turboprops are common for commuter and business airplanes, although there is a 
tendency for the flying public to prefer a "real jet" even if it is less efficient. 
When creating the aircraft configuration layout, the engine integration 
is a key task. The engine power has previously been calculated using 
performance requirements to determine P / W or power loading, which is 
then applied to the aircraft's sized takeoff gross weight. The dimensions of 
an engine producing this power must now be determined. 
In propeller aircraft design it is more common to size the aircraft to a 
known, fixed-size engine as opposed to the rubber-e ngine aircraft sizing 
more common early in jet-aircraft design. In fact, most propeller- aircraft 
designs are based around some production engine, prob ably because very 
few new piston or turboprop engines are being designed and certified. 
Many piston engines in production toda y were originally designed almost 
50 years ago. The high cost of developing and certifying a new engine, and 
the relatively small market, prevent new engines from appea ring. 
Even if an existing engine must ultimately be chosen, rubber- engine trade 
studies can be performed to poi nt to the existing engine that is best for that 
design. Also, the use of rubber- engine trade studies for comparison of 
alternate technologies (such as compo site vs aluminum structure) can 
prevent a bias in the results due to the use of a fixed engine size. 
If a production engine is to be used, dimensiona l and installation data 
can be obtained from the manufacturer. If a rubber engine is to be used, 
an existing engine can be scaled using the scaling equations defined in 
Table 10.3, developed by the author from data taken from [1l . 
Alternatively, the statistical models defined in Table 10.4 can be used to 
define a nominal engine.


<!-- p.320 -->

320 Air craft Desi gn: A Conceptual Appro ach 
Table 10 .3 Scaling Laws for Pis ton and Turboprop Engi nes 
Weight 
Length 
Diame ter 
I I • • . • 
0.7 8 
0.424 
Pi ston Eng in es 
0.78 
4.24 
* 
*W idth and heigh t vary insign ificantly with in +5 0% power. 
Xscaied = Xactua1SFt. 
tFrom table valu es SF= powerscaled/poweractual· 
41•111 Pis ton-E ngine Ins tall ation 
111 I 
0.809 
0.31 0 
0. 13 0 
1m.1.1w1 
0.803 
3.730 
0.1 20 
Piston engines have special installation require ments that can greatly 
affect the configuration layout. These are illustrated in Fig. 10.27. 
Cooling is a major concern. Up to 10% of the engine's power can be 
wasted by the drag asso ciated with taking in cooling air, passing it over the 
engine, and exiting it. To minimize this cooling drag, the cooling-air mass 
flow should be kept as small as possible and used as efficiently as possible . 
Typical air-cooled engines need about 1 lb of cool ing-air mass flow per 
second per 100 hp of the engine {'"'-' 0.6 kgps per 100 kW power} . Optimization studies indica te that the best intake sl ows the air to 30- 70% of 
the aircraft flight speed (climb speed in the worst case) . This results in the 
following equation for piston engine cooling area sizing [1l : 
Cooling intake area: 
A 1· - bhp {ft2} coo mg - 2 2 V: . 
· climb 
p 
A 1· - {m2} coo mg - SS V: . 
climb 
(10.2 5) 
(10.2 6) 
Power is in horsep ower or kilowatts. Vclimb is the climb speed in feet per 
second or meters per second. This is usually the critical cond ition for cool ing. 
Despite an old rule of thumb that says that the exit area should be 30% 
larger than the intake area, recen t analysis has shown that an exit area slightly 
smaller than the intake is actually better. For prelimina ry layout this author 
suggests designing to a ratio Aexit! Ainlet of 0.8 and providing adju stable cowl 
flaps that open to a ratio of 2 or more. Adjustable cowl flaps let us change the 
exit area in flight, which changes the cooling airflow. It is not necessa ry to 
vary the cooling intake area because the cooling airflow always adjusts to 
the exit area. If you don't want the comple xity of a variable exit, try an 
exit that is 30% larger than the intake, then carefu lly reduce it during the 
flight-test program while watching the cylinder head temperatures. 
For tractor engines, the cool ing-air intake is usually located direct ly in 
front of the engine cylinders. The air is diverted over the top of the engine


<!-- p.321 -->

Weigh t 
Length 
Diame ter 
Typical prope ll er, rpm 
Applicable bhp range 
Weight 
Length 
Dia meter 
Typical propeller , rpm 
Appl icable power ra nge, kW 
Table 10 .4 Pis ton and Turbopr op Statis tical Models 
5.47 0.780 5.22 0.780 
0.32 0.424 0.49 0.424 
Width 2.6 -2 .8 ft Width 1. 4-1 .6 ft 
Heigh t 1 .8-2 . l ft Heigh t 2-2 .2 ft 
2770 2770 
60-500 10 0-300 
4.90 0.8 09 1 .67 0. 803 
0.52 0.31 0 0.35 0.37 3 
1 .7 0. 13 0 0.8 0. 12 0 
2300 
200-2000 400-5000 
Metric: x = a(power)1' (kg or m] 
3. 12 0.780 2.98 0. 780 2. 82 0.8 09 0.96 0.8 03 
I I 
0. 11 0.424 : 0. 17 0.424 0. 17 4 0.31 0 0. 12 0.373 
Width 0.8-0 .9 Width 0.4-0.5 0.5 4 0. 13 0 0.25 0.1 20 
I 
Height 0.6-0 . 7 ! Heigh t 0.6-0 .7 
2770 2770 2300 
45-370 75-225 15 0- 1 500 300-3 728 
0 
:I: 
> 
"O 
-4 
m 
::i;J 
0 
-0 
0 
-0 
c 
'iii" 
5· 
::J 
c 
::J 
c.. 
'Tl 
c 
(/) 
-< 
CJ> ..... 
CD 
3 
::J ..... 
CD 
<C 
a ..... 
a· 
::J 
w 
N


<!-- p.322 -->

322 Ai rcr aft Desig n: A Concept ual Ap proa ch 
< 
Downd raft cooling 
Up d raft cooling 
-B9)=t 
Scoop 
Pusher prope ll er 
Up d raft cool ing 
Fig. 10 .27 Piston- eng ine installation . 
by "baffles," which are flat sheets of metal that direct the airflow within the 
engine comp artment. The air then flows down through and around the cylinders into the area beneath the engine and then exits through an aft-facin g 
hole below the fuse lage. This is referred to as "downdraft" cooling. 
Downdraft cooling exits the air ben eath the fuselage, which is a highpressure area and therefore a poor place to exit air. "Updraft" cooli ng 
flows the cooling air upward through the cylinders and exits it into 
low-pressure air above the fuselage, creating more efficient cooling flow 
due to a suction effect. 
However, updraft cooling dumps hot air in front of the windscreen; this 
can heat up the cabin. An engine oil leak can coat the windscreen with black 
oil. Aircraft engines have the exhaust pipes below the cylinders, so updraft 
cooling causes the cooling air to be heated by the exhaust pipes before reaching the cylinders. 
For pusher engines, cooling is much more difficult. On the ground a 
front-mo unted propeller blows air into the cooling intakes. This is not the 
case for a pusher engine. Also, the cooling- air intakes for a pusher engine 
are at the rear of the fuselage where the bounda ry layer is thick and 
slow-m oving. For these reasons most pist on-pu shers use updraft cooling 
with a large scoop mounted below the fuselage. Internal fans are sometimes 
needed to improve cooling on pusher configurat ions. 
Figure 10.27 also shows the motor mount and firewall. The motor 
mount-us ually fabricated from welded steel tubing-t ransfers the engine 
loads to the corners of the fuselage or the longerons. Typically, the motor 
mount extends the engine forward of the firewall by about half the length of


<!-- p.323 -->

CHAP TER 1 O Prop ulsi on and Fuel System In tegr ation 323 
the engine. This extra space is used for loca tion of the battery and nosewheel 
steering linkages. 
The firewall is typically a 0.015 -in. {0.4-mm steel sheet} (stainless or 
galvanized) attached to the first structural bulkhead of the fuselage or 
nacelle. Its purpose is to prevent a fire in the engine compartment from 
damaging the aircraft structure or spreading into the rest of the aircraft. 
The firewall should not be broken with cutouts (such as for a retractable 
nosewheel) . All controls, hoses, and wires that pass through the firewall have 
to be sealed with fireproof fittings. 
Piston- engine installation is covered in depth in[51l . 
- Fuel System 
The aircraft fuel system includes the fuel tanks, fuel lines, fuel pumps, 
vents, and fuel- management controls. While these are all impor tant during 
detail design, usually the tanks themsel ves are the only componen ts that 
affect the overall aircraft layout. For some aircraft like the B-70 
(Fig. 10.28), the fuel tanks define most of the internal volume of the aircraft. 
For normal airplanes, the tanks usua lly consist of a "wet" wing box and 
perhaps a few tanks in the fuselage. Their integrati on into the aircraft 
design is a major under taking. 
There are three types of fuel tanks: discrete, bladder, and integral. 
Discrete tanks are fuel co ntainers that are sep arately fabricated and 
mounted in the aircraft by bolts or straps. Discrete tanks are normally used 
only for small general aviation and homebuilt aircraft. They are often 
shaped like the front of an airfoil and placed at the inboard wing leading 
edge, or are squar e-i sh and placed in the fuselage directly behind the 
engine and above the pilot's feet. 
Bladder tanks are made by stuffing a shaped rubber bag into a cavity in 
the structure. The rubber bag is thick, causing the loss of about 10% of the 
Fig. 10 .28 B-70 fuel system.


<!-- p.324 -->

324 Ai rcraf t Design : A Conceptu al Appr oach 
available fuel volume. Des pite this loss, bladder tanks are widely used for 
military aircraft because they can be made self-sea ling. If a bullet passes 
through a self-sea ling tank, the rubber will fill in the hole preventing a 
large fuel loss and fire hazard. This offers a major improvement in aircraft 
survivability as approxi mately a third of com bat losses are attribute d to 
hits in the fuel tanks. 
Integral tanks are cavities within the airframe structure that are sealed to 
form a fuel tank. Idea lly, an integral tank would be created simply by sealing 
existing structure such as wing boxes and cavities created between two 
fuselage bulkheads. 
Despite years of research, integral tanks are still prone to leaks as seen 
during introduction of the B- lB. Such leaks are usually fixed by having 
the production people put more sealant in the problem area. With modern 
manufactur ing methods, parts simply fit each other better so leaks are less 
of a problem. Also, molded or bonded compos ite parts cannot leak except 
where mechanica lly fastened. 
Because of the fire hazard in the event of a leak or battle damage, integral 
tanks should not be used near personnel comp artments, inlet ducts, gun bays, 
or engin es. The fire hazard of an integr al tank can be reduced by filling 
the tank with a porous foam material, but some fuel volume is lost. Appr oximately 2.5% of the fuel volume is displaced by the foam. In addition, another 
2.5% of the volume is lost because the foam tends to absorb fuel. This reduces 
the usable fuel weight. Furthermore, the foam itself weighs roughly 1.3 lb per 
cubic ft {21 kg/m 3}. 
High-p erformance airplanes including airliners and most military aircraft 
will have tanks that are slightly pressurized, usually by engine bleed air or 
small ram scoops. This helps feed the fuel to the pumps espec ially during 
mane uvers, and reduces the tendenc y of shaken fuel to foam up. It's also 
good for safety-fuel is less likely to ignite at a higher pressure. Some aircraft 
such as the C-5 and the Dassault Falcon use nitrogen instead of air in the 
tanks, to prevent fire and explosion. 
Smaller aircraft usually have unpressurized tanks for simplici ty. These 
must be vented at the oppo site side of the tank from the fuel line, just like 
a canned beverage needs to be punctured at two sides. Amusi ngly eno ugh, 
the "winglets" on the Rutan Voyager were added solely to raise the fuel 
vents above the wing tanks when the wing tips bent down to the runway 
on takeoff. Their aerod ynamic effect was negligible, as proven when they 
were broken off after takeoff for the historic round- the-world flight. 
When the engine is picked, the fuel is also determined. If a piston engine 
is chosen, then the fuel will likely be "AvGas" (aviation gasoli ne) . This is a 
highly- processed derivative of petroleum. It comes in several grades depending upon its anti-knock prop erties and suitabil ity for use in high-performance 
super charged engines. To avoid catastrophic confusion, the various grades 
are color coded with dyes-blue, purple, red, or green. Putting jet fuel into 
a gasoline engine, or vice-versa, is even worse.


<!-- p.325 -->

CHAPTE R 1 O Propulsion and Fuel Syste m In teg rati on 325 
AvGas is similar to automobile gasoline (so metimes called "MoGa s") 
but uses a different octane rating system, related to the fuel's anti-knock 
quality. AvGas isn't necess arily "better" than auto gas, and it is more expensive so many general aviation airplanes have been converted to run on auto 
gas. MoGas is also about 7% denser, so more pounds of fuel can be packed 
into the tanks provided the aircraft can handle the extra weight. 
Some worry that use of auto gas will shorten the life of an aircraft 
engine. Others say it is better because it has less lead which causes fouled 
plugs and sticking valves. Auto gas shouldn't be used in an aircraft without 
a Supplemental Type Certificate (STC) authorizing it. In some cases, no 
change to the airplane is required other than paper work. Other airplanes 
may require different fuel pumps and other modifi cations. Note that auto 
gas containing ethanol may be problema tic-check the STC. Some aircraft 
owners prefer to get their MoGa s from boat marinas because it usua lly does 
not have ethanol even if local laws require ethanol for car gasoline. 
Turbine engines normally run on a type of kerosene, also a processed 
form of petroleum but with much less .processing than AvGas. This makes 
it cheaper. This fuel is usua lly called Jet Fuel, or Aviation Turbine Fuel 
(ATF) or sometimes "AvTur." It's normally colorless or somewhat strawcolored. The various types of jet fuel have different freezing points, smoke 
points, and flash points based on their exact chemist ry. 
Commercia l jet aircraft in the USA common ly use the variant called 
"Jet A" whereas in most of the rest of the world, "Jet A-1" is used. Jet A 
goes back to the 195 0s. Jet A-1 is similar but with a lower freezing point 
and an anti- static additive . 
For operation in extremely cold climates, Jet B has a much lower freezing 
point. This is actually a blend of kerosene and gasoline, roughly 30- 70, which 
makes it a bit more dangerous and fire-prone. 
For military use, jet fuels are called JP (Jet Prop ellant) and are mostly 
similar to civilian fuels. JP-8 resembles Jet A and is widely used by the US 
Military. JP-4, now obs olete but until rece ntly the standard fuel for the 
USAF, is much like Jet B but with a 50-50 blend of kerosene and gasoline. 
JP-5 is a special fuel for aircraft carrier operations, formulated to have 
reduced fire risk (high flash point) . It has no civilian coun terp art for 
obvious reasons. JP-6 and JP-7 were developed for high speed aircraft, the 
B-70 and SR-71 respect ively. JP- 10 is an exotic gas turbine fuel for missiles, 
formulated for high dens ity to give greater range. The various synthetic and 
biofuels are discussed in the next subchapter. 
The fuel for diesel piston engines is actually a kerosene similar to jet fuel. 
Since it is less refined than AvGas, diesel fuel is inhere ntly cheaper. Som e 
manufacturers are developing diesel aircraft piston engines that run on 
actual jet fuel, which is more available at airports. 
One imp ortant operational factor for aircraft fuel is water contaminat ion. 
Liquid water in the tanks is a common cause of crashes. Gen eral aviation 
aircraft are designed so that any water, which is heavier than gasoline, will


<!-- p.326 -->

326 Airc raft Des ign : A Conce ptual Approach 
find its way to drains located at the bottom of the tanks. A normal part of 
the preflight check is to drain some fuel into a clear tube and visually 
check for water cont aminat ion. Also, it is always wise to fill the tanks 
before lea ving the airplane overnight, so that water vapor in the air doesn' t 
condense in the tanks . 
Even water that is dissol ved into the fuel in minute quantities poses a 
threat. At altitude the temperature of the fuel will drop, causing the dissol ved 
water to condense out. Then it can freeze and block the fuel lines. For this 
reason, fuel heaters are commo nly used. There are also chemical tests that 
can detect water in jet fuel. 
The required volume of fuel tankage in a design layout is found from the 
fuel weight calculated during the mission sizing process, applied to the 
dens ity of the selected fuel. Table 10.5 is based upon data from [l?2] and 
provides reasonable average fuel densities at various temperatures. The 
bottom part of the table has the data converted for layout purposes, using 
the fact that 7.48 gallons occupies 1 ft3. The metric system makes this easy 
since 1000 liters* equals 1 m 3. 
There is a subst antial variation of fuel dens ity with temperature. Densit y 
is lower on a hotter day, so fewer pounds {or kilograms} of fuel will fit into the 
same tank. The aircraft's range is reduced, despite having "full tanks ." Even 
worse, cold fuel pumped into the tanks from und erground storage will 
warm up, expand, and run out on the ground. We normally use the 15° C 
values for aircraft layout and provide 3-5% of extra fuel volume to allow 
for this. On the F- 18 and several airliners, there are separate "expansion" 
tanks in the vertical tail into which the fuel can flow as it warms and expands. 
If fuel tanks of simple geom etry are used, the tank volume can be calculated direct ly. Wing-box fuel volume can be appro ximated by assuming 
a tapered box shape. For comple x integral and bladder tanks, the tank 
volume is determined using a fuel -volume plot as shown in Fig. 10.29. This 
is con structed by measur ing the cross -sec tional area of the tanks at various 
fuselage loc ations, then plotting those cross-s ectional areas on a volume 
plot similar to the aircraft volume plot already discussed. 
If a discrete tank is used, the available internal volume can be calculated by subtracting the wall thickness from the external dimensions. For 
integral and bladder tanks, the available tank volume must be reduced 
from the measured value to allow for wall thickness, internal structure, and 
bladder thickness. 
A rule of thumb is to assume that 85% of the volume measured to the 
external skin surface is usable for integral wing tanks and 92% is usable for 
integral fuse lage tanks . If bladder tanks are used, the values become 77% 
for wing tanks and 83% for fuselage tanks. 
*T he liter, or litre in official SI spelling, is a cubic decimeter or roughly a quart in the fps system. 
We rarely use decimeters otherwise. The SI kilogram is defined as the weight of one liter of ice cold 
water.


<!-- p.327 -->

AvGas 6. 13 
JET A-1 6.89 
JP-4/JET B 6.5 2 
JP-5 6.98 
JP-8/JET A 6.9 4 
JP-1 0 8.03 
AvGas 45 .8 
I 
JET A-1 51 .6 
I 
I I 
JP-4/JE T B 48.8 
JP-5 52.2 
JP-8/JE T A 51 .9 
JP-1 0 60 . 1 
Table 10 .5 Average Fuel Densities in (lb/gal) or [kg/l iter) 
{ - l8 °C } 
0.734 6.01 0.720 5. 93 
0.826 6.78 0.81 3 6.70 
0.781 6.40 0.767 6.32 
0.836 6.87 0.8 23 6.7 8 
0.8 32 I 6.83 0. 81 9 fl.74 
0.962 7.94 0.951 7.85 
Averag e Fuel Densities: lb/ tt3 or {k g/m 3 } 
734 44.9 720 44.3 
826 50 .8 I 81 3 50. 1 
781 47 .9 767 47.3 
836 51 .4 I 823 50.8 
832 51 . l 81 9 50.4 
I 
962 59 .4 : 951 58.7 
{ 1 5°C } i-PJ:I .. 
0.710 5.78 0.692 
0.803 6.57 0. 787 
0.757 6. 17 0. 739 
0. 81 3 6.65 0.797 
0.8 08 6.61 0.792 
0.94 1 7.71 0.924 
710 43 .2 692 
803 49 . 1 787 
757 46. 1 739 
81 3 49.8 797 
808 49 .4 792 
94 1 57.7 924 
(") 
:z: 
> 
"ti 
.... 
m 
::.1 
.... 
0 
.,, 
0 
"'O 
c 
(ii 
a· :J 
0 
:J 
0.. 
"T1 
c 
(/) 
-< 
CJ> ..... 
<D 
3 
:J ..... 
<D 
(Q 
a ..... 
a· 
:J 
w 
N 
.....


<!-- p.328 -->

328 Aircr aft Desig n: A Con ceptu al Appr oach 
Cross-se ction 
ar ea of ta nk s Tank volum e = ar ea under each cu rve 
Tank e.g. is centroid of ar ea plo t Tota l fuel e.g. must be near air craf t e.g. 
Fig. 10 .29 Fue l-tank volume pl otting . 
Note in Fig. 10.29 that the fuel volume plot allows the estimation of 
the center of gravity for each fuel tank, which is the centroid of the area 
plotted for the tank. The total fuel e.g. is simply the weighted average of 
the individual tank e.g. and should be close to the aircraft e.g. 
Fuel tanks can also be used to aero dynamica lly optimize the aircraft. As 
will be discussed in Chapter 12 , the downward tail force required to trim 
most aircraft causes a subst antial "trim drag, " which is greater when the 
e.g. is more toward the front of the aircraft. This is espec ially a problem in 
supersonic flight when the wing center of lift moves toward the rear, requiring even more tail -down trim load. To minimize this trim drag, aircraft such 
as the Concor de SST and the B-70 pump fuel toward the rear when cruising 
altitu de and speed are reached. Some commercial airliners have "trim tanks" 
in the horizo ntal tail for this purpose. 
Even subsonic commercial aircraft can benefit from keeping the e.g. as far 
to the rear as stabil ity and safety will allows. The MD- 11 has a fuel tank in the 
horizo ntal tail into which fuel is pumped during cruise to keep the e.g. at the 
aft-most limit. 
One final aspect of fuel system design, for military aircraft, is the 
provision of in-f light refueling cap ability. There are two options. The U.S. 
Air Force uses a "boom" system, whereas the rest of the world uses a 
"probe-and-d rogue" system. In the boom system, special tanker aircraft are 
equipped with a fueling boom positioned at the bottom rear of the tanker 
aircraft. This is "flown" by a boom operator and extended into a recept acle


<!-- p.329 -->

CHAPTE R 1 O Propulsion and Fuel System In tegration 329 
on the top of the aircraft needing fuel (which merely holds position under the 
aircraft). The refueling receptacle must be mounted some where fairly near 
the centerline of the aircraft, toward the front, but should not be direct ly 
in front of the pilot due to the fuel that is always spilled during disconnect. 
Boom oper ation can be seen in the open ing sequence of the classic movie, 
Dr. Strange/ave. 
In the probe-and- drogue system, the tanker aircraft extends a "drogue" 
with a parachute -like "basket" having a plug-in receptacle in the middle. The 
receiving aircraft has a probe, basica lly a pipe extending forward, which 
must be flown into the basket. The probe can be fixed to the outside of the 
aircraft, but this will add a large drag penalt y. Instead, most aircraft have a 
retracting probe. The probe must be easily visible to the pilot to facilitate 
"hitting" the basket and is usua lly loca ted on the right side of the aircraft ju st 
forward of the canopy. 
Boom systems allow higher fuel flow rates and are more forgiving of pilot 
error and fatigue, but require a fleet of dedicated and expensive tanker aircraft. It is far cheaper to modify an existing airplane to carry the drogue 
system. Also, probe -and- drogue systems can be installed in pods that look 
like external fuel tanks and can be bolted onto different aircraft. This even 
allows "buddy" tanking, where, say, two F-18s take off and fly halfway to 
the target where one aircraft gives the other most of the remaining fuel 
then flies home, allowing the other aircraft to strike at a much greater 
range than otherwise possible. 
r:J Green Propul sion 
ll1fill Why Green? 
Traditional aviation fuels are all derived from petroleum-crude oil that is 
pumped out of the ground, transported around the world, and then refined into 
many substances including gasolines and kerosen es. Petroleum has a great 
advantage: it comes from the ground alread y full of the energy needed to fly. 
The processed aviation fuels have high ener gy dens ity and can be stored at 
room temperature. Furthermore, they have a long shelf life. If you gas up 
your plane but don't fly it for several months, the gas is still "good to go." 
However, petro leum-based fuels have disadvantages. Despi te tremendous 
improvements in recent decades, they still burn somewhat "dirty" and leave 
pollutants in their wake. Commercial aviation alone produces 2% of all 
man-made C02 (but this is dwarfed by natural C02 emission s). Petrole umbased fuels are, by their very nature, volatile and are prone to fire and under 
certain circumstances, even explosion. And perhaps most impor tant, much 
of our petroleum is obtained from far- away countries that might not 
always offer a stable and affordable supply, yet environ mental concerns 
have limited the use of many loca tions such as offshore or in the far North.


<!-- p.330 -->

330 Aircr aft Desi gn: A Con cep tual Appr oach 
Ml1t.f J F-T, GTL, and Bio fuel s 
During World War II, Ger many had this very problem. Wartime restrictions prevented the purchase of sufficient petroleum on the world market, 
so Germans made their own. Franz Fischer and Hans Tropsch had, in the 
19 20s, developed a process for making synthetic fuels from coal, and 
Germany had lots of coal. The Fischer- Tropsch process, or F-T, was used 
to make almost 10% of German fuel during the war. 
Today an impro ved F-T process allows making fuel from natural gas as 
well as coal, and diesel and je t fuel are curre ntly being produced. Such 
synthetic jet fuels even offer a reduction in emissions including nitrogen 
oxide (NOx), sulfur oxide, and hydrocarbons such as C02. The Air Force 
has flown a B-52 on a 50-50 kerosen e-FT blend and in the future plans to 
operate most of its airplanes on alternative fuels. 
F- T, when applied to natural gas, is one of several processes that go by the 
generic name gas-to-liq uids (G TL) . An unmo dified Airbus A380 was flown in 
2008 on a 60-40 mix of kerosene and GTL synthetic fuel, and a passen gercarrying commercial flight has been flown in South Africa using 100% 
synthetic fuel. 
Other alternative fuels go by the name "biofuel, " being made from organic 
matter. Some estimates predict that biofuel could eventually reduce aviation 
greenhouse gas emissions by 60-80%. But, skeptics see little advantage in 
emissions because, whatever the source, the fuel itself is a volatile hydrocarbon that releases ener gy-and carbon-b y burning. 
Ethanol is now widely blended with gasoline for cars. It is produced by 
fermentation from sugar-rich crops, mostly corn and sugarcane, leading to 
concerns about fuel needs comp eting with food production. Biofuels can 
be fermented from anything that alcohol can be made from, includi ng 
wheat, rye, and potatoes. Biofuels are also made from animal and vegetable 
fats (cooking oil), nuts, and a type of succulen t plant called jatropha. Algae 
and fungus can be converted into biofuel as well. 
Emerging processes will allow fuel production from cellulose, that is, 
nonfood sources such as waste wood and rapidly growing gra sses. If cost 
comp etitive in large -sca le production, these could revolutionize the fuels 
business. 
Certain biofuels were approved for co mmercial airliners in 2011 . A 
number of revenue-p assenger flights have been made since then, mostly 
flying on biofuels made from cooking oil and jatropha. The USAF has even 
flown an F-22 on biofuel at super sonic speeds. At pres ent, though, biofue ls 
cost about double the cost of traditi onal fuels. 
Alternative hydrocarbon fuels are being devel oped from unlikely 
sources. Waste gases from steel prod uction, coal processi ng, and the 
"burn -off" gases from oil refineries can now be processed into kerosene-li ke 
fuels. Even more exotic is jet fuel from seawater! By sep arating hydrogen 
from the water and reacting it with the dissol ved C02, a kerosene-like fuel


<!-- p.331 -->

CHAP TER 1 O Prop ulsion and Fuel System In teg rati on 33 1 
can be produced. This last process requires tremendous energy input so that 
it is proba bly economical only if combine d with a nuclear powerplant or a 
giant hydroelectric plant, but those raise their own environmen tal concerns. 
Lest the readers become too excite d-be advised that traditi onal 
petroleum-based kerosenes and gasolines are likely to remain the fuels of 
choice for the foreseeable future. They come from the ground with energy 
already included, are easy to refine into exactly the desired characteristics, 
are much cheaper, and are still available in prodigious quantities especia lly 
if additional drilling is permitted. 
Adding one more consi deration for "green" propulsion-fuels expert 
Dr. Herb Lander, developer of JP- 10, notes that we can still make vast 
improvements on petroleum-based fuels. He says that "refining technol ogy 
can essentially remove compounds that contribute to unburned hydrocarbons, mainly aromatics, sulfur compounds, and other trace ingredients. 
These can be easily removed at the refinery, but existing fuel speci fications 
need to be upgraded to reduce these troublemakers ." He also notes that jet 
fuel can be derived from the abundan - western oil shale. When he served 
as chief of the USAF synthetic fuel effort in 19 76, they flew a T-39 on JP-4 
that was produced entirely from it. 
IPUI Hydr ogen and Methane 
GTL and biofuels are still kerosenes, quite conventional as fuels except 
that they are made from sources other than oil pumped from the ground. 
Aircraft design, sizing, and performance analysis should be unchanged by 
their use. Unfortunately, they also share many of the disadvantages. GTL 
and biofuels are little if any superior to petroleu m-based fuels in terms of 
being prone to fire. Furthermore, it isn't clear yet if they really will reduce 
C02 and other unwanted emissions enough to make up for the emissions 
during their manufacture. Other alternative fuels are vastly different and 
have a large impact on the aircraft design. 
Hydrogen and methane are both candida tes, and could be used in 
turbojet, turbofan, turboprop, or even piston-prop powerplants. (Hydrogen 
fuel cells for powering electric motors are discussed in the next section.) 
Hydrogen is commonly used for rockets and has the great advantage 
of potentially having zero emissions- when combusted with oxygen the 
product is H20. Unfortunately, when hydrogen is burned with air rather 
than pure oxygen, NOx is also produced. Hopeful ly, good combustor 
design can minimize this. 
Hydrogen has some problems for aircraft applicatio ns. While it has 
higher energy density per unit mass than tradit ional aviation fuels, it has a 
much lower energy dens ity per unit volume. Liquid hydrogen has a mass 
density of only 0.59 lb/ gal {0.07 1 kg/l}, roughly 11 times as bulky as kerosene. The tanks are huge! Even when adjusted for equivalent ene rgy 
content, liquid hydrogen is still about four times as bulky as kerosene.


<!-- p.332 -->

332 Air c raf t Des ign: A Concep tual Appro ach 
However, it weighs only one -third as much to provide the same energy. If that 
translates into actual fuel weight, the weight savings could offset the weight 
and drag of the tanks- maybe. 
LH2 can be stored under extreme pressure, or as a cryogen under extremely low temper atures. Either approach makes the tanks heavy. In both cases 
they are stored under high pressure so the tanks must be either balls or 
capped cylinders. Neither geomet ry facilitates installation in an airplane, 
and high-pressure tanks are dangerous in a crash. 
Another problem with hydrogen is its production. It is not somethin g 
that you "dig up" and instead must be produced. This involves a lot of 
energy expendi ture, such as elect rolysis of water, chemical reactions between 
acids and metals, or cracking from natural gas (the most common source) . 
Once created, its storage and transpo rtation are problem atic. It doesn't have 
a long shelf life. If you "gas up" your plane but don't fly it for a month, the 
tanks are empty. In fact, you have to cons tantly supply energy to keep 
them cold and proba bly cannot park a fueled plane unatte nded. Fuelin g 
up, like for rockets, is a last- minute thing. 
Hydrogen-po wered jet airplanes have flown. In 19 56, a B-57 Canber ra 
briefly flew with one of its engines operating on liquid hydrogen. In 19 88, 
a Tu- 15 4 airliner was extens ively flown with one of its three engines 
converted to hydrogen, with a large LH2 tank occ upying the back half of 
the passe nger compa rtment. 
There have been numerous studies of hydrogen-fueled airliner s 
throug h the years, including ongoing work by Tupo lev and recent proj ects 
by Airbus and Boeing. While it seems quite feasible, the vehicle desig ns 
feature bulbous fuselages to carry the hydrogen, leading to increased drag 
and weight. Also, crash survivability is a concern. The hydrogen is super 
cold, flammable, explosi ve, and in some designs, is loca ted directly above 
the passen ger comp artment. 
For hypersonic airbreathing propulsion, liquid hydrogen is an excellent 
fuel due to its high energy vs mass, its low atomic weight, and its excellen t 
mixing and combustion prop erties. The X-43 scram jet test vehicle demonstrated LH2-powered flight at Mach 10. (The later X-5 1 was kerosenepowered but "only" reached Mach 7.) 
While at Rockwell, this author was asked to design a hydrogen-fueled 
strategic bomber as a part of a maj or USAF -fun ded study of future 
bombers. The postulated hydrogen-fueled turbofan engines seemed 
reasonable and actually had bet ter speci fic fuel consumption than the 
kerosene-fueled engines, but the required tank volume was ridiculous, 
being as much volume as the entire fuselage (Fig. 10 .30). After looking at 
numerous arrangements, it was decided to carry the hydrogen in giant 
capped cylindrical tanks like those of a launch vehicle, but for structu ral 
reasons suspended from the tip of the canard to the middle of the wing. 
This worked well but the extra wetted area of the tanks gave too much 
drag, and the idea was dropped J52,53]


<!-- p.333 -->

CHAPTER 10 Propulsion and Fuel System In teg ration 333 
Fig. 10 .30 Hyd rogen-fueled strateg ic bomber study (D. Raymer , 19 78) . 
Piston engines can also run on hydrogen, benefi tting from the low-speed 
propulsion efficiency of a large propeller. The Boeing Phantom Eye, a longduration intellig ence/su rveillance UAV, uses two modified automobile 
engines converted to hydrogen fuel. With a 15 0-ft {46-m} wingspan, it will 
fly for four days at an altitude of 65,000 ft {20,000 m}. 
Methane is a hydrocarbon gas, mostly extracted from natural gas and 
coal seams, When burned, it has less hydrocarbon emission than kerosene 
and has more speci fic energy. It is alread y used as an alternative fuel for 
road vehicles, in a highly compressed and somewhat blended form called 
liquefied natural gas (LNG). Methane liquefies at a higher temp erature 
than hydrogen, so it is easier to use in cryogenic form. Liquid methane has 
a density of about 3.53 lb/ gal {0.423 kg/I}, better than hydrogen but still 
almost twice as bulky as kerosene. 
In 1989, the same Tu- 15 4 airliner that was converted for hydrogen 
research was flown with one engine converted to LNG and was taken on 
international demo nstration flights. Tupo lev is still working on both LNG 
and hydrogen-po wered airplanes for passenger and cargo applicat ions, 
claiming large savings in operating costs. 
While biofuels, hydrogen, and methane have great poten tial for reducing 
pollution and our dependence upon petroleum-based fuels, as of now it is 
just pote ntial. Actual experience with biofuels does not yet show such a 
marked drop in emissions, Even more impor tant, when assessing pollution and energy efficienc y vs petroleum it is esse ntial to take a complete


<!-- p.334 -->

334 Aircr aft Des ign: A Conce pt ual Approach 
system- level approach, including all of the pollut ion created and energ y 
expended in producing the fuel. According to some studies, the curre nt 
production of corn-based ethanol uses almost as much petroleum as the 
petroleum subst itute it produces. Surely this cannot be efficient, espec ially 
because it results in our litera lly "burning food." However, in the moredistant future these various green fuels show great promise. 
Ml1f.ll Nuclear 
Nuclear ener gy is rarely included on peoples' lists of "green" technologies, 
but it is. Barring waste disposal and the occasion al catastrophe, it is prob ably 
the greenest of technologies in terms of its impact on the environment per 
unit power output. The ground powerplants are relatively small and, once 
const ructed, put out power for decades with only warm water as a byproduc t. 
Even with recent disasters, the total death toll from nuclear energy is still far 
lower than that from the coal and oil industries. 
However, nuclear power scares people, and the issue of waste disposal 
and the fear of even worse catastro phes means that any decision to apply 
nuclear power is a poli tical one, way beyond the scope of this book. But we 
could apply nuclear power to airplanes and do so fairly easily. The obvious 
bene fit is nearly perpetua l and pollution-free flight. The obvious problems 
are legion. 
A recent article in Scientific American [s4] suggests that nuclear power 
might be the best answer even for comm ercial aviation in the distant 
future ("-' 2050), both for environmen tal reasons and to break the dependence 
upon fossil fuels. Also, elimination of the need for refueling would have an 
environmen tal and economic benefit to airpor ts and the airline's ground 
oper ations. The article goes on to discuss the many problems, espec ially 
radiati on. Even with shielding adequate for passenger protection, the flight 
crew could soon exceed the recommended cumu lative dosages. 
A nuclear reactor makes heat. We can use that heat to make mechanical 
power and turn a prop eller. Better yet, we can ju st heat up the air and crea te 
thrust. Like a je t engine, we need to compress the air before heating it. After 
the air is heated, we could extract mechanical power with a turbine, basica lly 
creating a nuclear-fueled turbojet, or we could make mechanical power 
direct ly from the reactor and use that to spin the compressor. 
The air can be heated by passing it through the nuclear core direct ly, or by 
passing it through a heat exchanger that uses sodium, liquid metal, or highly 
pressurized water to carry heat from the reactor. The direct heating approach 
is simpler, but since the air actually passes through the reactor, radioa ctive 
exhaust is a problem. The indirect approach should produce radiat ion-fr ee 
exhaust, but the plumbing asso ciated with the heat exchanger fluid creates 
challenging engineering tasks. 
While largely forgotten today, there were major efforts in the Unite d 
States and the Soviet Union to develop atomic-p owered airplanes. Over a


<!-- p.335 -->

CHAP TER 10 Prop ulsion and Fuel System In teg rati on 335 
15-year period starting in 1946, the U.S. government spent about $10 billion 
(today's dollars) in research, succe ssfully ground tested the direct heating 
approach using two modified General Elect ric J47 turboj et engines, and 
flew an aircraft with an oper ating 3-M W reactor. In this modified B- 36, 
the reacto r didn't power the airplane but was used for testing nuclear 
operations and shielding con cepts. It required almost 25,000 lb {11, 300 kg} 
of shielding in the cockpit alone. 
A follow- on proj ect was going to actually fly an airplane converted to 
use the nuclear turboj ets mentioned above, but was cancelled. The chosen 
airplane was the B-60, a swept-wing jet derivative of the B-36 and with a 
maximum takeoff gross weight of 300,000 lb {1 36,000 kg} . The total propulsion system would have weighed 16 5,000 lb {75 ,000 kg} , including 10 ,000 lb 
{4500 kg} for the reactor; 60,000 lb {27 ,000 kg} of reactor shielding; and 
37,000 lb {1 6,800 kg} of crew shielding. The nuclear turboj ets thems elves 
would have weighed 18 ,000 lb {8,10 0 kg} plus 40,000 lb {18, 100 kg} for 
inlet ducts and equipment. 
This total nuclear propulsion systeJTI would have been just over 50% of 
the aircraft's gross weight. This is less than the 65% fraction of the equivalent 
B-52 (total propulsion system including fuel) . Also, the 50% value for the 
nuclear airplane reflects a first- of-a-kind test aircraft and would likely be 
reduced with additional experience and newer technologies. 
However, for current com mercial airliners this total propulsion weight 
fraction is only about 35-45%, and a nuclear-p owered commercial aircraft would proba bly need far more shielding and far more extra weight 
allocated to safety than a military aircraft. Ground nuclear powerplants are 
supposedly designed to be strong eno ugh to take a direct strike by a commercial airliner-p erhaps nuclear airliners would have to be designed to be 
radiation- safe in the event of a similar straight -in crash. 
During the Rockwell future bomber study mentioned above, a nuclearpowered strategic bomber was also designed. l53l This was intended to 
improve first- strike survivability, by "flushing" the bombers at the first sign 
of international tension and letting them remain aloft for days. The propulsion department worked with one of the engine companies to define a 
modern airborne nuclear power plant and turbofan engine, upda ting the 
work done in the 195 0s. This author took that propulsion system and 
created the design shown in Fig. 10.3 1, based on the Rockwell Delta Spanloader stealth bomber concept (Fig. 22.3) and carrying a 50,000-lb payload. 
This resulted in a 65% propulsion weight fraction, including shieldi ng 
sufficient to hold yearly crew radiation dose levels to the US-N RC Occupational Dose Limit of 5 rem/year. This assumed about 10 h of flight time 
per month, lower than typical today, but it would be augmented by simulator time or flight hours in a convention ally powered variant of the same 
design. Allowing a 20-t imes greater dosage level for an airplane to be 
flown only during actual "flush" events, that propulsion weight fraction is 
reduced to 55%.


<!-- p.336 -->

336 Aircr aft Des ign: A Concep tual Approach 
Crew 
shield 
Fig. 10 .31 Nuclear -powered stea lth flying wing bomber study (D. Raymer , 19 78). 
This desi gn study was considered "interestin g," but at that time nobod y 
in the government wanted to pursue such a controversial approach. l3l 
Note: The material on Elect ric Aircraft which was in this location in the 
previous edition has been greatly expanded and moved to its own section, 
Chapter 20, 
What We've Learned 
We've been shown the basics of aircraft propulsion selection and installation, 
including the engine layout itself, plus the sizing of the inlet duct or propeller. 
Fuel-t ank layout also has a big effect on the design and must be done proper ly.
