# Raymer - Front Matter (contents, nomenclature)

*Converted from `Daniel P. Raymer - Aircraft Design_ A Conceptual Approach (2018, American Institute of Aeronautics and Astronautics Inc.) - libgen.li.pdf` by `tools/pdf_to_md.py`. Page markers are printed page numbers.*


<!-- p.1 -->

Aircraft Design: 
A Conceptual Approach 
Sixth Edition


<!-- p.2 -->




<!-- p.3 -->

Sixth Edition 
Daniel P. Raymer 
Conceptual Research Corporation 
Playa <lei Rey, California 
A/AA EDUCATION SERIES 
Joseph A. Schetz, Editor-in-Chief 
Virginia Polytechnic Institute and State University 
Blacksburg, Virginia 
American Institute of Aeronautics and Astronau tics, Inc.


<!-- p.4 -->

The cover shows a far-term tailless transport design developed by Dr. Raymer under 
contract to NASA-GRC. The use of advanced controls technologies permits the elimination of traditional tails, resulting in major savings in weight and drag. This exotic 
concept was designed and analyzed in the RDS-Pr ofessional aircraft design software 
and exported as a 3-D geometry file. The CAD rendering was done from that file by 
Alfredo Ramirez P. of the University of San Buenaventura, Bogota, Colombia, using 
the Blender 3D content creation suite and the YafaRay ray tracing program. Mr. 
Ramirez also created the color ful paint and marking scheme. 
American Inst itute of Aeronautics and Astronautics, Inc., Reston, Virginia 
2 3 4 5 6 7 8 9 10 
Library of Congress Cataloging-in-Publication Data 
Names: Raymer, Daniel P., author. 
Title: Aircraft design: a conce ptual approach/Daniel P. Raymer, Conce ptual 
Research Corpor ation, Playa del Rey, California. 
Desc ription: Reston, VA: American Institute of Aeronautics and Astronautics, 
Inc., [20 18 ] I Series: AIAA education series I Includes bibliographical 
references and index. 
Identifiers: LCCN 201 8033769 I ISBN 978 1624 104909 (hardcover) 
Subj ects: LCSH: Airplanes-Des ign and construction. 
Classification: LCC TL671.2 .R29 20 18 I DDC 629.1 34/ l-dc23 LC record available 
at https://na 01 .sa felinks.pr otect ion.outlook.com /?url=http s%3A%2 F%2Flccn.loc.g ov 
%2F201 803376 9&amp;data=02% 7CO 1%7 Ckatb%40aiaa.org% 7C6 dl3 6c5f53 c34ae3c7 
ad08d5f d503 5f2% 7C036e8 604b67 4406a80987 cb 72daf432b% 7CO% 7CO% 7C636693 44 
3349896 747&amp;sdata=EHvaC mS2wGY8ch%2 BC%2Bd06brGt fNztrjgXtPwvZ9Y 
5L7k %3D&amp;res erved=O 
Copyright © 2018 by Daniel P. Raymer. All rights reserved. Published by the American 
Institute of Aeronautics and Astronautics, with permission. Printed in the United States 
of America. No part of this publication may be reproduced, distributed, or transmitted, 
in any form or by any means, or stored in a database or retrieval system, without the 
prior written permission of the publisher. There are NO authorized electronic downloads so any website offering such is in violation of US and International copyright laws. 
Data and information appearing in this book are for information purposes only. Neither 
AIAA nor the author are responsible for any injury or damage resulting from use of or 
reliance upon the information contained in this book, nor do they warrant that use or 
reliance upon it will be free from privately owned rights.


<!-- p.5 -->

This book is dedicated to all who taught me, espe cially Lester Hen drix, 
Richard Hibma, Louis Hecq, Harry Scot t, Richard Child, Geo rge Owl, 
Robert Maie r, Ed McG achan, Doug Robinson, Steve White, Harvey Hoge, 
Michael Robinson, George Palmer, Henry Yang, Robe rt Swaim, C. T. Sun, 
David Schmidt, Bruce Reese, William Heise r, Tony Hays, Jess Spon able, 
and Gordon Raymer (test pilot, aeronautical engineer, and my father) . 
A spec ial thanks, nearly 30 years after its initial publication, to the 
60,000 + purchas ers of this book and to the hundreds of reade rs who have 
sent letters of appreciation and suggestions for improvements . You too 
have taught me. 
Thanks to Rockwell North American Aircraft Operations, Boeing, SAAB 
Aircraft, Composite Enginee ring, Mr. Alfredo Ramirez P., Mr. Lance Bradshaw, and Lockheed Martin for permission to use vario us illu strations. All 
other artwork is original, in the public domain, or co pyrighted by AIAA. 
Rockwell North American Aviation Advanced Design Department- 1980, 
Harry Scott at left, George Owl at far right. The author's drafting table was two 
rows in front of Harry's. (Photo courtesy of The Boeing Company.)


<!-- p.6 -->




<!-- p.7 -->

