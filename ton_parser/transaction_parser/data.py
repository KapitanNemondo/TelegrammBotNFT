from dataclasses import dataclass
from enum import Enum, auto
from datetime import datetime


class TransactionType(Enum):
    RECEIVE=auto()
    TRANSFER=auto()


@dataclass
class Transaction:
    participant: str
    time: datetime.time
    amount: float
    transaction_type: TransactionType
