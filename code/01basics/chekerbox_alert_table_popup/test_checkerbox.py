import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import alert
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)
import os


def test_login():
    driver = webdriver.Edge()
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    #btn1=driver.find_element(*(By.XPATH,"//input[1]"))
    #btn1.click()

    #btn2 = driver.find_element(*(By.XPATH, "//input[2]"))
    #btn2.click()

    checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
    for c in checkboxes:
        if not c.is_selected():
            c.click()
    time.sleep(5)
    driver.quit()


