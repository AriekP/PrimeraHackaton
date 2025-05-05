from sqlalchemy import (
    Column, Integer, Date, DECIMAL, String,
    DateTime, ForeignKey
)
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Contrato(Base):
    __tablename__ = "contratos"

    id               = Column(Integer, primary_key=True, index=True)
    empleado_id      = Column(
        Integer,
        ForeignKey("empleados.id", ondelete="RESTRICT", onupdate="CASCADE"),
        nullable=False,
        index=True,
        comment="FK a empleados.id"
    )
    fecha_inicio     = Column(Date, nullable=False)
    salario          = Column(DECIMAL(10,2), nullable=False)
    periodo_prueba   = Column(Integer, nullable=False)
    ruta_plantilla   = Column(String(255), nullable=True)
    fecha_creado     = Column(DateTime, default=datetime.utcnow)

    # Opcional: relación ORM para poder usar contrato.empleado
    empleado = relationship(
        "Empleado",
        back_populates="contratos",
        innerjoin=True
    )
