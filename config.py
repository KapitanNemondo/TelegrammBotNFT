
import telebot
from telebot import types
from presetBase import TOKEN, admin_list


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


    markup.add(get_info, url, stage_map, score, back_Menu)

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


