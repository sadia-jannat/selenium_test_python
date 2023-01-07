from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By 
import pytest


def test_table():
    driver = webdriver.Chrome("Downloads/chromedriver")
    #test_global.driver.maximize_window()
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(50)
    driver.get("https://qavbox.github.io/demo/webtable/")
    assert "webtable" in driver.title
    
    table=driver.find_element("id","table01")
    header=driver.find_element("tag","th")
    
    body=driver.find_element("tag","tbody")
    data=body.find_elements("tag", "td")
    row=body.find_elements("tag", "tr")
    #for head in header:
     #    print(head.text)
    #for tddata in data:
     #    print(tddata.text)
    print(len(row)) 
    
    #td check and match data one see.use for loop and if condition
    for i in range(len(row)):
        colum=row[i].find_element("tag","td")
        for j in range(len(colum)):
            if colum[j].text == "TFS":
                colum[0].click()
   
        
    time.sleep(3)     
    driver.quit()       
    