A/AA EDUCATION SERIES 
Editor-in-Chief 
Joseph A. Schetz 
Virginia Polytechnic Institute and State University 
Editorial Board 
Joao Luiz F. Azevedo 
Comando -G eral De Tecnologia 
Aeroespacial 
Marty Bradley 
The Boeing Company 
James R. DeBonis 
NASA Glenn Research Center 
Kaja/ K. Gupta 
NASA Dryden Flight 
Research Center 
Rakesh K. Kapania 
Virginia Polytechnic Inst itute and 
State University 
www.aircraftdesign.com 
Brian Landrum 
'University of Alabama, Huntsville 
Michael Mohaghegh 
The Boeing Company 
Conrad F. Newberry 
Naval Postgraduate School; California 
State Polytechnic University, Pomona 
Brett Newman 
Old Dom inion University 
Hanspeter Schaub 
University of Colorado 
David M. Van Wie 
Johns Hopkins University 
www.aiaa.org


<!-- p.8 -->

Author with Paris Airshow display model of his Advanced Supercruise Fighter 
Concept. c2oi (Photo courtesy of Rockwell International North American Aircraft.)


<!-- p.9 -->

FOREWORD 
The American Institute of Aeronautics and Astronautics is deli ghted to 
present another new edition of our bestselling textbook, Aircraft Design: A Conceptual Approach by AIAA Fellow Dr. Daniel P. Raymer. This is the standard textbook and reference throughout the world on the subject of aircraft 
conce ptual desi gn, and prou dly sits in ju st about every desi gn office on the 
planet. Most aeronautical engineers who've graduated in the last 25 years 
have used AD:ACA at some poi nt in their edu cation, and for most the 
book was a "keeper" even when the class was finish ed. 
In this sixth edition Dr. Raymer has expanded and updated his presentation of fast- moving technologies, added lots of new material, and rewritten 
intro ductor y material to make it even more "user-fr iend ly." Given the evergrowing impor tance of electric propulsion, Raymer has added a whole new 
chapter entitled Electric Aircraft. This prese nts technologies, desi gn-t o guidance, and rules of thumb, and offers electric aircraft performance and 
sizing equations der ived in a format familiar to those desi gning conventionally powered airplanes. 
This encyclo pedic book covers every topic necessary to the under standing 
of aircraft design. Prelimina ry sizing, aerod ynamics, structures, stab ility and 
control, propulsion, configuration layout, performance, cost analysis, and 
much more are all presented starting from first principles and building to 
a set of tools allowing the reader to actu ally do a realistic job of aircraft conceptual design. All topics are presented from the poi nt of view of the aircraft 
desi gner, not the specialist in any given topic area. 
After 19 chapters detailing the way to desi gn "nor mal" aircraft, Raymer 
concludes with four more chapters des cribing the desi gn of more exotic 
flight vehicles including elect ric aircraft, helicopters, vertical takeoff jets, 
hypersonic aircraft, launch vehicles, airship s, flying wings, forward- swept 
wings, asymmetric airplanes, and much more. Enjoy! 
Daniel Raymer is uniquely qualifie d to write this book because of his 
broad expertise in the field. He actu ally is an aircraft conc eptual des igner, 
doing blank-sh eet-of -paper designs for over 40 years for large and small aircraft companies. He also teaches aircraft desi gn both in a university setting 
and in his famous design short courses, and is widely published with topics 
ranging from actual desi gn studies, to design and CAD metho dologies, to


<!-- p.10 -->

x A1rcratt 1Jes1gn: A Conceptual Approach 
esoteric optimization metho ds as applied to aircraft design. His command of 
the material is excellent, and he is able to organize and presen t it in a very 
clear manner. 60,000 + purchasers seem to agree ! 
The AIAA Edu cation Series is a premier provider of textb ooks in the field of 
aerospace engineering. The Edu cation Series covers a broad range of related 
topics and includes textbooks of basic theor y, application, and design. Not 
ju st a "print house," the AIAA staff and working-e ngineer volunteers actively 
solicit submissions from world- renowned experts, then work with them to 
produce books which are suitable for both univers ity usage and as archi val 
sources of info rmation for working engineers. A comple te list of titles can 
be found at www.aiaa.org. Suggestions for new topics and new authors are 
always welcome. 
Joseph A. Schetz 
Edi tor-in- Chief 
AIAA Educa tion Series


<!-- p.11 -->

CONTENTS 
Preface xvii 
Author's Note Concerning Use of Metric Weight Units xix 
Nomenclature xxi 
Supponing Materials xxix 
Chapter 1 Design-A Separate Discipline 
1.1 What Is Design? 
1.2 Design: How Does It Start? 
1.3 An Airplane Designer: How Can I Become One? 
1.4 The Book: What Is Here and How It Is Organized 
Chapter 2 Overview of the Design Process 
2.1 Requirements 
2.2 Phases of Aircraft Design 
2.3 Aircraft Conceptual Design Process 
2.4 Integrated Product Development and Aircraft Design 
Chapter 3 Sizing from a Conceptual Sketch 
3.1 Introduction 
3.2 Takeoff-Weight Buildup 
3.3 Empty-Weight Estimation 
3.4 Fuel-Fraction Estimation 
3.5 Takeoff-Weight Calculation 
3.6 Design Example: ASW Aircraft 
Chapter 4 Airfoil and Wing/ Tail Geometry Selection 
4. 1 Introduction 
4.2 Airfoil Selection 
4.3 Wing Geometry 
1 
1 
2 
4 
6 
9 
9 
12 
18 
23 
27 
27 
28 
29 
31 
42 
42 
53 
53 
54 
72 
xi


