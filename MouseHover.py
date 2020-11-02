import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
driver.get('https://opensource-demo.orangehrmlive.com/')
print(driver.title)
driver.maximize_window() #maximize window size
driver.find_element_by_id("txtUsername").send_keys("admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
time.sleep(2)
admin= driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
usermgnt=driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
user=driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")

actions=ActionChains(driver)
actions.move_to_element(admin).move_to_element(usermgnt).move_to_element(user).click().perform()
time.sleep(2)
driver.close()

