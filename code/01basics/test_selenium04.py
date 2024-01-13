import pytest
from selenium import webdriver
import logging
import time


def test_open_login():
    # chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    print(driver.title)
    #navigation
    driver.back()
    driver.get("https://www.bling.com")
    print(driver.title)

    driver.forward()
    print(driver.title)

    driver.back()
    print(driver.title)
    driver.refresh()

    time.sleep(5)
    driver.quit()
    # driver.close()
