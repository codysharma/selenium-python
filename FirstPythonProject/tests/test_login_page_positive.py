import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from FirstPythonProject.page_objects.logged_in_successful import LoggedInSuccessfullyPage
from FirstPythonProject.page_objects.login_page import LoginPage

# pytest fixture is a function that runs before each test. If in the same folder as conftest.py, will auto import.

class TestPositiveScenarios:

    @pytest.mark.positive
    @pytest.mark.login
    def test_page_load(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        assert login_page.current_url == login_page.expected_url, "Page did not load correctly"

        # ______________________
        # driver = webdriver.Chrome()

        # navigate to webpage
        # driver.get("https://practicetestautomation.com/practice-test-login/")
        # actual_url = driver.current_url
        # assert actual_url == "https://practicetestautomation.com/practice-test-login/", "Page did not load correctly"

        # driver.quit()

    # these marks mean the test will run if either mark is run based on pytest.ini
    @pytest.mark.login 
    @pytest.mark.positive
    def test_positive_login(self, driver):
        # makes instance of LoginPage class
        login_page = LoginPage(driver)
        
        login_page.open()

        login_page.execute_login(
            username="student",
            password="Password123"
        )

        # makes instance of LoggedInSuccessfullyPage class
        login_success_page = LoggedInSuccessfullyPage(driver)
        assert login_success_page.current_url == login_success_page.expected_url, "Actual URL does not match expected URL"
        assert login_success_page.header == "Logged In Successfully", "Header text does not match expected text"
        assert login_success_page.is_logout_button_displayed(), "Logout button is not displayed on the page"

        # _________________________________

        # driver = webdriver.Chrome()
        # time.sleep(2)

        # navigate to webpage
        # driver.get("https://practicetestautomation.com/practice-test-login/")
        # time.sleep(2)
 
        # Type username student into Username field
        # username_locator = driver.find_element(By.ID, "username")
        # username_locator.send_keys("student")

        # # Type password Password123 into Password field
        # password_locator = driver.find_element("name", "password")
        # password_locator.send_keys("Password123")

        # # Push Submit button
        # submit_button_locator = driver.find_element(By.XPATH, "/html/body/div/div/section/section/div[1]/button")
        # submit_button_locator.click()
        # # time.sleep(2)

        # # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        # actual_url = driver.current_url
        # expected_url = "https://practicetestautomation.com/logged-in-successfully/"
        # assert actual_url == expected_url

        # # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        # new_page_text_locator = driver.find_element(By.TAG_NAME, "h1")
        # actual_text = new_page_text_locator.text
        # assert actual_text == "Logged In Successfully"

        # # Verify button Log out is displayed on the new page
        # logout_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
        # assert logout_button_locator.is_displayed()

        # driver.quit()


