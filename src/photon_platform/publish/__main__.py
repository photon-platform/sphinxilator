"""The package entry point into the application."""
from . import app

def run() -> None:
    app.cli()

if __name__ == "__main__":
    run()
