# Raymer Ch.22 - Extremes of Flight

*Converted from `Daniel P. Raymer - Aircraft Design_ A Conceptual Approach (2018, American Institute of Aeronautics and Astronautics Inc.) - libgen.li.pdf` by `tools/pdf_to_md.py`. Page markers are printed page numbers.*


<!-- p.807 -->

Extremes of Flight 
• Extre mes of ftight include lau nch veh icles , hyper sonic fti ers, and air ships of 
va rious types . 
• Des ign options and chan ges from " no rma l " air craf t de sign pra ctic e ar e 
presented here. 
• For space craf t and laun ch ve hic les, Del ta-V is equ ival ent to the ra nge req ui rement , 
and the Rocket equation is lik e Breguet's ra nge equat ion . 
• Air ship s ar e ana lyzed via Arch im edes' Princi ple , with help from Cha rles' and Boyl e's 
Laws . 
In trod ucti on 
T he previous chaP.ters cover the design of aircraft in the "normal" 
speed range, from low subsonic to about Mach 2.2. This chapter discusses excursions in both directions-much faster and much slower. 
Weirdly enough, there are some similarities in these extremes. For 
example, rocket launch vehicles and airships are both dominated in their 
design by the volume of their "prop ellant s," if you consid er an airship's 
lifting gas as propelling it upward. In fact, hydrogen is the ideal airship 
lifting gas and also the ideal rocket propel lant, if practical consi derations 
are ignored. Rockets and airships are both far more sensitive to vehicle 
empty weight than a normal aircraft. For different reasons, neither can use 
the Breguet range equation that we rely upon so much for other aircraft. 
Another simila rity is that these extremes of flight are both a lot of fun 
to design. 
805


<!-- p.808 -->

806 Air craf t Design : A Concep tual Approach 
Rocket s, Lau nch Vehi cle s, and Spac ecraft 
#f IJI Propulsion and lsp 
These days the line between aircraft and spacec raft design has gotten 
blurry. Many aircraft designers including this autho r are spending more 
and more time in the design of rockets, launch vehicles, and spacecr aft.* 
The design of these vehicles is most ly similar to aircraft design as descr ibed 
throughout this book. There is sizing, preliminary layout, design analysis, and 
performance calculat ions, and design iteration is an impor tant part of the 
process. There are also impor tant differences, which are discussed below. 
The histor y of rockets and space craft is well known and will not be 
repeated here. Suffice it to say that after countless ages of staring up at the 
skies and wishing to understand the mysterious moon and the fixed and 
moving lights seen overhead, mankind has finally developed the science to 
comprehend and the technolog y to reach at least some of them. We can 
even make our own and can put them up there for all to see. 
The design of launch vehicles and spac ecraft is largely driven by propulsion. The accele ration requireme nts to do any useful mission in space are so 
prodigious that the prop ellant is around 9/10 of the vehicle mass. This compares to a typical aircraft where it is one-t hird of the mass. The current record 
for aircraft fuel fraction is the Global Flyer, where propellant is 83% of total 
mass-a rather poor rocket value. 
Although we would like to grip the fabric of space-t ime and pull ourselves up to the stars, most forms of spacecr aft propulsion yet devised by 
mankind involve some sophisticated version of throwing rocks out of the 
back of a canoe. The more rocks you have and the faster you can throw 
them, the faster and farther your canoe can go. 
Such rock- throwing propulsion is called a reaction drive, and there are 
two categories. In most rocket propulsion the energy that accel erates the 
prope llant is actually contained in that propellant as chemical energy-the 
fuel throws itself out the back in a chemical reacti on that produces heat 
and pressure in the combustion chamber. 
In the other categor y of reaction drive, the ener gy sour ce is separate 
from the "rocks," typically being stored as electric ity, nuclear power, or 
solar-e nergy collec tion. In this case, the best rock to throw is hydrogen 
because it has the lowest atomic number. For chemical rockets we must 
compromise between low atomic number of the exhaust and the reaction 
energy content of the prope llants. 
Note some confusing terminolog y: "Ro cket" is used as a generic name for 
a reaction drive engine, but is also used to describe the entire vehicle. "Motor" 
*T o some, the term "spacecr aft" refers to satellites and planetary probes, not to the complete 
powered vehicle. Here it is used as the space equivalent of "aircraft, " and satellites and such are considered the spacecraft's payload.


<!-- p.809 -->

CHAPTE R 22 Extre mes of Fligh t 807 
generally refers to a solid rocket engine, whereas "en gine" refers to a liquid 
rocket engine. 
Whatever the source of the energy, the thrust of a reaction drive is found 
from Newton's Third and Second Laws. The Third Law says that for every 
reaction there is an equal and opposi te reactio n, so that if the rocket 
pushes the propel lant out the back, the propellant pushes the rocket 
forward. The Second Law allows us to calculate this force as being equal to 
the change in momen tum per change in time. Its full form includes both discrete masses (rocks) and ejected fluid mass flows, as follows (Vexhaust is relative to the vehicle) (Fig. 22. 1). 
Newton's Second Law: 
F = ma + rh Vexhaust (22. 1) 
The total impu lse applied to the rocket is this force times its duration, 
found by integra tion when assuming a fluid mass flow instead of rocks 
thrown out the back. 
There is also a pressure thrust contribution equal to the nozzle exit area 
times the difference between the exhaust pressure and the ambient atmospheric pressure. It is for this reason that rockets have different thrust at 
different altitu des. Oddly eno ugh, the maxi mum thrust is obtained when 
this pressure thrust is zero. This allows all of the energy available to be 
used to accelera te the exhaust. We usually set the nozzle exit area to minimize this pressure thrust averaged over the flight path, so it is ignored in 
the following analysis. 
With pressure thrust negated, integrating Eq. 20.l gives: 
Total impulse: 
t 
ft- J Fdt = 
0 
t 
J (rhVexhaust)dt 
0 
(22 .2 ) 
For the following performance calculations, we will need to know the 
impulse obtained per unit mass of prop ellant consumed, that is, the spec ific 
c:::: -) 
Fig. 22.1 Di screte and continu ous prop ellan ts pushing a rocket .


<!-- p.810 -->

808 Aircr aft Des ign : A Conce ptu al Appr oach 
impulse. However, to make the units come out nicely, we normally use unit 
prope llant weight instead of mass, as follows. 
Specific impulse: 
Total impulse J- (m Vexhaust)dt Vexhaust 1sp = Fuel burned = go I mdt = go (22·3 ) 
The last equality assumes that the exhaust veloc ity is const ant for the 
duration of the burn, which is reasonable in most cases. Note that go is the 
Earth-standard acceler ation constant but is used even if the space craft is 
far from Earth because it is being used to convert a mass to an equivalent 
weight force. Ad justing this term for altitude effects is a common student 
error. 
With this term proper ly employed, fsp becomes the ratio of the thrust 
force obtained per unit propellant mass flow in weight force equivalen t. 
Thus, the force terms cancel, and the fsp units become seconds, whether 
British or metric units are employed. If we chose to use mass flow rather 
than weight flow of prop ellant, the units of fsp would be the same as velocity, 
and, in fact, fsp would be identica l to the effective exhaust velocity. This 
more-c orrect definition is som etimes used (espe cially in Europe) but notice 
that the numer ical value changes in different systems of units. 
Specific impulse fsp is obviously related to the equivalent aircraft parameter, speci fic fuel consumption (SFC ). SFC is defined "upside down." In 
British units SFC is given in pounds weight of fuel per hour per pound of 
thrust force generated. We cancel the pounds, lea ving units of per hour. In 
British units, SFC and fsp are therefore the inverse of each other, except 
that one is in hours and the other is in seconds. Thus, fsp is 3,600 divided 
by SFC and vice versa. Also note that for SFC, "big is bad, " whereas for fsp 
"big is good." 
In metric units, the SFC is more proper ly defined as propellant mass flow 
per hour divided by thrust force produced, so the conversion of fsp to SFC 
requires use of the gravitational acce leration const ant (see Append ix A). 
One might ask, why don't rocket scien tists use the same specific fuel 
consumption definition that aircraft designers have always used? Perhaps 
the answer is historical. When Tsiolk ovsky derived the Rocket equation in 
1895)1 48] the aircraft term SFC had not yet been invented, neither had 
aircraft. Anot her possib ility was embarrassment. A bad jet engine has an 
SFC of 2. A good chemical rocket has an SFC of 10. The comparison is 
less obvious if we say instead that fsp = 360 s. This is not their fault. A 
rocket must carry its oxygen along as a propellant, whereas a jet gets it for 
free. (Actu ally not so free: an airbrea thing turboj et engine is 5-10 times 
heavier for the thrust it produces, mostly because of the difficulty in capturing and using that "free" oxygen) . 
The efficiency of a rocket engine changes with the exhaust velocity. This 
is similar to what was found in Chapter 13 for aircraft propulsion, with one


<!-- p.811 -->

CHAP TER 22 Extre mes of Fligh t 809 
important difference: the aircraft is accel erating an oncom ing fluid, namel y, 
air-the fuel being a negligible portion of the acce lerated mass flow. The 
rocket must accel erate fluid that it carries along. 
Rocket propulsion efficiency is forma lly defined as the ratio between the 
power inherent in the vehicle itself (thrust times veloc ity) divided by the total 
power inherent in the vehicle plus the residual kinetic energy of the exhaust, 
or as follows. 
Propulsi ve efficie ncy: 
where 
FV 2 V / Vexhaust 
T/p = 1 = 2 FV + 2 (m)( Vexhaust - V)2 l + ( V /Vexhaust ) 
F = thrust force 
V = vehicle velocity 
Vexhaust = effective exhaust veloc ity relative to vehicle 
Vexhaust = thrust/m ass flow = go fsp 
(22 .4) 
This is maximized when Vexhaust = V, yielding perfect efficiency ( = 1. 0) . 
This is the same analytical result as was obtained for aircraft but has a different impact. For aircraft, ideal efficie ncy produces zero thrust because this 
implies that there is no acceleration imparted to the oncom ing flow. For 
rockets, this is not the case because thrust is produced by accel erating the 
exhaust from its relative station ary cond ition inside the vehicle to its 
exhaust velocity. * 
Another interesting obser vation is that Vexhaust = V implies that the 
exhaust ends up with no veloc ity relative to an outside observer. If the 
exhaust really were rock -, it would appear that the spacecraft flew by and 
"laid" statio nary rocks along its path. This is, in fact, optimal because residual 
velocity in the exhaust takes energy to produce but does not help to push 
the rocket. 
Yet another obser vation is the following: although Vexhaust = V provides 
maximum efficiency in terms of energy usage, it does not provide maximum 
thrust per propel lant expended. If energy is readily available, by all means use 
the highest exhaust velocity technic ally possible. When the energy source is 
separate from the exhausted propel lant, such as in a nuclear-t hermal rocket, 
a trade stud y should be cond ucted to see if the mission performance is maximized with a more powerful but heavier energy sou rce, or with additional 
propellant mass. 
Typical values of fsp are provided in Table 22. 1. 
*N ote that "real" rocket scientists use C for Vexhaust• whereas for aircraft C is a shortened form of 
SFC and appears in the Breguet equation, among others.


