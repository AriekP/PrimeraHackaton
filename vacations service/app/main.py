from fastapi import FastAPI
from app.routes import vacaciones_router
from app.database import Base, engine

app = FastAPI(
    title="ARCA RRHH - Vacaciones Service",
    description="Microservicio para gestión de vacaciones del personal",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)
app.include_router(vacaciones_router)

@app.get("/")
def read_root():
    return {"message": "ARCA RRHH - Vacaciones Service"}