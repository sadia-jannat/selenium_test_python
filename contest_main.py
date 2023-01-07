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


#pytest.fixture akta parameter
@pytest.fixture 
def getDriver(self):
        _driver=None
        _driver = webdriver.Chrome("Downloads/chromedriver")
        _driver.get("https://www.saucedemo.com/index.html/")
        _driver.implicitly_wait(20)
        request.cls.driver=_driver
        yield request.cls.driver
        time.sleep(2)
        request.cls.driver.quit()