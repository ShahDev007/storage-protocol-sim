# utils/log_parser.py
import subprocess

def find_nvme_errors():
    try:
        logs = subprocess.check_output(["dmesg"], text=True)
        return [line for line in logs.splitlines() if "nvme" in line.lower() and "error" in line.lower()]
    except subprocess.CalledProcessError:
        return []
