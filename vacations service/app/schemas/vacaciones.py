from pydantic import BaseModel, validator
from datetime import date
from enum import Enum
from typing import Optional

class EstadoVacaciones(str, Enum):
    SOLICITADO = "SOLICITADO"
    APROBADO = "APROBADO"
    RECHAZADO = "RECHAZADO"
    GOZADO = "GOZADO"

class VacacionesBase(BaseModel):
    id_funcionario: int
    fecha_inicio: date
    fecha_fin: date
    gestion_completada: Optional[bool] = False

class VacacionesCreate(VacacionesBase):
    pass

class VacacionesResponse(VacacionesBase):
    id: int
    dias: int
    estado: EstadoVacaciones
    
    class Config:
        from_attributes = True