# Raymer Ch.4 - Airfoil and Wing-Tail Geometry Selection

*Converted from `Daniel P. Raymer - Aircraft Design_ A Conceptual Approach (2018, American Institute of Aeronautics and Astronautics Inc.) - libgen.li.pdf` by `tools/pdf_to_md.py`. Page markers are printed page numbers.*


<!-- p.53 -->

Airfo il and 
Wing/Tail 
Geom etry Selection 
• From the sizing resu lts, we sel ect the air foils and de fine the geome tries of the wings 
and ta ils. 
• We don' t ju st dr aw some thin g-we pic k cer ta in parame ters that relate to de sir ed 
ftigh t cha racteri st ic s. 
• These in iti al cho ices will be re vised la ter, so don't spend too mu ch time on them . 
In trod uction 
W hen we design a new airplane, we don't just draw wings and tails 
that look "right" and then measure their span and area. Instead, 
we pick values for certain parameters that set their shapes analytically. These planform parameters, such as aspect ratio, sweep, and area, 
are initially based upon a combination of experience, histor y, statistics, 
and, of course, a few quick calculations. There is always a tradeoff between 
aero dynamics, structures, and the needed geom etry for such neces sities as 
landing gear and fuel tanks. 
This chapter discusses the airfoil and the wing and tail geomet ric parameters and presents some quick methods for initially selec ting them. The 
actual wing and tail sizes are set later using methods discussed in Chapter 5, 
which also addre sses the selection of engine size. These are both set as 
ratios to aircraft weight, namel y, the wing loading and the thrust-to-w eight 
ratio (or horsepow er-to-w eight ratio for a propeller aircraft) . Chapter 6 provides a more refined method for initial sizing than the quick method presen ted 
in the last chapter and con cludes with the use of the sizing results to calculate 
the required wing and tail area, engine size, and fuselage volume and length. 
53


<!-- p.54 -->

54 Aircr af t Desi gn: A Conceptual Appr oa ch 
It isn't pos sible to pick initial values that will be perfect in the end, no 
matter how much time you spend or how many co mputer programs you 
write. Everything changes as you go through the design process-e ven the 
requirements . But you have to start some where. The methods presented 
here will get you close, and then the analysis and optimization methods 
described later will help to finalize things. Still, no airplane ever flew 
without the designer thinking, "I wish I could go back and change ... . " 
Airf oil Sele ction 
The airfoil, in many respects, is the heart of the air plane. The airfoil 
affects the cruise speed, takeoff and landing distances, stall speed, handling 
qualities (espec ially near the sta ll), and overall aerod ynamic efficiency during 
all phases of flight. 
Much of the Wright Brothers' success can be traced to their development 
of airfoils using a wind tunnel of their own desi gn, and the in- flight validation 
of those airfoils in their glider experiments of 19 01-19 02. The P-51 was 
regarded as the finest fighter of World War II in part because of its radical 
lamina r-flow airfoil. More recent ly, the low- speed airfoils developed by 
Peter Lissaman contributed much to the success of the man-po wered Gossamer Condor, and the airfoils designed by John Roncz were instrumental to 
the success of Burt Rutan's radical designs. 
Figure 4. 1 illustrates the key geomet ric parameters of an airfoil. The 
proper horizo ntal reference axis for an airfoil starts at the "leading edge" 
and goes back to the "trailing edge," but the exact definitions of those 
terms might not be obvious. It is difficult and unnecessa ry to build a perfe ctly 
sharp trailing edge, so most airfoils have a blunt trailing edge with some small 
finite thickn ess. By definiti on, the "trailing edge" defining the back of the 
reference axis is vertically located at the midpoint of this thick ness. 
The leading- edge point defining the origin of the proper reference axis 
(O, 0) is simply the point on the airfoil that is farthest away from the trailing 
edge. This may or may not be the exact place where the leading edge comes to 
its smallest radius. 
The horizo ntal reference axis is then prop erly defined by these two 
points. This results in the point at the exact leading edge having Z = 0, 
and the midpoint between upper and lower surfaces at the trailing edge is 
at Z = 0. 
The chord of the airfoil is defined as the distance along a straight line 
from the leading edge to the trailing edge, obviously following this horizo ntal 
reference axis. Airfoil coo rdinates tables usu ally provide values assuming a 
chord leng th of either one 1 or 100, and are scaled to fit the desired chord 
length at an actual location on the wing or tail.


<!-- p.55 -->

CHAP TER 4 Air foil and Wing /To il Geometr y Selection 55 
y 
Angle 
of attack 
Actual airfoil shape 
Chor d length "c" 
\ t 
---l__---=---===::;=====----x 
-\ Leadi ng-edge \ 
carnb er lin e 
r:::e:i:.. - - - - - - onc011'' radius 
a\l 
Lower su rface 
Thickne ss 
"t" = j{x) 
Thickness distribution 
Trailin g-edge 
th ickness 
Note: Lead in g-edge radius and traili ng-edge th ickness ar e exa gger ated for illus tration. 
Fig. 4. 1 Airfoil geome try. 
Unfortunately, airfoil coor dinates tables are often found which use 
an "improper" horizontal reference. You will see flat-bot tomed airfoils plotted using a reference axis oriented along the flat bottom, so that the 
leading-edge point is given as a pos itive value on the vertical axis. Computational airfoil design programs will spit out an airfoil defined by coo rdinates 
with no relationship at all to the proper "zero -ze- o-a t-the-le ading-edge" axis 
system. The points go where the compu ter sticks them. 
Use of an "improper" axis system is not really a problem for the designer 
except that one must be very careful while placing the airfoils at the desired 
incidence (pitch) angle. When the aerodynamics department tells you to set 
an airfoil at, say, two degrees incidence, you must always ask "with respect to 
what reference axis?" 
The front of the airfoil is defined by a leading-edge radius, tangent to the 
upper and lower surfaces. Leadin g-ed ge (LE) radius has a huge effect on aerodynamics including lift, drag, and stall characte ristics. Note that Figure 4. 1 
greatly exaggerates the leading-ed ge radius, for clarification. Real ones are 
much smaller and touch the airfoil only at the very front. Mathematica lly 
speaking, they define the curvature exactly at the poi nt of minimum radius 
(usually the LE). 
A large LE radius helps the air stay attached at higher angles of attack, 
giving a higher stall angle and more lift for takeoff and landing. On the 
other hand, an overly fat leading edge gives more drag. Even in such a 
simple decision, aircraft design is always a compromise. 
An airfoil designed to operate in supersonic flow may have a sharp or 
nearly-sharp leading edge to prevent a drag-producing bow shock. Alternatively, wing sweep can be used to reduce the supersonic drag. See below.


<!-- p.56 -->

56 A i rc ra ft Design : A Conc eptu al Approach 
"Camber" refers to the upward -bo wing curvature characteristic of most 
airfoils. Camber gives lift at zero angle of attack and increases the 
maximum lift of an airfoil, * but also increases drag and pitching moments. 
The "mean camber line" is the line equidistant from the upper and lower surfaces. Total airfoil camber is defined as the maximum distance of the mean 
camber line from the chord line, expressed as a percent of the chord. 
Camber lines are expressed mathematic ally, as in the old NACA airfoils, or 
are given as an x-ver sus-z table. 
In earlier days, most airfoils had flat bottoms, and it was common to refer 
to the upper surface shape as the "camber." Later, as airfoils with curved 
bottoms came into usage, they were known as "doubl e-ca mbered" airfoils. 
An airfoil with a conca ve lower surface was known as "undercambered" 
airfoil, generating a lot of lift but a lot of drag too. These terms are technically 
obso lete but are still in common usage. 
For a tailless or flying-w ing aircraft, one way to get natural stabili ty is to 
use an "S" -shaped camber line, with an upwards reflex at the trailing edge. 
This works just lik- the download seen on horizo ntal tails. Such reflexed airfoils have poorer L / D than an airfoil designed without this constraint, losing 
some of the drag benefit that flying wings experience due to their reduced 
wetted area. A computerized, "active" flight control system can remove the 
requirement for natural stabili ty and thus allow a non- reflexed airfoil. Tailless 
designs are discussed in detail in Chapter 22. 
The thickness distribution of the airfoil is the distance from the upper 
surface to the lower surface, measured perpend icular to the mean camber 
line. It's norma lly defined in percent of chord (C) , and provided as a function 
of the distance from the leading edge. The airfoil thickness ratio t/ c refers to 
the maximum thickness of the airfoil divided by its chord. 
For many aerodynamic calculations it has been traditional to sepa rate the 
airfoil into its thickness distribution and a zero -thickness camber line. The 
former provides the major influence on the profile drag, whereas the latter 
provides the major influence upon the lift, the drag due to lift, and the 
airfoil pitching moments. 
Classical airfoil design methods worked ju st this way, with one computer 
code to optimize the wing modeled as a zero- thickness curved camber line. 
To this was added a sepa rately- optimized thickness distribution (or that of 
a suitable existing airfoil). Today's best methods model the actual upper 
and lower surfaces for soph isticated optimization, but the old methods 
worked quite well for their day and can now be run on a laptop computer 
rather than the room-sized tape- driven monstrosi ties of the 19 60's. 
Watch out for this trap: If a cambered airfoil needs to be scaled in thickness, the camber line should remain unchanged to avoid changing the lift and 
pitching moment. Simply stretching the airfoil in the vertical direction will 
*To a very rough appro ximation, a one percent increase in camber provides a 0.03 increase in 
C1-max.


<!-- p.57 -->

CHAPTER 4 Air foil and Wing /Ta il Geome try Sel ecti on 57 
change both thickness and camber. To avoid changing the camber, the thickness distribution should be calculated from the airfoil geometr y, scaled vertically, and then added back to the original camber line to produce the new, 
scaled airfoil. To change camber without changing the thickness distribution, 
scale the camber line vertically as desired then add back the original thickne ss 
distribution. Good thing we have comp uters to do this stuff. 
#f II Airf oil Lift and Drag 
An airfoil generates lift by changing the velocity of the air passi ng over 
and under itself. The airfoil angle of attack and/ or camber causes the air 
over the top of the wing to travel faster than the air benea th the wing. 
Bernoulli's equation shows that higher velocities produce lower pressures, so that the upper surface of the airfoil tends to be pulled upward by 
lower-than-ambient pressures while the lower surface of the airfoil tends 
to be pushed upward by higher-than- ambient pressures. The integrated 
differences in pressure between the t9P and bottom of the airfoil generate 
the net lifting force.* 
Figure 4.2 shows typical pressure distributions 
for the upper and lower surfaces of a lifting airfoil 
at subsonic speeds. Note that the upper surface of 
the wing contributes about two-thirds of the total 
lift so the designer should avoid disturbing the top 
of the wing. If possible, put flow-disturbing components like wheel well bumps and wing struts on 
the bottom. 
When you have to 
do something bad to 
a wing, do it to the 
bottom of the wing. 
The top generates 
2/3 of the lift! 
Figure 4.3a illustrates the flowfield around a typical airfoil. The arrows 
represent airflow veloc ity vectors, with the vector length indicating loca l velocity magnitude. In Fig. 4.3b, the freestream veloc ity vector is subtracted 
from each loca l veloc ity vector, leaving only the change in velocity vector 
caused by the presence of the airfoil. It can be seen that the effect of the 
airfoil is to introduce a change in airflow, which seems to circulate around 
the airfoil in a clockwise fashion if the airfoil nose is to the left. 
This "circu lation" is the theoretical basis for the classica l calculation of lift 
and drag due to lift. The greater the circulation, the greater the lift. Circulation is usually represented by r and is shown as a circular flow direction as in 
Fig. 4.3c. 
* There is another way of looking at lift-behind the wing there will be a downwash, geometrically 
caused by the airfoil angle of attack and camber. Thus, the wing has accelerated the air downwards 
requiring a force to have been applied to the air, and by application of Newton's laws this means that 
the air has applied an equal and opposi te force to the wing. This down wash momentum in the air adds 
up to and equals the lift on the wing. People continue to have arguments over this distinction, often in 
the popular aviation magazines. Both ways of looking at lift are 100% correct. Lift equals the total 
downwash momentum imparted on the air, and lift equals the integrated vertical component of 
pressures on the wing. Which one truly "causes" the lift? Well, the only way a force is exerted on 
the wing is through pressures, so this author leans towards that explanation-but it really does 
not matter.


<!-- p.58 -->

58 Air c raft Desig n: A Conceptual Approa ch 
atmospheric 
a) 
Press ur e ab ove 
atmospheric 
Actual 
flowf ield 
b) Freestr eam 
Press ur e componen ts 
in lif t dir ection 
Fig. 4.2 Typica l air foil press ure di stri bution. 
- - - - --- - - - -- - - -.-- - - ----.... -- --- .__ 
- -- --- - - .__ ---.... .__ ......__ .__ --- - -- - ---- - (Arr ow length equals local velocit y) 
veloci ty vecto r • 
su btracted ' 
- from local 
vector 
c) "Cir cu lation" 
representation 
• 
• 
• 
• 
• 
Fig. 4.3 Airfoil flowfield and cir cu lation . 
T 
r 
'


<!-- p.59 -->

CHAPTER 4 Air foil and Wing /Ta il Geome try Selection 59 
Fig. 4.4 Effect of cam ber on separ ation. 
A flat board at an angle to the onco ming air will produce lift. However, 
the air going over the top of the flat "airfoil" will tend to separate from the 
surface, thus disturbing the flow and therefore reducing lift and greatly 
increasing drag (Fig. 4.4) . Curving the airfoil (i.e., camber) allows the 
airflow to remain attached, thus increasing lift and reducing drag. The 
camber also increases lift by increasing -the circulation of the airflow. 
In fact, an airfoil with camber will produce lift even at zero angle between 
the chord line and the oncoming air ("angle of attack") . For a cambered airfoil 
there is some negative angle at which no lift is produced, the "angle of zero 
lift." As a rule- of-thumb, this negative angle is approximately equal in degrees 
to the percent camber of the airfoil. 
Odd as it sounds, an airfoil in two-dimensio nal inviscid flow does not 
experience any drag due to the creation of lift. The pressure forces produced 
in the generation of lift are at right angles to the onco ming air. All twodimensional airfoil drag is produced by skin friction and pressure effects 
resulting from flow separation and shocks. It is only in three- dimension al 
flow that drag due to lift is produced. 
The airfoil section lift, drag, and pitching moment are defined in nondimensional form in Eqs. (4. 1- 4.3). By definition, the lift force is perpend icular 
to the flight direction while the drag force is parallel to the flight direction. 
The pitching moment is usually negative when measured about the aerodynamic center, implying a nose- down moment. Note that two-dimensio nal 
airfoil characteristics are denoted by lowercase subs cripts (e.g., Cz) whereas 
the three- dimensional wing characteristics are denoted by uppercase subscripts (e.g., Cr). 
Section lift coefficient: 
Section drag coefficient: 
C _ Section lift 1 - qc 
Section drag Cd =
----qc 
(4. 1) 
(4.2)


<!-- p.60 -->

