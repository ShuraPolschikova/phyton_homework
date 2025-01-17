from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/")
async def welcome():
    return "с новым годом!"


@app.get("/users")
async def get_users():
    return users


@app.post("/users/{username}/{age}")
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20,
                                                 description="Enter username", examples="Shura")],
                       age: Annotated[int, Path(ge=18, le=120, description="Enter age from 18 to 120",
                                                examples="28")]):
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'


@app.put("/users/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID from 1 to 100")],
                      username: Annotated[str, Path(min_length=5, max_length=20,
                                                    description="Enter username", examples="Shura")],
                       age: Annotated[int, Path(ge=18, le=120, description="Enter age from 18 to 120",
                                                examples="28")]):
    user_id = str(user_id)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"

@app.delete("/user/{user_id}")
def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID from 1 to 100")]):
    user_id = str(user_id)
    del users[user_id]
    return f"User {user_id} has been deleted"
