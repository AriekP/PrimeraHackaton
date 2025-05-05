from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database import get_db
from app.schemas.contrato import Contrato, ContratoCreacion
from app.crud.contrato import crear_contrato, obtener_contrato, listar_contratos
from app.crud.empleado import obtener_empleado  # <-- importar validación

router = APIRouter()

@router.post("/", response_model=Contrato)
def alta_contrato(data: ContratoCreacion, db: Session = Depends(get_db)):
    # 1) Validar que exista el empleado
    empleado = obtener_empleado(db, data.empleado_id)
    if not empleado:
        raise HTTPException(
            status_code=400,
            detail=f"Empleado con id={data.empleado_id} no existe"
        )

    # 2) Crear contrato y capturar violaciones de FK o integridad
    try:
        return crear_contrato(db, data)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="No se pudo crear el contrato (violación de integridad)"
        )

@router.get("/{ctr_id}", response_model=Contrato)
def leer_contrato(ctr_id: int, db: Session = Depends(get_db)):
    ctr = obtener_contrato(db, ctr_id)
    if not ctr:
        raise HTTPException(status_code=404, detail="Contrato no encontrado")
    return ctr

@router.get("/", response_model=list[Contrato])
def leer_contratos(
    empleado_id: int | None = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return listar_contratos(db, empleado_id, skip, limit)
