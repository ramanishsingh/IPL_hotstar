from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

binary = r'/bin/geckodriver'
options = Options()
options.binary = binary
cap = DesiredCapabilities().FIREFOX.copy()
cap["marionette"] = True #optional
driver = webdriver.Firefox(firefox_options=options, capabilities=cap)
driver.get("http://google.com/")
print ("Firefox Initialized")
driver.quit()
