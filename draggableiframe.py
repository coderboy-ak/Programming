# drag textbox using ActionChains in iframe
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
driver.get('https://jqueryui.com/draggable/')
driver.implicitly_wait(2)
print(driver.title)
driver.maximize_window()
# define frame
frame = driver.find_element_by_tag_name('iframe')
# switch to the frame
driver.switch_to.frame(frame)
try:
    element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.LINK_TEXT, 'Draggable')))
    print(element.is_displayed())
except:
    print('Exception occured in expected condition')

# define draggable element
draggable_element = driver.find_element_by_xpath('//*[@id="draggable"]')
# get location before drag
location1 = draggable_element.location
print('Before drag position : ', location1)
# get x position before drag
x1 = location1.get('x')
print('x1 location before drag ', x1)
# define Action Chains
actions = ActionChains(driver)
actions.drag_and_drop_by_offset(draggable_element, 100, 0)
actions.perform()
# sleep
time.sleep(5)
# get location after drag
location2 = draggable_element.location
x2 = location2.get('x')
print('x1 location before drag ', x2)
# verify that x position difference is 100
status = (x2 - x1 == 100)
assert status is True
print(status)
print('-----move to dialog  outside the frame ------------')
driver.switch_to.parent_frame()
driver.find_element_by_link_text('Dialog').click()
print('---- switch to iframe ------------')
# frame_d=driver.find_element_by_tag_name('iframe')
# driver.switch_to.frame('frame_d')
driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
iframe_title= driver.find_element_by_xpath("//span[text()='Basic dialog']")
assert iframe_title.is_displayed()
print(iframe_title.text)
driver.switch_to.parent_frame()
resizable=driver.find_element_by_link_text("Resizable")
print(resizable.get_attribute('href'))
driver.find_element_by_link_text('Droppable').click()
driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
#define draggable element
draggable= driver.find_element_by_xpath("//*[@id='draggable']/p")
#define droppable element
droppable=driver.find_element_by_xpath("//*[@id='droppable']/p")
#define Action Chains
actions=ActionChains(driver)
actions.drag_and_drop(draggable,droppable)
actions.perform()
time.sleep(2)
#get draggable location
draggable_loc=draggable.location
print('Draggable position :',draggable_loc)
#get x position of draggable
drag_x=draggable_loc.get('x')
print('draggable new x position',drag_x)
#get droppable location
droppable_loc=droppable.location
print('Droppable position :',droppable_loc)
#get x position of droppable
drop_x=droppable_loc.get('x')
print('droppable new x position',drop_x)
#verify that drag_x is greater than drop_x
print(drag_x>drop_x)
driver.close()
