from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean

metadata = MetaData()

user = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("first_name", String, nullable=False),
    Column("middle_name", String, nullable=False),
    Column("phone_number", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("parents_list", String, default=False, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False)
)


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


