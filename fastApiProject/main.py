from fastapi import FastAPI
from fastApiProject.routes.profesor import profesor
from fastApiProject.routes.clases import clase
from fastApiProject.routes.alumno import alumno
from fastApiProject.routes.asignatura import asignatura
from fastApiProject.routes.agenda import agenda

app = FastAPI()

app.include_router(clase)
app.include_router(profesor)
app.include_router(alumno)
app.include_router(asignatura)
app.include_router(agenda)
@app.get('/')
async def index():
    return {'message': 'Hello World'}