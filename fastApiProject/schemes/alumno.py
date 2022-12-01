import pydantic


class Alumno(pydantic.BaseModel):
    rut: str
    nombre: str
    apellido: str
    correo: str
