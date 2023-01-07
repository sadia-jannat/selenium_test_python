from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
import pytest


def test_action():
    driver = webdriver.Chrome("Downloads/chromedriver")
    #test_global.driver.maximize_window()
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(50)
    driver.get("https://qavbox.github.io/demo/signup/")
    assert "Registration" in driver.title
    
    action=ActionChains(driver)
    #start action test by user name click,write,create
    #ele=driver.find_element("id", "username")
    #action.click(ele).perform()
    #time.sleep(5)
    
    #action.send_keys("sadia").perform()  #1st time ele write korbe tai send_keys use
    #time.sleep(4)
    
    #action.send_keys_to_element(ele, "jannat").perform() #2nd time ele a write korbe.tai send_key_to_element use
    #time.sleep(4)
    #end 
    
    #start keys use for box value right click open,then arrow drown and click the iteam
    #driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
    #time.sleep(4)
    #rightclick=driver.find_element("xpath", "//span[contains(text(), 'right click me')]")
    #action.context_click(rightclick).send_keys(Keys.ARROW_DOWN).pause(3).send_keys(Keys.ARROW_DOWN).pause(3).send_keys(Keys.ENTER).perform()
    #end
    
    #signup,email fields gula value dea+copy paste like-ctrl+c,ctrl+v,ctrl+a asob use hobe
    username=driver.find_element("id", "signup")
    email=driver.find_element("id", "email")
    
    username.send_keys("watch sadia")
    action.key_down(Keys.CONTROL).key_down("A").key_up(Keys.CONTROL).perform()
    time.sleep(3)
    action.key_down(Keys.CONTROL).key_down("C").key_up(Keys.CONTROL).perform()
    time.sleep(3)
    action.click(email).key_down(Keys.CONTROL).key_down("V").key_up(Keys.CONTROL).perform()
    time.sleep(3)
    #end
    driver.quit()