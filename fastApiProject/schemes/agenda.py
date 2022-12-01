import pydantic
from datetime import datetime


class Agenda(pydantic.BaseModel):
    rut_prof: str
    id_clas: int
    cant_alum_pres: int
    fecha_clase: datetime
