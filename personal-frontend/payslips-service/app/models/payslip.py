from sqlalchemy import Column, Integer, DECIMAL, DateTime, ForeignKey
from datetime import datetime
from app.database import Base

class Payslip(Base):
    __tablename__ = "payslips"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, nullable=False)
    period_month = Column(Integer, nullable=False)
    period_year = Column(Integer, nullable=False)
    base_salary = Column(DECIMAL(10, 2), nullable=False)
    deductions = Column(DECIMAL(10, 2), default=0.00)
    net_pay = Column(DECIMAL(10, 2), nullable=False)
    generated_at = Column(DateTime, default=datetime.utcnow)