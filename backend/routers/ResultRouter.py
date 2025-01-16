from .BaseRouters  import Route
from models        import CResults, CDisciplines


@Route.get("/result")
async def Result_Endpoint() -> dict:
    Result: CResults = CResults()
    Discipline: CDisciplines = CDisciplines()

    _results: list = []
    for result in await Result.Read():
        _account = result.GetAccount()
        _olympiad = result.GetOlympiad()
        _discipline = await Discipline.GetObjectID(_olympiad.Discipline)
        
        _results.append({
            "id":           result.ID,
            "class":        _account.Class,
            "login":        _account.Login,
            "subject":      _discipline.Subject,
            "level":        _discipline.Level,
            "assessed":     result.Assessed,
            "body_reply":   result.Reply_Body
        })
    
    return {"results": _results}