<!-- p.812 -->

81 0 Airc raf t Design: A Conceptual Approach 
Table 22. 1 Typical Specific Imp ul se for Rockets 
Rocket Type Typical fsp• S 
Chem ica l, liquid prop ellant 
LOX-Hyd rogen 360-450 
LOX-Me tha ne 270 -350 
LOX-RP (kerosene) 250 -330 
Chemic al, solid prope llan t 18 0-2 20 
Nuclear ther mal 800-2000 
Nuclear pulse (Orion) 4000 + 
Ele ctrother mal 400-2000 
Ion 4000-25 ,000 
Solar heati ng 400-700 
Although lsp is very impor tant to rocket performance, there is another 
aspect of propulsion that must be considered. Different prop ellants have 
different densities, and this affects the size and empty weight of the 
vehicle. Hydrogen, which is excellent in terms of /5p, has a very low 
densit y, so its tanks must be large, leading to a larger, heavier airframe. 
This is also a serious problem whenever hydrogen is studied as an aircraft 
prop ellant (see Fig. 22.7) . Solid prope llants have worse lsp values than hydrogen but are very dense, leading to smaller stage s. 
Densi ty impulse is a useful parameter that designers sometimes use to 
make comparisons between prop ellant options. Densi ty impulse is calculated 
as the product of propellant specific gravity (dens ity) and lsp· A larger value 
implies a better vehicle design will result. However, dens ity impulse is only a 
guide, and a detailed design trade study is still required to determine the best 
prop ellant for a given mission. 
Spacecraft propulsion not involving the "throwing of rocks" is called a 
reactionless drive. There are few viable candida tes, and practical appli cation 
seems beyond current technolog y-but that might change. 
Solar sails use photonic pressure to create free thrust, but require sail 
areas measured in units more typical for real estate than for flight vehicles. 
The sail weight must be impossi bly light, and the problems of unfurling 
and controlling the sail have yet to be resolved. Resea rch is continuing, 
and solar sails might prove applicable for certain missions in the near future. 
Other candi date reactionless drives include tethers, space elevators, 
electrod ynamic, and more. A number of the exotic pos sibilities for future 
spacecr aft propulsion were described by science-fiction author and noted 
research scie ntist Dr. Robert L. Forward in the aptly titled book Indistinguishable from MagicJ149l 
There are two practical ways of changing the veloc ity of a space craft 
without propulsion: gravity assist and aerod ynamic assist. Gravity assist


<!-- p.813 -->

CHAP TER 22 Extre mes of Fligh t 81 1 
involves a flyby path near a planet and is similar to a bicyclist grabbing a 
passing car. If proper ly done, it will change the vehicle's speed and direction, 
while minut ely doing the reverse to the planet! 
Aeroassist involves the use of aerod ynamic drag for deceleration at a destination planet posses sing an atmosphere. The returning Apollo capsules 
used aeroassist to dissipa te the velocity acquired by "falling" from the orbit 
of the moon, thus saving a lot of rocket prope llant. 
#/Ill Delta-V 
For the selected propulsion system, we now need to determine the propellant required to obtain the desired mission ca pabilities. In aircraft 
design, we establish a mission range requirement at the start of a proj ect 
and then use equations such as those of Breguet to determine the required 
fuel fraction, which becomes a target for the design effort. 
We do something similar in the design of rockets. Rather than a range 
requirement, we determine an equivalent parameter called Delta-V. Rather 
than the Breguet equation, we use Tsio lkovsky's Rocket equat ion. These 
are described next. 
Delta-V is exactly what the name implies -a change in velocity. It applies 
regardless of propulsion type and is calculated from the overall mission 
objective. For example, to fly from Earth orbit to Mars orbit takes a certain 
total change in velocity, roughly 38,0 00 fps {1 2,000 mps}. 
This seems odd-sur ely, the important parameter is accelerat ion. After 
all, that is what the rocket engine provides. This is true, but the purpose of 
the acceleration is to change the veloci ty. The time of the rocket burn is normally so short compared to the transit time that it can be ignored for initial 
design purposes. 
The Delta-V obtained by a rocket burn is used to place us in a different 
orbit- one that takes us from where we are to where we wish to go. So, 
the calculation of the required Delta-V is actually an exercise in orbital 
mechanic s. 
When an object is in a circular orbit around some body, its horizo ntal 
speed is great enough that the centrifugal force equals the weight. Actually, 
centrifugal force is a fraudulent term-t here is no such thing. What is 
really happening is that the object is falling, but moving forward fast 
enough that the ground is falling away at the same rate. But, centrifugal 
force is a convenient engineering fiction. It is calculated as mass times velocity squared, divided by the distance R from the center of the body being 
orbite d. Setting this equal to the weight gives the following: 
Centrifugal force = weight: 
mv2 __ s = mg R (22.5)


<!-- p.814 -->

812 Ai rcraf t Desi gn: A Conceptual Appr oach 
From Newton's Law of Gravitatio n, we know that the acceleration due to 
gravity reduces as distance increases, giving the following: 
Gravitational acceler ation: 
( Ro ) 2 
g =go Ro+ h 
We can subs titute this into Eq. (22.5) and obtain the following: 
Required orbi tal veloc ity: 
- Vs= RoyR.-+ h 
where 
h = height above ground 
go = accel eration at planet's surface 
= 32.1 727 f/s2 {9.80 62 m/s 2} (Ear th) 
Ro = planet's radius 
= 20,925,6 46 ft {6,378, 137 m} (Ear th) 
(Data for other planets are in Table 22.2.) 
(22.6) 
(22.7) 
This equation tells us the veloc ity needed for orbit at a particular height. If 
you can get to that height, once there the Delta-V to enter orbit is just this 
required velocity minus your current veloc ity. 
If trying to reach a due- East Earth orbit from the ground, the rotational 
veloc ity of your starting point on the ground will help so that your Delta-V 
requirement can be reduced. This assistance equals the Earth's rotational 
speed at the equator [(1,5 42 fps) or {470 mps }] adjusted for latitude (multiply 
by the cosine of the latit ude). If launching into a polar orbit, the Earth's 
rotation does not help, and if you try to launch towards the West, you 
need additional Delta-V. Also, note that the closer the launch site is to the 
equator, the easier it is to reach orbit. It is for this reason that the Soviet 
Union chose Kazakhstan rather than a site in Russia for its launch comp lex. 
You must also fight both gravity and aerod ynamic drag on the way up. 
These add roughly 6,000 fps {l, 830 mps} to the Delt a-V required to reach 
Earth orbit. The energy height methods of Chapter 17 can be used to 
approxim ate the velocity equivalent of the altitude to be gained. For a 
better solution, time -stepping simulation programs are common ly used. 
To travel from planet to planet around the sun, or from Earth orbit to the 
moon, we first need to get out of the gravity well of the planet we are near. 
Escape veloc ity is the speed at which, for the current altitude, the kinetic 
energy of the vehicle equals the work needed to overcome gravity all of the 
way out to infinity. This equals the orbital veloc ity times the square root of 
two. From this we calculate a "planet exit" Delta-V. If we are already in 
orbit, we can credit the orbital veloc ity we alread y possess.


<!-- p.815 -->

