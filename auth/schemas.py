import uuid
from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    email: str
    username: str
    phone_number: str
    registered_at: str
    parents_list: set[str] = set()
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = True
    is_verified: Optional[bool] = True


class UserCreate(schemas.BaseUserCreate):
    email: str
    username: str
    password: str
    phone_number: str
    registered_at: str
    parents_list: set[str] = set()
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = True
    is_verified: Optional[bool] = True


class UserUpdate(schemas.BaseUserUpdate):
    pass

