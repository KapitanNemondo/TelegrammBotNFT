from typing import List, Dict, Any
from .typers import Transaction, TransactionType
from urllib.parse import urljoin
import requests
import json


API_PATH = "https://toncenter.com/api/v2/"


def __generate_method_href(method_path: str) -> str:
	return urljoin(API_PATH, method_path)


def __make_request(request_href: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
	params = params or dict()
	response = requests.get(request_href, params)

	if response.status_code != 200:
		raise Exception(f"[TokenParser.APIMethods] Не удалось обработать запрос : {response.url}\nКод ошибки: {response.status_code}")

	return json.loads(response.content)


def get_transactions(address: str, amount: int = 10, hash: str = None, lt: int = None) -> List[Dict[str, Any]]:
	params = {"address": address, "amount": amount}

	if hash is not None: params["hash"] = hash
	if lt is not None: params["lt"] = lt

	response = __make_request(
		__generate_method_href("getTransactions"),
		params=params
	)

	return response["result"]