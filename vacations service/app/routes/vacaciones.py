from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.vacaciones import VacacionesCreate, VacacionesResponse
from app.crud import vacaciones as crud_vacaciones

router = APIRouter(prefix="/api/vacaciones", tags=["vacaciones"])

@router.post("/", response_model=VacacionesResponse)
def solicitar_vacacion(vacacion: VacacionesCreate, db: Session = Depends(get_db)):
    db_vacacion = crud_vacaciones.crear_vacacion(db, vacacion)
    if not db_vacacion:
        raise HTTPException(
            status_code=400,
            detail="El funcionario no cumple con el año de antigüedad requerido"
        )
    return db_vacacion

@router.get("/calcular/{id_funcionario}")
def calcular_dias_vacaciones(id_funcionario: int, db: Session = Depends(get_db)):
    resultado = crud_vacaciones.calcular_vacaciones(db, id_funcionario)
    if not resultado:
        raise HTTPException(
            status_code=400,
            detail="No cumple requisitos para vacaciones"
        )
    return resultado