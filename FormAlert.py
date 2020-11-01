import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
print(driver.title)
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='HTML9']/div[1]/button").click()
driver.switch_to.alert.accept()
text=driver.find_element(By.ID,"demo").text
print("allert : ",text)
driver.find_element(By.XPATH,"//*[@id='HTML9']/div[1]/button").click()
driver.switch_to.alert.dismiss()
text2=driver.find_element(By.ID,"demo").text
print(text2)
driver.close()