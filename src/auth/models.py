from datetime import datetime
from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, ForeignKey, Boolean, MetaData
from kazak.models import kazak
from fastapi_users.db import SQLAlchemyBaseUserTable
from database import Base

metadata = MetaData()


user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String(20), nullable=False),
    Column("phone_number", String(13), nullable=True),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("parents_list", Integer, ForeignKey(kazak.c.id), nullable=True),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False)
)


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    email: str = Column(String(length=320), unique=True, index=True, nullable=False)
    username = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    parents_list = Column(Integer, ForeignKey(kazak.c.id))
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)

