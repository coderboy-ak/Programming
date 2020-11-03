import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
driver.get("https://www.tiny.cloud/docs/demo/full-featured/")
driver.maximize_window()
print(driver.title)
driver.switch_to.frame(driver.find_element_by_id("full-featured_ifr"))
edit= driver.find_element_by_id("tinymce")
edit.clear()
edit.send_keys("Selenium Master")
time.sleep(2)
edit.send_keys(Keys.ENTER)
edit.send_keys("Python Webdriver Tutorial")
time.sleep(4)
body_txt= edit.text
if body_txt.find("Python Webdriver Tutorial")>1:
    print("Test passed")
    print("Entered text : ",body_txt)
else:
    print("Test failed")
driver.close()