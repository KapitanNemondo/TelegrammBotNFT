from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import EdgeOptions
from selenium.webdriver import ChromiumEdge
#from webdriver_manager.chrome import ChromeDriverManager

from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium import webdriver


def create_driver() -> WebDriver:
    """Создание драйвера"""

    # options = ChromeOptions()
    options = EdgeOptions()
    #options.add_argument("--log-level=3")  # чтобы не выводились логи
    #options.add_argument('--headless') # без GUI

    #driver_path = ChromeDriverManager().install()

    driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    #driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)

    return driver