60 Airc raf t Des ign: A Conceptua l Approach 
Section moment coefficient: 
where 
c = chord length 
Section moment Cm = -------qc2 
q = dynamic pressure = p V2 /2 
a = angle of attack 
Cta = slope of the lift curve = 2'1T (theo retical thin airfoil) 
(4.3) 
When calculating any momen t, one has to choose which point to use as 
the reference loca tion. There is a poi nt on any airfoil about which the pitching moment remains nearly constant as the angle of attack is changed. This 
called the "aerod ynamic center" and is usua lly close to a point 25% back 
from the airfoil leading edge. We call this the "quarter -chord" point and 
choose it as our reference location for airfoil lift, drag, and pitchingmoment data. 
Because the pitching moment is almost independent of angle of attack 
about the quarter-chord, the derivative of pitching moment with respect to 
angle of attack (or lift) is near zero. When we take the derivative in our stability equations, those const ant moment terms disappear-a nice result that 
simplifies those complicated equatio ns. This is the very reason that we 
choose the quarter- chord loca tion as the reference for airfoil moments. 
The aerod ynamic center is not the same as the airfoil's center of pressure, 
the location where the vertical forces balance. The center of press ure is 
usually behind the aerodynamic center, and it moves back and forth as the 
angle of attack is changed. This makes it a poor choice for a reference 
loca tion. The center of pressure is sometimes called the "center of lift" (an 
obs olete term) and should never be confused with the aerod ynamic center. 
Here is another common source of confusion -the pitching moment 
itself is not usua lly zero around the quarte r-chord poi nt, just its derivative. 
Whatever pitching moment the airfoil has, measured around the quarterchord, it remains the same as angle of attack is changed. This holds true 
until high angles of attack where the flow sepa ration leading to stall causes 
the center of pressure to move forward or rearward, leading to nose-up or 
nose- down moments. 
Only symmetrical airfoils, or those carefully designed with this in mind, 
will have both pitching moment and moment derivative equal to zero 
about the quarte r-chord. 
The statement that the pitching moment is almost independent of angle 
of attack about the quarter- chord is actually true only in sl ower subsonic 
flight. At supersonic and even higher subsonic speeds, the true aerodynamic 
center moves rearward, migrating from the 25% point to around 35% or even 
40% of chord. The center of pressure moves rearward as well, causing a


<!-- p.61 -->

Lift 
CHAPTER 4 Air foil and Wing /Ta il Geome try Sel ecti on 61 
Pit ching moment 
cm ab ou t ai rfoi l 
qua rter -chor d 
(+) 
Un sta ble brea k 
( -) Sta ble break 
Dr ag polar 
La minar 
buck et 
Conventi onal 
air foil polar 
Cd 
Fig. 4.5 Airfoil li ft, pitch ing mom ent, and drag. 
nose- down pitching moment that must be corrected for some how. This will 
be discussed later. 
Lift, drag, and pitchin g-moment characteristics for a typical airfoil are 
shown in Fig, 45. The illustration on the left is common ly called the "lift 
curve" although it is most ly straight. Airfoil lift changes linearly with angle 
of attack, up to an angle near stall where flow sepa ration starts to occur. 
The pitching moment in the middle graph is nearly cons tant because we 
are delibera tely measuring it about the quarter-chord point. It is only near the 
stall angle that the moment "breaks" up or down., depending upon the shape 
of the airfoil itself. 
Sometimes we plot the pitching -moment coefficient vs the lift coefficient 
rather than the angle of attack This gives a better picture of how the aircraft 
will react in flight. Near the stall this can cause confusing loops in the line as 
the lift drops down while moment breaks one way or the other. 
As shown in the illustration on the right, we normally plot drag coefficient vs lift coefficient, not vs angle of attack as one might imagine. The 
resulting curve is called a "drag polar" because it resembles a parabola. In 
the case of three- dimensional wing data, the mathematical parabolic shape 
is actually obtained from a theoretical drag due to lift calculation, but for twodimensional airfoil data, there is no such thing as drag due to lift. Instead, this 
two-dimensional airfoil drag polar curve results entirel y from airflow sepa ration effects. This is commo nly confused. 
This illustration shows the lift coefficient on the vertical axis, matching 
the orientation of the lift-c urve graph. It is equally common to show the 
drag polar with the drag coefficient as the vertical axis, creating a 
U-sh aped plot. 
Airfoil characteristics are stro ngly affected by the Reynolds number at 
which the airfoil is oper ating. Reynolds number, the ratio between the 
dynamic and the viscous forces in a fluid, is calculated as airflow veloc ity V


<!-- p.62 -->

62 Aircr aft Desi gn: A Concept ual Approach 
times the leng th the fluid has traveled down the surface l, multiplied by the 
ratio of fluid dens ity to fluid viscos ity p/ /L A typical aircraft wing operates at 
a Reynolds number of about one to ten million, depe nding on the aircraft's 
size and speed. 
The Reynolds number stro ngly influ ences the parasitic drag coefficien t, 
whether the flow will be laminar or turbulent, and when and where flow separation will occur. This is impor tant-y ou cannot use airfoil data obtained at 
one Reynolds number and apply it to an airplane that will be flying at a very 
different Reynolds number. It isn't a matter of simple scaling. At widely 
different values of Reynolds number, an airfoil will act like two different 
airfoi ls! 
The drag polar in Fig. 4.5 also illustrates the so- called laminar bucket, 
shown dotted. (It looks more like a bucket when plotted with the drag coefficient as the vertical axis.) If an airfoil is designed to maintain a lot of laminar 
flow, it will have subs tantially less drag, as long as it is oper ating near its 
design lift coefficient. At higher or lower lift coefficients the flow will 
become turbulent or even separate, causing higher drag. This creates the 
characteristic "bucket" shape. 
Laminar flow is very dependent upon the actual surface smoothnes s. Dirt, 
rain, or insect debris on the leading edge can cause the flow to become turbulent, causing the bucket to disappear. The drag becomes much higher, and 
the lift and pitching moment are also affected. In certain early canard homebuilt designs using laminar flow airfoils, entering a light rainfall caused the 
canard's airflow to become turbulent, reducing canard lift and causing the 
aircraft to pitch downward. This scary effect was fixed with less sensi tive 
airfoils. 
In the past, the aircraft designer would select airfoils from a "catalog," 
most likely the famous book by Abbot and Von Doenhoff. [7) Airfoil selection 
would consider aerod ynamic factors such as the airfoil drag during cruise, 
stall behavior, and pitching-moment characteristic s. Selection would also 
consi der the thickness available for structure and fuel as well as the ease of 
manufacture. Designers, then and now, sometimes get "comfortable" with 
a certain airfoil and reuse it for many different airplane designs. 
Various typical airfoils are shown in Fig. 4.6. The early airfoils were developed mostly by trial and error. In the 19 30s, the NACA developed a widely 
used family of mathematic ally defined airfoils called the "four- digit" airfoils. 
In these, the first digit defined the percent camber, the second defined the 
location of the maximum camber, and the last two digits defined the airfoil 
maximum thickness in percent of chord. While rarely used for wing design 
today, the uncambered four- digit airfoils are still common ly used for tail 
surfaces of subsonic aircraft.


<!-- p.63 -->

