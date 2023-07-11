import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import undetected_chromedriver as uc
from fake_useragent import UserAgent

def spam():
    wait_time = 1
    random.seed(random.randint(0,999))
    abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345567890!@#$%^&*()`~-_=+[]\{}|"
    fake_pass = ""
    fake_email = ""

    our_name = ''.join((main.firstname_entry.get()," ",main.lastname_entry.get()))
    our_firstname = main.firstname_entry.get()
    our_lastname = main.lastname_entry.get()
    
    options = Options()
    ua = UserAgent()
    user_agent = ua.random
    print("User agent: " + str(user_agent))
    
    driver = uc.Chrome(chrome_options=options,headless=False)
    driver.get("https://www.linkedin.com/signup")
    
    for _ in range(random.randint(10,20)):
        fake_pass = ''.join((fake_pass,abc[random.randint(0,len(abc)-1)]))
    for _ in range(random.randint(10,20)):
        fake_email = ''.join((fake_email,abc[random.randint(0,52)]))
    fake_email = ''.join((fake_email,"@mail.com"))
    
    print(fake_pass)
    print("Beginning obfuscation for " + our_name + "...")
    print("Email Address: " + fake_email)
    print("Password: " + fake_pass)
    #Pauses are needed to not set off bot detection
    driver.find_element(By.ID,'email-address').send_keys(fake_email)
    time.sleep(wait_time)
    driver.find_element(By.ID,'password',).send_keys(fake_pass)
    time.sleep(wait_time)
    driver.find_element(By.ID,'join-form-submit').click()
    time.sleep(wait_time)
    driver.find_element(By.ID,'first-name').send_keys(our_firstname)
    time.sleep(wait_time)
    driver.find_element(By.ID,'last-name',).send_keys(our_lastname)
    time.sleep(wait_time)
    driver.find_element(By.ID,'join-form-submit').click()
    time.sleep(60)