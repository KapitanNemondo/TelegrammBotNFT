
import pymysql

host = "localhost"
port = 3307
user = "bot"
password = "Take_82A06"
db_name = "NFT_Sale"

#Подключение к базе-данных
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

def CreateNFT():
    mas = [2222, 1333, 666, 177, 46]
    name = ['Common', 'Rare', 'Epic', 'Legedary', 'Exclusive']
    count = 0
    index = 0

    with connection.cursor() as cursor:
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
                

           
    
    print('Successfully')

def UodateNFT():
    mas = [555, 333, 166, 40, 10]
    name = ['Common', 'Rare', 'Epic', 'Legedary', 'Exclusive']
    count = 0
    index = 0

    with connection.cursor() as cursor:
        for i in range(4445):
            count += 1

            try:
                # cursor.execute(f"UPDATE `base_nft` VALUES ('{i}', '{'LOCK'}', '{name[index]}')")
                cursor.execute(f"UPDATE `base_nft` SET acsess = '{'YES'}' WHERE `nft_id` = '{i}' AND `type` = '{name[index]}'")
                
            except:
                pass
            connection.commit()

            if count == mas[index]: 
                print('[Type]', name[index])
                index += 1
                count = 0
                

           
    
    print('Successfully')

#CreateNFT()
UodateNFT()