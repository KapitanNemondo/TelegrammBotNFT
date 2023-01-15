from turtle import get_shapepoly
import pymysql
import random
import enum
import hashlib
import uuid

from ton_parser.parser import filter_Transaction
from datetime import datetime
from config import host, port, user, password, db_name, admin_list

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
            # port=port,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print(f"[DataBase - {db_name}] Succsfull Connect...")
    except Exception as ex:
        print(f"[DataBase - {db_name}] Connection refused...")
        print(f"[DataBase - {db_name}]", ex)

def GetTelegrammURL(tg_id):
    try:
        with connection.cursor() as cursor:
            try:
                cursor.execute(f"SELECT telegramm_url FROM `base_user` WHERE telegramm_id= '{tg_id}'")
                row = cursor.fetchone()
                if len(row['telegramm_url']) > 0 or row['telegramm_url'] != '':
                    return row['telegramm_url']
                else:
                    return "Null"
            except:
                return "Null"
    except:
        Connect()
        GetTelegrammURL(tg_id)

def GetPlayLogin(message):
    try:
        with connection.cursor() as cursor:
            print("[ID]", message.chat.id)
            try:
                tg_id = int(message.chat.id)

                cursor.execute(f"SELECT EXISTS(SELECT login FROM base_user WHERE telegramm_id = '{tg_id}')")
                row = cursor.fetchone()

                print("[ROW]", row)

                count_records = row[f"EXISTS(SELECT login FROM base_user WHERE telegramm_id = '{tg_id}')"]

                print("[COUNT RECORDS]", count_records)

                if  count_records == 1:

                    tg_url = GetTelegrammURL(tg_id)

                    print("[TG_URL]", tg_url)

                    if tg_url != "Null":
                        login = tg_url[1:] + "_" + str(tg_id)[-3:]
                    else:
                        login = "User_" + str(tg_id)

                    cursor.execute(f"UPDATE base_user SET login = '{login}' WHERE telegramm_id= '{tg_id}'")
                    connection.commit()

                    print("[LOGIN]", login)
                else:
                    cursor.execute(f"SELECT login FROM base_user WHERE telegramm_id = '{tg_id}'")
                    row = cursor.fetchone()
                    login = row["login"]
                
                key = str(random.randint(0, 1000000000)) + login + "@TONELEPHANTS" + str(random.randint(0, 1000000000)) + 2 * login
                print("[KEY]", key)

                salt = uuid.uuid4().hex


                hach = hashlib.sha256(key.encode())
                key_hach = hach.hexdigest()

                print("[KEY HACH]", key_hach)


                cursor.execute(f"UPDATE base_user SET pass_key = '{key_hach}' WHERE telegramm_id= '{tg_id}'")

                print("[BASE DATA]", "SUCCSES")

                nameFile = login + ".txt"

                print("[FILE]", nameFile)

                with open(f"users_key/{nameFile}", "w") as File:
                    pass

                connection.commit()
                
                return login

            except:
                return "EROR"
            
    except:
        Connect()
        GetPlayLogin(message)

def GetShaLogin(message):
    try:
        with connection.cursor() as cursor:
            print("[ID]", message.chat.id)
            try:
                tg_id = int(message.chat.id)

                cursor.execute(f"SELECT login_sha FROM base_user WHERE telegramm_id = '{tg_id}'")
                row = cursor.fetchone()

                print("[ROW]", row)

                # count_records = row[f"EXISTS(SELECT login_sha FROM base_user WHERE telegramm_id = '{tg_id}')"]

                # print("[COUNT RECORDS]", count_records)

                if row["login_sha"] != None:
                    return "LOGIN"
                
                else:
                    return "NO LOGIN"

            except:
                return "EROR"
            
    except:
        Connect()
        GetShaLogin(message)


def ChekShaLogin(message, login, password):
    try:
        with connection.cursor() as cursor:
            print("[ID Chel Login]", message.chat.id)
            try:
                tg_id = int(message.chat.id)

                cursor.execute(f"SELECT login_sha, pass_sha FROM base_user WHERE telegramm_id = '{tg_id}'")
                row = cursor.fetchone()

                print("[ROW]", row)

                sha_login_bd = row["login_sha"]
                sha_passw_bd = row["pass_sha"]

                hach_log = hashlib.sha256(login.encode())
                login_sha = hach_log.hexdigest()

                hach_pass =  hashlib.sha256(password.encode())
                pass_sha = hach_pass.hexdigest()
                

                if sha_login_bd != login_sha and sha_passw_bd != pass_sha:
                    return True
                
                else:
                    return False

            except:
                return "EROR"
            
    except:
        Connect()
        with connection.cursor() as cursor:
            print("[ID Chel Login]", message.chat.id)
            try:
                tg_id = int(message.chat.id)

                cursor.execute(f"SELECT login_sha, pass_sha FROM base_user WHERE telegramm_id = '{tg_id}'")
                row = cursor.fetchone()

                print("[ROW]", row)

                sha_login_bd = row["login_sha"]
                sha_passw_bd = row["pass_sha"]

                hach_log = hashlib.sha256(login.encode())
                login_sha = hach_log.hexdigest()

                hach_pass =  hashlib.sha256(password.encode())
                pass_sha = hach_pass.hexdigest()

                print("[SHA LOGIN]", login_sha)
                print("[SHA PASSW]", pass_sha)
                
                

                if sha_login_bd != login_sha and sha_passw_bd != pass_sha:
                    return True
                
                else:
                    return False

            except:
                return "EROR"

