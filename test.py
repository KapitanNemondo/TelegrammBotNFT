# import pymysql
# import random

# from config import host, port, user, password, db_name, TON_NUMBER


# def Connect():     #Подключение к базе-данных
#     global connection
#     try:
#         connection = pymysql.connect(
#             host=host,
#             port=port,
#             user=user,
#             password=password,
#             database=db_name,
#             cursorclass=pymysql.cursors.DictCursor
#         )
#         print("[DataBase] Succsfull Connect...")
#     except Exception as ex:
#         print("[DataBase] Connection refused...")
#         print("[DataBase]", ex)

# def GetReadNumberScore(id):         # Получение номера тон счета
#     try:
#         with connection.cursor() as cursor:
#             try:
#                 cursor.execute(f"SELECT ton_number FROM `base_user` WHERE telegramm_id= '{id}'")
#                 row = cursor.fetchone()
#                 return row['ton_number']
#             except:
#                 return "Вы не привязали ваш ton счет"
#     except:
#         Connect()
#         GetReadNumberScore(id)

# def GetScore(id):   # Получение счета

#     try:
#         with connection.cursor() as cursor:
#             try:
#                 cursor.execute(f"SELECT ton_number FROM `base_user` WHERE telegramm_id= '{id}'")
#                 row = cursor.fetchone()

#                 cursor.execute(f"SELECT COUNT(*) FROM `shop_user` WHERE ton_number='{row['ton_number']}'")
#                 row = cursor.fetchone()
#                 return row['COUNT(*)']
#             except:
#                 return "Вы ещё ничего не купили"
#     except:
#         Connect()
#         GetScore(id)

nameFile = "Elovskij_212.txt"

# myfile = open(f"users_key/{nameFile}", "w")
# myfile.close()
flag = True
while flag:
    with open(f"users_key/{nameFile}", "r") as File:
                            dataFile = File.read()
                            print(dataFile)
                            if dataFile != "":
                                flag = False