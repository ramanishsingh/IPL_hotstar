from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome(executable_path = '/mnt/c/Program Files (x86)/Google/Chrome/Application/chrome.exe')
driver.get('http://www.google.com/');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()
