import baseReferData as baseRefer
import enum
import operator
from telebot import types # для указание типов
from config import bot, callback_capcha, flag_capcha, show_url_sub, show_data_user, new_refer_menu
from random import randint

CHANEL_ID = -1001688299683
"""ID канала в котором бот проверяет наличие подписки"""

GRUPP_ID = -1001747825412
"""ID чата в котором бот проверяет наличие подписки"""

main_url = 'https://t.me/ton_elephants_bot?start='

class InlineSet(enum.Enum):
    getReferUrl = 1
    updateDate = 2
    getScore = 3
    getAllUser = 4
    myUrl = 5
    search = 6

def ControllSkaner():
    """
    Проверка приглашенных пользователей на соответстиве требованиям конкурса:
    `Подписка на канал`, `подписка на чат`, `не бот`
    """
    dataUser = baseRefer.GetUser()
    goodUser = tuple()

    out = '🛡Нарушение правил розыгрыша🛡\n\n👮‍♀️Обнаруженные нарушители👮‍♀️:' + '\n' + '\n'

    count = 1
    predel = 15

    regim = baseRefer.GetConfig()

    for elem in dataUser:

        user = int(elem['tg_id_user'])

        dataGrupp = bot.get_chat_member(chat_id=GRUPP_ID, user_id= user)
        dataChanel = bot.get_chat_member(chat_id=CHANEL_ID, user_id= user)
        

        if dataChanel.status != 'left' and dataGrupp.status != 'left' and dataChanel.user.is_bot != True and dataGrupp.user.is_bot != True:
            bot.send_message(user, text="Подтвердите, что Вы не робот", reply_markup=show_data_user(user))
            pass
            
        else:
            out +=  f'Position:     {count}\n' \
                    f'Id User:      {user}\n' \
                    f'User name:    @{dataGrupp.user.username}\n' \
                    f'Chanel stat:  {dataChanel.status}\n'\
                    f'Grupp stat:   {dataGrupp.status}\n\n'

            count += 1

            refer = elem['tg_id_ref']

            """ !!! ------Обкатать перед запуском------ !!!"""
            baseRefer.SetCountRefer(refer, user)

        if count > predel:
            bot.send_message(baseRefer.admin_list[0], text=out)

            out = ''

            predel += 15
    bot.send_message(baseRefer.admin_list[0], text=out)
    bot.send_message(baseRefer.admin_list[0], text='Поиск окончен')
    


def GetInfoUser():
    """
    Получение данных о финалистах конкурса `Position`, `Id User`, `User name`, `Is bot`, `Count refer`
    """
    dataFinalist = baseRefer.GetFinalist()
    
    dataFinalist.sort(key=operator.itemgetter('count_refer'), reverse=True)

    out = 'Информация о финалистах:' + '\n' + '\n'

    count = 1
    predel = 50

    for elem in dataFinalist:

        user = int(elem['tg_id_ref'])

        
        data = bot.get_chat_member(chat_id=user, user_id=user)

        

        

        count_refer = baseRefer.FindItod(user)
        out +=  f'Position:     {count}\n' \
                f'User name:    @{data.user.username}\n' 
        #        f'Count refer:  {count_refer}\n\n'

        count += 1
#                   f'Id User:      {user}\n' \
#                    f'Is bot:       {data.user.is_bot}\n' \
        if count > predel:
            bot.send_message(baseRefer.admin_list[0], text=out)

            out = ''

            predel += 15
    bot.send_message(baseRefer.admin_list[0], text=out)

# ок
def _update():
    """Функция добавления кнопки `Обновить данные`"""
    markup = types.InlineKeyboardMarkup()
    

    # if ref_id != None:
    #     refer_id = ref_id
    # else:
    #     refer_id = None

    update = types.InlineKeyboardButton("Обновить данные", callback_data="updateDate")
    markup.add(update)

    return markup

# ок
def chek_sub_channel(chat_member_chal, chat_member_grupp, chat_id, message, ref_id=None):

    """
    Провекра подписки на телеграмм канал
    `chat_member` - словарь с данными о пользователе
    `chat_id` - id пользователя
    `ref_id` - id реферера по-умолчанию `None`

    """

    if ref_id != None:
        if chat_member_chal.status != 'left' and chat_member_grupp.status != 'left':
            # print("[Chek Sub Chanel] succesfull")
            baseRefer.UpdateCountRefer(ref_id, chat_id)

            getReferUrl = types.InlineKeyboardButton("🔗 Моя ссылка", callback_data="getReferUrl")

            

            return getReferUrl

        else:
            bot.edit_message_text(chat_id=message.chat.id, 
                                  message_id=message.id, 
                                  text="Подпишись на наши каналы и нажми на кнопку: Обновить данные", reply_markup=_update())
            return None
    else:
        if chat_member_chal.status != 'left' and chat_member_grupp.status != 'left':
            # print("[Chek Sub Chanel] succesfull")

            markup = types.InlineKeyboardMarkup()

            
            getReferUrl = types.InlineKeyboardButton("🔗 Моя ссылка", callback_data="getReferUrl")

            return getReferUrl
        
        else:
            bot.edit_message_text(chat_id=message.chat.id, 
                                  message_id=message.id, 
                                  text="Подпишись на наши каналы и нажми на кнопку: Обновить данные", reply_markup=_update())
            
            return None


def StartMessage(message):
    regim = baseRefer.GetConfig()
    id_refer = baseRefer.GetIdRefer(message.chat.id)

    print("[Regim]", regim)

    if regim == "open":

        print("[ID Refer]", id_refer)

        if id_refer == 0 or id_refer == None:


            chat_id = message.chat.id
            user = message.chat.first_name

            url = chek_sub_channel(bot.get_chat_member(chat_id=CHANEL_ID, user_id=message.chat.id),
                            bot.get_chat_member(chat_id=GRUPP_ID, user_id=message.chat.id),
                            message=message,
                            chat_id=message.chat.id
                            )

            if url != None:
                bot.edit_message_text(chat_id=message.chat.id, 
                                    message_id=message.id,
                                    text="Реферальная программа💎",
                                    reply_markup=new_refer_menu(message.chat.id, url))
            else:
                pass
            
            

            

        else:

            url = chek_sub_channel(bot.get_chat_member(chat_id=CHANEL_ID, user_id=message.chat.id),
                            bot.get_chat_member(chat_id=GRUPP_ID, user_id=message.chat.id),
                            message=message,
                            chat_id=message.chat.id,
                            ref_id=id_refer
                            )

            if url != None:
                bot.edit_message_text(chat_id=message.chat.id, 
                                    message_id=message.id,
                                    text="Реферальная программа💎",
                                    reply_markup=new_refer_menu(message.chat.id, url))
            else:
                pass
    elif regim == "close":
        bot.edit_message_text(chat_id=message.chat.id, 
                              message_id=message.id,
                              text="[Текст 3]",
                              reply_markup=show_data_user(message.chat.id))
    elif regim == "konez":
        bot.send_message(message.chat.id, text="[Текст 4]", reply_markup=types.ReplyKeyboardRemove())

def ChekUser(message, id_refer):
    global callback_capcha
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

    baseRefer.SetCapcha(message.chat.id, capcha_id, id_refer)

    bot.send_message(message.chat.id, text="Для обеспечения безопастности, необходимо пройти проверку\n"
                                            "Для этого, найдите и выберите одинаковый изображения\n"
                                            f"{capcha}",
                    reply_markup=markup
    )
    
