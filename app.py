from fastapi import FastAPI

from routes.payments import payments
from config.db import engine
from models.client import Base as ClientBase
from models.provider import Base as ProviderBase
from models.payment import Base as PaymentBase

ClientBase.metadata.create_all(bind=engine)
ProviderBase.metadata.create_all(bind=engine)
PaymentBase.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(payments)