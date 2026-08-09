# Raymer Ch.21 - VTOL Aircraft Design

*Converted from `Daniel P. Raymer - Aircraft Design_ A Conceptual Approach (2018, American Institute of Aeronautics and Astronautics Inc.) - libgen.li.pdf` by `tools/pdf_to_md.py`. Page markers are printed page numbers.*


<!-- p.765 -->

Vertical FlightJet and Prop 
• Verti cal ftight offers gr eat oper ationa l uti lity, and eve n gr eater ai rcraft 
des ign penalties. 
• Helic opter s ar e far mor e efficient for vertica l ftigh t but ca nn ot go fast . 
• Hover ing on je t thrust is costly , and the vertica l ftight eq ui pmen t pena l izes the design 
in many ways . 
f 111 Introd ucti on 
T he operational benefits of an ability to take off and land vertically are 
self-evident. Conventiona l aircraft must operate from a relatively 
small number of airpo rts or airbases with long paved runways. For 
commercial transpor tatiQfl, the airport is rarely 
where you actually wish to go and is usually crowded, causing delays in the air and on the ground. 
The military airbase is vulnerable to attack, and 
during a wartime situation the time spent cruising 
to and from the in-the- rear airbase increases the 
required aircraft range and also increases the 
amount of time it takes for the aircraft to respond 
to a call for support. 
The first type of vertical takeoff heavier-t han- air 
Vertical take-off is 
necessary only in 
a circus. -P. 
Dementyev, 
Chairman of State 
Committee of 
Aircraft Technology, 
USSR 
aircraft was the helicopt er, which was concei ved by Leon ardo da Vinci but not 
regularly used until shortly after World War II. The helicopter rapidly proved 
its worth for rescue operations and short- range point-to-point transportation, 
but its inherent speed and range limitations restricted its applicat ion. 
For aircraft designers, vertical flight in an otherwise "normal" airplane 
remains an elusi ve and challenging goal. A clear "best" solution for vertical 
763


<!-- p.766 -->

764 Aircr aft Des ign: A Conceptual Approach 
lift has yet to emerge. For propeller- powered aircraft, the tilt-rotor con cept 
has proven to be a good compromise between helicopter-like vertical flight 
and efficient wing-borne cruise. This is the basis of the combat-pro ven 
V-22 Osp rey, but other approaches are still being pursued and might ultimately prove superior. 
For jet aircraft, a "best" solution is even more elusive. Instead, there are 
many different vertical- lift con cepts, some tested and some not, available 
for incorpor ation into a new design. Selection of a best concept depends 
upon the intended mission and oper ational enviro nment as well as the technical details of the selected lift concept. Ultimately, system-le vel trade studies 
should be used to select the best approach for a new proj ect. But be suspicious of the latest innovation- new ideas always weigh more than we think 
they will, and weight is death to vertical takeoff airplanes. 
,,..,.. 21 .2 Jet VTOL 
#Jf JI In trod uction 
Vertical-t akeoff-and- landing (VTOL) capab ility was pursued almost as 
soon as the jet was invented. The jet engine's high thrust-to -weight ratio 
seems to lend itself to vertical flight, and both military and commerc ial customers would be delighted to be able to take off and land without the need for 
long runways. 
To date, there have only been three* oper ational jet VTOL designs: 
the British Harrier, the Russian YAK 38, and the US F-35B. The first two 
are subsonic aircraft and have limited range. Were it not for their vertical 
flight capabilit y and modern avionics, their overall flight performance 
would place them with aircraft of the mid 19 50's. 
A VTOL aircraft with supersonic capabilities is an orders- of-magnitude 
more difficult chall enge. Although the VTOL Mirage III-V flew at Mach 2 
back in 19 66, it was not considered practical eno ugh for operational development. Sim ilarly, the Russian YAK- 141 flew at Ml.7 but was cancel led as 
impractical and too expensive. For almost half a 
century after 19 66, not a single supersonic VTOL 
aircraft entered service. 
This is largely because the engine modifications 
and extra equipmen t for VTOL flight impose a huge 
weight penalty. This adds to the aircraft empty 
weight, and that imposes an even greater penalty as a 
result of the leverage effect on sized TOGW . There is 
also the increased internal volume required for the 
Supersonic STOVL: 
The Future is Now. 
-D. Raymer, 
slightly premature 
article title Aerospace America, 
Aug. 19 90 
vertical-lift apparatus and vertical- flight fuel. Finally, most conce pts for vertical 
lift tend to increase the aircraft's cross-s ectional area near the aircraft's wing, 
and that increases the supersonic wave drag. It has simply not been possible 
*I n all previous editions of the book, this said "two." Welcome aboard, F-35 B!


<!-- p.767 -->

CHAP TER 21 Vertical Flig ht-Jet and Prop 765 
up to now to provide both vertical flight and supers onic forward flight in an 
operational aircraft of any usable range. 
Thanks to broad advances in engines, structures, flight control, and 
VTOL technolog y, we can finally say "The Future Is Now! ". l130l The F-35B 
fighter, which is both VTOL and supersonic, has reached initial operational 
capability. While a huge improvement over the subsonic Harriers it will 
replace, it suffers by comparison to the similar but non-VTOL F-35 A. The 
B has about a third less fuel volume, lost to the vertical flight equipment. 
To save empty weight it was redesigned to a lower structural load factor capability-7 g rather than the 9 g of the A model. The B model can carry only 
1,000 lb weapons interna lly versus the 2,000 lb-ers of the A model. It has 
no internal gun, unlike the A, and must "strap on" a gun pod for missions 
where it may be needed, giving up even more range or payload. 
But for missions where a long runway or a huge aircraft carrier is not an 
option, the F-35B is the only option, and it brings stealth, incredible avionics, 
and advanced systems to the theater. Nothing else compares. 
As for commercial jet VTOL appli catio ns, passen ger aircraft that can fly 
off a downtown rooftop-t hat remains for the distant future, if ever. 
f lf II VTOL Term ino logy 
VTOL refers to a capability for vertical takeoff and landing, as opposed to 
conventional takeoff and landing (CTOL). 
An aircraft that has the flexibility to perform either vertical or short 
takeoffs and landings is said to have vertical or shor t-takeoff -and- landing 
(VSTOL) capab ility. An aircraft that has insufficient lift for vertical flight at 
takeoff weight but that can land vertically at landing weight is called short 
takeoff-vertical land (STO VL) . 
The "tail -sitter" or vertical- attitude- takeoff-and- landing (V ATOL) aircraft cannot use its vertical lift capab ility to shorten a conventional takeoff 
or landing roll. In contrast, a horizontal-attit ude- takeoff-and-land (HAT OL) 
concept can usually deflect part of its thrust downward while in forward 
flight enabling it to perform a short takeoff and landing (STOL). 
f Jf U Fundam ent al Problems of VTOL Design 
A number of unique problems characterize the design and operation of 
jet VTOL aircraft. Two fundamen tal problems stand out because they tend 
to have the greatest impact upon the selection of a VTOL propulsion 
concept and upon the design and sizing of the aircraft: balance and thrust 
matching. 
Modern supersonic jet fighters have a T / W exceeding 1. 0, so it would 
seem fairly easy to point the jet exhaust downward and attain vertical 
flight. Unfortunately, this is complica ted by the balance problem.


<!-- p.768 -->

766 Airc raf t Des ign: A Concept ual Approach 
a) Forwa rd flight /7 
d:-s-c""'="TI.b) Magic finger verti cal flight 
c) Thrust location moved 
Fig. 21 .1 The bala nce problem . 
t 
Many subsonic jets and virtually all supersonic jets are designed with the 
engine at the rear, the cockpit and avionics at the nose, and the pay load 
and fuel near the center of the aircraft. This traditional layout places the 
expendables on the e.g., collo cates the parts of the aircraft requirin g 
cooling (crew and avionic s), and keeps the avionics away from the hot and 
vibrating engine. 
Figure 21.la illustrates this traditional (and usua lly optimal) layout. If the 
aircraft's thrust exceeds its weight, vertical flight could be obtained simply by 
deflecting the thrust downward, as shown in Fig. 21. lb. However, a "magic 
finger" must hold up the nose to balance the vertical thrust force at the 
tail. This balance problem is poss ibly the single most impor tant driver of 
the design of the VTOL jet fighter. 
There are really only two conceptual approaches to solving the balance 
problem. Either the thrust can som ehow be moved to the e.g. (Fig. 21.lc ), 
or an additional thrust force can be loca ted near the nose (Fig. 21. ld). 
Both of these approaches will tend to compromise the aircraft away from 
the traditi onal and usua lly optimal layout. 
(While Director of Advanced Design at Lockheed, this author had the 
crazy idea to hold up the nose with gyroscopic flywheels, like a child's toy. 
A calculation was made of the needed gyroscopic forces. The required flywheels were way too heavy. Crazy Raymer.) 
For cruise- dominated VTOL aircraft such as transpor ts, a more severe 
problem involves thrust matching. If the thrust required for vertical flight 
is provided by the same engines used for cruise, the engines will be far too 
large for efficient cruis e. 
As an example, imagine designing a VTOL transport using four of the 
TF-39 engines used in the C-5. These produce about 40,000 lb {17 8 kN} of 
thrust at sea- level static cond itions, or 160,000 lb {712 kN} altogether. If


<!-- p.769 -->

CH APTE R 21 Vertical Flig ht-Jet and Prop 767 
the aircraft is to have a typical 30% thrust surplu s for vertical flight (T / 
W == 1. 3), then the aircraft can weigh no more than 12 3,077 lb {55,827 kg} 
at takeoff. Note that this is far less than the C-5 at 764,000 lb {346, 544 kg} . 
Assume a typical cruise L / D of 18 yields a required T / W during cruise of 
about 1/18 , or 0.056. If the aircraft weight at the beginnin g of cruise is about 
95% of the takeoff weight, then the total thrust required during cruise is only 
6,496 lb (1 23,077 x 0.95 x 0.056) {29 kN} . 
This is only 1, 624 lb {7 kN} of thrust per engine, which is about 18% of the 
available thrust for that engine at a typical cruise altitude of 35,000 ft 
(1 0,668 m}. It is doubtful that the engine would even run at that low of a 
thrust setting. 
At 35,000 ft and Mach 0.9, the best SFC for this engine would be about 
0.73 at a thrust of 9,000 lb {40 kN} per engine. The SFC at the 50% throttle 
setting is about 1. 2 {34 mg/Ns}. This is 64% worse than the SFC at the 
higher thrust setting. If the engine would run at only 18% of its available 
thrust, its SFC would be even worse than the 1. 2 value. 
Aircraft range is dire ctly propor tional to SFC. The mismatch between 
thrust for vertical flight and thrust for cruise will produce a fuel consumption 
and range penalty for a cruise- domina ted design that uses only the vectored 
thrust of its cruise engines for vertical flight. For this reason, many conceptual VTOL transpor t designs incor porate separate "lift engines" used during 
vertical flight. 
If three of the TF-39 engines in the previous example could be turned off 
during cruise (without a drag pena lty), the remaining engine could be operated at a 72% thrust setting where it gets an SFC of about 0.8 {23 mg/N s}. 
This is a big improvement over all engines being used for both lift and 
cruise. However, the use of separate lift engines introduces additional 
problems, as discussed later. 
There are numerous other problems associated with VTOL aircraft 
design including transiti -n, control, suckdown, hot gas ingestion, FOD, 
inlet flow matching, and ground erosion. These are discussed next following 
a brief discussion of the various VTOL jet propulsion options that are 
currently available to the designer. 
#Jf JI VTOL Jet Propulsion Options 
Broadly spea king, jet VTOL con cepts can be divided into those that 
utilize fairly conventional engines and those that use engines modified so 
that the fan and core air are split, with the fan air ducted and exhausted 
from some place separate from the core air. 
The conventional-en gine VTOL con cepts that do not use additional lift 
engines for vertical flight must have a net takeoff T / W in excess of 1. 0. 
If the jet exhaust is not diverted to some other loca tion for vertical flight, 
the aircraft must either be a tail sitter (V ATOL) or have the engine 
exhaust at the aircraft e.g. and capable of vectoring downward for vertical


