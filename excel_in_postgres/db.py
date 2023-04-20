from sqlalchemy import create_engine
import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql+psycopg2://postgres:260616@localhost:5432/search_kazak'
Base = declarative_base()


class Kazaks(Base):
    __tablename__ = "kazak"

    id = sq.Column(sq.Integer, primary_key=True)
    first_name = sq.Column(sq.String(20), nullable=False)
    last_name = sq.Column(sq.String(20), nullable=False)
    middle_name = sq.Column(sq.String(20), nullable=False)
    year = sq.Column(sq.String(10), nullable=True)
    fond = sq.Column(sq.String(50), nullable=True)
    rang = sq.Column(sq.String(50), nullable=True)
    city_out = sq.Column(sq.String(50), nullable=True)
    city = sq.Column(sq.String(50), nullable=True)
    info_db = sq.Column(sq.String(50), nullable=True)
    info = sq.Column(sq.String(200), nullable=True)
    user_id = sq.Column(sq.Integer(), nullable=True)


# try:
#     engine = create_engine(DATABASE_URL)
#     connection = engine.connect()
#
# except sq.exc.OperationalError:
#     print("Database doesn't exists or username/password incorrect")
#     input("Press any key to continue...")
# else:
#     print("База данных подключена")
#     input("Нажмите клавишу для продолжения....")
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     Base.metadata.create_all(engine)
#     print('finish')

