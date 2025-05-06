from sqlalchemy.orm import Session
from datetime import date, timedelta
from app.models.vacaciones import Vacaciones
from app.models.funcionario import Funcionario  # Importa el modelo Funcionario
from app.schemas.vacaciones import VacacionesCreate

def calcular_vacaciones(db: Session, id_funcionario: int):
    funcionario = db.query(Funcionario).filter(Funcionario.id == id_funcionario).first()
    if not funcionario:
        return None
    
    antiguedad = date.today() - funcionario.fecha_ingreso
    if antiguedad.days < 365:
        return None  # No cumple el año de antigüedad
    
    return {
        "dias": 15,
        "fecha_fin": date.today() + timedelta(days=15)
    }

def crear_vacacion(db: Session, vacacion: VacacionesCreate):
    # Verificar antigüedad
    funcionario = db.query(Funcionario).filter(Funcionario.id == vacacion.id_funcionario).first()
    if not funcionario or (date.today() - funcionario.fecha_ingreso).days < 365:
        return None
    
    db_vacacion = Vacaciones(
        id_funcionario=vacacion.id_funcionario,
        fecha_inicio=vacacion.fecha_inicio,
        fecha_fin=vacacion.fecha_fin,
        dias=15,  # Fijo según requerimiento
        gestion_completada=vacacion.gestion_completada,
        estado="SOLICITADO"
    )
    db.add(db_vacacion)
    db.commit()
    db.refresh(db_vacacion)
    return db_vacacion