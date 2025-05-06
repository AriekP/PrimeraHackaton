from sqlalchemy.orm import Session
from app.models.payslip import Payslip
from app.schemas.payslip import PayslipCreate

def create_payslip(db: Session, data: PayslipCreate):
    net = data.base_salary - data.deductions
    new = Payslip(**data.dict(), net_pay=net)
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

def get_all_payslips(db: Session):
    return db.query(Payslip).all()

def get_by_employee(db: Session, employee_id: int):
    return db.query(Payslip).filter(Payslip.employee_id == employee_id).all()