import pymysql
import random
from config import host, port, user, password, db_name, admin_list


out = "Tg_id_ref        count_refer\n"

def Connect():     #Подключение к базе-данных
    """Подключение к базе данных"""
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
        #print("[DataBase] Succsfull Connect...")
    except Exception as ex:
        print("[DataBase] Connection refused...")
        print("[DataBase]", ex)


def NewUser(id: int):
    """
    Добавление нового рефера
    """
    global connection
    #print("[Database] id user:", id)
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT EXISTS(SELECT tg_id_ref FROM `referal_user` WHERE tg_id_ref = '{id}')")
            row = cursor.fetchone()
            #print(row)
            count_records = row[f"EXISTS(SELECT tg_id_ref FROM `referal_user` WHERE tg_id_ref = '{id}')"]

            if  count_records == 0:
                cursor.execute(f"INSERT INTO `referal_user` VALUES ('{id}', '{0}')")
                #print("[Database] New id add succsfull")

            else:
                cursor.execute(f"SELECT COUNT(*) FROM `referal_user` WHERE tg_id_ref= '{id}' ")
                row = cursor.fetchone()

                if row["COUNT(*)"] == 0:
                    cursor.execute(f"INSERT INTO `referal_user` VALUES ('{id}', '{0}')")
                    #print("[Database] New id add succsfull")
            
        connection.commit()
    except:
        Connect()
        NewUser(id)

def UpdateCountRefer(id_refer, id_new):
    """
    Обновление количества приглашенных пользователей
    с проверкой уникального гостя
    """

    global connection
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT EXISTS(SELECT tg_id_ref FROM `base_user` WHERE tg_id_ref = '{id_refer}')")
            row = cursor.fetchone()
            count_records = row[f"EXISTS(SELECT tg_id_ref FROM `base_user` WHERE tg_id_ref = '{id_refer}')"]

            if  count_records == 0:
                cursor.execute(f"INSERT INTO `base_user` VALUES ('{id_refer}', '{id_new}')")
                cursor.execute(f"UPDATE referal_user SET count_refer = '{1}' WHERE tg_id_ref = '{id_refer}'")

            else:
                cursor.execute(f"SELECT COUNT(*) FROM `base_user` WHERE tg_id_user = '{id_new}'")
                row = cursor.fetchone()

                if row["COUNT(*)"] >= 1:
                    pass
                else:
                    cursor.execute(f"INSERT INTO `base_user` VALUES ('{id_refer}', '{id_new}')")

                    cursor.execute(f"SELECT count_refer FROM `referal_user` WHERE tg_id_ref = '{id_refer}'")
                    row = cursor.fetchone()
                    count_refer = row['count_refer']
                    count_refer += 1

                    cursor.execute(f"UPDATE referal_user SET count_refer = '{count_refer}' WHERE tg_id_ref = '{id_refer}'")
                
            connection.commit()        
    except:
        Connect()
        UpdateCountRefer(id_refer, id_new)
            
def GetScore(id_refer):
    """Получение количества приглашенных пользователей"""
    global connection

    try:
        with connection.cursor() as cursor:
            try:
                cursor.execute(f"SELECT count_refer FROM `referal_user` WHERE tg_id_ref = '{id_refer}'")
                row = cursor.fetchone()
                return row['count_refer']
            except:
                return "Eror"
    except:
        Connect()
        GetScore(id_refer)

def GetReferalUser():
    """
    Получение id участника и количетсво приглашенных пользователей
    """
    global connection
    

    try:
        with connection.cursor() as cursor:
            out = "Tg_id_ref        count_refer\n"

            cursor.execute("SELECT * FROM referal_user")
            rows_id = cursor.fetchall()

            return rows_id

            # cursor.execute("SELECT count_refer FROM referal_user")
            # rows_count = cursor.fetchall()
            for i in range(len(rows_id)):
                out += str(rows_id[i]['tg_id_ref']) + ":        " + str(rows_id[i]['count_refer']) + '\n'
            
            #return out
            
            
    except:
        Connect()

        with connection.cursor() as cursor:
            out = "Tg_id_ref        count_refer\n"

            cursor.execute("SELECT * FROM referal_user")
            rows_id = cursor.fetchall()

            return rows_id

            # cursor.execute("SELECT count_refer FROM referal_user")
            # rows_count = cursor.fetchall()
            for i in range(len(rows_id)):
                out += str(rows_id[i]['tg_id_ref']) + ":        " + str(rows_id[i]['count_refer']) + '\n'
 

