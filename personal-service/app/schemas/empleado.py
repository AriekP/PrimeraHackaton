from pydantic import BaseModel, condecimal
from datetime import date

class EmpleadoBase(BaseModel):
    nombre: str
    apellido: str
    area: str
    cargo: str
    salario: condecimal(max_digits=10, decimal_places=2)
    fecha_ingreso: date
    activo: bool = True

class EmpleadoCreacion(EmpleadoBase):
    pass

class EmpleadoActualizacion(BaseModel):
    area: str | None = None
    cargo: str | None = None
    salario: condecimal(max_digits=10, decimal_places=2) | None = None
    activo: bool | None = None

class Empleado(EmpleadoBase):
    id: int

    class Config:
        from_attributes = True
