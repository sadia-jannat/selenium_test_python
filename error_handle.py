from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException
import pytest
import time
import traceback


def test_error_handle():
    driver = webdriver.Chrome("Downloads/chromedriver")
    
    driver.get("https://qavbox.github.io/demo/signup/")
    assert "Registration" in driver.title
    
    #asseration error handling means Full Name ar jaygy Full Name1 lekha hoy
    try:
       el=driver.find_element("id", "lblname")
       assert "Full Name1" in el.text
    except NoSuchElementException:
        print(traceback.format_exc())   
    
    #try except handle username1 error.ata hobe username real..ami check korlm username1 ja vul silo.
    try:
        username=driver.find_element("id", "username1").send_keys("sadia call")
        assert "sadia call" in username.text
    except NoSuchElementException:
        print(traceback.format_exc())
    
    #upor ar code command kore rakty hobe ata korly
    driver.find_element("id", "username1").click()
    WebDriverWait(driver, 10).until(EC.alert_is_present()) #timeout exception  
    driver.switch_to_alert() #no such alert exception
        
    email=driver.find_element("id", "email").send_keys("sadia@gmail.com")
    
    time.sleep(3)
    driver.quit()
    
    