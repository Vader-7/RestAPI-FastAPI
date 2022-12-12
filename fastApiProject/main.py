from fastapi import FastAPI, Request
from routes.profesor import profesor
from routes.clases import clase
from routes.alumno import alumno
from routes.asignatura import asignatura
from routes.agenda import agenda
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.include_router(clase)
app.include_router(profesor)
app.include_router(alumno)
app.include_router(asignatura)
app.include_router(agenda)



@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
