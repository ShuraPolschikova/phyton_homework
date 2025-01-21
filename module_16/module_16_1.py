from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome():
    return "Главная страница"


@app.get("/users/Admin")
async def welcome_admin():
    return "Вы вошли как администратор"


@app.get("/users/{user_id}")
async def get_id(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user")
async def get_info(username: str, age: int):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
