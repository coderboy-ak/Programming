import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
driver.get("https://jqueryui.com/sortable/")
driver.maximize_window()
print(driver.title)
time.sleep(4)
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
#define item1
item1= driver.find_element_by_xpath("//ul[@id='sortable']/li[text()='Item 1']")
item_height= item1.size.get('height') # confusing how to locate height
#define ActionChains
actions= ActionChains(driver)
actions.drag_and_drop_by_offset(item1,0,item_height+10)
#perform actions
actions.perform()
time.sleep(4)
#get all items
all_items= driver.find_elements_by_xpath("//ul[@id='sortable']/li[contains(text(),'Item')]")
no_of_items= len(all_items)
print(no_of_items)

#define a list that contains all the text of the items
items_text= []

#Loop all items to get each item's text
for item in all_items:
    items_text.append(item.text)
    print(item.text)

#get item2 and item1 index

item2_index= items_text.index('Item 2')
item1_index= items_text.index('Item 1')
print(" Item 2 index : ", item2_index," Item 1 index : ",item1_index)
print(item1_index>item2_index)

driver.close()


