"""
run the main app
"""
from .publish import Publish


def run() -> None:
    reply = Publish().run()
    print(reply)
