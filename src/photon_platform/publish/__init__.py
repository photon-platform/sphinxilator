"""
publish
============

PHOTON platform
---------------



"""
import os

__author__ = "PHOTON platform"
__maintainer__ = "PHOTON platform"
__email__ = "github@phiarchitect.com"
__version__ = "0.1.2"
__licence__ = "MIT"

def get_path():
    """
    Return the path to the theme's directory.
    """
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), "themes")
