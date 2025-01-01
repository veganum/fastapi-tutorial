# Proyecto: Ejemplo de FastAPI

Este proyecto es un ejemplo básico de cómo iniciar un proyecto utilizando **Python** y **FastAPI**. Incluye pasos esenciales para configurar el entorno, instalar dependencias y ejecutar una aplicación FastAPI.

---

## Configuración del Entorno de Desarrollo

### Crear un Entorno Virtual

Un entorno virtual te ayuda a mantener las dependencias del proyecto aisladas:

```bash
python -m venv <nombre_del_entorno>
```

Ejemplo:

```bash
python -m venv env
```

### Activar el Entorno Virtual

En **Windows**:

```bash
env\Scripts\activate
```

En **macOS/Linux**:

```bash
source env/bin/activate
```

### Desactivar el Entorno Virtual

Cuando termines de trabajar en tu proyecto, desactiva el entorno virtual con:

```bash
deactivate
```

---

## Gestión de Dependencias

### Listar las Dependencias Instaladas

Muestra las bibliotecas instaladas en el entorno virtual:

```bash
pip freeze
```

### Guardar las Dependencias en un Archivo

Exporta las dependencias actuales a un archivo `requirements.txt` para compartirlas:

```bash
pip freeze > requirements.txt
```

### Instalar Dependencias desde un Archivo

Instala todas las dependencias listadas en `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Actualizar Pip

Es importante mantener pip actualizado para evitar problemas con instalaciones:

```bash
pip install --upgrade pip
```

### Desinstalar Paquetes

Si necesitas eliminar un paquete instalado, usa:

```bash
pip uninstall <nombre_del_paquete>
```

### Ver Información de un Paquete

Para obtener detalles sobre un paquete específico instalado:

```bash
pip show <nombre_del_paquete>
```

### Instalar una Versión Específica de un Paquete

Si necesitas instalar una versión específica de una biblioteca:

```bash
pip install <nombre_del_paquete>==<versión>
```

Ejemplo:

```bash
pip install fastapi==0.85.0
```

---

## Configuración de un Linter en Python

Para generar un archivo de configuración para **Pylint**, ejecuta el siguiente comando:

```bash
pylint --generate-rcfile > .pylintrc
```

---

## FastAPI

FastAPI es un framework moderno y de alto rendimiento para crear APIs con Python.

### Requisitos

Asegúrate de que **Python 3.8 o superior** esté instalado. Luego, instala FastAPI ejecutando:

```bash
pip install fastapi
```

También necesitarás un servidor ASGI como **Uvicorn**:

```bash
pip install uvicorn
```

---

## Ejecución de la Aplicación FastAPI

### Forma 1: Ejecutar con Uvicorn

Ejecuta el servidor con el siguiente comando:

```bash
uvicorn main:app --reload
```

- **main**: El nombre del archivo principal sin la extensión `.py`.
- **app**: El nombre de la instancia de FastAPI dentro del archivo.

### Forma 2: Código con Ejecución Directa

Añade el siguiente bloque al final de tu archivo `main.py`:

```python
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
```

Luego, ejecuta el archivo:

```bash
python main.py
```

### Documentación Interactiva

FastAPI genera automáticamente documentación interactiva en las siguientes URLs:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Validar Tu Código con `mypy`

Para verificar el tipo estático en tu proyecto FastAPI, instala `mypy` y ejecútelo:

```bash
pip install mypy
mypy main.py
```

### Ejecutar Servidor en Modo Producción

Utiliza **gunicorn** y **Uvicorn Workers** para un entorno de producción:

```bash
pip install gunicorn
```

```bash
gunicorn -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8000
```

---

## Estructura Básica de un Proyecto FastAPI

```plaintext
🗂 proyecto-fastapi/
├── 🗄 main.py        # Archivo principal con la instancia de FastAPI
├── 🗄 requirements.txt  # Dependencias del proyecto
├── 🗄 .pylintrc      # Archivo de configuración del linter
├── 🗂 env/           # Entorno virtual (excluido del control de versiones)
```

---

## Integración con Docker

### Construir y Ejecutar el Contenedor

Construye la imagen de Docker:

```bash
docker-compose build
```

Ejecuta el contenedor:

```bash
docker-compose up
```

Para detener el contenedor:

```bash
docker-compose down
```

---

## BBDD

### Script de ejecucion de usuarios

Insertar datos en la tabla usuarios

```bash
INSERT INTO usuarios (id, nombre, apellido, direccion, telefono, creacion_user)
VALUES
    (1, 'José', 'Franco Nieto', 'C/ incognito', 670302349, NOW()),
    (2, 'Bozhidara', 'Angelova Nedyalkova', 'C/ incognito', 670302349, NOW()),
    (3, 'Alejandro', 'García López', 'C/ Gran Vía nº 10 2ºB', 680123456, NOW()),
    (4, 'Lucía', 'Martínez Sánchez', 'C/ Alcalá nº 15 Bajo A', 690234567, NOW()),
    (5, 'Carlos', 'Hernández Gómez', 'C/ Serrano nº 45 3ºC', 670345678, NOW()),
    (6, 'María', 'Ruiz Fernández', 'C/ Velázquez nº 3 1ºA', 660456789, NOW()),
    (7, 'David', 'Pérez Torres', 'C/ Castellana nº 50 5ºD', 650567890, NOW()),
    (8, 'Elena', 'López Morales', 'C/ Hortaleza nº 100 4ºB', 640678901, NOW()),
    (9, 'Miguel', 'Gómez Martín', 'C/ Princesa nº 20 Bajo B', 630789012, NOW()),
    (10, 'Ana', 'Díaz Ramírez', 'C/ Mayor nº 80 2ºC', 620890123, NOW());
```

Con esta guía, puedes configurar, desarrollar y ejecutar proyectos básicos utilizando **Python**, **FastAPI** y **Docker**. ¡Listo para empezar! 🚀
