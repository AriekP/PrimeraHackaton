from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.payslip import PayslipCreate, Payslip
from app.crud.payslip import create_payslip, get_all_payslips, get_by_employee
from typing import List

router = APIRouter(prefix="/payslips", tags=["payslips"])

@router.post("/", response_model=Payslip)
def create(data: PayslipCreate, db: Session = Depends(get_db)):
    return create_payslip(db, data)

@router.get("/", response_model=List[Payslip])
def all(db: Session = Depends(get_db)):
    return get_all_payslips(db)

@router.get("/employee/{employee_id}", response_model=List[Payslip])
def by_employee(employee_id: int, db: Session = Depends(get_db)):
    return get_by_employee(db, employee_id)