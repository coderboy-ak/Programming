import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
driver.get("https://jqueryui.com/datepicker/#default")
driver.maximize_window()
print(driver.title)
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
datepicker= driver.find_element_by_id("datepicker")
datepicker.click()
time.sleep(2)
#find the day
day= driver.find_element_by_xpath("//table/tbody/tr/td/a[text()='2']")
day.click()
time.sleep(2)
datepicker= driver.find_element_by_id("datepicker")
date= datepicker.get_attribute('value')
print("date is : ",date)
if date=="11/02/2020":
    print("Test passed")
else:
    print("date is not selected")
print('-----move to menu  outside the frame ------------')
driver.switch_to.parent_frame()
driver.find_element_by_link_text('Menu').click()
driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
menu_element= driver.find_element_by_id("ui-id-9")
#define sub_menu element
sub_menu_element= driver.find_element_by_xpath("//*[@id='ui-id-17']")
#define action class
actions= ActionChains(driver)
actions.move_to_element(menu_element)
actions.perform()
time.sleep(2)
if sub_menu_element.is_displayed():
    print("Pop is displayed : test passed")
else:
    print("sub_menu is not displayed")
driver.close()


