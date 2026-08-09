# Raymer Ch.15 - Weights

*Converted from `Daniel P. Raymer - Aircraft Design_ A Conceptual Approach (2018, American Institute of Aeronautics and Astronautics Inc.) - libgen.li.pdf` by `tools/pdf_to_md.py`. Page markers are printed page numbers.*


<!-- p.559 -->

Weights 
• Weig hts esti mations dr ive the entir e res ult for ai rcraft desi gn. 
• Excess weight kills many "good" ideas. · 
• Concept ual de sign methods are hig hly sta tis tica l (nothing wrong with that! ). 
• Better statist ical methods sta rt with an unde rlying phy sic s-ba sed model . 
• "Right" ans wers come at the end of de ta iled design, but by then it is too late. 
In trod ucti on 
IJjll Weig hts Engi neeri ng-a Critic al Disci pline 
T he sizing and performance equations described throughout this book 
use analysis parameters in three disciplines, namely aerodynamics, 
propulsion, and -eights. All are impor tant to the calculations, and 
all have a huge effect on the takeoff gross weight, performance, cost, and 
viability of a design. Aircraft design organizations typically invest a lot of 
time, effort, and funding to develop methods and get good answers in the 
field of aerod ynamics. Engine companies do the same thing for the field of 
propulsion and work with the airplane companies. 
What about weights? The weights estimate is just as important as the 
other two, yet gets surprisin gly little attention in the formal discipline of 
aircraft design. This author knows of no university where an aeronautical 
student can major in weights engineer ing, nor of a chaired professor ship in 
aerospace weights engineering methodologies. There are few archival publications on aerospace weights engineering topics. In fact, some people seem 
to think that you can get a credible answer with a handful of equations 
developed from first principles by people who have never actually worked 
in the field. Imagine claiming that for aerodyna mics! 
559


<!-- p.560 -->

560 Aircr aft Desi gn: A Conceptual Approach 
And yet, the estimation of the weight of a conceptual aircraft is a critical 
part of the design process. In the past 30 years there have been many important aircraft development projects that have been canc elled or suffered performance pen alties due to weight growth. The A- 12 was to be a carrier -based 
stealthy attack bomber replacing the A-6 but fell to weight problems after 
billions were spent. Early estimates of the weight savings from composite 
materials simply did not materialize in full, espe cially after the intense 
loads from carrier operations were factored in. 
Weights problems have dogged the F-35B Joint Strike Fighter (JSF), 
designed to replace the Harrier. l11 2l The novel VTOL equipmen t (see 
Chapter 20) is heavier than early estimates, and the total empty weight is 
almost 10% over predictio ns. The designers have had to cut the internal 
payload in half, eliminate the internal gun, and reduce the limit load factor 
from 9 to 7 g. 
When talking about weights engineers, it is impor tant to realize that 
there are two different types. Most weights engineers work in detail design 
and production and are ess entia lly referees and acco untants. They keep 
track of the weight of the design, which in detail design is most ly estimated 
by multip lying material dens ity by the volume of the part as seen on the 
drawing or CAD file. They also track the weight of a particular airframe as 
it moves through the production floor and certify the weight and balance 
information for each airplane before it flies. This is an impor tant job, but 
there is another type of weights engineer with a compl etely different set 
of skills. 
The Advanced Design department has weights engineers who some times 
seem like magician s. They can take an initial Dash- One design layout and 
tell you what its compon ents will weigh, even the parts that aren't on the 
drawing! Magic-or at least years of experience and a rare talent. This type 
of weights engineering is the subject of this chapter. 
The skill set of a good advanced design weights engineer is broad and 
varied. An understanding of aircraft structures and mechanisms is obviously 
required, proba bly obtained through a degree in aero nautical or mechanical 
engineering plus a lot of experience. A strong background in statistics and 
regre ssion analysis methods is also required because we often estimate 
weights by compa rison to similar existing items. For example, when first proposed, the F-35B 's shaft- driven lift fan was unprecede nted, and there was no 
complete system "prior art" to reference for weight calcu lation, but the wise 
weights engineer could estimate its weight by comparison to similar equipment in helicopters- shafts, clutches, and gearboxe s- suitably adjusted for 
the greater power requirements . 
Advanced design weights engineers are often called upon to estimate the 
weight of a new technol ogy that has never been built, like the open-r otor jet 
engine being considered for next-gene ration airlines. Hop efully, the engine's 
own weight will be provided by weights experts at the engine compan y, but 
the installation weight must be estimated, and it might be different than for a


<!-- p.561 -->

CHAP TE R 15 Weig hts 56 1 
"normal" jet engine. This requires enough technolo gical savvy and breadth to 
understand the new technolog y and assess its weight impact. It also requires 
good communication skills: sometimes the truth is "out there," and the 
weights engineer needs to find the people who know. 
One more required skill -persistence. The weights engineer is often the 
bearer of bad news and gets yelled at by designers and proj ect managers 
alike. If the weights engineer bows to their demands and lowers the 
weights estimate or takes out some of the margin, disaster can ensue. 
But there can be another side to this. Sometimes the weights engineers 
get so cons ervative that future progress is stifled, buried under the "weight" 
of their unwillingness to put their necks out a bit. If everything new seems 
to weigh a lot more than the things we know, we'll never make any progres s. 
AEJf J Weig hts Estimation Methods 
There are many methods and many levels of weights analysis. Previous 
chapters have presented quick statis.tical techniques for estimating the 
empty weight for a given takeoff weight, even before the Dash-One desi gn 
layout has been made. Once a real design layout is made, those methods 
are replaced by compo nent weight calculation methods as described belo w. 
Fundamentally, there are four different ways that compo nent weights can 
be estimated. The first is "His torical Analog y," where a new compon ent is 
thought to be similar to a compon ent from an existing airplane, so it prob ably 
weighs about the same. For this reason, weights engineers are always look ing 
for data on existing airplanes wherever it can be found. 
Often some adjustments are required. For example, if a new airplane 
design has a canopy similar to that of the F-22, it proba bly weighs about 
the same. But perhaps it is subs tantially smaller-it should weigh less. The 
weights engineer might decide to adjust the weight by ratioing based on 
the difference in surface area. For other items such as landing gear, the ratioing might be done based upon takeoff gross weight, or empty weight, or some 
other parameter. 
"Statistics" is similar to historical analog y, but with more samples. 
Perhaps, in the previous example, the weights engineer can get data on 
many canopies. Rather than adjust the weight for a single parameter such 
as surface area, statistical "curve-fit" methods can be used to find an equation 
relating canopy weight to several parameters, perhaps surface area, maximum 
speed, and maximum altitude. 
The parameters are chosen based on guess and calcula tion. First, the 
weights engineer guesses a set of parameters that just might correlate to 
weight. Then a multivariable curve-fit routine is used to find the constants 
and exponents in an equation that matches, with minimum error, the available actual values. Any parameter that gets an exponent very near to zero is 
unimportant and is removed from the next curve-fit calculat ion. Eventually, a 
suitable equation is obtained.


<!-- p.562 -->

