
# import pymysql

# host = "localhost"
# port = 3307
# user = "bot"
# password = "Take_82A06"
# db_name = "NFT_Sale"

# #Подключение к базе-данных
# try:
#     connection = pymysql.connect(
#         host=host,
#         port=port,
#         user=user,
#         password=password,
#         database=db_name,
#         cursorclass=pymysql.cursors.DictCursor
#     )
#     print("[DataBase] Succsfull Connect...")
# except Exception as ex:
#     print("[DataBase] Connection refused...")
#     print("[DataBase]", ex)

# def CreateNFT():
#     mas = [2222, 1333, 666, 177, 46]
#     name = ['Common', 'Rare', 'Epic', 'Legedary', 'Exclusive']
#     count = 0
#     index = 0

#     with connection.cursor() as cursor:
#         for i in range(4445):
#             count += 1

#             try:
#                 cursor.execute(f"INSERT INTO `base_nft` VALUES ('{i}', '{'LOCK'}', '{name[index]}')")
#             except:
#                 pass
#             connection.commit()

#             if count == mas[index]: 
#                 print('[Type]', name[index])
#                 index += 1
#                 count = 0
                

           
    
#     print('Successfully')

# def UodateNFT():
#     mas = [555, 333, 166, 40, 10]
#     name = ['Common', 'Rare', 'Epic', 'Legedary', 'Exclusive']
#     count = 0
#     index = 0

#     with connection.cursor() as cursor:
#         for i in range(4445):
#             count += 1

#             try:
#                 # cursor.execute(f"UPDATE `base_nft` VALUES ('{i}', '{'LOCK'}', '{name[index]}')")
#                 cursor.execute(f"UPDATE `base_nft` SET acsess = '{'YES'}' WHERE `nft_id` = '{i}' AND `type` = '{name[index]}'")
                
#             except:
#                 pass
#             connection.commit()

#             if count == mas[index]: 
#                 print('[Type]', name[index])
#                 index += 1
#                 count = 0
                

           
    
#     print('Successfully')

# #CreateNFT()
# # UodateNFT()

# def WhiteList():
#     # data = [1970844037, 1490637384, 1317486098, 772914318, 644904426, 594680329, 498745815, 324850555, 560945352, 849231212, 5499581972,
#     # 493115134, 1803107169, 788532940, 524615551, 1490637384, 379373462, 795813196, 1192400800, 303780222, 721134254, 743741216, 
#     # 1241302903, 324850555, 498745815, 594680329, 644904426, 772914318, 1317486098, 1828738497, 1210354717, 401841115, 457449444,
#     # 5445884860, 714370319]

#     data = """5256187114
# 469364953
# 1658759242
# 509186843
# 1104032187
# 1924132251
# 2145617265
# 333684379
# 5446835479
# 251878343
# 1009055798
# 5142959133
# 5245343302
# 5241489391
# 5221851930
# 5459239613
# 5256187114
# 469364953
# 1658759242
# 509186843
# 1104032187
# 1924132251
# 2145617265
# 333684379
# 5446835479
# 251878343
# 1009055798
# 5142959133
# 5245343302
# 5241489391
# 5221851930
# 5459239613
# 5598382930
# 5789699140
# 5413966574
# 5715715315
# 5745397201
# 5788315137""".split('\n')

#     # print(len(data))

#     data = set(data)
#     print(data)

#     # id = 1

#     # with connection.cursor() as cursor:
#     #     for elem in data:

#     #         try:
#     #             cursor.execute(f"INSERT INTO `base_whitelist` VALUES ('{id}', '{elem}')")
#     #         except:
#     #             pass
#     #         connection.commit()

#     #         id += 1


# WhiteList()


