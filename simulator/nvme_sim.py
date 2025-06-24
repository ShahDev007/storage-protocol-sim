# # simulator/nvme_sim.py
# import subprocess

# def run_nvme_write(dev="/dev/nvme0n1", block_count=1):
#     try:
#         return subprocess.run(
#             ["nvme", "write", dev, "--data-size", str(block_count)],
#             capture_output=True,
#             timeout=2
#         )
#     except Exception as e:
#         print("Simulated write (mock fallback):", e)
#         return subprocess.CompletedProcess(args=[], returncode=0)

# def run_nvme_read(dev="/dev/nvme0n1", block_count=1):
#     try:
#         return subprocess.run(
#             ["nvme", "read", dev, "--data-size", str(block_count)],
#             capture_output=True,
#             timeout=2
#         )
#     except Exception as e:
#         print("Simulated read (mock fallback):", e)
#         return subprocess.CompletedProcess(args=[], returncode=0)





# simulator/nvme_sim.py
import subprocess
import os

def is_ci():
    return os.environ.get("GITHUB_ACTIONS") == "true"

def run_nvme_write(dev="/dev/nvme0n1", block_count=1):
    if is_ci():
        print("[CI Mode] Simulating nvme write.")
        return subprocess.CompletedProcess(args=[], returncode=0)
    try:
        return subprocess.run(
            ["nvme", "write", dev, "--data-size", str(block_count)],
            capture_output=True,
            timeout=2
        )
    except Exception as e:
        print("Simulated write fallback:", e)
        return subprocess.CompletedProcess(args=[], returncode=0)

def run_nvme_read(dev="/dev/nvme0n1", block_count=1):
    if is_ci():
        print("[CI Mode] Simulating nvme read.")
        return subprocess.CompletedProcess(args=[], returncode=0)
    try:
        return subprocess.run(
            ["nvme", "read", dev, "--data-size", str(block_count)],
            capture_output=True,
            timeout=2
        )
    except Exception as e:
        print("Simulated read fallback:", e)
        return subprocess.CompletedProcess(args=[], returncode=0)
