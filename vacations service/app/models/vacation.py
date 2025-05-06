from sqlalchemy import Column, Integer, Date, ForeignKey, Enum, Boolean
from sqlalchemy.orm import relationship
from app.database import Base
from enum import Enum as PyEnum

class EstadoVacaciones(PyEnum):
    SOLICITADO = "SOLICITADO"
    APROBADO = "APROBADO"
    RECHAZADO = "RECHAZADO"
    GOZADO = "GOZADO"

class Vacaciones(Base):
    __tablename__ = "vacaciones"
    
    id = Column(Integer, primary_key=True, index=True)
    id_funcionario = Column(Integer, ForeignKey("funcionario.id"), nullable=False)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)
    dias = Column(Integer, nullable=False)
    estado = Column(Enum(EstadoVacaciones), default=EstadoVacaciones.SOLICITADO)
    gestion_completada = Column(Boolean, default=False)
    
    funcionario = relationship("Funcionario", back_populates="vacaciones")