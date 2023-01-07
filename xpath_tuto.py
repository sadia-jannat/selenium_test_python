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


driver = webdriver.Chrome("Downloads/chromedriver")
#driver.maximize_window()
driver.implicitly_wait(5)
driver.set_page_load_timeout(5)
driver.get("https://www.w3schools.com/html/")
time.sleep(2)
driver.find_element(By.XPATH, "//a[@class='w3-bar-item w3-button']").click()
assert "HTML Tutorial" in driver.title
time.sleep(3)
driver.quit()