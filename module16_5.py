from fastapi import FastAPI, HTTPException, Path, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Annotated


# Создаем объект FastAPI
app = FastAPI()

# Настройка Jinja2Templates c новой папкой templates
templates = Jinja2Templates(directory="templates")

# Класс модели пользователя
class User(BaseModel):
    id: int
    username: str
    age: int

# Список для хранения пользователей
users = []

# Маршрут для получения всех пользователей
@app.get("/users")
async def get_users():
    """
    Возвращает список пользователей.
    """
    return users

# Маршрут для создания нового пользователя
@app.post("/user/{username}/{age}")
async def create_user(
        username: Annotated[str, Path(min_length=1)],
        age: Annotated[int, Path(gt=0)]
):
    """
    Создает нового пользователя.

    :param username: Имя пользователя (строка).
    :param age: Возраст пользователя (целое число).
    :return: Созданный пользователь.
    """
    # Находим максимальный ID пользователя
    max_id = max((user.id for user in users), default=0)
    new_id = max_id + 1

    # Создаем нового пользователя
    new_user = User(id=new_id, username=username, age=age)

    # Добавляем нового пользователя в список
    users.append(new_user)

    # Возвращаем созданного пользователя
    return new_user

# Маршрут для обновления информации о пользователе
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[int, Path(gt=0)],
        username: Annotated[str, Path(min_length=1)],
        age: Annotated[int, Path(gt=0)]
):
    """
    Обновляет информацию о пользователе.

    :param user_id: ID пользователя (целое число).
    :param username: Новое имя пользователя (строка).
    :param age: Новый возраст пользователя (целое число).
    :return: Обновленный пользователь.
    """
    # Проверяем, существует ли пользователь с указанным ID
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user

    # Если пользователь не найден, выбрасываем исключение
    raise HTTPException(status_code=404, detail="User was not found")

# Маршрут для удаления пользователя
@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(gt=0)]):
    """
    Удаляет пользователя.

    :param user_id: ID пользователя (целое число).
    :return: Удаленный пользователь.
    """
    # Проверяем, существует ли пользователь с указанным ID
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user

    # Если пользователь не найден, выбрасываем исключение
    raise HTTPException(status_code=404, detail="User was not found")

# Маршрут для отображения списка пользователей в шаблоне
@app.get("/", response_class=HTMLResponse)
async def read_users(request: Request):
    """
    Возвращает список пользователей в шаблоне.
    """
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

# Маршрут для отображения информации о конкретном пользователе в шаблоне
@app.get("/user/{user_id}", response_class=HTMLResponse)
async def read_user(request: Request, user_id: Annotated[int, Path(gt=0)]):
    """
    Возвращает информацию о конкретном пользователе в шаблоне.
    """
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})

    # Если пользователь не найден, выбрасываем исключение
    raise HTTPException(status_code=404, detail="User was not found")