from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Superclass parent class for all page objects

class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver
    
    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple, text: str, time: int = 10):
        # calls the _wait method to ensure el is visible before typing
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def _click(self, locator: tuple, text: str, time: int = 10):
        # calls the _wait method to ensure el is visible before clicking
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    def _get_text(self, locator: tuple, time = 10) -> str:
        self._wait_until_element_is_visibe(locator)
        # calls _find method to find element and return its text
        return self._find(locator).text

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))
    
    @property
    def current_url(self) -> str:
        return self._driver.current_url

    def is_displayed(self, locator: tuple) -> tuple:
        try: 
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False
    
    def _open_url(self, url: str):
        self._driver.get(url)

    
