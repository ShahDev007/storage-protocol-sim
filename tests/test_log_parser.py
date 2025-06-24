import pytest
import sys
from utils import log_parser

@pytest.mark.skipif(sys.platform.startswith("win"), reason="dmesg not available on Windows")
def test_find_nvme_errors():
    errors = log_parser.find_nvme_errors()
    assert isinstance(errors, list)