<!-- p.12 -->

xii Aircraft Design: A Conceptual Approach 
4.4 Biplane Wings 95 
4.5 Tail Geometry and Arrangement 97 
Chapter 5 Thrust-to-Weight Ratio and Wing Loading 115 
5.1 Introduction 115 
5.2 Thrust-to-Weight Ratio 116 
5.3 Wing Loading 123 
5.4 Selection of Thrust to Weight and Wing Loading 142 
Chapter 6 Initial Sizing 145 
6.1 Introduction 145 
6.2 "Rubber" vs "Fixed-Size" Engines 146 
6.3 Rubber-Engine Sizing 147 
6.4 Fixed-Engine Sizing 154 
6.5 Geometry Sizing 156 
6.6 Control-Surface Sizing 161 
Chapter 7 Configuration Layout and Loft 165 
7.1 Introduction 165 
7.2 End Products of Configuration Layout 167 
7.3 Conic Lofting 175 
7.4 Conic Fuselage Development 179 
7.5 Flat-Wrap Fuselage Lofting 185 
7.6 Circle-to-Square Adapter 188 
7.7 Loft Verification via Buttock-Plane Cuts 189 
7.8 Wing/Tail Layout and Loft 191 
7.9 Wetted-Area Determination 204 
7.10 Volume Determination 206 
7.11 Use of Computer-Aided Design (CAD) 
in Conceptual Design 207 
Chapter B Special Considerations in Configuration Layout 213 
8.1 Introduction 213 
8.2 Aerodynamic Considerations 214 
8.3 Structural Considerations 223 
8.4 Radar Detectability 233 
8.5 Infrared Detectability 243 
8.6 Visual Detectability 244 
8.7 Aural Signature 245 
8.8 Vulnerability Considerations 247 
8.9 Crashworthiness Considerations 249 
8.10 Producibility Considerations 250 
8.11 Maintainability Considerations 257


<!-- p.13 -->

CONTENTS xiii 
Chapter 9 Crew Station, Passengers, and Payload 261 
9.1 Introduction 261 
9.2 Crew Station 262 
9.3 Passenger Compartment 266 
9.4 Cargo Provisions 267 
9.5 Weapons Carriage 269 
9.6 Gun Installation 273 
Chapter 10 Propulsion and Fuel System Integration 275 
10.1 Introduction 275 
10.2 Propulsion Overview and Selection 276 
10.3 Jet-Engine Integration 281 
10.4 Propeller-Engine Integration 311 
10.5 Fuel System 323 
10.6 Green Propulsion 329 
Chapter 11 Landing Gear and Subsystems 337 
11.1 Introduction 337 
11.2 Landing-Gear Arrangements 338 
11.3 Tire Sizing 343 
11.4 Shock Absorbers 351 
11.5 Castoring-Wheel Geometry 359 
11.6 Gear Retraction Geometry 360 
11.7 Seaplanes 364 
11.8 Subsystems 366 
Intermission Step-by-Step Development of a New Design 379 
Chapter 12 Aerodynamics 389 
12.1 Introduction 389 
12.2 Aerodynamic Forces 390 
12.3 Aerodynamic Coefficients 396 
12.4 Lift 397 
12.5 Parasite (Zero-Lift) Drag 416 
12.6 Drag Due to Lift (Including Induced Drag) 442 
12.7 Computational Fluid Dynamics 452 
Chapter 13 Propulsion 463 
13.1 Aircraft Thrust-The Big Picture 463 
13.2 Jet-Engine Thrust Considerations 466 
13.3 Jet-Engine Installed Thrust 469 
13.4 Part Power Operation 479 
13.5 Piston-Engine Overview 480


<!-- p.14 -->

xiv Aircraft Design: A Conceptual Approach 
13.6 Propeller Analysis 481 
13.7 Piston-Prop Thrust Corrections 486 
13.8 Turboprop Performance 488 
Chapter 14 Structures and Loads 491 
14.1 Introduction 491 
14.2 Loads Categories 492 
14.3 Air Loads 494 
14.4 Inertial Loads 505 
14.5 Powerplant Loads 506 
14.6 Landing-Gear Loads 506 
14.7 Structures Fundamentals 507 
14.8 Material Selection 513 
14.9 Material Properties 517 
14.10 Structural-Analysis Fundamentals 527 
14.11 Finite Element Structural Analysis 551 
Chapter 15 Weights 559 
15.1 Introduction 559 
15.2 Approximate Weight Methods 567 
15.3 Aircraft Statistical Weights Method 569 
15.4 Additional Considerations in Weights Estimation 579 
Chapter 16 Stability, Control, and Handling Qualities 585 
16.1 Introduction 585 
16.2 Coordinate Systems and Definitions 587 
16.3 Longitudinal Static Stability and Control 589 
16.4 Lateral-Directional Static Stability and Control 611 
16.5 Stick-Free Stability 620 
16.6 Effects of Flexibility 620 
16.7 Dynamic Stability 622 
16.8 Quasi Steady State 627 
16.9 Inertia Coupling 629 
16.10 Handling Qualities 630 
Chapter 17 Performance and Flight Mechanics 637 
17.1 Introduction and Equations of Motion 637 
17.2 Steady Level Flight 639 
17.3 Steady Climbing and Descending Flight 649 
17.4 Level Turning Flight 653 
17.5 Gliding Flight 657 
17.6 Energy-Maneuverability Methods 661 
17.7 Operating Envelope 669


