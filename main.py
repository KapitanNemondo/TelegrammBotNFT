from email import message
from gc import callbacks
from random import randint
import telebot
import message as ms
from telebot import types # для указание типов
# import config
import bd
import sys


flag = False
flag_text = False

number_score = []

count = 0
score = 0

callback_capcha = ['👥', '👾', '🐰', '🍀', '🍌']
flag_capcha = False
capcha_id = -1

#main variables
TOKEN = "5441817147:AAE7iPvtrJuWpgVcmIvvjs0snF70pdrSKvw"
bot = telebot.TeleBot(TOKEN)

def DotMenu(message):
    markup = types.ReplyKeyboardRemove()
    return markup

def MainMenu(message):      # Главное меню
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton("💼 Мои покупки", callback_data="my buy")
    btn2 = types.InlineKeyboardButton("💵 Купить NFT", callback_data="buy nft")
    btn3 = types.InlineKeyboardButton("💰 Изменить номер счета", callback_data="edit number")
    btn4 = types.InlineKeyboardButton("🏦 Проверить счет", callback_data="chek score")
    markup.add(btn1, btn2, btn3, btn4)

    return markup


# Получение номера тон счета, режим 4
def getUserAdressNFT(message):
    
    global number_score

    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Yes = types.KeyboardButton("Да")
    No = types.KeyboardButton("Нет")
    Back = types.KeyboardButton('⬅️ Назад')


    number_score.append(message.text)

    markup.add(Yes, No, Back)
    bot.send_message(message.chat.id, text="Номер вашего счета совпадает?\n {text}".format(text=number_score[0]), reply_markup = markup)

    

    if message.text == "Да":
        bd.ToWriteNumberScore(message.chat.id, number_score[0])
        bot.send_message(message.chat.id, text="Номер счета успешно добавлен", reply_markup=MainMenu(message))
        flag = False
        flag_text = False
        number_score.clear()
        ChekMenu(message)
    elif message.text == "Нет":
        bot.send_message(message.chat.id, text="Попробуйте ещё раз")
        flag = True
        flag_text = False
        number_score.clear()
    elif message.text == '⬅️ Назад':
        bot.send_message(message.chat.id, text="Отмена операции", reply_markup=MainMenu(message))
        flag = False
        flag_text = False
        number_score.clear()
        ChekMenu(message)

# Меню покупки, режим 3
def BuyNFT(message):

    global count, score
                
    ms.c_m.GetParam()

    count = int(message.text[8:].replace('NFT', ''))
    
    for index in range(ms.c_m.param_stage):
        if ms.c_m.param_factor[index] == count and ms.c_m.param_status[index] == 'идёт в данный момент':
            ms.c_m.GetParam()
            score = count * ms.c_m.param_cost
            bot.send_message(message.chat.id, text="Для покупки отправьте: {score} Ton\nНа счет:".format(score= score))
            bot.send_message(message.chat.id, text=bd.TON_NUMBER)

            succsfull = types.KeyboardButton("💎Подтвердить перевод💎")
            back = types.KeyboardButton("⬅️ Назад")

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(succsfull, back)

            flag_stage = False

            bot.send_message(message.chat.id, text="После перевода подтвердите перевод", reply_markup=markup)

            break
                    
        else:
            flag_stage = True

    if flag_stage:   
        bot.send_message(message.chat.id, text='🔐Этап ещё не наступил🔐')
        
   

# Меню, режим 2 -----
def ChekMenu(message):

    global flag

    if message.text == '💼 Мои покупки':
        bot.send_message(message.chat.id, text='Ваши покупки \nNFT: {count}'.format(count=bd.GetScore(message.chat.id)))

    elif message.text == '💵 Купить NFT':

        if bd.ChekNumberScore(message.chat.id):

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            btn = []
            for i in range(ms.c_m.param_stage):
                btn.append(types.KeyboardButton("Купить x{factor} NFT".format(factor=ms.c_m.param_factor[i])))
                markup.add(btn[i])
                    
            back = types.KeyboardButton("⬅️ Назад")

            markup.add(back)
                    
            bot.send_message(message.chat.id, text='Выберите покупку\n\n{news}'.format(news=ms.DayNews()), reply_markup= markup)
            BuyNFT(message)
                
        else:
            bot.send_message(message.chat.id, text='Вы не ввели номер счета 😢\nВведите номер счета для того, чтобы совершить покупку:')
            flag = True

    elif message.text == '💰 Изменить номер счета':
        bot.send_message(message.chat.id, text='Введите номер счета:')
        getUserAdressNFT(message)
        
    elif message.text == '🏦 Проверить счет':
        #bot.send_message(message.chat.id, text='Текущий счет: {score} ₽'.format(score=bd.GetScore(message.chat.id)))
        bot.send_message(message.chat.id, text='Привязанный счет: {score}'.format(score=bd.GetReadNumberScore(message.chat.id)))

# Возврат в меню
def BackMenu(message):
    bot.send_message(message.chat.id, text=ms.DayNews(), reply_markup = MainMenu(message))
    ChekMenu(message)

