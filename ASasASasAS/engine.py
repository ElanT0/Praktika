from sqlalchemy import create_engine, text,select
from sqlalchemy.orm import Session

engine = create_engine("postgresql+psycopg2://postgres:univer@localhost/Auth")
session = Session(bind=engine)
# base = declarative_base()

# class LoginWindow(base):
#     __tabelname__ = "Auth"
#     id = Column(Integer, Identity(True), primary_key=True)
#     login = Column(String, nullable=False)
#     password = Column(String, nullable=False)

# base.metadata.create_all(engine)