from turtle import get_shapepoly
import pymysql
import random
import enum

import ton_parser.main as ton_parser
from datetime import datetime
from config import host, port, user, password, db_name

NFT_name = ['Common', 'Rare', 'Epic', 'Legedary', 'Exclusive']


class ParamStatus(enum.Enum):
    get_factor      =   0           
    """получение множителей"""
    get_coast       =   1            
    """получение стоимости"""
    get_news        =   2          
    """получение всех данных о продажи для представления о покупке"""
    get_sale        =   3
    """получение достпуных карточек к покупке"""
    get_mainTON     =   4
    """получение главного тон счета"""

class ParamCapcha(enum.Enum):
    set_capcha      =   1
    """Установка значения капчи"""
    get_capcha      =   2
    """Получение значения капчи"""

class ParamList(enum.Enum):
    whitelist       =   1
    standart        =   2
    close           =   3
    time_close      =   4




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


def NewUserNFT(id_tg, teg):  # Добавление нового пользователя
    
    try:
        with connection.cursor() as cursor:
            try:
                # cursor.execute(f"SELECT MAX(id_user) as max FROM `base_user`")
                
                # row = cursor.fetchall()
                # id_user = row['max']
                # id_user += 1 
                cursor.execute(f"INSERT INTO `base_user`(`telegramm_id`, `telegramm_url`, `ton_number`) VALUES ('{id_tg}','{teg}','')")
            except:
                pass
            connection.commit()
    except:
        Connect()
        with connection.cursor() as cursor:
            try:
                # cursor.execute(f"SELECT MAX(id_user) as max FROM `base_user`")
                
                # row = cursor.fetchall()
                # id_user = row['max']
                # id_user += 1 
                cursor.execute(f"INSERT INTO `base_user`(`telegramm_id`, `telegramm_url`, `ton_number`) VALUES ('{id_tg}','{teg}','')")
            except:
                pass
            connection.commit()

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

def GetSale(id):                    # Получение информации о будующей покупке пользователя
    
    try:
        with connection.cursor() as cursor:
            try:
                cursor.execute(f"SELECT `count_nft`, `score_nft`, `purch_ratio` FROM `desired_purchase` WHERE telegramm_id= '{id}'")
                row = cursor.fetchone()
                return row['count_nft'], row['score_nft'], row['purch_ratio']
            except:
                return 'False', 'False', 'False'
    except:
        Connect()
        GetSale(id)

def EditCount(index):               # Редактирование числа оставшихся нфт
    
    try:
        sale = GetParam(ParamStatus.get_sale, index=index)
        # print("Sale:", sale)
        # print("Param:", index)
        new_sale = sale + 1
        with connection.cursor() as cursor:
            try:
                cursor.execute(f"UPDATE `settings_shop` SET `sale` = '{new_sale}' WHERE `id` = '{index}'")
            except:
                pass
    except:
        pass

def ToWriteBdNFT(id): # Проверка транзакции, в случае успеха запись данных в БД

    
    count_nft, score, index = GetSale(id)

    if count_nft != 'False' and score != 'False' and index != 'False':

        flag_transaktion = False

        ton_number_id = GetReadNumberScore(id)

        data = datetime.now()
        now = datetime.now().minute

        while (now <= data.minute + 1):
            now = datetime.now().minute
            print("[DataMinute]", data.minute)
            print("[DataNow]", now)

            transaktion_flag = (ton_parser.GetTransaktion(GetParam(ParamStatus.get_mainTON), ton_number_id, score))
            # transaktion_flag = True
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
                
                EditCount(index)


                
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

                cursor.execute(f"SELECT `type` FROM `base_nft` WHERE `nft_id`= '{id_nft}'")
                row = cursor.fetchone()
                type = row['type']

                cursor.execute(f"UPDATE base_nft SET acsess = 'NO' WHERE nft_id= '{id_nft}'")
                cursor.execute(f"INSERT INTO `shop_user`(`data`, `time`, `telegramm_id`, `ton_number`, `nft_id`, `type`) VALUES ('{str(data.date())}','{str(data.time())}','{id_user}','{ton_number}','{id_nft}', '{type}')")
                connection.commit()

                cursor.execute("SELECT nft_id FROM `base_nft`")

                return id_nft
            except:
                return 6666
    except:
        pass

