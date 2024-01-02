import pytest
from selenium import webdriver

#w3c protocol ,selenium Manager which will automatically download the browser driver for you
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    # return driver, values are stored permentntly extra variables


def test_open_url_verify_title(driver):
    # session post request
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert "Login - VWO" == driver.title


#pytest "C:\Users\Dell\PycharmProjects\Py1xWebAutomation\code\01 basics\test_selenium02.py" -s -v --html=report.html

