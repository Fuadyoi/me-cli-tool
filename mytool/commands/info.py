import typer
from services.api import get_info

info = typer.Typer()

@info.command()
def run():
    data = get_info()
    typer.echo(data)
