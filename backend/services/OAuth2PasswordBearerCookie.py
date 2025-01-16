from fastapi.security   import OAuth2PasswordBearer
from fastapi.exceptions import HTTPException
from starlette.requests import Request
from typing             import Optional
from utility            import TokenRead, TokenValidate


class OAuth2PasswordBearerCookie(OAuth2PasswordBearer):
    def __init__(
        self,
        token_url: str,
        scheme_name: str = None,
        payload: dict = None,
        scopes: dict = None,
        auto_error: bool = True,
    ):
        self.payload = payload
        if scopes is None:
            scopes = {}
    
        super().__init__(tokenUrl=token_url, scheme_name=scheme_name, auto_error=auto_error)

    async def __call__(self, request: Request) -> Optional[str]:
        access_token: str = request.cookies.get("access_token")
       
        if (not TokenValidate(access_token)):
            if (self.auto_error):
                raise HTTPException(
                    status_code=401,
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            else:
                return None
        
        self.payload = TokenRead(access_token)
        return access_token
    
    def GetPayload(self) -> dict:
        return self.payload
