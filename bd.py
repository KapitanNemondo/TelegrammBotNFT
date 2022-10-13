import pymysql
import random
import enum

import ton_parser.main as ton_parser
import config_message as cm
from datetime import datetime
from config import host, port, user, password, db_name, TON_NUMBER

class ParamStatus(enum.Enum):
    get_factor  =   0           
    """получение множителей"""
    get_coast   =   1            
    """получение стоимости"""
    get_news    =   2          
    """получение всех данных о продажи для представления о покупке"""

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


def NewUserNFT(id, teg):  # Добавление нового пользователя
    
    try:
        with connection.cursor() as cursor:
            try:
                cursor.execute(f"INSERT INTO `base_user`(`telegramm_id`, `telegramm_url`, `ton_number`, `login`, `passwd`) VALUES ('{id}','{teg}','{''}', '{''}', '{''}')")
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
                if len(row['ton_number']) > 0 or row['ton_number'] != '':
                    return row['ton_number']
                else:
                    return "Вы не привязали ваш ton счет"
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

def GetSale(id):
    try:
        with connection.cursor() as cursor:
            try:
                cursor.execute(f"SELECT `count_nft`, `score_nft` FROM `desired_purchase` WHERE telegramm_id= '{id}'")
                row = cursor.fetchone()
                return row['count_nft'], row['score_nft']
            except:
                return 'False', 'False'
    except:
        Connect()
        GetSale(id)

def ToWriteBdNFT(id): # Проверка транзакции, в случае успеха запись данных в БД

    count_nft, score = GetSale(id)

    if count_nft != 'False' and score != 'False':

        flag_transaktion = False

        ton_number_id = GetReadNumberScore(id)

        data = datetime.now()
        now = datetime.now().minute

        while (now <= data.minute + 1):
            now = datetime.now().minute
            print("[DataMinute]", data.minute)
            print("[DataNow]", now)

            # transaktion_flag = (ton_parser.GetTransaktion(TON_NUMBER, ton_number_id, data, score))
            transaktion_flag = True
            if transaktion_flag:
                break
        
        print(transaktion_flag)
        
        if transaktion_flag:

            # with connection.cursor() as cursor:
            for i in range(count_nft):  
                rand_number = GetRandNFT(data, ton_number_id, id)

                if rand_number == 6666:
                    print("[Data Base]", "Eror 6666 - {Отказ в доступе}")
                    return False  


                
            return True

        return False

    else:
        return False

def GetRandNFT(data, ton_number, id_user):  # Получение рандомного номера из базы данных и запись даты, времени, номера и id покупки
    try:
        with connection.cursor() as cursor:
            try:
                cursor.execute(f"SELECT nft_id FROM `base_nft` WHERE acsess= 'YES'")
                row = cursor.fetchall()
                id_nft = (row[random.randrange(len(row))]['nft_id'])

                cursor.execute(f"UPDATE base_nft SET acsess = 'NO' WHERE nft_id= '{id_nft}'")
                cursor.execute(f"INSERT INTO `shop_user`(`data`, `time`, `telegramm_id`, `ton_number`, `nft_id`) VALUES ('{str(data.date())}','{str(data.time())}','{id_user}','{ton_number}','{id_nft}')")
                connection.commit()

                cursor.execute("SELECT nft_id FROM `base_nft`")

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



def GetConfigNFT():
    try:
        with connection.cursor() as cursor:
            try:
                cursor.execute("SELECT * FROM `settings_shop`")
                row = cursor.fetchall()
                return row
            except:
                return "Вы ещё ничего не купили"
    except:
        Connect()
        with connection.cursor() as cursor:
            try:
                cursor.execute("SELECT * FROM `settings_shop`")
                row = cursor.fetchall()
                return row
            except:
                return "Вы ещё ничего не купили"

def GetStatusNFT():
    try:
        with connection.cursor() as cursor:
            try:
                cursor.execute("SELECT * FROM `main_bank`")
                row = cursor.fetchall()
                return row
            except:
                return "Вы ещё ничего не купили"
    except:
        Connect()
        with connection.cursor() as cursor:
            try:
                cursor.execute("SELECT * FROM `main_bank`")
                row = cursor.fetchall()
                return row
            except:
                return "Вы ещё ничего не купили"


def GetParam(paramStat : ParamStatus):      # Получение информации из БД о количетсве доступных НФТ для продажи

    data_config = GetConfigNFT()                                            # Получение данных из БД о настройках покупки
    data_status = GetStatusNFT()

    count_stage = data_status[0]['count_stage']

    param = {
        "current_stage"     : int(),
        "count_stage"       : int(),
        "param_coast"       : int(),
        "param_stage"       : int(),
        "param_factor"      : [],
        "param_avalible"    : [],
        "param_status"      : [],
        "param_sale"        : [],
    }

    param["param_stage"] = param_stage = len(data_config)
    param_factor = []
    param_avalible = []
    param_status = []
    # param_factor - Коэффициент покупки
    # param_number - Количество доступных NFT
    # param_status - Статус этапов
    # param_stage - Текущий этап                                         
    # param_cost - Цена продажи
    # param_avalible - Достпуно в данный момент
    
    if paramStat == ParamStatus.get_factor:

        for i in range(param_stage):
            param_factor.append(data_config[i]['purch_ratio'])
        
        return param_stage, param_factor
    
    elif paramStat == ParamStatus.get_news:
        param["current_stage"]  = data_status[0]['current_stage']
        param["count_stage"]    = data_status[0]['count_stage']
        param["coast"]          = data_status[0]['prise']

        for i in range(param_stage):
            param["param_factor"].append(data_config[i]['purch_ratio'])
            param["param_avalible"].append(data_config[i]['avalible'])
            param["param_status"].append(data_config[i]['status'])
            param["param_sale"].append(data_config[i]['sale'])

        return param

    
def NewSale(id, count_nft, score):
    try:
        with connection.cursor() as cursor:
            try:
                cursor.execute(f"SELECT EXISTS(SELECT telegramm_id FROM `desired_purchase` WHERE telegramm_id = '{id}')")
                row = cursor.fetchone()
                count_records = row[f"EXISTS(SELECT telegramm_id FROM `desired_purchase` WHERE telegramm_id = '{id}')"]

                if  count_records == 0:
                    cursor.execute(f"INSERT INTO `desired_purchase`(`telegramm_id`, `count_nft`, `score_nft`) VALUES ('{id}','{count_nft}','{score}')")
                else:
                    cursor.execute(f"UPDATE `desired_purchase` SET `count_nft`='{count_nft}',`score_nft`='{score}' WHERE telegramm_id = '{id}'")

            except:
                pass
            connection.commit()
    except:
        Connect()
        NewSale(id, count_nft, score)

#Connect()
