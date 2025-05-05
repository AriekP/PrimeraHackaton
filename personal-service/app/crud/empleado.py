from sqlalchemy.orm import Session
from app.models.empleado import Empleado
from app.schemas.empleado import EmpleadoCreacion, EmpleadoActualizacion

def crear_empleado(db: Session, datos: EmpleadoCreacion):
    emp = Empleado(**datos.dict())
    db.add(emp)
    db.commit()
    db.refresh(emp)
    return emp

def obtener_empleado(db: Session, emp_id: int):
    return db.query(Empleado).filter(Empleado.id == emp_id).first()

def listar_empleados(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Empleado).offset(skip).limit(limit).all()

def actualizar_empleado(db: Session, emp_id: int, datos: EmpleadoActualizacion):
    emp = obtener_empleado(db, emp_id)
    if not emp:
        return None
    for campo, valor in datos.dict(exclude_unset=True).items():
        setattr(emp, campo, valor)
    db.commit()
    db.refresh(emp)
    return emp

def eliminar_empleado(db: Session, emp_id: int):
    emp = obtener_empleado(db, emp_id)
    if emp:
        db.delete(emp)
        db.commit()
    return emp
