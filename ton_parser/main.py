from .parser_lib.driver import create_driver
#from parser_lib.driver import create_driver
from .transaction_parser.parser import TransactionParser
from .transaction_parser.data import Transaction, TransactionType

import time
from datetime import datetime


"""Запуск парсера"""
print("[Ton Parser] Starting parser...")
driver = create_driver()

def ChekTime(transaction, data, ChekTon, score):

    scanData = (transaction.time.date == data.date and transaction.time.hour == data.hour)

    if transaction.participant == ChekTon and transaction.amount == score and scanData:
        print("[Data]", transaction.time.day)
        return True
    else:
        return False 


def GetTransaktion(MainTon, ChekTon, data, score):

    from .element_descriptor.utils import query_selector_all, query_selector
    import time

    try:

        driver = create_driver()

        driver.get("https://ton.cx/address/{token}".format(token=MainTon))

        

        parser = TransactionParser(driver)

        result = filter(
            lambda transaction: (transaction.transaction_type == TransactionType.RECEIVE and ChekTime(transaction, data, ChekTon, score)),
            parser.parse()
        )
        
        #driver.close()

        print(tuple(result))

        res = tuple(result)

        if len(res) == 0:
            return False

        return True
    except:
        return False

#driver.close()