<!-- p.15 -->

CON TE NTS xv 
17.8 Takeoff Analysis 671 
17.9 Landing Analysis 676 
17.10 Other Fighter Performance Measures of Merit 679 
Chapter 18 Cost Analysis 687 
18.1 Introduction 687 
18.2 Elements of Life-Cycle Cost 689 
18.3 Cost-Estimating Methods 691 
18.4 RDT&E and Production Costs 692 
18.5 Operations and Maintenance Costs 699 
18.6 Cost Measures of Merit (Military) 703 
18.7 Aircraft and Airline Economics 704 
Chapter 19 Sizing and Trade Studies 709 
19.1 Introduction 709 
19.2 Detailed Sizing Methods 710 
19.3 Improved Conceptual Sizing Methods 711 
19.4 Classic Optimization-Sizing Matrix and Carpet Plots 717 
19.5 Trade Studies 724 
Chapter 20 Electric Aircraft 735 
20.1 Introduction 735 
20.2 Review of Physics & Units 738 
20.3 Why Spark? 739 
20.4 Electric Motor Basics 742 
20.5 Power Supply: Batteries 745 
20.6 Power Supply: Fuel Cells 749 
20.7 Power Supply: Hybrid-Electric 750 
20.8 Power Supply: Solar Cells 753 
20.9 Power Supply: Beamed Power 754 
20.10 Electric Aircraft Run-Time, Range, Loiter, and Climb 755 
20.11 Electric Aircraft Initial Sizing 757 
Chapter 21 Vertical Flight-Jet and Prop 763 
21.1 Introduction 763 
21.2 Jet VTOL 764 
21.3 Prop VTOL and Helicopter 783 
Chapter 22 Extremes of Flight 805 
22.1 Introduction 805 
22.2 Rockets, Launch Vehicles, and Spacecraft 806 
22.3 Hypersonic Vehicles 819 
22.4 Lighter Than Air 823


<!-- p.16 -->

xvi Aircraft Design: A Conceptual Approach 
Chapter 23 Design of Unique Aircraft Concepts 833 
23. 1 Introduction 833 
23.2 Flying Wing, Lifting Fuselage, and Blended Wing Body 834 
23.3 Delta and Double-Delta Wing 839 
23.4 Forward-Swept Wing 841 
23.5 Canard-Pusher 843 
23.6 Multi-fuselage 845 
23.7 Asymmetric Airplanes 847 
23.8 Joined Wing 851 
23.9 Some More Innovative Wings 852 
23.10 Wing-in-Ground-Effect 859 
23.11 Unmanned/Uninhabited Aircraft 860 
23. 12 Derivative Aircraft Design 863 
Chapter 24 Conceptual Design Examples 
24.1 Introduction 
24.2 Single-Seat Aerobatic Homebuilt 
24.3 Lightweight Supercruise Fighter 
Appendix A Unit Conversion 
Appendix B Standard Atmosphere 
Appendix c Airspeed 
Appendix D Airfoil Data 
Appendix E Typical Engine Performance Curves 
867 
867 
868 
905 
959 
963 
969 
971 
987 
E. 1 Afterburning Turbofan 987 
E.2 High-Bypass Turbofan 991 
E.3 Turboprop 993 
Appendix F Design Requirements and Specifications 995 
Questions 999 
References 7 009 
Index 1017


<!-- p.17 -->

