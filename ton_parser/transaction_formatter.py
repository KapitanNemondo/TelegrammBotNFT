from typing import Dict, Any
from typers import Transaction, TransactionType
from datetime import datetime, timedelta


def __get_transaction_type(raw_data: Dict[str, Any]) -> TransactionType:
	if len(raw_data["out_msgs"]):
		return TransactionType.TRANSFER

	return TransactionType.RECEIVE


def __format_transaction_time(time: int) -> datetime:
	return datetime.utcfromtimestamp(time) + timedelta(hours=3)


def format_transaction(raw_data: Dict[str, Any]) -> Transaction:
	transaction_type = __get_transaction_type(raw_data)
	time = __format_transaction_time(raw_data["utime"])

	if transaction_type == TransactionType.TRANSFER:
		participant = raw_data["out_msgs"][0]["destination"]
		amount = raw_data["out_msgs"][0]["value"]

	if transaction_type == TransactionType.RECEIVE:
		participant = raw_data["in_msg"]["destination"]
		amount = raw_data["in_msg"]["value"]

	return Transaction(
		transaction_type=transaction_type,
		amount=float(amount) * (10 ** -9),
		time=time,
		participant=participant
	)
