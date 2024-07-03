import json
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from src.models.user import User
from src.auth.jwt_auth import create_jwt_token
from datetime import datetime, timedelta, timezone


app = FastAPI(title="API", openapi_tags=[
                  {  "name": "visualizar", "description": "" }
              ])

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserAuth(BaseModel):
    login: str
    password: str

@app.get("/api/user/auth")
def get_auth():
    user = User()
    user.create_table_user('usuario', 'id INTEGER PRIMARY KEY AUTOINCREMENT, login VARCHAR(255), password VARCHAR(100) ')
    user.insert_data('usuario', 'login, password', ('valdirsilva@gmail.com', '12345'))
    return { "usuario": "Valdir"}

@app.post("/api/user/auth")
def post_auth(user: UserAuth):
    user_login = user.login
    user_password = user.password
    
    user = User()
    user_data = user.get_user_authentication('usuario', user_login, user_password)
    if user_data is None:
        print("Login ou senha inválidos")
        return
    
    labels = ['id', 'login', 'password']
    _dict = dict(zip(labels, user_data))

    payload = {
        'user_id': _dict['id'],
        'user_login': _dict['login'],
        'role': 'ADMIN',
        'exp': datetime.now(timezone.utc) + timedelta(hours=1)
    }

    # Função responsável por gerar o JWT
    _token_jwt = create_jwt_token(payload)
    print(_token_jwt)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", reload=True)