l-Hul·-lilM 
Sun 
Moon 0.238 
Mer cu ry 35.9 6 
Venus 67 .20 
Ear th I 92 .90 
Mar s 14 1. 6 
Jupi ter 483 .3 
Saturn 886 .2 
Uranus 17 83 
Neptune 2794 
Pl uto 3670 
Table 22.2 Data for Heav enly Bod ies (after ll 50] ) 
Perio d of 
Revolu tion About Mean 
Sun Diame ter, km 
l ,393 ,000 
27 .3 days 3475 
87 .97 day s 4990 
224 .7 day s 12 ,2 00 
365.256 day s 12 ,7 55 
686 .98 day s 6760 
11. 86 yr 14 ,000 
29 .46 yr 12 5,000 
84 .0 yr 47 ,600 
16 4.8 yr 44,70 0 
248 .4 yr 14 ,0 00 
Specific Acceler ation of 
Rela tive Mass Gravity Grav ity af Escape Velocity 
(Eart h = 1. 0) (1 = water) Sur face, m/s 2 at Surface, m/s 
332 ,000 1. 41 273 .4 61 6,000 
0.01 2 3.34 1 .58 2380 
0. 053 5.30 3.60 4200 
0.81 5 4.95 8.50 10 ,300 
1 .00 5.52 9.8 06 11 , 17 9 
0. 10 7 3.95 3. 749 5000 
31 8.4 I 
I 
1 .33 26 .0 61 ,000 
95 .2 0.69 13 .7 36,600 
14 .5 I 1 .56 I 9.3 9 21 ,900 
17 .2 2.27 14 .9 25 ,000 
0.90 4.00 I 7.62 10 ,000 
(") 
::J: 
l> 
..... 
m 
::0 
N 
N 
m 
x <D 
3 
<D 
CJ> 
g_ 
"Tl 
c6' 
:; o:i ... 
w


<!-- p.816 -->

814 Air craf t Des ign: A Conceptual Approach 
Next, we need to find the Delta-V to travel from the orbital radiu s we are 
in to the orbital radius of the target, around the sun (or Earth, for travel from 
Earth to moon). There are several strategies we could follow, inclu ding just 
pointing where we want to go and firing up our science -fictio n "warp 
drive" engines. Given the limited capabilities of actual rocket engines, we 
prefer to follow a minimum-fuel trajector y called a Hohmann transfer 
orbit. This follows an elliptical orbit that is exactly tangent to the starting 
and ending orbital radii. Hohmann transfer orbit analysis can be found in 
Bate et aI. f151 l among others. Typical results from Earth orbit are summarized 
in Table 22.3. 
Although you can always do a Hohmann transfer from one planet's 
orbital radius to anot her, it is not always the case that the planet is there 
when you arrive ! Minimum fuel "windows" are times when the starting 
and ending planets are in the correct locations such that, after a Hohmann 
transfer flight, the target planet is there. If you cannot launch during such 
a window , a less optimal trajector y will be required, and more prope llant 
will be needed. 
Once at the target planet, we find that our velocity is not exactly the 
same as the orbital velo city at that radius, so we make a second Delta-V 
burn to "circularize" the orbit. If we are going to land, though, we can 
take advantage of the gravity well of the target planet to pull us in. In fact, 
we will have to somehow counter the extra velocity we pick up in falling 
from "infinit y" to that planet's surface, which equals the escape veloci ty 
ju st discussed. If the planet has an atmosphere, aeroassi sted braking can 
be used. 
Calculation of Delta- V to perform the required mission is, of course, 
more comp licated than this brief overview implies. This is espec ially the 
case where maneu vers like gravity assist are employed. To really get the 
correct answer, even Einstein's relativity must be considered. 
Table 22.3 Hohmann Transfer Orbit Resu lts 
Minimum Launching 
Plane t Velocity, mps 
Mercur y 13 .41 1 
Ven us l l, 582 
Mar s 11 ,582 
Jup iter 14 ,02 1 
Satur n 14 ,935 
Uranus 15 ,545 
Neptune 15 ,850 
Pluto 16 ,15 4 
.. 
11 0 day s 
15 0 days 
260 da ys 
2. 7 yea rs 
6 years 
16 year s 
31 yea rs 
46 yea rs


<!-- p.817 -->

CHAPTE R 22 Extre mes of Fligh t 81 5 
11111 Rocket Eq uation 
Once the design mission has been analyzed to determine the total 
Delta-Y required, the amount of propellant that must be carried by the 
vehicle to obtain that Delta-V can be found. For this, we use the famous 
Rocket equation . 
The Rocket equation is very much like the Breguet equation in that it 
relates prope llant consumption to the spaceflight equivalent of range, 
namely, Delta- V. The Rocket equation can be derived by starting with the 
top illustrati on in Fig. 22. 1. This shows a rocket pushing out a discrete 
"blob" of prope llant, the "rock" referred to earlier. By cons ervation of 
momentu m, we know that the momentum before the blob is pushed out 
has to equal the mome ntum afterwards, or 
Momen tum: 
Before: 
(mfinal + mpropellant ) Vo 
After: 
mfinal (Vo + - V) + mpropellant (Vo - Vexhaust ) 
where 
Vexhaust = relative to the vehicle 
- V = increase in veloc ity 
Equating and solving for - V gives 
- V = mpropellant Vexhaust mfinal 
(22.8) 
(22 .9 ) 
(22. 10) 
So the resulting change in vehicle veloc ity is just the relative exhaust veloc ity, 
ratioed by the propel lant mass vs final mass. 
Replacing the discre te prop ellant blob by a continuous mass flow and 
integrating from an ini tial mass to a final mass gives one form of the 
Rocket equation. Subst ituting from Eq. (22.3) gives a more useful form. 
Rocket equation usin g Vexhaust: 
(22. 11) 
Rocket equation using /5p: 
Ii V - gol,pt• (:;) (22. 12)


<!-- p.818 -->

816 Ai rcraf t Des ign : A Concep tual Appro ach 
Rocket equatio n-mass ratio: 
ilV ilV 
mi/ mj = ef'Ol>p = eVexhou>t (22. 13) 
An even more useful form for designers is found by solving for the 
required mass ratio, shown in Eq. (22. 13). This is in the form of a missionsegment weight fracti on as derived in Chapter 3, allowing the calcul ation 
of the propellant mass required to obtain the required Delta-V. 
One more consi deration- staging. The idea of stacking rockets on top of 
each other to impro ve performance was suggested in 1650 and theoretically 
analyzed by Tsiolk ovsky, who developed a modified version of the Rocket 
equation to analyze staging, shown in the following. 
The basic idea of staging is simple- improve performance by cutting 
away parts of the launch vehicle when they are no longer needed. Why 
carry big empty tanks to orbit? Throw them away as soon as they are 
empty. Why carry the big engines needed to lift off the ground when the 
vehicle will be much lighter after most of its prope llant is gone? Throw 
them away too. 
There are a number of staging geo metries that can be consid ered, shown 
in Fig. 22.2. Most staged rockets, including the one concei ved in 16 50, are 
stacked vertic ally requiring a sequen tial burn. The top- stage engines do 
not ope rate at liftoff and must be started immedia tely when the lower 
stage is dropped off. This seems like a bad idea, not using all engines on 
liftoff. Actually, engines that are designed to operate only at high altitudes 
will have higher thrust and fsp than engines that can also run well at sea 
level, so that it might be better if the upper- stage engines are not operating 
p 
Most Soyuz Atlas 
Sequential Par allel burn Para llel burn 
bur n stra p-on boosters engines 
Fig. 22.2 Stagin g geometries. 
-Sh uttle 
Dropped 
ta nk


<!-- p.819 -->

CH APTE R 22 Extre mes of Fligh t 81 7 
at liftoff. Also, vertical stacking will have less drag and proba bly less weight 
than the other approaches. 
The next two geometries allow parallel burn- all engines are operating at 
liftoff. This maximizes initial thrust and hence increases allowable GLOW 
(Gross Lift-Off Weight). The extra strap -on boo sters or engines are normally 
used just for initial portions of the flight and are dropped at a fairly low altitude. Parallel burn is normally combined with a third stage designed for 
high-altitude operat ion. 
The final geometry is used by the Space Shuttle. Prop ellant is carried in a 
fairly cheap external tank much like the throwaway drop tanks long used in 
military aircraft. The expensive stuff {main engines, avionics, etc.) is located 
in the recovered portion of the shuttle. The shuttle also incorpor ates strap -on 
parallel burn boos ters to increase GLOW. 
The Rocket equation is modified for a staged design just by adding up the 
Delta-V contribution of each stage [Eq. {22.14 )). The second equation details 
the individual stages' Delta-Vs. In the third equation, these are combined by 
assuming that all stages have the same fsp· This can be approximately true if 
the same engine type and prop ellants are used, but the altitude effect on 
engine performance must be con sidered. In the last equation, it is further 
assumed that the empty weight of all but the last stage can be ignored. 
This is dubious, but does illus trate how the mass ratio appea rs much 
better for a staged rocket than for a single stage. 
Staged Rocket equat ion: 
n 
- ij" = L - v = -Vi + -Vi + - V3 + ... 
1 
- ij" = golsptn [ mn l 
m f (last stage) 
(22. 14) 
(22.15 ) 
(22. 16) 
{22. 17) 
Another launch vehicle issue is receiving a lot of attention these days. 
Most existing launch vehicles are thrown away during each flight. The 
launch customer must buy a new flight vehicle each time- imagine doing 
that with airli ners! Even the Space Shuttle, developed for reusab ility, 
throws away its huge expendable prop ellant tank. It also drops its two 
solid boos ters, which are recovered but require complete disassem bly and 
remanufacture before they can be used again. 
Launch vehicle reusa bility should reduce operational costs, but adds to 
the system development cost and weight. The boo ster must survive the


<!-- p.820 -->

818 Ai rc raft Desig n: A Concept ual Approach 
heating and loads of reent ry. It must be capable of landing in some fashion, 
preferably at a preselected land location rather than parachuted into the 
ocean. This might require some sor t of "flyback" capability using turbojets, 
rockets, aerial towing, or efficient gliding. Aerod ynamic flight stability 
might be difficult to obtain because of the aft center of gravity typical for 
an empty booster stage. 
If reusab ility is desired, the boost er must be capable of operation for a 
greater flight duration, well past main engine cutoff. This increases subsystems requiremen ts driving up weight and cost. Finally, the boos ter must be 
sized to its mission including the empty weight impact of these addit ional 
needs. Launch vehicle boosters have extremely high sizing growth factors 
so the weight goes up even more. 
All of this adds to the weight and cost of a reusable system. The question 
is: are those costs so large that it remains cheaper to throw the whole thing 
away after each flight? 
The jury is still out, but the pot ential payoff is attractive. A lot of research 
and design effort is going into reusable launch systems such as the winged 
reentry boo ster depicted in Fig. 22.3, or the rocket-landed first stage boost ers 
rece ntly flight proven by the Space- X Falcon Heavy launch vehicle. 
Another approach is to use an aircraft "zero -th" stage. The Orbital 
Sciences Pegasus launch vehicle is carried aloft by a converted L-1011. 
Fig. 22.3 Reusa ble first-sta ge lau nch vehicle -Raymer 20 14 . [1 52l


<!-- p.821 -->

CHAP TER 22 Extre mes of Fligh t 81 9 
Scaled Composites' Ansari X-prize-w inning SpaceShipOne and passengercarrying SpaceS hipTwo are launched from the purpose -built White 
Knights One and Two. 
The enormous, soon-t o-fly Stratolaunch aircraft follows the same twin 
fuselage, payload- at-mid-w ing layout as the White Knight vehicl es. Also 
designed by Scaled Compos ites, it uses six engines from the Boe ing 747 
and has the largest wingspan ever built. Microsoft co- founder Paul Allen, 
who financed the constructi on, claims it is designed to carry three upper 
stage rockets at a time and says that eventually it may carry a fully- reusable, 
Space Shuttle-like launch vehicle known interna lly as "Black Ice". f174l 
The Pioneer Rocketplane was to use a manned first stage with a twist: it 
would take off using turboj et engines and then meet with a tanker aircraft to 
take on the heavy LOX needed to boost itself into space. f 153] While never 
built, it appears to have no serious technical problems except for the 
obvious-t he aerial transfer of freezing cold, highly flammable liquid 
oxygen has yet to be demonst rated. 
This brief introduction has barel y touched on the subj ect of the preliminary design of rockets, launch vehicles, and spacecraft. Other sources 
should be consulted for detailed descriptions of orbital mechanics, launch 
analysis, and rocket thrust calculations as previewed here, plus the 
numerous subjects untouched including structura l design, weight estimation, 
subsystems, avionics, communications, thermal management, guidance, 
control, payload, and others. 
EJ Hyper sonic Vehi cle s 
#/JI# Hype rsoni c Fl ight 
After a checkered histor y of promises and problems, hypersonic flight is 
undergoing a resurge nce. "Hypersonic" is roughly described as Mach 5 or 
higher (the Mach 3 SR-71 seems station ary by compa riso n), but is actually 
defined by the presence of the following flow characteristics not found at 
lower speeds: 
1. The shock angles are so steep that they lie close to the surface forming 
a "shock layer" and causing a strong interaction between the boun dary 
layer and the shocks. Because of this interact ion, the bou ndary layer is 
one to two orders of magnitude thicker than at lower speeds and 
creates an apparent body around the actual body. This causes the nose 
to appear blunt to the freestream flow no matter how pointed its actual 
shape might be. This shock-boun dary-layer interaction also violates a 
common assumption in CFD codes, so specialized hypersonic codes 
must be used. 
2. Extreme flow heating causes molecular excitati on and even disso ciation of 
the air into ions, so the air is not really air anymore! Again, regular


<!-- p.822 -->

820 Ai rc raft De sign: A Concep tual Approach 
aerod ynamics codes must be modified to account for this, and even the 
full NS equations do not include this possi bility. 
3. If the hypersonic flight is at high altitude, the low den sity /high spee d 
causes the usual "no- slip" assumption to be untrue. The molecules right at 
the surface have a tangential veloc ity, unlike the case in slower flows where 
they are "stuck" to the surface. Regular CFD codes assume "no-s lip. " 
4. Forces and momen ts change in a significan tly nonlinear fashion with 
respect to angle of attack. 
At hypersonic speeds, a first approximation of the pressures exerted upon 
the vehicle can be found from the Newtonian impact theor y. Newton thought 
that fluid flow could be modeled as a stream of pellets hitting the surface, 
which proved to be very wrong at subso nic speeds but reaso nably correct 
at Mach 5 or higher. The analysis assumes that air particles hitting the 
vehicle are turned parallel to the surface, and that the perpendicular component of the air's momen tum is exerted as press ure on the vehicle. 
From the Newtonian assumption, the center of lift of a hypersonic vehicle 
can be roug hly approximated as the geomet ric centroid of the total planform 
area (including fuselag e). The design must be configured so that this centroid 
is relatively close to the e.g. for hypersonic flight. The normal design require ments as to stabil ity must be accommoda ted in subson ic flight, which can 
place the wing farther back than desirable for hyperson ic balance. This 
often leads to the use of a strake or double- delta arrangement. 
A key issue for hypersonic vehicle design is thermal management. Supersonic aircraft like the SR-71 use their fuel supply as a heat sink, routing the 
fuel through heat exchangers to absorb the heat generated at the nose and 
leading edges, plus the excess engine heat. The black paint on the SR-71 is 
spec ifically formulated to radiate heat. Flight profiles are actually limited by 
heat-absor ption capabilities -when you cannot absorb any more heat, you 
have to slow down. 
The problems are even worse at hypersonic speeds, and thermal analysis 
must be incorpo rated from the earliest phases of design. The Space Shuttle 
experiences maximum surface temperatures of over 3000°F {1 650°C}. 
Extreme thermal loads limit the minimum radius on the nose of a hypersonic 
reentry veh icle to perhaps 1-2 ft {30 -60 cm}, and the nose behind this nose 
cap should not be sloped less than about 15 -20 deg from horizontal. Heating 
also limit s the leading- edge radius for the wing and tail to a minimum of 
roughly 1-2 in. {3-5 cm} unless very exotic materials plus active cooling 
are employed. 
Despi te the high-temper ature environm ent, the Space Shu ttle and 
various other hyperso nic designs use a conventional aluminum structure. 
This is protected by thermal tiles or blanke ts plus exotic materials such as 
carbon-ca rbon compo site or ceramics in the regions of highest heating 
(nose and leading edges) . The thickness and weight of such a "thermal protection syste m" (TPS) must be included in the earliest design stages, and TPS


<!-- p.823 -->

CHAP TER 22 Extre mes of Fligh t 82 1 
experts must select and analyze the materials and provide data to the configuration designer. As a first approxim ation, an allowance of about 1-2 in. 
{3-5 cm} on the bottom, and less than 1 in. on the top should suffice. 
Advanced TPS coverings weigh roughly 0.5- 1. 0 lb/ft 2 {2.4- 5 kg/m 2} of 
surface area, whereas the Space Shuttle tile TPS averages about 1. 6 lb/ft 2 
{7.8 kg/m 2}. To this must be added about 0.25 -1.0 lb/ft 2 for attachments, 
usually a bonding agent and a strain isolation pad. 
Altern atively, exotic materials might be employed without TPS, but 
numerous trade studies indicate that the total weight is usually heavier. 
Final selection depends upon maximum Mach number, duration of highspeed flight, and availability of fuel for co oling. 
Some hyperso nic vehicles such as the Space Shuttle and various cruise 
missi les have fairly no rmal fuselage-w ing configurations, with wing planform 
selected as a compromise between landing speed and high-speed drag. For a 
reentry vehicle, the reentry g-loading often sets a limit on wing loading. 
For efficient hypersonic cruise flight, a concept similar to the compression lift described in Chapter 8 offe_rs promise. The Hypersonic Waverider is bas ically a highly swept flying wing configured such that the shocks are 
defined and constrained by the leading edges, and the vehicle flies on top of 
the shock waves it creates. Early waverider concepts resembled swept triangular wedges with negative dihedral, but later analysis including the 
effects of viscos ity determined a revised optimal shape. The upper part of 
Fig. 22.4 shows a typical viscous-op timized Hypersonic Waverider shape, 
looking like a thumbnail in top view and a downward-po inting bow in 
cross section. This offers a hypersonic L/D substantially better than a 
simple wing-fus elage arrangement, but the integrati on of the optimal shape 
into a reasonable design, with engines, landing gear, cockpit, and payload, 
is left to the designer! The lower illustration in Fig. 22.4 shows a notional 
vehicle design done at the University of Maryland for a slightly different 
waverider geom etry. 
· 
Fig. 22.4 Hyper sonic Waveri der (NASA La ngle y /Un iversity of Mar yland).


<!-- p.824 -->

822 Air craf t Design : A Concep tual Approach 
#f Jf J Hyper sonic Propulsion 
The Space Sh uttle and ICBM reentry vehicles are actually unpo wered 
hypersonic gliders. Obtaining posi tive net thrust from an airbre athing 
engine is quite difficult at hyperson ic speeds (especi ally over about Mach 8). 
Net thrust for any airbreathing engine is found as gross thrust minus 
engine- related drag. The drag includes the momentum drag of slow ing the 
air down enoug h to mix it with fuel and get it to burn. If we slow the air 
down enoug h to make that easy, the momentum drag is so large that net 
thrust is virtually impossible. If we do not slow it down very much, it is 
very difficult to get the air mixed and burned in the fraction of a secon d 
that it is inside the engine. Even if we can, the net thrust will be found as 
the difference between two very large numbers, gross thrust and drag. If 
either of those changes by a small perce ntage from our expectations, the 
net thrust will be negative. 
Regular turboj ets require slowing the air down to about Mach 0.4-0 .5, 
which raises tempera ture as well as pressure. At speeds much over Mach 3, 
the temperature of the air itself is alread y almost too hot for turbine 
blades, and if we add fuel and combust the mixture, we will burn off any 
turbine blades. The air turbo rocket concept avoids this by not passing the 
outside air through the turbine blades. Instead, a rocket motor drives the 
turbine that in turn drives the compressor. The rocket is run fuel- rich, 
which keeps the tempera ture down, and provides leftover fuel to be burned 
when the rocket exhaust is mixed with the compressor air downstream of 
the turbine. Note that, even though this is an airbre athing engine, some 
amount of oxidizer must be carried for the rocket motor at its core. 
The ramjet concept avoids the turbine blade heating problem by not 
having any. Compression is provided by the inlet system alone. Fuel is 
added, burned, and exited through a nozzle to provide thrust. Of course, 
this does not work at low speeds, so some other propulsion device such as 
a rocket boos ter must be used for takeoff. The air turbo rocket does 
provide thrust at zero speed, one of its benefits, but the ramjet is more efficient at higher speeds. The hybrid air turbo rocket-ram jet (or ju st air turbo 
ramjet) diverts its flowpaths to form a ramjet at higher speeds. 
The ramjet slows the air down to subsonic speeds. At hypersonic velocities the momentum drag losses become excessi ve. The supersonic com bustion ram jet, or scramjet, attempts to mix and burn the air at 
supersonic internal speeds. While this has been demonst rated in the labora tory, an oper ational scram jet engine has not been developed yet. Figure 22.5 
shows the bottom of an airframe-in tegrated scramjet confi guration, illustrating CFD analysis done at NASA Langley Research Center. l154l Note that the 
vehicle's forebod y forms the inlet ramps, whereas the afterbod y forms a 
nozzle expansion surface. 
NASA's Hyper-X research vehicle (X-4 3), similar to Fig. 22.5, succes sfully 
flight tested its hypersonic scram jet engines at a speed of Mach 9.6 in 2004.


<!-- p.825 -->

CH APTER 22 Extre mes of Fligh t 823 
Fig. 22.5 Scramjet CFD ana lysis (NASA Langle y Research Center ). 
This proved that it is possi ble to obtain fuel mixing, combustion, and net 
thrust with internal flow speeds well above the speed of sound. However, 
this vehicle did not take off and fly to that test cond ition-it was boo sted 
by a rocket stage many times larger than itself. Also, its test time was just a 
few seconds. Then in 2010, Boeing's X-51 demonst rated scramjet burn for 
over 2 min, but at a relatively slow speed-on ly Mach 6! It too was boost ed 
to flight conditions by a large rocket stage. 
References [15 5, 156] are recommended for aerod ynamics, propulsion, 
and flight mechanics of hypersonic and ree ntry vehicl es. 
D Lig hter Than Air 
#jJll LTA Appl ications 
Wilbur and Orville were not the first to fly. This brash statement depends, 
of course, upon the definition of the words "to fly." 
If your definition matches the ancient dream of mankind-to ascend into 
the air, go where you wish under power and control, and safely return to 
Earth when and where you choose-t hen the first to truly fly was proba bly 
Alberto Santos-Du mont in his 1898 gasoline- powered airship .l15 7l In his 
first flight he reached 1,300 ft {400 m} above Paris, circling about with ease 
before an astounded and ecst atic crowd.* The landing was less than 
perfect because of a problem with the ballonet but as they would later say, 
any landing you can walk away from is a good one. 
*O thers had flown variously powered airships before but their designs were heavy and clumsy, 
their flights were not repeated, and they made no further developments.


<!-- p.826 -->

824 Airc raft De sign: A Concept ual Approach 
Said Santos- Dumont of that flight, in words that ring true to any pilot 
today, "I cannot describe the delig ht, the wonder, and the intoxicati on of 
this free diagonal movement onward and upward, or onward or downward, 
combined at will with brusque changes of direction horizont ally when the 
airship answers to the touch of the rudd er!" )15 8l 
In 19 01, Sant os-Du mont won the Deu tsch Prize and worldwide fame for 
a flight along a specified 7-m ile {11- km} course in less than 30 min includin g 
a rounding of the Eiffel Tower. By 19 03, Sant os- Dumont was flying almos t 
daily in his ninth design, landing on the roofs of his favorite Parisian restaurants and allowing an acquaintance to become the first woman to fly a 
powered flying machine -and she flew solo. These fellows from Ohio say 
they flew how far ... ? 
Count Ferdinand von Zeppelin, whose name has become synonymous 
with "airship ," launched his first design in 19 00. Unlike Santos- Dumont's 
balloon-like designs, the LZ- 1 featured a rigid outer structure with the 
lifting gas held in sep arate internal cells. It was huge-420 ft long {128 m} 
with a hydrogen lifting gas capac ity of 399,000 ft3 {11, 300 m3}. On its first 
flight it carried five people and, coincident ally, also reached an altitude of 
1, 300 ft {400 m}. Von Zepp elin, a retired general, immed iately began to 
explore military applications, and by WWI the zeppelin had evolved into a 
feared long- range bomber despite its explosi ve vulnerability. 
Following the war, the Zeppelin Company developed successful passenger airships that flew regul arly scheduled trans-A tlantic service at a time 
when heavier-t han- air airliners were in their infan cy. The 19 28 Graf Zeppeli n 
flew over a million miles without incident and made an aerial circumna vigation of the globe carrying passen gers . 
However, the fragilit y of the airship's lightweight structure coupled with 
the exp los ive prop erties of hydrogen led to numerous and highly public 
disasters. Other than the Graf Zeppelin, most of the famous airships eventually crashed. This culminated in the 19 37 Hindenburg disast er, caught 
on newsreel footage and endles sly repla yed in theaters around the world 
("Oh, the humani ty!") . This ended public faith in airships at about the 
same time that airplanes became practical for passen ger service, thus 
ending the "golden age of airship s." 
Light er-t han-air flight continued in the military. During WWII, U.S. Navy 
blimps were successful esco rts for shipping convoys because they could fly 
long distances at slow ship speeds and could spot and attack the enemy submarines. The last were retired in 19 62, after which powered lighter-than- air 
flight was mostly limited to advertising, notably the famous Good year Blimps. 
Today there is renewed interest in airships for various applica tions 
including sightseeing, carriage of bulky cargo, border patrol, and speci al missions such as logging and missile defense. A revital ized Zeppelin comp any is 
produ cing the passenger-c arrying Zeppelin NT, being used for sightseeing , 
research, and diamond mine explo ration. The famous Good year Blimp s 
have all been replaced with NTs which for historical reasons Good year still


<!-- p.827 -->

CHAP TER 22 Extre mes of Flight 825 
calls "blimps" even though they are technica lly semirigid airships (see below) . 
Both the U.S. Navy and Army are flying blimps again, for research and potential surveillance missions. High- altitude airships are being consi dered for 
65,000 ft or more {20,000 m} . The U.S. De partment of Defense (DoD) is 
investigating modern airships for cargo and spec ial applica tions. And 
unmanned airships are in development for tactical reconnaissan ce-or are 
they alread y operational? 
Lockheed has flown a large hybrid airship (see below) called P-791 and 
plans to offer commercial hybrid airships in the near future. Simil arly, Northrop Grumman in collabo ration with UK-based comp any Hybrid Air Vehicles 
has built and flown the HA V 304. This has evolved into the Airlander 10, currently in flight test with the intention of commercial operations. 
A non- traditi onal application of airships is the "poor- man's satell ite," 
where lighter-t han-air techn ology is used to hover indefinitely at high 
altitude over a single spot, with applica tions such as communica tions or 
cell-phone relay, wireless internet networking, and real- time sensing. The 
large size of an airship permits an enormous radar, offering range and 
resolution simply not available with radars that fit into airplanes. Perhaps 
the most ambitious idea is the "orbital airship," where a high- altitu de 
airship climbs to 200,000 ft {61 ,000 m} using buoyancy and then boos ts 
itself to orbital speeds using electric ion propuls ion! 
#J'Jf J Air sh ip Types 
There are three major types of airships, or "dirig ibles." The word dirigible 
is not a corruption of "rigid" as some suppose, but instead comes from the 
French dirigeable, that is, "steer able." 
Nonrigid airships are -asic ally streamlined ballo ons. They require a slight 
overpressure to hold their shape against the aerod ynamic "dishing" likely to 
occur from dynamic pressure at the nose. The overpressure required is small, 
typically about 5 psf {0.24 kN/ m2}, so that a puncture only results in a slow 
leak unless the hole is towards the top. Nonrigid airships are often called 
"blimps," a word said to come from a British military designation Type 
B-L imp. Others belie ve it comes from the odd sound made when you tap 
on the envelope. 
Semirigid airships are blimp-like and require internal pressure to hold 
their shape, but add an internal or external structure to distribute loads to 
the fabric. Most of Santos-Dumon t's designs were of semirigid construction, 
with the engine and cockpit attached to a braced frame slung below 
the envelope. 
Rigid airships, generica lly called "zeppelins," have an external structure 
that holds its shape without the need for internal press uriza tion. Most 
have fabric -covered skins, but some have been built with metal skins. Rigid 
airships usua lly hold their lifting gas in separate cells for redundanc y.


<!-- p.828 -->

826 Air craft Desi gn: A Conc ep tual Appro ach 
An interesting airship variati on is the hybrid, one that gets part of its lift 
from aero dynamics such as a lifting hull, airplane-like wings, or even a helicopter rotor (e.g., see Fig. 22.6). The airship portion can be no nrigid, semirigid, or rigid. The hybrid airship notion is not new; Santos- Dumont flew an 
airship with wings in 19 03. However, the 19 27 Airship Design textbo ok by 
C. Burgess f159 l flatly declared that such a craft "com bines the disad vantages, 
and loses the merits of both types." 
This is proba bly true in terms of weight and drag, but ignores the operational advantages of a hybrid vehicle over a tradit ional airship. The conventional airship is, by definition, as light as the air and thus is difficult to handle 
on the ground. To land, its lines must be caught by a ground crew or machin e 
and then attached to a mooring mast. There the airship must be free to pivot 
with the wind and must be moni tored or tied to make sure that a change in 
atmospheric dens ity or a wind gust cannot drive the tail into the ground, or 
lift it embarrass ingly and dangero usly vertical. With payload and fuel 
removed, the conventional airship experiences excess buoyancy and so 
must be ballasted before unloading. When fuel is burned during flight, it 
becomes too light to land, requiring the valving off of lifting gas, or the use 
of a mechanism to reco ver water vapor from the engine exhaust. 
The hybrid airship avoids these problems because it is actually heavier 
than air. With only partial hydro static lift, it has a substantial download 
when sitting on the ground and can land and taxi like a normal airplane. 
The hydrostatic lift reduces the need for aerod ynamic lift, which gives a 
high effective lift-to- drag ratio at low speeds. 
Hybrid airships vary widely in design and oper ation depending upon how 
the lift is spli t, ranging from basica lly an airplane with a little extra lift from 
helium, to an almost-no rmal airship that gets some help from a lifting hull. 
Analytical studies by this author indica te that a 50-50 split between aerodynamic and hydrostatic lift provides the best balance between cruising efficiency and ground handling, f1 7l but the result depends upon the 
Fig. 22.6 Ohio air ship "Dyna li fter" hybrid air ship (D. Raymer, 2001 ) .


<!-- p.829 -->

CHAP TER 22 Extre mes of Fligh t 827 
assumptions and applica tion. Note that hybrid airships cannot hover for 
cargo loading unless a powered VTOL mechanism is added or enough fuel 
has been burned off that it is 100% bu oyant by the time it has to hover. 
l/lfl Hyd rostatic Lift 
The design of an airship has many similarities to the design of any flying 
machine but has one obvious difference: the provision and accoun ting for 
hydrostatic lift. The concept is simple: the lifting gas has less dens ity than 
the air it displaces, so an upward force is exerte d. We merely need to 
provide sufficient internal gas volume and some form of containment, 
ensure that the lift loads are transferred to the structure of the vehicle, and 
calculate the weight of the componen ts and the lift of the gas. 
Airship lift is funda mentally determined by Archimedes Principle, which 
states that the gross buoyancy is determined by the weight of the displaced 
gas, namely, air. So, before we consider the lifting gas, we must look at the 
air to be displaced. Then we will sub tra,.ct the weight of the lifting gas used 
to displace the air to get the net lift. 
As found in Appe ndix B, air has a sea- level, standard- day (59°) dens ity of 
0.0023769 slugs/ft 3 {l .225 kg/m3), or a weight force equivalent (multiply by 
g) of 0.0765 lb/ft 3 {1 2.01 N/m3). This represents the weight force of the air 
that is displaced by the lifting gas, hence the gross lift. 
Air dens ity is affected by altitude, temperature, barometric pressure, and 
humidity. Atmosphere tables such as Appe ndix B give the altitude variati ons. 
The effects of temperature can be found using Charles' Law (volume varies 
directly with absolute temperature if pressure is held constant) . The effects 
of barometric pressure can be found using Boyle's Law (volume varies inversely with pressure if temperature is held constant) . 
Moist air is less dense than dry air because water vapor is less dense than 
the air it displaces. The -ater-carrying capabi lity of air depends upon the 
temperat ure- hotter air can hold more. At freezing temperature [( 32°F), 
{0°C}], fully saturated air weighs only 1/ 2% more than dry air, but at 90°F 
{32°C} saturated air weighs 5.2% more than dry air. The dens ity variati on 
is approximately linear with percen t saturation, and 50% saturated air is 
often used as a design assumption. 
There are three main lifting gases, namely, hydrogen, helium, and hot air. 
Hydrogen is desirable for several reasons. It is common, being an element of 
water, and can be produced anywhere by electrolysis or various chemical 
reactions. During the U.S. Civil War, army balloo nists traveled with 
wagons full of acid to make hydrogen. It also has a greater lifting capac ity 
than any other gas. It only has one problem: it is highly flammable and explosive under the right circumstan ces. For this reason it is now forbidden to use 
hydrogen in passenger-c arrying airship s. 
Helium has about 10% less lifting cap acity and is more expensive. Being 
an inert elem ent, helium does not combine to form chemical compounds and


