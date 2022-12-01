from fastapi import FastAPI

from routes.cursos import curso

app = FastAPI()

app.include_router(curso)