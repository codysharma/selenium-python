from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class ExceptionsPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_button_locator = (By.ID, "add_btn")
    __input_row1_locator = (By.XPATH, "/html/body/div/div/section/section/div/div[1]/div/input")
    __edit_button_locator = (By.XPATH, "/html/body/div/div/section/section/div/div[1]/div/button[1]")
    __save_button_locator = (By.XPATH, "/html/body/div/div/section/section/div/div[1]/div/button[2]")
    __input_row2_locator = (By.XPATH, "/html/body/div/div/section/section/div/div[3]/div/input")
    __row2_save_button_locator = ("/html/body/div/div/section/section/div/div[3]/div/button[1]")

    def __init__(self, driver):
        super().__init__(driver)
    
    