# crtrl+shift+i

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)


def test_login():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    # CSS selector
    search_box = driver.find_element(By.CSS_SELECTOR, value="input[id='gh-ac']")
    search_box.send_keys("16gb laptop")

    submit_btn = driver.find_element(By.CSS_SELECTOR, value="input[type='submit']")
    submit_btn.click()
    time.sleep(5)

    list_results = driver.find_elements(By.CSS_SELECTOR, value="span[role='heading']")
    # list_results = driver.find_elements(By.CSS_SELECTOR, value="span[role='heading'] and span[starts-with(text(),'Dell')]")
    for i in list_results:
        print(i.text)
    print("-----------------------------------------------------")

    # assert driver.current_url == "https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=16+gb+laptop&_sacat=0", "wrong Url"
    brand_element = driver.find_element(By.XPATH, value="//h3[normalize-space()='Brand']")
    brand_element.click()

    dell_element = driver.find_element(By.XPATH, value="//input[@aria-label='Dell']")
    dell_element.click()
    time.sleep(5)
    # wait=WebDriverWait(driver,10)
    # wait.until(EC.element_to_be_clickable())
    list_results_dell = driver.find_elements(By.CSS_SELECTOR, value="span[role='heading']")
    price = driver.find_elements(By.CSS_SELECTOR, value="span[class='s-item__price']")

    for i,j in zip(list_results_dell, price):
        print(i.text, "--->", j.text)
    # for i in price:
    #   print(i.text)

    time.sleep(5)
    driver.quit()
