import os
from dotenv import load_dotenv
load_dotenv()

def authenticate(email: str, password: str):
    token = f"{email}-token"  # dummy token
    with open(".env", "w") as f:
        f.write(f"TOKEN={token}\n")
    return token
