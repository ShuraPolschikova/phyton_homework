from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List
from pydantic import BaseModel


app = FastAPI()
users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/")
async def welcome():
    return "с новым годом!"


@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post("/users/{username}/{age}", response_model=User)
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20,
                                                 description="Enter username", examples="Shura")],
                       age: Annotated[int, Path(ge=18, le=120, description="Enter age from 18 to 120",
                                                examples="28")]):
    new_id = max((user.id for user in users), default=0)+1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/users/{user_id}/{username}/{age}", response_model=User)
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID from 1 to 100")],
                      username: Annotated[str, Path(min_length=5, max_length=20,
                                                    description="Enter username", examples="Shura")],
                       age: Annotated[int, Path(ge=18, le=120, description="Enter age from 18 to 120",
                                                examples="28")]):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
        else:
            raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}", response_model=User)
def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID from 1 to 100")]):
    for i, user in enumerate(users):
        if user.id == user_id:
            return users.pop(i)
    raise HTTPException(status_code=404, detail="User was not found")
