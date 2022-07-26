import telebot
import message as ms
from telebot import types # для указание типов
# import config
import bd
import sys


flag = False
flag_text = False
number_score = []
regim = 2
count = 0
score = 0

#main variables
TOKEN = "5441817147:AAE7iPvtrJuWpgVcmIvvjs0snF70pdrSKvw"
bot = telebot.TeleBot(TOKEN)


def MainMenu(message):      # Главное меню
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton("💼 Мои покупки")
    btn2 = types.KeyboardButton("💵 Купить NFT")
    btn3 = types.KeyboardButton("💰 Изменить номер счета")
    btn4 = types.KeyboardButton("🏦 Проверить счет")
    markup.add(btn1, btn2, btn3, btn4)

    return markup

@bot.message_handler(commands=['reset'])
def reset(message):
    bot.send_message(message.chat.id, text="💎TON ELEPHANTS💎\nПривет, {0.first_name}!\n{message}".format(message.from_user, message=ms.HellouText()), reply_markup = MainMenu(message))

# Проверка команды старт
@bot.message_handler(commands=['start'])
def start_handler(message):
    global regim
    regim = 1
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    login = types.KeyboardButton("💻 Зарегистрироватся")

    markup.add(login)
    bot.send_message(message.chat.id, text="💎TON ELEPHANTS💎\nПривет, {0.first_name}!\n{message}".format(message.from_user, message=ms.HellouText()), reply_markup = markup)

# Получение номера тон счета, режим 4
def getUserAdressNFT(message):
    global regim
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
        regim = 2
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
        regim = 2

# Меню покупки, режим 3
def BuyNFT(message):

    global regim, count, score

    if message.text[:8] == 'Купить x':
                
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
            
    elif message.text == '💎Подтвердить перевод💎':
        flag = bd.ToWriteBdNFT(message.chat.id, count, score)

        if flag:
            bot.send_message(message.chat.id, text='Вы успешно купили {count} слонов'.format(count=count))
        else:
            bot.send_message(message.chat.id, text='❌Ошибка транзакции❌')
            flag_stage = False 

    elif message.text == '⬅️ Назад':
        BackMenu(message)    

# Меню, режим 2
def ChekMenu(message):

    global regim, flag

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
            regim = 3
                
        else:
            bot.send_message(message.chat.id, text='Вы не ввели номер счета 😢\nВведите номер счета для того, чтобы совершить покупку:')
            flag = True

    elif message.text == '💰 Изменить номер счета':
        bot.send_message(message.chat.id, text='Введите номер счета:')
        regim = 4
        
    elif message.text == '🏦 Проверить счет':
        #bot.send_message(message.chat.id, text='Текущий счет: {score} ₽'.format(score=bd.GetScore(message.chat.id)))
        bot.send_message(message.chat.id, text='Привязанный счет: {score}'.format(score=bd.GetReadNumberScore(message.chat.id)))

# Возврат в меню
def BackMenu(message):
    global regim
    bot.send_message(message.chat.id, text=ms.DayNews(), reply_markup = MainMenu(message))
    regim = 2

# Обработка команд
@bot.message_handler(content_types=['text'])
def boot_message(message):
    global flag, regim
    
    if message.chat.type == 'private':

        if regim == 1:          # Режим регистрации
            if message.text == '💻 Зарегистрироватся':
                bd.NewUserNFT(message.chat.id)

                bot.send_message(message.chat.id, text='✅ Вы успешно зарегистрировались', reply_markup= MainMenu(message))

                regim = 2
        
        elif regim == 2:        # Режим общего меню
            ChekMenu(message)
        elif regim == 3:        # Режим Покупки
            BuyNFT(message)
        elif regim == 4:        # Режим Получения адреса
            getUserAdressNFT(message)
        
        if message.text == '⬅️ Назад':
            bot.send_message(message.chat.id, text="Отмена операции", reply_markup=MainMenu(message))
            regim = 2
            



# Изменение параметров через командную строку
# command = sys.stdin.readline()
# if (len(command) != 0):
#     ms.c_m.EditParam(command[:-1])
    


bot.infinity_polling(timeout=30, long_polling_timeout = 10)