<!-- p.770 -->

768 Air craft Des ign: A Concep tual Approach 
flight. This can be accomplished by using a vectoring nozzle or nacelle s that 
tilt (Fig. 21.2). 
The YAK- 36 and the X- 14 research aircraft had vectoring nozzles at the 
e.g., with the engines out in front. This is prob ably not a good arrang ement 
for most applications because the cockpit winds up in back, for balanc e, and 
thus does not provide accept able visibil ity for the pilot. Also, in forward flight 
the jet exhaust scrubs alongside the fuselage, causing thermal and acoustic 
problems. 
An alternat ive approach is to place the nozzles at the center of gravity and 
put the engine in the rear fuselage as on a regular aircraft, but installed backward! This RIVET concept offers design simplic ity, reduced weight, ease of 
transit ion, and inherent vectoring in forward flight (VIFF) . However , inlet 
duct losses of 5% or more will be caused by the 180-d eg bend required 
to supply air to a backwards engine. Sizing studies [13 0, 142] indicate 
that, despite these duct losses, RIVE T offers a viable option for super sonic 
V/STOL. 
Tilt nacelles, although heavy, might be the best compromise for some 
applicat ions. Grumman pursued a tilt-nacelle concept for naval applicatio ns 
for a number of years, even flying a subscale model. 
Some VTOL concepts provide a means of diverting the exhaust flow to 
gain vertical lift. This is gene rally done by a retracting blocker device in 
the engine that shuts off the flow through the rearward-facing nozzle. The 
flow is then diverted forward through internal ducting (Fig. 21 .3). 
a) Tail si tter 
b) Vectored th rust at e.g. 
c) Tilt nac elle at e.g. 
Fig. 21 .2 Conv entional engi ne, no li ft engine, no flow di version.


<!-- p.771 -->

a) Unaugme nted flow 
b) Ti p-driven fa n 
CHAP TER 21 Vertica l Flig ht-Jet and Prop 769 
Fig. 21 .3 Conven tiona l engine, no li ft engi nes, flow diversion used . 
The diverted flow can be exhausted directly downwards, or it can be "augmented" by either a gas- driven fan or an ejector. Both of these can increase 
the thrust obtained from the diverted flow by using the energy of the 
exhaust flow to accelera te a larger mass of air. This augments thrust by 
increasing the propulsi ve efficie ncy, as explained by Eq, (1 3.4), 
The gas- driven fan is a ducted fan that is turned by turbine blades spun 
by diverted engine exhaust or sometimes, diverted com pressor air. The gasdriven fan's turbine blades can be inside the fan or out at the tips of the fan 
blades, in which case it is sometimes called a tip- driven fan. 
The Ryan XV-SA used tip-driven fans and attained an "augmentation 
ratio" of almost three, that is, the lifting thrust attained with the tip- driven 
fans was almost three times the thrust produced by the jet engines alone. 
This is prob ably the highest augmentation ratio ever obtained for a jet 
VTOL design. The XV-SA was being considered for rescue oper ations 
where its combina tion of high forward speed and hover capab ility would 
be beneficial, but during tests, the dummy being winched into the airplane 
was somehow blown to the top of the wing and sucked into the tip- driven fan.


<!-- p.772 -->

770 Air craf t Des ign: A Concept ual Appr oach 
The ejector makes use of the viscosi ty of the air. Any exhaust jet will 
"drag" along adjacent air molecules, acceler ating the free air in its vicinity. 
The ej ector consists of a short duct with an exhaust stream blowing down 
it. Additional air is pulled by viscosi ty into the duct, accele rated, and 
ejected through a nozzle. This produces thrust greater than the thrust due 
to the jet exhaust alone. 
While ejectors promise theoretical augmentation ratios of 3 or more, a 
more realistic value ranges from about 1. 3 to perhaps 2.2. The Rockwell 
XFV- 12A featured ejectors along the entire span of the wing and canard. 
It was expected to produce a high value of augmentation rat io. The actual 
value achie ved was only about 1. 5, and it never flew. 
Both ejectors and gas-driven fans are heavy and tend to chop up the aircraft 
structure. Also, the internal ducting is bulky and poses a thermal problem. 
However, ejectors and gas-driven fans tend to reduce the thrust- matchin g 
problem because the engines do not have to be sized to lift the aircraft by jet 
thrust alone. The resulting improvement in cruise fuel consum ption can 
offset the weight of the ejector or gas- driven fan (but prob ably not) . 
One of the simplest ways of providing VTOL capability is to add lift engines 
to an essentially conventional aircraft (Fig. 21. 4). This brute-force approach 
was used in the Mirage III -V. Obviously, the separate lift engines add considerable weight and volume to the design, but the forward-flight engine can be 
sized for efficient cruise, thus solving the thrust-matching problem. 
Because the lift engines are designed for a single operating condition, 
they can be highly optimized for that cond ition. Existing lift engines have 
unins talled engine T/W on the order of 15, compared to about 6-8 for 
a typical forward- flight engine. Future lift engines are expected to have 
engine T / W of 25 or more. Inst allation including door s and a vectoring lift 
nozzle will roughly double the weight. 
The lift- engines -on ly approach seems rather silly. The airplane has a 
large jet engine for forward flight, but it is turned off for takeoff. If the forwardflight engine is fitted with some means for vectoring its thrust downward for 
takeoff, then the lift engines can be fewer or smaller. For balance reasons, the 
lift engines will be placed forward, proba bly ju st behind the cockpit. This is 
known as "lift plus lift /cruise" (L + L/C) and was used on the operational 
YAK-38 and the supersonic but ultimately unsuccess ful YAK- 141 . 
Numerous studies going back many years have identified L + L/C as a 
good and maybe the best approach for supersonic VTOL. It uses the lift of 
the main engine plus the extra lift of the lift engines (one or more), in a 
design that is not compromised away from a "normal" aircraft configuration. 
Geor ge Spangenber g, legen dary director of Naval Air Systems Command's 
Evaluation Divis ion, wrote, "If a supersonic V /S TOL fighter capability is 
required, it is probable that the lift plus lift cruise configurat ion is still the 
most promising. " 
A problem with L + L/C: If a lift engine should fail during vertical 
flight or transition, the aircraft would inst antly pitch nose down. The


<!-- p.773 -->

a) Sepa rate li ft engine s 
b) L + L/C (vectored) 
c) L + L/C (tilt nacelle) 
c::::: 
C::J 
CH APTER 21 Verti cal Flig ht-Jet and Prop 771 
J 
LI 
I I 
• 
Fig. 21 .4 Conven tional engine with li ft eng ine s. 
Yakovlev designs have an automatic ejection sea t to save the pilot in this 
event. To be fair, engine failure in any jet VTOL des ign requires immedia te 
ejection. 
During transition from hover to forward flight, the lift/ cruise engine's 
thrust is being vectored rearward, decreasing the vertical component of 
thrust. Because the lift/ cruise engine is at the back of the aircraft, there 
might be a nose-up pitching moment. Prob ably vectoring should be added 
to the lift engine to impro ve transition. 
If rearward vectoring is added to the lift engine, its thrust can be used to 
return to base in the event that the cruise engine fails. No other VTOL 
appr oach allows this. 
Perhaps the main problem with L + L/C is that the aircraft oper ators 
would rather not have to provide maintenance and suppor t for two types of 
engines in one aircraft. This was consid ered a serious dis advantage in the 
early downselect for the JSF /F-35 program. However, any choice should be 
based on the maintenance of the total system, and all VTOL concepts have 
problems in this area.


<!-- p.774 -->

772 Aircr aft Desig n: A Concept ual Appr oach 
The "shaft- driven lift fan" (SDLF) is bas ically L + L/C , but the front lift 
engine is replaced with a "fan, " which is really more like a jet engine compressor than a shrouded propeller. This is mechanica lly spun by a drivesh aft that 
is powered by an extra turbine in the engine exhaust. For horizo ntal flight the 
fan drive is declutched, and the now-unloaded turbine spins freely. 
Figure 21. 5 shows an early Lockheed SDLF concept [i3o] with stealth 
shaping, and of course, today's F-35B uses SDLF. 
SDLF has many of the bene fits of L + L/C but avoids the higher temper atures and maintenance of a separate lift engine. However, the shaft, clutch, 
gearbox, extra turbine, and the fan all add to the maintenance, which must 
be included in a system-le vel com parison to the other options for jet 
VTOL. Also, the return-to-base cap ability of L + L/C is lost. 
When the fan is engaged, mechanical power is extracted from the engine 
exhaust and applied to a larger amount of air, augmenting the thrust as 
explained by Eq. (1 3.4). Available F-35B data indica te a 1. 4 augmentatio n 
factor, but this augmentation produces less total lift than would be obtaine d 
by a same-size lift engine. 
Fig. 21 .5 Ea rly Lockheed shaf t-driven li ft fan STOVL fig hter concept .


<!-- p.775 -->

a) Vectored thrust 
Core 
., 
I 
..I 
CHAPTER 21 Verti cal Flig ht-Jet and Prop 773 
b) Tandem fan 
Core 
Fig. 21 .6 Split -flow engi nes (vectored fan air ). 
Interestingly, SDLF is slightly related to a 1956 design called the "Gyroptere," which had four lift fans mechanically powered by a shaft coming 
from a turbine engine. These rotated rearward for forward flight, but the 
design, never built, was found to be clumsy and heavy. Its concept of fourpost vectored thrust actually inspired the invention of the Pegasus engine 
used in the Harrier, described next. 
A number of VTOL propulsion concept s are based upon a "split-f low" 
modific ation to the turbofan engine. The airflow from the fan is split away 
from the core airflow and used in some fashion to address the balance 
and/or thrust-matching pr9blems. 
One such approach exhausts the fan air separately and provides a means 
for vectoring it downward for vertical flight (Fig. 21 .6a). The A V-8 Harrier 
uses the high- bypass Pegasus engine in which the fan air and core air are 
each separately vectored through "elbo w" nozzles (desc ribed later) . This 
permits nearly instantaneous vectoring of thrust with no mode changes 
(such as starting a lift engine or diverting air into an ejector) . This approach 
also simplifies transition and enhances maneu verability. 
On the negative side, the Pegasus-t ype engine suffers the thrust-matching 
problem because the engine thrust must provide all of the required lifting 
force. Also, the engine must straddle the aircraft e.g. This increases the 
aircraft's cross-s ectional area right at the wing loca tion and thus increases 
supersonic wave drag. The successful Harrier is subsonic so this isn't a 
problem. Despi te years of design studies, no viable supersonic configuration 
based on the split-f low approach was ever found. 
It is possi ble to augment the thrust of such an engine by essentially provid ing an "afterburner" for the fan and core airflows in so-ca lled plenum-ch amber


<!-- p.776 -->

