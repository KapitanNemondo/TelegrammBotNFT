import config_message as c_m


# Вывод текста при первом запуске бота, при вызове команды /start
def HellouText():
    c_m.GetParam()

    text = "TRACE NFT Presale. Продажа x" + str(c_m.param_factor[c_m.param_cur_stage - 1]) + " Contairse \n \n"
    hellou = "Добро пожаловать в бот для пересейла первых NFT Container. \nПродажа пройдёт в " + str(c_m.param_stage) + " этапа:\n\n"

    nft_score = ""

    for i in range(c_m.param_stage):
        nft_score += 'x' + str(c_m.param_factor[i]) + ' NFT Container - ' + str(c_m.param_number[i]) + ' штук - ' + str(c_m.param_status[i]) + '\n'
    
    end = "\nДля покупки достпуно: " + str(c_m.param_nft_avalible[c_m.param_cur_stage - 1]) + " из " + str(c_m.nft_all) + " по цене " + str(c_m.param_cost) + " TON за 1 NFT"

    return text + hellou + nft_score + end


# Вывод текста в любое другое время
def DayNews():
    c_m.GetParam()

    text = "💎TON ELEPHANTS💎\n" + "TRACE NFT Presale. Продажа x" + str(c_m.param_factor[c_m.param_cur_stage - 1]) + " Contairse \n \n"
    hellou = "Продажа проходит в " + str(c_m.param_stage) + " этапа:\n\n"

    nft_score = ""

    for i in range(c_m.param_stage):
        nft_score += 'x' + str(c_m.param_factor[i]) + ' NFT Container - ' + str(c_m.param_number[i]) + ' штук - ' + str(c_m.param_status[i]) + '\n'
    
    end = "\nДля покупки достпуно: " + str(c_m.param_nft_avalible[c_m.param_cur_stage - 1]) + " из " + str(c_m.nft_all) + " по цене " + str(c_m.param_cost) + " TON за 1 NFT"

    return text + hellou + nft_score + end

def BadText():
    
    text = "Очень сожаляем, но у тебя не получилось пройти наш тест, в связи с чем, мы вынуждены не пустить тебя дальше, но ты можешь попробовать ещё раз"
    text += "\n" + "/start"
    return text

