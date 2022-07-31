import sqlite3

def Connect():     #Подключение к базе-данных
    global connection
    try:
        connection = sqlite3.connect("databasenft.db")
        # connection = pymysql.connect(
        #     host=host,
        #     port=port,
        #     user=user,
        #     password=password,
        #     database=db_name,
        #     cursorclass=pymysql.cursors.DictCursor
        # )
        print("[DataBase] Succsfull Connect...")
    except Exception as ex:
        print("[DataBase] Connection refused...")
        print("[DataBase]", ex)

def BaseNFT():
    #with connection.cursor() as cursor:
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE TABLE base_nft (nft_id INTEGER UNIQUE, acsess TEXT, type TEXT)")
    except:
        pass
    connection.commit()
    print('[Base NFT] Successfully')

def BaseUser():
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE TABLE base_user (telegramm_id INTEGER UNIQUE, ton_number TEXT)")
    except:
        pass
    connection.commit()
    print('[Base User] Successfully')

def ShopUser():
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE TABLE shop_user (data TEXT,time TEXT,ton_number TEXT, nft_id INTEGER)")
    except:
        pass
    connection.commit()
    print('[Shop User] Successfully')

def CreateNFT():
    mas = [2222, 1333, 666, 177, 46]
    name = ['Common', 'Rare', 'Epic', 'Legedary', 'Exclusive']
    count = 0
    index = 0

    cursor = connection.cursor()
    for i in range(4445):
        count += 1

        try:
            cursor.execute(f"INSERT INTO `base_nft` VALUES ('{i}', '{'LOCK'}', '{name[index]}')")
        except:
            pass
        connection.commit()

        if count == mas[index]: 
            print('[Type]', name[index])
            index += 1
            count = 0
                
    print('[NFT Data] Successfully')

Connect()
BaseNFT()
BaseUser()
ShopUser()
CreateNFT()