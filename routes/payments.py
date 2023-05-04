from fastapi import Depends
from fastapi.responses import StreamingResponse
from io import BytesIO
from sqlalchemy.orm import Session
from fastapi import APIRouter

from config.db import SessionLocal
import controllers.payments as payments_controller
import schemas.payment as payment_schema


payments = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@payments.get("/payments/total", response_model=payment_schema.TotalPayments)
def get_total_payments(db: Session = Depends(get_db)):
    total = payments_controller.get_payments_total(db)
    return {"total": total}


@payments.get("/payments/download", response_model=payment_schema.DownloadPayments)
def download_payments_xlsx(db: Session = Depends(get_db)):
    file = payments_controller.create_xlsx_payments_file(db)

    headers = {"Content-Disposition": f"attachment; filename=payments.xlsx"}

    return StreamingResponse(
        BytesIO(file.getvalue()),
        media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        headers=headers
    )
