from sqlalchemy.orm import Session
from app.models.contrato import Contrato
from app.schemas.contrato import ContratoCreacion

def crear_contrato(db: Session, datos: ContratoCreacion):
    ctr = Contrato(**datos.dict())
    db.add(ctr)
    db.commit()
    db.refresh(ctr)
    return ctr

def obtener_contrato(db: Session, ctr_id: int):
    return db.query(Contrato).filter(Contrato.id == ctr_id).first()

def listar_contratos(db: Session, empleado_id: int = None, skip: int = 0, limit: int = 100):
    q = db.query(Contrato)
    if empleado_id:
        q = q.filter(Contrato.empleado_id == empleado_id)
    return q.offset(skip).limit(limit).all()
