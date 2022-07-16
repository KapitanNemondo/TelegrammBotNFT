from typing import Optional, Tuple

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def query_selector(element: WebElement, selection: str) -> Optional[WebElement]:
    try:
        selection_result = element.find_element(By.CSS_SELECTOR, selection)
    except NoSuchElementException:
        return None

    return selection_result


def query_selector_all(element: WebElement, selection: str) -> Tuple[WebElement]:
    try:
        selection_result = element.find_elements(By.CSS_SELECTOR, selection)
    except NoSuchElementException:
        return tuple()

    return tuple(selection_result)
