from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine  # type: ignore
from sqlalchemy.orm import sessionmaker  # type: ignore
from sqlalchemy.ext.declarative import declarative_base  # type: ignore

# URL de conexión a PostgreSQL
DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost:5432/mydatabase"

# Configuración del motor de base de datos
engine = create_async_engine(DATABASE_URL, echo=True)

# Creación de sesiones
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
)

# Base declarativa para los modelos
Base = declarative_base()


# Generador de sesiones para FastAPI
async def get_db():
    async with SessionLocal() as session:
        yield session
