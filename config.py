
import telebot
from telebot import types

host = "localhost"
port = 3307
user = "root"
password = "takeoff_2018"
db_name = "NFT_Sale"
db_name_refer = "Referal"

# admin_list = [849231212, 493115134, 560945352]
# """ Еловский, Гозенко Артём, Гозенко Анатолий """

admin_list = [849231212, 485563456, 675564806]
""" Еловский, Краснов, Попов"""

# TON_NUMBER = "EQCA0vWJntuL61f1-xQB2EwMorKpI448L5sh9c1kC29f8D4V"

#main variables
TOKEN = "5590720904:AAHZe3EuakfrLjFI-3kChcaYdLjyh8I2Wss"
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


    btn5 = types.InlineKeyboardButton("🎮 Войти в игру", callback_data="GoPlay")

    chat_id = message.chat.id

    markup.add(btn1, btn2, log_inst, log_tg, log_chat)

    for elem in admin_list:
        if elem == chat_id:
            markup.add(btn5)

    

    return markup

def show_url_sub():
    """Вывод инлайн кнопки с подписками"""
    
    markup = types.InlineKeyboardMarkup()

    markup.row_width = 2

    log_inst = types.InlineKeyboardButton(text="Instagram", url='https://instagram.com/ton_elephants')
    log_tg = types.InlineKeyboardButton(text="Telegram", url='https://t.me/ton_elephants')
    log_chat = types.InlineKeyboardButton(text='Наш чат', url='https://t.me/+4w1S6lz5c3s2MzJi')


    markup.add(log_inst, log_tg, log_chat)
    return markup

def NFT_Menu(message):      # Главное меню
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton("💼 Мои покупки", callback_data="my buy")
    btn2 = types.InlineKeyboardButton("💵 Купить NFT", callback_data="buy nft")
    btn3 = types.InlineKeyboardButton("💰 Изменить номер счета", callback_data="edit number")
    btn4 = types.InlineKeyboardButton("🏦 Проверить счет", callback_data="chek score")

    btn5 = types.InlineKeyboardButton("🎮 Войти в игру", callback_data="GoPlay")

    chat_id = message.chat.id

    markup.add(btn1, btn2, btn3, btn4)

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


    url = types.InlineKeyboardButton('Моя ссылка', callback_data="myUrl")
    score = types.InlineKeyboardButton('Счет', callback_data="getScore")

    #get_all_score = types.KeyboardButton(text='Показать счет всех участников')

    get_info_all_user = types.InlineKeyboardButton('Информация об участниках', callback_data="getAllUser")

    #updata_bot = types.KeyboardButton(text='Обновить бота')

    policeBot = types.InlineKeyboardButton('Активировать сыщика', callback_data="search")

    # getAutorization = types.KeyboardButton(text='Я не робот')

    
    

    for elem in admin_list:
        if elem == chat_id:
            if elem == admin_list[0]:
                markup.add(score, get_info_all_user)

    markup.add(url, score)
    
    # elif regim == 2:
    #     markup.add(score, getAutorization)
    
    return markup