562 Aircr aft Desig n: A Conceptual Approach 
Such a "blind statist ics" model is usua lly based upon an equation where 
the parameter is raised by an exponent and then multiplied by a constant 
(see Chapters 3 and 8). Such an equation represents a straight line on 
log-log graph paper-it seems that much of the universe follows this 
simple model! Methods for such curve fits are readily found, such as the 
linear least-sq uares curve fit method, which can be used to find a singlevariable equation of form y = Axe simply by taking the natural log of both 
X and Y values before applying the curve tit. For more than one parameter 
variable, a step -sea rching method is suitabl e. 
The best of the statistical equations are actually not "blind ." Going back to 
the 19 30s, weights engineers have developed equations by starting with a 
simplified analyti cal model, what is often called a "physics-based" model 
today. For example, a wing model could be written by relating the geometric 
parameters such as area, aspect ratio, and sweep, to the geomet ry of simplified wing spars and skins. A simplified load model is then applied, probably 
based on aircraft takeoff gross weight and maximum load factor, and the 
equation is sol ved for total volume. Multiplying this by a typical material 
dens ity gives an equation that predicts wing weight given wing geome try, 
aircraft weight, load factor, and perhaps other parameters. 
The job is half done. Next, the weights engineers would note that such 
equations rarely match data for actual airplanes. They would get data on as 
many airplanes as possi ble and load it all into a computer program in 
which the constants and expon ents of the physics-based model are subtly 
adjusted until the equation does a better job of predicting weights . 
Such equations can be very good predictors of component weight, but 
there is a danger. If a new design has a parameter that is far from the values 
of the airplanes used to calibrate the equation, it might give an answer that 
is very wrong. If you design a com mercial transport with a wing aspect ratio 
of 50, don't use the wing statistical equation presented below! 
To acquire a statistical database for developing such equations, weights 
engineers must obtain group weight statements and detailed aircraft drawings for as many current aircraft as possible. This has resulted in weights 
engineers trading group -weight statements much like baseba ll cards ("I'll 
trade you a T-45 for an F- 16 and a C- 17 "!). Unfortunately, this is no longer 
pos sible in the days of "black" program secu rity, so our real-world weights 
correlations are some what stuck in the past and need "fudge-factor" adjustments for modern designs. 
Useful statistical weight equations for various classes of aircraft are presented below. For most aircraft they work very well, provided that suitable 
technology adju stments are applied. 
When the design project moves into prelim inary and detail design, other 
component weight estimation methods become useful. One is "Compon ent 
Selecti on." Some components in a new airplane might litera lly be taken 
from an existing airplane. Use the actua l weight. This is more typical at the 
compon ent level, for example, in the avionics system when actual radios


<!-- p.563 -->

CHAPTE R 15 Wei gh ts 563 
and radars are being selected. During conceptual design, the avionics is probably estimated by historical ratio for the whole system. The same can be true 
for other subsystems such as landing gear, hydraulics, and electrics. The 
engine is another obvious example. 
Finally, weight can be estimated by actually designing and analyzing the 
component parts. This "Structural Analy sis" approach happens late in the 
design proc ess, normally during detail design. Not only do you need good 
design layout geometry for all of the parts, but you need to define all of the 
loading conditions that could poss ibly affect the part. Then you perform 
structural analysis to determine the stresses and other criteria, use material 
properties to selec t thicknesses of materials, calculate the volumes, and multiply by materi al densities to get the part weight. You must also add weight for 
finishes, fasteners, fittings, attachments, access panels, mechanisms, and the 
like. This is a large team effort, taking months or years . 
If JU Weig hts Reporti ng and C.G. Esti mation 
Component weights are calcu lated by the methods described above, 
perhaps using the equations in the following sections. Once calculated, 
the weights are usually reported in the standard 
"Summary Group Weight Statement" format 
shown in Table 15.1. This was defined by the old 
MIL-ST D-1 374, which is now administered by the 
Society of Allied Weights Engineers as SA WE-8 
(see www.sawe.org). This spec ification goes into 
exhaustive detail (taxi lights) , but at the conce ptual 
Never change the 
takeoff gross 
weight on the 
Group Weight 
Statement! 
level the major compon ent weights are summarized. They are classified 
into three major groupings (structure, propulsion, and equip ment) , which 
sum to the aircraft empty weight. This, plus the "useful loa ds group" including crew, payload, and fuef, sums to the takeoff gross weight. 
This group weight statement format is available as an Excel spreadsheet 
at the author's website, www.aircraft desig n.com. 
The structures group consists of the load-ca rrying componen ts of the 
aircraft and ess entially contains the major items that the aircraft manufacturer produces. Note that it usually includes the inlet (air- induction- system) 
weight and also the nacelle (engi ne-sect ion) weight including motor mounts 
and firewall provis ions-d espite their obvious relationship to the engine. 
However, if the engines are in separate podded nacelles, then their nacelle 
and inlet weights might be included in the propulsion group. 
The propulsion group contains the engines plus the engine-related equipment such as starters, exhaust, etc. The as- installed engine includes the propeller, if any. The fuel system is included here, but if the fuel tanks are 
sealed-off pieces of aircraft structure, they remain in the structures group. 
The equipment group is most ly things that the aircraft comp any purchases and bolts into the airplane, such as avionics and the elec trical


<!-- p.564 -->

564 Aircr aft Desig n: A Conceptual Appr oa ch 
Wing 
Horizontal toil 
Vertical toil 
Ventral toil 
Fuselage 
Main landing gear 
Nose landing gear 
Other landing gear 
Engine mounts 
Firewall 
Engine section 
Air induction 
Engine( s)-inst al led 
Accessory drive 
Exhaust system 
Engine cooling 
Oil cooling 
Engine controls 
Starter 
Fuel system/tanks 
Table 15 . 1 Group Weight State ment Format 
• 
.. : 
14 59 .4 23 .3 34 ,004 
280.4 39.2 10 ,992 
0 0 
0.0 0 
15 74 21 . 7 34 . 15 6 
63 1 . 5 23 .8 15 ,0 30 
17 1 . 1 13 .0 2224 
0.0 0 
39 . 1 33.0 12 90 
58.8 33.0 19 40 
21 33 .0 693 
29 1.1 22.5 6550 
0 
1517 33 .0 50,061 
0 
0 
17 2 33.0 5676 
37.8 33 .0 12 47 
20 33.0 660 
39 .5 15 .7 620 
568 22 .3 12 ,666 
0 
0 
0 
0 
Flighl controls 
APU 
Instruments 
Hydraulics 
Pneumatics 
Electrical 
Avionics 
Armament 
Furnishings 
Air conditioning 
Anti-icing 
Photographic 
Load & handling 
Mise equi pment & W, 
Useful load 
Crew 
Fuel-usable 
Fuel-trapped 
Oil 
Passengers 
Corgo /poylood 
Guns 
Ammunition 
Mise usefu l load 
Weigh! 
lbs 
... 
655 . 7 
12 2.8 
17 1. 7 
71 3.2 
989 .8 
21 7 .6 
19 0.7 
5.3 
10 00 
0.0 
10 .0 
21 .7 
21 .7 
21 .7 
10 .0 
0.0 
6.2 
15 .0 
15 .0 
31 .8 
49ss I 
220 15 .0 
3836 22.3 
39 22 .3 
50 33.0 
840 21 .7 
0 21 .7 
1 4,229 
0 
1 228 
3726 
0 
15 .4 76 
9898 
0 
13 49 
2860. 5 
0 
0 
79.5 
31 .800 
3300 
85.551 
864 
16 50 
0 
18 .228 
0 
0 
Takeoff gross weigh! I 16 .480 22.0 362. 744 
system. Armament is broken down into fixed items, which are in the equipment groups, and expendable items, which are in the useful load. Sometimes 
a ju dgment call is required. For example, a gun might be cons idered to be 
fixed equipment, or it might be viewed as readily remo vable and unim portant 
to flight and therefore a part of the use ful load. 
The stru ctures, propulsion, and equipment groups are summed to find 
the as- drawn empty weight. We often add an empty weight allowance of 
3-15 % at this point to allow for future weight growth and requirem ents 
creep. This margin gets summed into empty weight. 
Som etimes we add another type of margin here which really shoul d be 
factored in sep arately. Early in the design process we simply don't kno w 
enoug h about our design to know that we've included all items. We'll throw


<!-- p.565 -->

CHAPTER 15 Weig hts 565 
in an additional percentage, perhaps 5%, to account for all the "unkno wnunknowns" that the design may be hiding. 
The takeoff gross weight must be the sum of the empty weight and the 
useful load, including crew, payload, and fuel. This does not mean that we 
"add them up" to find the takeoff gross weight. The design layout was based 
around the initial estimate of Wo, which was used to size and calcula te the 
weights of the wings, tails, engines, landing gear, and more. If we magically 
change Wo on the group weight statement, all of those calculations are 
invalid. Inste ad, the fuel weight is adjusted up or down until the correct Wo 
is found. 
The takeoff gross weight reflects the weight at takeoff for the normal 
design missi on. The flight design gross weight represents the aircraft weight 
at which the structure will withstand the design load factors. Usually, this is 
the same as the takeoff weight, but some aircraft are designed assuming 
that maximum loads will not be permitted until the aircraft has taken off, 
climbed to altitude, and cruised some distance, thus burning off some fuel 
in the process. For military aircraft it js often assumed that flight design 
gross weight is takeoff weight but with only 50-6 0% of fuel remaining. 
For certain cost calculat ions, a subset of the empty weight is useful. 
Called the DCPR or Defense Cont ractors Planning Report weight, this can 
be viewed as the weight of the parts of the aircraft that the manufacturer 
makes, as opposed to buys and installs. DCPR weight equals the empty 
weight less the weights of the wheels, brakes, tires, engines, starters, 
cooling fluids, fuel bladders, instruments, batteries, electrical power 
supplies / converters, avionics, armament, fire-con trol systems, air conditioning, and auxiliary power unit. DCPR weight is also referred to as AMPR 
weight (Aeronautical Manufacturers Planning Report) , and sometimes as airframe unit weight. 
In a group weight statement, the distance to the weight datum (arbitrary 
reference point) is defined . and the result ing moment is calculated. These are 
summed and then divided by the total weight to determine the center -ofgravity location. However, the e.g. can vary subs tantially during flight. This 
is calculated by assu ming various fuel tanks have been emptied, landing 
gear has been retracted or extended, and other changes. The weight and 
e.g. for these different flight configurations are calculated and posted below 
the group weight statement, espe cially for the most-for ward and most-a ft 
results. 
To determine if the e.g. remains within the limits necessa ry for safe flight, 
a more-detailed "C.G.- Envelope" plot will be prepared (Fig. 15.1). This shows 
the current aircraft weight on the vertical axis and the correspo nding e.g. 
location on the horizon tal axis. It illustrates the e.g. loca tion throughout 
the mission as fuel is burned off, payload is dropped, wings are swept, or passengers congregate in back after dinner. Allowances for different payload 
loading arrangements must also be considered for some aircraft, espec ially 
large cargo airplanes.


<!-- p.566 -->

566 Aircr aft Des ign: A Con cep tual Appr oach 
Gross weight 
Wiand 
..., 
.s 
Ci 
u 
re 
0 u._ 
Take off 
e.g. location, % M.A.C. 
from Datum 
Fig. 15 .1 Center -of-g ravit y envelope diagr am. 
..., 
E 
Ci 
u 
.:= <( 
The difficult part of prep aring the C.G.- Envelope plot is determinin g 
exactly what those limits are. An old rule-of -thumb says that those limits 
must be sep arated by no more than 8% of the wing MAC. Finding the 
actual limits is a lot of work. These are often established by stability and 
control analysis, but structural limits must also be con sidered. 
Typically, the forward limit is set by elevator effectiveness for takeoff 
nose wheel rotation, or by pullup or level turn at some flight condition (see 
Chapter 16). Perc ent of weight on the nose wheel can be a limit, to avoid 
the "porpoi sing" described in Chapter 11. It can be set by trim drag, where 
a c.g.-for ward condition requires excess elevator deflection causing drag. 
The forward limit can also be set by various structural sizing cond itions, 
such as excessi ve "slapdo wn" loads on the nosewheel and adjacent structure . 
An X- 15 litera lly broke in half when a rough landing exceeded its slapdow n 
load. This "slap down" limit may appear as a corner clipped off the upper left 
side of the envelope. 
The aft- c.g. limit is usually set by directional stab ility as descr ibed in 
Chapter 16. The vertical tail area is set to an assumed e.g. and the plane 
shouldn't be flow with the e.g. any farther aft. Engine-out consid erations 
may also play a role. Sometimes the aft-c.g. limit must be moved forward 
because of spin entry or recovery problems, which may be learned only 
after detailed wind tunnel, spin tunnel, or flight tests. The aft e.g. limit 
could also be set by landing gear geom etry. Too little weight on the nose 
wheel might make steering difficult, or even result in a parked airplan e 
doing a "wheelie" as passe ngers disembar k from the front!


<!-- p.567 -->

CHAPTER 15 Weig hts 567 
There is a Mach effect on stabil ity that affects the e.g. limits as the aircraft 
aoes faster. When approa ching supersonic speeds, the aerodynamic centers 
-f wings and tails move rearward as descr ibed in Chapter 12, so the 
forward-c.g. limit might have to move rearward to allow longitudinal trim 
or pullup at supersonic speeds. At the same time the aft-c.g. limit may 
move forward because the vertical tail, like any lifting surface, loses effectiveness at supersonic speeds. This may require making the tail subs tantially 
bigger than required for subsonic flight. 
It is permissible to "se quence" the fuel tanks, selec ting to burn fuel from 
different tanks at different times to keep the e.g. within limits . For safety this 
should be done with an automated fuel management system. Other wise, a 
fairly minor "pilot error" could cause a crash. 
A sophisticated fuel management system can autom atically pump fuel 
between tanks to move the e.g. to the rear when approaching supersonic 
speeds. This is done in some commercial airliners and many military aircraft. 
This imposes additional cost and complexity and provides one more catastrophic failure mode. During the flight t-st of the B- lA, the fuel management 
system was turned off for test purposes while flying at supersonic speeds with 
the wings swept aft. Fuel had already been pumped to the rear. When they 
slowed down and unswept the wings, they forgot to turn it back on. The airplane crashed, and the company's lead test pilot died. 
Figure 15.l shows one typical format for a e.g. envelope diagram, based 
upon orthogonal graph paper. Another popular format looks like a part of 
a paper fan, with the x-axis narrowing as it goes to the bottom. Those fan 
lines would actually meet far below, at the weight = zero point. This 
format is more complicated to make but has the advantage of allowing the 
lines for fuel tank usage to be slid around the graph to quickly determine 
the effect of sequencing the tanks. In the graph paper format, this gives a 
slightly incorrect result. 
'fl App roxim ate Weight Methods 
For a quick look, the weights of the major aircraft componen ts can 
be approximated from simple ratios. For example, general aviation wings 
typically weight about 2.5 lbs/ft 2 {12 kg/m 2} of exposed wing area. Landinggear weight is typically propo rtional to the aircraft takeoff gross weight, 
roughly 5.7% for general aviation. These aren't very good estimates, but 
they are quick! 
Such historical values for various classes of airplane are provided in 
Table 15.2, along with their approximate loca tions on the componen t. 
These can be used early in design to make a rough e.g. estimate, checking 
that the desi gn isn't way off before it is finalized and analyzed proper ly. 
Note that wings and tail weights are based on their exposed planform, 
that is, the projected area of the exposed part of the wing. The fuselage 
weight is based upon its total wetted area. The installed engine weight is a


<!-- p.568 -->

Wing 
Horizonta l ta il 
Vertical ta il 
Fuselage 
La nding gear * 
Landing gear -N avy 
Ins talle d engine 
"All-else em pty" 
Table 15 .2 Appr oxi mate Emp ty Weight Buildup 
Fig hter s Transport & Bomber 
1''1JlWMiiWlllJJW 
9 44 l 0 49 
4 I 20 
5.3 I 26 
4.8 23 
Weigh t Ratio 
0.0 33 
0 .045 
1 .3 
0.1 7 
5.5 
5.5 
5 
IEllmE 
0.0 43 
1. 3 
I 0. 17 
27 
27 
24 
-illi,'ll-'ll'lli' 
limmli 
2.5 12 
2 10 
2 10 
1. 4 7 
mllimm 
0.057 
1 .4 
0.1 
Mul tiplier Appr oxima te Location 
Sexpose d planform 40% MAC 
Sexpose d planform 40% MAC 
Sexpose d planform 40% MAC 
Swetted area 40-50% length 
TOGW centr oid 
TOGW centr oid 
Engine weight centr oid 
TOGW 40-50% length 
* 15 % to nose gear, 85% to main gear: red uce gear wei gh t by O.Dl 4 Wo if fixed gear. 
UI 
0. 
()) 
... 
0 
... 
0 
:::t 
0 
<!> 
(,/) 
<.6' 
::i 
}> 
0 
0 
::i 
0 
<!> 
"'O 
-+ 
c 
0 
}> 
"'O 
"'O 
0 
Q 
0 
:T


