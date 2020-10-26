from selenium  import webdriver
# import time
driver=webdriver.Chrome("C:\driver\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(30)
driver.set_page_load_timeout(50)
driver.get("https://www.google.com/")
print(driver.title)
print(driver.current_url)
# print(driver.page_source)
driver.close()