CHAPTER 4 Air foil and Wing /Ta il Geo metry Sel ecti on 63 
Early 
Wright 19 08 
c== Bleriot 
c ---RAF-6 
c=:::::--.... 
Gottingen, 398 
Clark Y 
c ====-Munk M-6 
NACA 
c 
001 2 (4 Dig it) 
c 24 12 (4 Dig it) 
c :::::::..--.... 
4412 (4 Dig it) 
c: ====---=230 l 2 (5 Dig it) 
64 AOl 0 (6 Dig it) 
65 A008 (6 Dig it) 
Fig. 4.6 Typica l airf oils. 
Modern 
c:===::----... 
Lissa man 77 69 
c ==--====Ga (W)- 1 
c :::....... 
Ga -041 3 
Liebeck L 10 03 
C-5A ("Pea ky") 
Su per crit ical 
The NACA five-digit airfoils were developed to allow shifting the pos ition 
of maximum camber forward for greater maximum lift. The six-se ries airfoils 
were designed for increased laminar flow and hence reduced drag. Six-series 
airfoils such as the 64A series are still widely used as a starting point for high 
speed wing design. The Mach 2 F- 15 fighter uses the 64A airfoil modified 
with camber at the leading edge. Geom etry and characteristics of these 
classic NACA airfoils are summa rized in[2l . 
Other airfoil families include the lamina r-flow airfoils pioneered by 
F. X. Wortmann, Richard Eppler, and Robert Liebeck. There are also the 
NASA Supercr itical airfoils developed by Richard Whitcomb and others, 
and the newer NASA Natural -Laminar-Flo w (NLF) airfoils. 
However, the use of airfoil catalogs and families is becom ing a thing of the 
past. Today it is common for the aerod ynamicist on a project to desi gn 
all-new airfoils just for that design, as John Roncz did for many of Burt 
Rutan's record setting airplanes. In fact, Roncz wrote his own computer 
codes for airfoil design, starting with the methods of [?J . Even homebu ilders 
can now obtain an airfoil design computer program and use it to create 
optimal airfoils just for their design. 
Modern airfoil design is usually based upon inverse computational solutions for desired pressure or velocity distributions on the airfoil. Methods 
have been developed for designing an airfoil such that the press ure differential between the top and bottom of the airfoil quickly reaches a maximum 
value attainable without airflow sepa ration. Toward the rear of the airfoil, 
various pressure recovery schemes are employed to prevent separation 
near the trailing edge.


<!-- p.64 -->

64 Aircr af t Des ign: A Conceptual Approach 
These airfoil optimization techniques result in airfoils with substantial 
pressure differentials (lift) over a much greater percent of chord than a classical airfoil. This permits a reduced wing area for a required amount of lift, 
leading to reductions in drag and weight. Modern airfoil design methods 
can also produce pressure distributions that maintain laminar flow over 
much of the wing. These laminar flow airfoils work by having the pressure 
continuously drop from the leading edge to a position close to the trailing 
edge. This tends to "suck" the flow rearward, promot ing laminar flow-if 
bug guts don't ruin the flow. Figure 4.7 shows a typical laminar flow airfoil 
and its pressure distri bution. 
The most modern form of airfoil design actually analyzes the entire aircraft using computational fluid dynamics (CF D). The top and bottom wing 
surfaces are modeled in a way that permits the computer code to make parametric shape variations, "playing" with the geom etry until the lowest drag 
configuration is found. The airfoil is optimized, not in isolation, but as a 
part of the whole aircraft design. CFD is discussed in Chapter 12. 
There is a big problem when airfoils go fast. Since the airfoil is gene rating 
lift, the veloc ity of the air passing over its upper surface is increased. If the 
airplane is flying at just under the speed of sound, the faster air traveling 
over the upper surface will reach supersonic speeds causing a shock, as 
shown in Fig. 4.8. 
The speed at which supersonic flow first appears on the airfoil is called 
the "critical Mach" Merit· At higher speeds, the shock gets stronger. This 
causes a drag increase from the tendency of the rapid pressure rise across 
Liebeck LRl 022M 14 
c:::-- =-=-=-=-=="Roo ftop" cp 
(-) 
(+) 
Fig. 4.7 Laminar air foil.


<!-- p.65 -->

Hi gh subsonic 
flow 
M > Mcritical 
CH APTER 4 Air foil and Wing /Ta il Geome try Selection 65 
\• o 
\- "Bubble " of - su pers onic flow - 9, Sho ck-induc ed bo undar y layer 
_ _::>--->-:_::--==;;::--th-ic-kening and sepa ration 
V> >V0 
Classic airfoil 
-------. z 
"Bubble " of • - <" 
" 0 '} su perso nic flow ': 9:- Fig. 4.8 Transonic effects. 
Less BL thick ening 
and separation 
the shock to thicken or even separate the bound ary layer. This is so significant that commercial airliners generally cruise at about the critical Mach 
number, not daring to fly faster. 
This upper- surface shock also reduces lift and causes a change in the 
pitching moment. For a highly swept wing the loss of lift, which starts at 
the wing root, is forward of the center of gravity. This can result in the 
dreaded nose- down "Mach tuck ." 
A "sup ercritical" airfoil is one designed to minimize these effects. Modern 
computational methods allow design of airfoils in which the upper- surface 
shock is minimized or even eliminated by sprea ding the lift in the chordwise 
direction, thus reducing the upper- surface veloc ity for a required total lift. 
This increases the critical Mach number-a good thing. 
*'f JI Design Lift Coeff icien t 
For early concept ual design work, the designer usually relies upon existing airfoils. It simpl y isn't possi ble to optimize the airfoils for an aircraft that 
hasn't been designed yet. Instead we select from the existing airfoils, picking 
the one that comes closest to having the desired characterist ics. Later, the 
aerodynamics staff will design new airfoils just for our new aircraft. 
The first consi deration in initial airfoil selection is the "design lift coefficient." This is the lift coefficient at which the airfoil has the best lift-to- drag 
ratio (L/ D). This is shown in Fig. 4.9 as the point on the airfoil drag polar that 
is tangent to a line from the origin and closest to the vertical axis. 
There is a strong connection between airfoil camber and design lift coef ficient. Greater camber gives more lift at a given angle of attack so to obtain a


<!-- p.66 -->

66 Ai rcraft Desi gn: A Conceptu al Appr oach 
l'----t------- Cd 
Convent ional 
air foil 
La minar 
air foil 
Fig. 4.9 Design li ft coefficient. 
high design lift coefficient, there should be subs tantial camber. For the 
NACA 6-digit airfoils, the camber required in percent is about 5.5 times 
the desired desi gn lift coefficient. 
In subsonic flight a well-designed airfoil oper ating at its design lift coefficient has a drag coefficient that is little more than skin-fr iction drag. To 
maximize aerod ynamic efficienc y, the aircraft should be designed so that it 
flies most of its mission at or near the airfoil's desi gn lift coefficient. 
As a first approximation, it can be assumed that the wing lift coefficient 
CL equals the airfoil lift coefficien t Ct. In level flight the lift must equal the 
weight, so that the required design lift coefficient can be found as follows: 
W = L = qSCL - qSCt (4.4) 
(4.5 ) 
Dynamic pressure q is a function of veloc ity and altitude. By assuming a 
wing loading W/S as described later, the design lift coefficient can be calculated for the veloc ity and altitude of the key portions of the design mission. 
Note that the actual wing loading will decrease during the mission as fuel 
is burned. Thus, to stay at the design lift coefficient, the dynamic pressure 
must be steadily reduced during the mission by either slowing down, 
which is undes irable, or by climbing to a higher altitud e. This explains the 
"cruise- climb" that is often followed by an aircraft trying to maximize range. 
For airfoil selection on the initial aircra ft layout, the design lift coefficient 
can be calculated for a few key mission points as described above or can 
simply be based upon past experience (0.3-0.5 for most airpla nes) . When


<!-- p.67 -->

CHAP TER 4 Air fo il and Wing /Ta il Geome try Sel ecti on 67 
the layout is complete, optimization methods described in Chapter 19 can be 
used to find the airplane's optimal design lift coefficient. This is given to the 
aerodynamics staff as a starting poi nt for their comp utational airfoil design. 
#fJj Stall 
Stall characteristics play an impor tant role in airfoil selection. Some airfoils exhibit a gradual reduction in lift during a stall, whereas others show a 
violent loss of lift, accompanied by a rapid change in pitching moment. This 
difference reflects the existence of three entirely different types of airfoil stall. 
"Fat" airfoils (round leading edge and t / c greater than about 14%) stall 
from the trailing edge. The turbulent boun dary layer increases with angle 
of attack. At around 10 deg the boundary layer begins to sepa rate, starting 
at the trailing edge and moving forward as the angle of attack is further 
increased. The loss of lift is gradual. The pitching moment changes only a 
small amount. 
Thinner airfoils stall from the lead_ing edge. If the airfoil is of mo derate 
thickness (about 6-14%), the flow sep arates near the nose at a very small 
angle of attack, but immediately reattaches itself so that little effect is felt. 
At some higher angle of attack the flow fails to reattach, which almost 
immediately stalls the entire airfoil. This causes an abrupt change in lift 
and pitching moment. 
Very thin airfoils exhibit another form of stall. As before, the flow separates from the nose at a small angle of attack and reattaches almost immediately. However, for a very thin airfoil this "b1,1bble" continues to stretch 
toward the trailing edge as the angle of attack is increased. At the angle of 
attack where the bubble stretches all the way to the trailing edge, the 
airfoil reaches its maximum lift. Beyond that angle of attack, the flow is separated over the whole airfoil, so that the stall occurs. The loss of lift is smooth, 
but large changes in pitching moment are experienced. The three types of 
stall characteristics are depicted in Fig. 4. 10. 
Twisting the wing such that the tip airfoils have a reduced angle of attack 
compared to the root ("washout") can cause the wing to stall first at the root. 
This provides a gradual stall even for a wing with a poor ly stalling airfoil. 
Also, the turbulent wake off the stalled wing root might vibrate the horizo ntal 
tail, notifying the pilot that a stall is imminent. 
In a similar fashion, the designer might elect to use different airfoils at the 
root and tip, with a tip airfoil selected that stalls at a higher angle of attack 
than the root airfoil. This provides good flow over the ailerons for roll 
control at an angle of attack where the root is stalled. 
If different airfoils are used at the root and tip, the designer must develop 
the intermediate airfoils by interpolation (discussed later) . These intermediate airfoils will have section characteristics some where between those of the 
root and tip airfoils and can also be estimated by interp olation. This interpolation of section characteristics does not work for modern supercri tical or


<!-- p.68 -->

68 Ai rcraf t Desi gn: A Conceptu al Appr oach 
Trailing edge Leading edge 
r- Sepa ration bubble Th in air foil 
e::: ::---- "' 
-Ws'>'s- Separ ated 
-.22. flow 
(+) 
(-) 
I 
I 
I 
cm 
(+) 
a 
(-) 
(Pit ching mome nts ar e ab out air foil qua rter -chor d point ) 
Fig. 4. 10 Types of stall. 
lamina r-flow airfoils. Estimation of the section characteristics in those cases 
must be done computationa lly. 
Stall characteristics for thinner airfoils can be improved with various 
leadin g-ed ge devices such as slots, slats, leading- edge flaps, Krueger flaps, 
and active methods (e.g., suction or bl owing) . These are discussed in the 
aerod ynamics chapter. 
Wing stall is direct ly related to airfoil stall only for high-aspect- ratio, 
unswept wings. For lower -aspect- ratio or highly swept wings the thre edimensional effects dominate stall characteristics, and airfoil stall characteristics can be ess entially ignored in airfoil selection. 
Pitching moment must also be considered in airfoil selection. Horizontal 
tail or canard size is direct ly affected by the magnitude of the wing pitching 
moment to be balanced. Some of the supercritical airfoils use what is called 
"rear-lo ading" to increase lift without increasing the region of supersonic 
flow. This produces an excellent L / D, but can cause a large nose- down pitching moment. If this requires an excessi ve tail area, the total aircraft drag 
might be increased, not reduced . 
.m Airf oil Th ickness Ratio 
Airfoil thickness ratio has a direct effect on drag, maximum lift, stall 
characteristics, and structural weight. Figure 4. 11 illustrates the effect of


<!-- p.69 -->

CHAPTER 4 Air foil and Wing /Ta il Geom etry Selec ti on 69 
thickness ratio on subsonic drag. The drag increases with increasing thickness due to increased sepa ration. 
Figure 4. 12 shows the impact of thickness ratio on critical Mach number, 
the Mach number at which superso nic flow first appears over the wing. A 
supercritical airfoil tends to minimize shock formation and can be used to 
reduce drag for a given thickness ratio or to permit a thicker airfoil at the 
same drag level. 
The thickness ratio affects the maximum lift and stall characteristics primarily by its effect on the nose shape. For a wing of fairly high aspect ratio 
and moderate sweep, a larger nose radius provides a higher stall angle and 
a greater maximum lift coefficient, as shown in Fig. 4. 13. 
The reverse is true for low-aspect- ratio, swept wings, such as a delta wing. 
Here, a sharper leading edge provides greater maximum lift due to the formation of vortices just behind the leading edge. These leading- edge vortices 
act to delay wing stall. This three-dimensional effect is discussed in the 
aerodynamics chapter. 
Thickness also affects the structural weight of the wing. Statistical 
equations for wing weight show that the wing structural weight varies approximately inversely with the square-root-of -the-t hickness ratio. Halving the 
thickness ratio will increase wing weight by about 41%. The wing is typically 
about 15% of the total empty weight, so that halving the thickness ratio 
would increase empty weight by about 6%. When applied to the sizing 
equation, this can have a major impact. 
0.0100 
0.0075 
:-gc 
0 
V1 
..c 
::; 
0.0050 t] 
0.0025 
5 10 15 
tic (%) 
Fig. 4. 11 Effect of t/c on drag . 
20 25


<!-- p.70 -->

70 Ai rc raf t Des ign: A Conceptual Approach 
1.0 
0.9 
-'U 
- 0.8 
< 
0.7 
2.0 
1.5 
>< 
e u 1.0 
0.5 
5 10 
(Zero li ft) 
15 
tic (%) 
Su percri tical 
641 XXX 
20 
Fig. 4. 12 Effect of t/ c on critic al Mach nu mber. 
5 10 15 
tic (%) 
Fig. 4. 13 Effect of t/ c on maxi mum li ft. 
20 
NACA 
25 
25


<!-- p.71 -->

CHAPTER 4 Air fo il and Wing /Ta il Geome try Selec tion 71 
0. 18 .--_-----(-I -----, 
• 1 
- 0.12 e I + 
O I 
·- . 
j 0.06 , . / H;T'""" "";" .' > 
• 
• 
1 2 3 
Design Mach numb er (maxi mum ) 
Fig. 4. 14 Thic kness ratio hi storica l trend. 
4 
For initial selection of the thickness ratio, the historical trend shown in 
Fig. 4.14 can be used. A supercritical airfoil can be about 10% thicker (i.e., 
conventional airfoil thickness ratio times 1.1) than the historical trend. 
Frequently the thickness is varied from root to tip. Because of fusela ge 
effects, the root airfoil of a subsonic aircraft can be as much as 20-60% 
thicker than the tip airfoil without greatly affecting the drag. This is very beneficial, resulting in a structural weight reduction as well as more volume for 
fuel and landing gear. This thicker root airfoil should extend to no more than 
about 30% of the span. 
Sometimes the opposi te is done. If the wing is thicker out near the tips, it 
is more likely to stall at the root. This helps the pilot keep control of the 
airplane during a stall and is espec ially useful for aerob atic aircraft where 
you cannot use twist to fix tip stall. When you are flying upside down, 
normal twist makes the tips stall soon er! 
+,f ff Other Airf oil Consi der ations 
Another impor tant aspect of airfoil selection is the intended Reynolds 
number. Each airfoil is designed for a certain Reynolds number. Use of an 
airfoil at a greatly different Reynolds number (half an order of magnitude or 
so) can produce section characteristics much different from those expected. 
This is espe cially true for the laminar-flow airfoils and is most crucial 
when an airfoil is operated at a lower-than-desi gn Reynolds number. In the 
past this has been a problem for homebuilt and sailplane designers, but


<!-- p.72 -->

72 Ai rcraf t Des ign: A Concept ual Appr oa ch 
there are now suitable airfoils designed espe cially for these lower Reynolds 
number aircraft. 
The laminar airfoils require extrem ely smo oth skins as well as exact 
con trol over the actual, as-ma nufactured shape. These can drive the cost 
up significantly. Also, the camo uflage paints used on military aircraft are 
,rough compared to bare metal or compo site skins, This must be considered 
before sel ecting certain airfoi ls. 
While an understanding of the factors impor tant to airfoil selection is 
impor tant, an aircraft designer should not spend too much time trying to 
pick exactly the right airfoil in early conceptual design, Later trade studies 
and analytical design tools will determine the desired airfoil characteristics 
and geom etry. For early conce ptual layout, the selected airfoil is impor tant 
mostly for determining the thickn ess available for structure, landing gear, 
and fuel. Don't waste a lot of time on picking the perfect airfoil -it'll 
change soon. 
Appe ndix D provides geom etry and section characteristics for a few airfoils useful in conce ptual design. For swept-wing supersonic aircraft, the 
NACA 64A and 65A sections are good airfoils for initial design. The appendix describes a super critical sec tion suitable for transpo rts and other highsubsonic aircraft, along with a typical moder n NA SA sec tion for general 
aviation. A few specialized airfoils are provided for other applicat ions. 
The airfoils presented in Appe ndix D are not being recommended as the 
"best" sections for those applications, but rather as reasonable airfoils with 
which to start a conce ptual design. Again, l?l is highly recommended. Links 
to airfoil data websites are available on the author's website, www.aircraftde sign.com. 
Wi ng Geom etry 
The "reference" wing is the basic wing geom etry used to begin the layout. 
Its name comes from its use as the reference area for aerod ynamic coefficients. Figures 4. 15 and 4. 16 show the key geom etric parameters of the reference wing, which is also called the "trap ezoidal" or "trap " wing due to its 
obvious shape. 
The reference wing is partly fictitious. It extends through the fuselage to 
the aircraft centerline and has its tip squared off even if the real wing is 
rounded. The reference wing area (S) includes the part of the reference 
wing that sticks into the fuselage, plus the missing areas where the wingtips 
have been rounded. 
Another fiction-t he root airfoil for the reference wing is the airfoil of the 
trapezoidal reference wing at the centerline of the aircraft, not where the actual 
wing connects to the fuselage. But remember, this is just the reference wing, 
used to nondimensionalize the aerod ynamic coefficients. You don't build it. 
The actual reference wing area S is calculated from the required wing 
loa ding W / S and can be determined only after the takeoff gross weight is


<!-- p.73 -->

CH APT E R 4 Air foil and Wing /Ta il Geome try Selecti on 73 
S = Reference wing ar ea 
C = Chor d (distance L.E. to T.E.) 
A = Aspect ratio = b2!S 
tic = Air foil thick ness ratio 
(maxi mum thick ne ss/ch ord) 
A, = Taper ratio = C tip/C root 
b =S pan 
Gi ven WIS, A, A: 
S = W!(W!S) 
b = ,,r;r:s 
C root = 2 · S/[b(l + ?..)] C tip = A· C roo_t 
1------1 Ctip 
Fig. 4. 15 Wing geome try. 
h/2 
J 
determined (see Chapters 5 and 6). The shape of the reference wing is determined by its aspect ratio, taper ratio, and sweep. The initial selection of these 
parameters is discussed in the following subchapters. Their final determination is done using optimization methods after the initial design layout 
is completed. 
A 
LE 
\ Ai rcraft centerl ine 
\ 
\ 
Fig. 4. 16 Wing sweep (A).


<!-- p.74 -->

74 Aircr aft Des ign : A Conc ept ual Approa ch 
Sweep is a key parameter for wing geome try and is usua lly denoted either 
by Greek capital letter Ll (De lta) or A (Lambda) .* There are two impor tant 
sweep angles, as shown in Fig. 4. 16. The leading- edge sweep is the angle of 
concern in superso nic flight. To reduce drag, it is common to sweep the 
leading edge behind the Mach cone. 
The sweep of the quarte r-chord line is the sweep most related to subsonic 
flight. t It is very impo rtant to avoid confusing these two sweep angles. The 
equation at the bottom of Fig. 4. 16 allows converting from one sweep 
angle to the other. For a vertical tail, first double the aspect ratio (A). 
Airfoil moments are measured about the quart er- chord point where the 
subsonic airfoil pitching moment is essen tially const ant with changing angle 
of attack, i.e., the airfoil aerod ynamic center. A similar point can be found for 
the complete trapezoidal wing, where the pitching moment doesn't change 
with angle of attack. This is based on the concept of the "mean aerodynamic 
chord," as shown in Fig. 4. 17. 
! 
Cr oat 
Mean aer odyn amic 
-----• chor d (c) 
c = (2/3) C root (1 +A, + A,2)/(1 + /l) 
Y = (b/6) [(1 + 2/l)/(l + ll)] (assu ming lif t is pr opor tional to ch ord) 
Y mus t be doubl ed for a ver tical ta il 
Fig. 4. 17 Mean aer odynamic chor d. 
* From the top, a low aspect ratio swept wing looks like the letter <'.). (Delta ) whereas a high aspect 
ratio swept wing sweep looks like a A (Lambda ). This book uses A for sweep, mostly. 
t Actually, it appears that the sweep most related to subsonic flight characteristics is the sweep of a 
line connecting the airfoils at their point of maximum thickness. Use of the quarter-chord is probably 
an ancient approximation, more suitable in the days when airfoils had their point of maximum thickness far forward. The difference is trivial.


<!-- p.75 -->

CHAPTE R 4 Air foil and Wing /Ta il Geom etry Selec tion 75 
The mean aerod ynamic chord (MAC) is simpl y some wing chord c 
located at some distance Y from the centerline. The MAC is often shown 
as a letter c topped with a horizont al line or bar that resembles a chord 
and is therefore called c-bar. Simil arly, its distance from the center line is 
often denoted by the letter Y topped with a line and called Y-bar. 
What makes the MAC special is that it some how acts as if all the area of 
the wing is conc entrated on that chord. The entire wing has its aerod ynamic 
center at approximately the same percent location on the mean aerod ynamic 
chord as that of the airfoil alone. In subsonic flight, this is at the quarterchord point, i.e., 25% back from the leading edge of the MAC. If the total 
wing pitching moment is measured around that loca tion, it doesn't change 
when the angle of attack chang es. This is the subsonic aerod ynamic center 
of the whole wing. 
This is a critical parameter for initial aircraft design. The designer uses 
the subsonic aerod ynamic center, the X-location of the quarter- chord of 
the mean aerodynamic chord, to position the wing to attain the desired 
level of stability. This location is also a key parameter in stab ility calculations 
and is so important that it is common ly listed out with the other wing information on a drawing. 
Figure 4. 17 illustrates both graphical and analytical methods for finding 
the mean aerodynamic chord of a trapezoidal -wing planform. Note that for 
a vertical tail there is one slight change to the equations in Fig. 4.17. The 
spanwise location of the MAC (Y-bar) must be doubled for a vertical tail. 
This occurs because the total area of the vertical tail is half the value of a horizontal surface with the same trapezoid al shape. All other calculations are 
identical. Wing layout will be further discussed in Chapter 7. 
In supersonic flow, the wing aerod ynamic center, like that of an airfoil, 
moves back to about 35 -40% of the mean aerod ynamic chord. This will be 
considered in Chapter 16. 
*'fl# Aspect Ratio 
The first to investigate aspect ratio in detail were the Wright Brothers, 
using a wind tunnel they constructed themsel ves. They found that a long, 
skinny wing (high aspect ratio) has less drag for a given lift than a short, 
fat wing (low aspect ratio) . This is obvious if you look at birds. The ones 
that effortles sly glide have long wings . Those with shor t, stubby wings, 
while having greater maneu verabil ity, seem to work a lot harder to stay in 
the air. 
Because most early wings were rectangular in shape, the aspect ratio was 
initially defined as simpl y the span divided by the chord. For a tapered wing, 
the aspect ratio is defined as the span squared divided by the area (which 
defaults to the earlier definition for a wing with no taper) . 
Why is aspect ratio so impor tant? When a wing is generating lift, it has a 
reduced pressure on the upper surface and an increased pressure on the


<!-- p.76 -->

76 Aircr af t Des ign : A Conceptual Approach 
Lower 
pressu res 
/ Hi gher 
pressu res / 
Distribut ed 
Fig. 4. 18 "E sca pe" of air around the wing tip. 
lower surface. The air would like to "escape" from the bottom of the wing, 
moving to the top. This is not possi ble in two-dimensional flow unless the 
airfoil is leaky (a real problem with some fabric wing materials unless properly treated) . However, for a real, three-dimensional wing, the air can escape 
around the wing tip (Fig. 4. 18). 
Air esca ping around the wing tip lowers the pressure difference between 
the upper and the lower surfaces. This reduces lift near the tip. Also, the air 
flowing around the tip flows in a circular path when seen from the front and, 
in effect, pushes down on the wing. Strongest near the tip, this reduces the 
effective angle of attack of the wing airfoils. This circular, or "vortex, " flow 
pattern continues downstream behind the wing. The ene rgy asso ciated 
with creating these "trailing vortices" can be tremendous and represents a 
drag due to lift force exerted on the wing. 
A wing with a high aspect ratio has tips farther apart than an equal 
area wing with a low aspect ratio. Therefore, the amount of the wing affected 
by the tip vortex is less for a high-aspect- ratio wing than for a 
low- aspect- ratio wing, and the streng th of the tip vortex is reduced. Thus, 
the high-aspect- ratio wing does not experience as much of a loss of lift and 
increase of drag due to tip effects as a low- aspect- ratio wing of equal area. 
It is actually the wing span that determines the drag due to lift. A simple 
derivation based on the equations in Chapter 12 will prove that the drag 
due to lift is prop ortional to the inverse of the square of the span. Aspect 
ratio per se has nothing to do with it. However, when loo king at various 
options for the wing planform, the wing area is usua lly held cons tant 
unless widely different aircraft concepts are being evaluated. When wing 
area is held constant, the wing span varies by the square root of the 
aspect ratio, so the drag due to lift becomes inversely propor tional to 
aspect ratio. 
Another result of the air esca ping around the wing tip is an outward flow 
benea th the wing and an inward flow above it, shown in the bottom of


<!-- p.77 -->

CHAP TER 4 Air foil and Wing /Ta il Geome try Selec tion 77 
fig. 4. 18. This actually changes local flow directions and should be considered when orient ing nacelles or stores on the wing. 
As shown in Fig. 3.5, the maximum subsonic L / D of an aircraft increases 
approximately by the square root of an increase in aspect ratio (when wing 
area and Swet/Sref are held constan t). On the other hand, the wing weight 
also increa ses with increasing aspect ratio, by about the same factor. Once 
again, design is a tradeoff. 
Another effect of changing aspect ratio is a change in stalling angle. 
Because of the reduced effective angle of attack at the tips, a lower-aspectratio wing will stall at a higher angle of attack than a higher- aspect- ratio 
wing (Fig. 4. 19). This is one reason why tails tend to be of lower aspect 
ratio. Delaying tail stall until well after the wing stalls ensures adequate 
control. 
Conversely, a canard can be made to stall before the wing by making it a 
very high-a spec t-ratio surface. This prevents the pilot from stalling the wing 
and is seen in several canarded homebui lt designs. 
Later in the design process, the asp_ect ratio will be determined by a trade 
study in which the aerod ynamic advantages of a higher aspect ratio are 
balanced against the increased weight. For initial wing layout, the values 
and equations provided in Table 4. 1 can be used. These were determined 
through statistical analysis of a number of aircraft, using data from l6l . 
Sailplane aspect ratio was found to be directly related to the desired glide 
ratio, which equals the L / D. Propeller aircraft showed no clear statistical 
trend, so average values are presented. Jet aircraft show a strong trend of 
aspect ratio decreasing with increasing Macl\ number. This is proba bly 
Fig. 4. 19 Effect of aspect ratio on li ft.


<!-- p.78 -->

78 Air c raft De sign : A Concep tual Appro ach 
Table 4. 1 Aspect Ratio 
Equ iva lent aspect ratio = wing span squar ed/( wing and 
canar d areas) 
Equ ival ent Aspect Ratio 
Sa il plane 0. 19 (best L/D) l.3 
Prope ller Aircraft ! Equiv al ent Aspect Ratio 
Homebuil t 
Gener al avi ation- single engine 
Gener al aviatio n-twin engine 
Agricu ltur al air craft 
Twin tur bopr op 
Flying boat 
Jet Ai rcraft 
Jet trai ner 
Jet fighter (dogfig hter) 
Jet fig hter (other ) 
Mil itary cargo /bomb er 
Jet tra nsport 
6.0 
7.6 
7.8 
7.5 
9.2 
8.0 
Equ iva lent Aspect Ratio = aM-ax 
4.7 37 -0 .979 
5.41 6 -0 .622 
4. 11 0 -0 .622 
5.570 -1 .075 
7.5 0 to 10 0 
because of drag- due-to- lift bec oming relatively less impor tant at higher 
speeds. Desi gners of high-speed aircraft thus use lower- aspect- ratio wings 
to save weight. 
Note that, for statistical purposes, Table 4. 1 uses an equivalent wing area 
that includes the canard area when defining the aspect ratio of an aircraft 
with a lifting canard. To determine the actual wing geom etric aspect ratio, 
it is necessa ry to decide how to split the lifting area between the wing and 
canard. Typically, the canard will have about 10-25% of the total lifting 
area, so the wing aspect ratio becomes the statistica lly determined aspect 
ratio divided by 0.9-0.75. 
It is fairly common for the wing aspect ratio to be ultimatel y determined 
by a climb requirement, espec ially in the critical case of an engine failure for a 
multi-engine aircraft. If thrust is limited, a required rate of climb may be 
attained if the drag is reduced by an increase in aspect ratio. When the 
DC- 10 -20 was being developed, it was found that the weight increase over 
earlier models reduced the engine-out rate of climb below the FAA-req uired 
values. l8l To fix this, the wing was extended by 10 ft {3 m}. 
Cons ideration of the effect of aspect ratio on rate of climb requires 
more detailed analysis than we can do before the initial airplane layout is 
completed (see Chapters 12 and 17). For now, the trends of Table 4. 1 
are reasonab le.


<!-- p.79 -->

CHAPTER 4 Air foil and Wing /Ta il Geome try Sel ecti on 79 
#ff J Wing Sweep 
Wing sweep seems like a bad idea. It increases wing weight, reduces lift by 
the cosin e of the sweep angle, and makes the ailerons and flaps work poorly. 
Sweep also makes it more likely that the wingtips will strike the ground in a 
bad landing. For a low speed airplane, espe cially propeller-po wered, the best 
sweep is usually zero. 
But most high-speed aircraft have swept wings, and with good reason. 
Wing sweep reduces the adverse effects of transonic and supersonic flow. 
Theoretically, shock formation on a swept wing at high subsonic speeds is 
determined not by the actual velocity of the air passi ng over the wing, but 
rather by the air velocity in a direction roughly perpendicular to the 
leading edge of the wing. The distance from leading edge to trailing edge is 
shorter when measured perpendicular to the leading edge, so that its velocity 
appears slower, thus the shocks don't form. This odd result, first applied by 
the Germans during W odd War II, increases the speed at which shocks first 
form (called the Critical Mach Numbt::r). 
At supersonic speeds the loss of lift and increase in drag asso ciated with 
supersonic flow can be reduced by sweeping the wing leading edge aft of the 
Mach cone angle [arcsin (l /Mach #)]. This also improves drag -due-t o-lift at 
supersonic speeds, as will be explained in Chapter 12. 
Figure 4.20 shows a historical trend line for wing leading-edge sweep vs 
Mach number. Note that sweep is defined aft of a line perpendicular to the 
flight direction, while the Mach angle is defined with respect to the flight 
Ol 
<II 
"'O 
90 
I 60 
Q_ 
<II 
<II 
$: "' 
<II 
Ol 
"'O 
<II 
°' 
.!:: 
"'O 30 
ro 
His torica l trend line 
I I,, - ,. ;: _: -----"'"'.:lr.. ==-=-1 
I- . . 
--If 90-a rcsin (1 /Mach no .) 
: I 
2 
Maxi mum Mach numb er 
Fig. 4.20 Wing sweep historical trend . 
3 4


<!-- p.80 -->

80 Air c raf t De sign: A Conceptual Approach 
direct ion. Thus, the line labeled "90- arcsin (l/M ach no.)" is the wing sweep 
required to place the wing leading edge exactly on the Mach cone. 
The histo rical trend differs from this theo retical result for two reas ons. In 
the high-s peed regime, it becomes struc turally impract ical to sweep the wing 
past the Mach cone. At Mach 2.5 the wing would have to be swept over 66 
degrees. A more- practical wing sweep like 60 degrees puts the leading edge 
in front of the Mach cone. In other words, the leading edge is supersonic. 
To avoid a large drag penalt y, it is typical at such speeds to use sharp or 
nearly sharp airfoils. The alternative, using a rounded leading edge and 
accept ing a large drag penalty, is sometimes forced by thermal issues 
espe cially for reent ry vehicles like the Space Shuttle. 
At Mach one and below, selecting the wing sweep to equal the Machcone angle would suggest using zero sw eep. However, at a high subsonic 
speed the acceleratio n of the flow over the top of the wing leads to loca l 
supersonic flow and shocks. To avoid this, the wing is swept such that the 
airflow over the top of the wing stays subsonic when measured perpendicular 
to the leading edge. 
The exact wing sweep required to avoid shocks depends upon the 
selected airfoil, thickness ratio, taper ratio, and of course, the desired flight 
Mach number. Because wing weight increases with wing sweep, a tradeoff 
is always involved. 
We normally design subsonic aircraft so that the desired cruise speed is 
the Mach number at which shocks first form, i.e., the Critical Mach 
Number. If the plane flies a little faster, the drag goes up a lot because the 
shock gets stronger. This actually sets the wing sweep for most airliners. 
To proper ly set the wing sweep we must consider the impacts of structural weight, drag, lift, and other factors. These are difficult to calculate 
until an initial layout is completed and some powerful analysis tools can be 
employed. To make that initial layout, the trend line of Fig. 4.20 is reasonable. 
The dots are various actual airplanes. The outlier point at Mach 2 and "'3 0 
deg. sweep is the F- 104. This used a leading edge so sharp that protec tive 
cuffs had to be attached after landing, much like the blade guards used by 
figure skaters. 
There is no theoretical difference between sweeping a wing aft and 
sweeping it forward. In the past , wings have been swept aft because of the 
structural divergence problem asso ciated with forward sweep. With the use 
of compo site materials, this can be avoided for a small weight pena lty. See 
Chapter 22. 
Also, there is no reason why one cannot sweep one wing aft and the 
other wing forward, creating an "oblique wing." This arrangement produces 
unusual control responses, but a computerized flight control system can 
easi ly provide normal handling qualit ies. The oblique wing also tends to have 
lower wave drag due to a better volume distribution (see Chapters 8 and 22) . 
There are other reasons for sweeping a wing. For example, the fuselage 
layout may not otherwise allow locating the wing carry-thro ugh structure


<!-- p.81 -->

CHAP TER 4 Air foil and Wing /Ta il Geome try Sel ecti on 81 
at the correct place for balancing the aircraft. Canarded aircraft with pusher 
engines are freque ntly tail-heavy, requiring wing sweep to move the aerodynamic center back far enough for balance. This is why most canard pushers 
have swept wings. 
Wing sweep improves lateral stability. A swept wing has a natural dihedral effect. In fact, it is frequent ly necessa ry to use zero or negative dihedral 
on a swept wing to avoid excessive stability. Also, an aft-swept wing with 
some washout has additional pitch stability because the center of gravity 
must be moved forward for balance. 
If an aircr aft has its vertical tails at the wing tips, sweeping the wing will 
push the tails aft, increasing their effectiveness. This is also seen on many 
canard pusher aircraft. 
The wing sweep and aspect ratio together have a strong effect on the 
wing-alone pitch-up characterist ics. "Pitch-up" is the undesirable tendency 
of some aircra ft, upon reaching an angle of attack near stall, to sudden ly 
and uncontrolla bly increase the angle of attack. The aircraft continues pitching up until it stalls and departs totally out of con trol. The F- 16 fighter 
requires a computerized angle-of -attack limiter to prevent a severe 
pitch-up problem at about 25-d eg angle of attack. 
Figure 4.2 1 describes boundaries for pitch-up avoidance for combinations 
of wing quarter-ch ord sweep angle and aspect ratio. Pitch-up avoidance 
should be considered for military fighters, aerob atic aircraft, general aviation 
aircraft, and trainers. 
These boundaries may limit the allowable aspect ratio to a value less than 
that estimated earlier. However, Fig. 4.2 1 provides data for the wing alone. If a 
proper ly designed horizo ntal tail is used, the aspect ratio may be higher than 
that allowed by the graph. This is discussed later. Also, a large, all- moving 
canard such as that seen on the Grumman X-29 can be used to control a 
pitch-up tende ncy. However, this requires a computerized flight control 
system. 
For high-s peed flight, a swept wing is desirable. For cruise as well as 
takeoff and landing, an unswept wing is desirable. A wing of variable 
sweep would offer the best of both worlds. Variable sweep was first flighttested in the 19 50s and has been seen on operational military aircraft including the F- 111 , F-14 , B-lB , the European Tornado, and the Soviet TU-22M 
Backfire. It was proposed for the Boeing Supersonic Transpor t (SST), but 
weight pena lties resulted in the design being switched to a fixed delta 
wing-and then the whole program was cancelled. 
For design purposes, the planform for a variable- sweep aircraft should 
be developed in the unswept position and then swept to the desired 
leading-edge angle for high-speed flight. For structural reasons the pivot 
position about which the wing is swept should be near the thickest part 
of the chord, between about 30-40% of chord. Also, provisions must be 
made for smoot hly fairing the wing root in both extended and fully 
swept positions.


<!-- p.82 -->

82 Air c raf t De sign : A Concep tual Approa ch 
10 
8 
0 6 
:;:; 
.... 
u 
<lJ 
a. 
V\ 
<i: 4 
2 
NASA TN 10 93 
Incr eased pitch-up risk at 
h;7' of '1taok 
In creased stabil ity at 
high angle of attack 
20 40 60 
Quar ter chor d sweep-deg 
Fig. 4.21 Tail -off pit ch-up boundaries. 
80 
Controlling the balance of a variable- sweep aircraft is a major design 
problem. When the wing swings aft, the aerod ynamic center moves with it. 
The center of gravity also moves due to the wing movement, but not 
nearly as much as the aerod ynamic center. To balance the aircraft, either 
fuel must be pumped to move the center of gravity, or the tail must 
provide a tremendous download (or both) . Because of this balance 
problem it actually makes sense to have a variable sweep, forward swept 
wing, but that int roduces even more challenge s. 
Yet another problem with the variable- sweep wing is the weight penalty 
asso ciated with the pivot mechanism and less -than- optimal load paths. As 
shown in Table 3.1, variable sweep increases total empty weight roughly 
4%. The detailed statistical weight equations of Chapter 15 show a 19% 
increase in the weight of the wing itself if it has variable sweep. 
Wing taper ratio A is the ratio between the tip chord and the centerline 
root chord. Most wings of low sweep have a taper ratio of about 0.4 -0.5. 
Most swept wings have a taper ratio of about 0.2-0.3. 
Taper affects the distribution of lift along the span of the wing. As proven 
by the Prandtl wing theor y early in the last cent ury, the minimum drag due to


<!-- p.83 -->

CHAP TER 4 Air fo il and Wing /Ta il Geome try Selection 83 
lift (or "induced" drag) occurs when the lift is distributed in an elliptical 
fashion . For an untwisted and unswept wing, this occurs when the wing planform itself is shaped like an ellip se as shown in Fig. 4.22. This wonderful 
theoretical result was the basis of the graceful wing of the Supe rmarine 
Spitfire, a leading British fighter of World War IL 
An elliptical wing planform is difficult and expensive to build. The easiest 
wing to build is the untapered rectangular wing (A = 1. 0). However, the untapered wing has constant chord length along the span, so it has excessive 
chord length toward the tip when compared to the ideal elliptical wing. 
This "loads up" the tip, causing the wing to gener ate more of its lift toward 
the tip than is ideal. The end result is that an untwisted rectangular wing 
has about 7% more drag due to lift than an elliptical wing of the same 
aspect ratio. 
When a rectangular wing is tapered, the tip chords become shorter, alleviating the undesired effects of the constant-chord rectangular wing. In fact, a 
taper ratio of 0.45 almost comple tely eliminates those effects for an unswept 
wing and produces a lift distribution very close to the elliptical ideal 
(Fig. 4.23) . This results in a drag due to lift less than 1 % higher than the 
ideal, elliptical wing. When the weight reduction from increased taper is 
taken into acco unt, a taper ratio of about 0.4 is ideal for most unswept wings. 
A wing swept to the rear tends to divert the air outboard, toward the tips. 
Also, the greater pressures undernea th the wing at the root tend to prop agate 
to the tips, as do the reduced pressures above the wing root. These effects 
load up the tips, creating more lift outboard than for an equivalent 
unswept wing. To return the lift distribution to the desired elliptical lift distribution, it is necessa ry to increase the amount of taper (i.e., reduce the taper 
ratio ,\, so the tip chord is shorter). 
Figure 4.24 illustrates the results of NACA wind-tunnel tests to determine the taper ratio required to approximate the elliptical lift distribution 
6111 11 1 /IJ)\" 
Fig. 4.22 Ellip tica l wing .


<!-- p.84 -->

84 Air c raft Des ign- A Concep tual Approach 
1.6 
1.4 
1.2 
- 1. 0 c 
0 - :;:::; 
ro c u al 0.8 ..2 
c ro 
0.. 0.6 V1 
0.4 
0.2 
0 
0 
Root 
' ' 
0.2 0.4 
- - - - Taper ratio: A,= 0 
--- Taper ratio: A,= 0.5 
Taper ratio: A,= 1.0 
--- Ellip tic load ing 
0.6 
' ' ' ' ' ' ' ' ' 
0.8 
' ' ' ' 
Span location 
Fig. 4.23 Effect of toper on lif t dis tribution. 
1.0 
Ti p 
Toma hawk After NASA 921 
0 0 
(.)0.8 
§. 0.6 
lJ 
II 
« 
0 
·.:; 
- 0.4 
a; 
0.. 
0.2 
X29 
• 
Un twisted wing pla nforms 
with ap proxim ately ellip tica l 
lif t di stri butions 
\ / 
\,I< 
rROM t- -- .., 
I twi sted wings I 
J... ------' 
\ Sta rs hip 
\ . 
\ 
YC14 'Bj9, S3A e 'A4 
... 
FS F16 
o----------------· 
-40 -20 0 20 
Qua rter chor d sweep-deg 
Fig. 4.24 Effect of sweep on desir ed taper rati o. 
60 80


<!-- p.85 -->

CHAPTER 4 Air fo il and Wing /Ta il Geome try Selection 85 
for a swept untwisted wing. This figure can be used for a first app roximation 
of the desired taper ratio for a swept wing. However, taper ratios much lower 
than 0.2 should be avoided for all but delta wings, as a very low taper ratio 
tends to promote tip stall. 
Figure 4.24 also indicates that an untwisted wing with no taper should 
have a forward sweep of 22 deg to appr oximate an elliptical lift distribution. 
This unusual planform was the basis of the design presen ted in the first 
section as Fig. 2.6. The intent was to provide an elliptical lift distribution 
with an easy-to-con struct rectangular wing. 
Detailed aerod ynamic analysis showed that this actual ly works. Unfortunately, there was a weight increase caused by the lack of wing thickness at the 
root, compared to a conventional, tapered wing. With the leverage effect of 
the sizing equation, this design sized to a much higher takeoff gross 
weight, and therefore wound up cost ing more than a regular design! Well, 
at least it was an interesting trade study. 
The unusual Republic XF- 91 of 19 49 actu ally had reverse tapered wings . 
In other words, the wing tips had a greater chord than at the root, so that A 
was greater than one! This was appare ntly intended to reduce wing tip stalling at low speeds and, perhaps, to reduce wing-fuselage interference. It 
worked poor ly, looked really strange, added to the wing weight, and hasn't 
been attempted since. 
As mentioned above, the minimum drag elliptical wing is more expensi ve 
to build than a straigh t-taper wing. There are the extra costs of stretching 
skins to the required slight compound curvature, of fabricating ribs and 
spars with more complicated shapes, and of making the tooling to hold it 
all together while the aluminum parts are rivet-d into place. However, the 
cost penalties might go away if molded compo site const ruction is emplo yed. 
Once the molds are made, the curved shape shouldn't cost any more to fabricate. Perhaps there will be a revival of the elliptical wing providing grace, 
beauty, and reduced drag! 
+,QI Twist 
Wing twist is used to prevent tip stall and to revise the lift distribution to 
approximate an ellip se. Typically, wings are twisted between 0 and - 5 deg, 
the minus sign indicating that the lead ing edge is twisted downwa rds. 
"Geometric twist" is the actual change in airfoil angle of incidence, usually 
measured with respect to the root airfoil. A wing whose tip airfoil is at a negative (nose- down) angle compar ed to the root airfoil is said to have "washou t." 
A wing with washout will tend to stall at the root before the tip, which 
improves control during the stall and tends to reduce wing rock. 
Because of the problems of tip stall, a wing with "wash-in" is very unlik ely. 
Washout is so normal and expected that we designers get sloppy in our terminology and say "five degrees of twist" when we real ly mean "minus -five 
degrees ."


<!-- p.86 -->

86 Air c raf t De sign : A Conceptual Appr oach 
If a wing has "linear twist, " the twist angle changes in propor tion to the 
distance from the root airfoil. "Nonlinear" twists are certainly pos sible and 
proba bly more optimal, but they require soph isticated computer codes to 
achie ve the best distribution of twist from root to tip. 
"Aerod ynamic twist" is the angle between the zero- lift angle of an airfoil 
and the zero- lift angle of the root airfoil. If the identical airfoil is used from 
root to tip, the aerodynamic twist is the same as the geom etric twist. 
On the other hand, a wing with no geome tric twist can have aerod ynamic 
twist if, for example, the root airfoil is symmetric (zero-lift angle is zer o), but 
the tip airfoil is highly cambered (zero- lift angle is nonzer o). The total wing 
aerod ynamic twist equals the wing geometric twist plus the root airfoil zerolift angle, minus the tip airfoil zero- lift angle. 
When wing twist is used to reshape the lift distribution, the change in lift 
at some chord station along the span is propor tional to the ratio between the 
new airfoil angle of attack and the original one. Thus, the effect on lift distribution depends upon the original angle of attack of the wing, which in turn 
depends upon the lift coefficient at which the wing is flying. 
In other words, any attempt to optimize the lift distribution by twisting the wing will be valid only at one lift coefficient. At other lift coefficients, 
the twisted wing will not get the whole benefit of the twist optimizat ion. 
The more twist required to produce a good lift distribution at the design 
lift coeffici ent, the worse the wing will perform at other lift coefficients . It 
is for this reason that large amounts of twist (much over 5 deg) should 
be avoided. 
It is very difficult to optimize twist for an arbitrary wing planform. A computerized solution is emplo yed at large companies. For initial design purposes, historical data should be used. Typically, - 3 deg of twist provides 
adequate stall character istics. 
Twist also changes the spanwise lift distribution because it changes the 
loca l angle of attack seen by each airfoil. This has an effect on the drag due 
to lift. If the optimum taper ratio is found as in Fig. 4.24 but washout is 
used to impro ve stall characteristics, the washout reduces lift at the tips so 
that the tip chord must be increased a bit and the root chord reduced. 
This means that the taper ratio as found in Fig. 4.24 should be increased a 
bit, as shown by the dotted-line approximat ion. This is contrary to the 
wing structural effects, where a lower taper ratio is better for reducing 
weight. When the initial design layout is completed using these approximations, a detailed trade study should be conducted to optimize taper 
ratio, twist, sweep, and many other parameters. 
The wing incidence angle is the pitch angle of the wing with respect to 
the fuselage. If the wing is untwisted, the incidence is simply the angle 
between the fuselage axis and the wing's airfoil chordlines. If the wing is


<!-- p.87 -->

CHAP TE R 4 Air fo il and Wing /Ta il Geome try Selec tion 87 
twisted, the incidence is defined with respect to some arbitrarily chosen 
spanwise location of the wing, usually the mean aerodynamic chord or the 
root of the exposed wing where it intersects the fuselage. Freque ntly, the 
incidence is given at the root and tip, which then defines the twist as 
the difference between the two. 
Wing incidence angle is chosen to minimize drag at some oper ating condition, usually cruise. The incidence angle is chosen such that when the wing 
is at the correct angle of attack for the selected design condition, the fuselage 
is at the angle of attack for minimum total drag. 
For a typical, circular straight fuselage, this is often a few degrees 
nose-up, allowing the fusela ge to contribute to lift. For pass enger aircraft, 
the incidence angle must be carefully chosen to ensure that the flight 
attendants do not have to push the food carts uphill, as was the case in 
the L- 101 1! 
Wing incidence angle is ultimately set using wind-t unnel data. For most 
initial design work, it can be assumed that general aviation and homeb uilt aircraft will have an incidence of about 2 deg, transport aircraft about 1 deg, and 
military aircraft appr oximately zero. Later in the design process, aerod ynamic 
calculations can be used to check the actual wing incidence angle required 
during the design condition. 
These values are for untwisted wings . If the wing is twisted, the average 
incidence should equal these values. 
A few aircraft have been built with a variable wing incidence angle. The 
wing aft-attachment is pivoted, and the forward attachment connects to a 
powerful actuator that pushes the front of the. wing up for landing. This 
arrangement, seen on the Vought FSU Crusader aircraft, allows a short 
landing gear because the aircraft does not need to rotate to a high fuselage 
angle for additional lift during takeoff and landing. However, this arrangement is heavy and complicated and has not been attempted in many years. 
*ID Dihe dral 
Wing dihedral is the angle of the wing with respect to the horizo ntal 
when seen from the front. Posi tive (tips higher) dihedral tends to roll the 
aircraft level whenever it is banked. This is frequently, and incorre ctly, 
explained as the result of a greater proj ected area for the wing that is 
lowered. 
Actually, the rolling moment is caused by a sideslip intro duced by the 
bank angle. The aircraft "slides downhill" in the direction of the lowered 
wing. This sideways velocity, in effect a yaw angle, increases lift on the 
lowered wing (Fig. 4.2 5). The resulting rolling moment is approxima tely proportional to the dihedral angle. 
Wing sweep also produces a rolling moment due to sideslip, caused by 
the change in relative sweep of the left and right wings . For an aft- swept 
wing, the rolling moment produced is negative and propor tional to the


<!-- p.88 -->

88 Air craf t Desig n: A Concept ual Approach 
-"plac ement 
Fig. 4.25 Increased angle of attack and li ft. 
sine of twice the sweep angle. This creates an effective dihedral that adds to 
any actual geometric dihedral. 
Roug hly spea king, 10 deg of sweep provides about 1 deg of effective dihedral. For a forward- swept wing, the sweep angle produces a negative dihedra l 
effect, requiring an increased geometric dihedral in order to retain natural 
rolling stabili ty. 
In addition, the position of the wing on the fuselage has an influence on 
the effective dihedral, with the greatest effect provided by a high wing. This is 
freque ntly, and incorre ctly, explained as a pendulum effect. 
Actu ally, the fuselage in sideslip pushes the air over and under itself. If the 
wing is high-mou nted, the air being pushed over the top of the fuselage 
pushes up on the forward wing, providing an increased dihedral effect. The 
reverse is true for a low- moun ted wing. 
Because of the additive effects of sweep and wing posi tion, many highwinged transpor ts such as the Lockheed C-5 actually require a negative 
geome tric dihedral angle to avoid an excess of effective dihedral. Exces sive 
dihedral effect produces "Dutch roll," a repeated side-t o-side motion involving yaw and roll. To counter a Dutch roll tendency, the vertical tail area 
must be increased, which increases weight and drag. 
Unfortuna tely, there isn't a simple technique for selecting the correct 
dihedral angle. Like so many parameters in initial design, the dihedra l 
angle must be estimated from historical data and then revised following 
analysis of thedesign layout. 
Table 4.2, developed by the author from data taken from 16l , provides 
initial estimates of dihedral. For a wing in which the center section is flat 
and the outer sections alone have dihedral, a first approximation of the 
required dihedral for the outer panels is the one that places the wing tips 
as high as they would be for a wing with dihedral starting at the root.


<!-- p.89 -->

CHAPTER 4 Air foil and Wing /Ta il Geome try Sel ecti on 89 
Table 4.2 Dihe dral Guidelin es 
Uns wept (civil ) 
Sub sonic swept wing 
Su per sonic swept wing 
«ffl Wing Vertica l Location 
5 to 7 
3 to 7 -2 to 2 
Ot o 5 -5 to 0 
0 to 2 
-5 to -2 
-5 to 0 
The wing vertical loca tion with respect to the fuselage is generally set by 
the real-world enviro nment in which the aircr aft will operate. For example, 
virtually all high-speed commercial transport aircraft are of low-wing 
design, yet military transport aircraft designed to similar mission profiles 
and payload weights are all of high-w ing design. The reasons for this are 
discussed later. _ 
The major benefit of a high wing is that it allows placing the fusel age 
closer to the ground (Fig. 4.26) . For military transport aircraft such as the 
C-17 , C-5, and C-141, this allows loading and unloading the cargo without 
special ground-ha ndling gear. In fact, these aircraft place the floor of the 
cargo compartment about 4-5 ft {1. 5 m} off the ground, which is the 
height of the cargo area of most trucks. If cargo is needed at a remote field 
lacking ground-ha ndling gear, the trucks can be backed right up to the aircraft for loading. 
With a high wing, jet engines or propellers will have sufficient ground 
clearance without excessi ve landing-gear length. Also, the wing tips of a 
swept high wing are not as likely to strike the ground when in a nose- high, 
rolled attitude. For these reasons, landing-gear weight is genera lly reduced 
for a high-wing aircraft. 
Fig. 4.2 6 High wing.


<!-- p.90 -->

90 Air c raf t De sign : A Conceptual Appr oach 
For low-speed aircraft, external struts can be used to greatly lower wing 
weight. However, external struts add subst antially to the drag. Because 
roughly two-thirds of the lift is contributed by the upper surface of the 
wing, it follow s that less drag impact will be seen if the strut disturbs the 
airflow on the lower surface of the wing than if the strut is above the wing, 
as would be necess ary for a strut-brace, low wing. 
Another structural ben efit occurs if the wing box is carried over the top of 
the fuselage rather than passing through it. When the wing box passes 
through the fuselage, the fuselage must be stiffened around the cut-out 
area. This adds weight to the fuselage. However, passing the wing box over 
the fusela ge will increase drag due to the increase in frontal area. 
For an aircraft designed with short takeoff and landing (STOL) requirements, a high wing offers several advantage s. The high posi tion allows 
room for the very large wing flaps needed for a high lift coefficient. The 
height of the wing above the ground tends to prevent "floating, " where the 
ground effect increases lift as the aircraft approaches the ground. A floating 
tendency makes it difficult to touch down on the desired spot. Finally, most 
STOL designs are also intended to oper ate from unimp roved fields. A high 
wing places the engines and propellers away from flying rocks and debris. 
There are several disad vantages to the high-w ing arrangement. While 
landing gear weight tends to be lower than other arrangements, the fuselage 
weight is usua lly increased because it must be strengthened to suppor t the 
landing-gear loads. In many cases an external blister is used to house the 
gear in the retracted posi tion. This adds weight and drag. The fusela ge is 
also usua lly flattened at the bottom to provide the desired cargo -floor 
height above ground. This flattened bottom is heavier than the optimal circular fuselage. If the top of the fuselage is circular, as shown in Fig. 4.26, a 
fairing is required at the wing-fu selage junction. 
For small aircraft, the high wing arrangement can block the pilot's visibility in a turn, obsc uring the direction toward which the aircraft is 
turning. Also, the high wing can block upward visibility in a climb. A 
classic midair collision features a high-wing aircraft climbing into a 
low-wing airplane that is desce nding, so many high-winged light aircraft 
have transparent panels in the roof to help the pilot see upwards. 
If the fusela ge is roughly circular and fairings are not used, the midwing 
arrangement (Fig. 4.27) provides the lowest drag. High- and low-wing 
arrangements must use fairings to attain acceptable interference drag with 
a circular fuselage. 
The midwing offers some of the ground clearance benefits of the high 
wing. Many fighter aircraft are midwinged to allow bombs and missiles to 
be carried under the wing. A high-w ing arrangement would restrict the 
pilot's visibility to the rear-the key to survival of a fighter in combat. 
The midwing arrangement is proba bly superior for aeroba tic maneuverability. The dihedral usua lly required for adequate handling qualities in a 
low-wing design in normal flight will act in the wrong direction during


<!-- p.91 -->

CHAPTER 4 Air foil and Wing /Ta il Geom etry Selection 91 
Fig. 4.27 Mi dwing . 
6 in. {1 5 cm) 
clea ran ce 
inverted flight, making smoot h aerobatic maneuvers difficult. Also, the 
effective-dihedral contribution of either high or low wings will make it more 
difficult to perform high-sideslip maneu vers such as the knife-edge pass. 
Structural carrythrough presen ts the major problem with the midwing. 
As will be discussed in Chapter 8, the bending moment produced by the 
lift on the wing must be carried across the fuselage either by an extension 
of the wing box ("wing carrythrough box") or by a set of massi ve ring 
frames built into the fuselage. 
The carrythrough box often proves lighter, but cannot be used in a 
midwing design that must carry cargo or passengers. One exception to 
this, the Ger man Hansa executi ve jet, uses a mild forward sweep to place 
the carrythrough box behind the passen ger compartment (see Chapter 22) . 
A carrythrough box may be difficult to incorporate in a midwing fighter, in 
which most of the fuselage will be occupied by the jet engines and inlet ducts. 
The major advantage of the low-wing approach (Fig. 4.28) comes in 
landing -gear stowage. With a low wing, the trunnion about which the gear 
is retracted can be attached direct ly to the wing box, which, being strong 
already, will not need much extra strengthening to absor b the gear loads. 
When retracted, the gear can be stowed in the wing itself, in the wingfuselage fairing, or in the nacelle. This eliminates the external blist er 
usually used with the high-w ing approach. 
To provide adequate engine and propeller clearance, the fuselage must be 
placed farther off the ground than for a high-w ing aircraft. While this adds to 
the landing-gear weight, it also provides greater fuselage ground clearance. 
This reduces the aft-fus elage upsweep needed to attain the required takeoff 
angle of attack. The lesser aft-fuse lage upsweep reduces drag. 
While it is true that the low-wing arrangement requires special ground 
equipment for loading and unloading large airplanes, the high-speed


<!-- p.92 -->

92 Air c raf t De si gn: A Conceptual Approa ch 
6 in. (1 5 cm) 
clear anc e 
t 
_ j_ - - - - --=---=---=-.. - ---_.. ....__. ...._------......._""'""-- Sd eg 
Fig. 4.28 Low wing . 
comme rcial transpor ts are only oper ated out of established airfields with a 
full complement of equipment. This is the main reason why military and 
comme rcial transports are so different. 
Large transpor ts have a fuselage diameter on the order of 20 ft {6 m}, 
which allows an uninterrupted passen ger comp artment above the wing carrythrough box. The wing carrythrough box usually passes through the fuselage for reduced drag and splits the lower cargo compartment into two 
compartments . This efficient internal fuselage layout is virtually standard 
for comme rcial tra nsports. 
If the center-w ing panel of a low-wing aircraft lacks dihedral, a one- piece 
flap that passes under the fuselage can be used. This reduces comple xity as 
well as the risk of asymmetric lift caused by the failure of one flap to 
extend. Also, the continuous flap will produce more lift and drag than an 
equal -area flap that is broken at the fuselage. 
Several disadvantages of the low-wing approach have alread y been mentioned, including ground- clearance difficult ies. Freque ntly, low-wing aircraft 
will have dihedral angle set not by aerod ynamics but by the angle required to 
avoid striking the wing tip on the ground during a bad landing. As was mentioned before, it may require an increase in vertic al-tail size to avoid Dutch 
roll with an exces sive dihe dral angle. 
Clearance also affects propellers. To minimize the landing-gear length, 
many low-wing aircraft have the prope llers mounted subst antially above 
the plane of the wing. This will usua lly increase the interference effects 
between the wing and propeller and result in an increase in fuel consumption 
during cruise. 
In the discussion of aspect ratio, it was mentioned that the high-pressure 
air would like to "escape" from the bottom of the wing, moving around


<!-- p.93 -->

CHAP TER 4 Air fo il and Wing /Ta il Geome try Selecti on 93 
the wing tip to the top. This lowers the pressure difference between the 
upper and the lower surfaces, thus reducing lift, and also creates the tip 
vortices that actually cause the drag-due-to- lift. Clearly, we would like to 
prevent this or at least make it more difficult. Many schemes have been 
tried, mostly involving clever wing-tip shaping or by erecting some sort of 
a wall or fence to stop the flow around the wing tip. Wing- tip concepts are 
shown in Fig. 4.29. 
A smoot hly rounded wing tip, when seen nose-on , actually makes it easier 
for the air to flow around the tip. While it looks "streamlined" to the eye, it is 
not a very good shape as far as subsonic lift and drag are concerned. A wing 
tip with a sharp edge seen nose-on makes it more difficult for the air to flow 
around the tip, thus increasing lift and reducing the induced drag. Most of the 
new low-drag wing tips use some form of sharp edge. In fact,- even a simple 
cutoff tip offers less drag than a rounded-off tip, due to the sharp edges where 
the upper and lower surfaces end. 
One widely used low-drag approach is the Hoerner wing tip. l9l This is a 
sharp-edged wing tip where all of the reshaping is done on the lower surface. 
The upper surface continues its airfoil shaping all the way to the tip- remember that the upper surface generates 2/3 of the lift. The lower surface is 
"undercut" and canted approxima tely 30 deg to the horizontal. The lower 
surface may also be "undercambered" (i.e., conca ve) to better match the 
upper surface where they meet at the tip. 
The "drooped" and "ups wept" wing tips attempt to "trap" the air with a tip 
that is curved upward or downward. These work quite well, increasi ng lift 
_ _.__I )J I:> ---17 
Rou nded Shar p Cut- off Hoerner 
»is>-t-iln 
- I> 1;00 _J -;:J 
Ups wept Aft-swept Cut -off - Wing let 
forwa rd swept 
Fig. 4.29 Wing tips.


<!-- p.94 -->

94 Airc raf t De sign: A Concep tu al Approach 
and reducing drag by increasing the effective span without increasing the 
actual span. This effect is similar to that emplo yed by endplates and winglets, 
as discussed below. However, these tips sligh tly increase the total wetted area, 
which increases parasitic drag. Also, they add weight, increase wing torsional 
loads, and can cause flutter if not carefully designed. 
A swept wing tip can reduce the drag. The loca tion of the tip vortex 
defines the effective span of the wing. The tip vortex forms approximately 
at the trailing edge of the wing tip so that an aft-swept tip, with its greater 
trailing- edge span, tends to have lower drag. However, the aft-swept wing 
tip will increase the wing torsion al loads. 
A cutoff, forward -swept wing tip is some times used for supersonic aircraft. The tip is cut off at an angle equal to the supersonic Mach-cone 
angle because the area of the wing within the shock cone formed at the 
wing tip will contribute less to the lift. Also, this tip shape will reduce the torsiona l loads applied to the wing and can help with flutter problems. The F- 15 
fighter uses such a cutoff tip for both wings and horizo ntal tails. 
Induced drag and loss of lift are both caused by the higher-pr essure air at 
the bottom of the wing esca ping around the wing tip to the top of the wing. 
An obvious way to prevent this is to place a big vertical plate at the wing tip. 
The endplate effect has been known since the dawn of flight, but is rarely 
seen. The wetted area of the endplate itself creates drag. Also, an endplated 
wing has an effective span increase of only about 80% of the actual span 
increase caused by adding the endplates' height to the wing span. In most 
cases, you get a better airplane by increasing the span, but endplates can 
be useful when span must be limited for some reason. 
An advanced version of the endplate can offer lower drag than an equalarea increase in wing span. The "winglet," invented by NASA genius Richard 
Whitcomb,* gets an additional drag reduction by using the energy available 
in the tip vortex and can increase lift-to- drag ratio by up to 20%. 
The winglet is a vertical surface rising from the wing tip. Actually, a little 
wing, it is angled and cambered to create a strong lifting force poi nting 
inward. The wing tip's rotating vortex causes the local flow striking the 
winglet to be angled inwards, so the winglet's lifting force- perpendicular 
to the local flow direction-gets a noticeable forward compo nent. This 
forward lift component acts as a "negative " drag, reducing the total wing drag. 
The drag reduction of a winglet can also be visualized as an effective 
increase in span. Like all lifting surfaces, the winglet produces a downwash 
behind itself. Because the winglet is angled vertically, that downwash is 
actually an "outwash," which blows the tip vortices further apart. Aero dynamicall y, the distance between the tip vortices is the effective span of the 
wing, so the winglet increases the wing's effective span, hence reducing its 
drag-due-to-l ift. 
*W hitcomb also invented the area rule for supersonic drag reduction, and the supercritical wing 
for transonic drag reduction.


<!-- p.95 -->

CHAPTE R 4 Air fo il and Wing /Ta il Geome try Selec tion 95 
A prop erly designed winglet can potentially provide an effective span 
increase up to double that boug ht by adding the winglets' height to the wing 
span. Winglets provide the greatest benefit when the wing-tip vortex is 
strong. An already- efficien t, high aspect ratio wing may see little or no 
benefit. The most improvement will occur for a wing with aspect ratio lower 
than optimal, or a wing that is now carrying more aircraft weight than 
originally intended. 
One problem with winglets is that they add weight behind the elastic axis 
of the wing, which can aggravate flutter tendencies. Also, the twist and 
camber of a winglet must be optimized for one veloc ity. At other speeds, 
the winglet will provide less benefit and can actually increase the drag. 
For these and other reasons, winglets tend to be used more as add-on 
devices for existing wings requiring a little more efficienc y without major 
redesign. When an all new wing is being designed, it is usually better to 
rely upon increased aspect ratio to improve aerod ynamic efficie ncy. This is 
not always true, so a trade study should be conducted sometime during 
the concept ual design effort. Winglet design layout is presen ted in Chapter 7. 
Biplane Wings 
Biplanes dominated aviation for the first 30 years . The Wright Brothers 
were influenced by Octave Chanute, a noted architect and civil engineer 
who applied a structural concept used in bridge building to create lightweight 
biplane gliders. The early airfoils were thin and birdlike, requiring external 
bracing, and the biplane arrangement provided more structural efficiency 
than an externally braced monoplane. 
With the thicker airfoils now in use, the biplane arrangement is mainly 
reserved for recreational purposes. However, it should be considered whenever low structural weight is more important to the design than aerod ynamic 
efficiency, or when low speed is required without complicated high-lift 
devices or excessi ve wing span. The most typical application for biplanes 
today is in the aerobatic airplane, where a reduced span can allow a greater 
roll rate. 
A biplane should theoretic ally produce exactly half the induced drag of 
a monoplane with equal span. Induced drag, or drag-due-to-l ift, is proportional to the square of the lift being generated. If that lift is split evenly 
between two wings, each wing should have only one- fourth of the drag of 
the original wing. Therefore, the total induced drag of a biplane should be 
two-fou rths, or one- half of the value obtained with a monoplane of equal span. 
Unfortunately, mutual-interference effects prevent the full ben efit from 
being attained. Good design can yield on the order of a 30% reduction in 
drag-due-to -lift for a biplane when com pared to a monoplane of equal 
span. However, if the total wing area is held constant to provide the same 
wing loading for biplane and monoplane, and the monoplane has the same 
wing span as the biplane, then the aspect ratio of the two wings of the


<!-- p.96 -->

96 Airc raf t Des ign: A Conceptual Ap proa ch 
biplane must each be double the aspect ratio of the monoplane. Biplanes are 
rarely designed this way, so they rarely get this theor etical benefit. 
Biplane aerod ynamic analysis using Prandtl's interference factor is 
described in Chapter 12. For initial design purposes, several key concepts 
should be considered. These are the "gap," "span ratio," "stagger," and 
"deca lage ." 
Gap is the vertical distance between the two wings . If the gap were infinite, 
the theoretical result of a halving of the biplane induced drag when compared 
to an equa l-s pan monoplane would be attained. However, structural weight 
and the drag of connec ting struts genera lly limit the gap to a value approximately equal to the average chord length. A shorter gap will produce increasing interference between the two wings, raising the overall drag. 
Spa n ratio is the ratio between the shorter wing and the longer wing. If 
both wings are the same length, the span ratio is one. When span is 
limited, the minimum induced drag is obtained from equal-l ength wings. 
As described, the only technical reason for using the biplane arrangement 
is the case where span is limited, so the biplane with wings of unequal 
length should be rarely seen. However, a shorter lower wing has been used 
in the past to provide better ground clearance. 
Stagger is the longitudinal offset of the two wings relative to each other. 
Pos itive stagger places the upper wing closer to the nose than the lower wing. 
Stagger has little effect upon drag and is usua lly used to impro ve the visibility 
upward from a rear-located cockpit. Negative stagger was used in the beautiful Beech D-17 Stagger wing to impro ve visibility from an enclosed cabin 
cock pit and to reduce the pitching moment of the large flaps on the 
lower wing. 
Deca lage is the relative angle of incidence between the two wings of a 
biplane. Deca lage is posit ive when the upper wing is set at a larger angle 
than the lower. In early years much attention was paid to the selection of 
deca lage to minimize induced drag while enco uraging the forward wing to 
stall before the aft one, thus providing natural stall recovery. Most biplanes 
since World War I have been designed with zero decalage, although the 
Pitts Spec ial, holder of numerous world aeroba tic championships, has a positive decalage of 1.5 deg. 
Much of the previous discussions concerning the initial selection of wing 
geo metry can be applied to biplane wings . Most biplanes have wing aspect 
ratios comp arable to monoplanes of similar class (six to eight) . As discussed, 
this yields induced drag levels much higher than obtained from a monoplane 
with similar wing loading. Taper ratios for biplanes can be selected as for a 
monoplane, although many biplanes have untapered wings for ease of 
manufacture. 
One or both biplane wings can be swept to enhance stability, impr ove 
pilot visibilit y, or provide room for retractable landing gear. Biplanes typically 
have dihedral of about 2 deg. Aeroba tic biplanes can apply dihedral only to 
the lower wing.


<!-- p.97 -->

CH AP TER 4 Air fo il and Wing /Ta il Geo metry Selection 97 
The mean aerod ynamic chord of a biplane can be found as the weighted 
average of the mean chords of the two wings, weighted by the relative areas of 
the wings. The biplane aerod ynamic center is at approximately 23% of the 
mean aerodynamic chord, rather than 25% as for a monoplane, due to the 
wing interfe rence effects. 
Tail Geome try and Arran gem ent 
#Jj# Tail Fu ncti ons 
Tails are little wings. Much of the earlier discussion conc erning wings can 
also be applied to tail surfaces. The major difference between a wing and a tail 
is that, while the wing is designed to routinely carry a substantial amount of 
lift, a tail is designed to operate norma lly at only a fraction of its lift potential. 
Any time in flight that a tail comes close to its maximum lift pote ntial, and 
hence its stall angle, something is very wrong! 
Tails provide for trim, stability, and -ontrol. Trim refers to the generation 
of a lift force that, by acting through some tail moment arm about the center 
of gravity, balances some other moment produced by the aircraft. 
For the horizo ntal tail, trim primarily involves balancing of the moment 
created by the wing. An aft horizont al tail typically has a negative incidence 
angle of about 2-3 deg to balance the wing pitching moment. Because the 
wing pitching moment varies under different flight conditions, the horizo ntal 
tail incidence is usua lly adjustable through a range of about 3 deg up 
and down. 
Concerning the vertical tail, most aircraft are left- right symmetric, so 
unbalanced aerod ynamic yawing moments requiring trim are not created 
during normal flight. Propeller aircraft experience a yawing moment 
called "p-effect," which has several thrust-related causes. When the disk 
of the propeller is at an angle, such as during climb, the blade going 
downward has a higher angle of attack and is also at a slightly higher 
forward veloc ity. This condition produces higher thrust on the downwardmoving side and hence a yawing moment away from that side. Also, the 
propeller tends to "drag" the air into a rotational corkscrew motion. The 
vertical tail is pushed on sideways by the rotating propwash causing a 
yawing moment, which adds to the p-effect. To counter p-effect, many 
single- engine propeller airplanes have the vertical tail offset several 
degrees. 
The vertical tails of multi -engine aircraft must be capable of providing 
sufficient trim in the event of an engine failure. This produces yawing both 
from lack of thrust on one side and the extra drag of the stopped or windmilling engine. For props, engine -out yaw is espec ially severe when the engine 
that is still running has its downward-traveling blade on the side away 
from the fuselage. Some multi-engine aircraft have coun ter- rotating propellers to minimize the engine -out yawing.


<!-- p.98 -->

98 Ai rcraft De sig n: A Conceptu al Ap proa ch 
The Lockheed P-38 was notorious for having coun ter- rotating propellers 
that go the "wrong" way. Both propellers have their downward -going side 
away from the cockpi t, app arently due to pro pwash effects on the tails 
causing a wandering motion that affected gun accurac y. In the event of an 
engine failure on takeoff , the pilot had to immed iately reduce power on the 
running engine to avoid rolling upside down! 
The tails are also a key element of stabi lity, acting much like the fins on an 
arrow to restore the aircraft from an upset in pitch or yaw. Although it is 
possi ble to design a stable aircraft without tails, such a design is usua lly penalized in some other area, as discussed in Chapter 22. 
The other major function of the tail is control. The tail must be sized to 
provide adequa te con trol power at all critical conditio ns. These critical conditions for the horizo ntal tail or canard typic ally include nose wheel liftoff, 
low-speed flight with flaps down, and transonic maneu vering. For the vertical 
tail, critical conditions typic ally include engine -out flight at low speeds, 
maximum roll rate, and spin rec overy. 
Note that con trol power depends upon the size and type of the movable 
surface as well as the overall size of the tail itself . For example, several airliners use double- hinged rudders to provide more engine- out control power 
without increasing the size of the vertical tail beyond what is required for 
Dutch-rol l damping. Several fighters, including the YF- 12 and the F-10 7, 
have used all-mo ving vertical tails instead of sep arate rudders to increase 
con trol power. 
Prelimin ary methods for sizing tails are provided in Chapter 6, and stability and con trol analysis methods are provided in Chapter 16 . 
.m Ta il Arrangem ent 
Figure 4.30 illustrates some of the possi ble aft-tail arrangements. The first 
one has become "con ventional" for the simple reason that it works. Prob ably 
70% or more of the aircraft in service have such a tail arrangement. For most 
aircraft designs, the conventional tail will provide adequate stability and 
control at the lightest weight. This arrangement puts the horizontal surface 
in a location that usua lly sees smooth airflow, attaches that horizo ntal 
surface to the fuselage where there is usua lly adequate structure, and makes 
it easy to mechanize con trol linkage s. When developing a new design you 
should always consider a conventional tail, no matter how "bor ing" you 
think it is. However, there are many reasons for consi dering others. 
The "T-t ail" is also widely used. This arrangement is usua lly heavier than 
a con ventional tail because the vertical tail must be strengthened to support 
the horizon tal tail, but the T-tail provides compensa ting advantages in 
many cases. 
Because of end-p late effect, the T-t ail allows a smaller vertical tail. The 
T-t ail lifts the horizon tal tail clear of the wing wake and prop wash, which 
makes it more ef ficient and hence allows reducing its size. This also


<!-- p.99 -->

CH APTER 4 Air foil and Wing /Ta il Geome try Sel ecti on 
Fig. 4.30 Aft tail variations. 
reduces buffet on the horizont al tail, which reduces fatigue for both the structure and the pilot. 
In jet transport aircraft such as the DC-9 and. B-727, the T-tail allows the 
use of engines mounted in pods on the aft fuselage. Finally, the T-t ail is considered stylish, which is not a trivial consi deration. 
The cruciform tail, a compromise bet ween the conventional and T-t ail 
arrangements, lifts the horizontal tail to avoid proxi mity to a jet exhaust 
(as on the B- lB), or to expose the lower part of the rudder to undisturbed 
air during high angle- of-attack conditions and spins. These goals can be 
accomplished with a T-t ail, but the cruciform tail will impose less of a 
weight penalty. However, the cruciform tail will not provide a tail- area 
reduction due to endplate effect as will a T-t ail. 
The "H-t ail" is used primarily to position the vertical tails in undisturbed 
air during high-angle-of -attack conditions (as on the T-46) or to posi tion the 
rudders in the propwash on a multiengine aircraft to enhance engine- out 
control. The H-tail is heavier than the conventional tail, but its endpla te 
effect allows a smaller horizo ntal tail. 
On the A- 10, the H-t ail serves to hide the hot engine nozzles from heatseeking missiles when viewed from an angle off the rear of the aircraft. H-tails 
and the related triple-t ails have also been used to lower the tail height to allow 
an aircraft such as the Loc kheed Const ellation to fit into existing hangars. 
The "V-tail" (Fig. 4.3 1) is intended to reduce wetted area. With a V-tail, 
the horizontal and vertical tail forces are the result of horizo ntal and vertical


<!-- p.100 -->

10 0 Aircraf t Des ign : A Conceptu al Appr oach 
Fig. 4.3 1 Notio nal V-tail gull wing homebuilt (D. Raymer 2005 ). 
projections of the force exerted upon the V surfaces. For some required horizontal and vertical tail area, the required V surface area would theoretica lly 
be found from the Pythagorean theorem, and the tail dihedral angle would 
be found as the arctangent of the ratio of required vertical and horizontal 
areas. The resu lting wetted area of the V surfaces would clear ly be less 
than for sepa rate horizo ntal and vertical surfaces. 
However, extensive NACA research [lO] has concluded that to obtain satisfactor y stabil ity and control, the V surfaces must be upsized to about the 
same total area as would be required for sep arate horizo ntal and vertical surfaces. This is mo stly due to the effect that extreme dihedral angle has on a 
change in angle of attack. 
Even without the advantage of reduced wetted area, V-tails offer reduced 
interference drag. There is a pena lty in control actuation comple xity because 
the rudder and elevator control inputs must be blended in a "mixer" to 
provide the proper movement of the V-tail "rudder vators." 
When the right rudder pedal of a V-tail aircraft is pressed, the right ruddervator deflect s downward, and the left rudder vator deflects upward. The 
combined forces push the tail to the left, so the nose goes to the right as 
desired. However, the rudder vators also produce a rolling moment toward 
the left-in oppos ition to the desired direction of turn, an action called 
"adverse roll -yaw coupling." 
The inverted V-tail shown in Fig. 4.32 avoids this problem and instead 
produces a desirable "pro verse roll-y aw coupling. " The inverted V-tail is 
also said to reduce spiraling tendencies. This tail arrangement can cause difficulties in providing adequate ground cleara nce. 
The "Y-tail" is similar to the V-tail, except that the dihedral angle is 
reduced and a third surface is moun ted vertically beneath the V. This third 
surface contains the rudder, whereas the V surfaces provide only pitch


<!-- p.101 -->

CHAPTE R 4 Air foil and Wing /Ta il Geome try Selecti on 10 1 
control. This tail arrangement avoids the complexity of the rudder vators 
while reducing interference drag when compared to a conventional tail. 
Several pusher propeller designs have used the Y-tail because the bottom 
surface serves as a tail skid, stopping the propeller from hitting the ground. 
An inverted Y-tail is used on the F-4, primarily to keep the horizo ntal 
surfaces out of the wing wake at high angles of attack. 
Twin tails on the fuselage can posi tion the rudders away from the aircraft 
centerline, which can become blanketed by the wing or forward fusela ge at 
high angles of attack. Also, twin tails have been used simply to reduce the 
height required with a single tail. Twin tails are usua lly heavier than an equalarea single tail, but are often more effective. Twin tails are seen on most large 
modern fighters such as the F-14 , F- 15, F-18 , and MiG-25. 
Boom-mo unted tails have been used to allow pusher propellers or to 
allow location of a heavy jet engine near the center of gravity. Tail boom s 
are typically heavier than a conventional fuselage construction, but can be 
desirable in some applicat ions. 
Boom- mounted tails can have a midmounted horizo ntal tail or a high 
horizontal, as on the Cessna Skymaster. The inverted V-tail arrangement 
can be used with tail boom s, as on the small Aerosonde UAV, which 
crossed the Atlantic. The unmanned NASA HiMat research aircraft used 
Fig. 4.32 Notional inverted- V pusher (D. Raymer 2005) .


<!-- p.102 -->

l 02 Air c raft Design: A Conceptual Approach 
boom- mounted verticals with no conn ecting horizo ntal tail, instead relying 
on a canard for pitch control. 
The "ring-t ail" concept attempts to provide all tail contributions via an 
airfo il- sectioned ring attached to the aft fuselage, usually doubling as a propeller shroud. While concept ually appealing, the ring- tail has proven 
inade quate in applicat ion. The ring-tail JM-2 raceplane was ultimately converted to a T -tail. 
The location of an aft horizo ntal tail with respect to the wing is critical to 
the stall characteristics of the aircraft. If the tail enters the wing wake during 
the stall, control will be lost , and pitch-up can be encoun tered. Several 
T-tailed aircraft enco untered "deep stall" from which they could not be extricated. One T-t ail trainer was recent ly found to be three to seven times more 
likely to have a stall/ spin accident than other similar trainers . 
Figure 4.33 illustrates the boundaries of the acce ptable locations for a 
horizo ntal tail to avoid this problem. Note that low tails are best for stall 
recovery. Also, notice that a tail approx imately in line with the wing is accep table for a subsonic aircraft, but can cause problems at supersonic speeds 
due to the wake of the wing. 
A T- tail requires a wing designed to avoid pitch-up without a horizont al 
tail, as described by Fig. 4.2 1. This requires an aircraft stable eno ugh to 
recover from a stall even when the tail is blanketed by the wing wake. 
Several gener al aviation aircraft use this appro ach, which has the added 
benefit of a posi tive warning to the pilot of impen ding stall caused by buffeting on the tail as it enters the wing wake at high angle of attack. 
2 
0 + 
Wing qua rter chor d 
-1 
0 
C/4 
1 
Okay subsonic only 
Best location for ta il 
2 3 
Tail ar m/Cwing 
Fig. 4.33 Aft tail posit ioning . 
NACA TMX-26 
4 5


<!-- p.103 -->

Flyi ng wing 
CHAPTER 4 Air foil and Wing /Ta il Geom etry Selec ti on 10 3 
Fig. 4.34 Other tail confi gur ations. 
There are airplanes that don't have a horizont al tail in back. While birds 
seem to have settled the issue in favor of aft tails, the highly maneu verable 
bats do not have them, nor do most flying insects. The earliest experimen tal 
researchers such as George Cayley and Otto Lilien thal used bird-li ke aft tails, 
but both the Wright Brothers and Santos Dumon t used canards. It wasn't 
until Louis Bleriot flew the English Channel that the modern wing-plusaft-tail configuration came to dominate. 
Alternatives to the wing-plus-aft-t ail arrangement are depicted in 
Fig. 4.34 including tails in front, multiple wings, multiple tails, and no tails 
at all. All have advantages and disadvantages, and all have their vocal supporters. As designers, we shouldn't have a prefer ence. We should look at many 
alternatives, develop the best pos sible design for each, conduct detailed 
analysis and honest trade studies, and finally select the best approach to 
meet our customer's needs. Sometimes, though, one of our customer's 
needs-p erhaps unstated-is to fly an airplane that really looks innovative 
and exotic, regardless of its technical merits! 
Tails in front, called canards, were used by the Wright Brothers but 
soon fell out of favor mostly because of stability issues. The early Wright 
airplanes were quite unstable and required a well-trained pilot with 
quick reflexes. Movie footage taken by passen gers shows the Wright 
canards being continuous ly manipula ted from almost full-up to full-down 
as the pilot responded to gusts . While a canard airplane can be made


<!-- p.104 -->

10 4 Ai rcraf t De sign : A Conc eptu al Appr oach 
stable by careful design, doing so imposes other pena lties as described 
belo w. 
The canard configuration does have several advanta ges. An obvious 
advantage, and perhaps the real reason it was used by the Wrights, is that 
it places the pitch control surface in a region of undisturbed flow where its 
con trol response is sure and predictable. An aft tail is always flying in air 
that has been disturbed by its passage over the wing and fuselage. 
The canard arrang ement can imp rove stall safety. The canard tail itself 
can be designed to stall before the wing so that the nose lowers before the 
plane can get into troub le. This is the main reason why Burt Rutan and 
others have used canards on homebuilt designs such as the VariEze. To 
make the canard surface stall first, it can be designed with a higher aspect 
ratio than the wing, and the wing can be swept and fitted with leading- edge 
"cuffs" that curve down into the flow. 
The canard configuration can be used to avoid pitch -up. This is a dangerous co ndition wherein the nose comes up to a high angle and the pilot cannot 
put it back down. An all-moving canard capable of downward deflections of 
45 deg or more can be used to force the nose back down under almost any 
situation. This is seen on the X-3 1 which flew at 70-deg angle of attack, 
but requires a sophisticated comp uterized flight control system. 
A subtle aerod ynamic bene fit can be obtained with a canard configuration. If both wing and canard are highly swept, the canard vortex can be 
made to interact with the leading- edge vortex on the wing, increasing its 
strength and therefore augmenting its lift. This bene ficial interference is geometry depen dent and difficult to predict. The SAAB Viggen and Rock well 
HiMat both used this effect. 
One of the main benefits claimed by canard advocates and often seen in 
the aviation popu lar press is an inherent improvement in lift and drag vs conventional airplane s. An aft- tail airplane suffers from the download typically 
exerted by the horizontal tail and needed for stabil ity. Not only does this 
download create drag, but the wing must lift harder to cou nteract it, creating 
even more drag and requiring the wing to be made larger. The canard airplane, they say, bene fits because both of its surfaces are lifting upward s. 
This ignores a big problem of canards -they make the airplane inhere ntly 
unstable, for reasons explained below. To make a canard airplane stable, the 
designer must arrange the airplane so that the center of gravity is well to the 
front. In other words, the canard surface must carry far more than its "fair 
share" of the weight. The wing carries less than it should, so there isn' t as 
much total lift as there would be if the wing were "doing its share ." To 
meet stall speed requirements, the wing must be made larger, increasing 
weight and drag. 
If the canard airplane is designed with a mod ern comp uterized flight 
control system, it doesn't need natural stabil ity. The center of gravity can 
be further back, and the wing can "do its share" as discussed below. But a 
modern aft-tail aircraft is also designed to be some what unstable so that it


<!-- p.105 -->

CH APTE R 4 Air foil and Wing /Ta il Geome try Selec ti on 10 5 
normally flies with an upload, not a download on its tail. This is the very 
reason that computerized flight control systems with artificial stability 
were developed and put into production, first on the F- 16 over 40 years 
ago. So, it is misleading to compare an old "download-on-the- tail" conventional design with a modern compute r-con trolled canard design. 
There are actually two distinct classes of canard: the control- canard and 
the lifting-canard. In the control- canard design, the canard surface is used for 
pitch co ntrol just as an aft-tail is used. The wing carries most of the lift, and 
the canard surface is used primarily to control the angle of attack of the wing. 
It isn't norma lly lifting much, except perhaps to counter flap deflection for 
takeoff, landing , and maneu ver. Because the canard surface isn't norma lly 
lifting, it is not designed for lift efficiency and usually has the lower aspect 
ratio and low-camber airfoil typical of an aft tail. You can see this on such 
designs as the Grippen, Typhoon, X-29, and X-31. 
When doing the layout of an aircraft with a control canard, we normally 
design it so that it is about neutrally stable with the canard removed. The 
flight control computer then keeps the canard surface near zero angle of 
attack regardl ess of the pitch angle of the fuselage, only deflecting it with 
respect to the oncoming air when needed for pitch control. To facilitate 
this, the control-canard is usua lly a pivoting all- moving surface. 
If the contr ol- canard surface should lock in place, the airplane becomes 
extremely unstable, so a fast and highly reliable flight control system is 
required. Unfortunately, a frozen air data sensor on the X-31 rendered its 
computer clueless, resulting in an instantaneous loss of control. The pilot 
survived ejectio n. 
In contrast, a lifting-canard aircraft uses both the wing and the canard to 
provide lift all of the time. The lifting-canard surface must be a good wing as 
well as a control surface, so that it will have the greater aspect ratio and airfoil 
camber typical of a wing. The size of the canard relative to the wing is chosen 
by the designer more in response to balance and other consid erations than to 
control issues as for an aft-tail or control- canard. 
In the extreme, the lifting-canard surface can be as big as the wing-a 
tandem wing design. The tandem wing dates to the dawn of aviation. 
Samuel Langley's unmanned "Aerodrome" used tandem wings (plus an aft 
tail, for good measure) and flew almost a mile, seven years before the 
Wright Brothers first powered flight. 
The supposed benefit of the tandem wing is a theoretical 50% reduction 
in the drag- due-to- lift (induced drag) . This drag is a function of the square of 
the lift being produced. If the weight of the aircraft is evenly distributed to 
two wings, each wing would have only one-fo urth of the induced drag of a 
single wing. Thus, the sum of the induced drags of the two wings should 
be one- half of the drag of a single wing-theoretica lly. 
This theoretical result is not seen in practice. First, for it to be even theoretically true the two half-size wings would each have to have the same span as 
the original wing. They would not be photog raphic ally scaled small versions


<!-- p.106 -->

10 6 Air c raft Desi gn: A Conceptual Approach 
of the original wing, but would have to have aspect ratios twice as high. The 
weight pena lty is obvious, and therefore tandem wing designs usually have 
"nor mal" aspect ratios thus invalidating the one supposed benefit. 
However, the fundame ntal problem is even simpler-t he second wing 
must fly in the downwash of the first wing. This requires a higher angle of 
incidence on the second wing, but even more impo rtant, the direction of 
lift is turned. Lift is always perpen dicular to the local flow direction, and, 
as can be seen in Fig. 4.35, that direction has been turned by the front 
wing. The lift of the back wing therefore has a compone nt to the rear that 
is a newly created drag term! 
An even bigger problem results from the front wing's downwash: pitch 
stabil ity requires that if the nose comes up, mom ents are created that push 
the nose back down. In a tandem wing design the front wing sees the full 
increase in angle of attack that results when the nose comes up, and it generates additional lift. It also turns the flow, so that the back wing does not see 
the full increase in angle of attack. As a result, the back wing does not 
produce near ly as much extra lift. 
With the full extra lift in front and less extra lift in back, a nose-up 
moment is created that is the exact opposi te of what is needed. The front 
wing's down wash literally makes the airplane unstable. The only way to get 
natural pitch stabil ity with a tandem wing is to design it so that the center 
of gravity is far forward of the location that would provide for an even 
weight split. Thus, the aft wing is "lazy"-it carries much less than an 
equal share of the aircraft's weight. To create the required lift for flight, the 
Freestream flow direction 
- - - - -nge-------:_::::::::::::::=::::=::::::::--!1111- in AOA Reduced change in AOA 
Fig. 4.35 Downwa sh effect on back wing's li ft.


<!-- p.107 -->

CHAPTE R 4 Air foil and Wing /Ta il Geo metry Sel ecti on 10 7 
total area of the two lifting surfaces must be increased. This takes away the 
supposed drag benefit. 
This problem is worse when flaps are to be used. Flaps on the back of 
the front wing are very near the center of gravity, so they produce only a 
small nose-up pitching moment. Flaps on the back of the rear wing are far 
from the e.g., and so they produce a huge nose- down momen t. It is 
impossible to balance the aircraft. For this reason, tandem wing designs 
normally cannot use flaps on the back wing. Without flaps on all lifting 
surfaces, those surfaces must be made even larger to meet the stall speed 
requirement . 
Desp ite these problems, sometimes the tandem wing arrangement is 
useful for other reasons. Like a canard, it can be designed so that the front 
wing stalls first, which safely lowers the nose even if the pilot is still foolishly 
pulling back on the control stick. This was seen on Henri Mignet's tiny homebuilt "Pou-d u-Ciel," literally "Louse of the Sky" but more charitably translated as the "Flying Flea. " 
The tandem wing arrangement rnight allow one to efficien tly carry a 
large and bulky load, lifting from the ends like carrying a log. The Scaled 
Composites White Knight susp ends SpaceShipOne between tandem wings. 
Tandem wings are discussed further in Chapter 22. 
Back to canards-the lifting -canard configurati on is actually a tandem 
wing with a smaller front wing. It therefore suffers the same penalties 
caused by the downwash from the front wing (i.e., the canard) . The center 
of gravity must be far forward for stabil ity, the rear wing is lazy requiring a 
greater total area, and it is difficult to use flaps. on the rear wing. To allow 
at least some flaps on the wing, several designs have resor ted to the use of 
slotted canard flaps or even a canard that sweeps forward for takeoff and 
landing (Beech Starsh ip). 
The efficiency of the lifting-canard design is impro ved if the center of 
gravity can be moved farther to the rear, but this reduces stabil ity and eventually requires a comp uterized flight control system. The farther back the 
center of gravity is placed, the less lift is carried by the canard until finally 
it becomes a control-canard! 
A three-s urface arrangement includes both aft-tail and liftin g-ca nard 
surfaces. This allows use of the canard for efficient trim and pitch co ntrol 
without the difficulty of incorpor ating wing flaps as seen on a canard- only 
configura tion. 
The three- surface aircraft theore tically offers minimum trim drag. A 
canard or aft tail, when generating lift for trim purposes, will change the aircraft total lift distrib ution, which increases total induced drag. On a threesurface configuration the canard and aft tail can act in oppo site directions, 
thus cancelling out each other's effect upon the total lift distri bution. For 
example, to generate a nose-up trim the canard can gener ate an upward 
lift force while the tail generates an equal downward lift force. The combined 
effect upon total lift distribution would then be zero.


<!-- p.108 -->

10 8 Air c raf t Des ign : A Conceptu al Approach 
However, this reduction in trim drag is a theoretical far-field effect and 
might not be fully realized in an actual design. The drawback of the threesurface arrangement is the additional weight, comple xity, and interference 
drag asso ciated with the extra surfaces. 
The "bac k-por ch" or "aft- strake" is a horizont al control surface that is 
incorpor ated into a faired extension of the wing or fuselage. This dev ice, 
seen on the X-29, is most ly used to prevent pitch-up but can also serve as 
a prim ary pitch control surface in some cases. 
Sometimes, the best tail is no tail. The tailless config uration offers the 
lowest weight and drag of any tail configuration, if it can be made to work. 
For a stable aircraft, the wing of a tailless aircraft must be reflexed or 
twisted to provide natural stabil ity. This reduces the efficiency of the wing. 
For an unstable aircraft with a computerized flight con trol system, this 
need not be done. In fact, an unstable, tailless aircraft can be designed to 
be "self-trimm ing, " meaning that the wing trail ing- edge flap angles required 
to balance the aircraft at different speeds and angles of attack can be 
designed to be almost exactly the optimal flap angles for lift at different 
speeds. As the plane slows for landing, the flaps must deflect downwards 
for balance! 
This is very difficult to accomplish and is very sen sitive to the loca tion 
of the center of gravity. In fact, all tailless designs are sens itive to 
cente r-of-gravity loca tion and are most successful in designs in which the 
expendable fuel and payload are located very close to the empty center 
of gravity. 
The vertical tail can also be eliminated for reduced weight and drag. 
However, the fully tailless (flying-w ing) design is probably the most difficult configuration to stabilize, either naturally or by com puter. Unless vectored thrust is emplo yed, a fully tailless design must rely upon wing control 
surfaces for rudder control. This is usually provided by wing-tip -mou nted 
drag devices, as on the B-2 where the trailing edge spli ts apart to make 
drag. 
Thrust vector stabilization of a no-vertical- tail design was demonst rated 
using the X-3 1. While it had a vertical tail, it used its comp uterized flight 
control system to have the rudder and ailerons delibe rately negate the 
stabilizing effects of the vertical tail. Then, its nozzle thrust vectoring 
system was used to stabilize the aircraft in yaw. The vectoring system 
didn't have quite enoug h control authorit y, so on ly 70% effective tail 
removal could be reached in flight, but this was a good demon stration of 
the technolog yJll ] 
More rece ntly the unmanned McDonne ll Douglas/Boe ing X-36 fighter 
technolog y demons trator validated fully tailless flight. X-36 had no vertical 
tail and was naturally unstable in the yaw axis. It used an advanced thrust 
vectoring nozz le for directional control, making 31 flights. While the X-36 
had a canard for pitch control, it seems likely that future military aircraft 
will have neither vertical nor horizo ntal tail s.


