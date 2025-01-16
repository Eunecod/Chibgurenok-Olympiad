from services.OAuth2PasswordBearerCookie    import OAuth2PasswordBearerCookie
from fastapi                                import APIRouter, Depends


Route: APIRouter = APIRouter(prefix="/api")
Oauth2: OAuth2PasswordBearerCookie = OAuth2PasswordBearerCookie(token_url="/api")

@Route.get("/protected", dependencies=[Depends(Oauth2)])
async def Protected_Endpoint() -> dict:
    return { "session": True }