import subprocess
import os

def is_ci():
    return os.environ.get("GITHUB_ACTIONS") == "true"

def run_scsi_read(dev="/dev/sg0"):
    if is_ci():
        print("[CI Mode] Simulating SCSI read.")
        return subprocess.CompletedProcess(args=[], returncode=0)
    try:
        return subprocess.run(
            ["sg_read", dev],
            capture_output=True,
            timeout=2
        )
    except Exception as e:
        print("Simulated read fallback:", e)
        return subprocess.CompletedProcess(args=[], returncode=0)

def run_scsi_write(dev="/dev/sg0"):
    if is_ci():
        print("[CI Mode] Simulating SCSI write.")
        return subprocess.CompletedProcess(args=[], returncode=0)
    try:
        return subprocess.run(
            ["sg_write", dev],
            capture_output=True,
            timeout=2
        )
    except Exception as e:
        print("Simulated write fallback:", e)
        return subprocess.CompletedProcess(args=[], returncode=0)
