"""Live CFD campaign progress dashboard -- run in a separate terminal:

    python dashboard.py

Polls status.json (written by sweep_runner.py, refreshed every SU2 history
write) and redraws a simple text status pane every second. No dependencies
beyond the standard library, so it runs directly with plain Windows python.
"""
import json
import os
import sys
import time

STATUS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "status.json")

STAGE_NAMES = {
    "stage1_wing_winglet": "Stage 1: wing + winglet",
    "stage2_wing_fuselage": "Stage 2: + fuselage",
    "stage3_wing_fuse_nac": "Stage 3: + nacelle/pylon",
    "stage4_full": "Stage 4: + tail (full aircraft)",
}


def bar(frac, width=30):
    frac = max(0.0, min(1.0, frac))
    n = int(round(frac * width))
    return "[" + "#" * n + "-" * (width - n) + f"] {100*frac:5.1f}%"


def fmt_elapsed(seconds):
    seconds = int(seconds)
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def render(st):
    lines = []
    lines.append("=" * 60)
    lines.append(" SU2 CFD CAMPAIGN -- full_v7 staged buildup")
    lines.append("=" * 60)
    if not st:
        lines.append("(no status.json yet -- sweep_runner.py hasn't started)")
        return "\n".join(lines)

    stage = st.get("stage", "?")
    lines.append(f"Stage:      {STAGE_NAMES.get(stage, stage)}")
    lines.append(f"Solver:     {st.get('solver', '?')}")
    lines.append(f"Status:     {st.get('status', '?')}")

    total_pts = st.get("total_mach_points")
    idx = st.get("mach_point_idx")
    if total_pts and idx is not None:
        lines.append(f"Mach point: {idx + 1}/{total_pts}  "
                      f"(M={st.get('current_mach', '?')})")
        lines.append("  sweep " + bar((idx + (1 if st.get('status')=='done' else 0)) / total_pts))

    it = st.get("iteration")
    cap = st.get("iter_cap")
    if it is not None and cap:
        lines.append(f"Iteration:  {it}/{cap}")
        lines.append("  point  " + bar(it / cap))

    cl, cd = st.get("cl"), st.get("cd")
    if cl is not None:
        lines.append(f"CL={cl}   CD={cd}")

    t0 = st.get("sweep_start_time") or st.get("point_start_time")
    if t0:
        lines.append(f"Elapsed:    {fmt_elapsed(time.time() - t0)}")

    updated = st.get("updated")
    if updated:
        age = time.time() - updated
        stale = "  (STALE -- process may have stopped)" if age > 60 else ""
        lines.append(f"Last update: {age:.0f}s ago{stale}")

    lines.append("=" * 60)
    lines.append("Ctrl+C to stop watching (does not stop the run)")
    return "\n".join(lines)


def main():
    while True:
        st = None
        if os.path.exists(STATUS_PATH):
            try:
                with open(STATUS_PATH) as fh:
                    st = json.load(fh)
            except (json.JSONDecodeError, OSError):
                pass
        os.system("cls" if os.name == "nt" else "clear")
        print(render(st))
        time.sleep(1.0)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
