import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from FirstPythonProject.page_objects.login_page import LoginPage

# # fixture is a function that runs before each test
# @pytest.fixture()
# def driver():
#     print("creating driver")

#     my_driver = webdriver.Chrome()
#     my_driver.get("https://practicetestautomation.com/practice-test-login/")
#     yield my_driver
#     # yield means this executes before the tests. Everything after runs after the test

#     print("closing driver")
#     my_driver.quit()

class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error", [
        # each of the following parens contain data for relative tests, rendering them uncessary
        ("incorrectUser", "Password123", "Your username is invalid!"),
        ("student", "incorrectPassword", "Your password is invalid!"),])
    def test_negative_login(self, driver, username, password, expected_error):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(username=username, password=password)
        time.sleep(2)

        assert login_page.current_url == login_page.expected_url, "Page did not load correctly after login attempt"

        assert login_page.get_error_message() == expected_error, "Error message not expected"


        # ______________________________
        # username_locator = driver.find_element(By.ID, "username")
        # username_locator.send_keys(username)
        # # username_locator.send_keys("student")

        # password_locator = driver.find_element("name", "password")
        # password_locator.send_keys(password)

        # submit_button_locator = driver.find_element(By.XPATH, "/html/body/div/div/section/section/div[1]/button")
        # submit_button_locator.click()
        # time.sleep(1)

        # # verify error message is displayed
        # error_message_locator = driver.find_element("id", "error")
        # assert error_message_locator.is_displayed(), "Error message not displayed, but it should"

        # # verify error message text
        # actual_error_text = error_message_locator.text
        # assert actual_error_text == expected_error, "Error message not expected"

        # driver.quit()  

    # def test_negative_username(self, driver):

    #     # my_driver = webdriver.Chrome()
    #     # my_driver.get("https://practicetestautomation.com/practice-test-login/")

    #     username_locator = driver.find_element(By.ID, "username")
    #     username_locator.send_keys("incorrectUser")
    #     # username_locator.send_keys("student")

    #     password_locator = driver.find_element("name", "password")
    #     password_locator.send_keys("Password123")

    #     submit_button_locator = driver.find_element(By.XPATH, "/html/body/div/div/section/section/div[1]/button")
    #     submit_button_locator.click()
    #     time.sleep(1)

    #     # verify error message is displayed
    #     error_message_locator = driver.find_element("id", "error")
    #     assert error_message_locator.is_displayed(), "Error message not displayed, but it should"

    #     # verify error message text
    #     actual_error_text = error_message_locator.text
    #     assert actual_error_text == "Your username is invalid!", "Error message not expected"

    #     # driver.quit()       
        
    # def test_negative_password(self, driver):
    #     # from selenium import webdriver
    #     # from selenium.webdriver.common.by import By
    #     # import time

    #     # driver = webdriver.Chrome()
    #     # driver.get("https://practicetestautomation.com/practice-test-login/")

    #     username_locator = driver.find_element(By.ID, "username")
    #     username_locator.send_keys("student")

    #     password_locator = driver.find_element("name", "password")
    #     password_locator.send_keys("Password")

    #     submit_button_locator = driver.find_element(By.XPATH, "/html/body/div/div/section/section/div[1]/button")
    #     submit_button_locator.click()
    #     time.sleep(1)

    #     # verify error message is displayed
    #     error_message_locator = driver.find_element("id", "error")
    #     assert error_message_locator.is_displayed(), "Error message not displayed, but it should"

    #     # verify error message text
    #     actual_error_text = error_message_locator.text
    #     assert actual_error_text == "Your password is invalid!", "Error message not expected"

    #     # driver.quit()