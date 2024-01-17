 #    example of explicit wait
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)
import os
from dotenv import load_dotenv


@pytest.mark.positive
# >>pytest -k "positive"= will run all the positive test cases
def test_open_login():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
#    driver.implicitly_wait(10)
    # idea implicitly wait comes from waitr
    # all element wait, waste of time
    # relative xpath
    rel_xpath_email = driver.find_element(By.XPATH, "//input[@id='login-username']")
    rel_xpath_email.send_keys(os.getenv("EMAIL"))

    rel_xpath_password = driver.find_element(By.XPATH, "//input[@id='login-password']")
    rel_xpath_password.send_keys(os.getenv("PASSWORD"))

    rel_xpath_signinbtn = driver.find_element(By.XPATH, "//button[@id='js-login-btn']")
    rel_xpath_signinbtn.click()
    #at time one condition explicity wait
    #WebDriverWait(driver, 35).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".page-heading"), "Dashboard"))
    WebDriverWait(driver, 35).until(EC.visibility_of_element_located ((By.CSS_SELECTOR, ".page-heading")))
    # wait python interpreter ,not webdriver
    # assert driver.current_url == "https://app.vwo.com/#/dashboard", 'Wrong URL'
    # page_heading_element = driver.find_element(*(By.XPATH, "//h1[@class='page-heading']"))
    # assert page_heading_element.text == "Dashboard"
    page_heading_element_msg = driver.find_element(*(By.XPATH, "//span[@data-qa='lufexuloga']"))
    assert page_heading_element_msg.text == os.getenv("NAME")
    #---------------------------------------------------------------------------------------------------------
    #fluent wait----condition+frequency----customize exception
    #ignore_list=[ElementNotSelectableException,ElementNotVisibleException]
    #wait=WebDriverWait(driver,15,poll_frequency=1,ignored_exceptions=ignore_list)
   # element=EC.presence_of_element_located((By.CSS_SELECTOR,".page-heading"))


    #time.sleep(5)
    driver.quit()
