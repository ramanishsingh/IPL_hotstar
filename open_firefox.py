from selenium import webdriver

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('/mnt/c/Users/rstha/Documents/python_scripts/hotstar/FirefoxPortable/FirefoxPortable.exe')
driver = webdriver.Firefox(firefox_binary=binary)


#cap = DesiredCapabilities().FIREFOX
#cap["marionette"] = False

#firefox_profile = webdriver.FirefoxProfile()
#firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

#driver = webdriver.Firefox(firefox_profile=firefox_profile)
