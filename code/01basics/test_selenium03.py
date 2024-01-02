import time

import pytest
from selenium import webdriver
import logging


def test_open_login():
    chrome_options = webdriver.ChromeOptions()
    # adblocker chrome extension plugin  in chrome is manually
    # to do automatically download crx file from crx extractor
    # give path here
    # extension_path = "C:\Users\Dell\Downloads\adblockercrx.crx"
    # chrome_options.add_extension(extension_path)
    chrome_options.add_argument("--start-maximize")
    # change proxy,size,js disable,extention
    # session post request
    # driver = webdriver.Chrome(options=chrome_options)
    # LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.get("https://google.com")

    # fresh crome have nothing
    # driver.maximize_window()
    print(driver.title)
    # LOGGER.info(driver.title)
    # time.sleep(1000)
    driver.quit()
#quite browser,close all windows, sesssionid=none
# -s print the log
# -v verbose increse the logging
# -k expression
# -q =quiet the log few
# pytest "C:\Users\Dell\PycharmProjects\Py1xWebAutomation\code\01basics\test_selenium03.py" -q -s -v --html=report.html
