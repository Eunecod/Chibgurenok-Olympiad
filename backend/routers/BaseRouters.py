from services.OAuth2PasswordBearerCookie    import OAuth2PasswordBearerCookie
from fastapi                                import APIRouter, Depends
from utility                                import VerifySignKey


Route: APIRouter = APIRouter(prefix="/api")
Oauth2: OAuth2PasswordBearerCookie = OAuth2PasswordBearerCookie(token_url="/api")

@Route.get("/protected", dependencies=[Depends(Oauth2)])
async def Protected_Endpoint() -> dict:
    return { "session": True }

@Route.get("/admin/verification", dependencies=[Depends(Oauth2)])
async def Protected_Admin_Endpoint() -> dict:
    Payload: dict = Oauth2.GetPayload()
    _usr: dict = Payload.get("usr")

    sKey: str = _usr.get("key")
    if (sKey):
        return { "session": VerifySignKey(sKey) }
    else:
        return { "session": False }