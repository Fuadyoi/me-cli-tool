import typer
from services.auth import authenticate

login = typer.Typer()

@login.command()
def run(email: str, password: str):
    token = authenticate(email, password)
    typer.echo(f"Login sukses! Token: {token}")
