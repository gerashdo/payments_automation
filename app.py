from fastapi import FastAPI

from routes.payments import payments
from config.db import engine
from models.client import Base as ClientBase
from models.provider import Base as ProviderBase
from models.payment import Base as PaymentBase

ClientBase.metadata.create_all(bind=engine)
ProviderBase.metadata.create_all(bind=engine)
PaymentBase.metadata.create_all(bind=engine)

app = FastAPI(
    title="Payments API",
    description='API for payments management.',
    version="0.0.1",
    openapi_tags=[{
        "name": "payments",
        "description": "Payments endpoints."
    }]
)

app.include_router(payments)