<!-- p.569 -->

CHAPTE R 15 Weig hts 569 
iJ Furnishings 54 TOGW (W0) 2000 
['l Air condition ing 29 
D Avionics 29 
D Ele ctrica l 56 
D Hydra ul ics 4 
l!ll In stru ments 
0 Flight contr ols 
Ill! Engine ins t 
0 Engine 272 
D La nding gea r 
D Fuselage 
llll Tails 
ll!l Wing 
0. 0000 0.0500 0.10 00 0.1 500 
W!W0 
Fig. 15 .2 Weight budget. 
multiple of the uninstalled engine weight. The term "all else empty" is used to 
approximate the rest of the comp onents for balance calculat ions. 
Suc h quick results can also be used to check the results of the more 
detailed statistical methods later. If the later calculation says that a generalaviation (GA) airplane wing of 100 ft2 should weigh 90 lb, something is probably wrong! 
Another tool common ly used early in a design proj ect is the "weight 
budget." This is simply a listing of the major compo nents of the aircr aft, 
with rough estimates of their weight based on statistical ratios for typical aircraft in that class. An example for a new genera l aviation is shown as Fig. 15 .2. 
The ratios in this sample were taken from a number of GA and homebui lt 
airplanes including the BD-5, Cessna 17 2, and T-3 4C. 
A weight budget is NOT a target. If the wing weighs less than the budget 
implies, don't add rocks until the budget is met! It merely acts as a guide and 
a r eality check while the detailed calculations described below are being 
perfo rmed. 
' Ai rcraft Statis tic a l Weig hts Method 
A more refined estimate of the aircraft compo nent weights can be done 
using statistical equations based upon sophisticated regre ssion analys is,


<!-- p.570 -->

570 Air craft De si gn: A Conceptual Appr oa ch 
in some cases initiated with physics- based models. Development of these 
equatio ns represents a major effort as just descr ibed, and each company 
develops its own equatio ns. Luckily, some of them have been publ ished 
and are presented below, selec ted by this author as the best available 
methods having a reasonable number of inputs. 
The following equations typify those used in concept ual design by the 
major airframe companies and cover fighter/ attack, transpor t, and gener alaviation aircraft. They have been taken from (113-1 15] and other sources. 
Definitions of the terms follow the equat ions. A critical term Wdg is the 
flight desi gn gross weight. For military aircraft this is often less than the 
maximum takeoff weight. A common assumption is that only 50-6 0% of 
the fuel remains. 
Several of the weights categories below need explanat ion. Weng section 
is primar ily the motor mounts plus engine-asso ciated equip ment. 
wflight controls includes the mechanisms, actuators, control linkages , and 
in-co ckpit controls but not the weight of the actual control surfaces such 
as ailerons and flaps. Those are included in the wing and tail weight 
equatio ns. 
Wfurnishings typically includes items needed by the crew such as crew 
oxygen, fire suppression, and similar gear. The equations below for fig hter 
and GA aircraft do include the seats (eje ction seats for the fighters), but 
the equation for transpor t aircraft does not (see Table 15 .3 instead) . 
Whandling gear covers things like jacking pads, tiedowns, towhook attach ments, and the like. It is different from cargo handling gear, which includes 
the powered rollers that move pallets into position and lock them down. In 
the SA WES standard weights format they are lumped together. Kneeling 
landing gear is uncommon but is seen on the C-5 where the landing gear 
can lower the aircraft closer to the ground for lo ading. 
It should be understood that there are no "right" answers in weights estimation until the first aircraft flies. However, these equations should provide a 
reasonable estimate of the group weights. Other, similar weights equations 
can be found in[lG ,ls, 4oJ . It's a good idea to calculate the weight of each component using several different equations and then select an average, 
reasonable result. 
All weights analysis includes a lot of judgement and best- guesses by 
the person doing the estimation. It is common, even mandator y for "fudge 
factor" adjust ment of any equation result. These include adjustments for 
different technologies (espe cially what we always call "advanced"), different 
fabrication methods, geom etric differences from the "normal" designs 
assumed in the statistical equations, and sometimes just the weight analyst's 
gut feeling. Such adjust ments are described in Section 15. 4. 
Needless to say, these equations are complica ted, and it takes a lot of time 
to apply them succes sfully. Mistakes are easy, the most common being the 
use of limit load factor, where ultimate load factor Nz should be used 
instead. In the first edition, this author used a pocket calculator for the


<!-- p.571 -->

CHAPTE R 15 Weig hts 57 1 
Table 15 .3 Mi scella neous Weig hts (Approxima te) 
Component 
Mi ssiles 
Har poon (AGM-84) 
Phoe nix (AI M-54 A) 
Spa rrow (AIM-7) 
Side winder (AI M-9) 
Pylon and laun cher 
M61 Gun 
Gun 
940 rds ammu ni tion 
Comme rcial ai rcraf t pass enger 
(inclu des ca rry-on) 
Seats 
Fligh t deck 
Passe nger 
Troop 
Instru me nts 
Alti meter, air speed, 
acceler ome ter, rote of climb , 
cl ock, compass, turn & bank , 
Mach, tachom eter, man ifold 
pressu re, etc . 
Gyro horizon, dir ectiona l gyro 
Heads -up di splay 
Lavato ries 
Long-r o nge a i rcroft 
Shor t-ra nge air craft 
Busi ness / exec utive ai rcraft 
Arres ting gear 
Air Force-type 
Navy-type 
Cata pult gear 
Navy carri er-based 
Folding wing 
Navy carrier -based 
*M ass equ iva lent of weight. 
Weigh t 
12 00 
10 00 
500 
200 
0.1 2 W missile 
250 
550 
19 0 
60 
32 
11 
1- 2 each 
4-6 each 
40 
l .l l NJa-; 
0.31 NJa-; 
3.90 NJa-; 
0.0 02 Wdg 
0.008 Wdg 
0.0 03 Wdg 
0.06 Wwing 
544 
454 
227 
91 
11 3 
250 
86 
27 
15 
5 
0.5 -1 
2-3 
18 
0.5 NJa-; 
0. 14 NJa-; 
1 .76 NJa-;


<!-- p.572 -->

572 Airc raf t Desi gn: A Con ceptu al Appr oa ch 
Des ign Example weight calculations to "prove it could be done" and then 
made exactly this mista ke-now corrected! 
The RDSwin_Student compu ter program, available for purchase with this 
book, was created in part to help students with these calculat ions. RDSwin is 
described at www.aircraft design .com. 
Reference [18 ] tabulates group weight statements for a number of aircraft. 
These can also be used to help select a reasonable weight estimate for the 
compon ents by comp aring the component weights as a fraction of the 
empty weight for a similar aircraft. 
Table 15 .3 tabulates various miscellaneous weights. Other textbooks, old 
repor ts, and online sources can be used to find other such weights. 
When the compone nt weights are estimated using these or similar 
methods, they are tabulated in a Group Weight Statement (see Table 15.1) 
and are summed to determine the empty weight. Because the payload and 
crew weights are known, the fuel weight must be adjusted to yield the 
as- drawn takeoff weight that is the sum of the empty, payload, crew, and 
fuel weights. 
If the empty weight is higher than expected, there might be insufficient fuel 
to compl ete the design mission. This must be corrected by resizing and optimizing the aircraft as described in Chapter 19 , not by simply increasi ng fuel 
weight for the as- drawn aircraft (which would invalidate the compone nt 
weight predictions that were based on the as- drawn takeoff weight) . 
Mf DI Fig hter/ Attack Weight s (British Un its, Result s in Pound s) 
Wwing = 0.010 3KdwKvs(WdgNz)o.s 5-622 A 0·785(t/ c)root 
x (1 + A)0·05( cos A)-l. 05---4 
Whorizontal tail = 3.316 ( 1 + -:) -2.o (----z) o.260 S-t806 
Wvertical tail = 0. 452Krht(l + Ht/ Hv)05(WdgNz)0·488 se/18 M0·341 
x Lt i.o (1 + sr I Svtlo.348 Aei223 
x (1 + A)0.25( cos Avt)-0.323 
w. = 0 499/( w0.35 N0.25 L 0.5 x D0.849 w0.685 fuselage · dwf dg z 
w: ( W: N )0.290 L o.s N0.525 nose landing gear = l l n nw 
w: N0.795 T0.579N engine mounts = 0.013 en z 
(15 .1) 
(15 .2) 
(15 .3) 
(15 .4) 
(15 .5) 
(15.6 ) 
(15. 7)


<!-- p.573 -->

CH APTE R 15 We ig hts 573 
Wfirewall = l.13Sfw 
Wengines ection = 0.01 W--717NenNz 
W 
_ 
13 29v L0.643vo.1s2 air induction system - · 1'vg d 1'd 
x Nl.498(L /L )-0.373 D en s d e 
(15 .8) 
(15 .9) 
(15 .10) 
where Kd and Ls are from Fig. 15 .3. If Ls/ Ld is less than 0.25, use 0.25 
for this ratio. 
Wengine cooling = 4.5 5DeLshNen 
Woil cooling = 37.82N1-023 
w. lo 5Nl.008L0.222 engine controls = · en -ec 
w. - 0 025T0.760No.n starter(pneumatic) - · e en 
( v:) -0.095 Wfuelsystem andtanks = 7.45 Vt°'47 1 + (15 .11) 
(15 .12) 
(15 .13) 
(15 .14) 
(15 .15) 
x (i + Vp) N0.066 No.052 (T . SFC) 0.249 
Vt t en 1000 
w;fl. h = 36 28Mo.oo350.489N0.484N0.127 1g t controls · cs s c 
lv/. _ 8 0 + 36 37N0.676N0.237 
w instruments - · · en t 
+ 26.4(1 + Nci)1356 
Whydraulics = 37.23KvshN-·664 
w. 1 . 1 =1 72 2/(, Ro.152No.10Lo.10No.091 e ectnca · me kva c a gen 
W . . - 2 11 7W.0.933 av10mcs - · uav 
Wfurnishings = 217 .6Nc (inclu des seats ) 
Wairconditioning andantHce = 201 .6[(Wuav + 200Nc)/10 00]o.735 
Whandlinggear = 3.2 X 10-4 wdg 
(15 .16) 
(15 .17) 
(15 .18) 
(15 .19) 
(15 .20) 
(15.21) 
(15. 22) 
(15 .23) 
(15 .24)


<!-- p.574 -->

574 Ai rcraf t Des ign: A Concept ual Appr oach 
0 D 
Spli t du ct 
OD /- Ls J(d = 2.75 
In let front face 
Fig. 15 .3 Inle t du ct geome try. 
Eng in e 
front 
face 
4£ftJ Car go/T ransport Weight s (British Unit s, Result s in Pou nds) 
W, . = 0 005 l( W. N )0.55 7 50.649 A 0.5 (t/c) -0.4(l + A)O.l wmg · dg z w root 
x (cos A)-l.050.l csw 
Whorizontal tail = 0.0379Kuht(l + Fw/Bh)-0·25Wfg639N-·10 
x 50.75L-l. OK0.704( cos A )-1.0 ht t y ht 
x A-.166(1 + 5e/5ht)o.1 
w. 0 0026(1 + H /H )0.225 w0.556N0.536L-0.5 vertical tail = · t v dg z t 
x 5-5 K-.875 ( cos Avt)-1 Ae.35(t/ c)--·t5 
Wfuselage = 0.3280KdoorKLg(WdgNz)0·5L0·255J302 
X (1 + KwsP04(L/D)0·10 
(15 .25) 
(15.2 6) 
(15 .27 ) 
(15 .28) 
where Kws = 0.75 [(1 + 2A)/(1 + A)] (Bw/L) (tan A) to correct for effects of 
wing geom etry, espec ially sweep, on the fuselage weight. 
w. 0 010 6 T/ w0.888N0.25L0.4N0.321N-0.5 vo.1 main landinggear = · 1'-mp l l m mw mss stall (15. 29)


<!-- p.575 -->

CHAPTER 15 Weig hts 575 
, vr o 032 v w0.646No.2Lo.sNo.45 
w nose landing gear = · 1' np l l n nw 
(includes air induction and pylon) 
Wenginecontrols = 5. 0Nen + 0.80Lec 
1"en en (AT w. ) 0.541 
Wstarter (pneumatic) = 49 .1 9 lOOO 
Wfuel system = 2.405 Vt°"606(1 + Vi/Vi)-1.0(1 + Vp/Vi)N?5 
Wflightcontrols = 145.9Nj554(1 + Nm/NJ )-1.0 
x 50.20(1 x 10-6)0.07 cs yaw 
W APU installed = 2.2 W APU uninstalled 
\Vjnstruments = 4.509KrKtpN2·541 N;n(Lj + Bw)0·5 
Whydraulics = 0.2673Nj(Lj + Bw)0·937 
W. 7 291Ro.782L0.346No.10 electrical = · kva a gen 
W 1 W0.983 avionics = · 73 uav 
1 vr 0 0577No.l W0.393 ,...0_75 
w furnishings = · c c ;:c,j 
(15.3 0) 
(15 .31) 
(15.3 2) 
(15 .33) 
(15.3 4) 
(15.3 5) 
(15.3 6) 
(15.3 7) 
(15.3 8) 
(15.3 9) 
(15.4 0) 
(does not include cargo handling gear or seats) (15. 41) 
Wairconditioning = 62.36N-·25(Vpr/l 000)0·604w---O 
WantHce = 0.002Wdg 
Whandlinggear = 3.0 X 10-4wdg 
w . . 
= 2.4 x (cargo floor area, ft2) military cargo 
handling system 
(15 .42) 
(15 .43) 
(15. 44) 
(15 .45) 
If ffl Gener al Aviation Weig hts (British Un its, Resu lts in Poun ds) 
w, . = o 036S0.758w.o.oo35 __ 
qo.006 A0.04 ( A ) o.6 wmg . w fw cos 2 A 
(100 t I c) -0·3( )o.49 x 
A NzWdg cos 
(ignore second term if Wfw = O) (15 .46)


<!-- p.576 -->

576 Air c raf t Des ign: A Conceptual Approach 
0.414 0 .168 0.896 10 t c . ( 0 I ) -0 12 Whorizontal tail = 0.0l6( Nz Wdg) q S ht 
cos A 
x ( A ) 0.043 ,\ -0.02 cos 2 Aht h 
W'. 
( Ht) ( )0.376 0.122 o.873 vertical tail = 0.073 1 + 0. 2 Hv Nz Wdg q S vt 
x --,\ 0.039 ( lOOt/c) -0.49 ( A ) o.357 
cos Avt cos 2 Avt vt 
(If Avt is less than 0.2, use 0.2) 
w, - o 052 51.086(N W )0.177 L-0.051 fuselage - · 'j z d g t 
X (L / D)-0.072 q0.241 + Wpress 
Wmain landinggear = 0.095(Nt W1)0·768(Lm/l 2)0.409 
Wnose landinggear = O.l 25(Nt W1)0·566(Ln/l2) 0·845 
(reduce total landing gear weight by 1. 4% 
of TOGW if nonretractable ) 
W 0.922N. installed engine (total) = 2.5 75 wen en 
(includes propeller and engine mounts) 
0.726 ( 1 ) 0'363 0.242 0.157 Wfuels ystem = 2.49Vt l + Vi/Vi Nt Nen 
1vr l.536B0.371 (N W -4)0.80 Wflightcontrols = 0.053L w z dg X 10 
Wi v wo.8M0.5 hydraulics = 1'h dg 
Welectrical = 12 .5 7(Wfuel system + Wavionics)0.5l 
W'. W0.933 avionics = 2 .11 7 uav 
W 0 265wo.s2No.68 W0.17 M0.08 air conditioning and anti-ic e = · dg p avionics 
Wfurnishings = 0.0582 Wdg - 65 
Weig hts Equa tions Term inolo gy 
(1 5.47) 
(1 5.48) 
(15.4 9) 
(1 5.50) 
(15 .51) 
(15 .52) 
(15 .53) 
(15.5 4) 
(15.5 5) 
(15.5 6) 
(15 .57) 
(15.5 8) 
(15 .59 ) 
A aspect ratio (with subscr ipt "t" or "h" for horizon tal tail, "v" for 
vertical tail) 
Bh horizon tal tail span, ft


<!-- p.577 -->

Bw 
D 
De 
f w 
Ht 
Ht/Hv 
Hv 
I yaw 
Kcb 
f(d 
I< door 
KLg 
Kmc 
Kmp 
Kng 
Knp 
Kp 
Kr 
Krht 
Ktp 
Kt pg 
Ktr 
Kuht 
Kvg 
Kvs 
Kvsh 
Kws 
Ky 
Kz 
L 
La 
Ld 
Lee 
wing span, ft 
fuselage structural depth, ft 
engine diameter, ft 
fuselage width at horizo ntal tail intersection, ft 
horizont al tail height above fuselage, ft 
0.0 for con ventional tail; 1.0 for ''T" tail 
vertical tail height above fuselage, ft 
CH APTER 15 Weight s 577 
yawing moment of inertia, lb-ft 2 (see Chap. 16) 
2.25 for cross-beam (F-111 ) gear; = 1. 0 otherwise 
duct const ant (see Fig. 15 .3) 
1.0 if no cargo door; = 1. 06 if one side cargo door ; 
1.12 if two side cargo doors; = 1.12 if aft clamshell door; 
1. 25 if two side cargo doors and aft clamshell door 
0.768 for delta wing; = 1. 0 otherwise 
0.774 for delta -wing aircra ft; = 1.0 otherwise 
0.05 for low subsonic with hydraulics for brakes and retracts only; 
0. 11 for medium subsonic with hy-raulics for flaps; = 0. 12 for 
high subsonic with hydraulic flight controls; = 0.013 for light 
plane with hydraulic brakes only (and use M = 0. 1) 
1.12 if fuselage-mo unted main landing gear; = 1.0 otherwise 
1. 45 if mission completion required after failure; = 1. 0 otherwise 
1. 126 for kneeling gear; = 1. 0 otherwise 
1.017 for pylon- mounted nacelle; = 1.0 otherwise 
1.15 for kneeling gear (C-5); = 1.0 otherwise 
1. 4 for engine with propeller or 1. 0 otherwise 
1.13 3 if recipro cating engine; = 1. 0 otherwise 
1. 047 for rolling horizontal tail; = 1.0 otherwise 
0. 793 if turboprop; = 1. 0 otherwise 
0.826 for tripod (A- 7) gear; = 1.0 otherwise 
1.18 for jet with thrust reverser or 1. 0 otherwise 
1. 143 for unit (all-mo ving) horizontal tail; = 1. 0 otherwise 
1. 62 for variable geome try; = 1.0 otherwise 
1.19 for variable sweep wing; = 1.0 otherwise 
1. 425 for variable sweep wing; = 1. 0 otherwise 
wing sweep factor = 0.75 ((1 + 2A)/(l + A)] (Bw/L) (tan A) 
aircraft pitching radius of gyration, ft( - 0.3 Lt) 
aircraft yawing radius of gyration, ft ( - Lt) 
fuselage structural length, ft (excludes radome cowling, tail cap) 
electrical routing distance, generators to avionics to cockpit, ft 
duct length, ft 
routing distance from engine front to cock pit-t otal if multiengine, ft 
total fuselage length 
extended length of main landing gear, in.


<!-- p.578 -->

578 Air cr aft De sign: A Conc eptu al Appr oach 
Ln 
Ls 
Lsh Lt Ltp 
M 
Ne 
Nci 
Nmss 
Nmw Nnw 
Np 
Ns 
Nt 
Nu 
Nw 
N z 
q 
Rkva 
Scs Scsw Se 
sf 
Stw Sht 
Sn 
Sr 
Sstall Svt Sw 
SFC 
T Te 
extended nose gear length, in. 
single duct leng th (see Fig. 15 .3) 
length of engine cool ing shroud, ft 
tail length; wing quarter-M AC to tail quarter-MAC, ft 
length of tailpipe, ft 
Mach number (desi gn maximum) 
number of crew (use 0.5 for UAV) 
number of crew equival ents: 1.0 if single pilot; 
1. 2 if pilot plus backsea ter; = 2.0 pilot and copilot 
number of engines (tot al for aircraft) 
number of sepa rate functions performed by surface controls, 
including rudder, aileron, elevator, flaps, spoi ler, and speed brakes 
(typica lly 4-7) 
number of gener ators (typically = Nen) 
nacelle length, ft 
ultimate landing load factor; = Ngear x 1.5 
number of surface controls driven by mecha nical actuation inst ead of 
hydraulics (must be S.Nj and is typically 0-3) 
number of main gear shock struts 
number of main wheels 
number of nosew heels 
number of person nel onboard (crew and pass engers) 
number of flight control systems 
number of fuel tanks 
number of hydraulic utility functions (typica lly 5-15 ) 
nacelle width, ft 
ultimate load factor; = 1.5 x limit load factor 
dynamic press ure at cruise, lb/ ft2 
system electrical rating, kV · A (typically 40-60 for transpor ts, 
11 0- 16 0 for fighters and bombers) 
total area of control surfaces, ft2 
control surface area, ft2 (wing-mou nted, includes flaps) 
elevator area, ft2 
fuselage wetted area, ft2 
firewall surface area, ft2 
horizon tal tail area, ft2 
nacelle wetted area, ft2 
rudder area, ft2 
stall speed, kt 
vertical tail area, ft2 
trapezoidal wing area, ft2 
engine specific fuel consumption at maximum thrust, lb/h r/lb 
total engine thrust, lb 
thrust per engine, lb


<!-- p.579 -->

t/c 
Vi 
Vp 
Vpr 
Vt 
w 
We 
Wdg 
Wee 
Wuav 
A 
,\ 
CH AP TER 15 Weig hts 579 
thickn ess-to- chord ratio (if not constant, use average of portion of 
wing inboard of C-bar) 
integral tanks volume, gal 
self-sea ling "protected" tanks volume, gal 
volume of pressurized section, ft3 
total fuel volume, gal 
total fuselage structural width, ft 
maximum cargo weight, lb 
flight design gross weight, lb (typically 50-60% of internal fuel for 
military aircraft) 
weight of engine and contents, lb (per nacelle), 
- 2.331 W---?-e Kp Ktr 
engine weight, each, lb 
weight of fuel in wing, lb (if zero, ignore this term) 
landing design gross weight, lb 
weight penalty due to pres surization, 
11. 9( VprPdelta)0.27l , where Pdelta =c abin pressure differential, psi 
(typically 8 psi) 
uninstalled avionics weight, lb (typically = 800- 1400 lb) 
wing sweep at 25% MAC 
taper ratio (wing or tail) 
'} Addition al Con sider ations in Weig hts Esti mation 
These classical statistical equations are derived from a datab ase of existng aircraft. They work well for a "nor mal" aircraft which is fairly similar to 
:he various aircraft in the database. However, the use of a novel configur1tion such as a canard pusher, or an advanced technolog y such as a 
aminar flow coating may result in a poor weights estimate when using 
;uch statistical equations : To allow for this, weights engineers commo nly 
1djust the statistical equation results using "fudge factors" (humorousl y 
:lefined as the variable constant that you multiply your answer by, to get 
he right answer) . 
Fudge factors are also required to estimate the weight of a class of aircraft 
'or which no statistical equations are available. For example, there have been 
oo few Mach 3 aircraft to develop a good statistical database. Weights for a 
lew Mach 3 desi gn can be estimated by selec ting the closest available 
!quations (proba bly the fighter/ attack equations) and determining a fudge 
actor for each type of component. 
This is done using data for an existing aircraft similar to the new one 
such as the XB-70 for a Mach 3 design) and calculating its componen t 
veights using the selected statistical equatio ns. Fudge factors are then deternined by dividing the actual componen t weights for that aircraft by the 
:alcula ted compo nent weights. Then, to estimate the compon ent weights


<!-- p.580 -->

580 Ai rcraft De sign: A Conceptu al Appr oach 
for the new desi gn, these fudge factors are multiplied by the component 
weights as calculated using the selected statistical equat ions. You can then 
if approp riate, multiply again by some technolog y adjustment fudge factor. ' 
As an example, this author was recent ly asked to estimate the weight of a 
modern all-compo site je t trainer design. The Fighter/ Attack weights 
equations were used as a starting point, but "fudged." This was done by 
using actual data from the T-38/F-5B and comp aring it to a "clean " analysis 
using these equat ions. Results for the wing were 1067 lbs {484 kg} versus the 
actual value of 1042 lbs {473 kg} . This gives a ratio fudge factor of 0.9 77. It's 
close to 1. 0, indica ting that those equations aren't so bad even for an aircraft 
of a slightly different catego ry. This ratio was then multiplied by an assumed 
composite mater ial fudge factor of 0.85, giving a final fudge factor of 0.83. 
Then the estimated geomet ry and other inputs for weight analysis was 
used to calculate a "clean" wing weight, which was multiplied by 0.83 to complete the estimat e.* The same thing was done for other weight categories, 
then careful adju stments were made for things like engine and APU weight. 
Reaso nable Fudge Factors for compo site structure, wood or steel-tu be 
fuselages, braced wings, and flying-boat hulls are provided in Table 15.4. 
These are approximations only, and are subject to heated debate. Some 
claim that a prop erly designed steel-tube fuselage can be lighter than an 
aluminum fuselage. It's proba bly true, under certain special conditions . 
Usually not. 
Som etimes fudge factors are applied based just on the weight analyst's gut 
feeling. Don't laugh. If that person is experienced at "Dash-One" weight estimation, a gut feeling adjustment may be better than all the statistics and 
Category 
Table 15 .4 Weight s Esti mation "Fudge Factors " 
• I I I 11 • I I 
Advanced composites Wing 0. 85-0.9 0 
Braced wing 
Braced biplane 
Wood fuse lage 
Steel tube fuselage 
Flying boat hull 
Carrier-based ai rcraft 
Tails 
Fuselage/ nacelle 
Landing gear 
Air ind uction system 
Wing 
Wing 
Fuse lage 
Fuselage 
Fuse lage 
Fuselage and landing gear 
0. 83-0.8 8 
0.90 -0.95 
0.9 5-1 .0 
0. 85-0 .90 
0.8 2 
0.6 
l. 60 
l .80 
l .25 
l. 2-1 .3 
I 
*Yes, I get paid for doing stuff like this! Like the old car mechanic joke, it isn't the doing, it's 
the knowing.


<!-- p.581 -->

CHAPTER 15 Weig hts 581 
-nalytical estimation in the world. If you see the weights engineer hol ding 
1ands out, spreading them apart to measure length then bouncing them 
JP and down, palms up, as if weighing something invisible, you should 
1uietly tiptoe away. 
Several of the equations above use the number of flight crew personnel as 
1 term. For some aircraft that number is zero, causing statistical nightm ares. 
fhis author has found that assuming "half a man" in these equations gives 
·easonable numbers, at least until a better analysis method can be employed. 
)ince unmanned air vehicles (UA V) differ greatly, a top-le vel statistical 
-quation for all UA Vs is unlik ely. 
Ballast is another issue. No airplane in its as- designed configuration 
.hould have or need any ballast weights to correct the center of gravity, yet 
ome do. The hot little F-10 4F needed over 80 lbs of it, and the original 
:_ 15 A required hundreds of pounds of ballast. Why would this happen, 
vhen balla st is nothing but "dead" weight? 
Unfortunately, it is impossi ble to perfectly estimate the weight of every 
iart of the aircraft during conce ptual and prelimin ary design. When the air:raft goes through detail design, the actual weights are known for the first 
ime and often they are different-us ually higher-than previousl y estimated. 
'his almost always moves the center of gravity away from the engine. The 
ngine weight is pretty well known, so it is the rest of the aircraft that gets 
1eavier. If the engine is in front of the e.g., the added weight is usually 
·ehind it, and vice versa. Also, the e.g. is usua lly closer to the engine in the 
Tst place, making this effect even more pronounced. 
It may be found, late in detail design or even in protot ype weight and 
alance testing, that the e.g. is in the wrong place. By then it is way too 
1te to fix it by moving the wing. We easily move the wing in Conce ptual 
lesign, and carefully do in Prelimi nary Desi gn, but not after that. So, we 
dd ballast weight to fix t-e e.g., and include it under the Structures Group 
n the weight statement. Ballast may also be added to an existing aircraft if 
1ajor equipment is altered or the design is changed (different engine, 
tretched fusela ge, added winglets, etc.). 
Ballast is usually made from lead plates or bars. To minimize the volume 
>st to ballast, denser metals such as tungsten or even depleted uranium can 
e used. Depleted uranium is not signific antly radioact ive, but it is toxic so 
rash sites are of concern. 
Ballast that is always included whenever the aircraft flies poses a great 
ifety risk if somebod y ever remo ves it to make the airplane lighter, or 
mply forgets to replace it after a maintenance actio n. To avoid this, 
allast that is physically removable should be painted red and labelled "per1anent ballast-do not remove.'' 
Tempo rary or removab le ballast is a really bad idea, but sometimes 
eeded for an aircra ft where the loading conditions can widely vary. An 
-ample would be a pusher propel ler design where the people sit far in 
ont of the wing. When a small pilot is flying solo, tempo rary ballast may


<!-- p.582 -->

582 Ai rc raf t Desi gn: A Conceptual Appr oa ch 
be needed. It can consist of sand bags, lead bars or shot bags, or even a water 
tank. Extreme measures should be devised to ensure that the pilot never 
forgets to check the weight and balance before flight. 
Note that the mass balances used to avoid control surface flutter are also 
made from lead, tungsten, or depleted uranium. These are sometim es called 
"ballast" and included in the ballast item on the Group Weight Statement, 
rather than in the weight of the wing or tail. Either acco unting is acceptable, 
but statistical confusion can result. 
One final cons ideration in aircraft weight estimation is the weight growth 
that most aircraft experience during development and into the first few years 
of production. This growth in empty weight is due to several factors, such as 
increased avionics capabilities, struct ural fixes (such as replacing an aluminum fitting with steel to prevent cracking) , and additional weapons pylons. 
"Req uirements creep" is also a factor in many cases; customers want the airplane to do more than what they originally asked for. 
a) 20% 
..s= 
Weight growth during des !gn 
e 
O'l 
J: 10% O'l 
·a; 
3: 
};. 
c.. 
E 
LU 
F-5 
0% 
Sta rt of detail design Fir st flight 
b) 20% -+ 
After first flight 
..s= 
e 
O'l 
.... 
..s= 
10% O'l 
·a; 
3: 
:>, 
c. 
E 
LU 
0% 
Fir st flight 2 3 4 5 years 
Fig. 15 .4 Aircraft weight growth.


<!-- p.583 -->

CH I tK I 0 we1gm s :>83 
Figure 15. 4 shows the empty-weight growth of a number of aircra ft, both 
during the design phase and later after first flight. In the past, a weight growth 
of 5% in the first year after the start of flight test was considered common. 
Today's better design techniques and analytical methods have reduced that 
to less than 2% in the first year for normal designs. Groundbreaking 
designs such as a vertical takeoff and supersonic stealth fighter can still 
suffer large increase both during design and well into flight test. An allowance 
for weight growth during detail design and flight test should always be 
included in the conc eptual desi gn weight estimate, as described above. 
What We've Lear ned 
We've learned how to analyze the weight and balance of our design using 
top-level ratios, detailed statistical models, and structura l analysis. We've 
also learned that excess weight kills many otherwise good ideas. 
X-3 1 Enha nced Figh ter Ma neu verabil ity Aircraft in flight (NASA photo) .


<!-- p.584 -->

584 Ai rcraf t Design : A Con ceptu al Appr oa ch
