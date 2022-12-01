from fastapi import APIRouter
from fastApiProject.schemes.alumno import Alumno
from fastApiProject.configbs.db import cursor
from fastApiProject.configbs.db import conection
alumno = APIRouter()

@alumno.get('/alumnos')
async def getAlumnos():
    return cursor.execute('SELECT * FROM alumno').fetchall(), 'Alumnos obtenidos'

@alumno.post('/alumnos')
async def postAlumnos(alumno: Alumno):
    cursor.execute('INSERT INTO alumno(rut_alum, nombre_alum, apellidos_alum, correo_alum) VALUES(:rut, :nombre, :apellido, :correo)', alumno.dict())
    conection.commit()
    return alumno.dict(), 'Alumno creado'

@alumno.put('/alumnos/{rut}')
async def putAlumnos(rut: str, alumno: Alumno):
    cursor.execute('UPDATE alumno SET nombre_alum = :nombre, apellidos_alum = :apellido, correo_alum = :correo WHERE rut_alum = :rut', [alumno.nombre, alumno.apellido, alumno.correo, rut])
    conection.commit()
    return alumno.dict(), 'Alumno actualizado'

@alumno.delete('/alumnos/{rut}')
async def deleteAlumnos(rut: str):
    cursor.execute('DELETE FROM alumno WHERE rut_alum = :rut', [rut])
    conection.commit()
    return 'Alumno eliminado'

