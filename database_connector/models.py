from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.sql.expression import false, null
from sqlalchemy.sql.sqltypes import Boolean

Base=declarative_base()

class User(Base):
    __tablename__='users'
    telegram_id=Column(Integer, primary_key=True)
    user_name=Column(String(200), nullable=False, unique=True)
    
    gender=Column(Integer, )
    first_name=Column(String(200), nullable=False)
    last_name=Column(String(200), nullable=False)
    email=Column(String(200), nullable=False, unique=True)
    phone_number=Column(String)
    
    biography=Column(String)
    
    problems=Column(String)

    position_actual=Column(String)
    position_desired=Column(String)

    initial_questions=Column(String)

    image_uploaded=Column(Boolean)

    def __repr__(self) -> str:
        return super().__repr__()

        

