
from gc import callbacks
from os import access
from random import randint
import re
import telebot

import message as ms
from telebot import types # для указание типов
# import config
import bd

import enum
# import config
import sys
import operator
import referal_sys

from config import *




bd.Connect()






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
                                text="""
Введите номер вашего TON-кошелька💎
Если он совпадает с выведенным номером, то нажмите «✅ Да», если не совпадает, то нажмите «❌ Нет»
                                """,
                                reply_markup = markup)
    return mesg

def getUserLoginPassword(message):
    
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
                                text="""
Если он совпадает с выведенным номером, то нажмите «✅ Да», если не совпадает, то нажмите «❌ Нет»
                                """,
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



def getLogin(message):

    markup = types.InlineKeyboardMarkup()
    Yes = types.InlineKeyboardButton("Да", callback_data="Edit LoginPass: YES")
    No = types.InlineKeyboardButton("Нет", callback_data="Edit LoginPass: NO")
    # ChekNumber = types.InlineKeyboardButton("Проверить", callback_data="Edit score: Chek")
    Back = types.InlineKeyboardButton('⬅️ Назад', callback_data="Back")


    # number_score.append(message.text)

    markup.add(Yes, No, Back)

    return markup

# Меню покупки, режим 3
def BuyNFT(message, count):
                
    # param = bd.GetParam(bd.ParamStatus.get_news, tg_id=message.chat.id)

    # count = int(message.text[8:].replace('NFT', ''))
    
    # for index in range(param["count_stage"]):
    #     if param["param_factor"][index] == count and param["param_status"][index] == 'идёт в данный момент' and (param["param_avalible"][index] - param["param_sale"][index]) > 0:

    if count == 1:
        score = 20

    elif count == 3:
        score = 55

    elif count == 5:
        score = 75

    elif count == 10:
        score = 140
    
    bot.send_message(message.chat.id, text="Для покупки отправьте: {score} Ton\nНа счет:".format(score= score))

    bot.send_message(message.chat.id, text=f"`{bd.GetParam(bd.ParamStatus.get_mainTON)}`", parse_mode="Markdown")

    markup = types.InlineKeyboardMarkup()
    succsfull = types.InlineKeyboardButton("💎Подтвердить перевод💎", callback_data='transfer_conf')
    back = types.InlineKeyboardButton("⬅️ Назад", callback_data='Back')

    markup.add(succsfull, back)


    bot.send_message(message.chat.id, text="После перевода подтвердите перевод", reply_markup=markup)

    bd.NewSale(message.chat.id, count, score)

    #         break
                    
    #     else:
    #         flag_stage = True

    # if flag_stage:   
    #     bot.send_message(message.chat.id, text='🔐Этап ещё не наступил🔐')
        
# Возврат в меню
def BackMenu(message):
    bot.send_message(message.chat.id, text=ms.DayNews(message.chat.id), reply_markup = MainMenu(message))

def ChekUser(message, id_refer):
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

    bd.SetCapcha(message.chat.id, capcha_id, id_refer)

    print("[Set Capcha]", capcha_id, capcha)

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

def LoginPass(message):
    text = message.text
    login = text[:text.find("\n")]
    passwd = text[text.find("\n"):]

    bot.send_message(message.chat.id,
                        text="Ваш логин и пароль совпадают?\n"
                             f"Логие:`{login}\n"
                             f"Пароль:{passwd}`",
                             parse_mode="Markdown",
                        reply_markup=getLogin(message))


def GoPlay(message):
    login = bd.GetPlayLogin(message)
    bot.send_message(message.chat.id, text=f"Ваш логин: `{login}`", parse_mode="Markdown")
    

    status = bd.WaitPassword(message)

    if status[0] == "Enter Succses":
        bot.send_message(message.chat.id, text=f"Ваш ключ для входа в игру:\n`{status[1]}`", parse_mode="Markdown")
        BackMenu(message)
    else:
        bot.send_message(message.chat.id, text="Доступ запрещен")
        BackMenu(message)

