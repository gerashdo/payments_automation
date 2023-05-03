from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.db import Base

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))

    payments = relationship("Payment", back_populates="client")

