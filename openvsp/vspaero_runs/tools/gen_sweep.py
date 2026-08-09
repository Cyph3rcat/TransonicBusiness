"""Generates + runs VSPAERO taper/twist parametric variants of the v6 wing (fixed S=193.678 ft^2, b=41.5324 ft, Lambda25=13.8 deg, dihedral=3 deg, SC(2)-0412; varies taper at twist=-3, twist at taper=0.35; chords recomputed to hold S,b: cr=2S/(b(1+lam)), ct=lam*cr). Run from openvsp/vspaero_runs/: python tools/gen_sweep.py"""
import os
import subprocess
import sys

VSPSCRIPT = r"C:\Users\cyphe\Downloads\airplane\OpenVSP-3.51.2-win64-Python3.13\OpenVSP-3.51.2-win64\vspscript.exe"
ROOT = r"C:\Users\cyphe\Downloads\airplane\openvsp\vspaero_runs"
S = 193.678
B = 41.5324
CREF = 5.0236  # keep reference MAC constant across variants for comparability

TEMPLATE = """// AUTO-GENERATED taper/twist variant: {name}
void main()
{{
    string wid = AddGeom( "WING", "" );
    SetGeomName( wid, "MainWing" );
    SetDriverGroup( wid, 1, SPAN_WSECT_DRIVER, ROOTC_WSECT_DRIVER, TIPC_WSECT_DRIVER );
    SetParmVal( wid, "Span", "XSec_1", {semispan} );
    SetParmVal( wid, "Root_Chord", "XSec_1", {cr} );
    SetParmVal( wid, "Tip_Chord", "XSec_1", {ct} );
    SetParmVal( wid, "Sweep", "XSec_1", 13.8 );
    SetParmVal( wid, "Sweep_Location", "XSec_1", 0.25 );
    SetParmVal( wid, "Dihedral", "XSec_1", 3.0 );
    SetParmVal( wid, "Twist", "XSec_1", {twist} );
    SetParmVal( wid, "Twist_Location", "XSec_1", 0.25 );
    SetParmVal( wid, "SectTess_U", "XSec_1", 30 );
    SetParmVal( wid, "Tess_W", "Shape", 41 );
    Update();

    string af_file = "../../../../airfoils/dat_clean/sc20412_selig.dat";
    string xsec_surf = GetXSecSurf( wid, 0 );
    ChangeXSecShape( xsec_surf, 0, XS_FILE_AIRFOIL );
    ChangeXSecShape( xsec_surf, 1, XS_FILE_AIRFOIL );
    ReadFileAirfoil( GetXSec( xsec_surf, 0 ), af_file );
    ReadFileAirfoil( GetXSec( xsec_surf, 1 ), af_file );
    Update();

    Print( "TotalArea: " + GetParmVal( wid, "TotalArea", "WingGeom" ) );
    WriteVSPFile( "{name}.vsp3", SET_ALL );

    string cg = "VSPAEROComputeGeometry";
    SetAnalysisInputDefaults( cg );
    ExecAnalysis( cg );

    string an = "VSPAEROSweep";
    SetAnalysisInputDefaults( an );
    array<double> sref = {{ {S} }};   SetDoubleAnalysisInput( an, "Sref", sref );
    array<double> bref = {{ {B} }};   SetDoubleAnalysisInput( an, "bref", bref );
    array<double> cref = {{ {CREF} }};  SetDoubleAnalysisInput( an, "cref", cref );
    array<double> xcg  = {{ {xcg} }};   SetDoubleAnalysisInput( an, "Xcg", xcg );
    array<double> a0   = {{ 0.0 }};    SetDoubleAnalysisInput( an, "AlphaStart", a0 );
    array<double> a1   = {{ 10.0 }};   SetDoubleAnalysisInput( an, "AlphaEnd", a1 );
    array<int>    na   = {{ 6 }};      SetIntAnalysisInput( an, "AlphaNpts", na );
    array<double> m0   = {{ 0.30 }};   SetDoubleAnalysisInput( an, "MachStart", m0 );
    array<int>    nm   = {{ 1 }};      SetIntAnalysisInput( an, "MachNpts", nm );
    array<double> re   = {{ 8000000.0 }}; SetDoubleAnalysisInput( an, "ReCref", re );
    array<int>    ncpu = {{ 6 }};      SetIntAnalysisInput( an, "NCPU", ncpu );
    array<int>    wni  = {{ 5 }};      SetIntAnalysisInput( an, "WakeNumIter", wni );
    ExecAnalysis( an );
    Print( "DONE {name}" );

    while ( GetNumTotalErrors() > 0 )
    {{
        ErrorObj err = PopLastError();
        Print( err.GetErrorString() );
    }}
}}
"""


def make_variant(name, taper, twist):
    cr = 2 * S / (B * (1 + taper))
    ct = taper * cr
    # x of quarter-MAC for moment ref (LE sweep from Lambda25):
    import math
    lam25 = math.radians(13.8)
    semis = B / 2
    tan_le = math.tan(lam25) + 0.25 * (cr - ct) / semis
    ymac = (B / 6) * (1 + 2 * taper) / (1 + taper)
    mac = (2.0 / 3.0) * cr * (1 + taper + taper**2) / (1 + taper)
    xcg = ymac * tan_le + 0.25 * mac
    d = os.path.join(ROOT, "02_taper_twist", name)
    os.makedirs(d, exist_ok=True)
    script = os.path.join(d, "build_run.vspscript")
    with open(script, "w") as f:
        f.write(TEMPLATE.format(name=name, semispan=semis, cr=round(cr, 4),
                                ct=round(ct, 4), twist=twist, S=S, B=B,
                                CREF=CREF, xcg=round(xcg, 4)))
    return d, script


def run_variant(d, script):
    r = subprocess.run([VSPSCRIPT, "-script", "build_run.vspscript"], cwd=d,
                       capture_output=True, text=True, timeout=600)
    tail = "\n".join(r.stdout.splitlines()[-3:])
    print(f"{os.path.basename(d)}: {tail}")


variants = []
for lam in [0.25, 0.30, 0.35, 0.40, 0.45]:
    variants.append((f"tap{int(lam*100):02d}_tw-3.0", lam, -3.0))
for tw in [0.0, -1.5, -4.5]:
    variants.append((f"tap35_tw{tw:+.1f}", 0.35, tw))

for name, lam, tw in variants:
    d, script = make_variant(name, lam, tw)
    run_variant(d, script)
print("ALL DONE")
