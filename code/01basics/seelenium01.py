# call selenium
# pip install selenium
# selenium code(python,java)__> API HTTP Request___>chromeDriver/GecoDriver--->chrome/Firefox

from selenium import webdriver


# send command to navigate to url
browser= webdriver.Chrome()
browser.get("https://app.vwo.com")
