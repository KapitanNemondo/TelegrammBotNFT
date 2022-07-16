from typing import Any, Optional, Tuple

from selenium.webdriver.remote.webelement import WebElement

from ton_parser.element_descriptor.utils import query_selector, query_selector_all


class NullReferenceException(Exception):
    def __init__(self):
        super().__init__("Невозможно определить структуру для None значения")


class ElementStructure:
    _element: WebElement

    def __init__(self, element: WebElement) -> None:
        if element is None:
            raise NullReferenceException()

        self._element = element


class ElementDescriptor:
    _selection: str

    def __init__(self, selection: str) -> None:
        self._selection = selection

    def __get__(self, obj: ElementStructure, obj_type: Any=None) -> Optional[WebElement]:
        return query_selector(obj._element, self._selection)


class MultiElementDescriptor:
    _selection: str

    def __init__(self, selection: str) -> None:
        self._selection = selection

    def __get__(self, obj: ElementStructure, obj_type: Any=None) -> Tuple[WebElement]:
        return query_selector_all(obj._element, self._selection)
