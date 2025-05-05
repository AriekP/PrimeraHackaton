# app/models/empleado.py

from sqlalchemy import Column, Integer, String, Date, Boolean, DECIMAL, DateTime
from sqlalchemy.orm import relationship          # ← ¡No lo olvides!
from app.database import Base
from datetime import datetime

class Empleado(Base):
    __tablename__ = "empleados"

    id                = Column(Integer, primary_key=True, index=True)
    nombre            = Column(String(100), nullable=False)
    apellido          = Column(String(100), nullable=False)
    area              = Column(String(100), nullable=False)
    cargo             = Column(String(100), nullable=False)
    salario           = Column(DECIMAL(10,2), nullable=False)
    fecha_ingreso     = Column(Date, nullable=False)
    activo            = Column(Boolean, default=True)
    fecha_creado      = Column(DateTime, default=datetime.utcnow)
    fecha_actualizado = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    # Relación inversa: Empleado.contratos
    contratos = relationship(
        "Contrato",
        back_populates="empleado",
        cascade="all, delete-orphan"
    )
