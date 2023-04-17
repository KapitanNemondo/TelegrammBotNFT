import baseReferData as base_refer



def GetStageMap(tg_id):
    param = {
        "discount_flag"     : bool(),       
        # Разрешена ли пользователю скидка
        "discount_param"    : int(),        # Минимальное количество пользователей для скидки
        "discount_count"    : int(),        # Величина скидки 
        
        "energy_flag"       : bool(),       # Разрешена ли пользователю доп энергия
        "energy_param"      : int(),        # Минимальное количество пользователей для скидки
        "energy_count"      : int(),        # Величина энергии

        "boost_flag"       : bool(),       # Разрешена ли пользователю доп буст
        "boost_param"      : int(),        # Минимальное количество пользователей для скидки
        "boost_count"      : int(),        # Величина буста

    }

    photo_st = ["1-ST WAY 0.jpg", "1-ST WAY 1.jpg", "1-ST WAY 2.jpg", "1-ST WAY 3.jpg", "1-ST WAY 4.jpg", "1-ST WAY 5.jpg", "1-ST WAY 6.jpg"]
    photo_nd = ["2-ND WAY 0.jpg", "2-ND WAY 1.jpg", "2-ND WAY 2.jpg", "2-ND WAY 3.jpg", "2-ND WAY 4.jpg"]

    photo = ["", ""]


    stage_param = {
        "null"             : None,
        "discount_5_ton"   : "discount_5_ton",
        "energy_get"       : "energy_get",
        "boost_get"        : "boost_get",
        "epic_clothes"     : "epic_clothes",
        "discount_10_ton"  : "discount_10_ton",
        "get_nft"          : "get_nft"
    }

    count_refer = base_refer.GetScore(tg_id)
    set_count, flag_open, stage = base_refer.GetReferStatus(tg_id)

    if count_refer >= set_count:
        if count_refer == 3 and flag_open == 'open' and stage == stage_param["null"]:

            # flag_open = False
            stage = stage_param["discount_5_ton"]
            set_count = 3

            param["discount_flag"] = True
            param["discount_count"] = 5
            param["discount_param"] = 3

            photo[0] = photo_st[1]
        
        elif count_refer == 5 and flag_open == 'open' and stage == stage_param["discount_5_ton"]:

            # flag_open = False
            stage = stage_param["energy_get"]
            set_count = 5

            param["energy_flag"] = True
            param["energy_count"] = 1
            param["energy_param"] = 5

            photo[0] = photo_st[2]
        
        elif count_refer == 10 and flag_open == 'open' and stage == stage_param["energy_get"]:

            stage = stage_param["boost_get"]
            set_count = 10

            param["boost_flag"] = True
            param["boost_count"] = 2
            param["boost_param"] = 10

            photo[0] = photo_st[3]
        
        elif count_refer == 15 and flag_open == 'open' and stage == stage_param["boost_get"]:

            stage = stage_param["epic_clothes"]
            set_count = 15

            photo[0] = photo_st[4]

            # Что-то написать чтобы один раз выдало рандомную нфтишку
        
        elif count_refer == 20 and flag_open == 'open' and stage == stage_param["epic_clothes"]:

            stage = stage_param["discount_10_ton"]
            set_count = 20

            photo[0] = photo_st[5]

            param["discount_flag"] = True
            param["discount_count"] = 10
            param["discount_param"] = 3
        
        elif count_refer == 90 and flag_open == 'open' and stage == stage_param["discount_10_ton"]:

            stage = stage_param["get_nft"]
            set_count = 90

            photo[0] = photo_st[6]
        
        else:
            photo[0] = photo_st[0]
            

            

    if count_refer >= 3 and count_refer < 5:
        param["discount_flag"] = True
        param["discount_count"] = 5
        param["discount_param"] = 3

        param["energy_flag"] = False

        param["boost_flag"] = False
 