def StartPlay(message):

    print("[Start Play]")

    login_verifity = bd.GetShaLogin(message)

    print("[Start Play :: login_verifity]", login_verifity)

    if login_verifity == "LOGIN":


        bot.send_message(message.chat.id, text=f"Вы уже зарегестрированы в системе\n"
                                                "Повторное получение логина невозможно\n"
                                                "Для входа в личный кабинет пришлите ваш логин и пароль в одном сообщение, но с разных строк\n"
                                                "Пример\n\n"
                                                "`Ivan45\nkapusta`", parse_mode="Markdown")
    
    elif login_verifity == "NO LOGIN":
        chek_buy = bd.GetScoreNFT_Play(message.chat.id)

        if chek_buy == "YES":
            bot.send_message(message.chat.id,
                             text=f"Вы купили NFT из нашей коллекции\n"
                                    "За это Вы поучаете доступ к игре\n"
                                    "Для Регистрации в игре создайте логин и пароль, после чего отправьте боту в слудующем формате:\n"
                                    "Пример\n"
                                    "`Ivan45\nkapusta`\n"

                                    "После того как введёте нажмите на кнопку `Зарегестироватся`",
                                    parse_mode="Markdown",
                                    reply_markup=PlayRegistrMenu(message))

        elif chek_buy == "NO":
            bot.send_message(message.chat.id,
                             text="Вы ещё не купили ни одной NFT из нашей коллекции, купите для авторизации в игре\n",
                            reply_markup=BackMenu(message))
    

    


# Обработка команд