<!-- p.830 -->

828 Airc raf t Des ign : A Conceptual Approach 
thus cannot be "broken" out of readily obtainable substances. In fact, helium 
was unkn own to mankind until spect ral analysis of sunli ght revealed a new 
element that was wrongly thought to be a metal, hence the name ( -sun + 
metal). Luckily, helium is found blended with natural gas in under ground 
wells and can be purified out for a reaso nable price. 
As a conser vative rule of thumb, for each 1,000 ft3 of gas hydrogen will lift 
roug hly 68 lb, whereas helium will lift about 60 lb. A similar metric rule of 
thumb is, for each 1000 liters (cu bic meter) of gas, hydrogen will lift about 
1.1 kg, whereas helium will lift about 1.0 kg. 
Hot air is widely used for recreational balloons and sometimes airships, 
usually heated with propane burners. The air must be heated for the duratio n 
of the flight, thus limiting flight time. Depending upon temperature, hot air 
can lift roug hly 20 lb per 1,000 ft3 {0.300 kg per m3}. 
To proper ly calculate an airship's net lifting force, the gross lifting force of 
the displaced air is reduced by the weight force of the displacing gas. Under 
sea- level, standard- day (59°) conditions, hydrogen has a weight force density 
of 0.00532 lb/ft 3 {0.836 N/m 3), and helium has a weight force density of 
0.010 56 lb/ft3 {l .66 N/m 3). 
Densi ty and hence lifting capac ity are affected by the purity of the lifting 
gas. Although it should be nearly pure (98% or better) when first loaded into 
the airship 's gas cells, there will be a slight leakage with time that allows lifting 
gas to exit and air to enter and dilute the mixture. Golden Age airships would 
lose pu rity at a rate of about 2-3% per year. f16 0l Today it should be half that. 
When the lifting gas purity gets too low, the gas needs to be replaced or 
"scru bbed." The density of the impure gas mixture is found simply as the 
weighted average of the lifting gas and the air. 
For calculation of hydrostatic lift under nonstandard conditions, we 
would consider the dens ity variations in the lifting gas resulting from 
changes in altitude and temperature. However, these affect the lifting gas 
densi ty by the same amount that they affect the dens ity of the air being 
displaced. If the gas bag is free to expand or cont ract, the net lift will 
be unchanged. 
This seems odd but is true-as you climb higher, the gas bag expands, but 
the lifting force remains unchanged. Balloons designed for extreme altitude 
flight are huge and mostly empty when launched, resembling a tower of 
plastic with a jellyfish at the top, but they swell up to a nearly round shape 
at their design altitu de. If they go higher than the design altitude, the 
maximum volume is exceeded, and if the gas cannot be quickly vented, the 
balloon will burst. If the gas is vented, the lift is reduced, which can be a 
real problem when you later try to land! 
This maximum altitude is characteristic of all lighter-t han-a ir vehicles 
and is called the "pressure height." It is selected by the designer, and hull 
volume is calculated at pressure height making it much bigger than the 
volume of the required lifting gas at sea level. If a higher pressure height is 
selected, the gas bag will have to be made even larger, resulting in more


