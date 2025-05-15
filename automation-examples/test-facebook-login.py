# test_facebook_login.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_valid_login():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")

    email_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "pass")

    email_field.send_keys("validuser@example.com")
    password_field.send_keys("correctpassword")
    password_field.send_keys(Keys.RETURN)

    time.sleep(3)
    assert "Facebook" in driver.title
    driver.quit()
