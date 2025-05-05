from pydantic import BaseModel, condecimal
from datetime import date

class ContratoBase(BaseModel):
    empleado_id: int
    fecha_inicio: date
    salario: condecimal(max_digits=10, decimal_places=2)
    periodo_prueba: int
    ruta_plantilla: str | None = None

class ContratoCreacion(ContratoBase):
    pass

class Contrato(ContratoBase):
    id: int

    class Config:
        from_attributes = True
