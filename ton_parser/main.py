from .parser_lib.driver import create_driver
#from parser_lib.driver import create_driver
from .transaction_parser.parser import TransactionParser
from .transaction_parser.data import Transaction, TransactionType

import time
from datetime import datetime


"""Запуск парсера"""
print("[Ton Parser] Starting parser...")
driver = create_driver()

def ChekTime(transaction, ChekTon, score : float()):
    data = datetime.now()

    scanData = False
    scanTon = False
    scanScore = False

    # scanData = (transaction.date == data.day and transaction.time.hour == (data.hour - 1))

    if (transaction.time.hour == (data.hour) and (transaction.time.day == data.day)):
        scanData = True

    if (transaction.participant == ChekTon):
        scanTon = True
    
    if (transaction.amount == score):
        scanScore = True
    

    # print(transaction)

    # print("[Day]", transaction.time.day, data.day)
    # print("[Hour]", transaction.time.hour, data.hour)
    # print("[ToN]", transaction.participant, ChekTon)
    # print("[Score]", transaction.amount, score)


    # print("[Scan Data]", scanData)
    # print("[Scan Ton]", scanData)
    # print("[Scan Score]", scanData)
    

    if scanTon and scanScore and scanData:
        print("[Data]", transaction.time.day)
        return True
    else:
        return False 


def GetTransaktion(MainTon, ChekTon, score):

    from .element_descriptor.utils import query_selector_all, query_selector
    import time

    try:

        driver = create_driver()

        driver.get("https://ton.cx/address/{token}".format(token=MainTon))

        

        parser = TransactionParser(driver)

        result = filter(
            lambda transaction: (transaction.transaction_type == TransactionType.RECEIVE and ChekTime(transaction, ChekTon, score)),
            parser.parse()
        )

        # result = filter(
        #     lambda transaction: (transaction.transaction_type == TransactionType.RECEIVE),
        #     parser.parse()
        # )
        
        #driver.close()

        print(result)

        res = tuple(result)

        print()

        if len(res) > 0:
            return True

        return False
    except:
        return False




#driver.close()
