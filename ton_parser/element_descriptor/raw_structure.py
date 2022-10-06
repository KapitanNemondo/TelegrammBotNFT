from typing import Any

from selenium.webdriver.remote.webelement import WebElement

from element_descriptor import ElementStructure, MultiElementDescriptor


class RawStructure(ElementStructure):
    fields = MultiElementDescriptor("td")


class FieldDescriptor:
    _index: int

    def __init__(self, index: int) -> None:
        self._index = index

    def __get__(self, obj: RawStructure, obj_type: Any = None) -> WebElement:
        return obj.fields[self._index]
