# tests/test_nvme_sim.py
from simulator import nvme_sim
import time

def test_nvme_write_read():
    start = time.time()
    result_write = nvme_sim.run_nvme_write()
    result_read = nvme_sim.run_nvme_read()
    duration = time.time() - start

    assert result_write.returncode == 0, f"Write failed: {result_write.stderr}"
    assert result_read.returncode == 0, f"Read failed: {result_read.stderr}"
    assert duration < 2, f"Operation took too long: {duration:.2f} seconds"
