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
    @validator('dias')
    def validar_dias(cls, v, values):
        if v != 15:
            raise ValueError("Las vacaciones deben ser exactamente 15 días por gestión")
        return v

class VacacionesResponse(VacacionesBase):
    id: int
    dias: int
    estado: EstadoVacaciones
    
    class Config:
        from_attributes = True