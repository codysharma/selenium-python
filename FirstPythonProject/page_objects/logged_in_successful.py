from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from FirstPythonProject.page_objects.base_page import BasePage

class LoggedInSuccessfullyPage(BasePage):
    _url = "https://practicetestautomation.com/logged-in-successfully/"
    __header_locator = (By.TAG_NAME, "h1")
    __logout_button_locator = (By.LINK_TEXT, "Log out")

    def __init__(self, driver: WebDriver):
        # self._driver = driver
        super().__init__(driver)

    # the arrow function shows it should return a string
    @property
    def current_url(self) -> str:
        return self._driver.current_url
    
    @property
    def expected_url(self) -> str:
        return self._url

    @property
    def header(self) -> str:
        # calls the _get_text method from BasePage on the arg passed in "header_locator"
        return super()._get_text(self.__header_locator)
    
    def is_logout_button_displayed(self) -> bool:
        return super().is_displayed(self.__logout_button_locator)