<!-- p.109 -->

CHAPTE R 4 Air foil and Wing /Ta il Geom etry Sel ecti on 10 9 
Fig. 4.36 Tail less futur e airlin er (D. Raymer N+3 study for NASA-GRC) . 
Some fully tailless designs have drooped outer-wing panels for stability 
and control enhancement. These act somewhat like an inverted V-tail and 
provide the desirable proverse roll-y aw coupling with rudder deflection. 
Winglets or endplates mounted at the wing tips can be used in place of a 
vertical tail. This can provide the required vertical tail surface for free because 
the effective increase in wing aspect ratio can more than compensa te for the 
wetted area of the tail. To place these tip surfaces far enough aft to act like 
vertical tails requires either extreme wing sweep or a canard arrangement, 
or both. 
In a major study for NASA, this author applied the tailless approach to an 
otherwise conventional, "tube fuselage" commercial airliner, as seen in 
Fig. 4.36. This was funded by NASA Glenn Research Center (G RC) as part 
of the "N+3" research initiative, with goal of a 70% reduction in fuel consumption vs the current Boeing 737- 800. 
In this new design the elimination of both vertical and horizo ntal tails 
saved 10% in wetted area in the cruise condition, with no pena lties to


<!-- p.110 -->

11 0 Ai rcraf t Desig n: A Concept ual Appr oa ch 
frontal area or structure. Unlike some other advanced airliner conce pts, the 
wings can have typical airliner high-lift flaps. A pop- out canard is sequenced 
with the flaps for balance and control during takeoff and landing. For yaw 
control a small all- moving chin rudder is provided. 
Analysis shows a 60% reduction in fuel consum ption as a result of this 
and other advanced technolog ies-see the contract final report for detail s. fl2l 
Needless to say, a fully tailless, unstable airliner is a high- risk approach and 
suitable only for the distant future. But it ju st might work, and the expected 
benefits are impres sive. 
*'f D Ta il Arrange ment for Spin Recovery 
The vertical tail plays a key role in spin recov ery. An aircraft in a spin is 
esse ntially falling vertically and rotating about a vertical axis, with the inside 
wing fully stalled. The aircraft is also typically at a large sideslip angle. To 
recover from the spin requires that the wing be un- stalled, so the angle of 
attack must be reduced. First, though, the rotation must be stopped, and 
the sideslip angle reduced, or the aircraft will immedia tely enter another 
spin. This requires adequa te rudder cont rol even at the high angles of 
attack seen in the spin. 
Figure 4.37 illustrates the effect of tail arrangement upon rudder control 
at high angles of attack. At high angles of attack the horizo ntal tail is stalled, 
producing a turbulent wake extending upward at appro ximately a 45- deg 
angle. 
In the first example, the rudder lies entirely within the wake of the horizontal tail, so that little rudder control is available. The second example 
Desire- 1 /3 of rudder area to be unblank eted 
I 
I 
Fig. 4.37 Tail geome try for spin recover y. 
I


