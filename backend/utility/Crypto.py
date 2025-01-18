from bcrypt import gensalt, hashpw, checkpw


SECRET_KEY = '45cc5adfd4f2aed1613f4113cd83be275ac486db47d8f39c31bf63704e11654c'

def CreatePasshash(sPassword: str) -> str:
    byteSalt: bytes = gensalt()
    bytePasshash: bytes = hashpw(sPassword.encode("utf-8"), byteSalt)
    return bytePasshash.decode('utf-8')


def ComparePassword(sPassword: str, sPasshash: str) -> bool:
    bCheck: bool = checkpw(sPassword.encode("utf-8"), sPasshash.encode("utf-8"))
    return bCheck


def CreateSignKey() -> str:
    byteSalt: bytes = gensalt()
    byteSign: bytes = hashpw(SECRET_KEY.encode("utf-8"), byteSalt)
    return byteSign.decode('utf-8')


def VerifySignKey(sSign: str) -> bool:
    bCheck: bool = checkpw(SECRET_KEY.encode("utf-8"), sSign.encode("utf-8"))
    return bCheck