<!-- p.831 -->

CH APT ER 22 Extre mes of Flight 829 
weight, cost, and aerod ynamic drag. If a lower pressur e height is selected, the 
airship will be more limited in its flight routes and more susceptible to 
bad weather . 
The external shape of an airship cannot be allowed to change as the lifting 
gas bags swell and shrink with altitude. For a rigid airship, we simply make 
the hull large enough so that the fully expanded gas bags will fit. At altitu des 
below pressure height, external air enters the hull and presses the gas bags up 
towards the top of the hull (remember -they float) . 
For semirigid and nonrigid airships, the problem is especi ally severe. If 
the excess gas is vented while ascending, upon descen t the env elope will be 
only partially full and will tend to collapse. A clever solution (previous ly 
invented) was used on Santos-Du mont's first airship-the ballonet. This is 
a "balloon within a balloon" affixed to the inside of the airship hull. During 
ascent, this air-filled balloon is allowed to collapse as the lifting gas 
expands into its space. Air, not irreplaceable lifting gas, is vented overboard. 
During desc ent, the ballonet is reinflated by an air fan, pressing the lifting gas 
into the top of the hull. Altern atively, ram scoops behind the propellers can 
be used to reinflate the ballonet on descent. 
On Sant os-D umont's first flight the air fan (actua lly a pump) was not 
powerful enough to quickly reinflate the ballonet on descent. The weight 
of the engine and pilot pulled the cigar -shaped envelope into a dangerous 
"V" shape that could have torn the suspension lines loose, high over Paris. 
He was lucky to survive and devised more powerful air fans for his 
later designs. 
The calculation of the extra volume required within the hull can be made 
by determining the percent fullness (%F) at sea level based on the change in 
lifting gas dens ity, using Charles' and Boyle's Laws as follows: 
Percent fullness: 
%F = PH = PHTSL PSL PsL TH (22 .18) 
PH and TH are the atmospheric pressure and absolu te temperature at the 
desired pressure height. SL denotes the desired sea-le vel conditions, which 
might or might not be standard condi tions. This equation determines how 
full the lifting gas volume can be at sea level if the desired pressure height 
is to be reached without venting gas. To calcula te the total required 
volume, find the required lifting gas volume at sea level and divide it by 
the percent fullness. 
For example, to allow reaching an altitude of 10,000 ft without venting 
any lifting gas requires a sea-le vel percent fullness of about 0.74. Thus, the 
hull volume must be 1.35 times the volume of lifting gas required at sea 
level, and 26% of this hull volume will be air when the vehicle is at sea 
level. For a nonrigid or semirigid design, this air will be contained in 
bal!onets.


