import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# # open browser
# driver = webdriver.Chrome()
# time.sleep(2)

# # navigate to webpage
# driver.get("https://practicetestautomation.com/practice-test-login/")
# time.sleep(2)

# # Type username student into Username field
# username_locator = driver.find_element(By.ID, "username")
# username_locator.send_keys("student")

# # Type password Password123 into Password field
# password_locator = driver.find_element("name", "password")
# password_locator.send_keys("Password123")

# # Push Submit button
# submit_button_locator = driver.find_element(By.XPATH, "/html/body/div/div/section/section/div[1]/button")
# submit_button_locator.click()
# time.sleep(2)

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