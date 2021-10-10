from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By


#driver = webdriver.Chrome(executable_path="C:/Users/minhv/Downloads/chromedriver_win32/chromedriver.exe")
def test_setup():
    global driver
    s=Service("C:/Users/minhv/Downloads/chromedriver_win32/chromedriver.exe")
    driver = webdriver.Chrome(service=s)
def test_login():
    
    url="https:facebook.com"
    driver.get(url)
    driver.maximize_window()   #full size trình duyệt
    print("window maxmize")
    pagetitle = driver.title
    print(pagetitle)        #in title triinh duyet
    assert "Facebook - Đăng nhập hoặc đăng ký" in pagetitle
def test_tear():
    time.sleep(3)
    driver.quit()
