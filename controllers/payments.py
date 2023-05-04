from io import BytesIO
import pandas as pd
from sqlalchemy import func
from sqlalchemy.orm import Session

from models.payment import Payment

from helpers.payments import create_payments_dataframe


def get_payments_total(db: Session):
    return db.query(func.sum(Payment.amount)).scalar()


def get_all_payments(db: Session):
    return db.query(Payment).all()


def create_xlsx_payments_file(db: Session):
    payments = get_all_payments(db)

    dataframe = create_payments_dataframe(payments)

    print(dataframe)

    buffer = BytesIO()
    with pd.ExcelWriter(buffer) as writer:
        dataframe.to_excel(writer, index=False)

    return buffer
