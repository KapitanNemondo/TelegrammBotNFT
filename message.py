import bd


# Вывод текста при первом запуске бота, при вызове команды /start
def HellouText(tg_id):
    param = bd.GetParam(bd.ParamStatus.get_news, tg_id=tg_id)

    # print(param)
    start = """
Мы приветствуем тебя в официальном боте NFT-коллекции Ton Elephants🐘

Чтобы пользоваться всеми функциями бота, тебе необходимо зарегистрироваться😉
"""

    # text = "NFT Presale. Продажа x" + str(param["current_stage"]) + "\n \n"
    # hellou = "Добро пожаловать в бот для пересейла первых NFT. \nПродажа пройдёт в " + str(param["count_stage"]) + " этап:\n\n"

    # nft_score = ""

    # for i in range(param["param_stage"]):
    #     # nft_score += 'x' + str(param["param_factor"][i]) + ' NFT - ' + str(param["param_avalible"][i]) + ' штук - ' + str(param["param_status"][i]) + '\n'
    #     nft_score += 'x' + str(param["param_factor"][i]) + ' NFT - ' + str(param["param_status"][i]) + '\n'

    
    # end = "\nДля покупки достпуно: " + str(param["param_avalible"][param["current_stage"] - 1] - param["param_sale"][param["current_stage"] - 1]) + " из " + str(param["param_avalible"][param["current_stage"] - 1]) + " по цене " + str(param["coast"]) + " TON за 1 NFT"
    # end = "\nЦена одной NFT составляет: " + str(param["coast"]) + " TON"


    return start


# Вывод текста в любое другое время
def DayNews(tg_id):
    param = bd.GetParam(bd.ParamStatus.get_news, tg_id=tg_id)

    # text = "💎TON ELEPHANTS💎\n" + "NFT Presale. \n \n"
    # hellou = "Продажа проходит в " + str(param["count_stage"]) + " этапа:\n\n"

    # nft_score = ""

    # for i in range(param["param_stage"]):
    #     # nft_score += 'x' + str(param["param_factor"][i]) + ' NFT - ' + str(param["param_avalible"][i]) + ' штук - ' + str(param["param_status"][i]) + '\n'
    #     nft_score += 'x' + str(param["param_factor"][i]) + ' NFT - ' + str(param["param_status"][i]) + '\n'
    
    # end = "\nЦена одной NFT составляет: " + str(param["coast"]) + " TON"

    # end = "\nДля покупки достпуно: " + str(param["param_avalible"][param["current_stage"] - 1] - param["param_sale"][param["current_stage"] - 1]) + " из " + str(param["param_avalible"][param["current_stage"] - 1]) + " по цене " + str(param["coast"]) + " TON за 1 NFT"

    text = """Выберите вариант покупки🐘

x1 NFT - 20 TON💎
x3 NFT - 55 TON💎
x5 NFT - 75 TON💎
x10 NFT - 140 TON💎"""

    return text 

def BadText():
    
    text = "Очень сожаляем, но у тебя не получилось пройти наш тест, в связи с чем, мы вынуждены не пустить тебя дальше, но ты можешь попробовать ещё раз"
    text += "\n" + "/start"
    return text

def BlockText(tg_id):
    param = bd.GetParam(bd.ParamStatus.get_news, tg_id=tg_id)
    text = "NFT Presale.\n \n"
    hellou = """
Мы приветствуем тебя в официальном боте NFT-коллекции Ton Elephants🐘

В этом боте ты можешь:

◾️Купить наши NFT на Pre-Sale

◾️Воспользоваться нашей реферальной системой

◾️Найти все наши соцсети и узнать что-то новое

Надеемся, что вы нашли то, что вам по душе✨
Хорошего дня✌🏻
Команда Ton Elephants🐘
"""
    # bad = "К сожалению Вас нет в WhiteList, в связи с чем, вы не можете принять участие в покупке"

    return hellou

def BlockTime(tg_id):
    param = bd.GetParam(bd.ParamStatus.get_news, tg_id=tg_id)
    text = "NFT Presale.\n \n"
    hellou = """
Мы готовы представить Вам долгожданный первый PreSale Ton Elephants.\n
Сегодня PreSale открыт только для обладателей White List, он продлится с 15:00 по МСК 20 октября по 00:00 22 октября🔥\n
Всеобщий PreSale начнётся в 15:00 22 октября и продлится до 00:00 25 октября📈 \n
    """
    bad = "К сожалению время продаж не наступило"

    return text + hellou + bad