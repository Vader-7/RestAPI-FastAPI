from fastapi import APIRouter
from fastApiProject.schemes.asignatura import Asignatura
from fastApiProject.configbs.db import cursor
from fastApiProject.configbs.db import conection
asignatura = APIRouter()

@asignatura.get('/asignaturas')
async def getAsignaturas():
    return cursor.execute('SELECT * FROM asignatura').fetchall(), 'Asignaturas obtenidas'

@asignatura.post('/asignaturas')
async def postAsignaturas(asignatura: Asignatura):
    cursor.execute('INSERT INTO asignatura(id_asig, nombre_asig) VALUES(:id, :nombre, :id_prof)', asignatura.dict())
    conection.commit()
    return asignatura.dict(), 'Asignatura creada'

@asignatura.put('/asignaturas/{id}')
async def putAsignaturas(id: str, asignatura: Asignatura):
    cursor.execute('UPDATE asignatura SET nombre_asig = :nombre, id_prof = :id_prof WHERE id_asig = :id', [asignatura.nombre, asignatura.id_prof, id])
    conection.commit()
    return asignatura.dict(), 'Asignatura actualizada'

@asignatura.delete('/asignaturas/{id}')
async def deleteAsignaturas(id: str):
    cursor.execute('DELETE FROM asignatura WHERE id_asig = :id', [id])
    conection.commit()
    return 'Asignatura eliminada'
