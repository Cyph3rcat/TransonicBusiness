"""
Live terminal dashboard for the SC(2)-0412 v2 adaptive Mach sweep.

Polls whichever log_sc20412_v2_M*.txt was most recently written (i.e. the
currently-running point), parses the same iteration-row format
adaptive_sweep_v2.py itself parses, and redraws a single-screen status view:
which Mach point we're on (i/7), an iteration progress bar against the
ITER=4500 cap, live rms_rho/CL/CD, and an ETA estimated from the observed
iterations/sec of the current run.

Pure stdlib -- no pip installs needed, safe to run with the system python3
inside WSL (the venv with gmsh/meshio is NOT needed for this).

Run (inside WSL, from the working directory):
    python3 monitor_sweep.py
Or from Windows, without opening a WSL shell yourself:
    wsl -d Ubuntu -e bash -lc "cd /home/cyph3r/mses_replacement/mach_sweep_v2 && python3 monitor_sweep.py"
"""
import re
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent if "__file__" in dir() else Path(".")
ITER_CAP = 4500
MACH_POINTS = [0.5922, 0.6222, 0.6522, 0.6822, 0.7122, 0.7422, 0.7722]  # up to 7, adaptive-stop may end early
POLL_SECS = 3

ROW_RE = re.compile(r"^\|\s*(\d+)\|\s*(-?[\d.]+)\|\s*(-?[\d.]+)\|\s*(-?[\d.]+)\|\s*(-?[\d.]+)\|\s*$", re.MULTILINE)
TAG_RE = re.compile(r"log_sc20412_v2_M(\d+p\d+)\.txt$")


def latest_log() -> Path | None:
    logs = sorted(HERE.glob("log_sc20412_v2_M*.txt"), key=lambda p: p.stat().st_mtime)
    return logs[-1] if logs else None


def parse_progress(log_path: Path):
    text = log_path.read_text(errors="ignore")
    rows = ROW_RE.findall(text)
    if not rows:
        return None
    it, rms_rho, rms_e, cl, cd = rows[-1]
    return {"iter": int(it), "rms_rho": float(rms_rho), "cl": float(cl), "cd": float(cd),
            "n_rows": len(rows)}


def bar(frac: float, width: int = 30) -> str:
    filled = int(max(0.0, min(1.0, frac)) * width)
    return "[" + "#" * filled + "-" * (width - filled) + "]"


def main():
    completed_logs = sorted(HERE.glob("log_sc20412_v2_M*.txt"))
    start_time = time.time()
    last_iter_by_log = {}
    rate_ema = None  # iters/sec, exponential moving average

    print("Watching for SC(2)-0412 v2 sweep progress... (Ctrl+C to stop watching; the SU2 run keeps going)\n")

    while True:
        log_path = latest_log()
        if log_path is None:
            sys.stdout.write("\rNo log file yet -- waiting for first point to start...")
            sys.stdout.flush()
            time.sleep(POLL_SECS)
            continue

        all_logs = sorted(HERE.glob("log_sc20412_v2_M*.txt"))
        point_idx = len(all_logs)  # 1-based index of the currently-active/most-recent point

        prog = parse_progress(log_path)
        results_done = HERE / "adaptive_sweep_results_v2.json"

        now = time.time()
        if prog:
            prev = last_iter_by_log.get(log_path)
            if prev is not None:
                d_iter = prog["iter"] - prev[0]
                d_t = now - prev[1]
                if d_t > 0 and d_iter >= 0:
                    inst_rate = d_iter / d_t
                    rate_ema = inst_rate if rate_ema is None else 0.3 * inst_rate + 0.7 * rate_ema
            last_iter_by_log[log_path] = (prog["iter"], now)

            frac = prog["iter"] / ITER_CAP
            eta_str = "..."
            if rate_ema and rate_ema > 0:
                remaining = max(0, ITER_CAP - prog["iter"])
                eta_s = remaining / rate_ema
                eta_str = f"{eta_s / 60:.1f} min (this point)"

            line = (
                f"\rPoint {point_idx}/7  M={MACH_POINTS[point_idx - 1] if point_idx <= 7 else '?'}  "
                f"{bar(frac)} {prog['iter']:>5}/{ITER_CAP}  "
                f"rms_rho={prog['rms_rho']:+.3f}  CL={prog['cl']:.4f}  CD={prog['cd']:.5f}  "
                f"ETA(pt)={eta_str}   elapsed={((now - start_time) / 60):.1f} min   "
            )
            sys.stdout.write(line[:200].ljust(200))
            sys.stdout.flush()

        if results_done.exists():
            print(f"\n\nSWEEP COMPLETE -- {results_done} written. Stopping monitor.")
            break

        time.sleep(POLL_SECS)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nStopped watching (the SU2 sweep itself keeps running in the background).")
