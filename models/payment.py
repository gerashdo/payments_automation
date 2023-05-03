from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from config.db import Base, engine

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer)
    date = Column(DateTime)
    client_id = Column(Integer, ForeignKey("clients.id"))
    provider_id = Column(Integer, ForeignKey("providers.id"))

    client = relationship("Client", back_populates="payments")
    provider = relationship("Provider", back_populates="payments")

Base.metadata.create_all(bind=engine)