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
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    btn=driver.find_element(*(By.XPATH,"//button[@onclick='jsAlert()']"))
    btn.click()
    wait=WebDriverWait(driver,10)
    wait.until(EC.alert_is_present())
    alert=driver.switch_to.alert
    alert.accept()
    result=driver.find_element(*(By.XPATH,"//p[@id='result']"))
    print(result.text)

    btn2=driver.find_element(*(By.XPATH,"//button[@onclick='jsConfirm()']"))
    btn2.click()
    wait=WebDriverWait(driver,10)
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    print(result.text)
#for cancel button
    btn2 = driver.find_element(*(By.XPATH, "//button[@onclick='jsConfirm()']"))
    btn2.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.dismiss()# cancel button

    print(result.text)

    btn3=driver.find_element(*(By.XPATH,"//button[@onclick='jsPrompt()']"))
    btn3.click()
    wait=WebDriverWait(driver,10)
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.send_keys("Khushali")
    alert.accept()# ok button
    print(result.text)

    btn3 = driver.find_element(*(By.XPATH, "//button[@onclick='jsPrompt()']"))
    btn3.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.send_keys("Khushali")
    alert.dismiss()  # cancel button
    print(result.text)

    driver.quit()


