# Raymer Ch.12 - Aerodynamics

*Converted from `Daniel P. Raymer - Aircraft Design_ A Conceptual Approach (2018, American Institute of Aeronautics and Astronautics Inc.) - libgen.li.pdf` by `tools/pdf_to_md.py`. Page markers are printed page numbers.*


<!-- p.389 -->

Ae rodynamics 
• Now that the fir st design lay out is co mple ted it is time to analy ze it, see how we ll it 
per fo rms its ro le, an d find out how to make it bet ter. 
• Aerody nam ics calculations include maxi mum li ft, par asi tic dr ag, dr ag due to li ft, and 
sup er so nic wave dr ag. 
• Cla ssica l me thods ar e presented, and mod ern CFO is dis cussed . 
Introd uction 
T he start of this chapter represen ts a turning point in the book. Up 
to here, the book has shown how to take a set of requirements 
and create a credible "Dash-One" initial design layout. Starting 
from here, the book shows how to analyze and optimize that design, and 
describes how to dev elop an improved "Dash- Two" which is iterated until 
a design freeze can be declared. 
The desi gn layout began with initial sizing, back in Chapter 3. This was 
based upon rough estimates of the aircraft's aerodynamics, weights, and 
propulsion characterist ics. At that time we could not calculate the actual 
characteristics of the design bec ause the aircraft had not been desi gned yet! 
Now there is an actual design layout. It may not be perfect, but it 
has enough realism and definition to allow an "as- drawn" analysis rather 
than relying upon statistical and "eyeball" estimat es. The goal at this point 
is to see if it actually meets the required mission range as estimated in the 
initial sizing. If not, we will resize the aircraft until it does. 
Analysis of the as- drawn aircraft will also check a variety of design 
requirements and other needs. Stab ility and control is an obvious example. 
In previous chapters, an approximate tail volume coefficient method was 
used for tail sizing. Now that the aircraft is drawn, we can analytically determine if the selected tail sizes are adequa te, and also check control surface 
389


<!-- p.390 -->

390 Air craft Design : A Conceptual Approach 
sizing, dynamic stability responses, spin recovery, and more. Performance 
requirements such as takeoff distance and rate of climb must now be analyzed with real calculations from the as-dr awn aircraft. If it is supposed to 
be a stealth desi gn, the radar cross section can be calculated. 
Trade studies will be done to determine the best combination of desig n 
parameters (T/W, W/S, aspect ratio, etc.) to meet all mission and perform ance requirements at the minimum weight and cost. These results will form 
the basis of the Dash- Two drawing, and beyond. 
Analys is methods are presented in Chapters 12- 19, starting with the 
aerod ynamic analysis in this chapter. The techniques presented here are 
good prelimi nary methods, suitable for asses sing the design and performing 
trade studies, but they should not be viewed as the "final answer." These 
methods were carefully chosen to allow the design student to see the 
whole design process, not get bog ged down in detailed analysis. The basic 
process of desi gn, analys is, optimization, and re-de sign is the same regardless 
of analytical techniqu es. 
For the "final answer" in prelimina ry desi gn, the major aircraft compa nies 
will use their own metho ds. These are prop rietary, complicated, and highly 
computeri zed. Even so, the concept ual design analysis methods in this book 
are still useful-and used-e ven in the big companies. In the pre-com puter 
era, we built and flew airplanes based on analysis methods much like these. 
Aerody na mi c Forces 
As we get into aerod ynamic analys is, we break the aerod ynamics discipline into many parameters with strange names, defined by peculiar coefficients. Quite frankly, we confuse ourse lves with our notations and all of 
the different lifts and drags that we separately calculate. Please realize that 
these are all "acco unting fictio ns." They are defined just to make calcula tion 
easier. They don't represent the actual physics of airflow over a vehicle. 
As shown in Fig. 12.l, there are only two ways in which the air mass and 
the airplane can act upon each other. One is friction caused by shear layers, 
and the other is pressure. Friction is always tangential to the surface, and 
pressure is always perpendicular to it. All of our terminologies and coefficients are just different combinations of these two. 
As the aircraft moves forward, the air molecules 
slide over its skin. The molecules closest to the skin 
act as if they are stuck to it, moving with the aircraft 
Pressure and ShearLayer Friction-The 
Origins of 
Aerodynamics 
(no- slip cond ition) . If the air molecules closest to the aircraft skin are moving 
with it, there must be a slippage (or shear) between these molecules and the 
nonmoving molecules far away from the aircraft. 
"Viscos ity" is the honey-like tend ency of air to resist shear deformation. 
This causes additional air near the aircraft skin to be dragged along with 
the air that is "stuck" to the aircraft. The force required to overcome viscosity


<!-- p.391 -->

Shear "Stuck" 
molecules 
CHAP TER 12 Aerodyn ami cs 39 1 
Pre ssur e 
Loca l 
Shear 
Freest rea m 
veloc ity 
. . 
Freestr eam 
velocity 
(Pr essu res ar e with res pect to am bient air pressu re. Out war d 
arr ows represent pressu res belo w am bien t.) 
Fig. 12 .1 Origin of aer odynamic forces. 
and pull this bou ndary-layer air in the direction the aircraft is travelling 
produces skin- friction drag. 
If the air molecules slide over each other (shear) in an order ly fashion, the 
flow is said to be "lamin ar." If the molecules shear in a disord erly fashion, the 
flow is "turbulen t." This produces a thicker boun dary layer, indica ting that 
more air molecules are dragged along with the aircraft, generating more 
skin-friction drag. 
Airflow along a smooth plate becomes turbulent when the loca l Reynolds 
number reaches about one- half million but can become turbulent at a lower 
Reynolds number if there is sub stantial skin rough ness. Also, the curvature of 
the surface can either prevent or enco urage the transition from laminar to 
turbulent flow. Laminar flow is discussed below. 
The pressure forces shown in Fig. 12.1 are caused by changes in veloc ity. 
As the aircraft moves forward, the air molecules are pushed aside. This causes 
the relative veloci ty of the air to vary about the aircraft. In some places, 
mostly toward the nose, the air is slowed down. In other places the air is 
speeded up relative to the freestream velocity. 
According to Bernoulli's equa tion, the total pressure (static plus dynamic) 
along a subsonic streamline remains constant. If the local air veloc ity 
increases, the dynamic pressure has increased, so the static pressure must 
decrease. Similarly, a reduct ion in loca l air veloci ty leads to an increase in 
static pressure. 
Thus, the passa ge of the aircraft creates varying pressur es around it, 
which push on the skin as show n in Fig. 12.1. 
Lift is a summation of press ures in the vertical direction and is created by 
forcing the air that travels over the top of the wing to travel faster than the air 
that passes under it. This is accom plished by the wing's angle of attack and/ 
or wing camber. The resulting difference in air veloc ity creates a pressure 
differential between the upper and lower surfaces of the wing, which produces the lift that suppor ts the aircraft.


<!-- p.392 -->

392 Air c raf t De sign : A Conceptual Appr oa ch 
If the aircraft is traveling near or above the speed of sound, additio nal 
pressure forces are produced by the shock waves around the aircraft. Shock 
waves result whenever supersonic flow is being slowed down or turned. 
All aerod ynamic lift and drag forces result from the combination of shear 
and pressure forces. How ever, the dozens of classification schemes for aero dynamic forces can create cons iderable confusion because of overlappin g 
terminology. 
For example, the drag on a wing includes forces variously called airfoil 
profile drag, skin- friction drag, separation drag, parasite drag, camber drag, 
drag due to lift, wave drag, wave drag due to lift, interference drag-an d 
so forth. 
Figure 12 .2 pres ents the various drag terminologies using a matrix that 
defines the drag type based upon the origin of the drag force (shear or 
pressu re) and whether or not the drag is stro ngly related to the lift force 
being developed. 
Drag forces not strong ly related to lift are usually known as parasi te drag 
or zero-lift drag. In subson ic cruising flight of a well-des igned aircraft, the 
parasite drag consists most ly of skin- friction drag, which depends mostly 
upon the wetted area. 
The skin- friction drag of a flat plate of the same wetted area as the aircraft 
can be readily determined for using equations provided later. However, the 
Pa rasite 
dr ag 
Drag due 
to lif t 
[j(lift)] 
Reference 
ar ea 
Pre ssur e forces 
Shear 
forces Separ ation Shock Cir cu lation 
Visco us Wave 
Skin 
fri ction 
separ ation dr ag 
Scru bbing Shock -induced sepa ration 
dr ag "drag rise" 
In ter ference dr ag 
Profi le dr ag 
Camber dr ag 
Su perv elo city Su per veloc ity Induc ed 
effect on effect on dr ag 
skin pr ofi le Tri m dr ag friction dr ag-e .g., 
landing Wave dr ag due to li ft 
ge ar 
Swetted Max. cross-sec tion (Volume 
dis tribution} 
Fig. 12 .2 Drag term inolo gy matrix. 
sref


<!-- p.393 -->

