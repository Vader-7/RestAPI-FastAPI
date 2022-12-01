from fastapi import APIRouter
from schemes.agenda import Agenda
from configbs.db import cursor
from configbs.db import conection
agenda = APIRouter()

@agenda.get('/agenda')
async def getAgenda():
    return cursor.execute('SELECT * FROM agenda').fetchall(), 'Agenda obtenida'


@agenda.post('/agenda')
async def postAgenda(agenda: Agenda):
    cursor.execute('INSERT INTO agenda(rut_prof, id_clas, cant_alum_pres, fecha_clase) VALUES(:rut_prof, :id_clas, :cant_alum_pres, :fecha_clase)', agenda.dict())
    conection.commit()
    return agenda.dict(), 'Agenda creada'


@agenda.put('/agenda/{id}')
async def putAgenda(id: str, agenda: Agenda):
    cursor.execute('UPDATE agenda SET rut_prof = :rut_prof, id_clas = :id_clas, cant_alum_pres = :cant_alum_pres, fecha_clase = :fecha_clase WHERE id_clas = :id', [agenda.rut_prof, agenda.id_clas, agenda.cant_alum_pres, agenda.fecha_clase, id])
    conection.commit()
    return agenda.dict(), 'Agenda actualizada'


@agenda.delete('/agenda/{id}')
async def deleteAgenda(id: str):
    cursor.execute('DELETE FROM agenda WHERE id_clas = :id', [id])
    conection.commit()
    return 'Agenda eliminada'

