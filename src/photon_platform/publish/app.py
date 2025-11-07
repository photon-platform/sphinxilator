
"""
Command-line interface for the publish tool.
"""
import click
from . import publish

@click.group()
def cli():
    """A tool to streamline and enhance the Sphinx documentation framework."""
    pass

@cli.command()
def build():
    """Builds the documentation."""
    publish.build()

@cli.command()
def test():
    """Builds and serves the documentation locally."""
    publish.test()


