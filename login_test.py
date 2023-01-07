from selenium import webdriver
import time

# driver = webdriver.Firefox(executable_path="C:\\Grid\\geckodriver.exe")
# driver = webdriver.Ie(executable_path="C:\\Grid\\IEdriverserver.exe")
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("Downloads/chromedriver")
driver.maximize_window()
driver.implicitly_wait(50)
driver.set_page_load_timeout(50)
driver.get("https://foursquare.com/login?continue=%2Fv%2Fshimanto-square-shopping-mall%2F4e6ddd03fa768e6cee3d6485&clicked=true")
assert "Log in" in driver.title
driver.find_element("id", "username").click()
driver.find_element("id", "username").send_keys("sadia@gmail.com")
time.sleep(2)
driver.find_element("id", "password").click()
driver.find_element("id", "password").send_keys("12345678")
time.sleep(2)
driver.find_element("id", "loginFormButton").click()
#print("Sign up for Foursquare")
#use class name
a=driver.find_element(By.CLASS_NAME, "signupLink")
print(a.text)

"""
assert driver.find_element(By.CLASS_NAME, "signupLink").is_displayed() ==True
or
if (driver.find_element(By.CLASS_NAME, "signupLink").is_displayed()):
    print("ok")
else:
    print("no")
    
        
if (a.text == "Sign up for Foursquare"):
    print("success for login")
else:
    print("error")  
"""      
time.sleep(1)
#use tag name
driver.find_element(By.CLASS_NAME, "chicleText").click()
#aa.get("https://foursquare.com/explore?near=Dhaka%2C%20BD&cat=food&mode=chiclet")
#print(tag_name.text)
driver.get("https://www.dictionary.com/browse/page")
time.sleep(3)
driver.quit()