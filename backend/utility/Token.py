from .Chronos   import CurrentTimestamp
from jwt        import encode, decode


SECRET_KEY = '45cc5adfd4f2aed1613f4113cd83be275ac486db47d8f39c31bf63704e11654c'
ACCESS_TOKEN_EXPIRE_MINUTES = 1800
ALGORITHM = 'HS256'

def TokenCreate(Data: dict = {}, nSub: int = -1, nExp: int = ACCESS_TOKEN_EXPIRE_MINUTES) -> str:
    Header: dict = {
        "alg": ALGORITHM,
        "typ": "JWT"
    }
    Payload: dict = {
        "usr": Data,
        "sub": str(nSub),
        "iat": CurrentTimestamp(),
        "exp": CurrentTimestamp() + nExp * 60
    }
    
    return encode(Payload, SECRET_KEY, algorithm=ALGORITHM, headers=Header)


def TokenRead(sToken: str) -> dict:
    try:
        Payload: dict = decode(sToken, SECRET_KEY, algorithms=ALGORITHM)
        return Payload

    except:
        return {}


def TokenValidate(sToken: str) -> bool:
    try:
        decode(sToken, SECRET_KEY, algorithms=ALGORITHM)
        return True

    except Exception:
        return False