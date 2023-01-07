from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import traceback


def test_ec_locator_handle():
    driver = webdriver.Chrome("Downloads/chromedriver")
    
    driver.get("https://qavbox.github.io/demo/signup/")
    assert "Registration" in driver.title
    
#main code shortcut.1- click work done where driver means url and id name means form these box
    click(driver, (By.ID, "username"))
    driver.refresh()                  #ager kono data k refesh kore
    send_keys(driver, (By.ID, "username"), "sadia")   #2-last send keys dia value add kore
    
    click(driver, (By.ID, "email"))   #1- click work done where driver means url and id name means form these box
    driver.refresh()                  #ager kono data k refesh kore
    send_keys(driver, (By.ID, "email"), "sadia@gmail.com")   #2-last send keys dia value add kore
    
    
    time.sleep(3)
    driver.quit()

#2 method for handle any error problem strongly use EC and locator
def click(driver, locator):
    WebDriverWait(driver,10).until(EC.presence_of_element_located(locator)).click


def send_keys(driver, locator, value):
    WebDriverWait(driver,10).until(EC.presence_of_element_located(locator)).clear()
    WebDriverWait(driver,10).until(EC.presence_of_element_located(locator)).send_keys(value)   
    