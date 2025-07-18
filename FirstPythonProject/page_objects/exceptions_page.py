from page_objects.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class ExceptionsPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_button_locator = (By.ID, "add_btn")
    __row1_input_locator = (By.XPATH, "/html/body/div/div/section/section/div/div[1]/div/input")
    __row1_edit_button_locator = (By.XPATH, "/html/body/div/div/section/section/div/div[1]/div/button[1]")
    __row1_save_button_locator = (By.XPATH, "/html/body/div/div/section/section/div/div[1]/div/button[2]")
    __row1_add_button_locator = (By.XPATH, "/html/body/div/div/section/section/div/div[1]/div/button[3]")
    __row2_input_locator = (By.XPATH, "/html/body/div/div/section/section/div/div[3]/div/input")
    __row2_save_button_locator = (By.XPATH, "/html/body/div/div/section/section/div/div[3]/div/button[1]")
    __confirmation_locator = (By.XPATH, "/html/body/div/div/section/section/div/div[4]")
    __input_instructions_locator = (By.ID, "instructions")

    def __init__(self, driver):
        super().__init__(driver)
    
    def open(self):
        super()._open_url(self.__url)

    def add_second_row(self):
        super()._click(self.__add_button_locator)
        super()._wait_until_element_is_visible(self.__row2_input_locator)

    def is_row2_displayed(self) -> bool:
        return super().is_displayed(self.__row2_input_locator)
    
    def enter_row2_text(self, food: str):
        super()._type(self.__row2_input_locator, food)
        super()._click(self.__row2_save_button_locator)
        super()._wait_until_element_is_visible(self.__confirmation_locator)

    def get_confirmation_text(self) -> str:
        return super()._get_text(self.__confirmation_locator)
    
    def edit_row1_text(self, new_text: str):
        super()._click(self.__row1_edit_button_locator)
        super()._find(self.__row1_input_locator).clear()
        super()._type(self.__row1_input_locator, new_text)
        super()._click(self.__row1_save_button_locator)
        super()._find(self.__row1_input_locator).get_attribute("value")

    def check_instructions_disappear(self) -> bool:
        super()._click(self.__row1_add_button_locator)
        # Should return False if the instructions are no longer displayed
        return super().is_displayed(self.__input_instructions_locator)
