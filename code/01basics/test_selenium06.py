import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # priority: id,name,classname,linktext/partial,css selector,xpath
    # 1)best method
    make_appointment_btn = driver.find_element(By.ID, value="btn-make-appointment")
    make_appointment_btn.click()
    print(driver.current_url)
    # click on Make appointment
    # <a id="btn-make-appointment" href="./profile.php#login" class="btn btn-dark btn-lg">Make Appointment</a>

    # verification change page
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login", "ERROR wrong URL"
    username=driver.find_element(By.NAME, value="username")
    username.send_keys("John Doe")
    #< input type = "password"class ="form-control" id="txt-password" name="password" placeholder="Password" value="" autocomplete="off" >
    #coustem attributes it is not id,class,name
    password = driver.find_element(By.ID, value="txt-password")
    password.send_keys("ThisIsNotAPassword")

    submit_btn=driver.find_element(By.ID, value="btn-login")
    submit_btn.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment", "ERROR wrong URL"

    time.sleep(5)
    driver.quit()
