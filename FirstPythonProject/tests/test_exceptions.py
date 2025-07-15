import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestExceptions:

    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        add_button_locator = driver.find_element(By.ID, "add_btn") 
        add_button_locator.click()

        confirmation_locator = WebDriverWait(driver, 10).until(
              ec.presence_of_element_located((By.XPATH, "/html/body/div/div/section/section/div/div[3]/div/input"))
        )
        # confirmation_locator = driver.find_element(By.XPATH, "/html/body/div/div/section/section/div/div[3]/div/input")
        assert confirmation_locator.is_displayed(), "Confirmation message not displayed"

    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        add_button_locator = driver.find_element(By.ID, "add_btn") 
        add_button_locator.click()

        second_row_input = WebDriverWait(driver, 10).until(
              ec.presence_of_element_located((By.XPATH, "/html/body/div/div/section/section/div/div[3]/div/input"))
        )
        second_row_input.send_keys("Test")

        save_button_locator = driver.find_element(By.XPATH, "/html/body/div/div/section/section/div/div[3]/div/button[1]")
        save_button_locator.click()

        confirmation_locator = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "/html/body/div/div/section/section/div/div[4]"))
        )

        assert confirmation_locator.is_displayed(), "Confirmation message not displayed"

