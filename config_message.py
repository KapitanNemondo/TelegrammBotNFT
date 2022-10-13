import pandas as pd
import bd

# print(bd.GetConfigNFT())

name_file = 'Config NFT.xlsx'

file = pd.read_excel(name_file, sheet_name='config')

param_factor = file['Коэффициенты покупок'].tolist()                # Коэффициент покупки
param_number = file['Количество досутпных NFT'].tolist()            # Количество доступных NFT
param_status = file['Статус Этапов'].tolist()                       # Статус этапов
param_cur_stage = int(file['Текущий Этап'].tolist()[0])             # Текущий этап                                         
param_stage = int(file['Количество этап продажи'].tolist()[0])      # Количество этап продажи
param_cost = file['Цена'].tolist()[0]                               # Цена покупки
param_nft_avalible = file['Куплено'].tolist()                       # Достпуно в данный момент
nft_all = 0                                                         # Всего


def GetParam():
    global param_factor, param_number, param_status, param_cur_stage, param_stage, param_cost, nft_all, param_nft_avalible

    file = pd.read_excel(name_file, sheet_name='config')

    param_factor = file['Коэффициенты покупок'].tolist()                # Коэффициент покупки
    param_number = file['Количество досутпных NFT'].tolist()            # Количество доступных NFT
    param_status = file['Статус Этапов'].tolist()                       # Статус этапов
    param_cur_stage = int(file['Текущий Этап'].tolist()[0])             # Текущий этап                                         
    param_stage = int(file['Количество этап продажи'].tolist()[0])      # Количество этап продажи
    param_cost = file['Цена'].tolist()[0]                               # Цена продажи
    param_nft_avalible = file['Куплено'].tolist()                       # Достпуно в данный момент
    

    for index in range(param_stage):
        if param_status[index] == "идёт в данный момент":
            nft_all = param_number[index]

# def InitSell(count_purchased):
#     global nft_all, param_nft_avalible

#     GetParam()

#     with pd.ExcelWriter(name_file, mode="a", if_sheet_exists="replace") as write:



#     if (nft_all - param_nft_avalible - count_purchased >= 0):
#         sold = param_nft_avalible + count_purchased
#         file.update('Куплено', sold)


def PrintParam():
    global param_factor, param_number, param_status, param_cur_stage, param_stage, param_cost
    print(param_factor, param_number, param_status, param_cur_stage, param_stage, param_cost, sep='\n')


# Изменение параметров через командную строку (устаревшая версия)
def EditParam(command):
    print("Вы вошли в режим изменения параметров")
    while True:
        if command == "e_fac":
            print("Режим изменения коэффициента покупок")
            for i in range(param_stage):
                param_factor[i] = int(input())

            print(param_factor)
            break