774 Ai rcraf t Desi gn: A Concep tu al Approach 
burning (PCB). The desirability of such high-temperature exhaust passing next 
to the aircraft skins or blowing down on the landing site is debatable. 
Another means of providing afterburning to the Pega sus-t ype split flow 
engine is to change it to a conventional engine for forward flight, shutting 
off the side nozzles and ducting both fan and core air together. Then a conventional afterburner can be added. However, this requires that the engine be 
sized for vertical flight without after burning, leading to penalties in fuel efficienc y, weight, and cost. 
A close relative of the vector ed-t hrust split-f low engine is the tandem fan 
(Fig. 21 .6b), a dual- cycle engine that features an additional fan ahead of the 
regular one. During forward flight, the front fan acts to "superchar ge" the 
rear fan and engine core. 
For vertical flight the flow from the front fan is diverted by blocker doors 
and exits from a downward -facing front nozzle. Auxili ary doors open to 
provide air to the rear fan and engine core. This has the effect of increasin g 
the total amount of air that the engine acts upon and therefore increasing the 
thrust efficie ncy. 
The tandem fan is fairly heavy compared to a normal engine, but does 
provide a clever means of augmenting the vertical lift and of moving the 
center of vertical lift forward. The tandem fan engine has a much higher 
effective bypass ratio when operating in vertical than in forward flight. A 
modified version of the tandem fan called the hybrid fan (Fig. 21.6 c) 
permits the high- bypass mode to be used in forward flight. 
In the remaining class of jet VTOL propulsion con cepts, the engine 
airflow is sp lit, and the fan air is ducted away from the core air (Fig. 21 .7). 
a) Rem ote aug ment ed lif t system-RALS c) Ejector 
ID TI -; -'----, 
b) Tip-d riven fan 
Fig. 21 .7 Split -flo w engi nes (div erted fan air ).


<!-- p.777 -->

CHAPT ER 21 Verti cal Flig ht-Jet and Prop 775 
The core air is exited through a vectoring nozzle and is deflected downward 
for vertical flight. 
In forward flight the fan air goes out an aft-facing nozzle, whereas in vertical flight the fan air is ducted forward for balance. The fan air is usually augmented in some fashion to increase total thrust in vertical flight. The remote 
augmented lift system (RALS) acts like an afterburner. Fuel is added to the 
fan air and burned before exiting through a front nozzle. Gas- driven fans 
and ejectors can also be used to augment the fan- air thrust. These act in 
the manner already described. 
In addition to the concepts just descr ibed, there are many possi ble combinations of these basic VTOL propulsion scheme s. An advanced Harrierlike superson ic fighter was proposed to incor porate a PCB Pega sus-t ype 
engine as well as se parate lift engines. The astounding Dornier Do 31, 
designed to carry 36 soldiers into combat, flew in 19 67 with two Pegasus 
engines and eight Rolls Royce lift engin es. The noise when hovering must 
have been unbel ievable. This, the only vertical takeoff jet transpor t ever 
built, is also unusual in that it never crashed during its flight-test program 
and is hono rably retired to a museum near Munich. 
#lf JJ Vectoring No zzle Types 
The selection of the type of nozzle -vectoring mechanism is almost as 
important to a VTOL aircraft desi gn as the type of propulsion system. The 
ideal vectorin g mechanism would weigh little more than a conventional 
nozzle and would provide continuous vectoring from 0 to over 90 deg with 
negligible thrust loss. Such a nozzle has yet to be des igned. 
The common types of VTOL nozzle are shown in Fig. 21. 8. The most 
obvious means of vectoring the thrust, vectoring flaps (Fig. 21 .8a), deflect 
the engine flow much as wi_ng flaps deflect the external airflow. These vectoring flaps can be an integral part of the nozzle system, as shown. This type of 
vectoring system intro duces a thrust loss of ro ughly 3-6% when vectored 
90 deg. 
The vectoring flaps can also be external to the nozzle as a part of the wing 
flap system. This approach was used on the XC- 15 transpor t protot ype. 
Although this was not a VTOL aircraft, its wing flap system was able to 
turn the engine flow more than 60 deg for STOL landin gs. This, combined 
with a landing gear that permits a 30-deg nose-up posi tion, would provide 
the required 90 deg of total thrust vectoring for vertical flight. 
The bucket vectoring mechanism (Fig. 21.8b) is similar to the commo nly 
used clams hell thrust reverser. The great advantage of this concept is that 
the flow turning forces are all carried through the hinge line; thus, the actuator can be fairly small. Also, the bucket can be desi gned with a smooth 
turning surface to raise the turning efficienc y. A bucket vectoring nozzle 
can be desi gned to have a thrust loss of only about 2-3% when vecto red 
90 deg.


<!-- p.778 -->

716 Ai rc raft De sign : A Conc eptu al Appr oach 
a) Vecto ri ng flaps c) Rot ating 
c-I- ]-.. 
__,. 
~ ~ 
' 
[10 .... b) Bu cket d) Ventr al 
I!)-+ 1m: ]--... 
Side 
DD view s 
ct) YD 
' 
' 
Fig. 21 .8 Vectoring nozzles. 
Figure 21. 8c shows an axisymmetric vectoring system like that used on 
the Yak-41 and F-35B. The round tailp ipe is broken along slanted lines 
into three pieces, as shown. The three pieces are conn ected with circular 
rotating-ring bearings so that the middle (shaded) piece can be rotated 
about its longitudinal axis while the other parts remain unrot ated. This 
causes the middle and end pieces of the tailp ipe to vector downward as 
shown. Because the tailpipe is esse ntially round, it is lighter than other 
forms of VTOL nozzle. This has a 3-5% thrust loss when vectored 90 deg. 
The ventral nozzle (Fig. 21 .8d ) is simply a hole in the bottom of the 
tailpipe leading to a downwa rd-facing nozzle. To force the exhaust out the 
ventral nozzle, the regular exhaust is blocked off with some type of plate 
or door. The ventral nozzle has a thrust loss on the order of 3-6% when 
vectored 90 deg. 
To reduce hot- gas ingestion and damage to the runway, an afterburner is 
not normally used for vertical lift. A ventral nozzle can therefore be placed 
upstream (forward) of the afterburner. This moves the vertical thrust substantially forward compared to a vectoring nozzle at the end of the entire 
engine. That helps the balance problem. 
The "elbow" nozzle is used on the Pegasus engine in the highly successful 
A V-8 Harrier. In the elbow nozzle the flow is turned 90 deg outboard (see top 
view in Fig. 21 .8e) . A circular ring bearing conne cts to the movable part of the 
nozzle, which turns the flow 90 deg back to the freest ream direction. To 
vector the flow downward, the ring bearing is rotated 90 deg, as shown.


<!-- p.779 -->

CH APTE R 21 Vertical Flig ht-Jet and Prop 777 
The elbow nozzle is simple and lightweight and requires a minimum 
of actuato r force for vectoring. However, the flow is always being turned 
through a total of 180 deg, even in forward flight. Because of this, the 
engine is always suffering a thrust loss of approxima tely 6-8%. All of the 
other types of vectoring nozzle only impose a thrust loss during vertical flight. 
Another alternative is to provide elbow nozzles that are only used during 
vertical flight. A blocker door like that used for the ventral nozzle can divert 
the airflow from a conventional nozzle to the elbow nozzles. Like the ventral 
nozzle, the "part-time" elbow nozzles can be located forward of the afterburner for balance. The use of a conventional nozzle in forward flight saves fuel 
during cruise. This can more than compensa te for the extra nozzle weight. 
#Jf II Suckdown and Fount ain Lift 
The VTOL aircraft in hover is not in stagnant air. The jet exhaust that 
supports the aircraft also accelera tes the air mass around it. This entrainment 
is due to viscosity and is strongest near the exhaust plume, producing a 
downward flowfield about the aircraft (Fig. 21 .9a). 
This downward flowfield pushes down on the aircraft with a "vertical 
drag" force equival ent to a loss of typically 2-6% of the lift thrust. The magnitude of this vertical drag force depends largely upon the relative loca tions of 
the exhaust nozzles and the wing. If the nozzles are right under the wing, the 
entrained airflow will exert a large downward force. 
Figure 21 .9b shows the effect of the ground on the entrained flowfield. 
The jet exhaust strikes the ground and spreads outward. This increases the 
a) Free air entr ainm ent 
c) Mu ltiple jet ground 
effects-fount ain li ft 
b) Single jet ground effects 
d) LI DS-fount ain lift 
Fig. 21 .9 Suck down and founta in li ft.


<!-- p.780 -->

778 Airc raft Des ign : A Concep tual Appro ach 
mixing between the jet exhaust and the adjacent air, which increases the 
entrainment effect. The entrained download (or "suc kdown") therefo re 
increases as the ground is approached. 
A single-jet VTOL concept can experience a 30% reduction in effective 
lift due to suckdown. Furthermore, the suckdo wn increases as the grou nd 
is appro ached-a very undes irable handling quality! 
Figure 21. 9c shows a VTOL concept with widely sepa rated multiple 
nozzles near the ground. The jet exhausts strike the ground and spread 
outward. The exhausts meet in the middle. Because there is nowhere 
else to go, they merge and rise upward, forming a "foun tain" under the 
aircraft. 
This fountain pushes upward on the aircraft with a magnitude that will 
often cancel the suckdo wn force. The strength of the fountain lift depends 
upon the exact arrangement of the nozzles and the shape of the fuselage. 
Lower- fuselage shaping that makes it more difficult for the fountain to 
flow around the fuselage will increase the fountain effect. For example, 
square lower corners are better than round ones. 
Fountain lift increases as the ground is approached. This desirable handling quality coun ters the undesirable effect of suckdown. 
The fountain lift can be increased even more by the use of lift improvement devices (LIDS) (called cushion augme ntation devices in Britain) . 
These are longitudinal strakes located along the lower fuselage corne rs 
that capture the fountain (Fig. 21. 9d). LIDS added to the A V-8B increased 
the net vertical lift over 6%. 
#Jf 11 Recir cu lation and Hot-Gas Inge stion 
A VTOL aircraft hovering near the ground tends to "drink its own bathwater." The hot exhaust gases find their way back into the inlet, causing a 
signific ant reduction in thrust. Also, this recirculated air can include dirt 
and other erosion particles that can damage or destroy the engine. In some 
cases, the dirt kicked up by a hovering VTOL aircraft has completely 
obscured the pilot's vision. 
Figure 21.1 0 shows the three con tributors to exhaust recirculation: buoyancy, fountain, and relative wind. Buoyancy refers to the natural tende ncy of 
hot gases to rise. The jet exhaust mixes with the ambient air and slows down 
as it moves farther away from the airplane. Eventually, it has slowed enough 
that the outward momentum becomes negligible, and the buoyancy effect 
takes over. The now-warm air rises up around the aircraft and can eventually 
be drawn back into the inlet. 
The buoyancy effect takes time. It takes about 30 s in hover for the air 
around the Harrier to heat up by 5°C. This 5°C increase in air temperature 
entering the inlet reduces the engine thrust by about 4%. 
If the nozzle arrangement produces a fountain, the recirculation will be 
greatly increased. This causes additional hot-gas ingestion (HGI) in addition


<!-- p.781 -->

