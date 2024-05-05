#  from ablog.conf import *
from photon_platform.sphinxilator.global_conf import *
import photon_platform.sphinxilator as module

version = module.__version__

org = "photon-platform"
org_name = "photon-platform"

repo = "sphinxilator"
repo_name = "sphinxilator"

setup_globals(org, org_name, repo, repo_name)

html_theme = "sphinxilator_theme"
