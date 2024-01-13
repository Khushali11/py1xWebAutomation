import time
from selenium import webdriver
from selenium.webdriver.common.by import By


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
    for i in list_results:
        if i.text == "Dell":
            print(i.text)

    time.sleep(5)
    driver.quit()
