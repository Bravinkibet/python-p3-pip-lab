import pytest
from versions import python_version, requests_version, pytest_version

def test_python_version():
    version_info = python_version()
    assert version_info.major == 3
    assert version_info.minor == 8

def test_requests_version():
    version = requests_version()
    assert isinstance(version, str)
    assert version == "2.32.2"  # Update this to the actual installed version

def test_pytest_version():
    version = pytest_version()
    assert isinstance(version, str)
    assert version == "8.2.1"  # Update this to the actual installed version