a) Bu oya ncy 
/"CH APTE R 21 Ver tical Flight -Jet and Prop 779 
b) Fount ain 
t !'..__--=r---3 \ 
'- ..... __ Jl ___ ..,. 
c) Relat ive wind 
I 
r 
' 
/---Fig. 21 .10 Recir cu lati on. 
to the buoyancy effect. Unlike the buoyancy effect, the fountain effect takes 
little time to increase the tempera ture of the air entering the inlet. The 
Harrier experiences a l0°C tempera ture rise due to the fountain effect. 
This reduces thrust by about 8%. 
The third contributor to recirculation, relative wind, can be due to atmospheric wind or to aircraft forward velocity. Essent ially, the relative wind 
pushes back on the spreading exhaust gases, forcing them up. At some combination of relative wind and exhaust veloc ity, the hot gases will wind up back 
in the inlet. 
Hot-gas ingestion is typically limited to speeds below about 50 kt {93 km/h} . 
If the nozzles can rapidl Y. vector from full aft to a downward angle, a rolling 
takeoff can be used to minimize HGI problems. The pilot starts the takeoff 
with the nozzles fully aft and quickly accelera tes to about 50 kt. Then the 
nozzles are quickly vectored downward and the aircraft leaps into the air. 
Jump Jet is an old nickname for the Harrier! 
#Jf J:I VTOL Foot print 
The "footprint" of a VTOL aircraft refers to the effect of the exhaust upon 
the ground. This is largely determined by the dynamic pressure and temperature of the exhaust flow as it strikes and flows along the ground. Even a helicopter cannot operate from a very loose surface such as fine sand or dust. The 
exhaust of a turboj et VTOL aircraft can be of such high pressure and temperature that it can erode a conc rete landing pad if the aircraft is hovered in 
one spot for too long. 
No exact method exists to determine the acceptable exhaust pressures 
and temper atures for VTOL oper ation off of a given surface. Roughly


<!-- p.782 -->

780 Ai rcraf t Desi gn: A Conceptual Approach 
spea king, a turbojet exhaust is marginal for operation off concrete and is too 
hot and high pressure for asphalt. The front-fan exhaust of a split-f low turbofan is gener ally acceptable for concrete, asphalt, and dense sod. 
However, the core-f low exhaust of the turbofan might be too hot and high 
pressure for asphalt and sod. 
Ejectors and gas-driven fans sub stantially reduce the exhaust temper ature 
and pressure, perhaps allowing oper ation from regular sod and even 
hard-packed soil. 
In general, the nozzles should be as far above the ground as possible. The 
ground tempe ratures due to a turbofan will be reduced by about 30% if 
the nozzles are five nozzle diameters above the ground. This suggests that 
a pair of side-m ounted elbow nozzles are preferable to a single ventral 
nozzle because they are higher off the ground and have less diamet er for 
the same total airflow. This also suggests that the axisymmetric vectoring 
nozzle described above is undesirable; its geom etry places the exhaust very 
close to the ground. 
#}f JI VTOL Contro l 
The VTOL aircraft in hover and transition must be controlled by 
some form of thrust modulation. Most VTOL concepts use a reaction 
control system (RCS), in which high-pr essure air is ducted to the wing 
tips and the nose and/or tail. This high-pressure air can be expelled 
through valve-co ntrolled nozzles to produce yaw, pitch, and roll control 
moments. 
The high-pressure air for the RCS* is usua lly bled off the engine compressor , causing a reduction in thrust. The Harrier loses roughly 10% of its 
lift thrust due to RCS bleed air. 
While cost ly in thrust, bleed- air RCS systems can be light in weight. For 
the Harrier, the whole system only weighs about 200 lb {91 kg} . However, the 
RCS ducting occupies a significant volume in the aircraft. Also, RCS ducting 
is hot and cannot be placed too near the avionics. 
If a VTOL concept has three or more lift nozzles placed well away from 
the e.g., modu lation of the lift thrusts can be used for control in vertical flight. 
For example, if the thrust from the forward nozzle is reduced, the nose will 
pitch down. Vectoring the left-side nozzles forward and the right-side 
nozzles rearward will cause the nose to yaw to the left. 
In addit ion to three- axis control (roll, pitch, and yaw), a VTOL needs 
vertic al-veloc ity control ("hea ve" contro l). This is done by varying the 
lifting thrust. For an aircraft with fixed nozzle- exit area (such as the 
Harrier) , the lifting thrust is varied by engine throttle setting. 
* The VTOL and stealthy F-35B is probably the first airplane with RCS and low RCS. If you get the 
joke, you've been paying attention!


<!-- p.783 -->

CHAP TER 21 Verti cal Flig ht-Jet and Prop 781 
An engine with variable nozzle- exit area can change its lifting thrust more 
rapidly by changing exit area, leaving the throttle setting unchanged. Provision of acceptable heave control generally adds about 5% to the required 
hover T/W. 
A multi -engine aircraft should remain under control following the loss 
of an engine. This common requirement is far more difficult for a VTOL 
aircraft to meet than for a conventional aircraft. For example, if a VTOL 
aircraft requires two engines to hover, a third engine of the same thrust 
would be required to ensure hover ability after loss of an engine. Not only 
that, but the engines must be arranged so that their combined thrust 
passes through the e.g. with all engines running and with any one engine 
failed. Alternati vely, it can be assumed that upon failure of one engine, 
another engine on the opposi te side of the airplane will be imme diately 
stopped. 
Another technique for engi ne-ou t control involves cross- shafting the 
engine fans so that the fans of all of the engines can be driven from the 
cores of the other engines. This minimiz .es the asymmetric thrust loss from 
the failure of one engine core. However, the weight impact of the crossshafting mechanisms must be considered. 
Some multi-en gine VTOL con cepts have been designed with several jet 
engines ope rating together through some form of augme ntation devices. 
For example, the Ryan XV-SA had two jet engines that were diverted to 
three tip- driven fans. Either engine could drive all three fans. 
f lf Jl1I VTOL Propu lsion Consider ation 
Thrust matching has alread y been discussed as one of the key problems 
facing VTOL designers. Inl_et matching presents a similar problem. For efficient jet-en gine operation at zero airspeed, the inlet should look much like a 
bellmouth as seen on jet-engine test stands. The inlet should have a large 
inlet area and generous inlet-lip radii. These features cause unacceptable 
drag levels during high-speed flight. 
As a compromise, inlets can be sized for cruise oper ations and provided 
with auxiliary doors for VTOL oper ation. For reasonable low- speed efficiency 
these auxiliary doors must be very large compa red with typical auxiliary 
doors as seen on a CTOL aircraft. 
Another propulsion conside ration is the amount of vertical thrust 
required for vertical flight. As a minimum, the net T / W for vertical flight 
must obviously exceed 1. 0. For accep table response in heave (vertical acceleration) , the net T / W should equal or exceed 1. 05. 
The net thrust available for vertical lift will be reduced by suckdown, 
hot-gas ingestion, and RCS bleed. Because of these factors, the required 
T/W for vertical flight will exceed the 1. 05 value required merely to hold 
the airplane up and provide heave control. For most types of VTOL aircraft,


<!-- p.784 -->

782 Air craft Desig n: A Concep tual Approach 
the overall installed T / W for vertical flight ranges between about 1. 2 and 1 .5, 
with 1.3 being a typical value. 
f jf JIJ Weigh t Effects of VTOL 
It is difficult to assess the impact of VTOL on aircraft weights using statistical design data from existing aircraft. VTOL designs are so strongly driven 
by weight con siderations that the designers will push much harder to reduce 
weight than in a normal CTOL design. Customers will accept such compromises because, otherwise, the airplane prob ably won't meet its mission 
objectives. 
For example, the Harrier was designed so that it requires removing the 
wing to remo ve the engine. This would be considered a fatal design flaw 
in a CTOL aircraft but is tolerated in the Harrier because of the weight 
savings compared to the immense doors that would otherwise be require d 
to re move the engine. Because of such design compromises, the Harrier 
has an empty-weight fraction We/Wo of only 0.48, whereas a statistical 
approach based upon similar CTOL designs would indicate that the 
Harrier should have an empty-weight fraction of about 0.55. By way of 
reference, the A-4M, which performs a similar mission, has an empty-weight 
fraction of 0.56. 
Simi larly the F-35B, to address weight concerns, was only designed to a 
7-g load factor whereas the non-VTOL variants are designed to 9 g. 
If designed to the same ground rules as a CTOL aircraft, a VTOL aircraft 
will always be heavier in at least two areas, namely, propulsion and contro l 
systems. The propulsion system will be heavier due to the compromises 
ju st described for solving the balance and/or thrust- matching problems. 
The various VTOL propulsion con cepts all incorpor ate some additional 
features such as vectoring nozzles, extra internal ducting, tilt nacelles, or 
lift engin es. These add weight. 
Reference (1 43] compares CTOL and VTOL versions of a carrier-ba sed 
utility aircraft (similar to the S-3). The CTOL version's propulsio n-system 
weighs 8% of the takeoff weight. The VTOL version's tilt-nacelle propu lsion 
system weighs 20% of the takeoff weight. 
Data from (1 43-1 45] indicate that a typical supersonic CTOL fighter 
design can have a propulsion-s ystem weight about 16-18% of the takeoff 
weight. An equivalent VTOL design would have a propulsio n-system 
weight about 18 -22% of the takeoff weight. 
The far greater propulsion-s ystem weight for the cruise-dom inated utility 
aircraft reflects the fact that the fighter concept alread y requires large engines 
for supersonic flight. 
Control- system weights are increased about 50% for most VTOL designs. 
This is caused by the ducting, nozzles, and valves of the typical RCS. 
However, the total control- system weight is only a small fraction of the 
takeoff weight (2% for a typical CTOL design) , so the impact is slight.


<!-- p.785 -->

CHAP TE R 21 Vertical Flig ht-Jet and Prop 783 
It is difficult to provide an estimate for the total impact of VTOL on 
We/ W o based upon statistic s. Data in [1 43- 145] indicate that a fighter aircraft will experience an increase in We/Wo of ro ughly 4% if designed to 
the same ground rules as an equivalent CTOL aircraft. Simil arly, a transport/utility aircraft will have an increase in We/Wo of about 7%. These estimates are crude, and a detailed weight statement should be prepared to 
properly assess the weight impact of VTOL. 
jlf If I Sizing Effects of VTOL 
The sized takeoff gross weight of a VTOL aircraft will be increased by the 
empty weight effects just described. Also, a thrust misma tch between vertical 
flight and cruise can force the engine to be operated well away from the 
optimal thrust setting for cruise efficienc y. This increases fuel consumption, 
which increases sized aircraft weight. 
These factors will clearly increase the sized aircraft takeoff weight if 
a VTOL aircraft is flown over the same mission as an equivalent CTOL. In 
some cases, though, the mission requiremen ts can be reduced for some 
VTOL aircraft with no loss in ope rational effectiveness because the VTOL 
aircraft can proba bly be based closer to the combat zone. 
VTOL simplifies landings in bad weather. Helicopt ers can "feel their way 
around" in foggy cond itions that ground normal CTOL aircraft. A VTOL airplane should therefore be allowed reduced landing reser ves for loiter or 
diversion to alternate airpo rts. 
On the other hand, the fuel burned by a vertical landing can be substantial, whereas a CTOL aircraft uses virtually no fuel in landing. 
Another favorable effect of a VTOL capabil ity comes in the optimization 
of wing loading. For many aircraft the wing loading will be determined by 
either the takeoff or larrding requirements. A VTOL capab ility removes 
this consid eration, possibly permitting a smaller wing, which in turn 
reduces weight and fuel usage. This can be seen on the Harrier. 
Taken altogether, these factors indica te that the jet VTOL aircraft will 
usually be heavier than an equivalent CTOL design. An increase in sized 
TOGW of about 10-20% can be expected for a fighter design. A VTOL transport/utility design will usua lly weigh about 30-60% more than a CTOL 
design. The analysis and methods of this book should be used to get a 
more reliable answer. 
EJ Prop VTOL and Hel ico pter 
#Jfll Introd uction 
Jet VTOL, for all the progress being made, is still in its infanc y. As a 
measure of this, the Harriers, Yak-38s, and F-35B s can put on a great