CHAPTE R 12 Aerodyn amics 393 
actual parasite drag will be larger than this value because some pressure drag 
is added. 
One of the main causes of drag-pro ducing pressu re forces is viscous 
separation. This was the source of consi derable confusion during the early 
theoretical development of aerod ynamics. As the airflow moves around a 
body, it is accele rated until about the point of maximum thickness, then it 
slows back down as the rear is approached. This means that the pressure is 
doing the oppo site-it is stead ily reducing until roughly the point of 
maximum thickness, and then it "reco vers" to the or iginal pressure as the 
flow continues to the rear. 
If the theoretical pressure forces in a perfect fluid are integrated over a 
streamlined body without flow separation, it is found that the pressures 
around the front of the body creating a rearward drag force are exactly 
matched by the pressures around the rear of the body, which create a 
forward force. Thus, if skin friction is ignored, the net drag is zero ! 
This beau tiful theoretical result was known to be false and came to 
be called d'Alembert's paradox (1 752- . The paradox was finally resolved 
by Prandtl who determined that the boun dary layer, which is produced by 
viscosity, causes the flow to sepa rate somewhere on the back half of the 
body. Once the flow sepa rates, the pressures fail to fully recover to the original values, so the forward components of the pressures at the back of the 
body are not quite as large as they should be. This prevents the full attainment of those forward acting pressure forces, leaving a net drag force due 
to viscous separatio n. (See [67J for a more detailed discussion.) 
So the solution to d'Alembert's paradox is that a viscous phenomenon, 
normally asso ciated with skin- friction drag, actually triggers this unexpected 
pressure drag. 
Viscous sepa ration drag is also called "form drag" and depends upon the 
location of the separation point on the body. If the flow sepa rates nearer to 
the front of the body, the drag is much higher than if it sepa rates more 
towards the rear. Figure 12.3 shows typical sepa ration points for various 
shapes, but realize that the actual sepa ration point is complicated and 
changeable. 
Among other things, the loca tion of the sepa ration point depends upon 
the curvature of the bod y. Also, the sepa ration point is affected by the 
amount of energy in the flow. Turbulent air has more energy than laminar 
air, so a turbulent bounda ry layer actually tends to delay separatio n. 
If a body is small and flying at low speed, the Reynolds number will be so 
low that the flow will remain laminar resulting in separated flow very near the 
front. For this reason, a small bod y can actually have a lower total drag when 
its skin is rough. This produces turbulent flow, which will remain attached 
longer than would laminar flow. The dimples on a golf ball are an example 
of this. 
For a very long body such as the fuselage of an airliner, the turbulent 
boundary layer will become so thick that the air near the skin loses most


<!-- p.394 -->

394 Air craf t De sign: A Concep tual Approach 
Ellip soid 
- -r Airfoil L-.V --.........,,,_,-===========-====-====::::=::.::··--a..Fig. 12 .3 Airflow separ ation . 
of its energ y. It cannot go around the corner, which causes separation near 
the tail of the aircr aft and a high "bo attail drag." 
To prevent this, small vanes perpendicular to the skin and angled to the 
airflow are placed just upstream of the sepa ration poi nt. These "vortex generators" produce vortices off their ends, which mix the boun dary layer with 
highe r-ener gy air from outside the boun dary layer. This delays separation 
and reduces boattail drag. Vortex generators are also used on wing and tail 
surfaces (see Chapter 8). 
The subson ic drag of a streamlined, nonlifting body consists solely of skin 
friction plus viscous sep aration drag and is sometimes called the profile drag. 
Profile drag is usua lly referenced to the maximum cross-sec tional area of 
the body. Note that the terms "profile drag" and "form drag" are often intermixed, although strictly spea king the profile drag is the sum of the form drag 
and the skin- friction drag. Also note that the term "profile drag" is sometimes 
used for the zero-lift drag of an airfoil, which is sometimes called the 
wing profile. 
Sometimes flow sepa ration is forced by geometry, not the effects of viscosity. The air can't go around a rearward-facing sharp corner such as the 
back of a cutoff fuselage. This results in the low press ures being applied to 
the rearward-facing area creating "base drag." The air can't even go around 
a forward- facing corner if it is too sharp or the body is too blunt. A rectangular shape such as a square spring landing gear leg will have separation from its 
front corner causing a large drag pe nalty vs a streamlined shape. 
Another form of friction drag is called "scrubbing drag." This is caused by 
the propwash or jet exhaust flowing over or near the aircraft's skin. This produces a higher dynamic press ure in that region, hence higher skin- friction 
drag. Also, the jet exhaust is certainly turbulent, and the propwash is likely


<!-- p.395 -->

CHAPTER 12 Aerodyn amics 395 
to be, which increases drag even more. This is avoided with a pusherpropeller and is the reason that few modern jets have conformal nacelles 
in which the exhaust rubs along the aft fuselage. 
In supersonic and high subson ic speeds, shocks are formed at various 
places around the aircraft. There are greater pressures behind the shocks. 
There can also be supersonic expansion fans in which the flow accelerates 
around a rearward-facing corner, causing a reduction in pressure. The net 
rearward compo nents of these pressures produce additional drag. 
"Wave drag" is the drag caused by the formation of shocks at supersonic 
and high sub sonic speeds. At high subso nic speeds, the shocks form first on 
the upper surface of the wings because the airflow is accel erated as it passes 
over the wing. 
Drag forces that are a strong function of lift are known as drag due to lift. 
This includes all lift- related effects. The induced drag is actually a subset of 
the drag due to lift, being the drag that is directly caused by the mechanism 
that creates lift. This is the circulation about the airfoil that, for a threedimensional wing, produces vortices ip the airflow behind the wing. The 
energy required to produce these vortices is extracted from the wing as a 
drag force and is prop ortional to the square of the lift (see Sec. 12.6). 
Two-dimensio nal airfoil drag, or profile drag, is a combination of skinfriction drag and viscous separation drag. In inviscid flow there is no drag 
due to lift for the two- dimensional airfoil because the lift force is perpendic ular to the freestream directio n. However, in actual viscous air, the profile drag 
increases as the angle of attack is increased, leading to some confusion. 
This increase in two-dimensional airfoil drag is due to an increase in 
viscous separation caused by a greater pressure drop on the upper surface 
of the airfoil as the angle of attack is increased. This increase in profile 
drag with increasing angle of attack is not technica lly caused by the generation of lift but does vary as the lift is varied so that it gets "lumped in" 
with the actual induced drag in the parameter we call "drag due to lift." 
Many des igners (and this author) get sloppy with the terminolog y, saying 
"induced" drag when the broader "drag due to lift" term is meant. 
Most prelimina ry drag estimation methods do not actually use the airfoil 
profile drag data to determine total wing drag. Instead, the induced drag for 
an idealized wing with no camber or twist is determined, and then profile 
drag and twist/ camber effects are estimated and added in, often statistic ally. 
To coun ter the pitching moment of the wing, the tail surfaces produce a 
lift force generally in the downward direction. The induced drag of the tail is 
called "trim drag." Trim drag also includes the additional lift required of the 
wing to counter any download produced by the tail . 
When aircraft total drag vs lift is pres ented, the drag can be calculated 
with some fixed elevator deflection, or it can be calculated using the 
varying elevator deflections required to trim the aircraft at each lift coefficient. This "trimmed" drag provides the correct data for use in performance 
calculat ions.


<!-- p.396 -->

396 Air c raf t Des ign : A Conc eptu al Approach 
In superso nic flight there is a compon ent of wave drag that changes as the 
lift change s. The creation of lift results from changes in the press ure aro und 
the aircraft. Wave drag is a pressu re drag due to shock formation, and any 
changes in the pressures around the aircraft will change the location and 
strength of the shocks around it resulting in "wave drag due to lift." This 
drag is fairly small and is usually ignored in early conce ptual design. 
- 12 .3 Aerody nami c Coefficients 
Lift and drag forces are usua lly treated as nondimensio nal coefficien ts as 
defined in Eqs. (12.1) and (12 .2) . The wing reference area, Sref or simply S, is 
the full trapezoidal area extending to the aircraft centerline. The dynamic 
pressure of the freestream air is called q, as defined in Eq. (12 .3), 
where 
L = qSCr 
D = qSCD 
1 q = - pV2 2 
(12 .1 ) 
(12 .2) 
(12 .3) 
By definition, the lift force is perpendicular to the flight direction 
while the drag is parallel to the flight direct ion. Remember that the twodimensiona l airfoil characteristics are denoted by lowercase subscr ipts 
(i.e., Cl') whereas the three- dimensio nal wing characteristics are denoted by 
uppercase subs cripts (i.e., Cr). 
Drag is norma lly spoken of as so many "c ounts" of drag, meaning the four 
digits to the right of the decimal place. For example, 38 counts of drag mean a 
drag coefficient of 0.0038 . 
Figure 12.4 illustrates the drag polar, which is the standard presen tation 
format for aerod ynamic data used in performance calculat ions. The drag 
polar is simply a plot of the coefficient of lift vs the coefficient of drag. 
Note that the angle of attack a is indicated here by tic marks along the 
polar curve. This is not standard practice, but is useful for unde rstanding 
the relationship between lift, drag, and angle of attack. 
Uncambered: 
(12. 4) 
Cambered: 
(12 .5) 
For an uncambered wing, the minimum drag CDo occu rs when the lift is 
zero. The drag polar has an approx imately parabolic shape, as defined by Eq. 
(12. 4). The value of J( will be discussed later.


<!-- p.397 -->

Unc amb ered 
CHAP TER 12 Aerodyn ami cs 397 
Cam be red 
Camber dr ag 
at zero li ft 
Fig. 12 .4 Drag polar. 
For a cambered wing, the minimum drag CDmin occurs at some pos itive 
lift CLmin dra • The drag polar also has a parabolic shape but is offset vertically 
as defined by Eq. (12 .5). For wings of moderate camber, this offset is usua lly 
small, which implies that CD0 approximately equals CDmin and that Eq. (1 2.4) 
can be used. 
The point at which a line from the origin is just tangent to the drag polar 
curve is the point of maximum lift-to- drag ratio. Note that this is not the 
point of minimum drag! 
- Lift 
Figure 12.5 shows typical wing lift curves, how lift increases as angle of 
attack incre ases. The uncambered wing has no lift at zero angle of attack, 
while the cambered wing has a pos itive lift at zero angle of attack. A negative 
angle of attack is required to obtain zero lift with a cambered wing. 
An old rule of thumb is that the negative angle of attack for zero lift in 
degrees equals the airfoil's percen t camber (the maximum vertical displacement of the camber line divided by the chord) . 
Maximum lift is obtained at the stall angle of attack, beyond which the lift 
rapidly reduces. When a wing is stalled, most of the flow over the top has 
separated. 
The slope of the lift curve is essen tially linear except near the stall angle, 
allowing the lift coefficient below stall to be calculated simply as the lift-cur ve 
slope times the angle of attack (relative to the zero-lift angle) . At the stall, the


<!-- p.398 -->

398 Air craft De sign: A Concep tual Approach 
lift curve has become nonlinear such that the angle for maximum lift is 
greater than the linear value by an amount shown as -a at CLmax in the figure. 
Figure 12.5 also shows the effect of aspect ratio on lift. For an infiniteaspect- ratio wing (the two-dimensional airfoil case) the theoretical low- speed 
lift-cur ve slope is two times 7T (per radian ). 
Actual airfoils have lift-c urve slopes between about 90 and 100% of the 
theoretical value. This perce ntage of the theoretical value is sometimes 
called the airfoil efficiency Y/· 
Reduction of aspect ratio reduces the lift-cur ve slope, as shown. At very 
low aspect ratios, the ability of the high-pressu re air to escape aroun d the 
wing tips tends to reduce the lift. This also delays stalling at high angle s of 
attack, as described in Chapter 4. Also note that the lift curve becomes nonlinear for very low aspect ratios, due to the suction lift from the wingtip 
vortex. 
Increasing the wing sweep reduces the lift, roug hly by the cosine of the 
sweep angle. The resulting lift-cur ve slope looks like that of a low aspect- ratio 
wing and in fact, the two effects are additive. Highly swept wings of low 
aspect ratio get far less lift than a "normal" wing of the same area. 
The effect of Mach number on the lift-cur ve slope is shown in Fig. 12.6. 
The two-dimensiona l airfoil lines represent upper bounda ries for the nosweep, infinite -aspec t-ratio wing. The upward curve in the subsonic region 
and the correspo nding downward curve in the superson ic region are found 
by the theoretical Prandt l-Gla uert correction shown in the denomin ator. 
Real wings fall below these curves as shown. This is mo stly due to airfoil 
considerations and the effects of sweep and aspect ratio. 
Effect of ca mber 
CL 
--+-[ 
amax 
Lift 
Effect of as pect ratio 
CL Aspect ratio 
Fig. 12 .5 Wing lif t curve.


<!-- p.399 -->

10 
9 
8 
c 
-- 7 
-0 
- 6 Qj 
a. 5 ti 
0' 4 
3 
2 
1 
0 
0 
Sub son ic 2-D 
theor etica l 
0.5 1.0 
CHA PTE R 1 2 Aerodyn am ics 399 
Su per sonic 2-D 
the or etical 
c __ 4_ La- ,/M2- l 
Typical uns wept 
high as pect ratio wings 
Th in air foil 
Thick air foil 
Typical swept wings 
High as pect ratio 
Low as pect ratio 
1.5 . 2.0 2.5 3.0 
Mach numb er 
Fig. 12 .6 Lift-curve slope vs Mach numb er. 
Also, real wings don't go to infinity at Mach one, as implied by the 
Prandtl-G lauert correction. Instead, they follow a transition curve in 
the transonic regime between the upward -trending subso nic curve and the 
downward-trending supersonic curve. A fat and unswept wing will suffer 
an extra lift loss from shocks in the transonic regime whereas a thinner, 
swept wing does not. 
The lift-curve slope is needed during con ceptual design for three reas ons. 
First, it is used to proper ly set the wing incidence angle. This can be espec ially 
important for a transpor t aircra ft, in which the floor must be level during 
cruise. Also, the wing incidence angle influences the required fuselage 
angle of attack during takeoff and landing, which affects the aft-fusela ge 
upsweep and/ or landing gear length. 
Second ly, the methodol ogy for calcula ting drag due to lift for highperformance aircraft uses the slope of the lift curve, as will be seen. The 
third use of the lift- curve slope in conce ptual desi gn is for longitudinalstability analysis, as discussed in Chapter 16. 
If Jll Sub sonic Lift-Curve Slope 
Equation (12 .6) is a semi- empirical formula from[ 68l for the complete 
wing lift- curve slope (per radia n) . This is accura te up to the drag- divergent


<!-- p.400 -->

400 Ai rcraf t De sign : A Concep tual Approach 
Mach number and reaso nably accur ate almost to Mach 1 for a swept wing. 
21TA Cr,, = ----,=========== 
A 2 {32 ( tan2 Amax t) 2 + 
where 
4 + 7 l + {32 
{32 = l - M2 
Cc,, 
T/ = 2 7T/ f3 
(Sexposed) (F) Sref (1 2.6 ) 
(1 2.7 ) 
(1 2.8) 
Amax t is the sweep of the wing at the chord loca tion where the airfoil is 
thickest. 
If the airfoil lift-cur ve slope as a function of Mach number is not known, 
the airfoil efficiency T/ can be approximated as about 0.9 5. (In several textbooks this term is dropped by assum ing that T/ = 1.0 at all Mach numbers. ) 
Sexposed is the exposed wing planform, that is, the wing reference area 
less the part of the wing covered by the fuselage. Fi s the fuselage lift factor 
[Eq. (1 2. 9)] that accoun ts for the fact that the fuselage of diameter d 
creates some lift due to the "spil l-o ver" of lift from the wing. 
F = 1. 07(1 + d/b)2 (12 .9) 
Sometimes the product (Sexposed/ Sref )F is greater than one, implying that 
the fuselage produces more lift than the portion of the wing it covers. This is 
unlikely and should proba bly be suppressed by setting this product to a value 
slightly less than 1. 0, say, 0.9 8. 
The wing aspect ratio A in this equation is the geome tric aspect ratio of 
the complete reference planform. The aspect ratio term should be increased 
by the use of wing endplates or winglets, both of which work by increasi ng 
the effective span of the wing. An endplate rather crud ely prevents the highpressure air benea th the wing from "esca ping" to the top, providing an 
increase in lift and some benefit to the drag due to lift. The winglet, desc ribed 
in Chapter 4, cleverly obtains a forward thrust compon ent which provides a 
substantial reduction in drag due to lift. 
End plate: 
Aeffective = A(l + l.9 h/b) (12 . 10) 
Winglet: 
Aeffective = A(l + h/b)2 (12 . 11 ) 
where h = endp late or winglet height; b = wing span. 
The aspect ratio improvement for winglets estimated by Eq. (12 .11 ) is 
for a typical modern winglet. An expertly- designed winglet may have a 
25 % higher value for the h / b term. For a poor ly-designed winglet, little


<!-- p.401 -->

CHAPTER 12 Aerodyn am ics 401 
more than a fin stuck on the wingtip, there may be no benefit at all. Also, the 
actual increase in effective aspect ratio is a function of velocity and lift coefficient. It depends upon the selected airfoils and the relative location, geometry, and twist of the wing and winglet. It also depends upon the streng th of the 
wing's tip vortex, so a wing with a higher aspect ratio or lower span loading 
(weight/ span) will obtain less improvement by the use of winglets. 
The effective aspect ratio corrections for endplates and winglets should 
be used in the induced drag calculations provided below. 
#Jf J Supers onic Lift-Curve Sl ope 
For a wing in purely supersonic flow, the lift- curve slope is ideally defined 
by Eq. (1 2. 12), as shown in Fig. 12 .6. A wing is consi dered to be in purely 
supersonic flow when the leading edge is "superson ic," that is, when the 
Mach cone angle is greater than the leading-edge sweep [see Eq. (1 2.14 )]. 
cla =.4/{3 (12. 12) 
where 
f3 = VM2 -1 (12. 13) 
when 
M> 1/ cos ALE (12. 14) 
The actual lift-cur ve slope of a wing in superso nic flight is difficult to 
predict without use of a soph isticated computer program. The charts in 
Fig. 12. 7 are proba bly the best approximate method available. They were 
defined in[69l and have been used in a number of textbooks. 
These charts actually estima te the slope of the "nor mal force" co efficient 
Cn, that is, the lift-cur ve slope in a direction perpendicular to the surface of 
the wing. For low angles of attack, this is approx imately equal to the lift- curve 
slope so we ignore the difference. 
To use these charts, the wing aspect ratio, taper ratio, and leadin g-ed ge 
sweep are employed. The six charts each represent data for wings of a different taper ratio. If a chart for the actual taper ratio of a wing is not provided, 
interpolation must be used. 
The term {3 [Eq. (12.13 )] divided by the tangent of the leadin g-ed ge sweep 
is calculated and found on the horizo ntal axis of the chart. If this ratio is 
greater than 1. 0, it is inverte d, and the right side of the chart must be used. 
Then the appropriate line is selected by calculating the wing aspect ratio 
times the tangent of the leading- edge sweep, and the vertical-a xis value 
is read. 
To obtain the approxima te slope of the lift curve, this value is then 
divided by the tangent of the leading-edge sweep, if on the left side of the 
chart, or by {3 if on the right side of the chart.


<!-- p.402 -->

402 Ai rc raft Des ign : A Concept ual Approach 
a) 7 7 
'O 6 
~ 
6 
- 'O Q; 5 5 - -3- Q; >- 0.. 
2 4 4 
£ c-0 
-<:l 3 
v 
3 £ 
c} -<:l 
--;:;; c} _, 2 2_ < <::a.. c:: 
fl 0. 
0 0 0.2 0.4 0.6 0.8 1.0 0 0.8 0.6 0.4 0.2 0 
/3 tan ALE tan ALE -/3b) 7 7 
'O 6 
w 
6 
- 'O 
Q; 5 5 -3- Q; 
>-3-- 4 4 c-£ 0 
-<:l 
v 
3 3 £ 
c} --;<:l --;:;; 2 -!::'... _, 2 < <::a.. c:: 
fl 1 
0.25 
0 0 0.2 0.4 0.6 0.8 1.0 0.8 0.6 0.4 0.2 00 
/3 tan ALE tan ALE -/3c) 7 7 
6 A= 1/ 4 
w 
6 'O 
- 'O Q; 5 5 - -3- Q; >2 4 4 -3>£ i5 -<:l v 
c} 3 3 £ 
-<:l 
--;:;; 2 c} _, 2 < <::a.. c:: 
2 
0.25 
0 0 0.2 0.4 0.6 0.8 1.0 0 0.8 0.6 0.4 0.2 0 
/3 tan ALE tan ALE -/3Fig. 12 .7 Wing su personic normal- force-cu rve slope. 1691


<!-- p.403 -->

CHAP TER 12 Aerodyn ami cs 403 
d) 7 7 
6 .:l= 1/3 
w 
6 'O 
- 'O 
Qj 5 5 .3- Qj 
t- 4 4 .3-0 
t-" 
-5 0 
-- " 
(..) :.-: 
3 3 ......:§ ---;;:; 2 c} ...l 2-< co.. 
c:: 
fl 
0.25 
0 0 0 0.2 0.4 0.6 0.8 1.0 0.8 0.6 0.4 0.2 0 
/3 tan ALE tan ALE -/3e) 7 7 
'O 6 .:l = 1/2 6 - 'O Qj 5 5 - .3- Qj ;... .3-2 4 4 
-5 t-- 2 
c} 3 3 -5 
----;;:; c} ...l 2 2 < co.. c:: 
fl 1 
025 
0 0 0.2 0.4 0.6 0.8 1.0 0.8 0.6 0.4 0.2 00 
/3 tan ALE tan ALE -/3f) 7 7 
'O 6 6 
- 'O Qj 5 5 - .3- Qj <'.' .3-ill 4 4 ;... -5 5 -- 3 3 -5 c} ---;;:; c} ...l 2 < 2c:: co.. 
fl 1 1 0.25 
00 0.2 0.4 0.6 0.8 1.0 0.8 0.6 0.4 0.2 0 0 
/3 tan ALE tan ALE -/3Fig. 12 .7 (Con tin ued) .


<!-- p.404 -->

404 Air craf t De s ign : A Concep tual Ap proa ch 
As this value is referenced to the exposed planform of the wing, it must be 
multiplied by (Sexposed/Sref) as in Eq. (12 .6) . Also, the value must be multiplied by F from Eq. (1 2.6) to account for the fuselage lift effect. 
Note that these charts give best results only for trapezo idal wings without 
kinks or strakes. For highly nontrapezoidal planforms, [69] contains additional 
estimation procedures. However, those charts are now rarely used in industry 
where comp uterized methods are readily available. These are discusse d later. 
Mtlfl Tra nsonic Lift -Curv e Slope 
In the transonic regime (roughly Mach 0.8 5-1. 2 for a swept wing) , there 
are no good but quick estimation methods for slope of the lift curve. Instead, 
the calculated subson ic and superson ic values are plotted vs Mach number, 
then a smooth curve is faired between the subson ic and supersonic values, 
similar to the curves shown in Fig. 12 .6. This suffices for "Dash-One" analysis 
and optimization but is supplanted by computational aero dynamic methods 
as soon as possible. 
Mtlll No nli near Lift Effec ts 
For a wing of very high sweep or very low aspect ratio (under two or 
three) , the air esca ping around the swept leading edge or wing tip will 
form a strong vortex that creates additional lift at a given angle of attack. 
This additional lift varies approx imately by the square of the angle of 
attack. This nonlinear increase in the slope of the lift curve is difficult to estimate and can conser vatively be ignored during early conceptual design. 
However, the increase in total maximum lift from this vortex formation 
can be impor tant. This is discussed in the next section. 
Mtlf.1 Maxi mum Lift (Clean) 
The maximum lift coefficient of the wing will usua lly determine the wing 
area. This in turn will have a great influence upon the cruise drag. This 
strong ly affects the aircraft takeoff weight to perform the design mission. 
Thus, the maximum lift coefficient is critical in determining the aircraft 
weight, yet the estimation of maximum lift is proba bly the least reliable of 
all of the calculations used in aircraft concept ual design. Even refined windtunnel tests cannot predict maximum lift with great accuracy. Frequ ently 
an aircraft must be modified during flight test to achieve the estimated 
maximum lift. 
For high-aspect-ra tio wings with mode rate sweep and a large airfoil 
leading- edge radius, the maximum lift depends mostly upon the airfoil 
characteristic s. The maxim um lift coefficient of the "clean" wing (i.e. , 
without the use of flaps and other high-lift devices) will usua lly be about


<!-- p.405 -->

