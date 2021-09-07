from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# MySQL - didn't work when creating the model, yielded cryptic Python failure
engine = create_engine("postgresql+psycopg2://USER:PASSWORD@localhost:5432/DBNAME")
Session = sessionmaker(bind=engine)

Base = declarative_base()

