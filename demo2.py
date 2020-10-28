#printing all id locator values
from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")

driver.get('https://onecore.net/')

ids=driver.find_elements_by_xpath('//*[@id]')

for ii in ids:
    print(ii.get_attribute('id'))

driver.close()