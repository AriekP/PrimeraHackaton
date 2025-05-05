from fastapi import FastAPI
from app.database import Base, engine
from app.routes.empleado import router as empleado_router
from app.routes.contrato import router as contrato_router

# Crea tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="HR-Core Service",
    description="Gestión de empleados y contratos",
    version="0.1.0"
)

app.include_router(empleado_router, prefix="/empleados", tags=["Empleados"])
app.include_router(contrato_router, prefix="/contratos", tags=["Contratos"])
