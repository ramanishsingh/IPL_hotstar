from selenium import webdriver
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.binary = r"C:\Users\rstha\Documents\python_scripts\hotstar\FirefoxPortable\App\Firefox64\firefox.exe"

driver = webdriver.Firefox(firefox_options=opts)
