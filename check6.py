from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import string
import random
import time

def id_generator(size=16, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))


length_time=290

def play_hotstar(length_time):


    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")
    website="https://www.hotstar.com/us/sports/cricket"
    ua = UserAgent()
    userAgent = ua.random
    print(userAgent)
    options.add_argument(f'user-agent={userAgent}')
    driver = webdriver.Chrome(executable_path='/mnt/c/Users/rstha/Documents/python_scripts/hotstar/chromedriver_win32/chromedriver.exe', chrome_options=options)
    driver.get(website)

    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[1]/div/div[2]/div/div[5]/div'))
    )
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div'))
    )
    element.click()
    rand16=id_generator()

    inputElement = driver.find_element_by_id("fullname")
    inputElement.send_keys(rand16)
    inputElement = driver.find_element_by_id("email")
    inputElement.send_keys(rand16+"@gmail.com")
    inputElement = driver.find_element_by_id("password")
    inputElement.send_keys(rand16)

    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div/div/form/button'))
    )  
    element.click()
    time.sleep(4)
    element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div[3]/div[4]/span'))
    )   

    element.click()
    action = ActionChains(driver)
    #firstLevelMenu = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/div[9]/div/div[2]/div")
    #action.move_to_element(firstLevelMenu).perform()
    #time.sleep(1) 
    #element = WebDriverWait(driver, 20).until(
    #    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/div[9]/div/div[3]/div[2]/div[3]/div[4]/div/img'))
    #)
    #element.click()
  

    time.sleep(10)
    driver.find_element_by_tag_name('body').send_keys( 'F')
    time.sleep(length_time)
    driver.quit()

for i in range(100):

    play_hotstar(length_time)