<!-- p.786 -->

784 Aircr aft Des ign: A Concep tual Approach 
airshow simp ly by taking off straight up. The crowd loves it, but nobody is 
impressed when a helicopt er does the same thing. It happens every day . 
Vertical flight via some sort of "airscrew" was concei ved of by da Vinci, but 
he failed to anticipate blade aerod ynamics, power-to-w eight require ments 
or controllabi lity issues. It wasn't until Siko rsky's VS-3 00 that a helicopte; 
truly controllable in hover and forward flight would be demon strated 
(1 940) . This was such an advance on prior attempts that its succ essor, 
the R-4 Hoverfly, was immedia tely ordered into production and saw 
com bat service just four years later (earning the 
nickname "Eggbeate r," which is still applied to 
helicopt ers) . 
Fundament ally, the reason that helicopters are 
rout inely successful at vertical flight while jet 
VTOLs are putting on a show every time they do it 
is because helicopters make better use of Eq. (1 3.4). 
Helicopters really 
can't fly-they're 
just so ugly that the 
Earth repels them. 
-Anonymous 
This proved that efficient thrust is obtained by applying the power of the 
engine to a large cross section S of air, which is accelerated (V - Vo) by a relatively small amount. The large rotor "gent ly" accelerates a large disk of air, 
compared to the small exhaust flow "screaming" out of a jet engine at nearson ic speeds. Quite simply, the helicopter can hover on a much smaller 
power-to-w eight ratio than can the je t. 
This sub chapter presen ts an overview and key conc epts for design 
of helicopter and other propeller VTOL aircraft, including first-order analysis 
metho ds, with emphasis on how their design differs from and is similar to the 
design of other types of aircraft as discussed in this book. Specialized helicopter textbooks should be referred to for the details of blade aerod ynamics, 
rotor analysis, power estimat ion, vehicle dynamics, and range and performance analysis ((1 19 , 146, 147] are recommend ed) . 
Two fundamen tal differences between helicopter design and the design 
of wing-b orne aircraft should be noted. First, for helicopters there is 
nothing equivalent to the Breguet range equation [Eq. (3. 5)], that is, a 
simple equation relating the fuel burned to the range. This greatly complicates the calculat ion of range and the sizing of the helicopter to a range 
requirement as in Chapter 3. 
Second, the rotor blade aero dynamics domina tes even the earliest design 
studies. A helicopter's range and flight performance depend so much on the 
rotor analysis that the helicopt er designers almost immedi ately perform 
in- depth rotor calculations using blade element or numerical calculations. 
Helicopter designers simply don't spend much time doing top-le vel, 
order-of -magnitude conce ptual trade studies. 
A note on terminolog y: a helicopt er "rotor" is like a variable-pi tch "propeller, " but is much smarter: it can vary its pitch all at once ("collec tive") like 
the propeller, but can also vary its pitch as the blade goes around through 
360 deg of rotation ("cyclic") . In other words, the pitch can vary as the 
rotor "cycles" around.


<!-- p.787 -->

CHAP TER 21 Ver tical Flig ht-Jet and Prop 785 
Also, a helicopter is a "rotary-wing aircra ft." Helicopt er people don't like 
it when non- helicopter people use the word "aircraft" as synonymous with 
"fixed-wing aircraft." And, they don't like that jo ke about "ugly. " 
#Jff J Helic opter Design Conc epts 
There have been many different approaches to the basic helicopter idea. 
All must provide lift at the center of gravity and have good control about 
three axes while avoiding unneeded comp lexity and weight. Figure 21.11 
illustrates the most common approaches. 
The simplest helicopter concept uses just a single main rotor loca ted at 
the center of gravity. The vast majority of helicopters in production have a 
single main rotor. This can be called the "con ventional" helicopter approach, 
and as with aircraft tail arrangements, "con ventional" usually means best for 
most design applica tions. This provides the greatest disk area for a given 
weight of rotor system and, by helicopter standards, is fairly simple as to 
control mechanisms (described next) . However, the application of power 
to the single main rotor will cause a strong torque that must be coun tered 
in some fashion, as will be discussed later. Also, the large diameter of the 
single main rotor might be a disadvantage for high-speed flight because it 
causes the advancing tip to have a higher relative velocity and will reach 
Mach effects sooner. 
Single main 
/ 
Quadc opter 
Fig. 21.1 1 Helic opter concepts .


<!-- p.788 -->

786 Air craf t Des ign: A Concep tual Appr oach 
To avoid the torque problem, various versions of coaxial counter- rotating 
rotors have been used. The Kamov Desi gn Bureau in Russia is well known for 
this approach, which has also been empl oyed by U.S. helicopter desi gners. 
Counter- rotating prope llers have a slight advantage in propelle r efficiency resulting from the vector direction of the local flow as seen by the 
second prope ller. This in effect makes the blade lift more direct ly in the 
vertical direction, and can be visualized as "taking out the swirl" of th e first 
propeller (swirl represents wasted energy). 
Coaxial rotors have several disad vantages. The "mast" (vertical post on 
which the rotor is moun ted) must be quite tall to provide sufficient separation between the blades because it would be catastrophic for them to 
strike each other. This mast height, roughly 0.3 times the rotor radius, 
adds drag and weight. Also, the mechanization is quite complex. A counterrotating gearbox must convert the engine's power onto two conce ntric shafts, 
with suitable bearings. The pilot's control inputs must somehow be passe d 
through the plane of the lower rotor to reach the upper rotor, which of 
course is rotating in the opposi te direct ion. For a military helicopter, all of 
this mechanization adds to the vulnerable area. 
To avoid the comple xity of con centric shafts and passing of control 
inputs, the "intermeshed" rotor was developed. It has two counter- rotating 
rotors set at outward -tilting angles, driven by a single gearbox that ensures 
that the rotors just miss each other! This concept was pioneered by Kaman 
Corpo ration, which produced a number of such designs primarily used for 
U.S. Air Force search and rescue. 
The tandem helicopter is used to provide a wide e.g. range for a cargo 
helicopt er, such as the Boe ing CH47 or the classic Vertol H-21 Flying 
Banana. Lift can be shifted to the front or rear ju st by changing collect ive 
on the rotors. Also, placing the lift at the ends of the fuselage some what 
reduces its structural weight. Such designs obtain yaw control by "flying" 
the rotors to opposite roll angles (seen from the front) . The tandem helicopters suffer from interference effects between the two rotors that reduce efficiency and cause strange flying characteristics unless the controls are 
artificially augmented. 
The side -by-side helicopter is used for really large helicopt ers such as the 
Russian Mil V- 12. This arrangement suffers from extra structural weight 
resulting from the aircraft being suspended from the tips of its "wings," but 
avoids the interference problems of the tandem helicopter and may benefit 
in forward flight from an apparent doubling of the aspect ratio. (In forward 
flight the rotor disk acts like a wing, as will be discussed next.) 
The "quadcopter" arrangement proved impractical for gas-powered flight 
but lends itself well to electric power. Historica lly, the first helicopter to lift a 
man off the ground was a quadco pter, the gas- powered 19 07 Breguet "Gyroplane No.I" (yes, that Breguet) . Since it had no mechanism for co ntrol, it 
had to be held steady by a ground crew. In 19 22, Etienne Oehmichen flew 
a controllable quadcopt er and soon after, set distance records and took up


<!-- p.789 -->

CHAPTE R 2 1 Verti ca l Flig ht-Jet and Prop 787 
passenge rs. Still, the performance and controllabil ity of these early quadcopters was quickly eclipsed by single- rotor helicopt er designs leading up to Igor 
Sikorsky's 1939 VS-300, considered the first practical helicopter. 
Today, quadcopt ers are back. The combination of electric motors 
and cheap computerized electronics including attitude sensing solves the 
controllabilit y problems which made manually flown, gas-po wered quadc opters so impractical. As toys, they can be bought at any shopping mall. Modern 
manned versions have flown, and commerc ially- useful quadcopter UAVs are 
poised to begin package delivery services direct ly to our homes and 
business es, if safety and noise issues can be addres sed. 
The modern quadcopter typically has four fixed- pitch propellers attached 
to electric motors. The only flight control actuation is by varying the speed of 
the p ropellers, changing the thrust for roll, pitch, and heave control, and 
varying the torque for yaw cont rol. This yaw control is the reason that quadcopters are "quad ." Two of the propellers rotate in one direction, and the two 
diagonally opposi te rotate in the oppo site direct ion. By increasing the speed 
and torque of one diagonal pair and r-ducing for the oppo site pair, the lift 
stays the same along with pitch and roll, but the net torque is changed so 
the vehicle yaws. 
To provide engin e-out safety, some designs double the number of motors 
and propellers. These are either positioned back-to- back in an overall 
"double-q uad" arrangement or can be distributed around the vehicle such 
that should one quad set fail, the other set can fly the vehicle. Obviousl y, a 
completely separate power supply and control system is also required. 
Some "multi -copter" designs have a huge number of small motors and propellers spread all around the vehicle or attached to a framework, with careful 
summation of thrusts and torques used to control the vehicle. This approach 
provides redundancy and also addresses a fundamental problem with quadcopters-t hey don't scale up very well. Effective control requires rapid ly changing the thrust of the pr-pellers. The larger the prope llers and motors, the 
more rotational inertia they have, and the greater the lag time between commanded and realized change in thrust. A multitude of small motors provides 
better controllabili ty than a few large motors. The alternative is to use variable 
pitch propellers, but that adds comple xity, weight, and cost. 
Quadcopters and multi -copt ers are still in their infancy. We can expect 
much progress in the future, espec ially as battery technolog y improves the 
available flight time. Who knows, perhaps they'll finally allow the unfulfilled 
dream of a flying machine in every garage! 
For a normal helicopt er, the basic mechanization for rotor mechanization 
is almost scary to fixed-wing airplane designers and pilots. Control (and 
life) depend on the proper operation of an asse mbly of small mechanical 
parts rotating, vibrating, and rubbing on each other, and if one thing 
goes wrong .. ! However, it all works with a surprising degree of reliabil ity. 
Most helicopter crashes, like most aircraft crashes, involve a perfectly good 
machine flying into something hard.


<!-- p.790 -->

788 Air craf t Desig n: A Concept ual Approach 
Pitch cyclic ---..... 
Fig. 21 .1 2 Helic opter cyclic and colle ctive contr ols. 
Figure 21.12 shows the fundamen tal helicopter control mechanism, providing roll, pitch, and heave (vertical acceleratio n). Each rotor blade is free to 
independen tly pivot in pitch, which is controlled by a rod that is linked to a 
rotating "swashplate" placed around the mast. This swashplate rotates with 
the mast and blades and is connected to a nonr otating, or fixed swashplate 
such that when the fixed swashplate is moved up or down or is tilted, the 
rotating swashplate moves too. The pilot's "colle ctive" control moves 
the swashplates up and down, changing blade pitch to change total lift. 
The pilot's cyclic control tilts the swashplate s. When the swashplates are 
tilted, the rotor blades go from a higher pitch at one blade rotation angle 
to a lower pitch angle when that blade is on the oppo site side. This causes 
the plane of the rotor disk to tip, as the pilot desired. Because of gyroscopic 
Fig. 21 .13 Rotor-blade fla pping .


<!-- p.791 -->

