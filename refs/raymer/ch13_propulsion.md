# Raymer Ch.13 - Propulsion

*Converted from `Daniel P. Raymer - Aircraft Design_ A Conceptual Approach (2018, American Institute of Aeronautics and Astronautics Inc.) - libgen.li.pdf` by `tools/pdf_to_md.py`. Page markers are printed page numbers.*


<!-- p.455 -->

CHAPTER 12 Aerody nam ics 455 
shock formation and are very useful for transonic design compared to the 
linearized methods. The pote ntial flow codes are not usually consi dered to 
be true "CFD," but are prob ably the most widely used aerod ynamic codes 
that treat the entire flowfield rather than just the surface conditio ns. When 
a boundary-layer model is added, potential flow codes become even more 
useful for routine design analysis and optimizat ion. 
The "linearized" aerod ynamic codes are based upon a further simplification to the potential flow equations by neglecting the higher-or der terms. It is 
assumed that, because they involve small quantities multiplied by other small 
quantities, they must be very small and therefore negligi ble. At transonic 
speeds, however, these terms are not so small! 
The linearized potential flow equations are the basis of the indu stry 
methods described at the beginning of this section. These include the Harris 
wave drag and the USSAERO and similar panel metho ds. With further simplifications, such early methods as the lifting-line theor y are derive d. 
To recap, only the Large Eddy, Reynolds -averaged, and PNS codes are 
consider ed to be true Navier-St okes c;:odes. However, the Euler, pote ntial 
flow, and linearized aerodynamic codes are in fact successi ve simplifications 
of the NS equations. The choice of code for a given design problem depends 
upon the nature of the problem and the available budget (and not always in 
that order! ). 
If m Appl icat ions of CFD 
CFD does not replace the wind tunnel. In fact, it doesn't really reduce the 
number of wind-tunnel test hours, although it might cap the historical 
upward spiral in wind-tunnel hours (ro ughly one order of magnitude per 
decade) . 
CFD does permit you to design a better airplane by a truer understanding 
of the flowfield around it. Not only do the CFD codes determine the entire 
flowfield around the aircraft, but also, unlike the wind tunnel, the flowfield 
determination is done at the full-s cale Reynolds number. 
A perfect example of the use of CFD can be found at every major 
commercial airport in the cou ntry. The installation of the fuel- efficient 
CFM-56 engine on the Boeing 737 would not have been possi ble without 
the use of CFD, as described in [22l . 
The original Boeing 737 used the P&W JTSD, a low-bypass-r atio engine 
that was moun ted in a wing-con formal nacelle. The nacelle barel y cleared the 
ground, providing a minimum -weight landing gear. 
When Boeing decided to develop an updated version of the 737, the 
CFM-56 engine was the logical choice as a modern fuel- efficient engine of 
the required thrust class. However, it has a diameter some 20% greater 
than the old engine. Furthermore, the CFM-56 exits its fan air up front 
like most modern turbofans. For this reason, a wing-con formal nacelle was 
not possible.


<!-- p.456 -->

456 Ai rcraf t Design : A Concep tu al Appr oach 
In an earlier chapter, the cited rough rule of thumb for podded jet nace lles 
said that the inlet should be about two inlet diam eters forward of the 
wing and about one inlet diameter below it. A more refined empirical 
method of locating a turbofan engine indicated that the geom etry shown 
in Fig. 12 .41a was the closest acce ptable nacelle spacing. Clear ly this posed 
a ground clearance problem! 
The emp irical rules for nacelle spacing were based upon years of trial and 
error in the wind tunnel. Closer spacings were found to increase cruise drag, 
although the wind-t unnel investigations had not clearly determined jus t 
exactly what this "inter ference" drag consisted of. Various suspe cts include d 
increased skin friction due to super velocity, increased separation, shock 
effects, and a change in the wing's spanwise lift distribution resulting in an 
increase in the induced drag. 
Through the use of a nonlinear potential flow pane l program ( CFD state 
of the art in the 197 0s), Boeing was able to determine that it was in fact the 
induced drag effect that was creat ing the "interference drag." This impor tant 
piece of info rmation had not been determined in 20 years of wind- tunnel 
testing! 
With this information, Boeing was then able to contour a clos ely spaced 
podded nacelle to prevent any change in the wing's spanwise lift distribution. 
This was possible with CFD because the entire flowfield is sol ved, allowing 
the designers to study the streamlines and pressure fields res ulting from 
various design changes. The designers sought to minimize the impact of 
the nacelle on the streamlines of the bare wing. 
Figure 12.41b shows the resu lt, namely, a nacelle of extremely close 
spacing to the wing that, nevertheless, has acceptable drag characterist ics. 
The formation and effects of vortices at high angles of attack repres ent 
another area of substantial concern to the designers of fighter aircraft. 
These vortices produce compl etely different lift, drag, and pitching-m oment 
characteristics than those that would be predicted using the linear methods. 
a) "Rule -of-thumb " nacelle ins tal lation b) CFO-design nacel le ins tall ation 
Fig. 12 .41 CFO example -Boe ing 737 nac elle (after R. Bengelink , AIM Paper 88-2043) .


<!-- p.457 -->

TEAM 
com putations 
(49 x 145 x C-H) 
Measurements 
CHAP TER 12 Aerodyn amic s 457 
Cp 
0.20 
0.00 
-0.20 
-0.40 
-0.60 
-0.80 
r 
- 1. 00 
?lfiic", 
-4 -l. 20 
_J -1. 40 
' 
\_ - 1. 60 
- 1. 80 
-2.00 
-2.20 
-2.40 
-2.60 
-2.80 
-3.00 
-3.20 
Fig. 12 .42 Correlation of compu ted and measur ed surface pressur e contours; 75-deg/62-deg 
double -delta wing body; Moo = 0.3; a= 20 deg ([83]; repri nted with perm ission) . 
Reference [83] details the CFD solution of a typical vortex-flow problem 
using a Lockheed Euler code called TEAM (Thr ee-D imensional Euler Aerodynamic Method) . Figure 12. 42 shows the close match between the calculated and the measured pressures over the double- delta configuration used 
in the study. The vortex region can be seen by the diago nal pressure contours 
in both calculated and measured plots. 
Figure 12 .43 illustrates the power of CFD to fully analyze the flowfield 
around the aircraft rather than just at the surface. This figure shows streamlines around the Ohio Airships Dynalifter, a hybrid airship with wings and a 
lifting body. CFD was used to predict drag and optimized shaping. l17l 
Perhaps the most impor tant application of CFD is the inverse problem: 
given a desired aerod ynamic characteristic, what is the geometry to make 
it happen? This is the subject of vigorous research, and there has been 
great progress in using comput erized methods to aerod ynamically optimize 
external geom etry. Emerging methods such as those described by Jameson


<!-- p.458 -->