def GetScore(id : int):   # Получение количества купленных NFT
    global NFT_name
    count_nft = "\n" + "{:15}{:6}".format("Тип", "Кол-во") + "\n"
    try:
        # ton_number = GetReadNumberScore(id)
        with connection.cursor() as cursor:
            try:
                

                cursor.execute(f"SELECT `type` FROM `shop_user` WHERE `telegramm_id`= '{id}'")
                row = cursor.fetchall()

                for elem in NFT_name:
                    count_nft += "{:15}{:6}".format(str(elem), str(row.count({'type': elem}))) + "\n"

                return count_nft
            except:
                return "Вы ещё ничего не купили"
    except:
        Connect()
        with connection.cursor() as cursor:
            try:
                
                cursor.execute(f"SELECT `type` FROM `shop_user` WHERE `telegramm_id`= '{id}'")
                row = cursor.fetchall()
                for elem in NFT_name:
                    count_nft += "{:15}{:6}".format(str(elem), str(row.count({'type': elem}))) + "\n"

                return count_nft
            except:
                return "Вы ещё ничего не купили"

def GetConfigNFT():                 # Получение настроек продаж
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

def GetStatusNFT(mode = ParamList.standart):                 # получение главных параметров продаж
    """Получение информации из гланых настроек продаж"""
    try:
        with connection.cursor() as cursor:
            try:
                if mode == ParamList.standart:
                    type = 'standart'
                elif mode == ParamList.whitelist:
                    type = 'white'
                cursor.execute(f"SELECT * FROM `main_bank` WHERE `type_list` = '{type}'")
                row = cursor.fetchall()
                return row
            except:
                pass
    except:
        Connect()
        with connection.cursor() as cursor:
            try:
                if mode == ParamList.standart:
                    type = 'standart'
                elif mode == ParamList.whitelist:
                    type = 'white'
                cursor.execute(f"SELECT * FROM `main_bank` WHERE `type_list` = '{type}'")
                row = cursor.fetchall()
                return row
            except:
                pass

def GetList(tg_id):
    """Получения информации о пользователе белый лист"""                 
    try:
        with connection.cursor() as cursor:
            try:
                cursor.execute(f"SELECT COUNT(*) FROM `base_whitelist` WHERE `telegramm_id`= '{tg_id}'")
                row = cursor.fetchone()
                return row['COUNT(*)']
            except:
                pass
    except:
        Connect()
        with connection.cursor() as cursor:
            try:
                cursor.execute(f"SELECT COUNT(*) FROM `base_whitelist` WHERE `telegramm_id`= '{tg_id}'")
                row = cursor.fetchone()
                return row['COUNT(*)']
            except:
                pass

def GetParam(paramStat : ParamStatus, index = None, tg_id = None):      # Получение информации из БД о количетсве доступных НФТ для продажи

    data_config = GetConfigNFT()                                            # Получение данных из БД о настройках покупки
    data_status = GetStatusNFT()

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

    # print(data_status)

    param["param_stage"] = param_stage = data_status[0]["count_stage"]
    param_factor = []
    param_avalible = []
    param_status = []
    # param_factor - Коэффициент покупки
    # param_number - Количество доступных NFT
    # param_status - Статус этапов
    # param_stage - Текущий этап                                         
    # param_coast - Цена продажи
    # param_avalible - Достпуно в данный момент
    
    if paramStat == ParamStatus.get_factor:

        for i in range(param_stage):
            param_factor.append(data_config[i]['purch_ratio'])
        
        return param_stage, param_factor
    
    elif paramStat == ParamStatus.get_news:
        white_list = GetList(tg_id)
        if white_list > 0:

            data_status = GetStatusNFT(ParamList.whitelist)

            param["current_stage"]  = data_status[0]['current_stage']
            param["count_stage"]    = data_status[0]['count_stage']
            param["coast"]          = data_status[0]['prise']
        
        else:
            param["current_stage"]  = data_status[0]['current_stage']
            param["count_stage"]    = data_status[0]['count_stage']
            param["coast"]          = data_status[0]['prise']
        
        # param["coast"]

        for i in range(param_stage):
            param["param_factor"].append(data_config[i]['purch_ratio'])
            param["param_avalible"].append(data_config[i]['avalible'])
            param["param_status"].append(data_config[i]['status'])
            param["param_sale"].append(data_config[i]['sale'])

        return param
    
    elif paramStat == ParamStatus.get_sale:
        return data_config[index]['sale']
    
    elif paramStat == ParamStatus.get_mainTON:
        return data_status[0]["ton_number"]
    
