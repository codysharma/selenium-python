import pytest


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_username(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        import time

        driver = webdriver.Chrome()
        driver.get("https://practicetestautomation.com/practice-test-login/")

        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("incorrectUser")
        # username_locator.send_keys("student")

        password_locator = driver.find_element("name", "password")
        password_locator.send_keys("Password123")

        submit_button_locator = driver.find_element(By.XPATH, "/html/body/div/div/section/section/div[1]/button")
        submit_button_locator.click()
        time.sleep(1)

        # verify error message is displayed
        error_message_locator = driver.find_element("id", "error")
        assert error_message_locator.is_displayed(), "Error message not displayed, but it should"

        # verify error message text
        actual_error_text = error_message_locator.text
        assert actual_error_text == "Your username is invalid!", "Error message not expected"

        driver.quit()       
        

    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_password(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        import time

        driver = webdriver.Chrome()
        driver.get("https://practicetestautomation.com/practice-test-login/")

        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        password_locator = driver.find_element("name", "password")
        password_locator.send_keys("Password")

        submit_button_locator = driver.find_element(By.XPATH, "/html/body/div/div/section/section/div[1]/button")
        submit_button_locator.click()
        time.sleep(1)

        # verify error message is displayed
        error_message_locator = driver.find_element("id", "error")
        assert error_message_locator.is_displayed(), "Error message not displayed, but it should"

        # verify error message text
        actual_error_text = error_message_locator.text
        assert actual_error_text == "Your password is invalid!", "Error message not expected"

        driver.quit()