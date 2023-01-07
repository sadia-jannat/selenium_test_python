from selenium import webdriver
from selenium.webdriver.support.select import Select


def test_dropdown():
    driver = webdriver.Chrome("Downloads/chromedriver")
    #test_global.driver.maximize_window()
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(50)
    driver.get("https://qavbox.github.io/demo/signup/")
    assert "Registration" in driver.title
    
    select=Select(driver.find_element("name","sgender"))
    #select.select_by_visible_text("Male")
    #select.select_by_value("female")
    select.select_by_index(1)
    print("ok print: -"+ select.first_selected_option.text)
    #assert "Not Applicable" in select.first_selected_option.text
    
    #all element dekhabe.use for loop
    opts=select.options
    for opt in opts:
        print(opt.text)
    
    driver.quit()