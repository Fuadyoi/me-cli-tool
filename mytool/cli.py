import typer
from commands.login import login
from commands.info import info
from commands.paket import paket

app = typer.Typer()
app.add_typer(login, name="login")
app.add_typer(info, name="info")
app.add_typer(paket, name="paket")

if __name__ == "__main__":
    app()
