import pydantic


class Clase(pydantic.BaseModel):
    id_clas: int
    horario_ini: str
    horario_fin: str
    id_asig: int
