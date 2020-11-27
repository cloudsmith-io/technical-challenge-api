import click
from flask.cli import FlaskGroup

from challenge.app import create_app


def create_challenge(info):
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_challenge)
def cli():
    """Main entry point"""


@cli.command("init")
def init():
    """Create a new admin user"""
    from challenge.extensions import db
    from challenge.models import User

    click.echo("create user")
    user = User(username="admin", email="jobs@cloudsmith.com", password="admin", active=True)
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")


if __name__ == "__main__":
    cli()