def WaitPassword(message):
    try:
        with connection.cursor() as cursor:
            print("[ID]", message.chat.id)
            try:
                tg_id = int(message.chat.id)

                cursor.execute(f"SELECT login FROM base_user WHERE telegramm_id = '{tg_id}'")
                row = cursor.fetchone()
                login = row["login"]

                cursor.execute(f"SELECT pass_key FROM base_user WHERE telegramm_id = '{tg_id}'")
                row = cursor.fetchone()
                key = row["pass_key"]

                nameFile = login + ".txt"

                print("[FILE]", nameFile)

                data = datetime.now()
                now = datetime.now().minute

                while (now <= data.minute + 5):

                    with open(f"users_key/{nameFile}", "r") as File:
                            dataFile = File.read()
                            if dataFile != "":
                                print("[KEY GET]", dataFile)
                                if dataFile == key:
                                    return ["Enter Succses", key]
                                return ["Enter Close", "EROR"]
                return ["Time is over", 0]
            except:
                return ["EROR", 0]
            
    except:
        Connect()
        WaitPassword(message)

def NewUserNFT(id_tg, teg):  # Добавление нового пользователя
    
    try:
        with connection.cursor() as cursor:
            try:
                # cursor.execute(f"SELECT MAX(id_user) as max FROM `base_user`")
                
                # row = cursor.fetchall()
                # id_user = row['max']
                # id_user += 1 
                cursor.execute(f"INSERT INTO `base_user`(`telegramm_id`, `telegramm_url`, `ton_number`, `login`, `pass_key`) VALUES ('{id_tg}','{teg}','', '', '')")
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
                cursor.execute(f"INSERT INTO `base_user`(`telegramm_id`, `telegramm_url`, `ton_number`, `login`, `pass_key`) VALUES ('{id_tg}','{teg}','', '', '')")
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

def ToWriteLoginPass(id, login, passwd):
    try:
        with connection.cursor() as cursor:

            hach_log = hashlib.sha256(login.encode())
            login_sha = hach_log.hexdigest()

            hach_pass =  hashlib.sha256(passwd.encode())
            pass_sha = hach_pass.hexdigest()
            
            cursor.execute(f"UPDATE base_user SET login_sha = '{login_sha}' WHERE telegramm_id= '{id}'")
            cursor.execute(f"UPDATE base_user SET pass_sha = '{pass_sha}' WHERE telegramm_id= '{id}'")

            connection.commit()
    except:
        Connect()
        ToWriteLoginPass(id, login, passwd)
    

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

        while (now < data.minute + 1):
            now = datetime.now().minute
            print("[DataMinute]", data.minute)
            print("[DataNow]", now)
            
            transaktion_flag = filter_Transaction(score, ton_number_id, data.minute)
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


def GetScoreNFT_Play(id : int):   # Получение количества купленных NFT
    try:
        # ton_number = GetReadNumberScore(id)
        with connection.cursor() as cursor:
            try:
                

                cursor.execute(f"SELECT `type` FROM `shop_user` WHERE `telegramm_id`= '{id}'")
                row = cursor.fetchall()


                return "YES"
            except:
                return "NO"
    except:
        Connect()
        with connection.cursor() as cursor:
            try:
                

                cursor.execute(f"SELECT `type` FROM `shop_user` WHERE `telegramm_id`= '{id}'")
                row = cursor.fetchall()


                return "YES"
            except:
                return "NO"

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

            print(data_status)

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
    
def NewSale(id, count_nft, score, index=None):       # Запись в БД информации о будущей продажи
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

def SetCapcha(id, capcha_id, id_refer):
    try:
        with connection.cursor() as cursor:
            try:
                cursor.execute(f"SELECT EXISTS(SELECT telegramm_id FROM `desired_purchase` WHERE telegramm_id = '{id}')")
                row = cursor.fetchone()
                count_records = row[f"EXISTS(SELECT telegramm_id FROM `desired_purchase` WHERE telegramm_id = '{id}')"]

                # print(count_records)

                if  count_records == 0:
                    cursor.execute(f"INSERT INTO `desired_purchase`(`telegramm_id`, `capcha_id`,`refer_id`) VALUES ('{id}','{capcha_id}', '{id_refer}')")
                else:
                    cursor.execute(f"UPDATE `desired_purchase` SET `capcha_id`='{capcha_id}', `refer_id`='{id_refer}' WHERE telegramm_id = '{id}'")
            
            except:
                pass
            connection.commit()
    except:
        Connect()
        SetCapcha(id, capcha_id, id_refer)

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
