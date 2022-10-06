from element_descriptor import FieldDescriptor, RawStructure, MultiElementDescriptor, ElementDescriptor, ElementStructure


class InfoBlock(RawStructure):
    time = FieldDescriptor(1)
    amount = FieldDescriptor(3)


class ParticipantsBlock(RawStructure):
    first = FieldDescriptor(0)
    transaction_type = FieldDescriptor(1)
    second = FieldDescriptor(2)


class TransactionElement:
    info: InfoBlock
    participants: ParticipantsBlock

    def __init__(self, info_block: InfoBlock, participants_block: ParticipantsBlock) -> None:
        self.info = InfoBlock(info_block)
        self.participants = ParticipantsBlock(participants_block)


class Page(ElementStructure):
    transactions = MultiElementDescriptor("#txs-table-body tr")
    next_button = ElementDescriptor("#next-button")

    _NEXT_TRANSACTION_TEXT = "Next"

    def is_loaded(self) -> bool:
        return len(self.transactions) > 0

    def have_transactions(self) -> bool:
        return self.next_button.text == self._NEXT_TRANSACTION_TEXT

    def load_transactions(self) -> None:
        self.next_button.click()