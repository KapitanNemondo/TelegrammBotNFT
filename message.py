import bd


# Вывод текста при первом запуске бота, при вызове команды /start
def HellouText(tg_id):
    param = bd.GetParam(bd.ParamStatus.get_news, tg_id=tg_id)

    # print(param)
    

    text = "TRACE NFT Presale. Продажа x" + str(param["current_stage"]) + " Contairse \n \n"
    hellou = "Добро пожаловать в бот для пересейла первых NFT Container. \nПродажа пройдёт в " + str(param["count_stage"]) + " этапа:\n\n"

    nft_score = ""

    for i in range(param["param_stage"]):
        nft_score += 'x' + str(param["param_factor"][i]) + ' NFT Container - ' + str(param["param_avalible"][i]) + ' штук - ' + str(param["param_status"][i]) + '\n'
    
    end = "\nДля покупки достпуно: " + str(param["param_avalible"][param["current_stage"] - 1] - param["param_sale"][param["current_stage"] - 1]) + " из " + str(param["param_avalible"][param["current_stage"] - 1]) + " по цене " + str(param["coast"]) + " TON за 1 NFT"


    return text + hellou + nft_score + end


# Вывод текста в любое другое время
def DayNews(tg_id):
    param = bd.GetParam(bd.ParamStatus.get_news)

    text = "💎TON ELEPHANTS💎\n" + "TRACE NFT Presale. Продажа x" + str(param["current_stage"]) + " Contairse \n \n"
    hellou = "Продажа проходит в " + str(param["count_stage"]) + " этапа:\n\n"

    nft_score = ""

    for i in range(param["param_stage"]):
        nft_score += 'x' + str(param["param_factor"][i]) + ' NFT Container - ' + str(param["param_avalible"][i]) + ' штук - ' + str(param["param_status"][i]) + '\n'
    
    end = "\nДля покупки достпуно: " + str(param["param_avalible"][param["current_stage"] - 1] - param["param_sale"][param["current_stage"] - 1]) + " из " + str(param["param_avalible"][param["current_stage"] - 1]) + " по цене " + str(param["coast"]) + " TON за 1 NFT"

    return text + hellou + nft_score + end

def BadText():
    
    text = "Очень сожаляем, но у тебя не получилось пройти наш тест, в связи с чем, мы вынуждены не пустить тебя дальше, но ты можешь попробовать ещё раз"
    text += "\n" + "/start"
    return text

