import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .db_settings import *


# mysql+mysqlconnector://pyuser:s3cr37@localhost:33006/carparts
engine = sqlalchemy.create_engine(
    f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}',
    echo=False
)

Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
