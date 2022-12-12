from fastapi import APIRouter
from schemes.profesor import Profesor
from configbs.db import cursor
from configbs.db import conection

profesor = APIRouter()


@profesor.get('/profesores')
async def getProfesores():
    try:
        # Query the database to get all professors
        cursor.execute('SELECT * FROM profesor')
        professors = cursor.fetchall()

        # Return the list of professors
        return professors, 'Profesores obtenidos'
    finally:
        # Close the cursor and connection
        cursor.close()
        conection.close()


@profesor.post('/profesores')
async def postProfesores(profesor: Profesor):
    cursor._verify_open()
    try:
        # Check if the professor already exists
        cursor.execute('SELECT * FROM profesor WHERE rut_prof = :rut', [profesor.rut])
        existing_professor = cursor.fetchone()
        if existing_professor:
            # Return an error if the professor already exists
            return {"error": "El profesor ya existe"}, 400

        # Insert the new professor into the database
        cursor.execute(
            'INSERT INTO profesor(rut_prof, nombre_prof, apellidos_prof, correo_prof) VALUES(:rut, :nombre, :apellido, :correo)',
            profesor.dict())
        conection.commit()

        # Return the new professor
        return profesor.dict(), 'Profesor creado'
    finally:
        # Close the cursor and connection
        cursor.close()
        conection.close()


@profesor.put('/profesores/{rut}')
async def putProfesores(rut: str, profesor: Profesor):
    cursor._verify_open()
    try:
        # Check if the professor exists
        cursor.execute('SELECT * FROM profesor WHERE rut_prof = :rut', [rut])
        existing_professor = cursor.fetchone()
        if not existing_professor:
            # Return an error if the professor does not exist
            return {"error": "El profesor no existe"}, 404

        # Update the professor in the database
        cursor.execute(
            'UPDATE profesor SET nombre_prof = :nombre, apellidos_prof = :apellido, correo_prof = :correo WHERE rut_prof = :rut',
            [profesor.nombre, profesor.apellido, profesor.correo, rut])
        conection.commit()

        # Return the updated professor
        return profesor.dict(), 'Profesor actualizado'
    finally:
        # Close the cursor and connection
        cursor.close()
        conection.close()


@profesor.delete('/profesores/{rut}')
async def deleteProfesores(rut: str):
    try:
        # Check if the professor exists
        cursor.execute('SELECT * FROM profesor WHERE rut_prof = :rut', [rut])
        existing_professor = cursor.fetchone()
        if not existing_professor:
            # Return an error if the professor does not exist
            return {"error": "El profesor no existe"}, 404

        # Delete the professor from the database
        cursor.execute('DELETE FROM profesor WHERE rut_prof = :rut', [rut])
        conection.commit()

        # Return a success message
        return 'Profesor eliminado'
    finally:
        # Close the cursor and connection
        cursor.close()
        conection.close()


