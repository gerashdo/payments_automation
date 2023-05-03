
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:Stoker.3@localhost:3306/payment_project"

engine = create_engine( SQLALCHEMY_DATABASE_URL )

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()