<!-- p.832 -->

830 Aircr aft Des ign: A Concept ual Appr oach 
Some high- altitude balloons are of the "superpressure" type, where the 
internal pressure can be substantially greater than the external pressur e. 
This relaxes the requirements for percent fullness. The envelope is made 
strong eno ugh that at high altitude it can withstand the lifting gases' 
attempt to expand without valving off the excess gas. This is espec ially important for long-dur ation balloons where the heating during the day can over 
expand the gas leading to valving off. This is also being consi dered for longduration airships, although the weight pena lty is obvious. 
Another alternative to venting was considered during the early days of 
airships, abandoned as heavy and impractical, and is now being revived; 
namely compressing the extra helium as the airship ascends. Earlier concepts 
envisioned high-pressure metal tanks, but the modern approach uses fabric 
tanks like huge bicycle tires. The helium press urization scheme also allows 
"planting" the vehicle firmly on the ground after landing to simplify cargo 
loading. 
For lift calculat ions of a hot air balloon, Charles' Law is used to find the 
volume of the heated air. This determines dens ity, hence lift. Normally, the 
internal tempera tures of a hot-air-ba lloon envelope are about 250°F {1 20°C }. 
#f Jll Air sh ip Design and Ana lysis 
Although much of airship design is similar to aircraft design, there are 
impor tant differences. For example, airship designers cannot use wing area 
as the reference for aerod ynamic coefficients because there is not a wing. 
Frontal area is sometimes used, espec ially in drag tables. Normally though, 
the ref erence area used by airship designers is the total hull volume, raised 
to the 2/3 power to get units of area. 
Airship tail sizing is also based on v°·66, often estimated as 13% times this 
parameter. Most of the old airships were actually unstable in yaw, but the 
time to diverge was so long that a good "helmsman" had no trouble compensating. In pitch, the low center of gravity relative to the hull's hydrostatic lift 
provides additional stabil ity to counter the aerod ynamic instabil ity. 
Another interesting parameter in use is the standard displace ment D, 
which is the volume of the hull times the air's sea-le vel standar d-da y 
densi ty. In other words, D is the weight of air displaced by the hull. 
The optimal airship hull fineness ratio was discussed in Chapter 6 and 
should proba bly be some where between six and eight for best aerod ynamics. 
However, the structural weight is critical for airships, and a higher fineness 
ratio hull will be heavier. Recent studies indicate that nonrigid and semirigid 
airships should probably have a fineness ratio of about four. Rigid airships 
should be about six. 
The parasitic drag analysis methods described in Chapter 12 work fairly 
well for airship s. To estimate hull drag, a 0.85 adju stment factor should be 
applied to the body drag equation to account for beneficial scale effects.


<!-- p.833 -->

