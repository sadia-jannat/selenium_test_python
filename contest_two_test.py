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



@pytest.mark.usefixtures("getDriver")
class testDemo2:
    def test_two(self):
        driver = self.driver
        driver.find_element("id","user-name").send_keys("standard_user")
        driver.find_element("id","password").send_keys("secret_sauce")
        driver.find_element("id","login-button").click()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='product_label']")))  
        item_count= len(driver.find_elements_by_css_selector("div[class='inventory_item']"))
        assert 6 == item_count