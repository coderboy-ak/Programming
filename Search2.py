import time
from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")

from selenium.webdriver.common.keys import Keys


driver.get("http://google.com")

search=driver.find_element_by_name('q')
search.send_keys('Python 3')
search.send_keys(Keys.RETURN)
driver.refresh()  #refresh the page
driver.back()
elem=driver.find_element_by_link_text('About')
elem.click()
#elem.send_keys(Keys.END)   #Scroll Down Page
time.sleep(4)
#elem.send_keys(Keys.HOME)
driver.back()   #Navigate backward
time.sleep(2)
driver.forward() #Navigate forward
# search.send_keys('Python 2')
# search.send_keys(Keys.RETURN)
driver.close()