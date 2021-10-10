from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
def test_setup():
    global driver
    s=Service("C:/Users/minhv/Downloads/chromedriver_win32/chromedriver.exe")
    driver = webdriver.Chrome(service=s)
def test_element_search():
    url="https://www.google.com.vn/?hl=vi"
    driver.get(url)
    #driver.maximize_window()
    link = driver.find_element_by_css_selector("div:nth-child(1)")

    input = driver.find_element_by_name("q")
    #print(type(input))
    input.send_keys("phòng khám nhi hoạ mi")
    input.send_keys(Keys.RETURN)
    time.sleep(10)
    link.click()
    #time.sleep(5)
    driver.quit()
    print("complete")