458 Air craf t Design : A Conceptual Approach 
et al. [85] apply control theor y techniques to optimize aerod ynamic shapes 
using NS equations mode ling viscous compressible flow. In these techniques , 
an initial aircraft geomet ry is modified iteratively using one cycle's result 
to specify an improved geom etry for the next cycle. Resu lts for a sample 
transport aircraft optimizat ion show the elimination of wing shocks at 
Mach 0.83 and produce a 15-c ount drag reduction (8%). 
More often, though, we use CFD to iden tify problems such as shoc ks, 
unwanted vortices, component interactions and flow separation, and then 
use designer intuition to revise the geo metry in hopes of solving the 
problem. As the previous example showed, this works very well! 
Mf IJI CFO Issues and Challe nges 
We have come a long way since 18 79 when the annual proce edings of 
the British Royal Aerona utical Society could say, "Mathematics up to the 
present day has been quite useless to us in regard to flying" (quoted inl22l). 
However, there are still many problems asso ciated with the use of CFD for 
routine ly solving aircraft design problems. Two problems are especia lly 
impor tant: the influence of the turbulence model and the requiremen ts for 
flow gridding. 
The use of sep arate turbulence models for NS codes has been discussed. 
The results of the various NS codes are very sens itive to the turbul ence model 
used, espec ially when sep arated flow is present. 
CFD codes tend to produce reasonable-looking flowfields and pres sures, 
but sometimes the integration of the calculated pressures yields lifts, drags, 
and mome nts that do not match experience. Reproduction of experimental 
data sometimes requires extensive "calibration" (i.e., fudging) of the turbulence model. For this reason, CFD results are always some what suspect 
until the code has been checked against experiment al data for a similar 
confi guration. 
( 
Fig. 12 .43 CFO strea mlin es an dyna mic lif t air ship.[ 841


<!-- p.459 -->

15. 0 
JO .O 
5.0 
z 0.0 
-5 .0 
-1 0.0 
5.0 
10 .0 
15 .0 
20.0 
25.0 
30.0 
35.0 
40.0 
x 45.0 
CH APTE R 12 Aerodyn amics 459 
50.0 
55.0 
60.0 
65.0 
70.0 
75.0 
0.0 
-5 .0 
-10 .0 
-1 5.0 
-20.0 y 
-25.0 
Fig. 12 .44 Flowfield gridding ((82]; repri nted with permission) . 
The need to grid the entire flowfield around the aircraft prese nts another 
big problem for CFD users. "G ridding" refers to the breaking up of the space 
around the aircraft into numerous small blocks, or "cells," usually of roughly 
hexahedral shape. CFD methods calcula te the flow prop erties within each 
cell, using various convergence schemes to equate the flow properties 
along the bou ndaries connecting the cells. 
While gridding the space around a simple geomet ry is easy, the gridding 
around a full aircraft cannot yet be fully automated. The time required has 
gone from months to weeks and is now down to days, but it is still an unacceptable bottleneck. We designers want the answers, right now! Figure 12 .44 
illustrates the comple xity of the flowfield gridding. Note, for example, where 
the canopy meets the fuselage and where the cells must fan out in the empty 
region between wing and canard. 
Gridding is especia lly impor tant because the CFD results are highly 
sensitive to the shaping of the cells. You can actually get different answers 
for the same aircraft using two different gridding schemes. According to 
the author of186l , "this sens itivity is more pronounced than that due to the 
type of mathematical model being used, e.g., NS vs. Euler equat ions." 
To address the gridding problem, researchers are investigating 
artificial intelligence (AI) approaches to gridding. Another approach is the


<!-- p.460 -->

460 Ai rc raft De sign : A Concept ual Approach 
comp utatio nally adap tive gridding in which the gridding scheme is automatically adjus ted based upon the CFD results. 
A pro mising approach to developing automatic and instantaneous gridding for CFD is the "unst ructured grid ." The grid of Fig. 12 .44 is highly structured. It begins at the outside bou ndaries as simple brick-like shap es and 
transitions to the aircraft surface in a smo oth and structured fashion. 
While this makes it easier for a human to create a reason able grid, it is act ually easier for an automated computer routine to create a grid that does n ot 
look like a brick wall with an aircraft -shaped hole in the center. 
Instead, the unstructured grid typically uses tetrahedral cells that connect 
at their vertices and can be placed as needed to complete a three-dimensional 
grid of the flowfield. Rather than a brick-w all appea rance, the unstructured 
grid looks like the work of a demented spider attempting to capture your aircraft! With the unstructured appro ach, the grids can now be generated in just 
a few days. 
With unst ructured grids it is relatively easy to automa tically reduce the 
size of the cells where the flow properties are changing, such as around 
corners, to improve the accurac y of the CFD calculat ion. It is also easier to 
do this during execution (adaptive gridding) , so that the beginning grid 
pattern need not be quite so perfect. Another advantage of the unstructured 
grids is that they lend thems elves to parallel computer impleme ntation, 
which provides reductions in execution time and com puter costs. 
Problems of unst ructured gridding include computational difficulties 
with viscous terms, tendencies to have regions of dist orted cells, and computationa lly expensi ve flow solver routines. l87l But, unstructured grid CFD 
Fig. 12 .45 Uns tructured grid .


<!-- p.461 -->

CHAP TE R 12 Aerodyn ami cs 461 
programs are gaining wider acceptance and offer great promise for the future. 
Figure 12.45 illustrates an unstructured grid for an airfoil. Note how during 
iteration the flow solver has clustered small grids where it found large 
changes in pressu re, such as at the leading edge and through shocks. This 
increases compu tational accura cy. l88l 
As with structural finite element methods, most working aerod ynamic 
engineers will never be involved in writing CFD codes. The state of the art 
has advanced to the point where even big companies use commerc ial 
codes rather than attempt to write and maintain their own propr ietary 
codes. Instead, the working engineer must learn to use the available codes, 
understandin g their applicab ility and limi tations. Compl ete CFD analys is 
includes grid generation, flow definition (including initial conditions, properties, a ssumptions, and boun dary cond itio ns), calibration of the turbul ence 
model, code execution, postprocess ing, and evaluating and understanding 
the results . Finally, the CFD expert must provide the results to the aircraft 
designers in a manner that guides the improvement of the design. 
Cp 
1. 00 
-1 .00 
CFD ana lysis of the Gee Bee Racer (cou rtesy of David Led nic er/Ana lytica l Methods, Inc.). 
What We've Learned 
We've learned classical methods to calculate the aerodynamics of our conceptual design layout including maximum lift, parasi tic drag, drag due to lift, and 
supersonic wave drag. Better results are later found using CFD.


<!-- p.462 -->

462 Ai rcraf t Desig n: A Con ceptu al Approach 
Mig 29.


<!-- p.463 -->

Propulsion 
• Propul si ve th rust an d fuel con sump tion ar e ca lcu lated for the as-i nsta lle d engine. 
• Man ufacturer's da ta for fuel ftow an d jet th rust or engine shaf t power ar e obta in ed 
and adjus ted. 
• Propeller efficie ncy is used for th rust. 
• Powe r and dr ag los ses ar e applie d . 
• We sta rt with a simple th rust mod el. 
Air craft Th rust-The Big Pic tu re 
M ost forms of aircraft propulsion work by taking in air and then 
pushing it out the rear at a higher velocity. The fuel-gasoline, 
kerosene, or electri city-j ust provides the power to make it 
happen. To obtain a "big picture" unde rstanding of this, we begin propulsion 
analysis with the simple aircraft thrust model shown in Fig. 13.l, to which we 
will apply a version of Newton's famous equation, F =m a. 
This simplified geo metry has an oncom ing stream of air at initial velocity 
Vo passing through a "magic disk" of cross-s ectional area S, after which it has 
somehow acquired final veloc ity V. 
While we often write our equations as if the world is a wind tunnel with 
the airplane station ary and the air coming at it, the reality is the opposite. 
This model represents a generic aircraft propulsion system-a perfect propeller or a very short jet engine - which is actually flying through the air 
at velocity Vo and accelerating the air it enco unters by a change in velocity 
equal to (V - Vo). Subscript zero indica tes the freestream condition, and 
the mass flow of air passing through the disk is easily found as air density 
times vel ocity times cross- section area S. Newton's equation, redefined for 
fluid flows, states that the force produced equals the mass flow rate times 
the applied change in velocity, leading to Eq. (13.1). 
463


<!-- p.464 -->

464 Aircr aft Desi gn: A Concep tual Approach 
Fig. 13 .1 Simpl ified thrust ana lysis model . 
v 
The rate of useful work done by the propulsion system, called the thrust 
power Pt, equals the product of the thrust force and the aircraft velocity 
[Eq. (1 3.2 )]. 
The change in kinetic energy (i.e., work) impar ted to the fluid by the 
propulsion system is determined by the difference in fluid velocity. Taking 
the time derivative of work gives the power expended by this propulsion 
system, as shown in Eq. (13.3). 
The propulsion efficie ncy 1JPE is then defined as the ratio of thrust power 
obtained to power exp ended, as obtained in Eq. (1 3.4). This implies that the 
efficiency is maximized (= 1) when the velocities are the same (V = Vo). In 
other words, the best thrust efficiency occurs when there is no acceleration 
of the fluid flow. Unfortun ately, at this condition Eq. (13.1) shows that the 
thrust is zero! 
F =m a= mLlV = (pVS)(V - Vo) = pSV(V - Vo) 
Pt = FVo = pSV(V - Vo) Vo 
fJAE 1 . 2 1 . 2 1 2 2 Pt =-=- mV - -m V0 = -pVS(V - V0) expended fJt 2 2 2 
= pS V(V 2 VJ) 2 
Pt 
1JPE = Ptexpended 
2 
V/Vo + 1 
(13.1) 
(13 .2) 
(13. 3) 
(13.4 ) 
This simple an alysis shows that there is an unavo idable tradeoff between 
thrust and efficienc y, determined by the ratio between exhaust and freest ream 
fluid velocity. For maximum thrust, this ratio should be very high. For 
maximum efficiency, this ratio should be low-act ually unity. 
If maximum efficiency is desired, literally more thrust per unit power of 
the engine, then the change in veloc ity (V - Vo) must be as small as possi ble.


<!-- p.465 -->

CH APTE R 13 Pro pu lsion 465 
To get a reaso nable amount of thrust with such a small change in veloc ity, the 
cross-sectional area S must be as large as pos sible. This explains why helicopters have such large rotors and why propellers are more ef ficient than jets 
(at least at lower speeds ). 
A typical turboj et will operate with the ratio of 
exhaust velocity to freestream velocity at well 
above 3.0, whereas a typical propeller aircraft will 
operate with this ratio at about 1.5. 
The previous analysis is too simplistic for actual 
thrust calculation. It falsely assumes that the fluid 
velocity is const ant throughout the exhaust and 
that all of the accelerat ions experienced by the air 
Thrust is produced 
efficiently by 
applying a small 
change in flow 
velocity to a large 
cross section of 
oncoming air. 
mass occur at the propeller plane or within the jet engine. 
Actually, the exhaust of a jet engine is usua lly at a higher press ure than 
the outside air, so the flow expands after leaving the nozzle. In other 
words, the air is still accelerating after the aircraft has passed. For a propeller, 
the air-mass acceleration doesn't even. occur at the propeller disk. Roughly 
half the air-mass acceleration occurs before reaching the propeller, and the 
other half occurs after passing the propeller. 
Propulsion force estimation is also complicated by the fact that the 
propeller flowfield or the jet intake and exhaust will influence the whole 
flowfield of the aircraft. A pusher propeller will reduce the drag of a stubby 
aft fuselage by "sucking" air inward and preventing flow separat ion. Should 
this reduced drag be considered a part of the propulsi ve force because it is 
controlled with the throttl e? What about the increased drag due to the 
propeller wake on a conventional airplane? What about the freestream 
airflow acceleration that viscos ity causes near a jet exhaust, which can 
increase the dynamic pressure on nearby aircraft surfaces? These must be 
a part of a detailed propulsion analy sis. 
For a propeller aircraft, most of the propulsi ve force is exerted on the 
aircraft by the pull or push of the propeller shaft and then through 
the engine mounts. For a jet aircraft the force exerted through the engine 
mounts might only be a third of the total propulsi ve force, making analysis 
more difficult. To illus trate the comple xity, Fig. 13.2 shows the thrust contributors for a typical Mach 2.2 nacelle. The engine itself only contrib utes 
about 8% of the total. The nozzle, which generates thrust by expanding 
the high-pressure engine exhaust, contributes another 29%. So the force 
exerted through the motor moun ts onto the airframe is 37% of the total 
thrust. Where is the rest? 
The inlet system uses a system of shocks to slow the air to a subsonic 
speed. This creates a substant ial drag, making a 12% pena lty. So now we 
are missing a net of 75% of total thrust. Where is it? 
As the figure shows, it is the internal pressu re within the inlet duct that 
contributes the missing thrust. Inside the inlet duct, the dynamic press ure 
of the outside freestream air has been largely converted to static pressure


<!-- p.466 -->

466 Aircr aft De sign: A Conceptual Approach 
Mach 2.2 - Net th rust = 10 0% 
-12 % +75% +8% +29% 
Fig. 13 .2 Turbojet thrust contri butors (Nor th American Aviation A-5) . 
by the external shocks and internal subsonic expan sion of the flow. In fact, it 
is the forward componen ts of that massi ve pressure, acting on the walls of the 
duct, that pushes the airplane through the air. 
This example illust rates the difficult y of calculating jet thrust by any 
simple model. Of course, this effect is exaggerated at high super sonic 
speeds. In subsonic flight the thrust is prim arily- but not compl etelyfrom the engine's push on the motor mounts. 
The remainder of this chapter presents methods for estimating the net 
thrust provided by a propeller or je t engine as a part of the overall vehicle 
analysis and optimizat ion. These methods are suitable for initial design analysis by the aircraft des igners and are rapid enough for use in a college design 
course. The chapter will also introduce the more compli cated process of 
install ed-t hrust estimation used at major aerospace firms. Reference (42] 
provides a detailed treatment of jet-engine design and installation. 
Jet -Engine Th rust Consider ations 
As des cribed in Chapter 10 , a je t engine develops thrust by taking in air, 
compressing it, mixing in fuel, burning the mixture, and acceler ating the 
resulting high- pressure, high-temp erature gases out the rear through a 
nozzle (Fig. 13 .3) . To provide power to drive the compressor , a turbine is 
placed in the exhaust stream, which extracts mechanic al power from the 
high-pressure gases. 
If greater thrust is required for a short period of time, an afterburner can 
be placed downstream of the turbine perm itting the unburned air downstream of the turbine to combust with additional fuel and thereby increase 
the exhaust velocity. Afterburning (or "reheat") is common for sup ersonic 
aircraft, for which the nozzle must accelerate the exhaust to sup ersonic 
speeds to obtain any thrust. Thus, a converging- diverging nozzle is employe d, 
and it must allow varying both throat and exit area to be efficient at all operating conditions. For a subsonic je t airc raft, only a simple converging nozzle 
is needed, usually of fixed geomet ry.


<!-- p.467 -->

CHAPTER 13 Propuls ion 467 
"Gross thrust" results from the total momentum in the high-v eloc ity 
exhaust stream. "Net thrust" is calculated as the gross thrust minus the 
"ram drag," which is the total momentum in the inlet stream. Note that 
the ram drag, which results from the deceler ation of the air taken into the 
inlet, is included in the engine cycle analysis performed by the engine 
manufacturer to determine net uninstalled thrust. Airplane designers don't 
have to calculate it. 
Jet-engine cycle analysis, as detailed in[42l and other propulsion texts, is 
the straightforward application of the laws of thermody namics to this 
Brayton engine cycle. In an "ideal" analysis, the efficiencies of componen ts 
such as comp ressors and turbines are assumed to be 100%, that is, no losses, 
and the result ing thrust is calculated for a given fuel flow, altitude, and Mach 
number. While optimistic, such ideal cycle analysis is useful to the engine 
designers because it illustrates the trends produced by varying parameters 
such as overall pressure ratio, turbine inlet tempera ture, and bypass ratio, 
without the "clutter" of specific component estima tions. However, ideal 
cycle analysis is inapprop riate for use ii} aircraft design studies. 
One overriding factor in the determination of jet-engine performance is 
that the net thrust produced is roughly propor tional to the mass flow of air 
entering the engine. Whereas for a piston-pr opeller aircraft, the power produced doesn't increase with speed, so the thrust reduces with speed, in a jet 
the power does increase with speed. More air "down the hole" means that 
more fuel can be in jected and as a result, more power is produced. Rather 
than seeing a reduction in thrust as speed is increased, jets will show an 
increase in thrust until the speed is so high that inlet drag or shock effects 
become dominant. 
For a modern afterburning turboj et engine, roughly 100- 130 lb of thrust 
is developed for each pound per second of air taken in by the engine 
{1- 1.3 kN per kg/s}. This is called the "spe cific net thrust" based on 
airflow. For a turbofan engine, a specific net thrust of roughly 10-30 [0. 10.3] can be obtained (sea- level maximum static thrust) . 
Afterburner 
Fig. 13 .3 Turbojet engine.


<!-- p.468 -->

468 Air craf t De si gn: A Concept ual Appr oa ch 
Because thrust depends upon the air's mass flow, an increas e in air 
dens ity increases the thrust and vice versa. Hot day takeoffs from a highelevation airport such as Denver pose problems because the reduc tion in 
air dens ity causes a reduction in mass flow and, hence, thrust. This loss of 
thrust is compounded by the reduced wing lift in the thin air, making 
takeoff a real challenge. 
The effect of air densit y on jet-engine thrust can be approxim ated as 
the thrust at sea level for a given speed, multiplied by the ratio of air 
pressures and divided by the ratio of absolute air temperatures, relative 
to sea-le vel values. Pressures and temperatures for different altitudes can 
be found in Appen dix B. A simpler ad jus tment for temper ature, for 
hot- day oper ation thrust, can be reduced about 0.42% per 0R {0.75% 
per K}. 
Simil arly, an increase in aircraft veloc ity should increase thrust due to 
the ram effect increasing the mass flow. However, for a typical subsoni c 
jet the exhaust comes out the nozzle at a choked condition, so the exit 
velocity about equals the speed of sound regard less of aircraft velocity. As 
aircraft veloc ity approaches the speed of sound, the thrust is therefore 
reduced. When combined with the favorable ram effect, this results in a 
relatively constant thrust as veloc ity increases for the typical subs onic jet, 
dropping off as transo nic speeds are reached. 
For supersonic jet engines, a variable- area, converging- diverging nozzle 
is typically employed, which permits supersonic exhaust velocities. Therefore, the ram effect does cause the thrust to tend to increase with increasin g 
veloc ity until at high Mach numbers where excessi ve total pressure losses 
occur in the inlet, resu lting in thrust degradat ion. The Mach number at 
which inlet losses become excessi ve is determined by the number of 
shocks and the extent of variable geome try emplo yed, as described in 
Chapter 10. 
Thrust and propulsi ve efficiency are strongly affected by the engine's 
overall pressur e ratio (OPR ). OPR is the ratio of the pressures at the 
engine exhaust plane and inlet front face. This pressure ratio is a measure 
of the engine's ability to accele rate the exhaust, which produces thrust. 
OPRs usually range from about 15 to 1 to about 30 to 1. 
Another key parameter for turbine engine performance is the turbine 
inlet temp erature (TIT, also called turbine entry temp erature or combustor 
discharge temperat ure) . As mentioned earlier, maximum thrust and efficiency would occur with comb ustion at the stoichio metric air-fuel ratio of 
about 15 to 1. This produces temperatures far too high for current turbine 
materials, even using the best available cooling techniques. 
Instead, a more lean mixture of about 60 to 1 (air to fuel) is used, with 
the extra air keeping the combustor temperatures cooler. Unfortunatel y, 
this lean mixture results in less thrust and thermal efficie ncy. Prob ably the 
single greatest factor in the improvement of jet engines since the 1940s has 
been the increase in allowable TIT, on average roughly 320°F {1 80°C } per


<!-- p.469 -->

CHAPTER 13 Prop ul sion 469 
Fig. 13 .4 Turbofa n engine. 
decade. The earliest jets had values of around 15 00° F {800° C}. Today's typical 
values are about 2000-2500° F {"-' 11 00-14 00°C}, with the newest designs 
reaching 2900°F {16 00° C}. Perhaps some day the true stoichio metric jet 
engine might be possible. It will have much greater thrust and efficienc y, 
but how will we give it afterburning? 
To increase the propulsi ve efficienc y, the turbofan engine uses an oversized fan with some of the accelerated fan air "bypassed" around the 
engine, not being used for combustion (Fig. 13. 4). This has the effect of allowing the engine to accel erate a larger cross-s ectional area of air by a smaller 
change in velocity, which increases efficienc y as determined by Eqs. (13.1) 
and (13 .4) . The bypass ratio was defined in Chapter 10 as the ratio of the 
mass flows of the bypassed air and the air that goes throug h the core of 
the engine to be used for combustion. 
A higher bypass ratio, which enables the engine to accelera te a larger 
cross section of air, produces higher efficienc y and hence greater thrust 
for a given expenditure of fuel. However, the fan alone cannot efficiently 
accelerate the air to trans onic or supersonic exit speeds, so this favorable 
effect works only at lower speeds. Furthermore, the greater intake crosssection area of a high-by pass -ratio engine leads to a greater momentum 
ram drag, which increases roug hly by the square of the airsp eed. As was 
shown in Fig. 10.2, the high bypass turbofan is best at subsonic speeds, 
giving way to the low-by pass ratio turbofan at the low supersonic speeds. 
At higher supersonic speeds, much over Mach 2, the pure turboj et is 
superior. 
Several new turbofan engines are using gears between the fan and its 
turbine, to better match the preferred oper ating rpm of each. These 
"geared turbofans" allow higher and higher bypass ratios, but if the fan is 
too large, the drag and weight of its duct and cowling become excessi ve. 
This leads to the idea of the open rotor or prop-fan, discussed below. 
Q Jet-Engine In stal le d Th rust 
The airplane designers don't design the engine. Experts at the engine companies do that, and then they work with the airplane designers. The engine


<!-- p.470 -->

470 Air c raf t Desi gn: A Conc eptu al Appro ach 
comp any experts also calculate the performance of their engines, which the 
airplane designers usually use rather than attempt to do it thems elves. 
Engine performance analysis methods, called "cycle" analysis because they 
are based on the thermodynamic cycle, are introduced in[42l . 
When analyzing engine performance, assumptions must be m ade for 
parameters such as inlet duct efficienc y, power extracti on, and nozzl e 
performance. Unsurprising ly, the engine company experts tend to make 
assumptions that make their engine look good -wouldn't you? When applying these engine comp any results the airplane designers must adjust those 
results to better reflect how the engine will actually perform in the air. W e 
call this "installation analysis," and it is discussed in the subchapter s that 
follow. 
"Uninst alled" engine data can be obtained from the engine manufacturer , 
at least if you represent a serious aircraft design compa ny or governmen t 
design office. Data for several conce ptual engines suitable for quick studies 
and student proj ects are summarized in the appendices. 
It is also common early in design studies to approximate the perfo rmance 
of a new design engine by a "fudge-factor" approach. An existing engine 
with appro ximately the same bypass ratio is selected, and its size, weight, 
and performance data are multiplied by factors based upon the expected 
improvements by applying advanced technologies. 
For example, it might be assumed that an engine designed 10 years 
from now would have 25% less specific fuel consum ption, 30% less length, 
and 30% less weight compared with an existing engine. Such fudge factors 
are based upon either historical trend analysis or an approximate cycle analysis for expected technolog y improvements. 
Thrust-Drag Bookkeeping 
Book keeping is not normally consi dered an engineering subject. 
However, the interactions between thrust and drag are so complex that 
only a bookkeeping-like approach can ensure that all forces have been 
counted once and only once. 
In aircraft performance analysis, thrust and drag are never consid ered 
alone. The relevant terms in the performance equations always say "thrust 
minus drag." Drag items that relate to the engine could be included in the 
aerod ynamic department's drag tables, or they cou ld be included in the 
propulsion depa rtment's thrust tables by subtract ion. The effect on performance would be the same, so the only question is, which is easier? 
Each aircraft comp any develops its own system for thrust- drag bookkeeping. In most cases the guiding principle is whether that force changes 
when the throttle setting is changed. 
In an afterburning jet engine, the nozzles open wide when the throttle is 
advanced to the afterburning posi tion. This changes the aerod ynamic drag on 
the outside of the nozzles, so the entire nozzle aerod ynamic drag could be 
counted as a reduction in the engine thrust. However, this makes the


<!-- p.471 -->

CHAPTER 13 Propulsion 471 
aerodynamic drag tables seem incom plete because there is no value at all for 
nozzle drag. 
Probably a better way to handle the nozzle thrust- drag book keeping is 
to separate the nozzle drag into two compo nents, namely, the drag value 
at some fixed nozzle setting (usually full open), which is included in 
the aerodynamic drag data, and the variation of drag as the nozzle setting 
is changed, which is included as a subtraction in the propulsion installation 
data. 
Either bookkeeping approach will give correct results providing that the 
aerodynamics and propulsion departments both under stand it. It is not 
uncommon to discover, halfway through an aircraft design project, that 
some minor drag item has been either included in both the drag and the 
thrust calculations or has been ignored by both departments under the 
assumption that it is being included by the other! 
Thrust-dr ag bookkeeping becomes especi ally complex when sorting out 
the results of wind-tunnel testing. Different wind-tunnel models are used to 
test different thrust and drag items. T-e model used for determining basic 
aerodynamic and stability derivatives is usually unpo wered, and a separ ate 
powered model is used to estima te propulsion effects. Lack of a mutu ally 
understo od bookkeeping system by both the aerod ynamic and propulsion 
departments will cause chaos. 
The student should realize that the organization of this book assumes a 
thrust-drag bookkeeping system. Items presented in this chapter as 
reductions to thrust can be considered to be drag items in another bookkeeping system. Reference [ 67] cont ains a detailed review of the subject of thrustdrag bookkeeping. 
Installed Thrust Procedure 
The "installed net propulsi ve force" is the thrust force to be used in 
aircraft performance calculat ions. This is the unin stalled thrust corrected 
for installation effects, minus the drag contributi ons that are assigned to 
the propulsion system by the thrust- drag bookkeeping system in use. This 
correction procedure is depicted in Fig. 13.5. 
The "manufacturer's unin stalled engine thrust" is obtained from the 
engine comp any. For a proposed future engine, it is developed by cycle analysis. For an existing engine, it is found by testing. Whatever t_he source, the 
manufacturer's engine data include assumptions as to inlet efficienc y and 
distortion , engine bleed, engine power extraction, nozzle performance, and 
other factors. These are usually optimistic, and in some cases the losses are 
assumed to be zero. 
The engine thrust data are therefore corrected based on values of these 
parameters, which are reasona ble for the aircraft being analyzed. There are 
very detailed methods for estima ting those parameters that are used by the 
propulsion departments in the airplane companies. Simplified methods will 
be presented below. The corrected thrust values are then called "installed


<!-- p.472 -->

472 Air c raft De sign: A Concep tu al Appr oach 
Man ufactu rer's 
uni nst alle d 
engine thr ust 
·Ass um ed in let 
press ure recove ry 
·Ass um ed ble ed and 
powe r extr action 
·No dis tortion 
·Manuf actu rer's nozzle 
·Ca ution: Given SFC 
applie s to this th rust 
Less inst al lation 
In stalled 
engine 
thrus t 
·Actual pressur e 
recovery 
·Actual ble ed and 
powe r extra ction 
·Distortion effects 
·Actual nozzle 
performanc e 
Fig. 13 .5 Ins tall ed thr ust method olo gy. 
Ins talled net 
propulsi ve 
force 
·In let drag 
•No zzle & scru bbing 
drag 
·Throt tle-dependent 
trim drag 
engine thrust, " predictions of the thrust that will be generated by the engine 
when installed in that aircraft (middle illustration in Fig. 13 .4) . 
Further corrections to the installed thrust must be made to account for 
the aerod ynamic drags assoc iated with propulsion. These depend upon the 
thrust- drag book keep ing scheme employed. Often it is assumed that the aircraft is at maximum throttle for aerod ynamic drag calculations, with nozzle 
wide open and maximum mass flow down the inlet duct. The "drag model" 
includes this geomet ry, and any changes to drag resulting from a reduction in 
throttle setting get applied to the thrust. 
In addition, a change in throttle setting can cause a change in trim drag. 
A nozzle at the bottom of the aircraft will create a nose-up pitching 
momen t. If the trim drag required to coun teract that moment is include d 
in the aerod ynamic drag when thrust is at a maximum, a reduction in 
thrust will cause a reduction in that nose-up moment requiring a change 
in elevator trim. This will increase or decrease the drag, which must be 
calculated and used to adjust the net thrust according ly. This is often 
ignored in the initial aircraft analysis but must be included in a detailed performance calculat ion. 
So, the final "installed net propulsi ve force" is found as the installe d 
engine thrust minus the increments in inlet, nozzle, and throttle- depe ndent 
trim drags. 
Note that the SFC values supplied with the engine are based upon the 
manufacturer's uninstalled engine thrust, not the installed net propulsive 
force. When determining fuel usage, the SFC values must be adjuste d


<!-- p.473 -->

CHAPTER 13 Propulsion 473 
accordingly. While there are several ways to do this, it seems less confusing to 
take the uninstalled SFC values, convert them to fuel mass flow, calcula te the 
installed net propulsi ve force, and then divide to find the installed SFC. 
Next, the various steps as alread y described and depicted in Fig. 13.5 
are detailed. 
lffll Th rust Instal lation Correc tions 
The manufacturer's uninstalled engine thrust is based upon an assumed 
inlet press ure recovery, the total pressure at the engine front face (lo cation 1) 
divided by the total pressure in the freestream (loca tion O). For a subsonic 
engine, manufacturer's engine data usua lly assume that the inlet has 
perfect recovery, that is, Pi/ Po = 1. 0. 
Supersonic military aircraft engines are usua lly defined using an inlet 
pressure recovery of 1. 0 at subso nic speeds and at supersonic speeds, the 
inlet recovery defined by Mil-Spec MIL-E- 5008B [Eq. (1 3.5)) . Figure 13 .6 
shows this reference inlet press ure recovery plotted vs Mach number, 
compared to the recovery available for a normal -shock inlet and external 
compression inlets with one, two, and three ramps. Note that this widely 
used Mil-S pec pressure recovery schedule does not actually represent any 
particular inlet shock system. 
(Pi) = 1 - 0.0 75 (Moo - 1) 1.35 
Po ref 
(13.5 ) 
Figure 13 .7 provides the actual inlet pressure recoveries of some existing 
designs. These values can be used for pressure recovery estimation during 
early design studies if other data are not available. 
0.9 
0 0.8 
$ 
c( 
0.7 
0.6 
0.5 0 
MIL -E-5008 B 
- - - - - Mi xed 
com press ion 
External 
com press ion 
0.5 1.0 1.5 2.0 
Mach numb er 
Nor mal 
shock 
2.5 
- - Cone } lsentr opic 
spik e Cone 
Ramp ) 4-shock 
' Cone } 
Cone 3-shock 
Ramp 
3.0 
Fig. 13 .6 Reference and avail able inle t press ure recovery.


<!-- p.474 -->

474 Air craf t Desi gn: A Conceptual Appr oach 
0.95 
0.90 
0.85 
0.80 
Ideal 
mi xed-c ompr essio n 
isentropic spik e 
in let 
-F-16 F- 1 04 F-1 5 
• 
MIL -E-5008 B 
0.75 -----------------------0 0.5 1. 0 1.5 2.0 2.5 
Mach numb er 
Fig. 13 .7 Actual inle t pressur e recove ries. 
3.0 3.5 
The pressure losses inside the inlet duct must also be accounted for. 
These losses are determined by the length and diameter of the duct, the presence of bends in the duct, and the internal Mach number. 
For initial evaluation of a typical inlet duct, an internal pressure recovery 
of 0.96 for a straight duct and 0.94 for an S duct can be used. The short duct 
of a subsonic podded nacelle will have a pressure recovery of 0.98 or better. 
More detailed estimation of inlet internal -pressure loss is based upon experimental data (see (46] ) and requires a separ ate evaluation at each Mach 
number. 
A worse inlet pressure recovery has a greater-t han-pr opor tional effect 
upon the engine thrust and can be estimated by Eq. (13 .6) . The inlet ram 
recovery correction factor Cram is provided by the manufact urer for 
various altitu des, Mach numbers, air temperatures, and thrust settings . 
Typically, Cram ranges from 1. 2-1 .5. If the manufacturer's data are not 
available, Cram can be approximated as 1.35 for subsonic flight and by 
Eq. (13 .7) for supersonic flight. 
Percent thrust loss = Cram [ (p1) - (p1) ] x [1 00] 
Po ref Po actual 
Supersonic: 
Cram - 1 .35 - 0.15( Moo - 1) 
(13. 6) 
(13. 7)


<!-- p.475 -->

CHAPTER 13 Pro pulsion 475 
Actually, the inlet pressure recovery is a function of both Mach number 
and the inlet mass flow. At low speeds with a high throttle setting, the inlet 
"hole" isn't big enough and the engine has to "suck" the air into the inlet duct. 
This causes a lower pressure recover y, as seen to the left of Fig. 13.7. 
However, if the engine is demanding less airflow (lower throttle settin g), 
the inlet can more readi ly meet the demand so the pressure rec overy 
would be higher than the values shown. 
For the static F- 16 at maximum thrust, the pressure recovery drops to 
about 0.8 6. At half the maximum inlet mass flow, the static pressure recovery 
is over 0.96 . At Mach 0.6, the pressure recovery difference from full to half 
mass flow is only 2%, and it is less than that at higher Mach numbers. 
This mass-f low variation in pressure recovery must be accounted for in 
the detailed performance calculations but can be neglected for conce ptual 
design studies. 
Note that the uninst alled engine data alread y include the inlet momentum drag as a part of the cycle analysis results, so it doesn't have to be 
separately estimated. These inlets drag. corrections are related to the way 
that pressure recovery affects the engine, not the momentum drag itself. 
Inlet distortion, engine bleed, and engine power extraction also need to 
be adjusted from the manufacturer's values- they are often assumed to be 
zero. Also, the engine data are based upon the manufacturer's nozzle 
design so that if a different nozzle is to be used, corrections must be made. 
"Inlet distortio n" refers to press ure and veloc ity variations in the airflow 
as it is delivered to the engin e. It primarily affects the allowable operating 
envelope of the engine but can affect engine performance. This is difficult 
to calculate and usually to ignore for initial analysis. 
For most jet aircraft, high-pr essure air is bled from the engine compressor 
for cabin air, anti-icing, and other uses. This engine bleed air (not to be confused with inlet boun dary-layer bleed and other forms of seco ndary airflow) 
exacts a thrust penalty that is more than propor tional to the percent of the 
total engine mass flow extracted as bleed air. 
Equation (13 .8) can be used to calcula te thrust losses from bleed extraction. The "bleed correction factor" Cbleed is provided by the manufacturer for 
various flight conditio ns. For initial analys is, Cbleed can be approximated as 
2.0. The bleed mass flow typically ranges from 1-5% of the engine mass flow. 
( bleed mass flow ) Percent thrust loss = Cbleed . fl 
x [10 0] engme mass ow (13.8 ) 
Installed engine thrust is also affected by horsep ower extraction. Jet 
mgines are equipped with rotating mechanical shafts turned by the turbines. 
The electrical generators, hydraulic pumps, and other such componen ts 
:onnect to these shafts. 
This extraction is typically less than 200 hp {15 0 kW} for a 30,000-lb:hrust {133 -kN} engine and usu ally has only a small effect upon installed


<!-- p.476 -->

476 Ai rcraf t De sign: A Conceptual Approach 
thrust. If the power required to drive the compressor is kn own, the SFC 
increase and thrust loss are both slightly less than the percent of power 
that is extracted J89l Horse power extraction is included in the cycle analysis 
used for detailed calculation of install ed- engine thrust but can usual ly be 
ignored for initial analysis. 
Mode rate inlet distortion usua lly has minimal effect upon installed thrust 
but can restrict the engine oper ating envelope. The effects of disto rtion are 
calculated later in the design process. For initial desi gn, the guidelines 
suggested earlier for loca tion of inlets and for forebod y shaping should 
avoid any later problems with inlet distort ion. 
Nozzle efficiency has a direct effect upon thrust. However, it is rare to use 
a nozzle other than that provided by the manufacturer. When a different 
nozzle is used, such as for vectoring or stealth, the new nozzle can usually 
be designed to provide the same efficiency as the manufacturer's nozzle. 
The drag effects of alternate nozzles are discussed later. 
MwJ Ins tall ed Net Propu lsiv e Force 
The installed engine thrust is the actual thrust produced by the engine 
as install ed in the aircraft. However, the engine creates three forms of drag 
that must be subtracted from the engine thrust to determine the thrust 
force actu ally available for prope lling the aircraft. This propelling force, the 
installed net propulsi ve force, is the thrust value to be used for aircraft 
performance calculat ions. 
Most of the engin e-related drag is produced by the inlet as a result of a 
misma tch between the amount of air demanded by the engine and the 
amount of air that the inlet can supply at a given flight condition. When 
the inlet is providing exactly the amount of air the engine demands (massflow ratio equals 1. 0), the inlet drag is negligi ble. 
The inlet must be sized to provide enough air at the worst- case condition, 
when the engine demands a lot of air. This sets the capture area. Most of the 
time the engine demands less air than an inlet with this capture area would 
like to provide (i.e., mass-f low ratio is less than 1. 0) . 
When the mass- flow ratio is less than 1. 0, the excess air must either be 
spilled before the air enters the inlet or bypassed around the engine via a 
duct that dumps it overboard (Fig. 13 .8) or into an ejector-t ype engine nozzle . 
The drag from air spilled before entering the inlet is called "spil lage" or 
"addi tive" drag. Additive drag represents a loss in momentum of the air 
that is slowed and compressed by the external part of the inlet but not 
used by the engine. The additive drag is determined by calcul ating, for 
each flight Mach number and engine mass-f low ratio, the Mach numbers 
and pressures throughout the inlet and integrating the forces in the flight 
direction for the part of the air which is spilled. 
The spilled air will be turned back toward the frees tream direction by the 
inlet cowl lip, producing a reduced pressure on the cowl. This provides a


<!-- p.477 -->

CHAPTE R 13 Prop ul sion 477 
-r -frill-==- Ac 
J_ --- """"----Fig. 13 .8 Addi tive drag, cowl -lip suction, and bypass sub critic al oper ation . 
suction force with a component in the forward direction, that is, a thrust 
(as shown in Fig. 13.8). This cowl-lip suction reduces the additive drag by 
as much as 30-40% in the low-superso nic regime . For a subsonic jet with 
well-rounded cowl lips, this suction will virtually eliminate additive drag. 
Even with cowl-lip suction, the additive drag under certain flight 
conditions could exceed 20% of the total aircraft drag. A pena lty of this magnitude is never seen because the designers resort to inlet-air bypass whenever 
the additive drag is too great. 
Allowing the excess air to enter the inlet and be dumped overboard or 
into an ejector nozzle will keep the inlet additive drag to a small value , 
The resulting bypass drag will be substan tially less than the additive drag 
would have been. Bypass drag is calculated by summing the momentum 
loss experienced by the bypassed air. 
Another form of inlet drag is the momentum loss asso ciated with the inlet 
boundary-layer bleed. Air is bled through holes or slots on the inlet ramps 
and within the inlet to prevent shock- induced sep aration and to prevent 
the buildup of a thick tur bulent boundary layer within the inlet duct. This 
air is dumped overbo ard out an aft-facing discharge exit, which is usually 
located a few feet behind the inlet. 
(Note: Do not confuse inlet bound ary-layer bleed with the inlet 
boundary-layer diverter. The diverter prevents the fuselage bounda ry-layer 
air from entering the inlet. Diverter drag has been accounted for in the 
aerodynamic chapter.) 
Calculation of bleed, bypass, and additive drag including cowl-l ip suction 
is a complicated procedure combining analytical and empirical methods, The 
textbook methods (see [1 6, 44-46]) are very time cons uming and cannot 
account for the effects of the actual aircraft geomet ry, which can greatly 
affect both the inlet flowfield and the pressure loss through bleed and 
bypass ducts , 
In a major aircraft comp any such calculations are made by propulsion 
specialists using complex computer programs. The results are included in 
the installed net propulsi ve force data that are provided to the sizing and 
performance analyst. 
To permit rapid initial analysis and trade studies, Fig. 13. 9 provides a 
"ballpark" estimate of inlet drag for a typical supersonic aircraft. This chart


<!-- p.478 -->

478 Air cr aft Design : A Concept ual Appr oach 
was prepared by the author using data from [9o] and other sources and should 
be used with great caution as they are merely typical data, not an estim ate for 
any given inlet design. 
This chart assumes that the engine is operating at a maximum dry or 
afterburning power setting, and that the inlet is ope rating at a corresp onding 
mass-flow ratio. The chart does not reflect the increase in inlet drag experienced when the thrust setting is reduced (which reduces the mass-f low ratio) . 
However, this chart should provide a reasonable approximation of inlet drag 
suitable for initial analysis and student design studies. 
Nozzle drag varies with nozzle posi tion as well as with the flight 
condition. To proper ly determine nozzle drag, the actual nozzle geomet ry 
as a function of throttle setting and flight cond ition must be known and 
the drag calculated by taking into account the overall aircraft flowfield. As 
an initial approximation, the effect of nozzle position can be ignore d 
and the nozzle drag estimated by the typical subson ic values shown in 
Table 13.1 [1 6] for the nozzle types shown in Fig. 10.23. 
The nozzle drag increases transoni cally and then drops off at supersonic 
speeds. For initial analysis the subsonic value can be assumed for all spee ds. 
Note that these nozzle drags are referenced to the maximum cross-sect ional 
area of the fuselage. For a subson ic, podded nacelle, the nozzle drag is 
negligi ble. 
The remaining propulsion system drag is the variat ion of trim drag with 
throttle setting. If the engine thrust axis is not through the center of gravity, 
any thrust change will cause a pitching moment. The trim force required to 
counter this moment is charged to the propulsion in most thrust- drag 
0.3 
0.2 
-, " c:s0.1 
.0 0 0.5 
.(Rough ap proxima tion) 
2-D in let 
35 ,000 ft 
{1 0,668 m} 
Axisym metric in let 
/' ,,, 10 ,000 ft 
.- ,,,,- {3048 m} 
LO 1.5 
Mach numb er 
Fig. 13 .9 Inle t drag tren ds. 
2.0 2. 5


<!-- p.479 -->

CHAPTER 13 Propulsion 479 
Table 13 .1 Nozzle In crementa l Drag [1 6l 
Nozz le Type 
Conv ergent 
Convergent ir is 
Ejec tor 
Variable ejector 
Tran slating plug 
2-D nozzle 
Sub son ic __!!l_!J_ 
A fuselage 
0.036-0 .042 
0.00 1 -0.020 
0.025-0 .035 
0.01 0-0 .020 
0.01 5-0 .020 
0. 005- 0. 01 5 
Referenced to fus elage maxi mum cross-sec tion area. 
bookkeeping systems. For initial analysis this can be ignored unless the thrust 
line is substantially above or below the aircraft centerline. 
Part Power Oper ation 
Turboj et and turbofan engines do not like to operate at less than their 
maximum thrust setting. When you throttle back, the reduction in thrust 
is more than propor tional to the reduction in fuel flow, so the SFC increases. 
A noticeable increase in SFC typically begins when you throttle below about 
90% power. For this reason, engine companies prepare "part-po wer tables" 
listing fuel consumption as a function of thrust at different altitudes and 
speeds. The installation analysis just described should also be applied to 
the part-power tables. This is a very laborious process! 
The part-po wer effect on SFC can be approximated by a semi- empirical 
equation developed by Mattingly, coauthor ofl42l . This provides a realistic 
increase in SFC as thrust is reduced [Eq. (13 .9)]. 
( )0.8 
c 0. 1 0.2 4 T 
--- = + 08 + 0.6 6 Cmaxdry ( T /T max dry) (T /T max dry) · T max dry 
+ 0. lM[ l - ( T )] 
(T / T max dry) T max dry (13 .9) 
When a jet engine is throttled all the way back to "idle," neither the fuel 
flow nor the thrust actually goes to zero. This residual thrust can be a real 
problem when you are trying to descend. If residual thrust divided by aircraft 
weight T/Wi s equal to the inverse of the lift-to- drag ratio (l /L/D), the aircraft cannot descend! 
Engine companies provide tables of idle thrust and fuel flow that should 
be used if available. If data are not available, a rough approximation is that 
idle SFC will be 1.5 times the max- dry SFC. Use this to cap the values calculated by the equation above.


<!-- p.480 -->

480 Air craft Des ign: A Con cept ual Approach 
Pi ston-Engine Overvie w 
The typical aircraft piston engine operates on the four- stroke Otto cycle 
as used by automobi les. The thermod ynamic theory of the Otto- cycle reciproc ating engine is described in (47, 91, 92] . For design purposes the most 
important thing to know about the piston engine is that the power produced 
is direct ly prop ortional to the mass flow of the air into the intake manifold. In 
fact, horsep ower is app roximately 620 times the air mass flow (lb/ s) {or 
power in kW = 1019 times mass flow in kg/ s}. 
Mass flow into the engine is affected by the outside air dens ity (altitude, 
temperature, and humi dity) and intake manifold pressure. Equation (13 .10) 
acco unts for the air-densi ty effect upon power and is attributed to Gagg 
and Ferrar of the Wright Aero nautical Company (1 934). This equation indicates that at an altitude of 20,000 ft {6100 m} a piston engine has less than 
half of its sea-le vel power. 
( P 1 - P/Po) power = powersL -Po 7.55 
where Po is the sea-le vel standard day air densit y. 
(13.10) 
The intake manifold is usua lly at atmospheric pressure. A forward-faci ng 
air- intake scoop can provide some small increase in manifold pressu re at 
higher speeds. Large increases in manifold pressu re require mechanical 
pumping via a "supe rcharger" or "turb osup ercharge r." 
The sup ercharger is a centrifugal air compressor mechanica lly driven by a 
shaft from the engine. The amount of air compression available is proportional to engine rpm. The turbosuper charger, or "turbocha rger," is 
driven by a turbine placed in the exhaust pipe. This reco vers energy that 
would other wise be wasted and decouples the available amount of compression from the engine rpm. 
Supe rcharging or turbocharging is usually used to maintain sea-le vel 
pressure in the intake manifold as the aircraft climb s. Typically, the sea-le vel 
pressure can be maintained up to an altitude of about 15,000-20,0 00 ft 
{4500- 610 0 m}. Above this altitude the manifold pressure, and hence the 
power, drops. Figure 13.10 shows typical engine performance for nonsupercharged, supercha rged, and turbocharged engines. 
Supe rcharging or turboch arging can also be used to raise the intake manifold pressure above the sea-le vel value to provide additional power from a 
given engine. However, the increased internal pressures require a heavier 
engine for structural reasons. 
Piston- engine performance charts are provided by the manufact urer as a 
function of manifold pressure, altitude, and rpm. 
Electric motors are increasin gly used for aircraft propulsion. See Chapter 
20 for a detailed discussion of the motors and their power supplies. Once the 
motor has power, its thrust is determined using the same methods described 
below for piston-props.


<!-- p.481 -->

QI 
"O 
3 
·;:; 
<! 
ft m 
50,000 
40,000 
10,0 00 
30,000 
20,0 00 
5000 
10, 000 
CH APTE R 13 Propulsion 481 
(Typical 10 00 bhp engi ne) 
200 400 600 
o +--+--+--+--+--+-'--+--+--f'--+---+-- kW 
1000 bhp o 200 400 600 800 
Engine powe r 
Fig. 13 .1 O Effects of su perchar ging. 
J Propell er Ana lysis 
It is sometimes said that a propeller "turns power into thrust." This is 
-chnically incorrect. Power cannot be turned into thrust because the units 
re not compatible. Instead, a propeller turns power into another form of 
ower, namely, "thrust power." 
Thrust power is the thrust force times the aircraft velocity. If the propeller 
rere perfectly efficient, it would be easy to calculate thrust. Simply divide 
ower by velocity, making sure the units are consi stent. Unfortunately, proellers are not perfect ly efficient. They normally waste about 20% of the 
ower in the act of creating thrust. We therefore define the propeller effiiency 1Jp as the thrust power obtained divided by the engine power used, 
ormally about 80% [Eq. (13. 16)] . Thrust is then found as power times 
rop efficiency, divided by velocity [Eq. (13. 17)] .


<!-- p.482 -->

482 Air cr aft De sign: A Con ceptu al Appr oach 
However, even with a perfect prop eller there is a problem. The engine 
power doesn't change when the airplane goes faster, so the thrust power produced doesn't change. Because thrust power is thrust times veloc ity, as the 
velocity goes up, the thrust goes down. This is the result of basic physics 
and has nothing to do with propeller ef ficienc y. But propeller efficiency 
often gets worse at higher speeds, making the thrust drop off even more 
severely. 
A propeller is a rotating airfoil that generates thrust much as a wing 
generates lift. Like a wing, the propeller is designed to a particular flight 
condit ion. The propeller airfoil has a selected design lift coefficient (usually 
around 0.5), and the twist of the airfoil is selected to give the optimal 
airfoil angle of attack at the desi gn condit ion. 
Because the tangential velocities of the propeller airfoil sections increase 
with distance from the hub, the airfoils must be set at progres sively reduce d 
pitch angles going from root to tip. The overall "pitch" of a propeller refers to 
the blade angle at 75% of the radius (70% in some books) . 
Propeller theory is well covered in many textbooks such as [92]. While 
theor y is useful for propeller designers, the aircraft desi gners usually work 
with experiment al propeller data provided by the propeller companies. 
This data are expressed using a variety of parameters and coefficients . 
Commonly used coefficients are described below and are ultimately used 
to read prop eller efficiencies from data charts : 
Advance ratio: 
Power coefficient: 
Thrust coefficient: 
! = V/nD 
p 550 bhp 
Cp= -- = 
pn3D5 pn3D5 
Speed-po wer coefficient: 
cs = v\J p/ Pn2 
Activity factor: 
lOSJR AFper blade = -5 cr3 D O.lSR 
105c 
= 
root [0.25 - (1 - A.)0. 2] l6D 
(13 .11 ) 
(13 .12) 
(13 .13) 
(13 .14) 
(13.15)


<!-- p.483 -->

CHAPTER 13 Prop ulsion 483 
or 
Propeller efficiency: 
Thrust: 
TV TV 
Y}p = p = 550 bhp 
I 550 bhp Y}p T=PYJ V= ----P V (forward flight) 
T -- cy _P _- cy 550 bhp ( . ) static 
Cp nD cp nD 
where 
T = thrust (lb) or {kN} 
V = velocity (ft/s) or {m/s} 
P = power (ft-l b/s) or {kW} 
bhp = brake horsepower 
n = rotation speed (rev/ s) 
D = propeller diameter (ft) or {m} 
c = propeller airfoil chord (ft) or {m} 
(13. 16) 
(13. 17) 
(13. 18) 
The advance ratio is related to the distance the aircraft moves with one 
turn of the propeller. Advance ratio is sometimes called the "slip function" 
or "progre ssion factor." It is propor tiona l to the ratio between forward 
speed and rotational tip speed. A large advance ratio means that the aircraft 
velocity is large compared to the tip speed. 
The power and thrust coefficients are nondimensional measures of those 
quantities, much like the wing lift coefficient. The speed- power coefficient is 
defined as the advance ratio raised to the fifth power divided by the power 
coefficient. The speed-po wer coefficient is nondimensional and does not 
involve the propeller diameter, which is useful for comparison between 
propel lers of different sizes. 
The activity factor is a measure of the effect of blade width and width 
distribution on the propeller and is a measure of the propeller's ability to 
absorb power. Activity factors range from about 90-200, with a typical 
light aircraft activity factor being 100 and a typical large turboprop having 
an activity factor of 140. The final expression in Eq. (13.15 ) is the activity 
factor for a straight -tapered propeller blade of taper ratio ,\. 
Equation (13.16 ) relates the propeller efficiency, already discussed in 
Chapters 3 and 10, to the advance ratio and the ratio of the thrust coefficient 
to the power coefficient. This ratio is used in Eq. (13 .17 ) to determine the 
thrust at static conditions when the veloc ity is zero and the propellerefficiency equation cannot be used for thrust determinat ion.


<!-- p.484 -->

484 Ai rcraf t Des ign: A Con ceptu al Appr oach 
Propeller data are available from the man ufacturers as well as variou: 
NASA/ NACA reports. These data are provided in many different format: 
using different combina tions of the previous parameters and coefficients 
Whatever the forma t, Eq. (13 .17 ) is ultimatel y used to determi ne the propel 
ler thrust at a given flight con ditio n. 
Figures 13 .11 and 13.12 , propeller charts for static and forward fligh 
([ 93] , or see [92] ), have been chosen as typical of prop ellers used fo1 
modern light and business aircraft. These charts represent a three- bladec 
propeller with a design lift coefficient of 0.5 and an activity factor of 100. 
For a two-bladed propeller, the forward -flight efficiencies are about 391 
better than shown in Fig. 13. 12 , but the static thrust is about 5% less thar 
shown in Fig. 13 .11. The reverse trends are true for a four-bladed prope ller 
Also, a wooden propeller has an efficienc y about 10 % lower due to iti 
greater thickness. 
If the propeller is of variable-pi tch design, its pitch is adjusted to thE 
optimum blade angle at each flight cond ition to produce a con stant enginE 
rpm regardless of the horsep ower being produced. 
The advance ratio and power coefficient are then independent variables, 
and the prope ller efficiency can be read in Fig. 13.12 for any combina tion oJ 
advance ratio and power coefficient that can occur in flight. Blade angle for 
the variable- pitch prope ller can be read as a fallout parameter in Fig. 13.1 2. 
Propeller thrust in forward flight is propor tional to the inverse of the 
velocity, which would imply infini te thrust at zero velocity. This is clearly 
ridic ulous and indicates that the equat ion is inappropr iate at zero forward 
speed. Inst ead, the propeller static-t hrust value is estimated from Fig. 13 .11 , 
based on test data. 
4.0 
3.0 
rJ I::, 2.0 
\.) 
1.0 
Typi ca l 3-bladed propeller 
Activity factor = 10 0 
Blade design CL = 0.5 
O+-----+---+-----+---+-----+---+-----t0 0.05 0. 10 0. 15 0.20 0.25 
Fig. 13 .1 1 Static prop eller thrust ( atter f93J). 
0.30 0.35


<!-- p.485 -->

CHAPTE R 13 Propulsion 
Typica l 3-blade d propeller 
Activity factor = 10 0 
0.5 Blade design CL= 0.5 
0.4 e3/4 
0.3 40' 
0.. 35' u 
0.2 30' 
25' 
0. 1 20' 
15' 
0 0 0.2 0.4 0.6 0.8 LO 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6 2.8 
J 
fig . 13 .12 Forward-fligh t thrust and efficienc y (after [93]), wher e e314 is the blade pit ch at 75% 
of rad ius. 
In the speed range from 0 to about 50 kt (such as during takeoff), the 
thrust varies in a fashion that can be represented by a smooth curve faired 
between the static-thrust value and the calculated forward-flight thrust. 
If a fixed-pi tch propeller is used, the blade angle cannot be varied in flight 
to maintain engine rpm at any flight condition. Because the rpm and therefore horsepower will vary with velocity, the efficienc y and hence the thrust 
will be reduced at any speed other than the design speed. At lower speeds, 
the propeller blades are prone to stalling. At higher speeds they don't have 
enough local angle of attack to make full thrust. 
Propeller data such as Fig. 13.12 could be used to determine the thrust 
from a fixed-pi tch propeller by following the appropria te line for the selected 
blade angle, but the torque effects on engine rpm would also have to be 
considered. It is simpler to use the appro ximate method of Fig. 13.13 . 
This relates the fixed-pi tch propeller efficienc y at an off-design veloc ity 
and rpm to the on-d esign efficiency, which is attained by the propeller at 
some selected flight condition. The on- desi gn efficiency is obtained from 
Fig. 13.12 , which is also used to get the required blade angle for the 
design condition. 
The static thrust of a fixed-pitch propeller will be less than is estimated 
using Fig. 13 .11. A fixed-pi tch propeller suffers at low speeds due to the 
high local angles of attack of the blades at low speeds and high rpms, As a 
rough approximation, it can be assumed that the static thrust is about 60% 
higher than the thrust at 100 kt. 
These charts provide useful rough estimations of propeller performance, 
but actual charts for the selected propeller should be obtained from the manufacturer for any serious design effort. 
485


<!-- p.486 -->

486 Ai rc raft Des ign: A Concep tual Appr oa ch 
0.90 
0.80 
T/p 
(-)-- 0.7 0 T/p design 
0.60 
0.50 
0.40 0.50 0.60 0.70 0.80 0.90 1. 00 1.10 1. 20 1. 30 
- 13 .7 
/If design 
Fig. 13 .13 Fixed-p itch propeller adjustment. 
Pis ton-Pr op Th rust Corrections 
Propeller efficiency must be corrected for three important influences , 
namely, bloc kage, tip Mach, and scrubbing drag. Blocka ge refers to the 
effect of the nacelle immed iately behind the propeller. It "blocks" the flow, 
causing it to slow down before it reaches the propeller. While most corrections make the thrust worse, blockage usually makes it better because a 
slower airflow velocit y typically gives higher thrust with propellers. 
One way to correct for blocka ge is to adjust the advance ratio f prior to 
using a propeller efficie ncy chart such as Fig. 13.12. Equation (13.19 ), 
based on data from [40l , is a reason able first approximation for blockage 
and should be applied to f before f is used to find the propeller efficie ncy: 
J corrected = J(l - 0.3 29 Sc/ D2) (13. 19) 
where 
Sc = maximum cross- section area of cowling immed iately behind the 
propeller 
D = propeller diameter 
Another correction takes into account the increased drag if shocks form 
on the propeller tips. In Chapter 10 it was suggested that the propeller diameter be set so that the helical tip speed does not get too close to the speed of 
sound. High-speed propeller-p owered aircraft will prob ably see this problem 
anyway, reducing the thrust and increasing the torque exerted on the engine.


<!-- p.487 -->

CHAPTER 13 Prop uls ion 487 
Equation (13. 20), based on data from f13l , corrects the propeller efficiency for 
tip Mach effects. 
= - M · - 0 89 ( ) ( 0.16 ) 1/pcorrected Y/p tip · 0.48 - 3tjc for Mtip > 0.8 9 (13 .20) 
where 
Mtip = tip Mach number = ..j V2 + ( 7rD)2 /a 
a = speed of sound 
t/ c = propeller airfoil thick ness-to- chord ratio 
Scrubbing drag is the increase in aircraft drag resu lting from the higher 
velocity and turbulence experienced by the parts of the aircraft within the 
propwash. This drag could be calculated by determining, for each flight 
condition, the increased dynamic pressure within the propwash and using 
that value for the component- drag calculatio n. 
A simpler approach, called the SBAC (Soci ety of British Aircraft 
Constructors) method, adjusts the propeller efficienc y as in Eq. (13 .21). 
The subscr ipt "washed" refers to the parts of the aircra ft that lie within the 
propwash. If the parasite- drag coefficient for the propwashed parts of the 
aircraft cannot be determined, 0.004 is a reasonable estimate. 
= [1 - 1 .558 !!_ """"' c s 
] Y/ Peffective Y/p D2 Po L......,, ( fe wet) washed (13 .21 ) 
where Cle is the equivalent skin-friction (parasite) drag coefficien t, 
referenced to wetted area. 
For a pusher-propeller confi guration, the scrubbing drag is zero. 
However, the pusher propeller suffers a loss of efficienc y due to the wake 
of the fusela ge and wing. This loss is stro ngly affected by the actual aircra ft 
configuration and should equal about 2-5%. 
Cooling drag represents the momentum loss of the air taken into the 
cowling and passed over the engine for cool ing. This is highly dependent 
upon the detail design of the intake, baffles, and exit. 
Miscellaneous engine drag includes the drag of the oil cool er, air intake, 
exhaust pipes, and other parts. Cooling and miscellaneous drags for a 
well-designed engine installation can be estimated by Eqs. (1 3.22) and 
(13.23).f40l However, a typical light aircraft engine installation might experience cooling and miscellaneous drag levels two to three times the values 
estimated by these equations. Rather than use these equations, it is reas onable to assume that an expertly designed cooling system will produce a 
cooling drag equivalent to a 6% reduction in thrust, and a not-so-good


<!-- p.488 -->

488 Ai rcraf t Desig n: A Concept ual Approach 
system will produce an 8-10 % reduction in thrust. 
where 
-7 bhp . y2 (Djq)cooling = (4.9 X 10 ) u-Vpy2 
= 6 x 10 -8 -uV 
(Djq)misc = (2 X 10 -4) bhp 
= 2.5 X 10 -Sp 
T = air temper ature (0R ) or {K} V = velo city (ft/s) or {m/s} 
u = P/Po 
Turbopr op Performanc e 
{m2} (1 3.2 2) 
{ft2} 
{m2} (1 3.2 3) 
A turboprop is a jet engine that drives a propeller using a turbine in the 
exhaust. The jet exhaust retains some thrust capabi lity and can contribute as 
much as 20% of the total thrust. For this reason, the power rating of a 
turboprop engine includes the power equivalent of this residual thrust. 
This power equival ent of resi dual thrust is arbitrarily calculated under 
static conditions as the residual thrust divided by 2.5. Under forward-flight 
conditions it is calculated using Eq. (13.17 ) assumi ng that the propeller 
efficie ncy T/P = 0.80. The total of the mechanical and thrust residual 
power, in horsep ower, is called the equivalent shaft horsepo wer (ESHP). 
Analys is of the turboprop is a hybrid between the jet and the piston- prop 
analysis. The engine is analyzed like a jet, including the inlet effects. The 
residual thrust is provided by the manufacturer as a hors epower equivalent. 
The propeller is analyzed as just described, including the scrubbing- drag term. 
The conventional turboprop, like the piston-prop, is limited by tip Mach 
number to about Mach 0.7. The turboprop has higher efficienc y than the 
piston- prop at Mach numbers greater than about 0.5 due to the residual 
jet thrust, but the conventional turboprop is no match for a turbofan 
engine at the higher subsonic speeds. 
A new type of advanced propeller that offers good efficiencies up to about 
Mach 0.85 was developed in the late 19 70s. These are known as "propfans" 
or "unducted fans" (UDF) (Fig. 13.14 ). They are smaller in diameter than 
the regular propellers and feature numerous wide, thin, and highly swept 
blades. Test programs indicate that a well-designed propfan can retain 
propeller efficiencies of over 0.8 at speeds on the order of Mach 0.85. 
More rece ntly, the "open rotor" has been defined as a turbofan engine in 
which the fan blades (rotors) have such extreme diameter that the cowling 
ring around the rotors produces more drag than bene fit, so it is eliminate d.


<!-- p.489 -->

CHAPTE R 13 Prop ulsion 489 
Fig. 13 .14 Propfa n. 
This looks a lot like a propfan, but with more blades and proba bly more rows 
of blades. Ongoing development work is prom ising, but issues of weight, 
complexity, and noise need resolution. 
What We've Learned 
We've discovered methods to calculate propulsive thrust and fuel consumption for the as-inst alled engine, whether jet or propeller. Thrust adjustments 
for propulsion-rel ated drags must be included. 
Flying boat.


<!-- p.490 -->

490 Ai rcraf t Des ign: A Conceptu al Appr oach
