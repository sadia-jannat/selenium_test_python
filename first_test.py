from selenium import webdriver
import time

from selenium.webdriver.common.by import By


def test_first():
    driver = webdriver.Chrome("Downloads/chromedriver")
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(50)
    driver.get("https://qavbox.github.io/demo")
    assert "QAVBOX" in driver.title
    driver.find_element(By.LINK_TEXT, "SignUp Form").click()
    time.sleep(10)
    driver.quit()

