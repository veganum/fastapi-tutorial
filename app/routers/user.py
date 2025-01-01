"""
Módulo de gestión de usuarios para una API construida con FastAPI.

Este módulo define un conjunto de endpoints relacionados con la creación, consulta, actualización y eliminación de usuarios,
utilizando una base de datos PostgreSQL.
"""

from fastapi import APIRouter, Depends, HTTPException  # type: ignore
from sqlalchemy.ext.asyncio import AsyncSession  # type: ignore
from sqlalchemy.future import select  # type: ignore
from app.schemas import User  # Esquemas Pydantic # type: ignore
from app.models.user import UserModel  # Modelo SQLAlchemy
from app.core.database import get_db  # Sesión de base de datos

# Configuración del router
router = APIRouter(
    prefix="/user",
    tags=["Users"],
)


# ? CONSULTAR
@router.get("/users", summary="Obtener todos los usuarios")
async def obtener_usuarios(db: AsyncSession = Depends(get_db)):
    """Devuelve todos los usuarios en la base de datos."""
    result = await db.execute(select(UserModel))
    usuarios = result.scalars().all()
    return {"usuarios": usuarios}


@router.get("/user/{id}", summary="Obtener un usuario por ID")
async def obtener_usuario_por_id(user_id: int, db: AsyncSession = Depends(get_db)):
    """Devuelve un usuario específico por su ID."""
    usuario = await db.get(UserModel, user_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"usuario": usuario}


# ? CREAR
@router.post("/create", summary="Crear un nuevo usuario")
async def crear_usuario(user: User, db: AsyncSession = Depends(get_db)):
    """Crea un nuevo usuario en la base de datos."""
    nuevo_usuario = UserModel(**user.dict())
    db.add(nuevo_usuario)
    await db.commit()
    await db.refresh(nuevo_usuario)
    return {"usuario": nuevo_usuario}


# ? ACTUALIZAR
@router.put("/update/{id}", summary="Actualizar un usuario existente")
async def actualizar_usuario(
    user_id: int, user: User, db: AsyncSession = Depends(get_db)
):
    """Actualiza los datos de un usuario existente."""
    usuario = await db.get(UserModel, user_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    for key, value in user.dict().items():
        setattr(usuario, key, value)
    await db.commit()
    await db.refresh(usuario)
    return {"usuario": usuario}


# ? BORRAR
@router.delete("/delete/{id}", summary="Eliminar un usuario")
async def eliminar_usuario(user_id: int, db: AsyncSession = Depends(get_db)):
    """Elimina un usuario por su ID."""
    usuario = await db.get(UserModel, user_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    await db.delete(usuario)
    await db.commit()
    return {"message": "Usuario eliminado correctamente"}
