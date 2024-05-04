"""
run the main app
"""
from .sphinxilator import Sphinxilator


def run() -> None:
    reply = Sphinxilator().run()
    print(reply)
