from .BaseRouters  import Route, Oauth2
from fastapi       import Depends, Body
from models        import COlympiads, CQuizzes, CDisciplines, CResults, CAdmin
from utility       import CreatePasshash, CreateSignKey
import json


@Route.post("/admin/create/discipline", dependencies=[Depends(Oauth2)])
async def Create_Discipline_Endpoint(Data: dict = Body(...)) -> dict:
    Discipline: CDisciplines = CDisciplines()
    Discipline.Subject  = Data.get("subject")
    Discipline.Level    = Data.get("level")

    await Discipline.Create();

    _disciplines: list = []
    for discipline in await Discipline.Read():
        _disciplines.append({
            "id":       discipline.ID,
            "subject":  discipline.Subject,
            "level":    discipline.Level
        })

    return { "disciplines": _disciplines }


@Route.post("/admin/create/olympiad", dependencies=[Depends(Oauth2)])
async def Create_Olympiad_Endpoint(Data: dict = Body(...)) -> dict: 
    _olympiad:  dict = Data.get("olympiad")
    _questions: dict = Data.get("questions")

    _questionQuizBody:  list = []
    _questionQuizReply: list = []

    for question in _questions:
        _options: list = []
        for option in question.get("options"):            
            _options.append({
                "id":   option.get("id"),
                "text": option.get("text")
            })

        _questionQuizBody.append({
            "id":       question.get("id"),
            "type":     question.get("type"),
            "score":    question.get("score"),
            "issue":    question.get("issue"),
            "image":    question.get("image").get("name"),
            "options":  _options
        })

        _questionQuizReply.append({
            "id":       question.get("id"),    
            "score":    question.get("score"),
            "correct":  question.get("correct"),
        })

    Quiz: CQuizzes  = CQuizzes()
    Quiz.Quiz_Body  = json.dumps(_questionQuizBody)
    Quiz.Quiz_Reply = json.dumps(_questionQuizReply)

    Olympiad: COlympiads    = COlympiads()
    Olympiad.Title          = _olympiad.get("title")
    Olympiad.Discipline     = _olympiad.get("discipline")
    Olympiad.Describe       = _olympiad.get("describe")
    Olympiad.Passage_Time   = _olympiad.get("passage_time")
    Olympiad.Access_Date    = _olympiad.get("access_date")
    Olympiad.Path_Preview   = _olympiad.get("image").get("name")
    Olympiad.Document       = _olympiad.get("document").get("name")
    Olympiad.Quiz           = await Quiz.Create()

    await Olympiad.Create()

    return {}


@Route.get("/admin/get/reply/{result_id}", dependencies=[Depends(Oauth2)])
async def Get_Reply_Endpoint(result_id: int) -> dict:
    Result: CResults = CResults()
    _result = await Result.GetObjectID(result_id)
    
    Olympiad: COlympiads = COlympiads()
    _olympiad = await Olympiad.GetObjectID(_result.Olympiad_ID)
    _quiz = _olympiad.GetQuiz()

    return {"quiz_body": json.loads(_quiz.Quiz_Body), "reply_body" : json.loads(_result.Reply_Body)}


@Route.post("/admin/update/reply/{result_id}", dependencies=[Depends(Oauth2)])
async def Update_Reply_Endpoint(result_id: int, Data: dict = Body(...)) -> dict:
    Result: CResults    = CResults()
    Result.Assessed     = Data.get("assessed")
    Result.Reply_Body   = json.dumps(Data.get("reply_body"))
    
    await Result.Update(result_id)

    return {}


@Route.post("/admin/create/administrator", dependencies=[Depends(Oauth2)])
async def Create_Administrator_Endpoin(Data: dict = Body(...)) -> dict:
    Admin: CAdmin = CAdmin()

    Admin.Fullname  = Data.get("fullname")
    Admin.Login     = Data.get("login")
    Admin.Passhash  = CreatePasshash(Data.get("password"))
    Admin.Key       = CreateSignKey()
    
    await Admin.Create()

    return {}