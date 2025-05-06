from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship  # Asegúrate de tener esta importación
from app.database import Base

class Funcionario(Base):
    __tablename__ = "funcionario"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    ci = Column(String(20), unique=True, nullable=False)
    fecha_nacimiento = Column(Date)
    fecha_ingreso = Column(Date, nullable=False)
    estado = Column(Enum('ACTIVO', 'INACTIVO'), default='ACTIVO')
    id_area = Column(Integer, ForeignKey("area.id"))
    id_cargo = Column(Integer, ForeignKey("cargo.id"))
    remuneracion = Column(Integer)

    vacaciones = relationship("Vacaciones", back_populates="funcionario")   