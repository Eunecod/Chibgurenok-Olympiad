from .BaseRouters   import Route, Oauth2
from fastapi        import Depends
from utility        import CurrentDatestamp
from models         import CResults, COlympiads, CDisciplines, CSubscriptions             


@Route.get("/profile", dependencies=[Depends(Oauth2)])
async def Profile_Endpoint() -> dict:   
    _payload: dict = Oauth2.GetPayload()

    Subscription: CSubscriptions = CSubscriptions()
    _subscriptions = await Subscription.GetObject(CSubscriptions.Account_ID, _payload.get("sub"))
    _olympiads: list = []
    for subscription in _subscriptions.all():
        nActive: int = 1

        Olympiad: COlympiads = COlympiads()
        _olympiad = await Olympiad.GetObjectID(subscription.Olympiad_ID)

        Discipline: CDisciplines = CDisciplines()
        _discipline = await Discipline.GetObjectID(_olympiad.Discipline)

        Result: CResults = CResults()
        _results = await Result.GetObject(CResults.Account_ID, _payload.get("sub"))
        for result in _results.all():
            if (result.Olympiad_ID == _olympiad.ID):
                nActive = 0
                
        if (_olympiad.Access_Date != CurrentDatestamp()):
            nActive = 0

        _olympiads.append({
            "discipline":   {"subject": _discipline.Subject, "level": _discipline.Level},
            "quiz":         _olympiad.Quiz,
            "title":        _olympiad.Title,
            "describe":     _olympiad.Describe,
            "access_date":  _olympiad.Access_Date,
            "passage_time": _olympiad.Passage_Time,
            "path_preview": _olympiad.Path_Preview,
            "active":       nActive,
        })

    return {"payload" : _payload, "olympiads" : _olympiads}

