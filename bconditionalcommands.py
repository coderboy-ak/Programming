#use of is_selected(),is_Displayed and is_enabled()
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
driver.get('http://demo.guru99.com/test/newtours/index.php')
print(driver.title)
assert "Welcome: Mercury Tours" in driver.title
user_ele= driver.find_element_by_name("userName")
print(user_ele.is_displayed()) #returns true/false based of element status
print(user_ele.is_enabled())

pwd_ele=driver.find_element_by_name("password")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())
driver.implicitly_wait(1)
user_ele.send_keys("mercury")
pwd_ele.send_keys("mercury")
driver.find_element_by_name("submit").click()
driver.find_element_by_link_text("Flights").click()
time.sleep(2)
roundtrip_radio= driver.find_element_by_xpath("//input")
# roundtrip_radio= driver.find_element_by_css_selector("//input[value='roundtrip']")
print("status of roundtrip radio button: ",roundtrip_radio.is_selected())
time.sleep(2)
onetrip_radio=driver.find_element_by_xpath("//input[2]")
# onetrip_radio=driver.find_element_by_css_selector("//input[value='oneway']")
print("Status of onewar radio button: ",onetrip_radio.is_selected())

driver.close()