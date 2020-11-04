import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
driver.get("http://www.amazon.in/")
driver.maximize_window()
print(driver.title)
driver.save_screenshot("C:\df\scht1.png")
time.sleep(2)
driver.get_screenshot_as_file("C:\df\scht2.png")
driver.close()