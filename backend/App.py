from starlette.middleware.cors  import CORSMiddleware
from fastapi.staticfiles        import StaticFiles
from fastapi                    import FastAPI
from routers                    import Route
from uvicorn                    import run


app: FastAPI = FastAPI()
app.include_router(Route)
app.mount("/storage", StaticFiles(directory="./storage"), name="storage")

origins: list = [
    "http://localhost:8000",  # URL Vue.js приложения
]

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

if (__name__ == "__main__"):
    run("App:app", host="0.0.0.0", port=5000, reload=True)
