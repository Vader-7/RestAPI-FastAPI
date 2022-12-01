from fastapi import APIRouter
from schemes.profesor import Profesor
from configbs.db import cursor
from configbs.db import conection
profesor = APIRouter()

@profesor.get('/profesores')
async def getProfesores():
    return cursor.execute('SELECT * FROM profesor').fetchall(), 'Profesores obtenidos'

@profesor.post('/profesores')
async def postProfesores(profesor: Profesor):
    cursor.execute('INSERT INTO profesor(rut_prof, nombre_prof, apellidos_prof, correo_prof) VALUES(:rut, :nombre, :apellido, :correo)', profesor.dict())
    conection.commit()
    return profesor.dict(), 'Profesor creado'

@profesor.put('/profesores/{rut}')
async def putProfesores(rut: str, profesor: Profesor):
    cursor.execute('UPDATE profesor SET nombre_prof = :nombre, apellidos_prof = :apellido, correo_prof = :correo WHERE rut_prof = :rut', [profesor.nombre, profesor.apellido, profesor.correo, rut])
    conection.commit()
    return profesor.dict(), 'Profesor actualizado'

@profesor.delete('/profesores/{rut}')
async def deleteProfesores(rut: str):
    cursor.execute('DELETE FROM profesor WHERE rut_prof = :rut', [rut])
    conection.commit()
    return 'Profesor eliminado'

