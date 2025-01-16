from utility        import CurrentTimestamp
from models         import CSession, CQuizzes, CResults, COlympiads 
from services       import GetReplyBody, GetAssessedReply 
from fastapi        import Depends, Body
from .BaseRouters   import Route, Oauth2
import json


@Route.get("/quiz/{quiz_id}", dependencies=[Depends(Oauth2)])
async def Quiz_Endpoint(quiz_id: int) -> dict:
    _payload: dict = Oauth2.GetPayload()

    Quiz: CQuizzes = CQuizzes()
    _quiz = await Quiz.GetObjectID(quiz_id)
        
    Olympiad: COlympiads = COlympiads()
    _temp = await Olympiad.GetObject(COlympiads.Quiz, quiz_id)
    _olympiad = _temp.first()

    Session: CSession = CSession()
    _session = await Session.GetObject(CSession.Account_ID, _payload.get("sub"))

    nTimestamp: int = _olympiad.Passage_Time * 60      
    bFirstStarted: bool = True         
    for session in _session.all():
        if (session.Olympiad_ID == _olympiad.ID):
            nTimestamp = session.End - CurrentTimestamp()
            bFirstStarted = False

    if (bFirstStarted):
        Session.Account_ID  = _payload.get("sub")
        Session.Olympiad_ID = _olympiad.ID
        Session.Start       = CurrentTimestamp()                              
        Session.End         = CurrentTimestamp() + nTimestamp
        await Session.Create()

    return {"quiz": json.loads(_quiz.Quiz_Body), "timestamp": nTimestamp}


@Route.post("/submit/quiz/{quiz_id}", dependencies=[Depends(Oauth2)])
async def Quiz_Submit_Endpoint(quiz_id: int, Data: dict = Body(...)) -> dict:
    _payload = Oauth2.GetPayload()
        
    Olympiad: COlympiads = COlympiads()
    _olympiad = await Olympiad.GetObject(COlympiads.Quiz, quiz_id)

    Quiz: CQuizzes = CQuizzes()
    _quiz = await Quiz.GetObjectID(quiz_id)


    Result: CResults    = CResults()
    Result.Account_ID   = _payload.get("sub")
    Result.Olympiad_ID  = _olympiad.first().ID
    Result.Assessed     = GetAssessedReply(json.loads(_quiz.Quiz_Reply), Data.get("reply_body"))
    Result.Reply_Body   = json.dumps(GetReplyBody(json.loads(_quiz.Quiz_Reply), Data.get("reply_body")))
        
    await Result.Create()

    return {}