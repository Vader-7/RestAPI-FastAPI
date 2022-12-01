from fastapi import FastAPI
from routes.profesor import profesor
from routes.clases import clase
from routes.alumno import alumno
from routes.asignatura import asignatura
from routes.agenda import agenda

app = FastAPI()

app.include_router(clase)
app.include_router(profesor)
app.include_router(alumno)
app.include_router(asignatura)
app.include_router(agenda)


@app.get('/')
async def index():
    return {'message': 'Hello World'}
