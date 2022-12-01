import pydantic


class Curso(pydantic.BaseModel):
    nombre: str
    codigo: str
    credito: int

    class Config:
        orm_mode = True
