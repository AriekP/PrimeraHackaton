from fastapi import FastAPI
from app.database import Base, engine
from app.routes.payslip import router as payslip_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Payslip Microservice")

# Primero creas la app, luego le aplicas middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes restringir a ["http://localhost:5173"] si quieres más seguridad
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear las tablas si no existen
Base.metadata.create_all(bind=engine)

# Incluir el router
app.include_router(payslip_router)