CHAP TE R 21 Verti cal Flig ht-Jet and Prop 789 
Jag, the controls are mechanized such that the most posi tive blade pitch 
occurs 90 deg before the desired tilt. 
The rotor blades are hinged as shown in Fig. 21.13 to permit them to 
"flap" up and down to facilitate this tilting of the rotor plane. Even more 
important, because the blades are pivoted at the root, there cannot be any 
root bending moment. This allows the blades to be much lighter than if 
they were rigid (although "rigid-rotor" helicopters have been tested and do 
provide better maneuverability) . 
Such flapping also solves an obvious proble m-i n forward flight the 
advancing blade should get more lift because it sees a higher relative velocity, 
causing the helicopter to roll on its back. 
If the blades are permitted to flap as shown, the advancing blade will 
flap upward. This upward motion reduces its lift, while the retreating blade 
flaps downward, increasing its lift. The rotor flapping reaches equilibrium 
when the lift is balanced from side to side. This results in the plane of 
the rotor disk, defined by the track of the blade tips, being tipped backward 
relative to the actual plane of rotation . . 
As a result of this motion, the blade tip is accel erating and decele rating 
in its rotational motion around the helicopter causing in-p lane structural 
stresses. To avoid these stresses, yet another pivot is added, with a vertical 
shaft. This "lead- lag" hinge eliminates in-p lane stresses at the blade root. 
All together, a rotor blade is "attached" to the fuselage through four separate 
pivots: the rotor shaft, the pitch pivot, the flapping pivot, and finally the 
lead-lag pivot. 
In the single main rotor configuration, some form of antitorque device is 
required (Fig. 21. 14). For most helicopt ers this is provided by a tail rotor, 
,. 
/ 
Latera l thrus ter 
Fig. 21 .14 Antitorq ue devices . 
Shr ouded tail rotor 
Downwa sh


<!-- p.792 -->

790 Air craf t Desi gn: A Concep tual Approach 
which is driven by a shaft linked to the main rotor. Tail rotors are typically 
about 15-2 0% of the main rotor's diameter. The pilot's rudder pedals 
control the tail rotor's blade pitch, causing the yaw to change. For a helic opter 
without an augmented con trol system, the pilot must learn to "dance" on the 
rudder pedals, continuo usly making small corrections as every change in 
speed, altitude, power setting, cyclic control, and wind gust affects the yaw. 
The tail rotor, present on the first successful helicopter and on most helicopters since, is efficient and respon sive, but has a few problems. It is a significant 
source of noise and vibrati on. It also adds drag in forward flight. 
On some helicopters the tail rotor is significan tly angled as seen from 
the front. This is a clever way to get some almost-free lift. At th e typical 
20° of cant angle, there is a vertical compon ent of the rotor's thrus t equal 
to 34% of the tail rotor's thrust, at the cost of only 6% of thrust in the horizontal direct ion. For the Sikorsky H-60 Black hawk the canted tail rotor provides almost 3% of the total lift during hover. 
When walking to or from a helicopter with the rotor turnin g, a basic 
human instinct forces most of us to duck down, even if the rotor is at 
twice our height. For some reason, though, every year a few people try to 
run around the back of the helicopter and run into the forgotten, spinning 
tail rotor. Putting a shroud around the rotor minimizes this possibili ty. 
Also, the shroud can reduce noise and reduce drag in forward flight. The 
RAH-66 Comanche uses a shroud to reduce noise and to minimize its 
radar cross section from the front. 
A lateral thruster, really a ducted fan inside the aft fuselage, can be used 
for antito rque. While inefficient for hover, it can offer drag advantages in 
high-speed flight. 
Various conc epts for deflecting the rotor downwash to provide a sideways lift force for anti-torque have been attempted. The obvious use of a 
large airfoil vane has not been successful. However, the use of forced circulation by blowing has been. Se veral models of McDonne ll (Hughes) helicopters use what they call NOTAR (no tail rotor) in which the aft end of the 
fuselage has a round cross section and a fore-and-aft slot. An internal fan 
blows air out of the slot, tangent to the surface, forcing circu lation 
around the aft fuselage that produces a sideways lift force for antitorque. 
NOT AR reduces noise and drag in forward flight and cannot injure 
people on the gro und, but it consumes more power and is heavier than a 
conventional tail rotor. 
Helicopt ers have a big problem-t hey are inhere ntly slow, for a fundamental reason. The advancing blade has an airspeed equal to the helicopt er's 
airspeed plus the rotational veloc ity of the blade. The retreating blade has the 
helicopter's airspeed minus the blade's rotational veloci ty-and because the 
retreating blade has its trailing edge pointing the wrong way, the net airspeed 
must be a negative number. In other words, the rotor must spin fast enough 
that the retreating blade has a rearward rotational tip speed subst antially 
greater than the helicopter's forward speed if it is to develop any lift.


<!-- p.793 -->

CHAP TER 21 Verti cal Flig ht-Jet and Prop 791 
At a minimum, for the retreating tip to have zero net airspeed the advancing blade must have double the helicop ter's airspeed. To generate any lift on 
the retreating blade, the advancing blade must go perhaps three times the 
helicopter's airspeed, which means that the advancin g blade tip can approach 
sonic speeds when the helicopt er approaches just 200 kt {370 km/h} . 
This fundam ental helicopter speed limit can be circum vented in several 
ways, although all have their own penaltie s. One approach, the "compound 
helicopter," has a wing and an extra forward propulsion system (jet, prop, 
or ducted fan) . For high-speed oper ation, the rotor blades "unload," going 
to a flat pitch and gene rating little lift. The compound Euroco pter X3 now 
in flight test is expected to reach over 220 kt {410 km/h} . 
Figure 21.15 shows other approaches to beating the helicopter "speed 
limit." The advancing blade concept uses counter-rot ating rotors, unloading 
the retreating blades and flying only on the lift of the two advancing blades. 
This requires a sophis ticated blade pitch co ntrol system and usua lly entails 
an additio nal thrust system for high-speed flight. Also, the blades must be 
much stronger and therefore heavier th.an on a normal helicopter. 
The Sikorsky X2 uses the advancing blade concept with coaxial rotors 
and is the fastest true helicopter ever flown, reaching 250 kt {460 km/h} in 
2010. An enlarged operational version called the S-97 Raider is in flight 
test. With crew of two plus 6 troopers, it has a range of about 300 nmi 
{560 km} . 
The stopped rotor system does just that-the rotor is stopped for highspeed flight and acts as a wing. In the X-wing concept illustrated in 
Fig. 21.15 , the rotor has four blades arranged as an "X" and acts as a 
Tilt roto r 
Adv an cing 
blade 
Tilt wing 
Sto pped rotor 
(X-wi ng) 
Fig. 21 .15 Hig h-speed helic opter s and prop VTOLs.


<!-- p.794 -->

792 Aircr aft Desig n: A Concep tu al Appr oach 
strange tandem wing when stopped. The rotors must be rigid and with all of 
the strength of wings to carry the lift loads when stopped. Note that the airfoil 
on the retreating blade side of the aircraft will be in reverse flow when 
stopped: the "po inty end" will be forward. A circular-arc, sharp leadin g-edge 
airfoil can be used that will have acceptable aerod ynamics no matter, which 
end is forward, but it is a compromise. 
In a more sophisticated approach, a "circulat ion-con trol wing" can be 
used in which the trailing and leading edges are round, with spanwise slots 
out of which air can be blown. This blowing forces a circulation such that 
the airfoil gene rates lift. The greater the blowing, the more the lift. Thus, 
blowing can be used instead of changing blade pitch for control during 
helicopt er flight. In forward flight, the blowing on the retreating blade side 
of the aircraft can be switched to the opposi te end of the airfoil, making a 
good forward- flight wing. However, this system is quite complex and to 
date has not been used for a production aircraft. 
Proba bly the best way to make a helicopter go fast is to turn it into an 
airplane. In 19 28, ecc entric genius Nikola Tesla, inventor of the alternatin g 
current electric motor, patented a propeller -po wered "tail -sitter" vertical 
takeoff biplane, compl ete with rotating pilot's seat. The later turbopro p 
Lockheed XFV- 1 tail-s itter actually demonst rated vertical flight but was difficult to land and impractical to service once landed. 
The Focke-A chgelis Fa 269 was an innovative tilt-rotor concei ved in 
1941. Rather than rotate the whole aircraft, only the propellers would 
pivot. Oddly enough, these were pusher propellers that rotated downwards 
and under the wings, coming dangero usly close to the ground. It was 
never built. 
A viable tilt-rotor was first demo nstrated in the Bell XV-3, followed by 
the highly successful XV- 15. Today the V-22 is in service and the 9-passe nger 
Agusta Westland 609 is nearing certificat ion. The Army's Bell V-280 Valor, 
designed to carry 14 troops over a range of 210 0 nmi {3900 km}, is now in 
flight test. 
The tilt-rotor is fast. While few regular helicopters can exceed 170 kt 
{320 km/h}, the tilt-rotors exceed 300 kt {560 km/h} . For the tilt-rotor, the 
engine nacelles (or props alone) rotate out at the wing tips, requiring separate 
pivots and actuators plus some mechanism to guarantee that both move at 
the same time. 
In the similar tilt-wing, the entire wing rotates to tilt the rotors from 
vertical to horizontal. This seems intuitively simpler than the tilt-roto r. 
The nacelles can be firmly attached to the wing, and all that is needed to 
pivot the entire wing/nacelle/rotor asse mbly is a hinge and an actuator at 
the wing root. 
The tilt-wing should be lighter, simpler, more reliable, and because the 
wing is aligned with the propwash in hover, should attain a higher net lift. 
However, it has one large problem. During transition, the wing is at an 
extreme angle of attack, so it stall s. This makes controllabil ity difficult


<!-- p.795 -->

CH APTER 21 Vertical Flig ht-Jet and Prop 793 
unless the wing is almost entirely within the propwash and the engines are 
kept at a high power setting-d ifficult to do when you want to slow down. 
The tilt-wing concept was first tested in the Boeing Vertol VZ-2. This had 
rotors and used cyclic control for pitch, differential colle ctive for roll, and had 
a tail rotor for yaw. It flew quite well provided that transition was always done 
at a high power setting. 
Tilting wings or nacelles can also be used with propellers (i.e., blades 
without a cyclic capabi lity) or with ducted fans. In either case, differential 
blade pitch can be used for roll control, but some other means of yaw and 
pitch control must be provided. The propellers or ducted fans typically 
have a lesser diameter compared to tilting rotors so require more power 
for hover (see the following for power calculat ions) . 
The Chance-V ought XC-1 42 demo nstrated tilt-w ing with propellers 
and had impressi ve performance. Weighing 41 ,500 lb {1 8,82 4 kg}, it could 
fly from 30 kt {56 km/h} backward to 350 kt {643 km/h} forward and had 
range of 710 n miles {1 320 km} . However, in production it would have cost 
far more than a STOL aircraft carrying .a similar payload. 
f Jm Hel icopter Design Par ame ters and Bl ade Airf oil Sel ection 
When designing a helicopter or another type of propeller VTOL aircraft, 
two design parameters dominate, namely, power loading ( W / P) and disk 
loading (W/S). These are similar in importance and effect to the T/W 
and W / S for a fixed-wing aircraft, and together they largely determine the 
helicopter's hover, climb, speed, range, and autorot ate capabilit ies. (W is 
the takeoff gross weight, P is maximum engine power, and S is the rotor 
disk area, not to be confused with the actual area of the blades themsel ves.) 
The definition of power loading is iden tical to that of propeller- powered 
fixed-wing aircraft and A.as a similar reverse connot ation: a big number 
implies a small engine relative to the size of the helicopter. In fact, typical 
helicopter power lo adings are about the same as those of high-powered propeller aircra ft, roughly 4-8 lb/h p {2.4-4.9 kg/kW}. Table 21.1 provides 
typical power loadings for various classes of rotary-wing aircraft. 
Table 21 .1 Helic opter Power Loadi ngs 
@l\fl:. •lifjffiJl•na-• 
Scout /attack hel icopter 3-5 1 .8-3 . l 
Tran spor t helic opter 5-7 3. 1- 4.3 
Civi l/uti lity helic opter 3-8 1. 8-4 .9 
Tilt rotor 4-5 2 .4-3. l 
Tilt wing (propeller ) -3.4 -2 . l