CHAPTER 12 Aerod ynam ics 405 
c 
0.0015 c 0.06 c 
Fig. 12 .8 Airfoil leadi ng-edge sha rpness parame ter. 
90% of the airfoil's maximum lift as determined from the two-dimensional 
airfoil data at a similar Reynolds number (see typical data in Append ix D). 
Sweeping the wing reduces the maximum lift, which can be found by 
multiplying the unswept maximum lift · value by the cosine of the quarterchord sweep [Eq. (12.15 )] . This equation is reasonably valid for most subsonic aircraft of moderate sweep . 
Crmax = 0.9 Cemax cos Ao.2sc (12. 15) 
If a wing has a low aspect ratio or has substantial sweep and a relatively 
sharp leading edge, the maximum lift will be increased due to the formation 
of leading-ed ge vortices. This vortex formation is stro ngly affected by the 
shape of the upper surface of the leading edge. 
Leadin g-edge shape could be defined by the airfoil nose radius. However, 
the nose radius alone does not take into accoun t the effect of airfoil camber 
on the shape of the upper surface of the airfoil leading edge. 
Instead, an arbitrary leadin g-ed ge sharpness parameter has been defined 
as the vertical separation between the poin ts on the upper surface, which are 
0.15 and 6% of the airfoil chord back from the leading edge (Fig. 12.8). The 
leading-edge sharp ness parameter (or Liy) as a function of thickness ratio 
for various airfoils is provided in Table 12.1. 
Table 12 .1 -Y for Common Airfoils 
Airfoil Type 
NACA 4 digi t 
NACA 5 digi t 
NACA 64 series 
NACA 65 series 
Bic onvex 
26 t/c 
26 t/c 
21 .3 t/c 
19 .3t /c 
11. 8 t/c


<!-- p.406 -->

