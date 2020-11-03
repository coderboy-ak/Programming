import time
from selenium import webdriver
from selenium.webdriver import ActionChains
# inspect shortcut = function key+ f12
driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')
print(driver.title)
driver.maximize_window() #maximize window size
time.sleep(2)
button= driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")

actions= ActionChains(driver)
actions.context_click(button).perform() # mouse right click action

