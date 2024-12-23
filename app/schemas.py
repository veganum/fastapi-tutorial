from pydantic import BaseModel  # type: ignore
from typing import Optional  # type: ignore
from datetime import datetime


class User(BaseModel):  # Schema
    id: int
    nombre: str
    apellido: str
    direccion: Optional[str]
    telefono: int
    creacion_user: datetime = datetime.now()


class UserId(BaseModel):
    id: int
