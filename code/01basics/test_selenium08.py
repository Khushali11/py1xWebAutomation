#    example of xpath
import email

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# negative testcase ,relative xpath

def test_open_url():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")
    rel_xpath_email = driver.find_element(By.XPATH, value="//input[@type='email']")
    rel_xpath_email.send_keys("augtest_040823@idrive.com")
    rel_xpath_password = driver.find_element(By.XPATH, value="//input[@type='password']")
    rel_xpath_password.send_keys("")
    rel_xpath_submitbtn = driver.find_element(By.XPATH, value="//button[@class='id-btn id-info-btn-frm']")
    rel_xpath_submitbtn.click()

    time.sleep(5)
    driver.quit()