406 Ai rcraf t Design : A Concep tual Appr oa ch 
The leading-edge sharpness parameter has been used in[69l to develop 
methods for the construction of the lift curve up to the stall for low- o r 
high-aspect- ratio wings. For high-aspec t-ratio wings, Eq. (12 . 16) is used 
along with Figs. 12 .9 and 12.10. The first term of Eq. (12 .1 6) represen ts the 
maximum lift at Mach 0. 2, and the second term repres ents the corr ection 
to a higher Mach number. 
High aspect ratio: 
C -C (CLmax) + LlC Lmax - Cmax C Lmax fmax 
(1 2.1 6) 
where Cemax is the airfoil maximum lift coefficient at M = 0. 2. This trapezoidal planform maximum lift can be ad justed for exposed planform and fuselage lift effects, as in Eq. (12 .6) . 
The angle of attack for maximum lift is defined in Eq. (12 .1 7) with the 
help of Fig. 12 .11 . Note that the first and second terms represent the angle 
of attack if the lift-c urve slope were linear all the way up to stall. The 
second term can be approximated by the airfoil zero-lift angle, which is negative for a cambered airfoil. If the wing is twisted, the zero-lift angle is approximately the zero-lift angle at the mean chord loca tion. The third term in Eq. 
(12 . 17 ) is a correction for the nonlinear effects of vortex flow. 
Note: unt wisted, cons ta nt-a ir foil -sec tion wings 
1.6 ,------------------M"'0 .2 
1.4 
+ 
1.2 
06 -++t t . 
0.4 -----------------__J 
0 10 20 30 
ALE (deg) 
40 50 
Fig. 12 .9 Subson ic maxi mum li ft of hig h-as pect-r atio wings. [69] 
60


<!-- p.407 -->

-0.2 
-0.4 
-0.6 
Mach numb er 
0.4 0.6 
2.5 
3 
4 
-0.2 
-0.4 
CHAP TE R 12 Aerodyn ami cs 407 
Mach numb er 
0.4 
ALE = 20 deg 
0.6 
- -y 
2.25 
2.5 
3 
4 
4.5 
-0.6 -------0.8 ------Mach numb er Mach numb er 
-y 
2 
g-.2 o.4 o.- -Y 
2.25 
-c . 3 Lmax · 
4 
Ace , 60 deg -0.2 4.5 
ALE = 40 deg 
-0.4 ------Fig . 12 .1 0 Mach-n umber correc tion for su bson ic maxi mum li ft of hig h-as pect-r atio wings. [691 
High aspect ratio: 
Crmax + +A O'.CL = -- O'.OL ilO'.CL max 
CLa 
max 
(12. 17) 
A different set of charts is used for a low-aspect- ratio wing, where vortex 
flow dominates the aerod ynamics. For use of these charts, low aspect ratio is 
defined by Eq. (12 .18 ), which uses the parameter C1 from Fig. 12.12 . 
Maximum lift of a low-aspect- ratio wing is defined by Eq. (12.1 9) using 
Figs. 12. 13 and 12. 14. The angle of attack at maximum lift is defined by 
Eq. (12 .20) using Figs. 12 .15 and 12. 16. 
Low aspect ratio if: 
A< 3 
- (C1 + l)( cos ALE) (1 2.1 8)


<!-- p.408 -->

408 Ai rcraf t Desig n: A Concept ual Approach 
°' 
<Ii 
x 
8 
G' 
<::I 
<l 
i2 .--,--------.------------....,.--., -1 1---aCL 
10 
8 
6 
4 
/. max 
a 
0.2 -M - 0.6 
o ----------------0 10 20 30 
ALE (deg) 
40 50 60 
Fig. 12 .1 1 Angl e-of-at tack in crement for subson ic maxi mum li ft of hig h-as pect- ratio wing s. f69] 
Low aspect ratio: 
Crmax = (CLmax) base + f:.CLmax 
acLmax = (aclma)base + f:.a clmax 
(12.19 ) 
(12.2 0) 
At transonic and supersonic speeds, the maximum lift a wing can achieve 
is usually limited by structural cons iderations rather than aero dynamics. 
Unless the aircraft is flying at a very high altitude, the available maximum 
lift at Mach 1 is usually enoug h to break the wings off! 
Also, maximum lift is often limited by buffeting, controllab ility, or flexibility rather than by actual maximum lift. Wind-tunnel and flight-test data 
1.5 .---------c, -:53 
0 0 .2 0.4 0.6 0.8 1.0 0.6 0.8 
Taper ratio , A, Taper ratio , A, 
Fig. 12 .12 Taper-ratio correction factor s for low-aspe ct-ratio wings. f691 
1.0


<!-- p.409 -->

CHAPTE R 12 Aerody nam ics 409 
1.6 ----------------------1.4 
1.2 
0.8 
0.6 
Low as pect ratio 
Up per limi t of 
low-a sp ect-ratio 
ra nge 
Bor der line 
as pect ratio 
0·4 0 0.4 0.8 1.2 1.6 2 .0 2.4 2 .8 3.2 3.6 4 .0 4.4 
A (C1 + 1) {j cos ALE 
Fig. 12 .13 Maxi mum subson ic li ft of low-aspect-ratio wings. 1691 
from similar designs are usually used to estimate the usable lift beyond the 
Mach limit of the previous methods. Figure 12.17, developed by the author 
from various empirical sources, is a reasonable first approximation for 
normal designs. Determine the maximum lift coefficient at Mach 0.5 from 
the previous methods and then multiply it by the factors from the curve. 
If JP Maxi mum Lift wit h Hig h-Lift Devi ces 
There is always a basic incom patibility in aircraft wing design. For cruise 
efficiency a wing should have little camber and should operate at a high 
wing-loading. For takeoff and landing a wing should have lots of lift, which 
x 
e 
u"' 
<1 
0.4 
0.2 
0 
-0.2 0 2 4 6 8 
(C2 + 1) A tan ALE 
f f 
t 
t 
10 12 
Fig. 12 .14 Maxi mum -l ift inc rement for low-aspect-ratio wings. 1691 
14


<!-- p.410 -->

410 Air craf t Design : A Concep tual Appr oach 
40 
:li 
1l 30 
-K 
E 
- 20 
10 
Low as pect ratio 
Up per limi t of 
low-as pect- ratio 
ra nge 
Borderl ine 
as pect ratio 
0.4 0.8 1.2 1.6 2.0 2.4 2.8 3.2 3.6 4.0 4.4 
(C1 +1 ) -cos ALE 
Fig. 12 .15 Ang le of attack for subsonic maxi mum li ft of low-aspect-ratio wings .[ 69l 
means a lot of camber and a low wing-loading. In other words, for cruise you 
want a small wing, but for takeoff and landin g, you want a big wing. 
In the histor y of aviation, almost every imaginable device for varying the 
wing camber and wing area has been attempted, including a wing with a telescoping outer panel, a fabric membrane that unfurls behind the wing, a device 
that pivots out from the fuselage forming an extended flap, and even something called a "mutable" wing having variable span, camber, and sweep J7°l 
Figure 12 .18 illustrates the common ly used high lift flaps. The plain flap is 
simpl y a hinged portion of the airfoil, typically with a flap chord Cf of 30% 
of the airfoil chord. The plain flap increases lift by increasing camber. For 
a typical airfoil, the maximum lift occurs with a flap deflection angle of 
about 40-45 deg. Note that ailerons and other control surfaces are a form 
of plain flap. 
20 
r-Ci 10 
A cos ALE [l + (2,1.)2] 
<]) 
:s 
K 
E _, 
- 0 
<l 
-10 0 2 4 
i 
t 
... t 
6 8 
(C2 + 1) A tan ALE 
... 
i. 10 12 14 
Fig. 12 .16 Ang le-of-atta ck inc rement for su bson ic maxi mum lif t of low-aspect-r atio wings .[691


<!-- p.411 -->

1. 000 
0.800 
0' 0.60 0 
-6 E K 
- E u ' 
u_, 0.400 
0.200 
CHAPTE R 12 Aerodyn amics 41 1 
+ 
0.000 -----------------------0.500 1. 000 1.5 00 2.0 00 2. 500 3.000 
Mach numb er 
Fig. 12 .1 7 Maxi mum li ft adjus tment at high er Mach numb ers . 
The split flap is like the plain flap except that only the bottom surface of 
the airfoil is hinged. This produces virtually the same increase in lift as 
the plain flap. However, the split flap produces more drag and much less 
change in pitching momen t, which can be useful in some designs. Split 
flaps are rarely used now but were common during World War IL 
-+---- c -------1--cr( __ -:::):::. Plain flap 
'\ 
Split flap 
c __ "J ___ «'-Slo tted flap 
""\ 
I 
c C'I 
t:: =c-- I Slo tted Fowler flap c ____ ---J-- ---Double slo tted flap 
c =-:c-Tri ple sl otted flap Fig. 12 .1 8 Flap types .


<!-- p.412 -->

412 Aircr aft Desig n: A Conceptual Approach 
The slot ted flap is a plain flap with a slot between the wing and the flap. 
This permits high-pressure air from beneath the wing to exit over the top of the 
flap, which tends to reduce separ ation. This increases lift and reduces drag. 
The Fowler-type flap is like a slotted flap, but mechanized to slide rearward as it is deflected. This increases the wing area as well as the camber. 
Fowler flaps can be mechanized by a simple hinge loca ted below the wing, 
or by some form of track arrangement contained within it. 
To further improve the airflow over the Fowler flap, double- and even 
triple-s lotted flaps are used on some airliners. These increase lift but at a considerable increase in cost and comple xity. 
Aft flaps do not increase the angle of stall. In fact, they tend to reduce the 
stall angle by increasing the press ure drop over the top of the airfoil, which 
promotes flow sepa ration. To increase the stall angle, some form of 
leading- edge device is required, as shown in Fig. 12.19. 
The lead ing- edge slot is simply a hole that per mits high-pr essure air from 
under the wing to blow over the top of the wing, delaying separation and stall. 
Usually such a slot is fixed, but might have closing doors to reduce drag at 
high speeds. 
A leading-ed ge flap is a hinged portion of the leading edge that droops 
down to increase camber. This has the effect of increasing the curvature 
CiC __ --Leadi ng-edge slot 
,(JL Lead in g-edge flap 
,,-c - (J- Slo tted le adi ng-edge 
flap (slat ) 
c - /J Kruger flap 
Wing in 
top view 
Fig. 12 .19 Leading -ed ge devices . 
Wing strake 
or le adingedge extension 
(LEX) 
Vortex


<!-- p.413 -->

CHAP TER 12 Aerody nam ics 413 
on the upper surfac e. The increase has been shown to be a major factor in 
determining maximum lift. Leading-edge flaps are usually used for improving 
the transonic maneuvering performance of high-speed fighters, which need a 
thin wing for supersonic flight. 
A slotted leadin g-ed ge flap ("slat") provides increased camber, a slot, and 
an increase in wing area. Slats are the most widely used leading-edge device 
for both low- speed and transonic mane uvering. At transonic speeds, slats 
are also useful for reducing the buffeting tende ncy, which might limit the 
usable lift. At Mach 0.9 the use of slats improved the usable lift of the F-4 by 
over 50% . 
The Kruger flap is used mostly by large air liners. It works as an air dam, 
forcing air up and over the top of the wing. Kruger flaps are lighter in weight 
than slats but produce higher drag at the lower angles of attack. Kruger flaps 
have a subtle advantage in that they do not leave a crack on the upper side of 
the leading edge like a slat does, so it is easier to maintain laminar flow over 
the wing. 
The wing strake, or "leading -edge . extension" (LEX) , is similar to the 
dorsal fin used on vertical tails. Like dorsal fins, the LEX at high angle of 
attack produces a vortex that delays sepa ration and stall. Unfortuna tely, a 
LEX tends to promote pitch -up tendencies and so must be used with care. 
Figure 12 .20 illustrates the effects these high-lift devices have upon the lift 
curve of the wing. The non- extending flaps such as the plain, split, or slotted 
flaps act as an increase in camber, which moves the angle of zero lift to the left 
and increases the maximum lift. The slope of the lift curve remains 
unchanged, and the angle of stall is some what reduced. 
An extending flap such as the Fowler type acts much like the other flaps 
as far as zero-lift angle and stall angle are concerned. However, the wing area 
is increased as the flap deflects, so the wing generates more lift at any given 
angle of attack compared to the non- extending flap. 
Because the lift coefficient is referenced to the original wing area, not the 
extended wing area, the effective slope of the lift curve for an extending flap is 
increased by approxima tely the ratio of the total extended wing area to the 
original wing area. 
Double- and triple- slotted flaps act much like single- slotted Fowler flaps, 
but the maximum lift is increased. 
A leading-edge slot acts only to delay stall. A leading-edge flap or slat delays 
the stall, but also has the effect of reducing the lift at a given angle of attack (i.e., 
the lift curve moves to the right) . This is because the droop in the leading edge 
acts as a reduction in the effective angle of attack as measured from the leading 
edge to the trailing edge. Note that a leading- edge slat, which increases wing 
area, also increases the slope of the lift curve much as does a Fowler flap. 
Leading-edg e devices alone do little to improve lift for takeoff and landing 
because they are effective only at fairly high angles of attack. However, they 
are very useful when used in combination with trailing -ed ge flaps because 
they prevent premature airflow sepa ration caused by the flaps.


<!-- p.414 -->

414 Air c raft Design : A Conc eptu al Appr oach 
/' Sl otted flap 
None xtending flaps 
Extending flaps 
Leading -edge slo t 
Leading -edge flap or slat 
Wing stra ke (LEX) 
Fig. 12 .20 Effects of high -l ift devic es. 
The wing strake, or LEX, delays the stall at high angles of attack (over 
20 deg) . Also, the area of the LEX pro vides additional lift, thus increasing 
the slope of the lift curve. However, the LEX does little to increase lift at 
the angles of attack seen during takeoff and landing. The LEX does not 
delay the premature stall asso ciated with trail ing-edge flaps. 
Estimating a wing's maximum lift with flaps is extremely difficult. Deflection of a high-lift device changes the airflow over the rest of the wing, 
even upstream, affecting the local flow and local stall angle of attack. The 
effects of the fuselage, nacelles, landing gear, and flap actuators are difficult 
to predict. Even tiny changes in the gap between wing and flap can have a 
large effect on lift. An unexpected amount of flap structural bend ing can 
change that gap and literally make the airplane stall at too high of a spee d. 
Maximum lift calculation methods used in con cept ual design are based 
on empirica l data, extrapolations from two- dimensio nal tests, and simpli fied


<!-- p.415 -->

CHAPTE R 12 Aerodyn ami cs 415 
analysis. Some useful handb ook methods are detailed inf69l (see also f71l). A 
reasonable first- order method is presented next, but if at all pos sible, it 
should be calibrated with test data on an actual airplane with similar flap 
geometry. 
Chapter 16 provides a method for estimating the lift increment due to a 
simple plain flap. That method is useful for con trol surface calcula tionsafter all, control surfaces are ju st flaps, used for control. It can also be used 
for calculating the extra lift from a plain flap on a straight wing, with suitable 
weighting for area and adjustment for sweep. 
For more complicated flap geometries, Eqs. (12.21) and (12 .22) provide a 
reasonable estimate of the increase in maximum lift and the change in the 
zero-lift angle for various types of flaps and leading- edge devices when 
deployed at the optimum angle for high lift during landing. 
fl Co values should be obtained from test data for the selected airfoil or <max 
can be appro ximated from Table 12.2. For takeoff flap settings, lift increments of about 60- 80% of these values should be used. The change in zerolift angle for flaps in the two-dimensional case is approximately -15 deg at 
the landing setting, and -10 deg at the takeoff setting. 
(Sflapped) ilCL = 0.9/lCc cos Att L max max 
Sref · · 
(Sflapped) AaoL = (Aaod airfoil cos Att.L. Sref 
(12.21) 
(12.2 2) 
In Eqs. (12 .21) and (12 .22), H.L. refers to the hinge line of the high-lift 
surface. Sflapped is defined in Fig. 12. 21. The lift increment for a leading-e dge 
extension can be crudel y estimated as 0.4 at high angles of attack. 
Table 12 .2 Appr oxi mate Lift Contri butions of 
Hig h-Lif t Devices 
High-lift Device 
Flaps 
Plain and split 0.9 
Slo tted 1 .3 
Fowl er 1. 3 c' /c 
Dou ble sl otted 1.6 c1 /c 
Tri ple slo tted l. 9 c' /c 
Leading-e dge devices 
Fixed slo t 0.2 
Leadi ng-edge ftap 0.3 
Kruger ftap 0.3 
Slat 0.4 c' /c


<!-- p.416 -->

416 Air craft Des ign : A Conceptual Approach 
Leadi ng-edge devices 
- Sl ats 
- LE flap s 
- Slo ts 
Fig. 12 .21 "Flap ped" wing area . 
Sflapped = Area of 
wing having fla p, not 
ar ea of flap alone! 
Snapped 
Other methods for increasing the lift coefficient involve active flow 
control using either suction or blowing. Suction uses mechanical air 
pumps to suck the thickening bound ary layer off the wing before it causes 
sepa ratio n. This increases the stall angle of attack and therefore increases 
maximum lift in a manner similar to leading- edge flaps. 
Blowing uses compressor bleed air or compressed air provided by a 
mechanical air pump to prevent flow separation and increase the freestream flow turning. Typically, the compressed air is exited through rearward- facing 
slots over the flaps or leading-edge flaps. 
Pa rasit e (Zer o-Lift ) Drag 
Mf Jjl Equ ival ent Ski n-Friction Method 
Two methods for the estimation of the parasite drag CD0 are presented. 
The first is based upon the fact that a well-designed aircraft in subson ic 
cruise will have parasite drag that is most ly skin-fr iction drag plus a small 
sepa ration pressure drag. The latter is a fairly consistent percen tage of the 
skin-fr iction drag for different classes of aircraft. This leads to the conce pt 
of an "equivalent skin friction coefficient" Cfe, which includes both skinfriction and separation drag. 
Cfe is multiplied by the aircraft's wetted area to obtain an initial estimate 
of parasite drag. This estimate [Eq. (1 2.23) and Table 12.3] is suitable for 
initial subsonic analysis and for checking the results of the more detailed 
method desc ribed in the next sec tion. 
C _ C Swet 
Do fe S ref (12. 23)


<!-- p.417 -->

CHAPTER 12 Aerodyn ami cs 417 
If Jf J Component Buildup Method 
The compon ent buildup method estimates the subsonic paras ite drag 
of each compon ent of the aircraft using a calculated flat-pla te skin-fr iction 
drag coefficient Cf and a compon ent "form factor" FF that estimates the 
pressure drag due to viscous sepa ration. Then the interference effects on 
the component drag are estimated as a factor Q, and the total compo nent 
drag is determined as the product of the wetted area, Cf, FF, and Q. 
(Note that the interference factor Q should not be confused with dynamic 
pressure q.) 
Misc ellaneous drags CDmisc for speci al features of an aircraft such as flaps, 
un-retracted landing gear, an upswept aft fuselage, and base area are then 
estimated and added to the total, along with estimated contribut ions for leakages and protuberances CDL&r · Subson ic parasite- drag buildup is shown in 
Eq. (12 .24), where the subscript c indicates that those values are different for 
each compon ent. 
(12 .24) 
For superson ic flight, the skin- friction contribution is simpl y the flatplate skin- friction coefficient times the wetted area. The supersonic pressure 
drag contributions are included in the wave-drag term, which is determined 
from the total aircraft volume distribut ion. 
For transonic flight, a graphical interpolation 
between subson ic and supersonic values is used. 
Supersonic and transonic drag calculations are 
discussed later. 
Component buildup 
method estimates 
parasitic drag. 
Table 12 .3 Equ ival ent Ski n-Friction Coeffici ents 
Bomber 0.0 030 
Civil transport 0 .0026 
Mil itar y cargo (hi gh upsweep fuselage ) 0.0035 
Air Force figh ter 0.0 035 
Navy fighter 0.0040 
Clean supersonic cruise ai rcraft 0.0 025 
Light ai rcraft-single eng ine 0.0 055 
ligh t ai rcraft-twin engine 0.0 045 
Prop sea plane 0.0 065 
Jet seaplane 0 .0040


<!-- p.418 -->

418 Ai rcraft Design: A Conce ptu al Ap proach 
Mf JD Fl at-Pl ate Ski n-Fric tion Coeff icient 
The most impor tant factor affecting skin- friction drag is the extent to 
which the aircraft has laminar flow over its surfaces. The skin- friction drag 
can literally be doubled if the flow is turbulent rather than laminar. Unfortunately, it often is. 
Everyone has seen the smoke from a cigaret te rise up in smoot h parallel 
flow, then after a short distance, break into a wider and ju mbled flow. 
Laminar becomes turbulent, no matter how still the air. The same thing 
happens to the airflow along an airplane's skins. The distance at which the 
flow becomes turbulent is determined by the flow's Reynolds numb er R 
[Eq. (12 .25 )], which includes both length and veloc ity, multiplied by the 
ratio of the air's densi ty and viscos ity. 
pVf, R= µ (12. 25) 
The f, in Eq. (1 2.25) is the characteristic leng th. For a fuselage, f, is the 
total length. For a wing or tail, f, is approximated by the mean aerodynamic 
chord leng th (C-bar) . 
On a smo oth flat plate, laminar flow will be maintained until the local 
Reynolds number reaches ro ughly half a million, at which point it will 
transition to turbulent. For complicated three-d imensio nal shapes like airplanes, the transition point is very difficult to estimate. Dep ending upon the 
shape, the velocity, the Mach number, the pressure gradients, the smoothness 
of the surfaces, and even the presence of rain and bug sp latters, the flow can 
transition anywhere from the leading edge to very close to the rear. 
For a smo oth wing or tail, transition usually occu rs ju st downstream 
of the point of minimum pressure, which is usua lly at or near the point of 
maximum thickness. This is why "laminar flow" airfoils have their point of 
maximum thickness much farther to the rear than the old NACA airfoils. 
The amount of laminar flow on an airplane has a huge effect on its drag. 
NASA tests [72] of the VariE ze, Long-EZ, and Bellanca Skyrocket airplanes, all 
of which have significant laminar flow, showed that delibera tely "tripping" the 
flow to turbulent right at the wing leading edge caused a 25% increase in 
cruise drag of the whole airplane. 
How do we estimate this all-impor tant phenomenon? For now, we guess. 
The best computational fluid dynamic codes (CFD) in use today still apply 
quasi- empirical models to predict loca l transitio n-a fancy way of gues sing. 
For initial analysis in conceptual design, we make a broader guess, by assuming a percen tage attainment of laminar flow then calcu lating a weighted 
average between the laminar and turbulent skin- friction coefficients estimated bel ow. 
Traditional airplanes have turbulent flow over most of their external 
("wetted") surfaces, although some laminar flow can be seen at the front of 
the wings and tails. A carefully designed modern compo site aircraft such


<!-- p.419 -->

CHAPTER 12 Aerodyn am ics 41 9 
as the Piaggio GP18 0 can have laminar flow over as much as 50% of the wings 
and tails, and about 20-35% of the fuselage. 
Anyone who does this for a living keeps careful track of the state of 
the art, looking for values on new airplanes as reported in jour nal and maga zine articles (but we don't always belie ve them !). This author's current best 
guesses are in Table 12. 4, but the final guess is yours. If you guess higher 
values than you can actually attain, your airplane will look good in concept ual 
design analysis but won't reach its range and performance goals when the 
airplane is built. If you guess too far on the conser vative side, you may 
never get to build the airplane because the predicted performance won't 
excite potential customers. Of course, aerod ynamic methods used later in 
the design process will do a much better job of predicting this, so there 
will be time to correct it if the initial guess is a little off. 
Laminar flow is unlikely downstream of a spanwise crack such as where a 
leading-edge flap or slat meets the wing. For this reason, Kruger flaps might 
be preferable on a laminar wing design. Also, the flow near an engine nacelle 
is disturb ed enough that laminar flow is unlikely nearby. Excess sweep makes 
laminar flow difficult. While earlier tests seemed to indicate that laminar flow 
is basically impossible behind a propeller, later tests indicate that some 
Table 12 .4 Laminar Flo w Esti mation Guidelin es 
Attainable Lamin ar Flo w as a Percentage of 
Wetted Area Gener al aviati on-sm ooth metal (no rivets or crack s) 
Gener al aviatio n-sm ooth molded com posites 
Sailpl ane -smoo th molded com posites 
Hel icopter-trad itio nal desi gn 
Heli copter-s mooth design 
Civi l jet-clas si c prod uction metal 
Civil jet-research goal (pass ive) 
Civil jet-research goal (with activ e suction) 
Mil itar y air craft with camouftage 
Supersonic 
Current 
Research goal (with active suction) 
- Unl ikely past crack far movable sur faces lik e leadi ng-edge flaps 
- Unlik ely near wing-mou nted engi nes ( - 1 diame ter each side ) 
- More dif ficult for wings with mor e sweep 
10 
25 
35 
0 
20 
5 
25 
50 
0 
0 
20 
- Reduces behind prop eller (for area in propw ash, mul tiply ab ove by 0.8 and 0.9 ) 
- These are for entir e wetted area of wing, not ju st 20 air foil 
- These are a percenta ge of tota l wetted area, not the length from the nose 
Wing and Tails, 
"lo 
35 
50 
70 
0 
20 
10 
50 
80 
0 
0 
40


<!-- p.420 -->

420 Ai rcr aft Desi gn: A Concept ual Appr oach 
laminar flow is indeed seen behind a propeller. Also, it appears that when the 
flow does go turbule nt, the resu lting drag increase can be slightly reduced in 
the propeller slipstream. 
There are two approaches to increas ing the amount of laminar flow: 
passi ve and active. Passi ve basica lly means shaping and surface finish. We 
use good design practice and fancy comp uter prog rams to shape the 
surface to keep the pressu re reducing as you go from front to rear, for as 
long as pos sible. Obviou sly, you can't keep reducing pressure all of the way 
to the back, so there is a limit. A super smo oth surface finish helps a lot; 
also, we must avoid any cracks, gaps, or other disco ntinuit ies. Even a dried 
bug spla tter will cause laminar flow to become turbulent. 
It is also possible to extend the length of laminar flow by active suction. 
Holes or slot s or porous surfaces are added to the skins, with approp riate 
ducting to either a mechanical air pump or an exit into a low-pres sure 
region outside the airplane. If prop erly sized and loca ted, this literally 
sucks the bound ary-layer air away ju st before it transitions to turbulent. 
The drag reduction is obvious, but studies to date show only marginal 
payoff when the weight, comple xity, power, and volum etric impacts of the 
suction hardware are fully factored. 
In the future it is likely that careful application of active suction, limited 
to a few key areas, will show a subst antial net gain. Other emerging technologies such as the use of tiny dots or ridges ("r iblets") on the skins, or 
soft "compli ant" skins, also show promise and don't require pumps and 
plum bing. 
If an aircraft is designed to have a large amount of laminar flow, it might 
be dangerous to assume that it works all of the time. What about a shortrange comm ercial airliner on the last flight of a long day? After several 
takeoff and landing cycles, dirt and bug splatter can reduce laminar flow 
enough to affect both range and stall speed. Perhaps such airplanes will 
need to factor a worst-case assum ption for fuel reser ves and approach speeds. 
For the por tion of the aircraft that has laminar flow, the flat-plate skinfriction coefficient is expressed by Eq. (1 2.26). For turbulent flow the flatplate skin -friction coefficient is determined by Eq. (12 .2 7), which incl udes 
a Mach number correction, which is trivial at low speeds. Figure 12 .22 
graphs the flat-pla te skin- friction coefficient vs Reynolds number found 
from these equat ions. 
Laminar: 
c1 = i.3 2s;v'R (12. 26) 
Turbulent:


<!-- p.421 -->

0.0070 
0.0060 
0.0050 
c 0.0040 
f 
0.0030 
0.0020 
0.0010 
CHAPTER 12 Aerodyn am ics 42 1 
0.0000 ------------------------0 5 x lQS 1Q6 1.5 x 1Q6 2 x 106 
Reyrrolds numb er 
Fig. 12 .22 Fl at-plate ski n-fric tion coeffici ent vs Reynolds nu mber. 
If the skin surface is relatively rough, the flow will be extra turbulent and 
the friction coefficient will be even higher than indicated by Eq. (12 .27). This 
could be addre ssed with a "fudge factor" multiplied into the Cf result, but a 
better method has been developed. It adjusts not the coefficient itself but the 
Reynolds number used to calcula te the coefficient. 
This is done with a fictitio us "cutoff Reynolds number," determined from 
Eq. (12.28) or (12 .29) using the characteristic length £ and a skin-roughness 
value k from Table 12.5. If the calculated cutoff Reynolds number is lower 
than the actual Reynolds number, then the roughness will increase the 
drag, so the cutoff Reynolds number should be used in Eq. (12 .27) . 
Subsonic: 
Surface 
Rcutoff = 38.21 (£/k) L053 
Table 12 .5 Skin Rough ness Value k 
k, ft 
Camouftage paint on aluminum 3.33 x lo -5 
Smooth pain t 2.os x l o-5 
Production sheet metal l. 33 x 10 -s 
Poli shed sh eet metal 0.5 0 x l o-5 
Smooth molde d composite 0.7 x 10 -5 
(12 .28) 
k. m 
1 .01 5 x 10 -s 
0.6 34 x lo -5 
0.405 x lo -5 
0. 15 2 x 10 -5 
0.052 x lo -5


<!-- p.422 -->

422 Air craft Desi gn: A Conceptual Approach 
Transonic or supersonic: 
R = 44 62(£/k) i. o53 Ml. 16 cutoff 
· (12. 29) 
Once laminar and turbulent flat-plate skin-friction coefficients have been 
calculated, an averaged coefficient is found as the weighted average of the 
two, based on the attainable percent of laminar flow estimated above. 
Mf JJI Component Form Factors and Adju stments 
The calculated flat-plate skin-friction coefficient must be adjusted upwards to take into account the pressure drag caused by flow separationPrandtl's solution to d'Alembert's paradox. This is done with empirical 
"form factors" that have been derived from theoretical and empirical 
consideratio ns. 
Flow sep aration, like the transition from laminar to turbulent, is difficult 
to predict. There are semi- empirical methods to predict separation based on 
calculated press ure coefficients, a common one being "Stratford's Criterio n." 
These are used in computer codes to reshape airfoil and fuselage geomet ry, 
moving the sep aration poi nt as far back as possible. Also, turbulent flow is 
less likely to sepa rate than laminar flow, so where sepa ration is expected, 
designers can delibera tely trigger transition by adding roughness, sharp 
edges, or vortex generato rs. 
Form factors for subson ic drag estimation are presen ted in Eqs. (12. 3012.32). These are considered valid up to the drag- divergent Mach number. In 
Eq. (1 2.30) , the term (x/c)m is the chordw ise location of the airfoil maximum 
thickness poi nt. For most low- speed airfoils, this is at about 0.3 of the chord. 
For high-spee d airfoils this is at about 0.5 of the chord. Am refers to the sweep 
of the maximum-thickness line. 
Wing, tail, strut, and pylon: 
FF= [1 + - (!) + 100 (!) 4] [1 .34M0·18 (cos Am)0· 28J 
(x/c)m c c 
Fuselage and smooth canopy* : 
(12.3 0) 
(12.31) 
*I n prior editions of this book, the fuselage form factor was given as FF = 1 +6 0/f3 + f/400, a 
classic RAND estimation method used in the DATCOMl691 and other sources. This provides a 
good correlation for fineness ratios (f) above 6 as is typical for high-speed and military aircraft, but 
seems to overestimate drag for fineness ratios much below 5. Equations in other sources including 
[40] and [9] provide much lower values at the lower fineness ratios but appear theoretical in derivation. As a compromise, this author has developed the equation shown here. This has same equation 
format of the original but with revised terms bringing it closer to those other equations for lower fineness ratios. It gives conse rvative (larger ) values to account for the additional separation press ure drag 
likely in real airplanes with a short, fat fuselage. At the higher fineness ratios all these equations exponentially approach 1. 0 indica ting that form factor drag becomes nearly negligible.


<!-- p.423 -->

CHAPTER 12 Aerodyn ami cs 423 
Nacelle and smooth external store: 
where 
FF= 1 + (0.35 /f) 
£ £ 
f - - - ----==== - d - )(4/ 7T)Amax 
(12 .3 2) 
(12.3 3) 
A tail surface with a hinged rudder or elevator will have a form factor 
increment* about 10% higher than predicted by Eq. (1 2.3 0) due to the 
extra drag of the gap between the tail surface and its control surface. 
For a fuselage with a steep aft-fus elage closu re angle in front of a pusher 
propeller, the separation drag will be lower than predicted using this 
form-factor equation. The propeller pulls the air around the corner-as 
long as it is spinning (author's wild guess: reduce form factor increment by 
50% but when the engine stops, double it) . 
A square -sided fusel age has a form factor increment about 30-40% 
higher than the value estimated with Eq. (1 2.3 1) due to additional separation caused by the corners. This can be some what reduced by rounding 
the corners. A flying-boat hull has a form factor increment about 50% 
higher, and a float has a form factor increment about three times the 
estimated value. 
Equation (12 .3 1) predicts the form factor for a fuselage but can be used for 
a smoothly lofted blister or fairing such as a pod used for landing-gear 
stowage. It also estimates form factor for a smoot h, one-piece fighter 
canopy such as seen on the F-16. For a typical two-piece canopy with a 
fixed but streamlined winds creen (i.e., F- 15 ), a form factor increment of 
about 40% should be applied. For a canopy with a flat-sided windscreen 
(A- 10 or Me- 109), an increment of 300% should be applied to the canopy estimate. Better yet, find actual drag for a similar canopy and ratio it by fro ntal 
area-see [9l. 
The external bounda ry-layer diverter for a jet inlet mounted on the fuselage can have a significant pressure drag co ntribution which is best estimated 
by comparison to actual data for a similar diverter. As a rough estimate, 
equations (1 2.3 4) and (12 .35) provide form factors to use for a double -wedge 
and single-wedge diverter. The loca l Reynolds number is determined using £, 
and the wetted area is defined as shown in Fig. 12.23. Remember to double 
the drag if there are two inlets. 
Double wedge: 
FF= 1 + (d/£) (12.3 4) 
* These form factor adjustments should be applied only to the pressure-caused increment over the 
skin-friction drag, i.e., the portion of the form factor above 1. 0. If the calculated form factor is 1.2 and 
you wish to apply a 30% increase, the resulting form factor is 1. 26 not 1. 56.


<!-- p.424 -->

424 Ai rcraf t Design : A Conc ept ual Approach 
Double wed ge 
T - 1 
,
t:.
-celle 
I- I 
e -----.._,,,__ , 
I 
Single wedge 
- /l:S: Nacelle 
I ) 
' 
-e ,' 
-, ' 
I 
Fig. 12 .23 Inle t boundar y-layer di verter. 
Single wedge: 
FF = 1 + (2d/£) (12. 35) 
The form factors presented above work quite well for normal aircraft 
designs where reasona ble care has gone into streamlining. Don't apply 
them to automobiles or other non- airplane shapes because those can have 
much more airflow sepa ration, hence higher drag. 
Also, these form factors are based on historical desi gn methods. With our 
modern comp utational tools and superior theoretical underst anding, we are 
smarter than that. For example, the Stratford Criteria mentioned above can 
be used to crea te bodies with less separation and less press ure drag. These 
often have a tadpole-like aft end appearance, as seen on the MD-80 and on 
many human- powered vehicl es. 
If such tools are used to optimize the geomet ry of the fuselage and other 
componen ts, these form factors can be subst antially reduced. Ask your aerodynamics exper t, then carefully check CFD results to confirm any savings. 
This author's wild guess: for smoot h bodies you can prob ably reduce the 
form factor increments above by 10-20%, maybe more. 
Such form factors are corrections to account for pressur e drags and are 
applicable only in subsonic flight. At supersonic speeds, the pressure drags 
covered by these terms are included in the "wave drag" and are estimated 
in a comp letely diff erent manner, described below. 
4f JJj Component Int erference Drag 
Parasi tic drag is increased by the mutual interference between com ponents. This is a catch- all phrase for the various ways that two compon ents,


<!-- p.425 -->

CH APTE R 12 Aerodyn amics 425 
brought together, will have more drag than the sum of their separate drags. 
Interference drag is called Qi n Eq. (1 2.24) and comes from several sources. 
Wherever two componen ts intersect each other, like the wing and fuselage or the vertical and horizon tal tails, their bound ary layers interact. 
Rather than maintaining a sharp corner like the surfaces themsel ves, the 
boundary layers tend to "fill in" the corner. As a result, the boun dary layer 
is thicker, causing more drag. With the thicker boundary layer, there is 
also more oppor tunity for pressure-induced separation and flow reversal. 
This causes even more drag. Fillets are often used to prevent this . 
Another source of interference drag is the "sup ervelocity" effect. The 
airflow around a body such as the fuselage is accelerated to a speed higher 
than the freestream speed. The air is litera lly going faster, so it has a 
higher dynamic pressure. This increases drag for any component immersed 
in that flow, which gets lumped into the interf erence drag term. 
Interference drag is best calculated by a high-end computational aerod ynamics code and is naturally included in wind-tunnel results. For prelimi nary 
estimation, we have to guess it as a percent increase in compon ent drag. 
Again, experience and test data are our guides. 
For a nacelle or external store mounted directly on the fusela ge or wing, 
the interference factor Q is about 1. 5. If the nacelle or store is mounted less 
than about one diameter away, the Q factor is about 1.3. If it is mounted 
much beyond one diameter, the Q factor approaches 1.0. Wing-tip-mou nted 
missiles have a Q factor of about 1.25. 
For a high-wing, a midwing, or a well-filleted low wing, the interference 
will be negligible so that the Q factor will be about 1.0. An undiluted low wing 
can have a Q factor from about 1.1-1 .4. 
The fuselage has a negligible interference factor (Q = 1.0) in most cases. 
Also, Q = 1.0 for a boundary-layer diverter. For tail surfaces, interference 
ranges from about 3% (Q = 1.03) for a clean V-tail to about 8% for an 
H-tail. For a conventional tail, 4-5% can be assumed. l9l 
A favorable interference is possi ble, that is, a drag reduction. If one body 
is substantially behind the other, the one in back will have reduced drag 
because it sees a lower dynamic pressure, and even the body in front can 
have reduced drag because the body in back exerts pressures forward. This 
is the basis of "drafting, " a dangerous practice wherein truck drivers on a 
highway will line up like a train, nose to tail and almost touching, to 
reduce fuel consumption. 
Favorable interference is likely for componen ts placed undernea th the 
wing. Down there, the flow veloc ity is reduced at a higher lift coefficient, 
the opposi te of what happens above the wing. In detailed landing-gear drag 
calculations this should be considered, but we usua lly ignore it for preliminary analysis. 
Component parasite drags can now be determined using Eq. (12 .24) with 
skin-friction coefficients, form factors, and interference factors as described 
above.


<!-- p.426 -->

426 Aircr aft Desi gn: A Conceptual Approach 
4f JD Mi scella neous Drags 
The drag method described above works well for streamlined objects 
such as wings, tails, and fuselage s. For various miscellaneous obje cts sticking 
out into the flow, we rely upon test data and empirical methods, some of 
which are presented below. The results are then added to those smoot h component drags. 
While the drag of smo oth external stores can be estimated using Eq. 
(12. 31), many external stores are not very smoot h, so these methods don't 
really work. Inst ead, we rely upon test data. Figures 12. 24- 12.26 provide 
drag data for typical external fuel tanks and weapons, presented as drag 
divided by dynamic pressur e (D-over-q or D / q). 
D/q is a commo nly used parameter and has units of square feet (or 
meters ), so is some times called the "drag area." D/q times the dynami c 
pressure gives you the actual drag force. Or, if D / q is divided by the wing 
reference area, it yields the parasi tic drag coefficient for that compon ent. 
Most transport and cargo aircraft have a pronounced upsweep to the 
aft fuselage (Fig. 12.27) causing additional flow separation. This increases 
the drag beyond the value calculated using Eq. (12 .31). This extra drag is a 
D!q 
ft2 m2 300- gallon ta nk 
2.5 on wing 
30 0-gallon ta nk 
0.20 on fuse lage 
2.0 
15 0-ga ll on ta nk 
on wing 
0.15 
15 0-ga llon ta nk 
on fuse lage 
1.5 
0.10 
1.0 
05 ,___o_.o_5 __________ _ 
O +------------------0.4 0.5 0.6 0.7 0.8 0.9 
Mach nu mber 
Fig. 12 .2 4 Extern al stores (fuel tonks) drag. 
1.0


<!-- p.427 -->

Dlq 
ft2 m2 
2.5 
0.20 
2.0 
L5 0.15 
LO 0.10 
0.5 0.05 
CHAPTE R 12 Aerodyn amics 427 
6-500 lb bomb clus ter 
(no t including rack dr ag) 
6-250 lb bomb cl uster 
(not including rack dr ag) 
2000 lb bomb on fuselage 
2000 lb bomb on wing 
Aim-9 missile and 
pyl on 
o -+---------------------0.4 0.5 0.6 0.7 0.8 0.9 LO 
Mach numb er 
Fig. 12 .25 Bomb and mi ssile drag . 
1.1 L2 
complicated function of the fuselage cross-s ectional shape and the aircraft 
angle of attack, but can be approximated using Eq. (1 2.36) where u is the 
upsweep angle (radians) of the fuselage centerline (not the belly angle) and 
Dlq 
ft2 m2 
1.5 
1.0 0.10 
0.5 0.05 
Mu ltiple bo mb cl uster rack 
__..- Fuselage stores pyl on 
- Wing stores pylon 
0 -+------------------0.5 0.6 0.7 0.8 0.9 1.0 
Mach nu mber 
Fig. 12 .26 Pylon and bomb rack drag . 
1.1


<!-- p.428 -->

428 Ai rcraf t Des ign: A Conce pt ual Approach 
(u is in radia ns) 
Fig. 12 .27 Fuselage upsweep. 
Amax is the maximum cross-sec tional area of the fuselage. 
D/qupsweep = 3.83u2·5 Amax (12 .36) 
Rearward-facing flat areas are called "base" and create a large drag called 
"base drag." This can be estimated using Eqs. (12.37) and (12.38). l73l The 
term Abase includes actual aft-facing flat surfaces as well as the aft-projected 
areas of steeply angled regions likely to experience separated airflow. Roughly 
speaking, this should be expected any place where the aft angle to the freestream exceeds about 20 deg. As already mentioned, a pusher propeller can 
prevent aft-fuselage separation despite an aft fuselage angle of 30 deg or more. 
Subsonic: 
(Djq)base = [0.139 + 0.419(M - 0.161 f]Abase (12 .37) 
Supersonic: 
(Djq)base = [0.064 + 0.042(M - 3.84)2]Abase (12 .38) 
When calc ulating aircraft drag, there are a number of odd compone nts, 
many of them small, that need to be included for a full estimate. Some of 
them are lumped into the "lea kage and protuberance" drag term discussed 
belo w. Others must be estimated by whatever means can be found, includ ing 
test data from similar airplanes, sep arate compon ents drag tests, and educated guesses based on the closest thing that can be found. 
Reasona ble estimates for various compon ents seen on airplanes can be 
found in Table 12.6, taken from many sources, especia lly. l9l These values 
times the fro ntal area of the indicated component yield D / q values, which 
are divided by the wing reference area to obtain parasitic drag coefficients. 
Drag coefficients that are referenced to the compo nent's frontal area are 
sometimes called CD71"· 
Speed brakes are plates that extend from the fuselage or wing. They 
are used to slow down in flight, establish a rate of descent espec ially for 
land ing, and slow down after touchd own. They are espec ially needed for 
jet aircraft because jet engines produce substantial thrust even at their lowest 
power setting. Speed brakes mounted on top of the wing will disturb the


<!-- p.429 -->

CH APTE R 12 Aerody namics 429 
airflow and spoil the lift, so they are also called "spoilers." These further 
reduce landing distance by transferring more of the aircraft's weight to the 
landing gear, which increases the braking action. 
The strut, wire, and fitting data in Table 12.6 can be used to estimate 
the drag for a braced wing or biplane. For struts, the optimal thickness 
ratio considering both aerod ynamic and structural efficie ncy is about 0.19 
for a strut in tension and about 0.23 for a strut in compression. 
Landing -gear drag is best estimated by compa rison to actual test data, 
preferably comp any data for a recent and similar design. Some data are 
available in[9,i5,47l and other references, but adjustments are required to 
reflect the geomet ry of a new design. 
Table 12 .6 Mi scella neous and Landi ng- Gea r Com ponent Drags 
[ D/q ] CD - ---1 " - Frontal Area 
Flat plate perpe ndicular to ftow 1. 28 
Sphere al one-h igh R# 0. 10 
Sph ere alon e-low R# 0.3 -0.5 
Hol low sp here, open end forward 1. 40 
Hollo w spher e, open end to rear 0.4 0 
Bul let sha pe, blun t back 0.3 0 
Exposed water-c ooled radia tor 1. 00 
Cowled water-c ooled radia tor 0.3-0 .5 
Air scoops 1. 2-2 .0 
Contr ol horn 0.3 -0.8 
Speed bra ke-fuselage mounted 1 .00 
Speed bra ke-wi ng mou nted 1. 60 
Windshield smo othly faired into fuselage O.Q7 
Windsh ield-sharp edged, poorly faired 0. 15 
Open cockpit (ref. wind screen A-fronta l) 0.5 0 
Parach ute or drogue chute 1. 40 
Regular wheel and tir e 0.25 
Second wheel and tir e in tandem 0. 15 
Strea mlin ed wheel and tire 0. 18 
Wheel and tir e with fairing 0. 13 
Streamli ned strut (1/6 < t/c < 1/3) 0.05 
Round strut or wire (R# > 3 x 10 5) 0.30 
Round strut or wire (R# < 3 x 10 5) 1. 17 
Flat spring gea r leg 1 .40 
Fork, bogey, irregular fitting 1 .0-1 .4


<!-- p.430 -->

430 Air craft Des ign : A Conceptual Approach 
Another way to estimate landing-gear drag is to sum drag estimate s 
for the individual landing-gear componen ts including wheels, struts, forks, 
and others. Suitable values can be found in Table 12 .6. To account for 
mutual interfere nce, the sum of the gear component drags can be multipli ed 
by 1. 2. Also, the total gear drag should be increased by about 7% for a retrac table landing gear in which the gear doors are left open when the gear 
is down. 
As mentioned in the last sec tion, landing-gear drag is actually a functi on 
of lift. The more lift the aircraft wing is producing, the slower the airflow 
undernea th the wing where the gear is loca ted. Hence, at higher lift coeffi cients the gear drag is reduced. This can be ignored for initial analysis. 
Other aircraft compo nent drag estimates are provided in Table 12 .7, 
including drag of a pilot in various attitudes for an aircraft with an unenclosed cockpit, arresting hooks, and machine-gun and cannon ports These 
are actual values rather than ratioed to frontal areas because they are 
actual compone nts. Flap drag is discussed in Sec. 12.6.5, and drag data suitable for helicopter analysis are found in Chapter 20. 
Mf Jff Leak age and Protuber anc e Drag 
Leakage and protuberances add drag that is difficult to predict by any 
method. Leakage drag is due to the tendency of an aircraft to "inhale" 
through holes and gaps in high-pressure zones and "exhale" into the lowpressure zones. The freestream momen tum of the air "inhaled" contributes 
directly to drag, and the air "exhaled" tends to produce additional airflow separation wherever it escapes. 
Protuberances include antennas, lights, door edges, fuel vents, control 
surface external hinges, actuator fairings, and such manufacturing defects 
as protruding rivets and rough or misaligned skin panels. These are things 
that don't appear on a configurat ion layout during conce ptual design and 
aren't fully defined until detail desi gn and fabricat ion. It simpl y isn't possi ble 
to calculate their drag directly-we don't know what they are! 
Instead, these drag increments are estimated as a percen tage of the 
total parasite drag. Typical factors are given in Table 12.8. An aircraft with 
Table 12 .7 Component Misc ella neous Drags 
l•ll•l•llufl 
Arrestin g hook-USN 0. 15 0.01 4 
Arrestin g hook -USAF 0. 10 0. 009 
Machine gun ports 0.02 0.0 02 
Cannon port 0.20 0.01 9 
Exposed pilo t-prone 1 .20 0.1 11 
Exposed pil ot-seated 6. 00 0. 557 
Exposed pilo t-spread eag le 9.00 0.836


<!-- p.431 -->

CH APTER 12 Aerodyn ami cs 43 1 
Table 12 .8 Leak age and Protuber an ce Drag 
Air craft Type I It •• 
Propeller ai rcraf t 5-1 0 
Jet tra nspor ts or bom bers 2-5 
Non- stea lth fig hter s 10 -1 5 
Stealth fighters 3-5 
variable- sweep wings will have an additional protuberance drag of about 3% 
due to the gaps and steps of the wing pivot area. 
If special care is taken during desi gn and manufacturing, these drag increments can be reduced to near zero but at a considerable expense. Normally, 
only race planes are subj ected to such extreme "clea nup," but the careful 
elimination of protuberances required for stealth desi gn does result in an 
aerodynamic benefit. 
If JJ:I Stopped-Pr ope ller and Win dmilli ng Engine Drags 
The specifications for civilian and military aircraft require takeoff and 
climb capabilities following an engine failure. Not only does this reduce 
the available thrust, but the drag of the stopped propeller or windmilling 
engine must be considered. 
Data on the drag of a stopped or windmilling propeller are normally 
obtained from the manufacturer. For a jet engine, detailed knowledge of 
the characteristics of the engine, inlet, and nozzle are required to estimate 
the drag from a stopped or windmilling engine. In the absence of such 
data, the following rough approximations can be used. 
For a stopped propeller, l9J indicates that the subsonic drag coefficien t will 
be about 0. 1 based upon the total blade area if the propeller is feathered 
(turned so that the blades align with the airflow) . If the propeller has fixed 
pitch and cannot be feathered, the drag coefficient is about 0.8. 
To determine the total blade area, it is necessa ry to know or to estimate 
the propeller solidity u, the ratio between the total blade area and the propeller disk area. This can be shown to equal the number of blades divided by the 
blade aspect ratio and 7T. 
For a typical blade aspect ratio of 8, the solidity will be 0.04 times the 
number of blades. A small piston-prop engine will gene rally use a two-bladed 
propeller. A fast piston-prop or a small turboprop will use a three-b laded 
propeller, whereas a large turboprop can use a four-b laded propeller. 
Drag of a feathered propeller can be roughly estimated by Eq. (12. 39) . 
For an unfeathered, stopped prope ller, the 0.1 term is replaced by 0.8. 
(D / q)feathered prop = O. lo-Apropellerdisk (12 .39) 
For jet engines, [74] indicates that the subsonic drag coefficient of a windmilling turboj et engine will be about 0.3, referenced to the flow area at the


<!-- p.432 -->

432 Aircr aft Desi gn: A Con cep tual Approach 
engine's front face. Thus, the drag of a windmilling turbojet will be appro ximately 
(D / q )windmilling jet = 0.3Aengine front face (12. 40) 
Mf f p Super soni c Par asit e Drag 
The supersonic parasite drag is calculated in a similar fashion to the subsonic drag, with two except ions. The supersonic skin- friction drag does not 
recei ve adjustments for form factors, nor for interference effects. These are 
both pressure drags. In supersonic flight, all pressure drags are included 
in a new term called "wave drag." In other words, we set FF and Q equal 
to 1.0 and then add a wave drag term which incorpo rates them. 
Wave drag is the extra drag at supersonic speeds and acco unts for the 
pressure drag due to shock formation. Supersonic parasite- drag buildup is 
then defined in Eq. (12 .41): 
C . = -(CfcSwetJ C C C Dosupersomc S + Dmisc + DL&P + Dwave ref (12. 41) 
The supersonic turbulent skin-fr iction coeffici ent was already presen ted 
in Eq. (1 2.27), using the cutoff Reynolds number from Eq. (1 2.29). 
Various "Miscellaneous" drag calculations in supersonic flight were presented above. More can be found in[9] and other references, espec ially NACA 
repor ts. Of course, many of the items that produce miscellaneous drag for 
subsonic aircraft will not appear on a supersonic aircraft-f loats, open cockpits, wing struts (bu t see Chapter 22!). 
To a first approximation, the drag due to leaks and protuberances in 
supersonic flight follows about the same percentages as presen ted for subsonic flight. 
This new term, supersonic "wave drag'', will often be greater than all of 
the other drags put together. Wave drag is pressure drag due to shocks 
and is a direct result of the way in which the aircraft's volume is distributed 
from nose to tail. 
An ideal volume distribution is produced by the Sears- Haack body)25l 
which was shown in Fig. 8.3. A Sears- Haack body, as defined by Eq. 
(1 2.42) , has a wave drag with a simple analytical calculation as seen in Eq. 
(1 2.44). This is the minimum possi ble wave drag for any closed-end circular 
cross-s ection body of the same length and total volume. 
r 
(12 .42) 
where 
r = the cross-se ction radius 
e = the long itudinal dimension


<!-- p.433 -->

CHAP TER 12 Aerodynamics 433 
and 
-£/2 s x s £/2 
91T Amax ( )2 
(D/q)wave = 2 -£where Amax is the maximum cross-sec tional area. 
(12 .43) 
(12 .44) 
The linear area- rule theory says that the theoretical wave drag of an aircraft at Mach 1. 0 is identica l to the wave drag of a body of revolution with the 
same volume- distrib ution plot. In other words, the actual cross-s ectional 
shape at a given longitudinal loca tion has no effect on wave drag at Mach 
1.0. All that matters is the cross-s ectional area at each longitudinal location 
and the way that the cross-sec tional area varies longitudi nally. 
This leads to the area-rule principle for minimizing wave drag. Wave drag 
at Mach 1. 0 is minimized when the aircraft has a volume distribution 
identical to that of a Sear s-Ha ack body. Drag is reduced when the volume 
distribution is changed to more resemble the Sears-Ha ack's, which has a 
minimal amount of longitudinal curvature .* 
As discussed in Chapter 8, the wave drag at Mach 1.0 is direct ly related to 
the second derivative (i.e., curvatu re) of the longitudinal volume distri bution. 
To minimize wave drag, the designer should try to arrange the configurati on 
so that the volume distribution is smoot h and bell- shaped, looking like a 
Sears-Haack body. Unfortunately, the wing tends to put a "bump" in the 
volume distribution. This bump can be reduced by pinching in the fuselage at 
the wing location, creating the characteristic "coke-bottle" area-ruled fuselage. 
No realistic aircraft will have a volume distribution identical to that of a 
Sears- Haack body, so we cannot expect our desi gn to reach the ideal wave 
drag of that shape. However, a typical supersonic aircraft will have a wave 
drag that is perhaps twice the Sears-Ha ack value. Ratios of actual wave drag 
to the optimum Sear s-Ha ack value will be used below as a first-order wave 
drag estimation method. 
At Mach 1. 0, shocks form at an angle of 90 deg to the freestream direction. At Mach numbers greater than 1. 0, the shocks form at an angle 
greater than 90 deg. The "Mach angle" is the smallest angle at which a 
shock can form, repres enting a "zero- strength" shock. Mach angle is defined 
as arcsine (1/ M). 
At Mach 1. 0, the wave drag is based upon the aircraft's cross-s ectional 
areas found by the intersection of the aircraft and an infinite plane set at 
an angle perpendicular (90 deg) to the freestream direction. At speeds 
higher than Mach 1. 0, the wave drag still depends upon the volume distribution as before, but with one ma jor exception. At higher Mach numbers 
* Strangely, the drag theory that gives this beautiful result isn't really applicable at Mach l, because 
it assume that changes in flow velocity in the flow direction are negligible. This is a good approximation at higher Mach numbers but clearly untrue at Mach 1. Still, the theory points us to an 
optimal shaping strategy which wind tunnel and flight test data have repeatedly confirmed.


<!-- p.434 -->

434 Air c raf t Desi gn: A Conceptual Appr oach 
the volume distribution is based upon aircraft cross sections that are determined by intersect ing the aircraft with "Mach planes ," set at the approp riate 
Mach angle to the freestream direction ("cut plan es") . 
A Mach plane can be rolled about the freestream direction to any roll 
angle. Figure 12.28 shows two roll angles. Note that the different Mach-p lane 
roll angles produce entirely different volume- distribution plots. In the left 
illustration, the Mach-plane cut includes the fuselage and canopy plus a 
slice of the left wing. In the right illustration, only the fuselage and canopy 
are cut, producing a much smaller cros s-se ctional area at that location . 
For each Mach-plane roll angle, a volume-dist ribution plot can be prepared by taking Mach-pla ne cuts at a number of longitudinal locations . 
According to linear wave drag theory, l75l the superson ic wave drag at 
Mach numbers greater than 1.0 is determined by averaging the wave drags 
of the Mach-plane-cut volume distributions for different roll angles. 
This is the basis of the classic Harris wave drag code. f76l A simpli fied 
comp uter code suitable for university use is presented in[77] altho ugh these 
days the full Harris code is available for use on person al computers. 
The use of canted Mach-plane cuts to determine the volume dist ribution 
at Mach numbers greater than 1.0 requires a different approach to area 
ruling. Pinc hing the fuselage at the wing location might smoot h out the 
volume distribution for one Mach-plane roll angle, but might make the 
volume distribution even less smooth at another Mach-plane roll angle. 
Cross-sect ion 
ar ea* 
Cross-sec tion 
ar ea* 
Flight 
dir ection 
Fuselage station Fuselage station 
*P rojected for ward onto a plane perpe ndicular to the fl ight dir ection 
Fig. 12 .28 Mach-p lane cut volume di stri bution (two roll angle s).


<!-- p.435 -->

CHAP TER 12 Aerodyn ami cs 435 
At higher Mach numbers it is very difficult to minim ize total wave drag by 
"eyeball" area ruling. Instead it is more profitable to smooth the entire configuration through wing-body blen ding, as seen on the B- lB and in the desi gn 
concept of Fig. 7 .2. 
For preliminar y wave drag analysis without use of a computer, a cor relation to the Sears- Haack body wave drag is presented in Eq. (1 2.45). The 
Sears- Haack wave drag D/q is easi ly calculated using Eq. (1 2.44). 
The maximum cross-se ctional area Amax is determined from the 
aircraft volume- distribution plot. Inlet capture area should be subtracted 
from Amax· The length term £ is the aircraft length except that any portion 
of the aircraft with a constant cross- sectional area should be subtracted 
from the length . 
If a desi gn has the location of its maximum cross-se ction area far behind 
the midpoint of its fuselage, it should be assumed that the fusela ge length is 
double the distance from nose to the location of maximum cross-s ection 
area. In such a case, though, there will prob ably be increased sepa ration 
and hence larger base drag from this -edge -shaped design. l78l 
0.57 7r: LE-deg 
[ ( A0.77 )] (D/q)wave =EwD 1 - 0.386(M - l.2) 1 - lOO (D/q)sears-Haack 
(12 .45) 
Ewd is an empirical wave-drag efficiency factor and is the ratio between 
actual wave drag and the Sears- Haack value. For a perfect Sears- Haack 
body, Ewd = 1.0. 
A very clean aircraft with a smooth volume distribution, such as a 
blended- delta-w ing design, might have an EwD as low as 1.2. A more 
typical supersonic fighter, bom ber, or SST design has an EwD of about 
1.8-2.2. A poor supersonic design with a very bumpy volume distribution 
can have an EwD of 2.5-3.0. The F-1 5, optimized for the dogfight instead 
of supersonic flight, has an EwD of about 2.9. l67l 
Note that this efficienc y factor is less impor tant in drag determination 
than the fineness ratio as represented by (Amax/£). This term is squared, 
which explains why area ruling that actually reduces Amax provides a far 
greater drag reduction than does merely smoot hing the volume distribution 
without lowering Amax· 
The complicated middle term in Eq. (1 2.45) encased in square brackets 
represents the drop off in wave drag coefficient as speed increases past 
Mach 1.2. This is proba bly due to the wing effects on the canted-cut 
volume distributions as described earlier. This author notes that this old 
empirical relationship seems overly optimistic and gets better results by 
replacing the 0.386 term with 0.2.


<!-- p.436 -->

436 Aircr aft De sign : A Concep tu al Approach 
Af Jjl11 Tran soni c Par asit e Drag 
The transonic flow regime extends roughly from Mach 0.8- 1.2. Technically, it is defined as the Mach numbers at which there is both subsonic and 
supersonic flow around the aircraft. At high subsonic speeds, the flow over 
the wings and perhaps near the front of the fuselage is accele rated to supersonic speeds. Then once the aircraft is actua lly flying at supersonic speed s, 
there are regions around the aircraft where the flow is shocked down to 
subsonic speeds, such as direct ly in front of the canopy. At an even higher 
speed, all flow is supersonic. 
The increase in drag as an aircraft accelerates through the transonic 
regime, called the "drag rise," is due to the formation of shocks. The critica l 
Mach number Mer occurs when shocks first form on the aircraft. The dragdivergent Mach number Moo is the slightly higher Mach number at which 
the format ion of shocks begins to subst antially affect the drag. 
The definition of what speed constitutes Moo is arbitrary, and several 
definitions are in use. The Boeing definition is that Moo is where the drag 
rise reaches 20 counts. Moo (Bo eing) is usua lly about 0.08 Mach above the 
critical Mach number. The Douglas definition, also used by the U.S. Air 
Force in [69l , defines Moo as the Mach number at which the rate of change 
in drag with Mach number (dCD0 /dM) first reaches 0.10 . 
The Douglas Moo is typically 0.06 Mach above the Boeing Moo and represe nts a drag rise of perhaps 80- 100 counts. Jet transpor ts usually cruise at 
about Moo (Boei ng) and have a maximum level speed of about Moo 
(Dougla s). 
Shocks are formed on the top of the wing as a result of the increased 
airflow veloc ity, so that Moo reduces with an increased lift coefficient. For 
example, the Boeing 727 has an Moo of about Mach 0.86 when the lift coefficient is only 0.1, but when the lift coefficient is increased to 0.3, the Moo 
reduces to about Mach 0.82. 
A prelimi nary estimate of wing Moo (Boei ng) is provided by Eq. (1 2.46) 
using Figs. 12 .29 and 12. 30. Figure 12.2 9 provides the wing drag- divergence 
Mach number of an uncambered wing at zero lift. Figure 12.30 adjusts Moo 
to the actual lift coefficient. 
The last term in Eq. (1 2.46) is an adjus tment for the wing desi gn lift coefficient (i.e., camber and twist) . Initially, it can be assumed that the design lift 
coefficien t is the same as the lift coefficient at cruis e. 
(12.4 6) 
If the wing uses a supercritical airfoil, the actual thickness ratio should be 
multiplied by 0.6 before using these figures. This approximation is to acco unt 
for the shock- delaying characteristics of the supercritical airfoil. 
Moo changes with lift coefficient. Lift coefficient changes with weight 
and altitude, both of which can change during cruise. To be completely accurate, it is necessa ry to calculate Moo for each point in the mission. For initial


<!-- p.437 -->

1.0 
0.95 
gi 0.90 
'(jj 
0 
0 
0 
- 0.85 
tic 
0.04 
0.06 
0.80 0.08 
0. 10 
0.12 
'C L= CLdesign = 0 
• Conv enti onal 
air foil 
CHAPTE R 12 Aerodyn ami cs 437 
0.75 +-----+----+-----+---___,f-----+-----+10 20 30 50 60 70 
Fig. 12 .2 9 Wing drag-div ergence Mach nu mber. 
analysis, however, it is acceptable to use a single Moo based upon a midmission weight and cruise altitu de. 
If the fusela ge is relatively blunt, it will experience shock formation before 
the wing does. In this case, Moo is set by the shape of the forebod y. Body 
Moo can be estimated using Fig. 12. 31J7 9l where Ln is the length from the 
nose to the longitudinal loca tion at which the fusela ge cross section 
becomes ess entially cons tant. The body diameter at that location is d. If 
the fuselage is noncir cular, d is an equivalent diameter based upon the fuselage cross-sec tional area. Dete rmine both wing and fus elage Moo, and use 
the lower value. 
0.1 0.2 0.3 
Lift coeff icient CL 
Fig. 12 .30 Lift adj ustment for M00 . 
tic 
0.04 
0.06 
0.08 
0.10 
0.14


<!-- p.438 -->

438 Aircr aft Desi gn: A Con cep tual Approach 
1. 0 
Sup ers onic design 
0.9 \ 
Cl ':E.Cl 0.8 
0.7 
0.6 +---t---+---t----t--t---+---t---+----+----1 
0 2 4 6 8 10 12 14 16 
(2-n) 
Fig. 12 .31 Body drag-d iverg ent Mach numb er. 
18 20 
The linear wave drag analysis gives complet ely incorrect results in the 
transonic regime. This analysis is called "linear" because the higher-or der, 
nonlinear terms have been dropped from the aerod ynamic equations to 
permit compu tation. Some of these dropped nonlinear terms accou nt for 
any changes in the airflow longitudinal veloc ity. At high supersonic speeds 
these terms have little effect compared to the far greater aircraft velocity. 
However, the drag rise at transonic speeds is largely caused by the increase 
in airflow veloci ty over the top of the wing. Thus, drag rise below Mach 
1.0 is in fact caused by the terms that are dropped in the linear analysis! 
So-c alled "no nlinear" compu tational aerod ynamic progr ams can give reasonable analytical results within the transonic regime, as do high-end Euler and 
Navier-Stokes codes. 
Empirical methods for the calculation of the drag rise are pres ented in[69l . 
These estimate the drag rise for the wing and fuselage separa tely, so the 
benefits of area ruling are ignored. These methods are very time cons uming 
and not very accurate, so an approximation technique is presented next. 
For initial analysis the drag rise can be graphic ally estimated using a few 
rules of thumb, as shown in Fig. 12.32. The drag at and above Mach 1.2 
(labeled A in the figure) is determined using Eq. (1 2.45) (divided by wing 
reference area) . The drag at Mach 1.05 (labeled B) is typically equal to the 
drag at Mach 1.2.


<!-- p.439 -->

CHAPTER 12 Aerodyn amics 439 
The drag at Mach 1. 0 (labeled C) is about half of the Mach 1. 05 value. The 
drag rise at Moo (just determined) is 0.0 02 by definition (labeled D). Mm the 
beginning of drag rise, is roughly 0.08 slower in Mach number than Moo and 
is labeled E. 
To complete the transonic-d rag-rise curve from these points, draw a 
straight line through points B and C, extending almost to the horizon tal 
axis. Then, draw a curve from Mer through Moo, which fairs smoot hly 
into the straight line as shown. If a smoot h curve cannot be drawn, the 
Mer point (E) should be moved until an approxima tely circular arc can be 
drawn. Finally, draw a smooth curve connecting B to A. 
This technique can be used even for subsonic transport aircraft. The 
supersonic wave drag (point B) is determined from Eq. (1 2.45) even 
though the aircraft will never fly at this speed. When calculating the 
Sears -Ha ack D/q for Eq. (1 2.44), remember to subtract from the aircraft 
length the portions of the aircraft where the cross-sec tiona l area is constant. 
Also, data indicate that an Ewd of 4.0 will approximate a transport aircraft's 
drag rise. 
If Jjll Comple te Parasit e-Dr ag Buil dup 
Figure 12. 33 illustrates the complete buildup of paras ite drag vs Mach 
number for subsonic, transonic, and supersonic flight. The subsonic drag 
consists of the skin-friction drag, including form factor and interfere nce, 
Dr ag 
rise 
0.002 
c 
0 '--------------'-+----+-+---+----O E Mach 
1. 20 
Fig. 12 .32 Transonic drag rise esti mat ion. 
numb er


<!-- p.440 -->

440 Ai rc raft Desig n: A Concep tual Approach 
Leaks and 
protu berances 
Mi scella neous 
Form and interference 
-- - - - --Skin fric tion drag 
o- --------+----t----t-------O Mach numb er 
MDD 1.0 1.2 
Fig. 12 .33 Comple te parasite drag vs Mach numb er. 
plus miscellaneous drag and leak and protuberance drag. The superson ic 
drag includes the flat-pla te supersonic skin-friction drag, miscella neous 
drag, leak and protuberance drag, and wave drag. 
In the transonic regime, the skin-friction drag is estimated simply by 
drawing a straight line between the skin-friction drag at MDD (which includes 
form factor and interference) and the skin-friction drag at Ml.2 (which does 
not) . This does not reflect any reduction in drag, merely a change in bookkeeping. The pressure drags represented by the form and interference 
terms at subsonic speeds are included in the wave-drag term at superson ic 
speeds. 
In Fig. 12 .34, the actual parasite drag and drag rise are shown for a 
number of aircraft. The various symbols are to help track the lines from subsonic to supersonic and have no other meaning. The Rock well A TF is the 
author's never-bui lt Super cruise desi gn for the Advanced Tactical Fighter 
program, seen in Fig. 7.2. The ATF program ultimatel y produced the F-22, 
not this wave-drag optimized configura tion. l2l 
It is difficult to compare the different airplanes in this figure because they 
all have different wing areas. Is the B-70 as great as it appears? Its drag is 
referenced to its huge wing area. Prob ably the best way to compare different 
airplanes in subsonic flight is to normalize their drag based upon their 
maximum cross- section areas, not their wing areas. For supersonic drag, it 
is proba bly best to comp are values of Ewd, the empirical wave-drag efficiency 
factor presen ted above as the ratio between actual wave drag and the SearsHaack drag value for that airplane's length and maximum cross-s ection


<!-- p.441 -->

CHAPTE R 12 Aero dynamics 44 1 
area. A desi gn with a low Ewd shows clever and efficient aerodynamic design, 
not just a high fineness ratio or a large reference wing. 
gJJf I Drag Map 
A "Drag Map" is a useful and under-a ppreciated tool for those desi gning 
aircraft intended to cruise at high subsonic speeds, espec ially commercial airliners which generally cruise at about the speed at which shocks first form on 
the top of the wings. The Drag Map is simply a plot of drag versus Mach 
number and includes the drag rise from shock formation. Unlike Figure 
12 .33, it includes the drag-due-to-l ift at various arbitrary lift coefficien ts 
so there are several lines, not just one. The Drag Map also includes the lift 
coefficient effect on the drag-di vergent Mach number, which is not apparent 
on a plot of CD0 alone. A typical Drag Map is shown as Figure 12.35. 
From the completed Drag Map one can see the effect of lift coefficien t on 
total drag and the drag divergent Mach number. You can also infer the desirability of climbing to a higher altitude for cruise -the thinner air requires a 
higher lift coefficient, and that might subj ect you to the drag rise. 
Drag Maps are an excellent tool for comparing the relative aerod ynamic 
efficienc ies of different aircraft, although taking account of the differing wing 
reference areas can be problematic. They also allow you to calculated L/D 
and ML/D for different Mach numbers. For a detailed discussion of Drag 
Maps and their application, see [175l . 
0.06 
F- 15 --a 
0.05 
-0 
0.04 F-4 
c 
e cJ F- 10 5 k 
RA-5C ---o 0 0.03 
cJO 
0.02 F-1 0 
ock well ATF-B-70 
o -------------0.5 1.0 1. 5 
Mach numb er 
Fig. 12 .34 Parasite drag and drag rise. 
2.0 
l 
I 
I 
2.5


<!-- p.442 -->

442 Ai rcr aft Desig n: A Conceptual Appr oach 
0.0500 ---------------------0.0450 I-------+------+------+'-' -----+-• 0.5 . . 
0.4 0.0400 !------+------+----- ---+--------;-. 
/ : 0.3 , / I 0.0350 1------------+--------+------C-t-----;f--. . . . . . . . . . . . . . . . . . . . . . . . . . . . ....... J t·2 
0.0300 1-------+-------+-------+-r'----+---+---lJ / /
1 -- --- ------ .. .. .. .... .. .... .... .. .. .. .. .... .. .. .. .. .. ...... .. .. .. .... .. . . . 
0.0250 t=====t=====t======r-,,..,_-1;11,-0.0 0.0200 1-----J-----+----=-=-_./------7L__----f-i/L 
---+----+----r-- __/ 0.0150 l------l-----+---==:f== :::::: ::::::::__-1-0.0100 '-------'-------------'-----------'0.5 0.6 0.7 0.8 
Mach numb er 
Fig. 12 .35 Drag Map for Typical Commer cial Airliner (after Hays) . 
Drag Due to Lift (Incl uding Ind uced Drag) 
0.9 
"Induced drag" is the drag that is literally caused by the creation of lift. 
When a wing is lifting, the higher-pressure air under the wing escapes 
around the wing tip to the wing's upper surface, reducing the lift and creating 
tip vortices from the rotational inertia of the air. The rotational energy left in 
those tip vortices after the airplane passes does nothing useful for the airplane, but is ultimately energy taken from the gas tank. This induced drag 
is theo retic ally propor tional to the square of the lift coefficient-double the 
lift, and you get four times the drag. 
"Drag due to lift" is the broader term and includes all of the drags that 
change as the lift is changed. A major portion of drag due to lift is obviously 
the induced drag, and we often get sloppy and use either term interchangeably. Drag due to lift also includes the changes in viscous separation drag that 
occur as airfoil angle of attack is changed because the sep aration point moves 
forward at higher lift coefficients. There are other, lesser effects that are 
included such as the slight change in parasitic drag resulting from the 
changes in flow velocity above and below a wing as its angle of attack 
is varied. 
These additional contributors to drag due to lift also tend to vary by the 
square of the lift coefficien t, not exactly but close enou gh that the total


<!-- p.443 -->

CHAPTE R 12 Aerodyn ami cs 443 
follows about the same trend as the induced drag portion alone, at a slightly 
higher magnitude. 
There is anot her effect that gets lumped into the drag due to lift and is 
typical for a wing designed for laminar flow. The po int on the airfoil at 
which the flow transitions from laminar to turbulent will move forward 
with increased angle of attack, causing an increased skin-friction drag that 
varies with lift co efficient. NASA tests of the Cessna P-210 Centurion 
showed that while it had laminar flow on the upper surface for the first 
44% of the wing's chord at a lift coefficient of 0.26, this dropped to 29% for 
an almost trivial increase in the lift coefficient to 0.28. At a lift co efficient 
of 0.35, this plummeted to only 5% of chord. This causes the so -called 
"laminar bucket" typically seen on laminar-f low airfoils and wings . Note 
that the lower surface did not see this effect in testing, transitioning at 
about 40% of chor d all the time. 
These non- induced- drag contributors to drag due to lift must be included 
in drag analysis but are difficult to predict by anything less than full com putational fluid dynamics (CFD, desc ribed later) . Instead, we generally rely 
upon some statistical method to "bump up" the easily calculated theoretical 
induced drag portion. 
To a good first approxima tion, at moderate angles of attack the induced 
drag is propor tional to the square of the lift co efficient, with a proportio nality 
called the "drag- due-to -lift factor," or K [see Eq. (1 2.4)]. Theoretic ally, the 
induced drag in inviscid flow has a K-factor of simply the inverse of the 
product of aspect ratio and 7T. This easy calculation underpredicts the drag 
due to lift because it doesn't include the non-in duced- drag portions, and 
also because it assumes a perfect elliptical lift distrib ution. 
Two methods of estimating a more realistic K-factor will be presented. 
The first is the classica l method based upon e, the Oswald span efficie ncy 
factor. Methods are presented for subsonic monoplanes and biplanes along 
with an empirical equation for supersonic speeds. 
The secon d method for the estimation of K is based upon a concept 
called "leading- edge sucti on" and provides a better estimate of ](, one that 
includes the effects of the change in viscous separati on as lift co efficient 
is changed, and also handles the Mach effects 
ignored in simpler metho ds. This method also 
reflects the impact of the designer's chosen wing 
design lift co efficient. 
If DI Oswa ld Spa n Efficienc y Method 
Twice the lift gives 
four times the 
drag-due-to-lift. 
According to classical wing theory, the induced- drag co efficient of a 
three-dimensional wing with an elliptical lift distribution equals the square 
of the lift coefficient divided by the pro duct of aspect ratio and 7T. 
However, few wings actually have an elliptical lift distribution. Also, this 
doesn't take into account the wing separation drag.


<!-- p.444 -->

444 Aircr af t Des ign: A Conceptual Approach 
The extra drag due to the none lliptical lift distribution and the flow 
sep aration can be accoun ted for using e. This effectively reduces the aspect 
ratio, producing the following equation for K: 
1 K = 1TAe (1 2. 47) 
The Oswald efficiency factor* is typically between 0.7 and 0.85. Numer ous estimation methods for e have been developed over the years, such as 
those by Glauert and Weissinger. These tend to produce resu lts higher 
than the e values of real aircraft. More realistic estimation equations based 
upon actual aircraft [SO] are pres ented here: 
Straight-wing aircraft: 
e = 1.7 8(1 - 0. 045A0·68) - 0.6 4 
Swept-w ing aircraft: 
e = 4.61(1 - 0.0 45A0·68)( cos ALE)0·15 - 3.1 
(where ALE > 30 deg) 
(12 .48) 
(12. 49) 
These equations should only be used with "nor mal" aspect ratios and 
sweeps and are not valid for high-asp ect- ratio designs such as sailplane s. 
For sweeps between 0 and 30, line arly interpolate between results from the 
two equat ions. If the wing has endplates or winglets, the effective aspect 
ratio from Eq. (12 .10) or (12 .11 ) should be used in Eq. (1 2.47) . Note that 
this e method is simplistic, and you should consider using the superior 
"leading- edge suction" method described below. 
Drag due to lift for a biplane was first analytically determined by Max 
Munk in 19 22, based upon the calculation of an equivalent monoplane 
span providing the same wing area and the same drag. Prandtl developed a 
better method using an interference factor (a, shown in Fig. 12 .36), which 
is used in Eq. (1 2.50) to determine a biplane span efficiency factor J1 9l The 
biplane aspect ratio this applies to is the square of the longer span divided 
by the total area of both wings. 
Biplane: 
µ,2(1 + r)2 e=------ µ,2 + 2aµ,r + r2 
where 
µ, = shor ter span/l onger span 
r = lift on shor ter wing/lift on longer wing 
(app roxima tely = area of shorter wing/area of longer wing) 
(12.5 0) 
* Presented in the doctoral dissertation of W.B. Oswald at California Institute of Technology .


<!-- p.445 -->

CH APTE R 12 Aerodyn am ics 445 
1.0 
0.90 
0.80 µ= b sh orte r 
b longer 
0.70 1.0 
b 0.9 
.9 0.60 
u 
<1J 0.50 u 
c 
Q; 0.40 
c 
0.30 
0.20 
0.10 0.4 
0 0 0.10 0.20 0.30 0.40 ( Gap ) 
Average span 
Fig. 12 .36 Prandtl's biplane interference facto r. l1 9J 
For a biplane with wings of equal geometry and lift, Eq. (1 2.50) simplifies 
to [2/(1 + u)]. Typical values for the vertical gap divided by the average span 
are about 0.15; in other words, the span is about seven times the gap. This 
gives an e of about 1.3, greater than one! Remember, though, that the 
aspect ratio is based on the total wing area so that it is about half the 
aspect ratio of the individual wing panels. 
Actually, this Prandtl biplane span efficiency method seems a bit optimistic when compared to actual aircraft data, so it is suggested that the results be 
multiplied by 0.8 before application to Eq. (1 2.47). 
At supersonic speeds, the drag-due-to- lift factor K increases subs tantially. 
In terms of Oswald efficie ncy factor, e is reduced to approximately 0.3-0.5 at 
Mach 1.2. Equation (12 .51) provides a quick estimate of ]( at supersonic 
speeds[Sl] although the leading- edge suction method presented next is 
far preferabl e. 
Supersonic speeds: 
A(M2 - 1) cos ALE 
]( = -----,===--(4A v M2 - 1) - 2 (12 .51)


<!-- p.446 -->

446 Air c raf t Des ign: A Concep tual Approach 
Mf Jf J Lead in g-Edge -Suc tion Method 
Drag at angle of attack is strongly affected by viscous separation. At high lift 
coefficients the drag polar breaks away from the parabolic shape represe nted 
by a fixed value of Ki n Eq. (12 .4). The e method ignores this variation of J( 
with lift coefficient. For a wing with a large leading-edge radius this is acceptable, but for most supersonic aircraft it gives a poor approximation. 
A semi- empirica l method for estimation of K allows for the variation of J( 
with lift coeffici ent and Mach number. This is based upon the conc ept 
of "leading-e dge suction", illustrated in Figure 12.37. The thick airfoil on 
the left is at an angle of attack below that at which subs tantial sepa ration 
occurs. The flow streamlines curve rapid ly to follow the leading- edge 
radius over the top of the wing. 
This rapid curvature creates a pressur e drop on the upper part of the 
leading edge. The reduced pressure exerts a suction force on the leading 
edge in a forward direction. This leading-edge suction force S is shown at 
the bottom of the figure in a direction perpend icular to the normal force N. 
If there is no viscous separation or induced downwash, the leading-ed ge 
suction force exactly balances the rearward component of the normal force 
and the airfoil experiences zero drag. This is the ideal two-dimensi onal case 
described by d'Alembert's paradox and is called "10 0% leadin g-edge suctio n." 
A three- dimensional wing is cons idered to have 100% leading- edge 
suction when the Oswald efficiency factor e exactly equals 1.0. When e 
equals 1.0, the induced- drag constant K exactly equals the inverse of the 
aspect ratio times 7r. 
On the right side of Fig. 12. 37 is a zero- thickness flat-plate airfoil. Even 
without the leading-edge sepa ration, which will almost certainly occur, this 
airfoil must have higher drag because there is no forward-facing area 
for the leading-ed ge pressure forces to act against. All pressure forces for a 
zero-t hickness flat plate must act in a direction perpe ndicular to the plate, 
Leading -edge 
. N 
suction / 
Pre ssur e di stri bution 
No leadings..__v.B=> 0 
v, ;;;;ctl==c 
Res ol ution of forces 
Fig. 12 .37 Leadi ng-edge suction defi niti on.


<!-- p.447 -->

CHAPTE R 12 Aero dyna mi cs 447 
shown as N. There is zero leading-edge suction, and the lift and induced 
drag are simply N times the cosine or sine of the angle of attack 
[Eqs. (1 2.52) and (12 .53 )] . 
or 
but (assuming a is smal l), 
so that 
L = Nc os a 
Di = N sin a = L tan a 
aCr a 1 K= - = - = -Cz Cr er" 
(12.5 2) 
(12.5 3) 
(12 .54) 
(12 .55) 
(12 .56) 
Thus, in the worst case of zero leading- edge suction, the drag- due-to-lift 
factor K is simply the inverse of the slope of the lift curve (in radi ans) . 
All real wings operate some where between 0% and 100% leading- edge 
suction. The per centage of leading- edge suction a wing attains is called S 
(not to be confused with the force S in Fig. 12.37). 
During subsonic cruise, a wing with moderate sweep and a large leadingedge radius will have S equal to about 0.85 to 0.95, i.e., 85- 95% leading- edge 
suction. The wing of a supersonic fighter in a high-g turn might have an S 
approaching zero. 
The calculation of K is done using an estima te of the percent of 
leading-edge suction (S) attainable by the wing. The actual value of K at 
each lift coefficient is interpolated between the K values for 0% and 100% 
suction. This is shown in Eq. (12 .57): 
K = SK100 + (1 - S)Ko (12 .57) 
The 0% K value is the inverse of the slope of the lift curve, as determined 
before. The 100% K value in subsonic flight is the inverse of the aspect ratio 
times 'TT. If using winglets or end plates, the adjusted aspect ratio should be 
used in these calculat ions. 
In transonic flight, starting at Moo, the shock formation interferes 
with leading-edge suction. This increases the K value, increasing drag. 
When the leading edge becomes supersonic, the suction goes to zero, so 
the K value equals the terrible 0% K value. 
This occ urs at the speed at which the Mach angle ( arcsin 1 / M) equals the 
leading-edge sweep. Above that speed the wing has zero leading-edge suction 
so that the K value is always the inverse of the slope of the lift curve.


<!-- p.448 -->

448 Air craft Des ign: A Conceptual Appr oach 
0.3000 
0.2500 
0.2000 
]( 0. 1500 
Actual K va lu es 
lie in this reg ion 
0.10 00 """""----------0.0500 
K100 = l/nA Mach angle matches 
leadin g edge sweep 
/ 
0.0000 -------------------------0.200 0.400 0.600 0.800 1.0 00 1. 200 
Mach nu mber 
Fig. 12 .38 Zero and l 00% K vs Mach numb er. 
1. 400 1. 600 
For initial analysis, the supersonic behavior of the 100% ]( line can be 
approximated by a smoot h curve, as show n in Fig. 12.38. This shows the 
typical behavior of the 10 0 and 0% ](v alues vs Mach number. 
The only unkn own remaining is the value of S, the percen tage of 
leading-edge suction actually attained by the wing at the flight condition in 
question. S depends largely upon the leading-edge radius and is also affected 
by the sweep and other geome tric parameters . 
Si s also a strong function of the wing design lift coefficient and the actual 
lift coefficient at which the aircraft is flying. When we design an aircraft's 
wing, we optimize it based on the missions it is expected to fly. The optimization includes the planform parameters previously discussed (area, aspect 
ratio, taper ratio, and sweep) and also includes the airfoil shape, thickness, 
and wing twist. If the expected missions require a lot of time at high lift coefficients, such as an airplane with extended loiter or flight at extreme altitudes, 
the optimal airfoil will have high camber (Chapter 4). If most of the mission is 
at low lift coeffi cients as for high-speed cruise, then the optimal airfoil will be 
nearly uncambered. 
Later in the design process, soph isticated computer programs will be used 
to define the airfoils (including twist) . This is done to minimize drag at a particular lift coefficient, selected from mission considerat ions. This "design lift 
coefficient" can be selected by a hand calculation of the lift coefficient at the 
middle of a long cruise. Or it can be found by computerized methods wherein 
the design lift coefficient is actuallr a variable in a multi-disciplin ary, multivariable optimization program .l141


<!-- p.449 -->

CH APTE R 12 Aero dynamics 449 
However it is selected, the wing will be designed such that it has the 
maximum value of leading edge suction S when it is oper ating at its own 
design lift coefficient.* 
For most wings, S equals approxi mately 0.9 when operating at the 
wing's own design lift coefficient. At other lift coefficients, the value of S 
will be lower so the drag- due-to- lift will be higher. How much lower Sw ill 
become depends upon many factors. 
For a subsonic wing with large leading-ed ge radius and moder ate sweep, 
the value of Sw ill change very little with lift coefficient until the wing is near 
the stall angle of attack. In other words, S reduces for lift coefficients higher 
than the design value, but is essen tially unchanged for lower values. 
For the thin, swept wings typical in supersonic airc raft, the value of S can 
change subs tantially. This occurs at lift coefficients both higher than and 
lower than the design lift coefficient value. A wing with an S of 0.9 at its 
design lift coefficient of 0.5 can have an S value less than 0.3 at a lift coefficient of 1. 0. 
Proper calculation of S for an actµal wing is complex. An empirical 
approach can be used during con ceptual design. Figure 12 .39 provides a 
1.0 
Design CL 
0.9 
0.8 
0.8 
V) 
...:B 0.7 
u 
- 0.6 
c 0.6 0 
·;:; 
u 
::; 
Vl 
0.5 QJ 
°' 
" 
0.5 QJ 
0.4 °' 
.i:: 
" 
"' 0.3 0.4 QJ _J 
0.2 0.3 
0.1 0.1 
0 0 
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1. 0 
Lift coefficient CL 
Fig. 12 .39 Typical desi gn goal value s for su pers onic ai rcraft . Leadi ng-edge suction vs CL 
*I n some sophisticated optimization methods the entire wing is optimized to directly maximize 
mission performance, rather than first finding a desired design lift coefficient.


<!-- p.450 -->

450 Aircraf t Desig n: A Conceptu al Appr oach 
first-or der estimate of the percent of leading- edge suction for a typical supersonic aircraft's wing, given the actual lift coefficient and the design lift coefficient. (This determines which curve to use.) Note that this chart assumes a 
well-designed wing, and at some later date the aerod ynamics department 
must optimize the twist and camber to attain these values. 
Figure 12.39 estimates the leading-edge suction at various lift coefficients 
for typical, well- designed wings. This allows adding curves to Fig. 12.38 that 
represent the estimated I< value for different lift coefficients as a function of 
Mach number, as in Fig. 12. 40. These are then used for total drag estimation 
via Eq. (1 2.4). 
As mentioned, a subsonic wing with large leading- edge radius will see 
little change in S until near the stall. For such wings the left side of the 
suction curves of Fig. 12.39 should be replaced by a straight line at S 
equals 0.93 (or greater if high aspect ratio; see the following) . This is 
typical for airliners. In fact, the big airliner companies often used a straight 
flat line to the left of a value slightly higher than the design lift coefficien t, 
and a descen ding straight line to the right of it. This crude repres entation 
simplified computer coding, way back when. 
For wings with high aspect ratios, the leading-ed ge suction schedule 
actually becomes a function of aspect ratio, with S increasing to values of 
0.95 -0.97 as higher aspect ratios are employed. The best way to use the 
leadin g-ed ge suction method for such a wing is to use suction test data 
from a similar geom etry wing. If that is not available, a leading-ed ge 
suction schedule can be const ructed by assuming that the Oswald span 
J( 
0.3000 
0.2500 
0.1 500 
Lift coeff. (Cl) 
- i. 4 
--0.35 -0.45 -------". 0.10 00 0.5 ___ ___ _. 
0.0500 
0.0000 ------------------------0.200 0.400 0.600 0.800 1. 000 1. 200 
Mach numb er 
Fig. 12 .40 Sample resul ts-K vs Mach and CL. 
1. 400 1.6 00


<!-- p.451 -->

CHAPTER 12 Aerodyn am ics 451 
efficiency factor (e) at the design lift coefficie nt equals some specified value 
(typically e = 0.8) and solving for the equivalent S in Eq. (12 .58). This S 
can be assumed to apply from zero lift up to about 0.1 CL above the wing 
design CL, after which it drops off to about 80% of the equivalent design S 
at the stall lift coefficient. Although crude, this approximation correlates 
well with actual aircraft data and is more realistic than simpl y using 
Oswald's method with no adjustment for lift coefficient. 
For the sake of comparison, Eqs. (12 .58) and (12. 59) relate S to e and a 
parameter called D..N, used in several other textbooks: 
1 e= --------( 7TA/CLJ (l - S) + S (12 .5 8) 
D..N = s (-1 - _1 ) 
CLa 7TA (12.5 9) 
lfUI Tri m Drag 
The drag values used for performance calculations should include the 
trim drag. This additional drag is caused by the horizon tal tail force required 
to balance (trim) the aircraft so that the total pitching moment about the aircraft e.g. will be zero for any given flight condition. 
The tail usually trims the aircraft with a download that must be countered 
by additional lift from the wing. This produces an increase in the wing 
induced drag that must also be included in the trim drag, along with the 
drag due to lift of the tail itself. However, the tail is flying in the downwash 
off the wing so the directio n of its downward lift is actually slightly 
forward. This reduces the trim drag. 
Trim calculation is discussed in Chapter 16. The trim drag is determined 
using the previous induced- drag methods once the tail lift force required for 
trim is known, taking into account the induced drag from the lift of the tail, 
the extra wing induced drag, and the parasitic drag of the deflected tail and/ 
or elevator. 
If Ill Ground Effect 
When a wing is near the ground, say less than half the span away, the drag 
due to lift J( can be substanti ally reduced. This is theoretica lly explained as 
a reduction in the induced downwash angle, but can be visualized as the 
trapping of a "cushion of air" under the wing. This effect is accounted for 
by multiplying K by the factor calculated in Eq. (1 2.60) [82l : 
J( 33 (h/b) l.5 effective 
J( 1 + 33 (h/b) l.5 
where h is wing height above ground. 
(12.6 0)


<!-- p.452 -->

452 Ai rcr aft Desig n: A Concep tu al Appr oach 
4f Uj Flap Drag 
Flaps affect both the parasitic and induced drag. The flap contribution to 
paras itic drag is caused by the sep arated flow above the flap and is best calculated with a detailed aerod ynamic code that can estimate the amoun t of 
separation and its impact on drag. Flap parasitic drag can be roughly estimated using Eq. (12.61) for most types of flap. This is referenced to wing 
area, not the area of the flap alone. Typically, the flap deflection is about 
60- 70 deg for landing and about 20-4 0 deg for takeoff. Light aircraft 
usually take off with no flaps. 
where 
Oflap = in degrees 
Fflap = 0.014 4 for plain flaps = 0.0074 for slot ted flaps 
Cf = chord length of flap (see Fig. 12.18 ) 
(12. 61) 
The deflection of a flap also affects the induced drag. Additional lift 
occurs in the part of the wing that has the flap (the "flapped" wing area as 
shown in Fig. 12 .2 1). This affects the spanwise lift distribut ion. Induced 
drag is minimized when the wing has an elliptical lift distrib ution. After 
the flaps are deflected, the lift distribution is far from elliptica l so the drag 
due to lift is increased and possi bly doubled. 
Calculation of this effect is best done with a comput er program capable of 
predicting the effect of the flaps on lift distribution and then converting that 
into drag due to lift. For initial analysis it is common in comp any desi gn 
groups to app roximate this effect using wind-tunnel data for a similar configurati on. Methods in [9,l8,69l are also useful. 
As a first approximation, the following equation can be used based on the 
increase in lift due to the flap: 
(12.6 2) 
where k_r = 0.14 for full-span flaps and 0.28 for half-span flaps. This induced 
drag increment is added to the drag due to lift for the total lift using the clean 
wing drag due to lift factor. 
Comp utat ional Fluid Dynami cs 
Mf HI Pre-CFO Indu stry Practi ce 
The aerod ynamic methods presen ted above are used only during early 
con cept ual design studies. Today, most aerod ynamic analysis depends 
upon comp utational fluid dynamic codes (CFD), which are available even 
to homebuilders. Previou sly, maj or aircraft companies relied upon linearized


<!-- p.453 -->

CHAPTER 12 Aerodyn ami cs 453 
computer codes such as the Harris wave-drag code, the Sommer and Short 
skin-friction code, and panel codes such as USSAERO for induced effects. 
More soph isticated panel codes such as PANAIR and QUADPAN were 
used to estimate the induced effects and the wave drag simultaneou sly. 
These linearized computer codes, once available only to major comp anies 
with huge comp uter facilities, can now be run on desktop computers. 
However, they can provide correct results only when the airflow around 
the aircraft is steady, unsep arated, and does not contain any strong vortices. 
This is typically true only during cruising flight. Lift and drag at high angles of 
attack could only be estimated empi rically using correlations to flight-test 
and wind-tunnel data for similar confi gurations. 
The same is true for transonic lift and drag, where some of the very 
terms that are thrown away to linearize the equations are the longitudinal 
velocity-variation terms that produce the transonic shocks. Empi rical data 
were therefore used for the transonic regime. 
Desp ite these problems, the classic indust ry practice of combining linearized comput er codes with empi rical data and corrections produced good 
results in most cases. Actual flight-measured values of lift and drag are 
usually within about 2-10% of the estimat es. Also, the estimates are the 
most accurate for the cruise por tions of the flight where the most fuel is 
burned. 
However, the fact that we can estimate a given design's lift and drag with 
reasonable accuracy does not guarantee that these methods will produce 
the best of all poss ible designs. These methods gave us numerical answers, 
but they did not tell us why the design had problems, or how it could be 
improved. Aerodynamic design had to rely upon a trial-a nd-er ror process 
of design, analyze, test, and redesign. 
Mf UJ CFO Defi ni tions 
It is for these reasons that CFD has rapid ly become a key part of the aircraft design process. CFD is a catch- all phrase for a number of comp utational 
techniques for aerodynamic analysis. It differs from prior aerod ynamic codes 
by solving for the comp lete prop erties of the flowfield around the aircraft, 
rather than only on the surface of the aircraft. 
CFD codes are based upon the Navier- Stokes (NS) equatio ns, which were 
first derived in 18 22. The NS equations comp letely describe the aerod ynamics of a fluid (except for chemical-rea ction effects at high temp erature s). 
NS includes equations based upon the existence of flow continu ity, the conservation of momen tum, and the cons ervation of energy. These are derived in 
many textbooks on theoretical and computational aerod ynamics and will not 
be repeated here. 
The NS equations seem straightfor ward enough but cannot be analytically solved for any useful flow conditions. The author otl22l describes 
them as "some of the nastiest differential equations in theoretical physics."


<!-- p.454 -->

454 Air c raf t Desi gn: A Con ceptu al Appro ach 
The histor y of theoretical aerod ynamics to date can largely be descri bed 
as the quest for solvable simplificat ions of the NS equat ions. The class ical 
lifting-line theor y is one such simplification, as are the linearized wave-drag 
and panel codes, the Euler codes, and the various NS codes. 
There is a complete hierarchy of aerod ynamic codes depending upon 
how many flow phenomena are neglected from the full NS equation s. 
While "direct numerical simulat ion" codes are beginning to solve the full 
NS for simplified geomet rics and conditions, no curre ntly practical codes 
for aircraft design solve the full NS equations because of the difficulty in 
mathematic ally analyzing turbulence. Turbulence occu rs at the molecu lar 
level, which would probably require gridding the flowfield with billions of 
molecule-sized grids. 
The current so- called Navier- Stokes codes actually use a simpli fication 
in the handling of turbulence, which is the most difficult flow phenomen on 
to analyze mathematic ally. Turbulence is handled with some type of separate 
statistically calibrated model apart from the NS solution. 
The most sophisticated codes to date, the large eddy simulation codes 
(LES), use a statistically based turbulence model for small-scale turbulence 
effects. Large eddy codes are capable of direct ly analyzing the larger turbulent 
eddies. The large eddy simulation is now considered the high-end state of the 
art for a com plex aircraft configurat ion. 
The more- affordable state of the art for comple x aircraft configurati ons is 
the Reynolds- averaged Navier- Stokes (RANS ). This has both large and small 
eddies (turbulence) modeled statistica lly. It is assumed the actual turbulence 
levels can be approximated by averaged levels in a grid, which simplifies the 
solution down to "only" solution of about 60 partial derivative equatio ns! 
Reynolds- averaged codes can handle most of the comple x flow pheno mena 
that elude linearized codes, including vortex formation, sep aration, transonic 
effects, and unst eady effects. 
The NS workh orse for supersonic design analysis, the parabolized 
Navier- Stokes (PNS), drops the viscous terms in the streamwise direction. 
This negates streamwise sep aration effects. However, with a good turbulence 
model the PNS codes give correct and illuminating resu lts for many design 
problems. 
If all viscos ity effects are ignored and the flow is assumed to be steady, the 
Euler equations are derived from the NS equat ions. Euler codes are much 
cheaper to run than even PNS codes. The inviscid assumption is quite 
good outside of the boun dary layer so in many cases, an Euler code is 
adequate. The Euler codes can handle vortex formation and with the addition 
of a sep arate bounda ry-layer code can also realistically estimate viscous and 
sepa ration effects. 
The "pot ential flow" equations are further simplified from the Euler 
equations by dropping the rotational terms. This prevents the analysis of 
vortex flow, which is impor tant at high angles of attack but is of lesser importance during cruise conditions. Potential flow codes can handle transoni c
