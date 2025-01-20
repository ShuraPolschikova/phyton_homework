from sqlalchemy import Column, Integer, String
from module_17.module_17_1.app.backend.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(Integer)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    tasks = relationship("Task", back_populates="user")

if __name__ == "__main__":
    print(CreateTable(User.__table__))