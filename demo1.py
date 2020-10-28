#locating elements using id and tag_name
from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")

driver.get("https://www.google.com/")
try:
    driver.find_element_by_name('q')
    print('test pass : id found')
    driver.find_element_by_tag_name('form')
    print('passed test : tag name found')

except Exception as e:
    print("Exception found ", format(e))
driver.close()