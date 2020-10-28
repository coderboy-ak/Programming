#printing all id,class and href locator values
from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")

driver.get('https://onecore.net/')

ids=driver.find_elements_by_xpath('//*[@id]')

for ii in ids:
    print(ii.get_attribute('id'))

hrefs = driver.find_elements_by_xpath('//*[@href]')
print('All elemets belongs to href are : ')
for ii in hrefs:
    print(ii.get_attribute('href'))

classes = driver.find_elements_by_xpath('//*[@class]')
print('All class names are : ')
for ii in classes:
    print(ii.get_attribute('class'))

driver.close()