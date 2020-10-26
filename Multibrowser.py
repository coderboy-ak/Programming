from selenium import webdriver
from selenium.webdriver.common.keys import keys

driver=webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")

driver.get("https://www.google.com/")
print(driver.title)
print(driver.curent_url)
print(driver.page_source)
driver.close()