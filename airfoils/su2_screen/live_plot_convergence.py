"""Live-updating matplotlib view of the currently-running SU2 Mach point's convergence, read straight off the \\\\wsl.localhost UNC path so this runs on Windows without shelling into WSL."""
import re
import time
from pathlib import Path

import matplotlib.pyplot as plt

WSL_DIR = Path(r"\\wsl.localhost\Ubuntu\home\cyph3r\mses_replacement\mach_sweep_v2")
POLL_SECS = 5

ROW_RE = re.compile(r"^\|\s*(\d+)\|\s*(-?[\d.]+)\|\s*(-?[\d.]+)\|\s*(-?[\d.]+)\|\s*(-?[\d.]+)\|\s*$", re.MULTILINE)


def latest_log() -> Path | None:
    logs = sorted(WSL_DIR.glob("log_sc20412_v2_M*.txt"), key=lambda p: p.stat().st_mtime)
    return logs[-1] if logs else None


def parse_rows(log_path: Path):
    text = log_path.read_text(errors="ignore")
    rows = ROW_RE.findall(text)
    iters = [int(r[0]) for r in rows]
    rms_rho = [float(r[1]) for r in rows]
    cd = [float(r[4]) for r in rows]
    return iters, rms_rho, cd


def main():
    plt.ion()
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 7), sharex=True)
    fig.suptitle("SC(2)-0412 v2 sweep -- live convergence (auto-refresh)")

    current_path = None
    results_done = WSL_DIR / "adaptive_sweep_results_v2.json"

    while plt.fignum_exists(fig.number):
        log_path = latest_log()
        if log_path is not None:
            if log_path != current_path:
                current_path = log_path
                print(f"Now watching: {log_path.name}")

            try:
                iters, rms_rho, cd = parse_rows(log_path)
            except Exception as e:
                print(f"read error (transient, SU2 may be mid-write): {e}")
                time.sleep(POLL_SECS)
                continue

            if iters:
                ax1.clear()
                ax1.plot(iters, rms_rho, color="#1f77b4", lw=1.2)
                ax1.axhline(-3.0, color="0.6", ls="--", lw=0.8, label="observed plateau (~-3.0)")
                ax1.set_ylabel(r"$\log_{10}(rms_\rho)$")
                ax1.set_title(f"{log_path.stem}  --  iter {iters[-1]}")
                ax1.legend(fontsize=8, loc="upper right")
                ax1.grid(alpha=0.3)

                ax2.clear()
                ax2.plot(iters, [c * 1e4 for c in cd], color="#d62728", lw=1.2)
                ax2.set_ylabel(r"$C_D$ (counts)")
                ax2.set_xlabel("Inner iteration")
                ax2.grid(alpha=0.3)

                fig.canvas.draw()
                fig.canvas.flush_events()

        if results_done.exists():
            print("Sweep complete -- results file written. Leaving final plot up.")
            plt.ioff()
            plt.show()
            break

        plt.pause(POLL_SECS)


if __name__ == "__main__":
    main()
