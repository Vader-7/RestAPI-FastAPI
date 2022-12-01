from fastapi import APIRouter
from schemes.clase import Clase
from configbs.db import cursor
from configbs.db import conection
clase = APIRouter()


@clase.get('/clases')
async def getClases():
    return cursor.execute('SELECT id_clas, horario_ini_clas, horario_fin_clas FROM clases').fetchall(), 'Clases obtenidas'


@clase.post('/clases')
async def postClases(clase: Clase):
    cursor.execute('INSERT INTO clases(id_clas, horario_ini_clas, horario_fin_clas, id_asig) VALUES(:id_clas, :horario_ini, :horario_fin, :id_asig)', clase.dict())
    conection.commit()
    return clase.dict(), 'Clase creada'


@clase.put('/clases/{id}')
async def putClases(id: str, clase: Clase):
    cursor.execute('UPDATE clase SET horario_ini_clas = :horario_ini, horario_fin_clas = :horario_fin, id_asig = :id_asig WHERE id_clas = :id_clas', [clase.horario_ini, clase.horario_fin, clase.id_asig, id_clas])
    conection.commit()
    return clase.dict(), 'Clase actualizada'


@clase.delete('/clases/{id}')
async def deleteClases(id: str):
    cursor.execute('DELETE FROM clases WHERE id_clas = :id_clas', [id])
    conection.commit()
    return 'Clase eliminada'

# Path: fastApiProject/routes/curso.py
