from datetime import datetime
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, Boolean, JSON

metadata = MetaData()

user = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("phone_number", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("parents_list", JSON, default=False, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False)
)


kazak = Table(
    "kazak",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('first_name', String(20), nullable=False),
    Column('last_name', String(20), nullable=False),
    Column('middle_name', String(20), nullable=False),
    Column('year', String(10), nullable=True),
    Column('fond', String(50), nullable=True),
    Column('rang', String(50), nullable=True),
    Column('city_out', String(50), nullable=True),
    Column('city', String(50), nullable=True),
    Column('info_db', String(50), nullable=True),
    Column('info', String(200), nullable=True),
    Column('user_id', Integer(), nullable=True)
)





