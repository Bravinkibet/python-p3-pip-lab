import sys
import requests
import pytest

def python_version():
    """Return the version information of the Python interpreter."""
    return sys.version_info

def requests_version():
    """Return the version of the requests library."""
    return requests.__version__

def pytest_version():
    """Return the version of the pytest library."""
    return pytest.__version__
