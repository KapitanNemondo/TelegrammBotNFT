
import telebot
from telebot import types

import baseReferData as base_refer

host = "localhost"
port = 3307
user = "site_setting"
password = "holocoastneverhappened"
db_name = "NFT_Sale"
db_name_refer = "Referal"

# admin_list = [849231212, 493115134, 560945352]
# """ Еловский, Гозенко Артём, Гозенко Анатолий """

admin_list = [849231212, 485563456, 675564806, 493115134, 560945352]
""" Еловский, Краснов, Попов, Гозенко Артём, Гозенко Анатолий"""

# TON_NUMBER = "EQCA0vWJntuL61f1-xQB2EwMorKpI448L5sh9c1kC29f8D4V"

#main variables
TOKEN = "5665892960:AAH2FgPw_bMqirFEqBlXe8CePTm7mv0f_KQ"
bot = telebot.TeleBot(TOKEN)

callback_capcha = ['👥', '👾', '🐰', '🍀', '🍌']
flag_capcha = False


def DotMenu(message):
    markup = types.ReplyKeyboardRemove()
    return markup

def MainMenu(message):
    markup = types.InlineKeyboardMarkup()

    markup.row_width = 2

    btn1 = types.InlineKeyboardButton("📂 Мои NFT", callback_data="my nft")
    btn2 = types.InlineKeyboardButton("🔗 Реферальная программа", callback_data="refer programm")

    log_inst = types.InlineKeyboardButton(text="📱 Instagram", url='https://instagram.com/ton_elephants')
    log_tg = types.InlineKeyboardButton(text="✈ Telegram", url='https://t.me/ton_elephants')
    log_chat = types.InlineKeyboardButton(text='🗣 Наш чат', url='https://t.me/+4w1S6lz5c3s2MzJi')


    btn5 = types.InlineKeyboardButton("🎮 Войти в игру", callback_data="New Play")

    chat_id = message.chat.id

    markup.add(btn1, btn2, log_inst, log_tg, log_chat)

    for elem in admin_list:
        if elem == chat_id:
            markup.add(btn5)

    

    return markup

def PlayRegistrMenu(message):
    markup = types.InlineKeyboardMarkup()

    markup.row_width = 2

    btn1 = types.InlineKeyboardButton("📱 Зарегестрироватся", callback_data="RegistrInPlay")
    back_Menu = types.InlineKeyboardButton(text="⚙️ Вернутся в главное меню", callback_data="BackToMain")


    markup.add(btn1, back_Menu)

    return markup

def new_refer_menu(chat_id, url):
    """Новое меню рефералов"""
    markup = types.InlineKeyboardMarkup()

    markup.row_width = 3

    get_info = types.InlineKeyboardButton(text="ℹ️ Информация", callback_data="GetInfoRefer")
    #url = types.InlineKeyboardButton('🔗 Моя ссылка', callback_data="myUrl")
    score = types.InlineKeyboardButton('🧮 Счет', callback_data="getScore")

    back_Menu = types.InlineKeyboardButton(text="⚙️ Вернутся в главное меню", callback_data="BackToMain")

    get_info_all_user = types.InlineKeyboardButton('📝 Информация об участниках', callback_data="getAllUser")

    stage_map = types.InlineKeyboardButton('📜 Карта призов', callback_data="ref_stageMap")


    markup.add(get_info, url, stage_map score, back_Menu)

    for elem in admin_list:
        if elem == chat_id:
            if elem == admin_list[0]:
                markup.add(get_info_all_user)


    return markup


def show_url_sub():
    """Вывод инлайн кнопки с подписками"""
    
    markup = types.InlineKeyboardMarkup()

    markup.row_width = 3

    log_inst = types.InlineKeyboardButton(text="📱 Instagram", url='https://instagram.com/ton_elephants')
    log_tg = types.InlineKeyboardButton(text="✈ Telegram", url='https://t.me/ton_elephants')
    log_chat = types.InlineKeyboardButton(text='🗣 Наш чат', url='https://t.me/+4w1S6lz5c3s2MzJi')

    back_Menu = types.InlineKeyboardButton(text="⚙️ Вернутся в главное меню", callback_data="Back")

    


    markup.add(log_inst, log_tg, log_chat, back_Menu)

    


    return markup

def NFT_Menu(message):      # Главное меню
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton("💼 Мои покупки", callback_data="my buy")
    btn2 = types.InlineKeyboardButton("💵 Купить NFT", callback_data="buy nft")
    btn3 = types.InlineKeyboardButton("💰 Изменить номер счета", callback_data="edit number")
    btn4 = types.InlineKeyboardButton("🏦 Проверить счет", callback_data="chek score")

    back_Menu = types.InlineKeyboardButton(text="⚙️ Вернутся в главное меню", callback_data="BackToMain")

    btn5 = types.InlineKeyboardButton("🎮 Войти в игру", callback_data="New Play")

    chat_id = message.chat.id

    markup.add(btn1, btn2, btn3, btn4, back_Menu)

    for elem in admin_list:
        if elem == chat_id:
            markup.add(btn5)

    

    return markup

