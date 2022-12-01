import pydantic


class Asignatura(pydantic.BaseModel):
    id: int
    nombre: str
