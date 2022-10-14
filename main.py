from email import message
from gc import callbacks
from random import randint
import re
import telebot
import message as ms
from telebot import types # для указание типов
# import config
import bd


callback_capcha = ['👥', '👾', '🐰', '🍀', '🍌']
flag_capcha = False

bd.Connect()

#main variables
TOKEN = "5628398708:AAEL5B1CuGzQ4tHTF4Y6hjXyflL2Do2fjYU"
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
    
    markup = types.InlineKeyboardMarkup()
    # Yes = types.InlineKeyboardButton("Да", callback_data="Edit score: YES")
    # No = types.InlineKeyboardButton("Нет", callback_data="Edit score: NO")
    # ChekNumber = types.InlineKeyboardButton("Проверить", callback_data="Edit score: Chek")
    Back = types.InlineKeyboardButton('⬅️ Назад', callback_data="Back")


    # number_score.append(message.text)

    markup.add(Back)
    # bot.send_message(message.chat.id, text="Введите номер вашего счета, если он совпадает с выведенными номером, "
    #                                  "нажми Да, если нет, то Нет", reply_markup = markup)
    mesg = bot.edit_message_text(chat_id=message.chat.id, 
                                message_id=message.id, 
                                text="Введите номер вашего счета, если он совпадает с выведенными номером, "
                                     "нажми Да, если нет, то Нет",
                                reply_markup = markup)
    return mesg

    

# Получение номера тон счета, режим 4
def getQ(message):

    markup = types.InlineKeyboardMarkup()
    Yes = types.InlineKeyboardButton("Да", callback_data="Edit score: YES")
    No = types.InlineKeyboardButton("Нет", callback_data="Edit score: NO")
    # ChekNumber = types.InlineKeyboardButton("Проверить", callback_data="Edit score: Chek")
    Back = types.InlineKeyboardButton('⬅️ Назад', callback_data="Back")


    # number_score.append(message.text)

    markup.add(Yes, No, Back)

    return markup


# Меню покупки, режим 3
def BuyNFT(message):
                
    param = bd.GetParam(bd.ParamStatus.get_news)

    count = int(message.text[8:].replace('NFT', ''))
    
    for index in range(param["count_stage"]):
        if param["param_factor"][index] == count and param["param_status"][index] == 'идёт в данный момент' and (param["param_avalible"][index] - param["param_sale"][index]) > 0:

            score = count * param["coast"]
            bot.send_message(message.chat.id, text="Для покупки отправьте: {score} Ton\nНа счет:".format(score= score))

            bot.send_message(message.chat.id, text=f"`{bd.GetParam(bd.ParamStatus.get_mainTON)}`", parse_mode="Markdown")

            markup = types.InlineKeyboardMarkup()
            succsfull = types.InlineKeyboardButton("💎Подтвердить перевод💎", callback_data='transfer_conf')
            back = types.InlineKeyboardButton("⬅️ Назад", callback_data='Back')

            markup.add(succsfull, back)

            flag_stage = False

            bot.send_message(message.chat.id, text="После перевода подтвердите перевод", reply_markup=markup)

            bd.NewSale(message.chat.id, count, score, index)

            break
                    
        else:
            flag_stage = True

    if flag_stage:   
        bot.send_message(message.chat.id, text='🔐Этап ещё не наступил🔐')
        
# Возврат в меню
def BackMenu(message):
    bot.send_message(message.chat.id, text=ms.DayNews(), reply_markup = MainMenu(message))

def ChekUser(message):
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # capcha_one = types.KeyboardButton(text=callback_capcha[0])
    # capcha_two = types.KeyboardButton(text=callback_capcha[1])
    # capcha_tree = types.KeyboardButton(text=callback_capcha[2])
    # capcha_four = types.KeyboardButton(text=callback_capcha[3])
    # capcha_five = types.KeyboardButton(text=callback_capcha[4])


    markup = types.InlineKeyboardMarkup()

    capcha_one = types.InlineKeyboardButton(text=callback_capcha[0], callback_data=callback_capcha[0])
    capcha_two = types.InlineKeyboardButton(text=callback_capcha[1], callback_data=callback_capcha[1])
    capcha_tree = types.InlineKeyboardButton(text=callback_capcha[2], callback_data=callback_capcha[2])
    capcha_four = types.InlineKeyboardButton(text=callback_capcha[3], callback_data=callback_capcha[3])
    capcha_five = types.InlineKeyboardButton(text=callback_capcha[4], callback_data=callback_capcha[4])

    markup.add(capcha_one, capcha_two, capcha_tree, capcha_four, capcha_five)
    
    markup.row_width = 2

    capcha_id = randint(0, 4)

    capcha = callback_capcha[capcha_id]

    bd.SetCapcha(message.chat.id, capcha_id)

    bot.send_message(message.chat.id, text="Для обеспечения безопастности, необходимо пройти проверку\n"
                                            "Для этого, найдите и выберите одинаковый изобраения\n"
                                            f"{capcha}",
                    reply_markup=markup
    )


def ChekScore(message):
    bot.send_message(message.chat.id,
                        text="Номер вашего счета введён правильно?\n"
                             f"{message.text}",
                        reply_markup=getQ(message))