def NewSale(id, count_nft, score, index):       # Запись в БД информации о будущей продажи
    # print("Param_Factor:", param_factor)
    try:
        with connection.cursor() as cursor:
            try:
                cursor.execute(f"SELECT EXISTS(SELECT telegramm_id FROM `desired_purchase` WHERE telegramm_id = '{id}')")
                row = cursor.fetchone()
                count_records = row[f"EXISTS(SELECT telegramm_id FROM `desired_purchase` WHERE telegramm_id = '{id}')"]

                if  count_records == 0:
                    cursor.execute(f"INSERT INTO `desired_purchase`(`telegramm_id`, `count_nft`, `score_nft`, `purch_ratio`) VALUES ('{id}','{count_nft}','{score}', '{index}'")
                else:
                    cursor.execute(f"UPDATE `desired_purchase` SET `count_nft`='{count_nft}',`score_nft`='{score}', `purch_ratio`='{index}' WHERE telegramm_id = '{id}'")

            except:
                pass
            connection.commit()
    except:
        Connect()
        NewSale(id, count_nft, score, index)

def GetCapcha(id):
    try:
        with connection.cursor() as cursor:
            try:
                # print("YES")
                cursor.execute(f"SELECT `capcha_id` FROM `desired_purchase` WHERE telegramm_id = '{id}'")
                row = cursor.fetchone()
                # print(row['capcha_id'])
                return row['capcha_id']
            except:
                pass
            connection.commit()
    except:
        Connect()
        GetCapcha(id)

def SetCapcha(id, capcha_id):
    try:
        with connection.cursor() as cursor:
            try:
                cursor.execute(f"SELECT EXISTS(SELECT telegramm_id FROM `desired_purchase` WHERE telegramm_id = '{id}')")
                row = cursor.fetchone()
                count_records = row[f"EXISTS(SELECT telegramm_id FROM `desired_purchase` WHERE telegramm_id = '{id}')"]

                # print(count_records)

                if  count_records == 0:
                    cursor.execute(f"INSERT INTO `desired_purchase`(`telegramm_id`, `capcha_id`) VALUES ('{id}','{capcha_id}')")
                else:
                    cursor.execute(f"UPDATE `desired_purchase` SET `capcha_id`='{capcha_id}' WHERE telegramm_id = '{id}'")
            
            except:
                pass
            connection.commit()
    except:
        Connect()
        SetCapcha(id, capcha_id)

def GetAcsess(tg_id):
    try:
        with connection.cursor() as cursor:
            try:
                # print("YES")
                cursor.execute(f"SELECT `acsess` FROM `settings_acsess`")
                row = cursor.fetchone()
                
                if row['acsess'] == 'white':
                    count = GetList(tg_id)

                    if count > 0:
                        return True
                    else:
                        return False
                
                elif row['acsess'] == 'all':
                    return True
                
                # elif row['acsess'] == 'time_close':
                #     return ParamList.time_close
            except:
                pass
    except:
        Connect()
        with connection.cursor() as cursor:
            try:
                # print("YES")
                cursor.execute(f"SELECT `acsess` FROM `settings_acsess`")
                row = cursor.fetchone()
                
                if row['acsess'] == 'white':
                    count = GetList(tg_id)

                    if count > 0:
                        return True
                    else:
                        return False
                
                elif row['acsess'] == 'all':
                    return True
                
                # elif row['acsess'] == 'time_close':
                #     return ParamList.time_close
            except:
                pass

# Connect()

# print(ton_parser.GetTransaktion("EQCA0vWJntuL61f1-xQB2EwMorKpI448L5sh9c1kC29f8D4V", "EQALe1ZAjze9o0pgyxSHNfzqfKDmirqneLgJZnDyDAJ13SED", 35))
