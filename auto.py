from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import time
import numpy as np

fmps = []

#browser.get('https://qa.www.origin.com')
#sign_in_button = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Sign In')]"))) 
#sign_in_button.click()
#browser.close()

def login(browser):
    browser.get('https://accounts.int.ea.com/connect/auth?response_type=token&scope=basic.identity+basic.persona+signin+offline&client_id=ORIGIN_PC')
    email =  WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "email")))
    email.send_keys('atom123@ea.com')
    password =  WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "password")))
    password.send_keys('Welcome123')
    signin = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.ID, "btnLogin")))
    signin.click()

def goto_myhome(browser):
    #browser.get("https://orps-6698.dev.www.origin.com/can/en-us/my-home?cmsstage=preview")
    browser.get("https://before-6200.dev.www.origin.com/can/en-us/store")
    WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Trending')]"))) 

for i in range(100):
    try:
        browser = webdriver.Chrome('C:\DevTools\chromedriver_win32\chromedriver.exe')
        #login(browser)
        goto_myhome(browser)
        time.sleep(3)
        fmp = browser.execute_script("return window.performance.getEntriesByName('FMP:STORE_HOME')[0].duration")
        if fmp is not None: 
            fmps.append(fmp)
    except Exception as e:
        print(e)
    finally:
        browser.close()

print(fmps)
print(np.percentile(fmps,75))