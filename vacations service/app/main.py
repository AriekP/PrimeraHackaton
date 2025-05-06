from fastapi import FastAPI
from app.database import Base, engine

app = FastAPI(title="Vacations Service")

# Importa los modelos después de crear la app pero antes de create_all
from app.models import vacaciones, funcionario, area, cargo

# Crea todas las tablas
Base.metadata.create_all(bind=engine)

# Importa el router después de los modelos
from app.routes import vacaciones_router
app.include_router(vacaciones_router)

@app.get("/")
def read_root():
    return {"message": "Vacations Service is running"}