PREFACE 
Aircraft Desi gn is a challenging, rewarding, and fun career. There are 
dozens of different activities involved in creating a new air vehicle conce pt, 
different speci alties ranging from initial configura tion layout to system optimization and cost estimat ion. These activities can be grouped into two equally 
important aspe cts of aircraft design: design layout and design analysis. While 
some people do both, in most cases these differing aspects attract different 
types of people. Certain people love playing with numbers and comput ers, 
whereas others can't stop doo dling on every piece of paper within reach. 
This book offers a balanced overview of these two aspects of desi gn, integrated together and presented in the manner typically seen in an aircraft 
design proj ect at a major aero space compan y. Whiche ver aspect you may 
lean towards, the book should help get you started and will provide a resource 
of material throughout your career. 
Aircraft design depends on the reliable calculation of numb ers but in the 
end, the only thing that actu ally gets built is the configuration concept shown 
on the drawing or CAD file. Its creat ion is not a trivial task of drafting based 
upon the analysis results, but rather it is a key element of the overall design 
process and ultima tely determines the performance, weight, and cost of the 
aircraft. Blunt ly stated, if you don't have a good drawing, you don't have an 
aircraft design. The "Co nceptual Approach" mentio ned in the book's title 
refers to a design process centered around a realistic concept layout. 
It is difficult to visualize and draw a new aircraft that has a streamlined 
aerodynamic shape and an efficient internal layout and yet satisfies an incre dible number of real-world const raints and desi gn spe cifica tions. Aircraft conceptual desi gn layout is a rare talent that takes years to cultivate. Although to 
some extent good des igners are "born, not made," the proven methods and 
best practices of aircraft configura tion layout can be taught and are 
covered here in the first half of this book. These apply equ ally to traditional 
drafting table drawings and to mode rn computer- aided design. 
It is also true that a nice aircraft drawing is nothing without the analytical 
results to supp ort it, and it will be a much better design if clever optimization 
metho ds are employ ed. So, a good desi gner or design team must find an 
appropriate balance between design layout and desi gn analysis. The second 
half of this book covers analysis and optimization metho ds that will tell 
xvii


<!-- p.18 -->

xviii Aircraft Design: A Conceptual Approach 
you if the design works, if it meets its design requirements, and how you can 
make it better in the next drawing. 
Writing-and rewriting-this book has been an educa ting and humbling 
experience. It is my sincere wish that it helps aspi ring aircraft des igners to 
"lea rn the ropes" more quic kly. My greatest pride in the previous editions 
has been the thanks from the studen ts who've used the book in their 
design classes, and the desi gners of buil t-and- flown airplanes who've told 
me that they made extensive use of my book. Thanks-t hat means a lot. 
Daniel P. Raymer 
Los Angeles, California 
June 20 18 
The author's Aircraft Conceptual Design Web site at www.aircraftdesig n.com 
includes examination questions for the book, advice to students and wouldbe inventors, sample aircraft design layouts, free design software, tips for the 
use of the companion RDS-Student desi gn software, and information on aircraft 
design shor t courses. It is free, and all are welcome! 
Raymer's Reverse Installation Vectored Engine Thrust ("RIVET") supersonic 
VSTOL concept. r130J


<!-- p.19 -->

AUTHOR'S NOTE CONCERNING USE OF 
METRIC WEIGHT UNITS 
Metric units (SI or mks) are more universal and technica lly consis tent 
than British Imperial units (fps) and also reduce the possi bility of stupid 
errors in aircraft calculat ions. However, one must still decide exactly which 
metric unit multipliers to use. Should masses be defined in grams or in kilograms ? Should time be in seconds or in hours, or used as needed to make the 
numbers "nice"? These decisions change the numbers, and, unfortunate ly, 
different organizations use slightly different combinations of unit multipliers 
and times. To maximize cons istency with prior literature, the metric unit 
terms used in Jane's All the World's Aircraft[6] and in Stinton's The Design of the Aeroplane [47l were employed in this book. Values in this book are presented first in British units, and then in metric units enclosed in braces {}. 
A key issue and the source of much confusion is the treatment of "weight" 
in metric units. Weight by definit ion is a force, not a mass. However, 
pilots and working engineers describing the weight of the Airbus A340 
would say 126,000 kg, not 1,235,682 kN. What those pilots and engineers 
really mean is, "the Airbus exerts a weight force equival ent to that exerted 
by a 12 6,000 kg mass in a 1-g gravitational field." This book follows this 
common practice -don't let it confuse you! When doing an analysis such 
as calculating lift force and equating it to weight, the "weight" of 
126,000 kg (actually mass) must first be converted to proper force units 
(Newtons) by multiplying by the 1-g acceleration constant (g = 9.807 m/s 2). 
This verbal equating of weight with force in a 1-g gravitati onal field is 
carried over to the definitions of ratios such as wing loading (kg/ m2) and 
power loading (kg/k W). Because of this, the values of these ratios as given 
in the tables are not technica lly correct when applied to the various equations 
that use them. The mass terms must be converted to force by multipl ying by 
g. Thus, a wing loading given in "pilot talk" as 586 kg/m 2 must be converted 
to 5,7 46.9 N/m2 to apply in equations relating lift to weight (for example, see 
Table 5.5). 
The values given for thrust- to-w eight ratio (T/W) do not require conversion. In traditional (fps) practice the thrust is given in lbs-for ce, and the 
weight is given in lbs- mass (exerted force assuming a 1-g field) , so that the 
xix


<!-- p.20 -->

xx Aircraft Design: A Conceptual Approach 
ratio is nondimensi onal and the same as the desired SI units of Newtons/ 
Newton. A T / W greater than one means the aircraft can acce lerate straight 
up, regardless of the units in which it was designed! 
X-15 rollout (U.S. Air Force photo). 
Learjet (USAF C21-A) (U.S. Air Force photo).


<!-- p.21 -->

