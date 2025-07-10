# fixture is a function that runs before each test
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# pytest fixture is a function that runs before each test. If in the same folder as conftest.py, will auto import.

@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    print(f"creating {browser} driver")

    # my_driver = webdriver.Chrome()
    # my_driver = webdriver.Firefox()
    if browser == "chrome":
        my_driver = webdriver.Chrome()
    elif browser == "firefox":
        my_driver = webdriver.Firefox()
    else:
        raise TypeError(f"Expected chrome or firefox, but got {browser} instead.")
    
    my_driver.get("https://practicetestautomation.com/practice-test-login/")
    yield my_driver
    # yield means this executes before the tests. Everything after runs after the test

    print("closing driver")
    my_driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")