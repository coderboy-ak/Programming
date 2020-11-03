import time
from selenium import webdriver
from selenium.webdriver import ActionChains
# inspect shortcut = function key+ f12
driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
print(driver.title)
driver.maximize_window() #maximize window size
time.sleep(2)

source_element= driver.find_element_by_xpath("//*[@id='box6']")
target_element= driver.find_element_by_xpath("//*[@id='box106']")

actions= ActionChains(driver)
actions.drag_and_drop(source_element,target_element).perform()
time.sleep(2)
sc2= driver.find_element_by_xpath("//*[@id='box1']")
tr2= driver.find_element_by_xpath("//*[@id='box107']")
actions.drag_and_drop(sc2,tr2).perform()
