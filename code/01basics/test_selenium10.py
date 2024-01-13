import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#multiple browser---parallel excicution possible

# id,name,classname,css selector,xpath(Direct),xpath fuction,xpath axes
# test case shouldbe automatic so,at last you have to undo all the things
def test_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com")
    make_appointment_btn = driver.find_element(By.XPATH, value="//a[starts-with(text(),'Make App')]")
    # value="//*[@id='btn-make-appointment']" find in the all the tag name.it is slow
    make_appointment_btn.click()

    time.sleep(5)
    driver.quit()


def test_login_edge():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com")
    make_appointment_btn = driver.find_element(By.XPATH, value="//a[starts-with(text(),'Make App')]")
    # value="//*[@id='btn-make-appointment']" find in the all the tag name.it is slow
    make_appointment_btn.click()

    time.sleep(5)
    driver.quit()
