from fastapi import APIRouter
from schemes.curso import Curso
from configbs.db import cursor
from configbs.db import conection
curso = APIRouter()


@curso.get('/cursos')
async def getCursos():
    return cursor.execute('SELECT nombre, codigo, credito FROM cursos').fetchall()

@curso.post('/cursos')
async def postCursos(curso: Curso):
    cursor.execute('INSERT INTO cursos(nombre, codigo, credito) VALUES(:nombre, :codigo, :credito)', curso.dict())
    conection.commit()
    return curso.dict(), 'Curso creado'

@curso.put('/cursos/{codigo}')
async def putCursos(codigo: str, curso: Curso):
    return cursor.execute('UPDATE cursos SET nombre = :nombre, credito = :credito WHERE codigo = :codigo', [curso.nombre, curso.creditos, codigo])
    conection.commit()
    return HTTPException(status_code = 200, detail = 'Curso actualizado con exito')

@curso.delete('/cursos/{codigo}')
async def deleteCursos(codigo: str):
    return cursor.execute('DELETE FROM cursos WHERE codigo = :codigo', [codigo])
    conection.commit()
    return HTTPException(status_code = 200, detail = 'Curso eliminado con exito')
