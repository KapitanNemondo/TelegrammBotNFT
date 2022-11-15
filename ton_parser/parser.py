from typing import Iterable
from typers import Transaction
from api_methods import get_transactions
from transaction_formatter import format_transaction
from time import sleep
from datetime import datetime
from typers import TransactionType

def _protected_get_transactions(*args, **kwargs):
	while True:
		try:
			result = get_transactions(*args, **kwargs)
		except:
			continue

		return result


class TransactionParser:
	_address: str

	def __init__(self, address: str):
		self._address = address

	def parse(self, protected: bool = True, start: datetime = None, end: datetime = None) -> Iterable[Transaction]:
		get_method = _protected_get_transactions if protected else get_transactions

		raw_data = get_method(self._address)

		while raw_data:
			for raw_transaction_data in raw_data:
				transaction = format_transaction(raw_transaction_data)

				if (end is not None) and (end < transaction.time):
					continue

				if (start is not None) and (transaction.time < start):
					return

				yield transaction

			last_transaction = raw_data[-1]
			last_hash = last_transaction["transaction_id"]["hash"]
			last_lt = last_transaction["transaction_id"]["lt"]

			while True:
				try:
					raw_data = get_method(self._address, hash=last_hash, lt=last_lt)
				except: continue
				break


parser = TransactionParser("EQCA0vWJntuL61f1-xQB2EwMorKpI448L5sh9c1kC29f8D4V")

# for transaction in parser.parse():
#     print(transaction)



def filter_Transaction(amount : float, participant : str, minute):
	now = datetime.now()

	no_out = tuple(parser.parse(end=datetime.now(), start=datetime(year=now.year, month=now.month, day=now.day, hour=now.hour, minute=minute)))
	
	out = list(filter(lambda pars : pars.amount == amount and pars.participant == participant, no_out))

	if len(out) != 0:
		return True
	else:
		return False

	