def GetFinalist():
    """
    Получение `tg_id_ref` и `count_refer`  финалистов
    """

    global connection

    try:
        with connection.cursor() as cursor:
            try:
                cursor.execute(f"SELECT tg_id_ref, count_refer FROM `referal_user` WHERE count_refer >= 1")
                row = cursor.fetchall()

                return row
            except:
                return "Eror"
    except:
        Connect()
        with connection.cursor() as cursor:
            try:
                cursor.execute(f"SELECT tg_id_ref, count_refer FROM `referal_user` WHERE count_refer >= 1")
                row = cursor.fetchall()

                return row
            except:
                return "Eror"

def GetUser():
    """
    Получение `tg_id_ref` и `tg_id_user`  пользователей
    """

    global connection

    try:
        with connection.cursor() as cursor:
            try:
                cursor.execute(f"SELECT tg_id_ref, tg_id_user FROM `base_user`")
                row = cursor.fetchall()

                return row
            except:
                return "Eror"
    except:
        Connect()
        with connection.cursor() as cursor:
            try:
                cursor.execute(f"SELECT tg_id_ref, tg_id_user FROM `base_user`")
                row = cursor.fetchall()

                return row
            except:
                return "Eror"

def GetSubber():
    """
    Получение `id` участника пользователей
    """
    

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT tg_id_ref FROM referal_user")
            rows_id = cursor.fetchall()
            # cursor.execute("SELECT count_refer FROM referal_user")
            # rows_count = cursor.fetchall()
            
            
            return rows_id
            
            
    except:
        Connect()
        with connection.cursor() as cursor:
            cursor.execute("SELECT tg_id_ref FROM referal_user")
            rows_id = cursor.fetchall()
            # cursor.execute("SELECT count_refer FROM referal_user")
            # rows_count = cursor.fetchall()
            
            
            return rows_id

def EditStatus(id_user):
    """
    Изменение статуса на YES
    """

    global connection
    try:
        with connection.cursor() as cursor:
            yes = "YES"
            cursor.execute(f"UPDATE `base_user` SET status='{yes}' WHERE tg_id_user = '{id_user}'")
            connection.commit()  
                  
    except:
        Connect()
        EditStatus(id_user)

def FindItod(id):
    """
    Поиск победителей по данным подписанных участников
    """

    global connection
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT COUNT(*) FROM `base_user` WHERE tg_id_ref = '{id}'")
            row = cursor.fetchone()

            return row["COUNT(*)"]
                  
    except:
        Connect()
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT COUNT(*) FROM `base_user` WHERE tg_id_ref = '{id}'")
            row = cursor.fetchone()

            return row["COUNT(*)"]
        
def GetConfig():                 # Получение настроек продаж
    try:
        with connection.cursor() as cursor:
            try:
                cursor.execute("SELECT `acsess` FROM `settings_referal`")
                row = cursor.fetchone()
                # print(row)
                return row['acsess']
            except:
                return "close"
    except:
        Connect()
        with connection.cursor() as cursor:
            try:
                cursor.execute("SELECT `acsess` FROM `settings_referal`")
                row = cursor.fetchone()
                return row['acsess']
            except:
                return "close"


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
                    cursor.execute(f"INSERT INTO `desired_purchase`(`telegramm_id`, `capcha_id`, `refer_id`) VALUES ('{id}','{capcha_id}', '{id_refer}')")
                else:
                    cursor.execute(f"UPDATE `desired_purchase` SET `capcha_id`='{capcha_id}' WHERE telegramm_id = '{id}'")
            
            except:
                pass
            connection.commit()
    except:
        Connect()
        SetCapcha(id, capcha_id, id_refer)


def GetIdRefer(id):
    try:
        with connection.cursor() as cursor:
            try:
                # print("YES")
                cursor.execute(f"SELECT `refer_id` FROM `desired_purchase` WHERE telegramm_id = '{id}'")
                row = cursor.fetchone()
                # print(row['capcha_id'])
                return row['refer_id']
            except:
                pass
            connection.commit()
    except:
        Connect()
        GetIdRefer(id)

def SetCountRefer(id_refer, id_user):

    """
    Обновление количества приглашенных пользователей
    с вычитаем приглашенных пользователей не соблюдавших условия конкурса

    минусование количества реферов и удалением пользователей из системы
    """

    global connection
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT count_refer FROM `referal_user` WHERE tg_id_user = '{id_refer}'")
            row = cursor.fetchone()
            count_refer = row['count_refer']

            if count_refer > 0:
                count_refer -= 1
                cursor.execute(f"DELETE FROM `base_user` WHERE tg_id_user = '{id_user}'")
            else:
                 count_refer = 0

            cursor.execute(f"UPDATE referal_user SET count_refer = '{count_refer}' WHERE tg_id_ref = '{id_refer}'")
        
            connection.commit()        
    except:
        Connect()
        UpdateCountRefer(id_refer, id_user)
