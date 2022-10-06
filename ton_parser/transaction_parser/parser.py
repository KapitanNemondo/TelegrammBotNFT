from typing import Iterable

from transaction_parser.data import Transaction, TransactionType
from transaction_parser.page_structure import Page, TransactionElement, ParticipantsBlock
from selenium.webdriver.remote.webelement import WebElement

from datetime import datetime
import time

from progress.bar import IncrementalBar


def parse_time(element: WebElement) -> datetime.time:
    return datetime.strptime(element.text, "%d.%m.%Y %H:%M:%S")

def parse_amount(element: WebElement) -> float:
    return float(element.text.split(" ")[0][1:])

def parse_transaction_type(element: WebElement) -> TransactionType:
    parse_map = {
        "IN" : TransactionType.RECEIVE,
        "OUT" : TransactionType.TRANSFER
    }

    return parse_map[element.text]

def get_other_participant(participants: ParticipantsBlock) -> str:
    other_participant_index = {
        TransactionType.RECEIVE: lambda el: el.first,
        TransactionType.TRANSFER: lambda el: el.second
    }

    t = parse_transaction_type(participants.transaction_type)
    return other_participant_index[t](participants).text

class TransactionParser:
    _page: Page

    def __init__(self, page: WebElement) -> None:
        self._page = Page(page)

    def _wait_for_load(self) -> None:
        print("[TransactionParser] wait for loading page...")
        while not self._page.is_loaded():
            pass

    def _parse_transaction_element(self, block: Iterable[WebElement]) -> TransactionElement:        
        return TransactionElement(
                    info_block=block[0],
                    participants_block=block[-1]
                )

    def _get_transaction_elements(self) -> Iterable[TransactionElement]:
        current_block = []
        current_state = None

        print("Load transactions...")
        while self._page.have_transactions():
            self._page.load_transactions()
            time.sleep(0.2)

        progress_bar = IncrementalBar("Parsing", max=len(self._page.transactions))
        for raw in self._page.transactions:
            raw_state = raw.get_attribute("class")

            if raw_state != current_state and current_state is not None:
                yield self._parse_transaction_element(current_block)
                current_block = []

            current_block.append(raw)
            current_state = raw_state
            progress_bar.next()

        yield self._parse_transaction_element(current_block)
        progress_bar.finish()

    def parse(self) -> Iterable[Transaction]:
        self._wait_for_load()

        for transaction_element in self._get_transaction_elements():
            try:
                amount=parse_amount(transaction_element.info.amount)
            except ValueError:
                continue

            yield Transaction(
                participant=get_other_participant(transaction_element.participants),
                time=parse_time(transaction_element.info.time),
                amount=amount,
                transaction_type=parse_transaction_type(transaction_element.participants.transaction_type)
            )
