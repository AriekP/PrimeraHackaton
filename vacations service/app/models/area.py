from sqlalchemy import Column, Integer, String
from app.database import Base

class Area(Base):
    __tablename__ = "area"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)