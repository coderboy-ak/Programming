#error in this program
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
driver.get('https://robotframework.org/')
print(driver.title)
driver.maximize_window()
#define get libraries link
library_link=driver.find_element_by_xpath("//a[@href='#libraries']")
#click on the get libraries link
library_link.click()
window_before=driver.window_handles[0]
#define Builtin link
builtin_link=driver.find_element_by_link_text("Builtin")
#click Builtin Link
builtin_link.click()
time.sleep(2)
window_after=driver.window_handles[1]
windows=driver.window_handles
#count all windows
no_of_windows= len(windows)
driver.switch_to.window(window_before)
#define Builtin Text element
expected_text=driver.find_element_by_link_text("Builtin").text
#print the text from first window
print(expected_text)
driver.close()
