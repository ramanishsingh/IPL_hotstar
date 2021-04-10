from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path='/mnt/c/Program Files (x86)/Mozilla Firefox/firefox.exe')
driver.get("https://www.google.com")
time.sleep(10)

driver.get("https://seleniumbyexamples.github.io/scrapingapp/")
time.sleep(10)

driver.close()
