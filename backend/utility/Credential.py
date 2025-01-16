from random import choices
from typing import LiteralString
from string import ascii_letters, digits


LOGIN_LENGHT       = 10
PASSWORD_LENGHT    = 15 

def CredentialGenerator() -> dict:
    _characters: LiteralString = ascii_letters + digits
    sLogin: str     = ''.join(choices(_characters, k=LOGIN_LENGHT))
    sPassword: str  = ''.join(choices(_characters, k=PASSWORD_LENGHT))

    return {"login": sLogin, "password": sPassword}