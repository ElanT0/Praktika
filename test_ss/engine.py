from sqlalchemy import create_engine, text
from sqlalchemy.orm import create_session

engine = create_engine("postgresql+psycopg2://postgres:1337@localhost/test")
session = create_session(bind=engine)

def add_data(login, password):
    session.execute (text(f"INSERT INTO public.db(login, password) VALUES ('{login}', '{password}') "))
    session.commit()
    session.close()