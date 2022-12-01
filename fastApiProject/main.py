from fastapi import FastAPI
from fastApiProject.routes.profesor import profesor
from fastApiProject.routes.clases import clase
from fastApiProject.routes.alumno import alumno

app = FastAPI()

app.include_router(curso)
app.include_router(profesor)
app.include_router(alumno)

@app.get('/')
async def index():
    return {'message': 'Hello World'}