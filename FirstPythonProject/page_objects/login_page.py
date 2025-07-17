# creating this class to be called in mutliple test cases to avoid duplication

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class LoginPage:
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_locator = (By.ID, "username")
    __password_locator = (By.NAME, "password")
    __submit_button_locator = (By.XPATH, "/html/body/div/div/section/section/div[1]/button")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    # initial opening of the page
    def open(self):
        self._driver.get(self.__url)

    def execute_login(self, username: str, password: str):
        wait = WebDriverWait(self._driver, 10)
        # username_locator = self._driver.find_element(self.__username_locator)
        # username_locator.send_keys(username)

        # password_locator = self._driver.find_element(self.__password_locator)
        # password_locator.send_keys(password)

        # submit_button_locator = self._driver.find_element(self.__submit_button_locator)
        # submit_button_locator.click()

        # more efficient code:
        wait.until(ec.visibility_of_element_located(self.__username_locator))
        self._driver.find_element(self.__username_locator).send_keys(username)

        wait.until(ec.visibility_of_element_located(self.__password_locator))
        self._driver.find_element(self.__password_locator).send_keys(password)

        wait.until(ec.visibility_of_element_located(self.__submit_button_locator))
        self._driver.find_element(self.__submit_button_locator).click()
