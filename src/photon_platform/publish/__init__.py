"""
publish
============

PHOTON platform
---------------

.. todo:: complete documentation

"""
import os

__author__ = "PHOTON platform"
__maintainer__ = "PHOTON platform"
__email__ = "github@phiarchitect.com"
__version__ = "0.2.8"
__licence__ = "MIT"

def get_path() -> str:
    """Return the absolute path to the theme's directory."""
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), "themes")
