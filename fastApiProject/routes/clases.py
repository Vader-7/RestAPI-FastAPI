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
    cursor._verify_open()
    try:
        # Check if the class already exists
        cursor.execute('SELECT * FROM clases WHERE id_clas = :id_clas', [clase.id_clas])
        existing_class = cursor.fetchone()
        if existing_class:
            # Return an error if the class already exists
            return {"error": "La clase ya existe"}, 400
        # Check if the asignatura exists
        cursor.execute('SELECT * FROM asignatura WHERE id_asig = :id_asig', [clase.id_asig])
        existing_asignatura = cursor.fetchone()
        if not existing_asignatura:
            # Return an error if the asignatura does not exist
            return {"error": "La asignatura no existe"}, 404

        # Insert the new class into the database
        cursor.execute(
            'INSERT INTO clases(id_clas, horario_ini_clas, horario_fin_clas, id_asig) VALUES(:id_clas, :horario_ini, :horario_fin, :id_asig)',
            clase.dict())
        conection.commit()

        # Return the new class
        return clase.dict(), 'Clase creada'
    finally:
        # Close the cursor and connection
        cursor.close()
        conection.close()


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
