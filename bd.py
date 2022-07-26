import pymysql
import random

import ton_parser.main as ton_parser
import config_message as cm
from datetime import datetime
from config import host, port, user, password, db_name, TON_NUMBER


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
    
    try:
        with connection.cursor() as cursor:
            try:
                cursor.execute(f"INSERT INTO `base_user` VALUES ('{id}', '{''}')")
            except:
                pass
            connection.commit()
    except:
        Connect()
        NewUserNFT(id)
    

def ToWriteNumberScore(id, adress): # Запись номера тон счета с привязкой к id
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"UPDATE base_user SET ton_number = '{adress}' WHERE telegramm_id= '{id}'")
            connection.commit()
    except:
        Connect()
        NewUserNFT(id)
    

def GetReadNumberScore(id):         # Получение номера тон счета
    try:
        with connection.cursor() as cursor:
            try:
                cursor.execute(f"SELECT ton_number FROM `base_user` WHERE telegramm_id= '{id}'")
                row = cursor.fetchone()
                return row['ton_number']
            except:
                return "Вы не привязали ваш ton счет"
    except:
        Connect()
        GetReadNumberScore(id)

def ChekNumberScore(id):            # Проверка наличия номер тон счета
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT ton_number FROM `base_user` WHERE telegramm_id= '{id}'")
            row = cursor.fetchone()['ton_number']
            
            if row != '':
                return True
            else:
                return False
    except:
        Connect()
        ChekNumberScore(id)

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
    try:
        with connection.cursor() as cursor:
            try:
                cursor.execute(f"SELECT nft_id FROM `base_nft` WHERE acsess= 'YES'")
                row = cursor.fetchall()
                id_nft = (row[random.randrange(len(row))]['nft_id'])

                cursor.execute(f"UPDATE base_nft SET acsess = 'NO' WHERE nft_id= '{id_nft}'")
                cursor.execute(f"INSERT INTO `shop_user` VALUES ('{str(data.date())}', '{str(data.time())}', '{ton_number}', '{id_nft}')")
                connection.commit()
                return id_nft
            except:
                return 6666
    except:
        Connect()
        GetRandNFT(data, ton_number)

def GetScore(id):   # Получение количества купленных NFT

    try:
        ton_number = GetReadNumberScore(id)
        with connection.cursor() as cursor:
            try:
                cursor.execute(f"SELECT COUNT(*) FROM `shop_user` WHERE ton_number= '{ton_number}'")
                row = cursor.fetchone()
                return row['COUNT(*)']
            except:
                return "Вы ещё ничего не купили"
    except:
        Connect()
        GetScore(id)


#Connect()