<!-- p.111 -->

CHAPTER 4 Air fo il and Wing /Ta il Geom etry Selecti on 111 
shows the effect of moving the horizont al tail forward with respect to the 
vertical tail. This "unco vers" part of the rudder, improving rudder control. 
The next example moves the horizo ntal tail aft with respect to the vertical 
tail, with the same result. As a rule of thumb, at least a third of the rudder 
should be out of the wake. 
The next two examples show the effect of moving the horizon tal tail 
upward. The T-tail arrangement compl etely unco vers the rudder but can 
result in pitch-up and loss of elevato r control. 
The last illustration in Fig. 4.37 shows the use of dorsal and ventral fins. 
The dorsal fin impro ves tail effectiveness at high angles of sideslip by creating 
a vortex that attaches to the vertical tail. This tends to prevent the high angles 
of sideslip seen in spins and augments rudder control in the spin. The ventral 
tail also tends to prevent high sideslip and has the extra advantage of being 
where it cannot be blanketed by the wing wake. Ventral tails are also used 
to avoid lateral instability in high-speed flight. 
*f JI Tail Geome try 
The surface areas required for all types of tails are direct ly propor tional to 
the aircraft's wing area, so that the tail areas cannot be selected until the 
initial estimate of aircraft takeoff gross weight has been made. The initial estimation of tail area is made using the "tail volume coefficient" method, which 
will be discussed in Chapter 6. 
Other geometric parameters for the tails can be selected at this time. Tail 
aspect ratio and taper ratio show little variation over a wide range of aircraft 
types. Table 4.3 provides guidance for selection of tail aspect ratio and taper 
ratio. Note that T-t ail aircraft often have lower vertical tail aspect ratios to 
reduce the weight pena lty of the horizont al tail's loca tion on top of the vertical tail. Also, some gener al aviation aircraft use untapered horizo ntal tails 
(A = 1. 0) to reduce manufacturing costs. 
Leading-edge sweep of the horizo ntal tail is usua lly set to about 5 deg 
more than the wing sweep. This tends to make the tail stall after the wing 
and also provides the tail with a higher critical Mach number than the 
wing. This avoids loss of elevator effectiven ess due to shock formation. For 
Table 4.3 Tail Aspect Ratio and Ta per Ratio 
onta l Tail 
Fig hter 3-4 0.2-0 .4 0.6 -1 .4 0.2-0 .4 
Sailp lane 6-1 0 0.3-0 .5 1 .5-2 .0 0.4 -0 .6 
Others 3-5 0.3 -0 .6 l .3 -2 .0 0.3 -0 .6 
T-tail 0.7-1 .2 0. 6-1 .0