<!-- p.796 -->

794 Aircr af t Desig n: A Conceptual Approach 
Table 21 .2 Hel icopter Disk Loadings* 
Scout / attack helic opter 
Tra nspor t helic opter 
Civil /util ity helic opter (low speed) 
Civi l/util ity helic opter (high speed) 
Tilt roto r 
Tilt wing (prope ll er) 
*L ow speed - < 15 0 kt {280 km/h} 
Typic al W/S 
w1in=wmw 
8-1 0 39-4 9 
6-15 29-73 
4-6 20-29 
6- 10 29-49 
15 -25 73-1 22 
-50 -245 
As can be seen, there is a lot of scatter in the data, and this author has 
not found a reliable statistical correlation between the desired helicopter 
speed and its power loading as was presented in Table 5.4 for fixed-wing 
aircraft. 
Disk loading (W/S) is the equivalent of wing loading for a fixed-win g 
aircraft, and the disk area is the same as the S of Eq. (1 3.4). This proved 
that higher thrust efficiency is obtained by app lying the power of the 
engine to a large cross section of air. Therefore, the lower the disk loadin g, 
the smaller the engine required to hover or climb (i.e., the larger the power 
loading permi tted) . However, a lower disk loading implies a larger rotor 
blade that has more weight, more drag in forward flight, and a greater tendency to enco unter shocks on the advancing blade. Thus, for high speed 
the disk loading should be higher, but as will be shown next, the vertical 
sink speed in a power-off autorot ate is prop ortional to the square root of 
the disk loading, putting an upper limit on W / S. 
Typical helicopter disk loadi ngs are provided in Table 21.2. These data 
also have a lot of scatter, and an actual W / S for a similar helicop ter should 
be used where possible. 
As with T /Wa nd W / S for fixed-w ing aircraft, the helicopter's power and 
disk loadings must be determined simultaneously using performance calculations based on design requirements. App roximate methods are present ed 
next, but for any serious helicopter design work, detailed analysis methods 
should be used. 
Another key parameter in the design of a helicopter rotor is the "solid ity" 
or u. This is the ratio of the total blade area to the total disk area and, like 
activity factor [Eq. (13.15)], is a measure of how much power can be put 
into the rotor. A high disk loading, high-p owered helicopter needs a high 
soli dity to absorb all of the power and convert it into lift and thrust. Otherwise, the blades will stall before full power is reached. 
Airfoil selection for a helicopter rotor blade is similar to the selec tion 
of wing airfoils, but has several key differences. Low drag at the desi gn lift


<!-- p.797 -->

CH APTER 21 Verti cal Flig ht-Jet and Prop 795 
coefficient is, of course, good, as is a high drag-divergent Mach number, 
to delay formation of shocks on the advancing blade. A high maximum 
lift is also good, to avoid blade stall that usually limits the helicopter's 
hover ceiling. Unfortunately, many of the airfoils that are "good" for 
wings in terms of maximum lift or shock- delayi ng characteristics are 
not good for rotors because their shape creates an excessi ve pitching 
moment. This causes torsional twisting on the rotor. Because of its 
extreme span relative to its chord length, a rotor blade is torsio nally 
very weak. For this reason many rotor-blade airfoils are symmetric, or 
nearly so. 
To avoid torsional flutter, it is neces sary to mass- balance a rotor blade 
everywhere along its span such that the e.g. is at the airfoil's aerod ynamic 
center. Thus, it is good to select an airfoil whose aerod ynamic center is 
more toward the rear, minimizing the amount of weight required to balance. 
A good blade airfoil is thick enough for structural depth and has a simple 
shape for ease of manufacture. 
#Jf(I Mome ntu m Theor y for Hover and Vertic al Climb 
In Chapter 13 , the thrust of an aircraft propeller was calculated by defining an efficie ncy parameter equal to the thrust power obtained in forward 
flight (T x V) divided by the power put into the propeller P. Because this 
method breaks down at zero speed, empirical static thrust data were 
applied and visually faired to the forward flight results. This suffices for aircraft performance estimation where the static thrust is of concern only for 
the start of the takeoff roll. For helicopters, the ability to hover is crucial to 
the determination of pow er requirements, so a more sophisticated thrust 
method must be employed. 
In static conditions, a· rotor (or propeller) does not actually experience 
zero airflow velocity. The rotor induces a velocity, pulling the air into 
itself. This is shown in Fig. 21.16 where the rotor disk area is S. Vo is the velocity high above the rotor, and because the helicopter is hovering, 
Vo = 0. The veloc ity right at the rotor disk is Vi, and the downwash veloc ity 
below the helicopter is Vi. 
Hover momentum theory is derived by equating the power inherent in 
the induced veloc ity at the rotor disk Vi [Eq. (21 .2)) with the increase 
in kinetic energy in the downwash Vi [Eq. (21.3)) . Equations (2 1. 4-21. 7) 
equate the two and solve for the induced veloc ity at the plane of the rotor 
disk in terms of the thrust disk loading T/S. 
T =m t. v = (pViS )( Vi - Vo) = pViS Vi (2 1.1 ) 
At 1: 
P = TV = pVfSVi (2 1.2 )


<!-- p.798 -->

796 Airc raf t Desi gn: A Concep tu al Approach 
At 2: 
so 
Fig. 21 .16 Helic opter in hover. 
P = -K inetic Ener gy = -(1/2 mV2) = I/2 pViSV} (21 .3) 
pVf SVz = l/2 pViSV} 
Vi= Vz/2 
T = 2pVfS 
V1 = y'(T /S)/2 p 
(21 .4) 
(21 .5) 
(21 .6) 
(21. 7) 
The induced veloc ity determined in Eq. (21.7) can then be applied to 
the definition of power to determine the induced or ideal power [Eq. 
(21. 8)]. This can be solved for the ideal thrust of a rotor in hover as a function 
of power and disk loading [Eq. (21.9)]. This assumes that thrust disk loading 
T / S equals the weight disk loa ding W/ S, but actually we should add 
roughly 3% for the force of the downwash blowing on the fusela ge, or 
(T/S) = 1. 03( W/S). 
P = TVi = Ty'(T/S)/2p (21. 8) 
Tideal S=! P)2p/( W /S) = 550 hp)2p/( W /S) (21.9)


<!-- p.799 -->

CHAP TER 2 1 Ver tical Flig ht-Jet and Prop 797 
Inherent in momen tum theor y are a number of assumptions including 
uniform flow throughout the rotor disc and an instanta neous, "magical" 
imparting of energy to the airflow. It also ignores airfoil profile drag losses, 
tip losses, and residual rotationa l velocities. Actual helicopter losses 
include roughly 6% for nonuniform inflow, up to 30% for airfoil profile 
drag, about 3% for tip losses, and less than 1 % for slipstream effects. 
Together, the net thrust is typically 83% or less of the theoretical ideal thrust. 
An empirical "measure of merit" M is used to adjust the momentum 
theory's estimation of power required, much as propeller thrust is ad justed 
by the propeller efficienc y parameter. To avoid the "V = O" problem just discussed, the measure of merit [Eq. (2 1. 10)] is defined as the ratio between the 
ideal power [Eq. (21.8)] and the actual power required. Typically, M = 0.6 to 
0.8 and is used to estimate actual power required via Eq. (2 1.11 ) [Eq. (2 1. 12) 
in British units] . (Do not confuse measure of merit M with Mach number.) 
Define the following: 
M = Pideai / P actual 
p'""'I -:fl! 
hPactual = (T /550 M) J(T /S) /2p {fps} 
Ptotal = (Protor + Ptail rotor )/7/mechanical 
where 
7/mechanical - 0.97 
P (l + Ptail rotor) rotor p rotor 
7/mechanical 
Ptail rotor/Protor - 0.14 to 0.22 
(2 1. 10) 
(21 .11 ) 
(2 1. 12) 
(21 .1 3) 
This estimate of actual power required by the main rotor for hover must 
be further adjusted to account for the power required to drive the tail rotor 
and for mechanical losses, as shown in Eq. (2 1. 13). 
Another consideration in hover is the ground effect, which has the same 
beneficial effect on helicopt ers as was described in Chapter 12 for fixed-wing 
aircraft. By constraining the downwash, ground effect increases efficienc y, 
which reduces the power (required for hover) . At half the rotor's diameter 
above the ground, a helicopter gains about 5% in thrust, and at a height of 
20% of the rotor's diameter, thrust increases by about 18%. This allows helicopters to take off and land when in mountainous terrain at an altitude well 
above the free-air hover ceiling. 
Momentum theory can be extended to analysis of the vertical climb of a 
helicopter. One might assume that the additional power to climb would equal


<!-- p.800 -->

798 Airc raf t Desi gn: A Concep tu al Approach 
the theoretical time derivative of the increase in potential energy, that is, the 
weight times the climb speed. This is pes simistic because the climb speed 
favorably affects the thrust equation. Climb momen tum theory is bas ed on 
Fig. 21. 16, setting Vo equal to climb speed Ve. Repea ting the derivatio ns of 
Eqs. (2 1.1-21. 8) will derive the conclusion that the additional power to 
climb is only half the time derivative of the increase in potential energy, 
that is, the additional power required to climb is approximately half of the 
helicopter's weight times the climb speed. This is added to the hover 
power requirement to determine total power to climb. 
Combining these equations yields Eq. (2 1.1 4), which can be used to calcula te power required for vertical climb or hover (setting climb rate to zero). 
Hover or vertical climb: 
Pc1imb = [(JW fjW/S) + WVc1imb] [(1 + Ptail rotor /Protor)] 
M V 2P 2 7Jmechanical 
where 
W = helicopter weight 
S = rotor disk area 
M = measure of merit 
vclimb = climb speed (=0 for hover) 
(21 .1 4) 
f = adjustment for downwash on fuselage (typically f = 1. 03) 
(in fps units, divide by 550 to yield horsep ower) 
Another impor tant cons ideration is the requirement for "autorotat ion." 
When a helicopter's engine fails, it does not imme diately fall out of the 
sky. The rotor will turn of its own accord if it is set to a lower pitch. 
When a rotor is autorot ating, by definition, its power requirement is zero. 
Referring to Fig. 21.16 and Eq. (21 .2), it is clear that because power equals 
thrust times veloc ity and the power during autorot ation is zero, the 
induced velocity through the rotor disk must also be zero. This implies 
that the rotor is acting like a parachute, creating vertical drag by preventing 
airflow through its disk. 
If we assume an ideal parach ute with drag coefficient of 1. 0 and set vertical drag equal to weight, we can solve for descent veloc ity and find that 
it equals twice the induced veloc ity in hover (2 Vi), as determined by 
Eq. (21 .7). This simply derived approximation is actua lly reaso nably close 
to the correct answer. 
#JU) Powe r Requir ed for Forwa rd Fl ight 
Proper analysis of the helicopter in forward flight requires blade element 
or numerical methods as described next. For initial analysis, we can roughly 
analyze power requirements by treating the rotor like a wing. Actually, in


