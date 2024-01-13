#    example of xpath
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


@pytest.mark.positive
# >>pytest -k "positive"= will run all the positive test cases
def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    #driver.implicitly_wait(10)
    #idea implicitly wait comes from waitr
    #all element wait, waste of time
    #all element wait, waste of time
    # relative xpath
    rel_xpath_email = driver.find_element(By.XPATH, "//input[@id='login-username']")
    rel_xpath_email.send_keys("contact+atb5x@thetestingacademy.com")

    rel_xpath_password = driver.find_element(By.XPATH, "//input[@id='login-password']")
    rel_xpath_password.send_keys("ATBx@1234")

    rel_xpath_signinbtn = driver.find_element(By.XPATH, "//button[@id='js-login-btn']")
    rel_xpath_signinbtn.click()

    time.sleep(10)
    # wait python interpreter ,not webdriver
    assert driver.current_url == "https://app.vwo.com/#/dashboard", 'Wrong URL'
    page_heading_element = driver.find_element(*(By.XPATH, "//h1[@class='page-heading']"))
    assert page_heading_element.text == "Dashboard"
    page_heading_element_msg = driver.find_element(*(By.XPATH, "//span[@data-qa='lufexuloga']"))
    assert page_heading_element_msg.text == "Aman"


# negative test case with abslute xpath, from root path if any change in html it will not work
def test_open_url():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    abs_xpath_email = driver.find_element(By.XPATH,
                                          value="/html/body/div[2]/div[1]/div[2]/div/div[1]/div/div/div[3]/form[1]/ul/li[1]/div/input")
    abs_xpath_email.send_keys("Admin")
    abs_xpath_password = driver.find_element(By.XPATH,
                                             value="/html/body/div[2]/div[1]/div[2]/div/div[1]/div/div/div[3]/form[1]/ul/li[2]/input")
    abs_xpath_password.send_keys("Admin")
    abs_xpath_signinbtn = driver.find_element(By.XPATH,
                                              value="/html/body/div[2]/div[1]/div[2]/div/div[1]/div/div/div[3]/form[1]/ul/li[6]/button")
    abs_xpath_signinbtn.click()
    assert driver.find_element(By.XPATH,
                               value="//div[contains(text(),'Your email, password, IP address or location did not match')]") == True, "Error----"

    time.sleep(5)
    driver.quit()
