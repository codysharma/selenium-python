import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestExceptions:

    @pytest.mark.exception
    def test_element_slow_load(self, driver):
        