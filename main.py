from fastapi import FastAPI  # type: ignore
import uvicorn  # type: ignore
from app.routers import user

app = FastAPI()
app.include_router(user.router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