<!-- p.112 -->

11 2 Aircr aft De sign: A Conceptual Appr oach 
low-speed aircraft, the horizo ntal tail sweep is freque ntly set to provide a 
straight hinge line for the elevator, which usually has the left and right 
sides conn ected to reduce flutter tendencies. 
Vertical- tail sweep varies between about 35 and 55 deg. For a low- speed 
aircraft, there is little reason for vertical -tail sweep beyond about 20 deg other 
than aesthet ics. For a high-speed aircraft, vertical-t ail sweep is used primarily 
to ensure that the tail's critical Mach number is higher than the wing's. 
The exact planform of the tail surfaces is actua lly not very critical in the 
early stages of the design process. The tail geomet ries are revised during later 
analytical and wind-tunnel studies. For conceptual design, it is usua lly acceptable simply to draw tail surfaces that "look right," based upon prior experience and similar designs, provided that the total area is correct. 
Tail thickness ratio is usua lly similar to the wing thickness ratio, as determined by the historical guidelines provided in the wing-geome try sectio n. For 
a high- speed aircraft, the horizo ntal tail is freque ntly about 10% thinner than 
the wing to ensure that the tail has a higher critical Mach number. 
Note that a lifting canard or tandem wing should be designed using the 
guidelines and procedures given for initial wing design, instead of the tail 
design guidelines alread y descri bed. 
Landing of the super sonic -capable F-86 (pho to from U.S. Air Force) .


<!-- p.113 -->

CHAPTER 4 Air foil and Wing /Ta il Geome try Sel ecti on 11 3 
F-35 Joint Stri ke Fig hter (pho to from U.S. Air Force) . 
What We've Learned 
We've seen how to select reason able values for the wing and tail geometric 
parameters, suitable for that first layout but likely to be revised later. Also, 
we know how the choice of tail arrangement (conventional, canard, etc. ) 
affects the design.


<!-- p.114 -->

11 4 Air c raft Des ign : A Concep tu al Appr oa c h 
Photo cred it: D. Raymer.
