from utility            import ComparePassword, CreatePasshash, TokenCreate, CredentialGenerator
from fastapi            import HTTPException, Response, Depends, Body
from models             import CAccounts, CAdmin, COlympiads, CSubscriptions
from fastapi.security   import OAuth2PasswordRequestForm
from .BaseRouters       import Route, Oauth2 


@Route.post("/login")
async def Login_Endpoint(response: Response, Data: OAuth2PasswordRequestForm = Depends()) -> dict:
    Account: CAccounts = CAccounts()
    _accounts = await Account.GetObject(CAccounts.Login, Data.username)

    for user in _accounts.all():
        if (Data.username == user.Login and ComparePassword(Data.password, user.Passhash)):
            access_token = TokenCreate({
                "fullname": user.Fullname
            }, user.ID)
            response.set_cookie(key="access_token", value=access_token, httponly=True, samesite="Lax")
            
            return {"autorized": True, "grand" : False}
        

    Admin: CAdmin = CAdmin()
    _admin = await Admin.GetObject(CAdmin.Login, Data.username)

    for admin in _admin.all():
        if (Data.username == admin.Login and ComparePassword(Data.password, admin.Passhash) and admin.Active):
            access_token = TokenCreate({
                "fullname": admin.Fullname,
                "key": admin.Key,
            }, admin.ID)
            response.set_cookie(key="access_token", value=access_token, httponly=True, samesite="Lax")
            
            return {"autorized": True, "grand" : True}

    raise HTTPException(status_code=401, detail="Invalid login or password")


@Route.get("/logout", dependencies=[Depends(Oauth2)])
async def Logout_Endpoint(response: Response) -> dict:
    response.delete_cookie(key="access_token")        
    return {}


@Route.post("/signup")
async def Signup_Endpoint(Data: dict = Body(...)) -> dict:
    _credential = CredentialGenerator()

    Account: CAccounts  = CAccounts()
    Account.School      = Data.get("school")
    Account.Class       = Data.get("level")
    Account.Fullname    = Data.get("fullname")
    Account.Login       = _credential.get("login")
    Account.Passhash    = CreatePasshash(_credential.get("password"))

    nAccountID: int = await Account.Create()

    for subscribe in Data.get("subscribers"):
        Olympiad: COlympiads = COlympiads()
        _olympiads = await Olympiad.GetObject(COlympiads.Discipline, subscribe.get("id"))
        
        for olympiad in _olympiads.all():
            Subscription: CSubscriptions    = CSubscriptions() 
            Subscription.Account_ID         = nAccountID
            Subscription.Olympiad_ID        = olympiad.ID
            
            await Subscription.Create()
    
    User: list = [{"ФИО": Data.get("fullname"), "Логин": _credential.get("login"), "Пароль": _credential.get("password")}]
    return {"signup_csv": User}


@Route.post("/signup/csv")
async def SignupCSV_Endpoint(Data: dict = Body(...)) -> dict:
    Users: list = []

    CSV: dict = Data.get("CSV")
    for user in CSV:
        _credential = CredentialGenerator()
        Subscription: CSubscriptions = CSubscriptions()
    
        Account: CAccounts = CAccounts()
        Account.School      = user.get("Школа")
        Account.Class       = user.get("Класс")
        Account.Fullname    = user.get("ФИО")
        Account.Login       = _credential.get("login")
        Account.Passhash    = CreatePasshash(_credential.get("password"))
        
        nAccountID: int = await Account.Create()
    
        for subscribe in Data.get("subscribers"):
            Olympiad: COlympiads = COlympiads()
            _olympiads = await Olympiad.GetObject(COlympiads.Discipline, subscribe.get("id"))
            
            for olympiad in _olympiads.all():
                Subscription: CSubscriptions = CSubscriptions()
                Subscription.Account_ID     = nAccountID
                Subscription.Olympiad_ID    = olympiad.ID
    
                await Subscription.Create()
    
        Users.append({"ФИО": user.get("ФИО"), "Логин": _credential.get("login"), "Пароль": _credential.get("password")})

    return {"signup_csv": Users}
