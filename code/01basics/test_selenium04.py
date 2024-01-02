import pytest
from selenium import webdriver
import logging
import time

def test_open_login():
    #chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    print(driver.title)
    time.sleep(5)
    driver.quit()
    #driver.close()