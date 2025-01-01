from fastapi import FastAPI  # type: ignore
from app.routers import user
from app.core.database import Base, engine
import uvicorn  # type: ignore

app = FastAPI()

# Registrar las rutas
app.include_router(user.router, prefix="/api/v1")


# Crear tablas al iniciar la aplicación
@app.on_event("startup")
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
