"""
Módulo de gestión de usuarios para una API construida con FastAPI.

Este módulo define un conjunto de endpoints relacionados con la creación, consulta, actualización y eliminación de usuarios.
Utiliza un conjunto de datos en memoria para simular una base de datos.

Importaciones:
- `APIRouter`: Clase de FastAPI para definir rutas agrupadas con prefijo.
- `User`, `UserId`: Esquemas de datos utilizados para validar y estructurar las solicitudes y respuestas.
"""

from fastapi import APIRouter  # type: ignore
from app.schemas import User, UserId  # type: ignore

# Configuración del router
router = APIRouter(
    prefix="/user",  # Prefijo común para todas las rutas en este módulo.
    tags=["Users"],  # Categoría para la documentación generada.
)

# Lista de usuarios (simulación de base de datos)
users = [
    {
        "id": 0,
        "nombre": "José",
        "apellido": "Franco Nieto",
        "direccion": "C/ Algaba nº 22 3ºC",
        "telefono": 670302349,
        "creacion_user": "2024-12-23T20:36:59.613695",
    },
    {
        "id": 1,
        "nombre": "Bozhidara",
        "apellido": "Angelova Nedyalkova",
        "direccion": "C/ Antonio Prieto nº 50 1ºA",
        "telefono": 670302349,
        "creacion_user": "2024-12-23T20:36:59.613695",
    },
    {
        "id": 2,
        "nombre": "Alejandro",
        "apellido": "García López",
        "direccion": "C/ Gran Vía nº 10 2ºB",
        "telefono": 680123456,
        "creacion_user": "2024-12-23T21:00:00.000000",
    },
    {
        "id": 3,
        "nombre": "Lucía",
        "apellido": "Martínez Sánchez",
        "direccion": "C/ Alcalá nº 15 Bajo A",
        "telefono": 690234567,
        "creacion_user": "2024-12-23T21:15:00.000000",
    },
    {
        "id": 4,
        "nombre": "Carlos",
        "apellido": "Hernández Gómez",
        "direccion": "C/ Serrano nº 45 3ºC",
        "telefono": 670345678,
        "creacion_user": "2024-12-23T21:30:00.000000",
    },
    {
        "id": 5,
        "nombre": "María",
        "apellido": "Ruiz Fernández",
        "direccion": "C/ Velázquez nº 3 1ºA",
        "telefono": 660456789,
        "creacion_user": "2024-12-23T21:45:00.000000",
    },
    {
        "id": 6,
        "nombre": "David",
        "apellido": "Pérez Torres",
        "direccion": "C/ Castellana nº 50 5ºD",
        "telefono": 650567890,
        "creacion_user": "2024-12-23T22:00:00.000000",
    },
    {
        "id": 7,
        "nombre": "Elena",
        "apellido": "López Morales",
        "direccion": "C/ Hortaleza nº 100 4ºB",
        "telefono": 640678901,
        "creacion_user": "2024-12-23T22:15:00.000000",
    },
    {
        "id": 8,
        "nombre": "Miguel",
        "apellido": "Gómez Martín",
        "direccion": "C/ Princesa nº 20 Bajo B",
        "telefono": 630789012,
        "creacion_user": "2024-12-23T22:30:00.000000",
    },
    {
        "id": 9,
        "nombre": "Ana",
        "apellido": "Díaz Ramírez",
        "direccion": "C/ Mayor nº 80 2ºC",
        "telefono": 620890123,
        "creacion_user": "2024-12-23T22:45:00.000000",
    },
    {
        "id": 10,
        "nombre": "Pablo",
        "apellido": "Vega Serrano",
        "direccion": "C/ Atocha nº 15 1ºD",
        "telefono": 610901234,
        "creacion_user": "2024-12-23T23:00:00.000000",
    },
]

# ? CONSULTAR
@router.get(
    "/ruta1",
    summary="Mensaje de bienvenida",
    description="Devuelve un mensaje de bienvenida para verificar el funcionamiento de la API.",
)
def ruta1():
    return {"mensaje": "Bienvenido a tu primera api"}


@router.get(
    "/users",
    summary="Obtener todos los usuarios",
    description="Devuelve una lista completa de todos los usuarios registrados en el sistema.",
)
def obtener_usuarios():
    return users


@router.get(
    "/user/{id}",
    summary="Obtener un usuario por ID",
    description="Busca y devuelve un usuario específico por su ID. Si no se encuentra, devuelve un mensaje de error.",
)
def obtener_usuario_por_id(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return {"usuario": user}
    return {"response": "Usuario no encontrado!!"}


# ? CREAR O GRABAR
@router.post(
    "/postUser",
    summary="Crear un nuevo usuario",
    description="Recibe un objeto de tipo `User` y lo agrega a la lista de usuarios registrados.",
    response_model=dict,
)
def crear_usuario(user: User):
    usuario = user.dict()
    users.append(usuario)
    return {"response": "Usuario creado exitosamente"}


@router.post(
    "/postUserById/{id}",
    summary="Crear un usuario por ID",
    description="Busca un usuario existente por su ID y lo devuelve. Si no se encuentra, devuelve un mensaje de error.",
    response_model=dict,
)
def crear_usuario_por_id(user_id: UserId):
    for user in users:
        if user["id"] == user_id:
            return {"usuario": user}
    return {"response": "Usuario no encontrado!!"}


# ? ACTUALIZAR
@router.put(
    "/user/{id}",
    summary="Actualizar un usuario existente",
    description="Busca un usuario por su ID y actualiza sus datos con los proporcionados en el objeto `User`.",
    response_model=dict,
)
def actualizar_usuario(user_id: int, user: User):
    for index, usuario in enumerate(users):
        if usuario["id"] == user_id:
            users[index] = user.dict()
            return {"response": "Usuario actualizado correctamente"}
    return {"response": "Usuario no encontrado!!"}


# ? BORRAR
@router.delete(
    "/user/{id}",
    summary="Eliminar un usuario",
    description="Busca un usuario por su ID y lo elimina de la lista. Simula la eliminación actualizando sus datos.",
    response_model=dict,
)
def eliminar_usuario(user_id: int, updateUser: User):
    for index, usuario in enumerate(users):
        if usuario["id"] == user_id:
            # Actualización de usuario para simular eliminación
            users[index]["id"] = updateUser.dict()["id"]
            users[index]["nombre"] = updateUser.dict()["nombre"]
            users[index]["apellido"] = updateUser.dict()["apellido"]
            users[index]["direccion"] = updateUser.dict()["direccion"]
            users[index]["telefono"] = updateUser.dict()["telefono"]
            return {"response": "Usuario actualizado correctamente"}
    return {"response": "Usuario no encontrado!!"}
