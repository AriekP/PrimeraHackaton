from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.empleado import (
    Empleado, EmpleadoCreacion, EmpleadoActualizacion
)
from app.crud.empleado import (
    crear_empleado, obtener_empleado,
    listar_empleados, actualizar_empleado,
    eliminar_empleado
)

router = APIRouter()

@router.post("/", response_model=Empleado)
def alta_empleado(emp: EmpleadoCreacion, db: Session = Depends(get_db)):
    return crear_empleado(db, emp)

@router.get("/{emp_id}", response_model=Empleado)
def leer_empleado(emp_id: int, db: Session = Depends(get_db)):
    emp = obtener_empleado(db, emp_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return emp

@router.get("/", response_model=list[Empleado])
def leer_empleados(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return listar_empleados(db, skip, limit)

@router.put("/{emp_id}", response_model=Empleado)
def modificar_empleado(emp_id: int, datos: EmpleadoActualizacion, db: Session = Depends(get_db)):
    emp = actualizar_empleado(db, emp_id, datos)
    if not emp:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return emp

@router.delete("/{emp_id}", response_model=Empleado)
def baja_empleado(emp_id: int, db: Session = Depends(get_db)):
    emp = eliminar_empleado(db, emp_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return emp
