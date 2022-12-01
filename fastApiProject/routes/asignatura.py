from fastapi import APIRouter
from schemes.asignatura import Asignatura
from configbs.db import cursor
from configbs.db import conection
asignatura = APIRouter()

@asignatura.get('/asignaturas')
async def getAsignaturas():
    return cursor.execute('SELECT * FROM asignatura').fetchall(), 'Asignaturas obtenidas'

@asignatura.post('/asignaturas')
async def postAsignaturas(asignatura: Asignatura):
    cursor.execute('INSERT INTO asignatura(id_asig, nombre_asig) VALUES(:id, :nombre)', asignatura.dict())
    conection.commit()
    return asignatura.dict(), 'Asignatura creada'

@asignatura.put('/asignaturas/{id}')
async def putAsignaturas(id: str, asignatura: Asignatura):
    cursor.execute('UPDATE asignatura SET nombre_asig = :nombre WHERE id_asig = :id', [asignatura, id,asignatura.nombre])
    conection.commit()
    return asignatura.dict(), 'Asignatura actualizada'

@asignatura.delete('/asignaturas/{id}')
async def deleteAsignaturas(id: str):
    cursor.execute('DELETE FROM asignatura WHERE id_asig = :id', [id])
    conection.commit()
    return 'Asignatura eliminada'
