import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")
driver.maximize_window()
print(driver.title)
print("switch to first frame")
driver.switch_to.frame("packageListFrame")  #first frame
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
print("switch to parent frame before switching to next frame")
driver.switch_to.parent_frame()
print("switch to second frame")
driver.switch_to.frame("packageFrame") #second frame
time.sleep(2)
driver.find_element(By.LINK_TEXT,"WebDriver").click()
time.sleep(2)
print("switch to parent frame before switching to next frame")
driver.switch_to.parent_frame()
print("switch to third frame")
driver.switch_to.frame("classFrame") #third frame
driver.find_element(By.XPATH,"/html/body/div[1]/ul/li[5]/a").click()
driver.close()


