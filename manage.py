"""
Flask CLI configuration
"""

from flask.cli import FlaskGroup

from render import app


cli = FlaskGroup(app)


if __name__ == "__main__":
    cli()
