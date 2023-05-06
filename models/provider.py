from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.db import Base, engine

class Provider(Base):
    __tablename__ = "providers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))

    payments = relationship("Payment", back_populates="provider")