<!-- p.801 -->

CHAPTER 21 Verti cal Flig ht-Jet and Prop 799 
forward flight the rotor does act like a wing-b oth turn the flow inducing a 
downwash, both form trailing vortic es, both experience a drag due to lift, 
and both have roughly an elliptical lift distribution . If the rotor were a 
round wing, it would have an aspect ratio of [d2 / 7r (d2 /4)] = [4/ 7r]. Empirical data suggest that, oper ating as a wing, the rotor has an equivalent 
Oswald's efficienc y factor e of 0.5 to 0.8, which can be used in Eq. (1 2.48) 
to estimate induced drag. 
Parasitic drag can be estimated using the methods of Chapter 12, plus 
some helicopter-spe cific drag data as provided in Table 21. 3. Not having a 
wing, the drag of a helicopter is normally given in terms of drag area (D / q). 
The data in Table 21. 3, multiplied by frontal area of the componen t, give D / q. 
Note that a well-streamlined helicopter fuselage could be analyzed using 
the form factors and skin-friction values estimated in Chapter 12, but most 
helicopters have a fuselage of such irregular shape that the drag is better estimated using these D / q data. Better yet would be the use of wind-tunnel data 
on a similar configurati on, ratioed by fusel age frontal area. 
The rotor also provides the forward propulsion of a helicopter, so that 
it can be analyzed as if it were an aircraft propeller. Empirical data indica te 
a propeller efficiency Y/p of 0.6 to 0.85, applied to Eq. (13. 17), gives a 
reasonable approximation of the effectiveness of the rotor for forward 
thrust. 
Setting thrust equal to drag [Eq. (13.17 ) = Eq. (1 2.4)] and solving for 
power yield the power required for the rotor. To this, we add the adjustments 
above for the tail rotor and mechanical losses, yielding Eq. (21.15). Note that 
S is the rotor disk area, and the rotor disk aspect ratio [4/ 7r] is already 
included in the equation. 
Level forward flight: 
Pievel = - {q(D/q) + W2 } (1 + Ptail rotor/Prator) 
Y/p 4eqS YI mechanical 
Table 21 .3 Helic opter Drag Data 
Component D / q 
Fuselage 
Tubular landing skid 
Strea mlin ed landing skid 
Un fair ed rotor hub 
Fa ired rotor hub 
Downwa sh interfere nce drag (per uni t 
fuselage fronta l area) 
Leakage and protuberance drag 
(Per Un it Front al Area) 
0.07-0 . 10 
1 .01 
0.40 
1 .0-1 .4 
0.5 -0.8 
0.02 
l 0-20% added to 
parasitic drag 
(21 .15)


<!-- p.802 -->

800 Air craft Des ign: A Conceptual Appr oach 
Climbing forward flight: 
pclimb = -{q(Djq) + w2 + W sin r} (1 + Ptail rotor /Protor) 
7Jp 4eqS 7Jmechanical (21 .1 6) 
{in fps units, divide by 550 to yield horsep ower} 
As was presen ted in Eq. (1 7.35), an aircraft in a climb has a projected 
weight contribution in the drag direction, based on the climb path angle 
y. This can be added to the drag term in forward flight result ing in 
Eq. (2 1.16). (We neglect the slight reduction in required lift impli ed by 
Eq. (1 7.36) .] 
Usually, the power required for climb at a mod erate forward speed is 
sub stantially less than the power required for a vertical climb as expressed 
in Eq. (2 1. 14). For this reason, helicopter pilots often lift the helicop ter a 
few feet off the ground, acceler ating forward while staying in ground 
effect, and begin to climb only when a substantial forward speed is 
reached. 
#JfD Blade El em ent Theor y and Num eric al Methods 
At helicopter design organizat ions, momentum theor y/ measure of merit 
methods are used only for the earliest rough calculat ions. Almost as soon as a 
design project is begun, computerized rotor analysis methods are employed 
to optimize W /A and W / P, select soli dity and the blade airfoil, and determine 
the blade planform and twist. These computer programs are based on either 
blade element theor y or numerical methods. 
In blade element theory, the blade is broken into chordwise strips from 
root to tip, and the angle of attack of each blade element is described in 
equations as a function of helicopter forward velocity, rotationa l velocity, 
loc al induced velocity, blade twist, cyclic control input, radial position, 
azimuth position, and blade flapping. The analysis must also consider advancing blade compres sibilit y, retreating blade stall, and tip losses. Once local 
angle of attack is determined cons idering the previous, the lift and drag 
can be integrated over the blade elem ents and res olved into the thrust 
and torque directions, then summed. Blade element theor y is very complex 
mathematica lly, with multipage equations, but "canned" computer prog rams 
are readily available. 
Numerical methods have largely supplanted blade element methods 
because, once someone else has written the computer program, they are 
no more difficult to use and give better results. Numerical methods use 
various aerod ynamics analysis techniques ranging from relatively simple linearized panel codes to Navier-St okes CFD codes (see Chapter 12). The rotor 
blade is divided into panels, and the flowfield is gridded if CFD is employed . 
The analysis can include all of the cons iderations ju st described as well as


<!-- p.803 -->

CHAPT ER 21 Verti cal Flight -Jet and Prop 80 1 
the effects of unstead y flow, nonu niform induced velocities, regions of 
reversed flow, dynamic stall, blade flapping, and even dynamic blade 
bending and twisting. Numerical methods typically follow a blade around 
one rotation, integrating the forces and moments acting on the blade to 
calculate the vertical position of the blade after one complete revolution. 
The co mputer program iterates until the calculated end position equals 
the start position, as it must in the real world. Then thrust and torque 
can be summed. 
Figure 21.17 illustrates research at NASA Ames Research Center into the 
application to helicopters of unstructured grid, Reynolds-a veraged NavierStokes (NS) methods (see Chapter 12). The gridding of the flowfield 
around a rotor is illustrated, along with calculated pressure contours on 
a Comanche helicopter from a different analysis. Curre ntly, full NS CFD 
analysis of the complete helicopter including spinning rotor blades and 
blade vortex interactions is just possible, but difficult and expensive. Research 
is progressing rapidly. 
f lfff Hel icopter Range Anal ysis 
As mentioned in the intro duction to this section, there is no equation 
for helicopters equival ent to the Breguet range equation [Eq. (3.5 )], which 
for aircraft directly relates the fuel burned to the range obtained. Calculation 
of helicopter range or the sizing of the helicopter to a range requirement 
must be done by a method similar to that used in the most sophisticated aircraft range calculations progr ams. The actual drag is calculated at the current 
flight cond ition, then the power setting required to overcome that drag is 
Fig. 21 .1 7 Helic opter CFO nu merical methods (NASA Ames Resea rch Center ).


<!-- p.804 -->

802 Ai rcraft Desig n: A Conce ptu al Appr oach 
calculated, and then the engine's fuel con sumption data are used to determine fuel flow. 
For helicopters, the fuel used during a cruise mission segment is estimated as follows: 
1. Assume a helicopter weight (between the start weight and the end weight 
of crui se) . 
2. Calculate power required using the previous equations, or by iteratin g 
power until the desired veloci ty is obtained using more sophi sticated 
analysis techniques. 
3. Calculate or look up the fuel flow at that power setting. 
4. Calculate the specific range (distance traveled per unit fuel used) as 
velocity divided by fuel flow. 
5. Iterate back to step 1, assuming another helicopter weight. Then, plot 
speci fic range vs helicopter weight. The total range is found by graphical 
integration, that is, the area under the curve. 
This is actually similar to the derivation of the Breguet range equation 
where we integrated a speci fic range equation with respect to a change in aircraft weight. The reason that we cannot derive a similar direct equation for 
helicopt ers is that there is nothing equivalent to L / D since the rotor provides 
both lift and thrust. 
For loiter, the same method is followed, but the spe cific loiter (time per 
unit fuel used) is graphic ally integrated rather than the specific range. 
#JH:I Helic opter In itial Sizing 
To determine a first estimate of helicopter weight and fuel weight to 
perform the required mission, we use the aircraft sizing equation [Eq. 
(3.4)], repeated next. Fuel fraction is found, not from a mission- segment 
fuel fraction based on Breguet, but from the "known-time fuel burn" equation 
[Eq. (1 9.6)] that is modified to use power speci fic fuel consu mption and the 
helicopter power loading in Eq. (21.18 ). The total mission duration is 
assumed from the desired range and cruise speed, plus an allowance for 
takeoff and climb. This assumes that the helicopter flies at nearly full 
power throughout the mission, ignoring the effect of the weight reduction 
as fuel is burned, so it is probably conser vative, and we can safely ignore 
the time spen t in descent and landing. Helicopt ers typically require a 5% 
margin on engine fuel consumption plus a 10% fuel res erve, or an allowance 
equal to 20-30 min of flight at best loiter speed. 
Wcrew + Wpayload Wo = ----------1 - (ltj/Wo) - (We/ Wo) 
Wi Cpowerd 
--= l- -=--wi-l W/P 
(21. 17) 
(21.18 )


<!-- p.805 -->

CHAP TER 21 Ver tical Flig ht-Jet and Prop 803 
Table 21 .4 Helic opter Emp ty Weigh t Frac tions 
Air craft Type 
Scout /attack helic opter -ligh t ar mor and wea pons 
Scout /atta ck helic opter -he avy armor and wea pon s 
T ro nspor t helic opter 
Civil /util ity hel icopter 
Tilt rotor 
Typical We/ Wo 
0.5 -0.6 
0.6-0 .8 
0.45 -0.55 
0. 45-0.6 
0.5 5-0 .7 
Empty weight fraction is determined historic ally; typical data are in 
Table 21. 4, but actual data for a similar helicopter should be used where 
available. Note that the empty weight fractions in the table are not given 
as functions of takeoff weight as they were for fixed-wing aircraft. The historical data do not suppor t such a trendline. This does simplify the solution 
of Eq. (2 1.17 )-u nlike the case with fixed-wing aircraft, no iterati on is 
required! 
llffl Helic opter Design Process 
Helicopter design is similar to the steps described in the Intermission 
between Chapters 11 and 12, but with certain key differences. As with aircraft, you must have desi gn requirements to begin, including payload and/ 
or number of passe ngers, range, rate of climb, and certain flight speeds 
espec ially maximum and cruis e. For a helicopter you also need allowab le 
autorotate descent speed and required hover ceiling (in- or out- of-ground 
effect) . As with an aircraft, you must gather a lot of data such as internal component geometries and weights and should also iden tify some candidate 
engines and obtain geometric, weights, and performance data. 
You might wish to develop design sketches of alternative configura tion 
concepts, including different options for rotor configuration and antitorque 
technique. The next task is to select initial values for W /A and W / P and 
perform initial sizing calculations to estimate design takeoff gross weight 
and fuel weight. 
A fixed-wing aircraft designer would continue on developing an initial 
configuration layout based on these initial estimate s. However, at this time 
the helicopter designer will proba bly run a computer program to better calculate and optimize the rotor parameters including details as to soli dity, blade 
shape, airfoil, twist, and similar parameters, and determine in more detail the 
optimal disk loading and the required power. 
Then, the actual design layout can be developed as described in the 
Intermission .


<!-- p.806 -->

804 Ai rcraf t Design : A Conceptu al Appr oach 
' 
STS l l 4-S-03 7 Spac e Sh uttle launch (NASA pho to) . 
Whar We've Learned 
Vertical flight is difficult and greatly compromises the aircraft desi gn, but is 
well worth it for certain missions. Helicopters are more efficient than jet 
VTOL but cannot go fast.
