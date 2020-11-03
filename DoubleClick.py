import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
driver.get('http://testautomationpractice.blogspot.com/')
print(driver.title)
driver.maximize_window() #maximize window size
time.sleep(2)
element= driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")

actions= ActionChains(driver)
actions.double_click(element).perform() #Double click on button
