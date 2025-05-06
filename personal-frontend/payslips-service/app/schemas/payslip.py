from pydantic import BaseModel
from datetime import datetime

class PayslipBase(BaseModel):
    employee_id: int
    period_month: int
    period_year: int
    base_salary: float
    deductions: float = 0.0

class PayslipCreate(PayslipBase):
    pass

class Payslip(PayslipBase):
    id: int
    net_pay: float
    generated_at: datetime

    class Config:
        orm_mode = True