import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login():
    driver = webdriver.Chrome()
    driver.get("https://www.awesomeqa.com/xpath/")
    ancestor_mammal = driver.find_element(By.XPATH, value="//div[@class='Mammal']/ancestor::div")
    print("ancestor_mammal------------------")
    print(ancestor_mammal.text)
    parent_mammal = driver.find_elements(By.XPATH, value="//div[@class='Mammal']/parent::div")
    print("parent_mammal-------------------------")
    for i in parent_mammal:
        print(i.text)

    child_mammal = driver.find_elements(By.XPATH, value="//div[@class='Mammal']/child::div")
    print("child_mammal---------------")
    for i in child_mammal:
        print(i.text)
    sibling_mammal = driver.find_elements(By.XPATH, value="//div[@class='Mammal']/following-sibling::div")
    print("silbing-----------")
    for i in sibling_mammal:
        print(i.text)
    descendant_mammal = driver.find_elements(By.XPATH, value="//div[@class='Mammal']/descendant::div")
    print("descent---------------------")
    for i in descendant_mammal:
        print(i.text)
    time.sleep(5)
    driver.quit()
