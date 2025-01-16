from fastapi            import HTTPException, UploadFile, Depends, Query, File
from models             import CDisciplines, COlympiads, CResults
from fastapi.responses  import FileResponse
from .BaseRouters       import Route, Oauth2
from PIL                import Image
from typing             import List
import shutil, os


UPLOAD_DIRECTORY = "./storage/file"

@Route.get("/get/olympiads")
async def Get_Olympiads_Endpoint() -> dict:
    Olympiad: COlympiads = COlympiads()

    _olympiads: list = []
    for olympiad in await Olympiad.Read():
        _discipline = olympiad.GetDiscipline()    
        
        _olympiads.append({
                "discipline":   {"subject": _discipline.Subject, "level": _discipline.Level},
                "title":        olympiad.Title,
                "describe":     olympiad.Describe,
                "access_date":  olympiad.Access_Date,
                "passage_time": olympiad.Passage_Time,
                "path_preview": olympiad.Path_Preview,
                "document":     olympiad.Document
            })

    return {"olympiads": _olympiads}


@Route.get("/get/disciplines")
async def Get_Disciplines_Endpoint() -> dict:
    Discipline: CDisciplines = CDisciplines()

    _disciplines: list = []
    for discipline in await Discipline.Read():
        _disciplines.append({
            "id":       discipline.ID,
            "subject":  discipline.Subject,
            "level":    discipline.Level
        })

    Data: dict = {
        "disciplines":  _disciplines,
    }

    return Data


@Route.get("/admin/result", dependencies=[Depends(Oauth2)])
async def Get_Result_Endpoint(subject: str = Query(...), level: str = Query(...)) -> dict:
    Result: CResults = CResults()

    _results: list = []
    for result in await Result.Read():
        Discipline: CDisciplines = CDisciplines()
        _olympiad   = result.GetOlympiad()
        _discipline = await Discipline.GetObjectID(_olympiad.Discipline)
        
        if (_discipline.Subject == subject or _discipline.Level == level):
            _account = result.GetAccount()
       
            _results.append({
                "id":           result.ID,
                "class":        _account.Class,
                "login":        _account.Login,
                "subject":      _discipline.Subject,
                "level":        _discipline.Level,
                "assessed":     result.Assessed,
                "reply_body":   result.Reply_Body
            })
    
    return {"results": _results}


@Route.post("/admin/upload/file")
async def UploadFile_Olympiad_Endpoint(File: List[UploadFile] = File(...)) -> dict: 
    os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)
    for blob in File:
        sLocation: str = f"{UPLOAD_DIRECTORY}/{blob.filename}"
        with open(sLocation, "wb") as buffer:
            shutil.copyfileobj(blob.file, buffer)
        
        if blob.content_type.startswith("image/"):
            with Image.open(sLocation) as img:
                img.save(sLocation, optimize=True, quality=80)

    return {}


@Route.get("/download/file/{Filename}")
async def download_file(Filename: str):
    sFilePath = os.path.join(UPLOAD_DIRECTORY, Filename)
    if (not os.path.isfile(sFilePath)):
        raise HTTPException(status_code=404, detail="File not found")
    
    return FileResponse(path=sFilePath, filename=Filename)