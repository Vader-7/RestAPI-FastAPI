import pydantic


class Profesor(pydantic.BaseModel):
    rut: str
    nombre: str
    apellido: str
    correo: str
