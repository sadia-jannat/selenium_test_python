from selenium import webdriver
#from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By 
import pytest


def test_dragdrop():
    driver = webdriver.Chrome("Downloads/chromedriver")
    #test_global.driver.maximize_window()
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(50)
    driver.get("https://qavbox.github.io/demo/dragndrop/")
    assert "DragnDrop" in driver.title
    
    action= ActionChains(driver)
    #source=driver.find_element_by_id("draggable")
    source=driver.find_element("id","draggable")
    target=driver.find_element("id", "droppable")
    #see drag and drop method
    #action.drag_and_drop(source, target).perform()
    #see move drag and drop method
    action.click_and_hold(source).pause(3).move_to_element(target).perform()
    #x,y axis drag drop calculate method
    #action.click_and_hold(source).pause(3).move_to_element_with_offset(target, 100, 100).perform()
    
    time.sleep(2)
    assert "Dropped!" in target.text
    #driver.save_screenshot("Downloads/cv") filename location ta error dekhay
    driver.quit()