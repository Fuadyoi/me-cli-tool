import typer
from services.api import list_paket

paket = typer.Typer()

@paket.command()
def list():
    items = list_paket()
    for pkt in items:
        typer.echo(f"- {pkt['nama']} ({pkt['harga']})")
