import click as click

from database import db
from main import app


@click.group()
def cli():
    pass


@click.command()
def initdb():
    with app.app_context():
        db.create_all()


cli.add_command(initdb)

cli()
