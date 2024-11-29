from fastapi import FastAPI, Query

# Создаем объект FastAPI
app = FastAPI()

# Маршрут к главной странице
@app.get("/")
def read_root():
    return {"message": "Главная страница"}

# Маршрут к странице администратора
@app.get("/user/admin")
def read_admin():
    return {"message": "Вы вошли как администратор"}

# Маршрут к страницам пользователей с параметром в пути
@app.get("/user/{user_id}")
def read_user(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# Маршрут к страницам пользователей с передачей данных в адресной строке
@app.get("/user")
def read_user_info(username: str = Query(..., description="Имя пользователя"), age: int = Query(..., description="Возраст пользователя")):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

# Запуск приложения
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)