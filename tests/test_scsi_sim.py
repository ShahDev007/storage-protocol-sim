from simulator import scsi_sim
import time

def test_scsi_write_read():
    start = time.time()
    result_write = scsi_sim.run_scsi_write()
    result_read = scsi_sim.run_scsi_read()
    duration = time.time() - start

    assert result_write.returncode == 0, f"SCSI write failed: {result_write.stderr}"
    assert result_read.returncode == 0, f"SCSI read failed: {result_read.stderr}"
    assert duration < 2, f"Operation took too long: {duration:.2f} seconds"
