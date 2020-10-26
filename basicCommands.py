from selenium  import webdriver
import time
driver=webdriver.Chrome("C:\driver\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("")