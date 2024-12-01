from fastapi import FastAPI, HTTPException, Path, Query
from typing import Annotated

# Создаем объект FastAPI
app = FastAPI()

# Словарь для хранения пользователей
users = {"1": "Имя: Example, возраст: 18"}


# Маршрут для получения всех пользователей
@app.get("/users")
async def get_users():
    """
    Возвращает словарь с пользователями.
    """
    return users


# Маршрут для создания нового пользователя
@app.post("/user/{username}/{age}")
async def create_user(
        username: Annotated[str, Path(min_length=1)],  # Исправлено: используем Path для параметра пути
        age: Annotated[int, Path(gt=0)]  # Исправлено: используем Path для параметра пути
):
    """
    Создает нового пользователя.

    :param username: Имя пользователя (строка).
    :param age: Возраст пользователя (целое число).
    :return: Сообщение о регистрации пользователя.
    """
    # Находим максимальный ID пользователя
    max_id = max(map(int, users.keys())) if users else 0
    new_id = str(max_id + 1)

    # Добавляем нового пользователя в словарь
    users[new_id] = f"Имя: {username}, возраст: {age}"

    # Возвращаем сообщение о регистрации
    return {"message": f"User {new_id} is registered"}


# Маршрут для обновления информации о пользователе
@app.put("/user/{user_id}")
async def update_user(
        user_id: Annotated[str, Path(min_length=1)],  # Исправлено: используем Path для параметра пути
        username: Annotated[str, Query(min_length=1)],  # Исправлено: используем Query для параметра запроса
        age: Annotated[int, Query(gt=0)]  # Исправлено: используем Query для параметра запроса
):
    """
    Обновляет информацию о пользователе.

    :param user_id: ID пользователя (строка).
    :param username: Новое имя пользователя (строка).
    :param age: Новый возраст пользователя (целое число).
    :return: Сообщение об обновлении пользователя.
    """
    # Проверяем, существует ли пользователь с указанным ID
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    # Обновляем информацию о пользователе
    users[user_id] = f"Имя: {username}, возраст: {age}"

    # Возвращаем сообщение об обновлении
    return {"message": f"User {user_id} has been updated"}


# Маршрут для удаления пользователя
@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[str, Path(min_length=1)]):  # Исправлено: используем Path для параметра пути
    """
    Удаляет пользователя.

    :param user_id: ID пользователя (строка).
    :return: Сообщение об удалении пользователя.
    """
    # Проверяем, существует ли пользователь с указанным ID
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    # Удаляем пользователя из словаря
    del users[user_id]

    # Возвращаем сообщение об удалении
    return {"message": f"User {user_id} has been deleted"}