# ок
def show_data_user(chat_id):
    """
    Получение зарегистрированной уникальной ссылки 
    и количества пользователей, подписавшихся с ней
    """
    # regim = baseRefer.GetConfig()
    markup = types.InlineKeyboardMarkup()

    markup.row_width = 2

    url = types.InlineKeyboardButton('🔗 Моя ссылка', callback_data="myUrl")
    score = types.InlineKeyboardButton('🧮 Счет', callback_data="getScore")

    back_Menu = types.InlineKeyboardButton(text="⚙️ Вернутся в главное меню", callback_data="BackToMain")


    #get_all_score = types.KeyboardButton(text='Показать счет всех участников')

    get_info_all_user = types.InlineKeyboardButton('📝 Информация об участниках', callback_data="getAllUser")

    #updata_bot = types.KeyboardButton(text='Обновить бота')

    policeBot = types.InlineKeyboardButton('Активировать сыщика', callback_data="search")

    # getAutorization = types.KeyboardButton(text='Я не робот')

    
    

    for elem in admin_list:
        if elem == chat_id:
            if elem == admin_list[0]:
                markup.add(get_info_all_user)

    markup.add(url, score, back_Menu)
    
    # elif regim == 2:
    #     markup.add(score, getAutorization)
    
    return markup

def MarkupBackMenu():
    markup = types.InlineKeyboardMarkup()

    back_Menu = types.InlineKeyboardButton(text="⚙️ Вернутся в главное меню", callback_data="BackToMain")

    markup.add(back_Menu)
    
    return markup

def PlayMenu(message):
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton("🛡 Настройки", callback_data="play settings")
    btn2 = types.InlineKeyboardButton("🔑 Выйти на всех устройствах", callback_data="out all devices")
    

    back_Menu = types.InlineKeyboardButton(text="⚙️ Вернутся в главное меню", callback_data="BackToMain")

    # btn5 = types.InlineKeyboardButton("🎮 Войти в игру", callback_data="New Play")

    chat_id = message.chat.id

    markup.add(btn1, btn2, back_Menu)

    # for elem in admin_list:
    #     if elem == chat_id:
    #         markup.add(btn5)

    

    return markup


def GetStageMap(tg_id):
    param = {
        "discount_flag"     : bool(),       
        # Разрешена ли пользователю скидка
        "discount_param"    : int(),        # Минимальное количество пользователей для скидки
        "discount_count"    : int(),        # Величина скидки 
        
        "energy_flag"       : bool(),       # Разрешена ли пользователю доп энергия
        "energy_param"      : int(),        # Минимальное количество пользователей для скидки
        "energy_count"      : int(),        # Величина энергии

        "boost_flag"       : bool(),       # Разрешена ли пользователю доп буст
        "boost_param"      : int(),        # Минимальное количество пользователей для скидки
        "boost_count"      : int(),        # Величина буста

    }

    photo_st = ["1-ST WAY 0.jpg", "1-ST WAY 1.jpg", "1-ST WAY 2.jpg", "1-ST WAY 3.jpg", "1-ST WAY 4.jpg", "1-ST WAY 5.jpg", "1-ST WAY 6.jpg"]
    photo_nd = ["2-ND WAY 0.jpg", "2-ND WAY 1.jpg", "2-ND WAY 2.jpg", "2-ND WAY 3.jpg", "2-ND WAY 4.jpg"]

    photo = ["", ""]


    stage_param = {
        "null"             : None,
        "discount_5_ton"   : "discount_5_ton",
        "energy_get"       : "energy_get",
        "boost_get"        : "boost_get",
        "epic_clothes"     : "epic_clothes",
        "discount_10_ton"  : "discount_10_ton",
        "get_nft"          : "get_nft"
    }

    count_refer = base_refer.GetScore(tg_id)
    set_count, flag_open, stage = base_refer.GetReferStatus(tg_id)

    if count_refer >= set_count:
        if count_refer == 3 and flag_open == 'open' and stage == stage_param["null"]:

            # flag_open = False
            stage = stage_param["discount_5_ton"]
            set_count = 3

            param["discount_flag"] = True
            param["discount_count"] = 5
            param["discount_param"] = 3

            photo[0] = photo_st[1]
        
        elif count_refer == 5 and flag_open == 'open' and stage == stage_param["discount_5_ton"]:

            # flag_open = False
            stage = stage_param["energy_get"]
            set_count = 5

            param["energy_flag"] = True
            param["energy_count"] = 1
            param["energy_param"] = 5

            photo[0] = photo_st[2]
        
        elif count_refer == 10 and flag_open == 'open' and stage == stage_param["energy_get"]:

            stage = stage_param["boost_get"]
            set_count = 10

            param["boost_flag"] = True
            param["boost_count"] = 2
            param["boost_param"] = 10

            photo[0] = photo_st[3]
        
        elif count_refer == 15 and flag_open == 'open' and stage == stage_param["boost_get"]:

            stage = stage_param["epic_clothes"]
            set_count = 15

            photo[0] = photo_st[4]

            # Что-то написать чтобы один раз выдало рандомную нфтишку
        
        elif count_refer == 20 and flag_open == 'open' and stage == stage_param["epic_clothes"]:

            stage = stage_param["discount_10_ton"]
            set_count = 20

            photo[0] = photo_st[5]

            param["discount_flag"] = True
            param["discount_count"] = 10
            param["discount_param"] = 3
        
        elif count_refer == 90 and flag_open == 'open' and stage == stage_param["discount_10_ton"]:

            stage = stage_param["get_nft"]
            set_count = 90

            photo[0] = photo_st[6]
        
        else:
            photo[0] = photo_st[0]
            

            

    if count_refer >= 3 and count_refer < 5:
        param["discount_flag"] = True
        param["discount_count"] = 5
        param["discount_param"] = 3

        param["energy_flag"] = False

        param["boost_flag"] = False
 
