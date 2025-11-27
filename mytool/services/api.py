import os
from dotenv import load_dotenv
load_dotenv()

def get_info():
    token = os.getenv("TOKEN", "tidak login")
    return {"status": "OK", "token": token}

def list_paket():
    return [
        {"nama": "Paket A", "harga": "10K"},
        {"nama": "Paket B", "harga": "20K"}
    ]
