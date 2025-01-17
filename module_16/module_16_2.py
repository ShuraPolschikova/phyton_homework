from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()


@app.get("/")
async def welcome():
    return "Главная страница"


@app.get("/users/Admin")
async def welcome_admin():
    return "Вы вошли как администратор"


@app.get("/users/{user_id}")
async def get_id(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID from 1 to 100")]):
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/users/{username}/{age}")
async def get_info(username: Annotated[str, Path(min_length=5, max_length=20,
                                                 description="Enter username", examples="Shura")],
                       age: Annotated[int, Path(ge=18, le=120, description="Enter age from 18 to 120",
                                                examples="28")]):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
