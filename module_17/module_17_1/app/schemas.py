from pydantic import BaseModel


class CreateUser(BaseModel):
    username: str
    lastname: str
    firstname: str
    age: int


class UpdateUser(BaseModel):
    firstname: str
    firstname: str
    age: int


class CreateTask(BaseModel):
    title: str
    content: str
    priory: int


class UpdateTask(BaseModel):
    title: str
    content: str
    priory: int
