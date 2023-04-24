from sqlalchemy import MetaData, Table, Column, Integer, String

metadata = MetaData()

kazak = Table(
    "kazak",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('first_name', String(20), nullable=False),
    Column('last_name', String(20), nullable=False),
    Column('middle_name', String(20), nullable=True),
    Column('year', String(10), nullable=True),
    Column('fond', String(50), nullable=True),
    Column('rang', String(50), nullable=True),
    Column('city_out', String(50), nullable=True),
    Column('city', String(50), nullable=True),
    Column('info_db', String(50), nullable=True),
    Column('info', String(200), nullable=True),
    Column('user_id', Integer(), nullable=True)
)