NOMENCLATURE 
Coefficients, parameters, and Greek letters commo nly used in aircraft 
design are listed below, followed by various abbre viations and acron yms. 
For updates and more definitions, see www.aircraftdesign .com/ abrv.html . 
The terms speci fic to the statistical weights equations presen ted in Chapter 
15 are listed in that chapter and are not repeated here. 
Aircraft Design Coefficients and Parameters 
A 
A 
Ac 
Awetted 
A* 
b 
EMF 
c 
c 
c 
cbleed 
CD 
CDi 
Co min 
Cowave 
CDo 
Cd 
Cf 
cfe 
CHT 
CL 
Ct 
Ct 
cfo 
C1a 
aspect ratio of wing (=b2 /Sref) 
helicopter rotor disk area 
capture area of jet engine inlet duct 
wetted aspect ratio ( = b2 I Stotal wetted area) 
cross-s ection area if that flow stream was at Mach 1 
wing span 
Battery Mass Fraction 
chord length 
speci fic fuel consu mption (also SFC) 
exhaust veloc ity (rockets) 
bleed coefficient (adjusts thrust for amount of bleed air) 
wing or whole airplane drag coefficient 
induced- drag coefficient 
minimum drag coefficient (=CDo if uncambered) 
supersonic wave-drag coe fficient (also CDw) 
drag coe fficient at zero lift 
airfoil drag coefficient 
flat-p late skin- friction coefficient 
equivalent skin-fr iction coefficient 
horizo ntal tail volume coefficient 
wing or whole airplane lift coefficient 
airfoil lift coefficient 
rolling-moment coefficient 
wing or whole airplane slope of the lift curve 
airfoil slope of the lift curve ( =27T theoretica lly) 
xxi


<!-- p.22 -->

