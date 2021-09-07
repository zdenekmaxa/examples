"""
SQLAlchemy experiment 2021-09-07

Didn't work with MySQL database, failed with cryptic Python failure
    when creating the table (model). With PyMySQL 1.0.2
Worked out-of-the-box with PostgreSQL+psycopg2 - model created, entity
    inserted.

Source: https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/

"""
from datetime import date

from base import Session, engine, Base
from movie import Movie

Base.metadata.create_all(engine)
session = Session()

bourne_identity = Movie("The Bourne Identity", date(2002, 10, 11))
session.add(bourne_identity)
session.commit()
session.close()

