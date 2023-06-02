from email.policy import default
from enum import unique
import flask
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
base = declarative_base() 
motor = create_engine("mysql://root:@localhost/alchemy")
class User(base):
    __tablename__ = "users"
    id = Column(Integer(), primary_key = True)
    Username =  Column(String(50), nullable = False, unique = True)
    mail =  Column(String(50), nullable = False, unique = True)
    def __str__(self):
        return self.Username

sesion = sessionmaker(motor)
sesion1 = sesion()
if __name__ == "__main__":
    base.metadata.drop_all(motor)
    base.metadata.create_all(motor)
    user1 = User(Username = "Mateo", mail = "mateo@gmail.com")
    user2 = User(Username = "lucas", mail = "lucas@gmail.com")
    sesion1.add(user1)
    sesion1.add(user2)
    sesion1.commit()

    vari = sesion1.query(User).filter(
        User.id > 100
    ).first()
    if vari:
        print(vari)
    else:
        print("Nooooo")

