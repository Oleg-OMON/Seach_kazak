from typing import List
from urllib.request import Request
from fastapi.encoders import jsonable_encoder
from pydantic import ValidationError
from starlette import status
from starlette.responses import JSONResponse
import uuid
from fastapi import FastAPI
from fastapi_users import fastapi_users, FastAPIUsers
from auth.manager import get_user_manager
from auth.auth import auth_backend
from auth.schemas import UserRead, UserCreate
from model import user, Kazak

app = FastAPI()


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()}),
    )

fastapi_users = FastAPIUsers[user, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

@app.get('/users/{user_id}', response_model=List[user])
def get_user(user_id: int):
    """Получить юзера по id"""
    return [user for user in fake_users if user.get("id") == user_id]


@app.get('/users')
def get_users():
    """получить список юзеров"""
    users = []
    for user in fake_users:
        users.append(user)
    return users


@app.get('/search_kazak/{last_name}/{city}', response_model=List[Kazak])
def get_kazak(last_name: str, city: str):
    """получить казака по имени и населеному пункту"""
    for kazak in kazaks_list:
        if kazak.get('last_name') == last_name and kazak.get('city') == city:
            return [kazak]


@app.post('/kazak_add')
def post_kazak(id, first_name,last_name, middle_name,rang,year,fond,city_out,city,info_db,info,photo,user_id):
    kazak = {
        "id": id,
        "first_name": first_name,
        "last_name": last_name,
        "middle_name": middle_name,
        "rang": rang,
        "year": year,
        "fond": fond,
        "city_out": city_out,
        "city": city,
        "info_db": info_db,
        "info": info,
        "photo": photo,
        'user_id': user_id
    }

    kazaks_list.append(kazak)
    return kazaks_list


@app.get('/kazaks/{kazak_id}', response_model=List[Kazak])
def get_kazak_id(kazak_id: int):
    """Получить казака по id"""
    return [kazak for kazak in kazaks_list if kazak.get("id") == kazak_id]


@app.get('/kazaks')
def get_kazaks():
    """получить список казаков"""
    kazaks = []
    for kazak in kazaks_list:
        kazaks.append(kazak)
    return kazaks


fake_users = [
    {"id": 1,
     "login": "Father",
     "first_name": "Oleg",
     'last_name': 'Zasedatelev',
     'phone_number': "899977777777",
     "privat": False,
     'creation_date': "2023-03-11T09:25:55.074Z",
     'parens_list': [],
     'password': 'qwe123'
     },
    {"id": 2,
     "login": "Investor",
     "first_name": "Ruslan",
     "last_name": "Kamishev",
     "phone_number": "89998888888",
     "privat": True,
     "creation_date": "2023-03-11T09:25:55.074Z",
     'parens_list': [],
     "password": 'asd321'
     },
    {"id": 3,
     "login": "Kazak",
     "first_name": "Aleksey",
     "last_name": "Eshenko",
     "phone_number": "89996666666",
     "privat": False,
     "creation_date": "2023-03-11T09:25:55.074Z",
     'parens_list': [],
     "password": '1234567'
     }
]

kazaks_list = [
    {"id": 104,
     "first_name": "Селиверст",
     "last_name": "Ананьев",
     "middle_name": "",
     "rang": "младший урядник",
     "year": "",
     "fond": "",
     "city_out": "",
     "city": "Чамлыкская",
     "info_db": "База казаков кубанцев Русско-Японская 1905г",
     "info": "",
     "photo": "kazak.jpg",
     'user_id': 0
     },
    {"id": 19509,
     "first_name": "Леон",
     "last_name": "Польской",
     "middle_name": "Сидоров",
     "year": "",
     "fond": "",
     "rang": "",
     "city_out": "Нет данных",
     "city": "Витязевская ст.",
     "info_db": "База переселенцев на Северный Кавказ и Кубань (по документам РГВИА и РГИА)",
     "info": "",
     "photo": "",
     'user_id': 0
     },
    {"id": 4259,
     "first_name": "Роман",
     "last_name": "Ярчуков",
     "middle_name": " Лукьянович",
     "year": "",
     "fond": "40215-2-99 ",
     "rang": "",
     "city_out": "",
     "city": "Чамлыкская",
     "info_db": "Анкеты военнопленных и перебежчиков из Белых армий, действовавших на юге России, 1920г.",
     "info": "",
     "photo": "",
     'user_id': 0
     }
]