def ChekUser(message):
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # capcha_one = types.KeyboardButton(text=callback_capcha[0])
    # capcha_two = types.KeyboardButton(text=callback_capcha[1])
    # capcha_tree = types.KeyboardButton(text=callback_capcha[2])
    # capcha_four = types.KeyboardButton(text=callback_capcha[3])
    # capcha_five = types.KeyboardButton(text=callback_capcha[4])

    global capcha_id

    markup = types.InlineKeyboardMarkup()

    capcha_one = types.InlineKeyboardButton(text=callback_capcha[0], callback_data=callback_capcha[0])
    capcha_two = types.InlineKeyboardButton(text=callback_capcha[1], callback_data=callback_capcha[1])
    capcha_tree = types.InlineKeyboardButton(text=callback_capcha[2], callback_data=callback_capcha[2])
    capcha_four = types.InlineKeyboardButton(text=callback_capcha[3], callback_data=callback_capcha[3])
    capcha_five = types.InlineKeyboardButton(text=callback_capcha[4], callback_data=callback_capcha[4])

    markup.add(capcha_one, capcha_two, capcha_tree, capcha_four, capcha_five)
    
    markup.row_width = 2

    capcha_id = callback_capcha[randint(0, 4)]

    bot.send_message(message.chat.id, text="Для обеспечения безопастности, необходимо пройти проверку\n"
                                            "Для этого, найдите и выберите одинаковый изобраения\n"
                                            f"{capcha_id}",
                    reply_markup=markup
    )


# Обработка команд

@bot.callback_query_handler(func = lambda call : True)
def ChekCapcha(call):
    global capcha_id
    message = call.message
    if call.data == capcha_id:

        

        markup = types.InlineKeyboardMarkup()
        login = types.InlineKeyboardButton("💻 Зарегистрироваться", callback_data="login")
        markup.add(login)

        bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.id, 
                                text="💎TON ELEPHANTS💎\nПривет, {0.first_name}!\n{message}".format(call.from_user, message=ms.HellouText()),
                                reply_markup=markup)

    elif call.data == "login":
        bd.NewUserNFT(call.message.chat.id)

        bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.id, 
                                text='✅ Вы успешно зарегистрировались',
                                reply_markup= MainMenu(call.message))

        ChekMenu(call.message)
    
    elif call.data == "my buy":
        message = call.message
        bot.send_message(message.chat.id, text='Ваши покупки \nNFT: {count}'.format(count=bd.GetScore(message.chat.id)))

    elif call.data == "buy nft":
        if bd.ChekNumberScore(message.chat.id):

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            btn = []
            for i in range(ms.c_m.param_stage):
                btn.append(types.KeyboardButton("Купить x{factor} NFT".format(factor=ms.c_m.param_factor[i])))
                markup.add(btn[i])
                    
            back = types.KeyboardButton("⬅️ Назад")

            markup.add(back)
                    
            bot.send_message(message.chat.id, text='Выберите покупку\n\n{news}'.format(news=ms.DayNews()), reply_markup= markup)
            BuyNFT(message)
                
        else:
            bot.send_message(message.chat.id, text='Вы не ввели номер счета 😢\nВведите номер счета для того, чтобы совершить покупку:')
            flag = True
    
    elif call.data == "edit number":
        bot.send_message(message.chat.id, text='Введите номер счета:')
        getUserAdressNFT(message)
    
    elif call.data == "chek score":
        bot.send_message(message.chat.id, text='Привязанный счет: {score}'.format(score=bd.GetReadNumberScore(message.chat.id)))

    else:
        bot.send_message(call.message.chat.id, text="💎TON ELEPHANTS💎\nПривет, {0.first_name}!\n{message}".format(call.from_user, message=ms.BadText()))
    
    

           
@bot.message_handler(commands=['reset'])
def reset(message):
    bot.send_message(message.chat.id, text="💎TON ELEPHANTS💎\nПривет, {0.first_name}!\n{message}".format(message.from_user, message=ms.HellouText()), reply_markup = MainMenu(message))

# Проверка команды старт
@bot.message_handler(commands=['start'])
def start_handler(message):

    ChekUser(message)

    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # login = types.KeyboardButton("💻 Зарегистрироваться")

    
    # if ChekUser(message):
    #     markup.add(login)
    #     bot.send_message(message.chat.id, text="💎TON ELEPHANTS💎\nПривет, {0.first_name}!\n{message}".format(message.from_user, message=ms.HellouText()))

@bot.message_handler(content_types=['text'])
def boot_message(message):
    
    if message.chat.type == 'private':
        
        if message.text == '⬅️ Назад':
            bot.send_message(message.chat.id, text="Отмена операции", reply_markup=DotMenu(message))
            bot.send_message(message.chat.id, text="Главное меню", reply_markup=MainMenu(message))

            ChekMenu(message)
        
        elif message.text[:8] == 'Купить x':
            BuyNFT(message)

        elif message.text == '💎Подтвердить перевод💎':
            flag = bd.ToWriteBdNFT(message.chat.id, count, score)

            if flag:
                bot.send_message(message.chat.id, text='Вы успешно купили {count} слонов'.format(count=count))
            else:
                bot.send_message(message.chat.id, text='❌Ошибка транзакции❌')

        
        
            # if message.text == capcha_id:
            #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            #     login = types.KeyboardButton("💻 Зарегистрироваться")

            #     markup.add(login)

            #     bot.send_message(message.chat.id, text="💎TON ELEPHANTS💎\nПривет, {0.first_name}!\n{message}".format(message.from_user, message=ms.HellouText()))

            #     flag_capcha = True
 


# Изменение параметров через командную строку
# command = sys.stdin.readline()
# if (len(command) != 0):
#     ms.c_m.EditParam(command[:-1])
    


bot.infinity_polling(timeout=30, long_polling_timeout = 10)