@bot.callback_query_handler(func = lambda call : True)
def ChekCapcha(call):
    # message = call.message
    global callback_capcha
    capcha_id = bd.GetCapcha(call.message.chat.id)
    print("[Get Capcha]", capcha_id, callback_capcha[capcha_id], "\n")

    if call.data == callback_capcha[capcha_id]:

        acsess = bd.GetAcsess(call.message.chat.id)

        if access:

            markup = types.InlineKeyboardMarkup()
            login = types.InlineKeyboardButton("💻 Зарегистрироваться", callback_data="login")
            markup.add(login)

            # print(call.message.chat.id)

            bot.send_photo(chat_id=call.message.chat.id,
                           photo=open("photo/ded_moroz.jpg", "rb"),
                           caption="💎TON ELEPHANTS💎\nПривет, {0.first_name}!\n{message}".format(call.from_user, message=ms.HellouText(call.message.chat.id)),
                           reply_markup=markup)

            # bot.edit_message_text(chat_id=call.message.chat.id, 
            #                         message_id=call.message.id, 
            #                         text="💎TON ELEPHANTS💎\nПривет, {0.first_name}!\n{message}".format(call.from_user, message=ms.HellouText(call.message.chat.id)),
            #                         reply_markup=markup)

            
            
            # print("OK")

        else:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                                    message_id=call.message.id, 
                                    text="💎TON ELEPHANTS💎\nПривет, {0.first_name}!\n{message}".format(call.from_user, message=ms.DayNews(call.message.chat.id))
                                )
        # elif acsess == bd.ParamList.time_close:
        #     bot.edit_message_text(chat_id=call.message.chat.id, 
        #                             message_id=call.message.id, 
        #                             text="💎TON ELEPHANTS💎\nПривет, {0.first_name}!\n{message}".format(call.from_user, message=ms.BlockTime(call.message.chat.id))
        #                         )

    elif call.data == "login":

        bd.NewUserNFT(call.message.chat.id, f"@{call.message.chat.username}")

        # bot.edit_message_text(chat_id=call.message.chat.id, 
        #                         message_id=call.message.id, 
        #                         text='✅ Вы успешно зарегистрировались')

        bot.edit_message_caption(chat_id=call.message.chat.id, 
                                message_id=call.message.id, 
                                caption='✅ Вы успешно зарегистрировались')

        bot.send_message(chat_id=call.message.chat.id, 
                         text="💎TON ELEPHANTS💎\nПривет, {0.first_name}!\n{message}".format(call.from_user, message=ms.BlockText(call.message.chat.id)),
                         reply_markup=MainMenu(call.message))
        
        

        
        # referal_sys.StartMessage(call.message)
    
    elif call.data == "my nft":
        
        bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.id, 
                                text='Возможные операции с NFT💎',
                                reply_markup=NFT_Menu(call.message))
    
    elif call.data == "refer programm":
        referal_sys.StartMessage(call.message)

    
    elif call.data == "my buy":
        
        bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.id, 
                                text='Ваши покупки \nNFT: {count}'.format(count=bd.GetScore(call.message.chat.id)),
                                reply_markup=NFT_Menu(call.message))

    elif call.data == "buy nft":
        if bd.ChekNumberScore(call.message.chat.id):

            markup = types.InlineKeyboardMarkup()

            param_stage, param_factor = bd.GetParam(bd.ParamStatus.get_factor)

            # btn = []
            # for i in range(param_stage):
            #     btn.append(types.KeyboardButton("Купить x{factor} NFT".format(factor=param_factor[i])))
            #     markup.add(btn[i])

            buy_x1 = types.InlineKeyboardButton("Купить х1 NFT", callback_data="buy x1")
            buy_x3 = types.InlineKeyboardButton("Купить х3 NFT", callback_data="buy x3")
            buy_x5 = types.InlineKeyboardButton("Купить х5 NFT", callback_data="buy x5")
            buy_x10 = types.InlineKeyboardButton("Купить х10 NFT", callback_data="buy x10")
                    
            back = types.InlineKeyboardButton("⬅️ Назад", callback_data="Back")

            markup.add(buy_x1, buy_x3, buy_x5, buy_x10, back)
                    
            bot.send_message(call.message.chat.id, text='Выберите покупку\n\n{news}'.format(news=ms.DayNews(call.message.chat.id)), reply_markup= markup)
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
                                text='Привязанный счёт 💳:\n `{score}`'.format(score=bd.GetReadNumberScore(call.message.chat.id)),
                                reply_markup=NFT_Menu(call.message), parse_mode="MarkDown")
    
    elif call.data == "Edit score: YES":
        index = call.message.text.find("\n") + 1
        # print(call.message.text[index:])
        bd.ToWriteNumberScore(call.message.chat.id, call.message.text[index:])
        bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.id, 
                                text="Номер счета успешно изменён", reply_markup=NFT_Menu(call.message))
        # flag = False
        # flag_text = False
        # number_score.clear()
        # ChekMenu(call.message)
    
    elif call.data == "Edit LoginPass: YES":
        index = call.message.text.find("\n") + 3
        # print(call.message.text[index:])

        text = call.message.text[index:]

        login = text[:text.find("\n")]
        passwd = text[text.find("\n"):]

        bd.ToWriteLoginPass(call.message.chat.id, login, passwd)
        bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.id, 
                                text="Аккаунт успешно создан, не теряйте логин и пароль!", reply_markup=NFT_Menu(call.message))


    elif call.data == "RegistrInPlay":
        mesg = getUserLoginPassword(call.message)
        bot.register_next_step_handler(mesg, LoginPass)
    

    elif call.data == "Edit score: No":
        bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.id, 
                                text="Попробуйте ещё раз")
        
        
    elif call.data == "transfer_conf":

        param = bd.GetParam(bd.ParamStatus.get_news, tg_id=call.message.chat.id)
        count, score, index = bd.GetSale(call.message.chat.id)

        # if param["param_sale"][index] >= param["param_avalible"][index]:
        #     bot.edit_message_text(chat_id=call.message.chat.id, 
        #                         message_id=call.message.id, 
        #                         text='❌Все распродано, этап завершён❌', reply_markup=MainMenu(call.message))

        markup = types.InlineKeyboardMarkup()
       
        Back = types.InlineKeyboardButton('⬅️ Назад', callback_data="Back")


        # number_score.append(message.text)

        markup.add(Back)
        
        bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.id, 
                                text='Проверка наличия транзакции\n Время подтверждения может занимать от одной до трёх минут',
                                reply_markup=markup)

        flag = bd.ToWriteBdNFT(call.message.chat.id)
        

        if flag:

            text = """Поздравляем! 

Вы купили {count} NFT Ton Elephants🐘

При покупке на Новогоднем Pre-Sale вы получаете эксклюзивную одежду в виде зимнего свитера🥳

Носите на здоровье😉
Команда Ton Elephants🐘""".format(count = count)

            bot.send_photo(chat_id=call.message.chat.id,
                           photo=open("photo/switer.jpg", "rb"),
                           caption=text,
                           reply_markup=NFT_Menu(call.message))
        else:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.id, 
                                text='❌Ошибка транзакции❌', reply_markup=NFT_Menu(call.message))
        
    elif call.data == "Back":
        bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.id, 
                                text="Главное меню", reply_markup=NFT_Menu(call.message))
    
    elif call.data == "BackToMain":
        bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.id, 
                                text="Главное меню", reply_markup=MainMenu(call.message))

    elif call.data == "GoPlay":
        bot.edit_message_text(chat_id=call.message.chat.id, 
                              message_id=call.message.id,
                                text="Чтобы войти в игру Вам необходимо получить Ваш уникальный логин, который пришлёт наш бот\n"
                                     "После чего Вам необходимо вставить логин в игру и дождатся когда бот пришёл код\n"
                                     "Если Вы входите в игру не первый раз, то Вы можете воспользоватся уже ранее плученным логином,"
                                     " если Вы забыли - можете запросить логин повторно",
                                reply_markup=GoPlay(call.message))
    
    elif call.data == "New Play":
        bot.edit_message_text(chat_id=call.message.chat.id, 
                              message_id=call.message.id,
                                text="Чтобы войти в игру Вам необходимо иметь на Вашем счету хотя бы одну NFT из нашей коллекции\n"
                                     "Если вы ещё не купили нашу NFT, то переходите в соотвествующее меню\n")
        StartPlay(call.message)

    elif call.data == "updateDate":
        refer_id = referal_sys.baseRefer.GetIdRefer(call.message.chat.id)
        if refer_id != None:
            referal_sys.chek_sub_channel(bot.get_chat_member(chat_id=referal_sys.CHANEL_ID, user_id=call.message.chat.id),
                        bot.get_chat_member(chat_id=referal_sys.GRUPP_ID, user_id=call.message.chat.id),
                        call.message.chat.id, ref_id=refer_id
                        )
        else:
            referal_sys.chek_sub_channel(bot.get_chat_member(chat_id=referal_sys.CHANEL_ID, user_id=call.message.chat.id),
                        bot.get_chat_member(chat_id=referal_sys.GRUPP_ID, user_id=call.message.chat.id),
                        call.message.chat.id, ref_id=refer_id
                        )
        
    elif call.data == "getReferUrl":
        referal_sys.baseRefer.NewUser(call.message.chat.id)
        bot.send_message(call.message.chat.id,
                        text="Ваша уникальная ссылка:"
                            "\n`{url}`".format(url=referal_sys.main_url + str(call.message.chat.id)),
                        reply_markup=show_data_user(call.message.chat.id), parse_mode="MarkDown"
                        )

    elif call.data == "getScore":
        bot.send_message(call.message.chat.id, text="Ваш счет: {count}".format(count=referal_sys.baseRefer.GetScore(call.message.chat.id)))
    
    elif call.data == "myUrl":
        bot.send_message(call.message.chat.id,
                            text="Ваша уникальная ссылка:\n`{url}`".format(url=referal_sys.main_url + str(call.message.chat.id)),
                            parse_mode="MarkDown"
                        )
    
    elif call.data == "GetInfoRefer":

        markup = types.InlineKeyboardMarkup()
        back_Refer = types.InlineKeyboardButton(text="⚙️ Вернутся в главное меню", callback_data="refer programm")


        markup.add(back_Refer)
        text = """Вы заинтересовались реферальной программой? Давайте мы вам всё расскажем👌🏻
В чём смысл реферальной программы?
Всё очень просто. Вы приглашаете как можно больше людей и получаете награды в игре, а так же автоматически участвуете в частых розыгрышах только для участников реферальной программы Ton Elephants🐘💎

Следите за новостями, 
Команда Ton Elephants🐘💎"""
        bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.id, 
                                text=text,
                                reply_markup=markup)

    elif call.data == "buy x1":
        BuyNFT(call.message, 1)
    
    elif call.data == "buy x3":
        BuyNFT(call.message, 3)

    elif call.data == "buy x5":
        BuyNFT(call.message, 5)

    elif call.data == "buy x10":
        BuyNFT(call.message, 10)
    
    elif call.data == "getAllUser":
        referal_sys.GetInfoUser()

    else:
        bot.send_message(call.message.chat.id, text="💎TON ELEPHANTS💎\nПривет, {0.first_name}!\n{message}".format(call.from_user, message=ms.BadText()))
    
    

           


# Проверка команды старт
@bot.message_handler(commands=['start'])
def start_handler(message):
    id_refer = message.text[7:]

    if id_refer == "":
        id_refer = 0
    else:
        id_refer = int(id_refer)
    ChekUser(message, id_refer)
    
    


    
@bot.message_handler(content_types=['text'])
def boot_message(message):
    
    if message.chat.type == 'private':

        print("[User index Text]", message.text.index)

    
 


# Изменение параметров через командную строку
# command = sys.stdin.readline()
# if (len(command) != 0):
#     ms.c_m.EditParam(command[:-1])
    


bot.infinity_polling(timeout=30, long_polling_timeout = 10)