from fastapi import FastAPI
from app.database import Base, engine
from app.routes.empleado import router as empleado_router
from app.routes.contrato import router as contrato_router
from fastapi.middleware.cors import CORSMiddleware 

# Crea tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="HR-Core Service",
    description="Gestión de empleados y contratos",
    version="0.1.0"
)
# --- CORS middleware -----------------------------------
origins = [
    "http://localhost:5173",   # la URL de tu front
    # si en dev usas otro host/puerto, agrégalo aquí
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],       # GET, POST, PUT, DELETE…
    allow_headers=["*"],       # Content-Type, Authorization…
)
# -------------------------------------------------------
app.include_router(empleado_router, prefix="/empleados", tags=["Empleados"])
app.include_router(contrato_router, prefix="/contratos", tags=["Contratos"])
