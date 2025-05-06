from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Cargo(Base):
    __tablename__ = "cargo"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)