import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import time


def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # priority: id,name,classname,linktext/partial,css selector,xpath
    # 1)best method
    #make_appointment_btn=driver.find_element(By.ID,value="btn-make-appointment")
    #make_appointment_btn.click()
    #2)method
    #make_appointment_btn=driver.find_element(By.PARTIAL_LINK_TEXT, value="tment")
    #Make Appointment,Make,App,tment
    #make_appointment_btn.click()
    #3)method:full exact match
    #make_appointment_btn = driver.find_element(By.LINK_TEXT, value="Make Appointment")
    #make_appointment_btn.click()
    #4)method:this web site has so many same class value so use elements,use . in space
    #make_appointment_btn = driver.find_elements(By.CLASS_NAME, value="btn.btn-dark.btn-lg")
    #make_appointment_btn[1].click()
    #5)method:
    make_appointment_btn = driver.find_elements(By.TAG_NAME, value="a")
    make_appointment_btn[5].click()

# click on Make appointment
#<a id="btn-make-appointment" href="./profile.php#login" class="btn btn-dark btn-lg">Make Appointment</a>

    time.sleep(5)
    driver.quit()