xxii Aircraft Design: A Conceptual Approach 
Ctf3 
Cm 
Cm 
Cma 
Cn 
Cnf3 
Cram 
CvT 
E 
EHA 
Esh 
Ewd 
e 
FAA 
FAI 
FF 
ls 
g 
J 
/( 
L/D 
LE 
M 
m 
MAC 
mb 
Mer 
Moo 
n 
Ps 
Fused 
Q 
Q 
rolli ng moment with sideslip angle (dihe dral effect) 
airfoil pitching-mo ment coefficient 
wing or whole airpla ne pitchi ng-mo ment coefficient 
pitching-mome nt derivative with angle of attack 
yawing-mo ment coefficient 
yawing-moment derivative with sideslip angle 
ram coefficient (adj usts thrust for inlet pressur e recovery) 
vertical tail volume coefficie nt 
Young's modµlus, or modulus of elasticit y 
Elect rohydrostatic Actuator 
battery speci fic energy {wh/kg} 
wave-drag efficiency factor [ = Cowave/ Cowave(Sears-Haack)l 
Oswald's span effici ency factor (adjusts aspect ratio) 
Federal Aviation Administration 
Federation Aeronautique International (aviation record 
certifying agen cy) 
form factor term (pressure drag) for parasitic drag 
calculation 
fuel specific energy (P5/fuel flow) 
accele ration due to gravity, standard values: 32. 174 ft/s 2 or 
9. 80665 m/s 2 
shear modulus, or modulus of rigidi ty 
energy height (actual height plus height equivalent of kinetic 
energy) 
specific impulse (rock et propella nt cons umption) 
rolling mass moment of inertia 
pitching mass mome nt of inertia 
yawing mass moment of inertia 
incidence angle 
propeller advance ratio ( = V / nD) 
drag due to lift factor 
lift-t o-d rag ratio 
leading edge (of airfoil or wing) 
Mach number (multiple of speed of sound) 
total aircraft mass {kg} 
mean aero dynamic chord 
mass of batteries {kg} 
critical Mach number (where shocks first form) 
drag- divergent Mach number (where drag increases) 
load factor 
speci fic excess power 
average motor power used {kW} 
interference factor for pa rasitic drag calculation 
produc tion quantity


<!-- p.23 -->

q 
q 
R# 
RAND 
Rcutoff 
s 
Sexposed 
SFC 
T/W 
t 
t/c 
TE 
Ude 
Ve 
Vi 
Vi 
Wdg 
We 
Wr 
Wo 
W/S 
dynamic pressure (of air) 
dynamic pressure, = ! p V2 
Reynolds number (also R or R no.) 
Nomenclature xxiii 
RAND Corp. -Resea rch ANd Development (think-tank for 
USAF) 
Cutoff Reynolds number, adjusts skin friction for roughness 
leading-edge suction (force or percent attainment) 
exposed wing planform (wing less portion of wing covered 
by fuselage) 
speci fic fuel cons umption (also C) 
thrust-to -weight ratio 
airfoil thick ness 
airfoil thickne ss-to- chord length ratio 
trailing edge (of airfoil or wing) 
derived equivalent gust velocities (used for gust load 
calculation) 
equivalent airspeed (dynamic pressure based, Ve= Vactual 
sqrt[p/ PoD 
never- exceed speed 
maneu ver (pullup) speed (max. speed for full controls 
deflections) 
takeoff decision speed 
takeoff safety speed 
flight design gross weight 
empty weight 
fuel weight 
takeoff gross weight 
wing loading 
Aerospace Applications of Greek Letters 
a (alpha) 
f3 (beta) 
f3 (beta) 
8 (delta) 
8 (delta) 
Li (Delta) 
e (epsilon) 
y (gamma) 
y (gamma) 
f (Gamma) 
YJ (eta) 
Y/b2s 
Y/p (eta-p) 
angle of attack 
sideslip angle 
Prandt l-G lauert compressi bility cor rection 
change in some parameter 
deflection of controls 
wing sweep (see also A) 
unit strain 
shearing strain 
flight-p ath angle 
wing dihedral angle 
efficiency 
total system efficiency from battery to motor output shaft 
propeller efficiency


<!-- p.24 -->

xxiv Aircraft Design: A Conceptual Approach 
Y/p (eta-p) 
A (lambda) 
A (Lambda) 
µ, (mu) 
µ, (mu) 
7r (pi) 
II (Pi) 
p (rho) 
p (rho) 
p (rho) 
o- (sigma) 
o- (sigma) 
-(Sigma) 
T (tau) 
propulsi ve efficiency (rockets) 
wing taper ratio ( Ctip/ Croot) 
wing sweep (see also Ll) 
visco sity 
micro (one millionth = 1/10 6) 
3.141 592653589793 ... 
product operator 
air dens ity 
conic shape parameter 
radius of gyration 
unit stress 
air dens ity ratio (= p/ Po) 
summat ion oper ator 
unit shear stress 
Abbreviations and Acronyms 
AAW 
ABC 
A/C 
AC 
AF 
AFRL 
AMAD 
AMPR 
AMRAAM 
AOA 
APU 
ASW 
ATC 
ATF 
AWACS 
BFL 
BINGO 
BL 
BMI 
BPR 
CAD 
CAIV 
CAM 
CAS 
CCC 
CER 
CFD 
active aeroelastic wing 
activity- based cost ing 
aircraft 
Alternating Current 
Air Force 
Air Force Rese arch Lab 
airframe mounted accessor y drive 
airframe manufacturers planning report 
advanced medium-r ange air-to- air missile (now AIM- 12 0) 
angle of attack 
auxiliary power unit 
antisubmarine warfare 
air traffic control 
Advanced Tac tical Fighter (F-22 predecessor program) 
airborne warning and control system 
balanced field leng th 
fuel state at which a pilot must begin to return to base 
bounda ry layer 
bismaleimide (high-temp compo site material) 
turbofan engine bypass ratio 
computer-aided desi gn 
cost as an independ ent variable 
computer-aided manufacturing 
calibrated airspeed 
command, control, and communica tions ("C-cubed") 
cost-est imating relationship 
computational fluid dynamics


<!-- p.25 -->

e.g. 
COT S 
cs 
CTOL 
CV 
CVN 
DAPCA 
DARPA 
DATCOM 
DC 
DCPR 
Decalage 
DOC 
DoD 
DOF 
Drag Counts 
EAS 
ECCM 
ECM 
ECS 
EHP 
EASA 
ESHP 
EW 
F/A 
FAA 
FAR 
FAR 
FB 
FBW 
FEM 
FUR 
FOD 
FSW 
FY 
GA 
GA 
G&A 
Gap 
G&C 
GLOW 
GPS 
HALE 
center of gravity 
Nomenclature xxv 
commercial off-the-shelf (no development required) 
EASA Certificati on Speci fications (like FARs) 
conventional takeoff and landing 
aircraft carrier, heavie r-than- air aircraft 
aircraft carrier, heavier-than- air, nuclear powered 
development and procurement cost of aircraft (cost model) 
Defense Advanced Research Proj ects Agency 
Data Compendium (USAF aerod ynamics methodolog y 
repor t) 
Direct Current 
defense contractors planning report 
incidence angle between two wings of a biplane 
direct operating costs 
Dep artment of Defense 
degree of freedom (6-DOF = X, Y, Z, roll, pitch, yaw) 
four digits to right of decimal place in coefficient 
equivalent air speed 
electronic counter-co untermeasures 
electronic coun termeasures 
environmental control system 
equivalent horsepo wer 
European A via ti on Safety Agency (like FAA) 
equival ent shaft hors epower (includes residual thrust) 
electronic warfare 
fighter/ attack 
Federal Aviation Administ ration 
Federal A via ti on Regulations (certific ation specs) 
Federal Acquisition Regulations 
fighter-bomber 
fly by wire 
finite element method (for calculation, usually of structures) 
forward-look ing infrared 
foreign object damage 
forward-swept wings 
fiscal year 
general aviation 
genetic algorithm (optimization method) 
general and adminis trative (overhead expenses) 
vertical distance between two wings of a biplane 
guidance and control 
gross liftoff weight (Wo for rockets) 
global positioning system 
high- altitude long endurance


<!-- p.26 -->

xxvi Aircraft Design: A Conceptual Approach 
Helo 
HGI 
hp 
HUD 
IAS 
!CAO 
IFR 
IFR 
ILS 
INS 
roe 
IPPD 
IPT 
IR 
ISO 
JAR 
JATO 
JDAM 
JP 
JSF 
KISS 
LCC 
LOX 
L&P 
LTA 
MECO 
MDO 
MMH/FH 
MSL 
MTOW 
MZFW 
NASA 
NASTRAN 
NAV 
NC 
NOT AR 
NPV 
NS 
NURBS 
O&S 
OEM 
OEI 
p-Effect 
helicopter 
hot- gas ingestion 
horsep ower ( = 550 ft-lb/s = 746 W) 
head-up displa y 
indic ated airspeed 
International Civil Aviation Organization 
instrument flight rules 
in- flight refueling 
instrument landing system 
inertial navigation system 
indirect operating costs 
integrated product and process development 
integrated product team 
infrared 
International Standards Organization 
jo int aviation requirements (European cert. specs) 
jet-a ssisted takeoff 
jo int direct attack munition 
jet propellant (kerosene-based fuel) 
Joint Strike Fighter (pro ject leading to F-35) 
keep it simple, stupid (attributed to Ed Heinemann) 
life-c ycle cost (total cost from product development to 
retirement) 
liquid oxygen 
leakage and protuberances (causing additional drag) 
lighter than air (airship) 
main engine cutoff (shu tdown) 
multi disciplin ary design optimization 
mainte nance man-hours per flight hour 
mean sea level 
maximum takeoff weight 
maximum zero fuel weight 
National Aero nautics and Space Admini stration 
NASA Structural Analysis (FEM software) 
navigation 
numeric ally controlled 
no tail rotor (helicopter) 
net present value 
Navier-Stokes (high-end CFD) 
nonu niform rational B- Spline (cur ve equat ion for CAD) 
operations and suppor t 
original equipment manufacturer 
one engine inope rative 
yawing moment due to propeller


<!-- p.27 -->

PPP! 
pre-preg 
QFD 
RCS 
RCS 
RDS 
RDT&E 
RFI 
RFP 
RFQ 
Reece 
Rec on 
RPM 
RP 
RPV 
SAM 
SAR 
S&C 
SHM 
SL 
SOP 
SST 
Stagger 
STOL 
STOVL 
T&E 
TAS 
TRL 
TOGW 
TPS 
TQM 
TVC 
UAV 
UCAV 
VFR 
VIFF 
V/STOL 
VTO 
VTOL 
WBS 
WIG 
ZFW 
Nomenclature xxvii 
preplanned product improvement (P3I or P-cubed I) 
pre- impregnated (composi te materials) 
quality function deplo yment 
radar cross section 
reaction control system (small thrusters for co ntrol) 
Raymer's design system (aircraft design software) 
resear ch, dev elop ment, test, and evaluation (costs) 
request for information (usua lly unpaid) 
request for proposa ls 
request for quotations 
reconnaissance 
reconnaissance 
revolutions per minute 
rocket propellant (kerosene-based fuel) 
remote-pi loted vehicle 
surfac e-to-a ir missile 
synthetic aperture radar 
stability and control 
structural health monitoring 
sea level 
standard oper ating proce dure 
supersonic transport 
long itudinal offset of two wings of a biplane 
short takeoff and landing 
short takeoff/vertical landing 
test and evaluation 
true airspeed 
technol ogy readiness level 
takeoff gross weight 
thermal protection system (for reentry) 
total quality management 
thrust vector control 
unmanned or uninhabited aerial (or air) vehicle 
unmanned or uninhabited combat air vehicle 
visual flight rules 
vectoring in forward flight 
vertical/ short takeoff and landing 
vertical takeoff 
vertical takeoff and landing 
work breakd own structure 
wing-in-g round effect 
zero fuel weight


<!-- p.28 -->

xxvi ii Aircraft Design: A Conceptual Approach 
Daniel P. Raymer at the North American Aviation Trisonic Wind Tunnel, holding a 
supersonic model of his Advanced Tactical Fighter design.


<!-- p.29 -->

SUPPORTING MATERIALS 
To download supple mental material files, please go to AIAA's elec tronic 
library, Aerospace Resea rch Central (ARC) , at arc.aiaa.org. Use the menu bar 
at the top to navigate to Books > AIAA Educa tion Series; then, navigate to 
the desired book's landing page by clicking on its title. On the landing 
page, click the link benea th "Supp lemen tal Materials," enter the pass word 
ADACA6E, and follow the directions provided. 
A com plete listing of titles in the AIAA Educa tion Series is available from 
AIAA's electronic libr ary, Aerospace Research Central (ARC), at arc. aiaa.or g. 
Visit ARC freque ntly to stay abreast of product changes, cor rections, speci al 
offers, and new publicat ions. 
AIAA is committed to devoting resources to the educa tion of bot h 
practicing and future aerospace professionals. In 19 96, the AIAA Foundation was founded. Its programs enhance scie ntific literac y and advance 
the arts and sciences of aerospace. For more information, please visit 
www.aiaafoun datio n.org.


<!-- p.30 -->

xxx Aircraft Design: A Conce ptua l Appr oach