CHAP TER 22 Extre mes of Fligh t 83 1 
You can use whatever reference area you choose in the equations including 
the airship convention (v° ·66), but don't get confused later. 
The lift calculation methods of Chapter 12 work poor ly for airship s. An 
airship hull is not just a wing of extreme low aspect ratio. The flow is 
highly three-dimensional, and the loca tion of flow separation is a complicated 
line running fore and aft as well as wrapping around the hull. Even high-end 
CFD may have difficulty estimating hull lift due to real-w orld effects including irregularities and the fact that most airship hull skins are not very rigid. 
The hull shape changes under load! 
As a rough approximat ion, data on airship hulls indicates that at low 
angles of attack, the slope of the lift curve (Cr0J is approximately 0.6 referenced to (v° ·66), or 0.24 when referenced to the total planform area. The 
lift curve is very nonlinear, and the stall is not defined. But norm ally, 
airship hulls are doing very little lifting. That's what the gas is for. 
A big difference compared to normal aircraft an alysis is that the Breguet 
range equation does not apply to airship s. Breguet integrates for range 
using the aerod ynamic lift-to -drag rati.o as the vehicle weight changes. A 
conventional airship has little or no aerod ynamic lift. Therefore, drag 
does not change as vehicle weight changes, and Breguet is therefore not 
applicable. Instead, range is found simply as engine run time multip lied 
by speed. 
Because of the large size of airships, the engines must accelera te not just 
the vehicle's mass but also the "appa rent mass." This is the outside air that, 
through viscos ity, clings to the vehicle and therefore must also be accelerated. 
An old rule of thumb (NACA TR 11 7) suggests using 2.5% of the total hull 
volume, times the dens ity of air, as an apparent mass for airship acceleration 
calculat ions. Apparent mass also exists for airplanes, but we normally ignore 
it. Also, for an airship the mass of the lifting gas must be accelera ted even 
though the gas seems to have a negative weight! 
For a hybrid airship iri: which subst antial aerod ynamic lift is used during 
cruise, the aircraft performance equations including Breguet can genera lly be 
used after one impo rtant substi tution-a ll vehicle weight terms W should be 
reduced by the hydrostatic lift. This reduces the weight being carried by the 
wings and hence reduces drag due to lift. 
This simple analysis adjustment does not work for performance calculations involving acceleratio ns, such as takeoff, because the engines must 
accelerate the full mass of the vehicle, not just the net weight. Also, the 
engines must accelerate the apparent mass and the mass of the lifting gas. 
Weights analysis of airships is similar to that of aircraft. Statistica l and 
analytical methods can be used, but unfortunately most of the available 
statistical methods are approaching the centur y mark in age and are more 
rules of thumb than sophisticated statistical equat ions. For example, one 
old approximation says that fixed weight excluding powerplant is 30% of 
the hull's standard displacement D (just defined) . Crew, ballast, and stores 
weights were estimated together as 5.5% of D.


<!-- p.834 -->

832 Air c raf t Desig n: A Concep tual Approach 
To get better weights estimates, structural analysis methods have to be 
applied along with information from vendors of the various subsystems, 
skin coverings, and gas cell materials used in the design. Note that some of 
the structural loads that must be con sidered are unique to airships, and to 
save weight the airship structure is designed to be as flimsy as possible. 
The possi bility of an in-f light breakup is very rea l-be careful! 
Airship design criteria can be found in FAA Docum ent P-8 11 0-2. Type 
certification requirements are descr ibed in FAA Docum ent AC 21.17 -l A. 
NASA Schweizer 1- 36 deep sta ll research ai rcraft (NASA photo) . 
What We've Learned 
We've learned how to apply the aircraft design process to spacecraft, launch 
vehicles, hypersonic aircraft, and airships. The overall process is similar, but 
the design layout and analysis methods are revised.


<!-- p.835 -->

Design of Unique 
Aircraft Concepts 
• This cha pter presents mor e nons ta ndar d ai rcraf t conce pts, from Canar ds to C-wi ngs. 
• Keep an eye on wetted ar ea and tr im med maxi mum li ft: these ki ll man y novel ideas. 
• Caution : new ideas alw ays weigh far mor e tha n you th ink , even if you think you ar e 
bei ng properly conser vativ e . 
• Don't think that nor mal designs ar e only for tho se stuck in the past; the "c onventio nal" de sign ap proach beca me conv entional beca use it is usua ll y better. 
• But sti ll, we can dr ea m. 
In troduc tion 
''T hey laughed at the Wright Brothers !" Throughout the history of 
aviation, thi- refrain has been quoted by thousands of wacky 
inventors with ridiculous ideas. This author had the dubious 
privilege at two major aircr aft companies of being the person who got to 
read, evaluate, and reply to the unsoli cited inventions and design concepts 
that would arrive. And, if I see one more flying saucer proposa l. .. ! 
But, som etimes wacky ideas work. At least, sometimes they work for a 
particular applica tion or requirement. And sometimes, today's wacky idea 
is tomorrow's normal design practic e, such as sweptback wings, canard 
pushers, helicopters, and airplanes made of strings and glue (i.e., composite s). 
But usually, today's wacky idea is tomorrow's wacky idea, and those ideas 
keep on coming back! 
Following are some unique aircraft concepts that seem to have merit. 
Some of them might eventually find widespread use-p erhaps the blended 
wing body and the asymmetrical aircraft. Others might not, but who can 
tell which? These unique conce pts are presen ted here mainly to discuss 
how their design differs from the design of normal aircraft as described in 
833


<!-- p.836 -->

834 Ai rcraft De sign: A Conceptu al Appr oach 
the previous chapters and to provide some specific design guideli nes and 
analysis methods and data for those attempting to design such aircraft. 
Be advised that others, espe cially proponen ts of a particular unique 
conce pt, might hotly disagree with some of this author's opinions and data 
that follow. Also, no claim is made as to the absolute correctness of this information. It might be too pess imistic, reflecting the author's "show- me" engineering ment ality, or it might be too optimistic, reflecting this author's love of 
novel and creative engineering approaches. After all, this author has the patent 
on the RIVE T VSTOL fighter, the one with the engine mounted backward! 
When reading the following sections, be aware that most "great ideas" in 
aircraft design fail to fulfill their promise. There are reasons why most airplanes follow the same basic arrangeme nt, and it isn' t "conser vatism" or 
worse by the designers. 
There are three main problems that sink new ideas. Two are rel ated: 
wetted area and trimmed maximum lift coefficient. Wetted area directly 
drives the parasitic drag and also has a large effect on empty weight. If a 
new idea has features that increase the wetted area over a normal design, it 
is unlike ly that it will be worth it in the end. 
The problem with trimmed maximum lift capabi lity is more subtle. Many 
innovative ideas include a lifting surface farther to the rear than a regular 
wing. This is fine in normal flight, but for landing it is not possible to trim 
the design when large flaps are deflected on the back wing. Without large 
flaps on all lifting surfaces, for trim or any other reason, those lifting surfaces 
must be made bigger. This makes them heavier, increases wetted area, and 
usually obliterates whatever ben efit was expected. 
The third problem: We always fool oursel ves in weight estimat ion. When 
evaluating the new hardware needed to implement our innovation, we have 
little unde rstanding of the real-w orld problems. Nobod y has made one like 
that before. We also show little patience with a conser vative weight 
estimation since it will make our wonderful idea look bad. Believe me on 
this-w hatever you think it will weigh during con ceptual design studies, 
when it's all done it can easily weigh double that. 
Or more. 
Fl ying Wing, Lifting Fus elage , and 
Blen ded Wi ng Body 
The pure flying wing, with neither fuselage nor 
tails, is the "ultimate airplane" in the minds of many. 
Flying wing advocates point out that all an aircraft 
really needs is lift and thrust , and that a fuselage, 
tails, nacelles, and other compo nents just add weight 
and drag! All else being equal, they are right, but practical problems overcome the theoretical advantages 
for many applications. 
• If longer than 
wide, it's a 
lifting body 
• If wider than 
long, it's a 
flying wing 
• If they're the 
same, it's a 
flying saucer ... 
and it doesn't 
work


<!-- p.837 -->

CHAPTE R 23 Design of Unique Air craft Con cepts 835 
Early pioneers of the pure flying wing were Reimar and Walter Horten of 
Germany, and Jack Northrop of the United States. The Hor tens flew their 
first powered all-wing design, the H Ilm D-Ha bicht in 1935. With the pilot 
lying prone, the only "bump" from the pure wing geometry was the 
landing gear and the faired shaft for the propeller. Over the next 10 years 
the Hortens flew dozens of designs culmina ting in the first ever turboj etpowered flying wing, the Ho IX, which flew in 19 45. This pure flying wing 
had a span of 52.5 ft {16 m} and was capable of 470 kt {870 km/h}. As mentioned in Chapter 8, this advanced design used RAM and configuration 
shaping for stealth. Its successor, the never flown Ho229, can be seen in 
pieces at the Smithsonian Paul Garber Facil ity, awaiting restorat ion. 
The Hortens employed a design philoso phy of reducing the lift at the wing 
tips to nearly zero, twisting the wing to genera te most of the lift on the 
inboard part of the wing. This allowed moving the e.g. forward and created 
a design very stable in pitch, and, with proper sweepback, in yaw and roll. 
The Horten wings did not require any vertical tails nor the negative -dihedral 
"crank" seen on the outboard panels of -ome flying wings (see Fig. 23. 1). The 
inefficiency of the unusual lift distribution was corrected with increased 
aspect ratio. Notion ally, you can think of the Horten wings as conventional 
aft-tailed aircraft but with those aft tails stuck out on the wing tips. 
Jack Northro p's first flying wing flew in 19 40. Like the Horten wings it 
was virtually pure, with only the canopy and propeller shaft violating the 
wing contours. The N- lM origina lly had the negative -dihedral crank 
already mentioned, but it was removed after initial testing. After flying a 
one-t hird scale prot otype and several related designs, Northrop began 
work on the huge XB-35 flying wing bomber that first flew in 1946. It was 
converted to jet power and redesi gnated YB-49, flying in 1948. Much 
Fig. 23. 1 Horten Jet flying wing.


<!-- p.838 -->

836 Ai rc raft Des ign: A Conceptu al Appr oach 
bigger than the Horten je t, this had a span of 172 ft {52.4 m}, a weight of 
196,1 93 lb {88, 990 kg}, and a speed of 430 knots {800 km/h} .f1 61 l 
Northrop preferred to avoid excess twist, and his designs requir ed some 
vertical tail surface. In the propeller versions the fairing for the propeller 
shaft and the stabilizing effect of the pusher- propellers thems elves provided 
all of the needed directional stabil ity. When converted to a jet, the YB-49 
required small vertical tails to replace the lost contribution of the propellers. Flying-w ing fanatics are still arguing as to whether the several 
crashes of Northrop flying wings, including the YB-49, were cause d by 
pitch instab ility or by more mundane causes such as structural or hydraulic 
system failures. Whatever the cause, the flight performance of the YB-49 
was outstanding for its day. The only technical diffic ulty this author is 
aware of, a tendenc y to "hunt" in yaw making for a poor bombing platfor m, 
could have been solved a few years later with the active yaw damper developed for the B-47. 
Northrop was vindicated late in life when his comp any won the contract 
to build the B-2 stealth bomber. While technica lly not direct ly related to the 
YB-49, its outstanding aero dynamics and low obser vability have taken the 
flying wing out of the "oddi ty" category and into the "viable option" category. 
Flying-w ing design is similar to the design of other aircraft, with a few key 
differences. Obvious ly, the planform wing geomet ry, twist, and airfoil shaping 
must be carefully consid ered and analyzed as quickly as possible, and a 
detailed stabilit y and control analysis should be done early in the proj ect. 
Center-of -gravity location is critical. Use of sweepback and twist to attain 
pitch stabili ty has been discussed. Alternat ively, a "reflexed" airfoil can be 
selected, having the trailing edge lifted slightly to provide a naturally stable 
airfoil. Such airfoils tend to be less efficient and are typically limited to 
slower aircraft. 
The relax ed-st ability, active flight controls developed for fighter aircraft 
permit the B-2 and other modern flying wings to be more optimized for aerodynamics with less of a compromise for stabilit y and control. This is 
especia lly bene ficial because the use of longitudinal instabil ity allows the 
flying wing to take off and land with its trailing- edge surfaces angled downwards like flaps, rather than upward (see Chapter 16). 
The flying wing requires speci al at tention as to yaw control. Northrop's 
wings, including the B-2, rely on wing- tip-mounted surfaces that split 
open, creating drag that gives a yaw force. This has a very nonlinear resp onse. 
When first opened, nothing happens. When it is opened more, it suddenly 
"catches" the air creating a large yawing moment. For this reason the B-2 
has a "pilot comfort" mode wherein both of these drag rudders are cracked 
open ju st to the point of "catching, " allowing the flight control system to 
fine tune the aircraft's dynamic motion and dampen any "hunting" in yaw. 
This can be seen in most pictures of the B-2 in flight. 
Other possible wing- tip drag rudders are plates that extend up and down 
near the middle of the airfoil and clamshell-like devices at the leading edge.


<!-- p.839 -->

CHAPTER 23 Design of Unique Airc raft Concep ts 837 
Less "pure" flying wings have used vertical tails, often at the wing tips. 
Conventional rudders can then be used. If they cannot provide eno ugh 
yawing momen t, they can be mechanized to increase drag as they open 
outward, magnifying their effect. 
Roll and pitch con trol for flying wings is usually done with conventional 
trailing-edge surfaces. It is best to combine these functions as elevo nselevator-ailer ons-so that the nose-up deflection, which is trailing edge up, 
delays stall at the wing tips and enhances rather than reverses the wing 
twist effect. Several early Horten designs had ailerons outboard and elevators 
inboard and were almost unflyable. 
Proper ly done, the flying wing should obtain reduced wetted area compared to a conventional design and should also have a lower structura l 
weight. This is due to the reduced number of compo nents, and also due to 
the "spa nloa ding" effect discussed in Chapter 8. In fact, the "spanloaded 
flying wing" has been proposed as a massive cargo aircraft. Designs large 
enough for a root-to -tip cargo bay capable of holding U.S. Air Force outsized 
cargo within the airfoil contours have been proposed. Nobod y has 
determined where to land such a monster, however! 
Flying wings should have a lower structural weight than a conventiona l 
design. The statistical weight equations of Chapter 15 can be applied, including the 0. 7 68 wing weight adjust ment typical for delta wings if the flying wing 
is well designed and reasonably spanloaded. However, for structural purposes 
the "wing" is not the entire wing. The center section of the vehicle, despi te 
looking like part of the wing on the outside, will be constructed more like 
a fuselage with cutouts for cockpit, landing gear, engine access, and 
weapons bays or passenger doors as appropriate. This center portion of the 
airplane should therefore be an alyzed using the fuselage statistical equations, 
probably with a weight adjustment of 0.774 as used for delta wings . 
Reference [16 2] is rec9mmended for further information on flying wings 
and tailless aircraft. 
The lifting fuselage grows out of the desire to make the best possible use 
of all aircraft components. Rather than allow the fuselage to go "along for the 
ride," Burnelli and others have designed aircraft where the fuselage is shaped 
like a wing so that it can co ntribute to the lift. Burnelli envisioned a wide 
fuselage with an airfoil shape from front to rear, resembling an untapered 
wing of aspect ratio 0.4 or less, with conventional wings attached. This 
would have a high structural weight, prob ably overco ming any potential 
aerodynamic ben efits. 
However, virtually all airliners incorpor ate the lifting fuselage principle to 
some extent. By designing so that the fuselage is at a small angle of attack 
during cruise, a little bit of lift is generated for free, and a dip in the spanwise 
lift distribution is avoided. Also, the posi tive pressures that this causes under 
the fuselage help to turn the flow at the back of the aircraft, reducing separation drag. This was overdone on the Lockheed L- 10 11 , and flight attendants 
have been complaining ever since that they have to push the carts uphill.


<!-- p.840 -->

838 Air c raf t Design: A Conceptual Approach 
Fig. 23.2 Blend ed-wi ng-body air plane concept (courtesy of The Boeing Compan y). 
It is genera lly assumed that the next airliner is going to look ju st like the 
last airli ner-a tubular fuselage with low wings, a conventional tail, and 
nacelles either under the wings or on the aft fuselag e.* This might not 
always be true, and Boeing is current ly investigating the radical blendedwing-bod y (BWB) concept that might provide a revolutionar y improvement 
in subsonic airliner efficiency (Fig. 23.2) . 
The BWB is basica lly a flying wing with a delta -shaped wing/fuselage in 
the center, large eno ugh for a passenger cabin. In some sense it is related to 
*But see this author's tailless airliner concept, on the cover and described in Chapter 4.


<!-- p.841 -->

CHAP TER 23 Design of Unique Air craft Concep ts 839 
the Burnelli configurati on just described, but the center section is blended into 
the wing panels. This concept reduces the total wetted area of the airplane and, 
with its deep center section, improv es structural efficienc y. The BWB has 
about half of the root bending stresses of a conventi onal configuration. The 
wing-tip -mounted vertical tails also act as winglets to reduce drag due to 
lift. BWB requires relaxed static stability and an automated flight control 
system to fly efficiently, optimize span loading, and avoid the need for a tail. 
The BWB optimizes at a wing loading of about 100 psf {488 kg/ m2}, much 
less than the 160 psf {78 1 kg/m 2} of most airliners. This low wing loading 
permits the elimination of high-lift flaps, and only a leading- edge slat on the 
outboard wing is needed in addition to the wing trailing-edge controls. 
Boeing studies predic t, com pared with an equivalent conventional configuration, a 15 % reduction in sized takeoff weight, a 20% improvement in 
L/ D, and a 27% reduction in fuel usage [16 3l ). A crucial problem to solve is 
the attainment of a cabin pressure vessel without a huge weight penalty 
because the cabin is not a capped cylinder as in a conventional airliner. 
Also, for packaging reasons it seems that BWB is most suitable for a very 
large airliner (800 passen gers ), and there is concern that the dearth of 
windows might be claustro phobic to some passengers. 
EJ Delta and Doubl e-Delt a Wing 
The delta-wing configuration offers certain advantages, espec ially for 
high-speed flight. Extensive research led by Alexander Lippisch showed 
that the true delta (straight trailing edge) or near- delta planform offers 
benefits in wing structural weight, increased internal volume, and transonic 
and supersonic drag. 
Although tailless flying-wing delta designs are more "pure," Lippisch 
favored the inclusion of _vertical tails as seen on his Me- 163 Comet. He 
stated that "without these vertical surfaces it is impossible to obtain a 
degree of directional stabil ity comparable to the normal aircraft'' J164l The 
A- 12 carrier-based attack aircraft was to be a pure tailless flying-wing 
design, relying on modern computerized flight control systems to obtain 
the stability that Lippisch could not. It was cancelled mostly because of 
weight growth- always a problem, espec ially when a design has to compl y 
with carrier launch and recovery requirements (see Appe ndix F) . 
Delta wings usua lly offer structural weight savings compa red to a conventional swept wing because, with the delta, the internal structure need not be 
swept. Typically, a delta wing has its spars going out perpendicular to the 
fuselage, and the load path from tip to tip is a straight line. The statistical 
weight equations of Chapter 15 suggest a 0.768 wing weight adjustment for 
delta wings and a further weight adjus tment to the fuselage of 0.77 4. 
The high-speed drag reductions are obvious from the sweep of the delta 
wing. Because the wing has relatively small aspect ratio and a near-zero taper 
ratio, the wing root chord is very large, so the root thickness is very deep.


<!-- p.842 -->

840 Ai rcraf t De sign: A Concept ual Appr oach 
This reduces structural bending loads and provides extra room for fuel, 
landing gear, and structure. 
This long wing root can be a disadvantage. Sometimes there is no room 
left for a horizo ntal tail, forcing the use of a cantilevered structure, or the use 
of a canard, or the use of a tailless desi gn approach. Because of the high sweep 
and low aspect ratio, deltas often require a lower wing loading. 
During advanced bomber desi gn studies at Rockwell North American 
Aviation (1 977), a delta-shaped stealth flying wing incor porating the span 
loading philosoph y was conc eived by this author and named the "Delta 
Spanloader" (Fig. 23.3). Extensi ve analysis indicated a substantial structural 
weight savings, and the RCS test results were quite good. f52l Like the B-2, 
this concept used relaxed static stabil ity to minimize trim drag and permit 
oper ation of flaps for takeoff and landing. This conce pt yielded a sized 
takeoff gross weight a full 30% lower than a conventional bomber design 
with the same technologies and design mission. 
r 
Fig. 23.3 Delta Spanloader stea lth flying wing (D. Raymer , 19 77).
