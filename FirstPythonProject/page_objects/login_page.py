# creating this class to be called in mutliple test cases to avoid duplication

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from page_objects.base_page import BasePage

class LoginPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_locator = (By.ID, "username")
    __password_locator = (By.NAME, "password")
    __submit_button_locator = (By.XPATH, "/html/body/div/div/section/section/div[1]/button")

    def __init__(self, driver: WebDriver):
        # inherets init for driver from BasePage
        super().__init__(driver)

    # initial opening of the page
    def open(self):
        # self._driver.get(self.__url)
        super()._open_url(self.__url)

    # big method to do all login steps
    def execute_login(self, username: str, password: str):
        # username_locator = self._driver.find_element(self.__username_locator)
        # username_locator.send_keys(username)
        # password_locator = self._driver.find_element(self.__password_locator)
        # password_locator.send_keys(password)
        # submit_button_locator = self._driver.find_element(self.__submit_button_locator)
        # submit_button_locator.click()

        # more efficient code:        
        # wait = WebDriverWait(self._driver, 10)
        # wait.until(ec.visibility_of_element_located(self.__username_locator))
        # self._driver.find_element(self.__username_locator).send_keys(username)
        # wait.until(ec.visibility_of_element_located(self.__password_locator))
        # self._driver.find_element(self.__password_locator).send_keys(password)
        # wait.until(ec.visibility_of_element_located(self.__submit_button_locator))
        # self._driver.find_element(self.__submit_button_locator).click()

        # We can inheret the methods from BasePage to avoid code duplication
        super()._type(self.__username_locator, username)
        super()._type(self.__password_locator, password)
        super()._click(self.__submit_button_locator)
