import subprocess
from pathlib import Path

def run_scan(target):
    output_dir = Path(f"scans/{target}")

    cmd = [
        "autorecon",
        target,
        "-o",
        str(output_dir)
    ]

    print(f"[+] Starting AutoRecon against {target}")
    subprocess.run(cmd)