# Обработка команд

@bot.callback_query_handler(func = lambda call : True)
def ChekCapcha(call):
    # message = call.message
    global callback_capcha
    capcha_id = bd.GetCapcha(call.message.chat.id)
    if call.data == callback_capcha[capcha_id]:

        markup = types.InlineKeyboardMarkup()
        login = types.InlineKeyboardButton("💻 Зарегистрироваться", callback_data="login")
        markup.add(login)

        bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.id, 
                                text="💎TON ELEPHANTS💎\nПривет, {0.first_name}!\n{message}".format(call.from_user, message=ms.HellouText()),
                                reply_markup=markup)

    elif call.data == "login":

        bd.NewUserNFT(call.message.chat.id, f"@{call.message.chat.username}")

        bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.id, 
                                text='✅ Вы успешно зарегистрировались',
                                reply_markup= MainMenu(call.message))

    
    elif call.data == "my buy":
        
        bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.id, 
                                text='Ваши покупки \nNFT: {count}'.format(count=bd.GetScore(call.message.chat.id)),
                                reply_markup=MainMenu(call.message))

    elif call.data == "buy nft":
        if bd.ChekNumberScore(call.message.chat.id):

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            param_stage, param_factor = bd.GetParam(bd.ParamStatus.get_factor)

            btn = []
            for i in range(param_stage):
                btn.append(types.KeyboardButton("Купить x{factor} NFT".format(factor=param_factor[i])))
                markup.add(btn[i])
                    
            back = types.KeyboardButton("⬅️ Назад")

            markup.add(back)
                    
            bot.send_message(call.message.chat.id, text='Выберите покупку\n\n{news}'.format(news=ms.DayNews()), reply_markup= markup)
            # BuyNFT(call.message)
                
        else:
            bot.send_message(call.message.chat.id, text='Вы не ввели номер счета 😢\nВведите номер счета для того, чтобы совершить покупку:')
            flag = True
    
    elif call.data == "edit number":
        mesg = getUserAdressNFT(call.message)
        bot.register_next_step_handler(mesg, ChekScore)
        # getUserAdressNFT(message)
    
    elif call.data == "chek score":
        bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.id, 
                                text='Привязанный счет: {score}'.format(score=bd.GetReadNumberScore(call.message.chat.id)),
                                reply_markup=MainMenu(call.message))
    
    elif call.data == "Edit score: YES":
        index = call.message.text.find("\n") + 1
        # print(call.message.text[index:])
        bd.ToWriteNumberScore(call.message.chat.id, call.message.text[index:])
        bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.id, 
                                text="Номер счета успешно изменён", reply_markup=MainMenu(call.message))
        # flag = False
        # flag_text = False
        # number_score.clear()
        ChekMenu(call.message)

    elif call.data == "Edit score: No":
        bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.id, 
                                text="Попробуйте ещё раз")
        
        
    elif call.data == "transfer_conf":

        param = bd.GetParam(bd.ParamStatus.get_news)
        count, score, index = bd.GetSale(call.message.chat.id)

        if param["param_sale"][index] >= param["param_avalible"][index]:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.id, 
                                text='❌Все распродано, этап завершён❌', reply_markup=MainMenu(call.message))
        
        else:

            flag = bd.ToWriteBdNFT(call.message.chat.id)
            

            if flag:

                markup = types.InlineKeyboardMarkup()
                btn2 = types.InlineKeyboardButton("💵 Купить NFT", callback_data="buy nft")
                back = types.InlineKeyboardButton("⬅️ Назад", callback_data='Back')

                markup.add(btn2, back)

                bot.edit_message_text(chat_id=call.message.chat.id, 
                                    message_id=call.message.id, 
                                    text='Вы успешно купили {count} слонов'.format(count=count), reply_markup=markup)
            else:
                bot.edit_message_text(chat_id=call.message.chat.id, 
                                    message_id=call.message.id, 
                                    text='❌Ошибка транзакции❌', reply_markup=MainMenu(call.message))
        
    elif call.data == "Back":
        bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.id, 
                                text="Главное меню", reply_markup=MainMenu(call.message))
    else:
        bot.send_message(call.message.chat.id, text="💎TON ELEPHANTS💎\nПривет, {0.first_name}!\n{message}".format(call.from_user, message=ms.BadText()))
    
    

           


# Проверка команды старт
@bot.message_handler(commands=['start'])
def start_handler(message):

    ChekUser(message)

    
@bot.message_handler(content_types=['text'])
def boot_message(message):
    
    if message.chat.type == 'private':
        
        if message.text == '⬅️ Назад':
            bot.send_message(message.chat.id, text="Отмена операции", reply_markup=DotMenu(message))
            bot.send_message(message.chat.id, text="Главное меню", reply_markup=MainMenu(message))

        
        elif message.text[:8] == 'Купить x':
            BuyNFT(message)

    
 


# Изменение параметров через командную строку
# command = sys.stdin.readline()
# if (len(command) != 0):
#     ms.c_m.EditParam(command[:-1])
    


bot.infinity_polling(timeout=30, long_polling_timeout = 10)