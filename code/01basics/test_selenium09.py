import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#id,name,classname,css selector,xpath(Direct),xpath fuction,xpath axes
def test_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com")
    assert driver.title == "CURA Healthcare Service"
    list_element = driver.find_elements(By.XPATH, value="//*[contains(text(),'A')]")
    # list of elements are find out
    # //p[contains(text(),"A")],p paragraph
    # //p[contains(@class,"text-muted")]
    for i in list_element:
        if i.text == 'Make Appointment':
            i.click()
            break




    # print(i.text)


    # make_appointment_btn=driver.find_element(By.XPATH,value="//a[@id='btn-make-appointment']")
    # print(make_appointment_btn)
    # make_appointment_btn = driver.find_element(By.XPATH, value="//a[starts-with(text(),'Make App')]")
    # value="//*[@id='btn-make-appointment']" find in the all the tag name.it is slow
    # make_appointment_btn.click()

    # assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    # xpath function
    # text-->//a[text()="Make Appointment"]
    # contains----->//a[contains(text(),"Make App")]Partial match
    # starts -with--->//a[starts-with(text(),"Make App")]
    #multiple boolean function----->//a[text()="Make Appointment" and contains(@id,"btn-make-appointment")]
    # And gives single value but Or give multiple values



    time.sleep(5)
    driver.quit()
