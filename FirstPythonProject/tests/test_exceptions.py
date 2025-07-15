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

    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        edit_button_locator = driver.find_element(By.XPATH, "/html/body/div/div/section/section/div/div[1]/div/button[1]")
        edit_button_locator.click()

        input_field_locator = driver.find_element(By.XPATH, "/html/body/div/div/section/section/div/div[1]/div/input")
        input_field_locator.clear()
        input_field_locator.send_keys("Test")

        save_button_locator = driver.find_element(By.XPATH, "/html/body/div/div/section/section/div/div[1]/div/button[2]")
        save_button_locator.click()

        # get_attribute("value") pulls the value of the input field unlike .text
        new_text = input_field_locator.get_attribute("value")
        assert new_text == "Test", "Input field did not update correctly"

    @pytest.mark.exceptions
    def test_timeout_exception(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        WebDriverWait(driver, 2).until(
            ec.invisibility_of_element_located((By.XPATH, "/html/body/div/div/section/section/div/div[3]/div/input"))
        )

        add_button_locator = driver.find_element(By.XPATH, "/html/body/div/div/section/section/div/div[1]/div/button[3]")
        add_button_locator.click()

        # Wait for the new input field to appear
        new_input_locator = webdriver.support.ui.WebDriverWait(driver, 3).until(
            ec.visibility_of_element_located((By.XPATH, "/html/body/div/div/section/section/div/div[3]/div/input"))
        )
        assert new_input_locator.is_displayed(), "New input field did not appear in time"







