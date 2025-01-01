from sqlalchemy import Column, Integer, String, DateTime  # type: ignore
from datetime import datetime
from app.core.database import Base


class UserModel(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    direccion = Column(String, nullable=True)
    telefono = Column(Integer, nullable=False)
    creacion_user = Column(DateTime, default=datetime.now)
