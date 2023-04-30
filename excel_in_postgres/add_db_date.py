# import time
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# # from db import Kazaks, DATABASE_URL
# from tqdm.auto import tqdm
# import openpyxl
#
# wookbook = openpyxl.load_workbook("vgd_baza_pereselencev_20221031.xlsx")
# worksheet = wookbook.active
#
#
# def parse_kazak_in_excel():
#     list_kazaks = []
#     for kazak in range(3, 28801):
#         new_list = []
#         for col in worksheet.iter_cols(1, worksheet.max_column):
#             new_list.append(col[kazak].value)
#         list_kazaks.append(new_list)
#     return list_kazaks
#
#
# def add_in_db(first_name, last_name, middle_name, city_out, city, year):
#     engine = create_engine(DATABASE_URL)
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     kazaks = Kazaks(first_name=first_name,
#                     last_name=last_name,
#                     middle_name=middle_name,
#                     city_out=city_out,
#                     city=city,
#                     year=year)
#     session.add(kazaks)
#     session.commit()
#
#
# def add_date(date):
#     for kazak in tqdm(date):
#         time.sleep(0.01)
#         last_name = kazak[0].split()[0]
#         first_name = kazak[0].split()[1] if len(kazak[0].split()) > 1 else ""
#         middle_name = kazak[0].split()[2] if len(kazak[0].split()) > 2 else ""
#         city_out = kazak[1]
#         city = kazak[2]
#         year = kazak[3]
#         add_in_db(first_name, last_name, middle_name, city_out, city, year)
#
#
# result = parse_kazak_in_excel()
# add_date(result)
