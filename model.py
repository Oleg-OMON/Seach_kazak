from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    id: int
    login: str
    first_name: str
    last_name: str
    phone_number: str
    privat: bool
    creation_date: datetime
    parents_list: Optional[List] = []
    password: str


class Kazak(BaseModel):
    id: int
    first_name: str
    last_name: str
    middle_name: Optional[str]
    year: Optional[str]
    fond: Optional[str]
    rang: Optional[str]
    city_out: Optional[str]
    city: str
    info_db: str
    info: Optional[str]
    photo: Optional[str]
    user_id: Optional[int] = 0


