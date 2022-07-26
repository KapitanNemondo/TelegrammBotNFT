import pymysql
import random

import ton_parser.main as ton_parser
import config_message as cm
from datetime import datetime
from config import host, port, user, password, db_name, TON_NUMBER

price = 200


#cur.execute("CREATE TABLE IF NOT EXISTS `test` (`ID` INT, `NFTcount` INT, `Score` INT)")


def Connect():     #Подключение к базе-данных
    global connection
    try:
        connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("[DataBase] Succsfull Connect...")
    except Exception as ex:
        print("[DataBase] Connection refused...")
        print("[DataBase]", ex)


def NewUserNFT(id):  # Добавление нового пользователя
    Connect()
    with connection.cursor() as cursor:
        try:
            cursor.execute(f"INSERT INTO `base_user` VALUES ('{id}', '{''}')")
        except:
            pass
        connection.commit()
    connection.close()

def ToWriteNumberScore(id, adress): # Запись номера тон счета с привязкой к id
    Connect()
    with connection.cursor() as cursor:
        cursor.execute(f"UPDATE base_user SET ton_number = '{adress}' WHERE telegramm_id= '{id}'")
        connection.commit()
    connection.close()

def GetReadNumberScore(id):         # Получение номера тон счета
    Connect()
    with connection.cursor() as cursor:
        try:
            cursor.execute(f"SELECT ton_number FROM `base_user` WHERE telegramm_id= '{id}'")
            row = cursor.fetchone()
            connection.close()
            return row['ton_number']
        except:
            return "Вы не привязали ваш ton счет"

def ChekNumberScore(id):            # Проверка наличия номер тон счета
    Connect()
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT ton_number FROM `base_user` WHERE telegramm_id= '{id}'")
        row = cursor.fetchone()['ton_number']
        
        connection.close()
        if row != '':
            return True
        else:
            return False

def ToWriteBdNFT(id, count_nft, score): # Проверка транзакции, в случае успеха запись данных в БД
    flag_transaktion = False

    ton_number_id = GetReadNumberScore(id)

    data = datetime.now()
    now = datetime.now().minute

    while (now <= data.minute + 2):
        now = datetime.now().minute
        print("[DataMinite]", data.minute)
        print("[DataNow]", now)

        transaktion_flag = (ton_parser.GetTransaktion(TON_NUMBER, ton_number_id, data, score))
        if transaktion_flag:
            break
    
    print(transaktion_flag)
    
    if transaktion_flag:

        # with connection.cursor() as cursor:
        for i in range(count_nft):  
            rand_number = GetRandNFT(data, ton_number_id)

            if rand_number == 6666:
                print("[Data Base]", "Eror 6666 - {Отказ в доступе}")
                return False                       
            
        return True

    return False

def GetRandNFT(data, ton_number):  # Получение рандомного номера из базы данных и запись даты, времени, номера и id покупки
    Connect()
    with connection.cursor() as cursor:
        try:
            cursor.execute(f"SELECT nft_id FROM `base_nft` WHERE acsess= 'YES'")
            row = cursor.fetchall()
            id_nft = (row[random.randrange(len(row))]['nft_id'])

            cursor.execute(f"UPDATE base_nft SET acsess = 'NO' WHERE nft_id= '{id_nft}'")
            cursor.execute(f"INSERT INTO `shop_user` VALUES ('{str(data.date())}', '{str(data.time())}', '{ton_number}', '{id_nft}')")
            connection.commit()
            connection.close()
            return id_nft
        except:
            connection.close()
            return 6666

def GetScore(id):   # Получение счета
    return "[Data Base] Eror 6666 - {Отказ в доступе}"  # DELETE AS CONFIGURATE NORM
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT ton_number FROM `base_user` WHERE telegramm_id= '{id}'")
        row = cursor.fetchone()

        return row['ton_number']
