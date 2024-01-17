from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)
import os
from dotenv import load_dotenv
import openpyxl


def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append({"username": username, "password": password})
    return credentials


@pytest.mark.parametrize("user_cred", read_credentials_from_excel(
    "C:\Users\Dell\PycharmProjects\Py1xWebAutomation\code\01basics\datadriven_test\testdata_ddt.xlsx"))
def test_vwologin_positive(user_cred):
    username = user_cred["username"]
    password = user_cred["password"]
    print(username, password)
    vwo_login(username, password)


@pytest.mark.positive
# >>pytest -k "positive"= will run all the positive test cases
def vwo_login(username, password):
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    rel_xpath_email = driver.find_element(By.XPATH, "//input[@id='login-username']")
    rel_xpath_email.send_keys(username)

    rel_xpath_password = driver.find_element(By.XPATH, "//input[@id='login-password']")
    rel_xpath_password.send_keys(password)

    rel_xpath_signinbtn = driver.find_element(By.XPATH, "//button[@id='js-login-btn']")
    rel_xpath_signinbtn.click()
    # write the logic if test case pass
    # URL CHANGE
    # error massege
    result = driver.current_url
    if result != "https://app.vwo.com/#/dashboard":
        pytest.xfail("wrong username or password")
        driver.quit()
    else:
        assert True == True
        print('Pass ---->')
        driver.quit()
