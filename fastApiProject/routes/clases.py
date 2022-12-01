from fastapi import APIRouter
from fastApiProject.schemes.clase import Clase
from fastApiProject.configbs.db import cursor
from fastApiProject.configbs.db import conection
curso = APIRouter()


@curso.get('/clases')
async def getClases():
    return cursor.execute('SELECT asignatura.nombre_asig, id_clas, horario_ini_clas, horario_fin_clas FROM clase JOIN asignatura ').fetchall(), 'Clases obtenidas'


@curso.post('/clases')
async def postClases(clase: Clase):
    cursor.execute('INSERT INTO clase(id_clas, horario_ini_clas, horario_fin_clas, id_asig) VALUES(:id, :horario_ini, :horario_fin, :id_asig)', clase.dict())
    conection.commit()
    return clase.dict(), 'Clase creada'


@curso.put('/clases/{id}')
async def putClases(id: str, clase: Clase):
    cursor.execute('UPDATE clase SET horario_ini_clas = :horario_ini, horario_fin_clas = :horario_fin, id_asig = :id_asig WHERE id_clas = :id', [clase.horario_ini, clase.horario_fin, clase.id_asig, id])
    conection.commit()
    return clase.dict(), 'Clase actualizada'


@curso.delete('/clases/{id}')
async def deleteClases(id: str):
    cursor.execute('DELETE FROM clase WHERE id_clas = :id', [id])
    conection.commit()
    return 'Clase eliminada'

# Path: fastApiProject/routes/curso.py
