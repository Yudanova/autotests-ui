import pytest
import sys

SYSTEM_VERSION = "v1.2.0"  # Version of testing system ("girsa")


@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.3.0",  # Scip test if the version is "v1.3.0"
    reason="Test can not be run in the version v1.3.0"
)
def test_system_version_valid():  # This test will run in the current configuration
    pass


@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.2.0",  # Skip test if the system version is v1.2.0
    reason="Test cannot be run for the version v1.2.0"
)
def test_system_version_invalid():  # This test will not run
    pass

# python -m pytest -k "test_system_version" -s -v // EXPECTED:  1 passed, 1 skipped, 6 deselected in 0.83s 
