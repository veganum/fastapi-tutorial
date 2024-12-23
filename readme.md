# Ejemplo FastAPI

Este proyecto es un ejemplo básico de cómo iniciar un proyecto con FastAPI.

## Requisitos básicos

Asegúrate de tener los siguientes requisitos instalados antes de comenzar:

1. Python 3.8 o superior.
2. FastAPI:

   ```bash
   pip install fastapi


## Ejecución

Dos formas de ejecutar Fastapi

1. Ejecutar con uvicorn:

   ```bash
   uvicorn main:app
   ```

2. Agregar las líneas de código:

   ```python
   if __name__ == "__main__":
       uvicorn.run("main:app", port=8000)
   ```

   Y luego correr main.py
