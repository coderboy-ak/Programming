#locating elements using id , tag_name,partial link text ,link text and xpath
from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")

driver.get("https://www.google.com/")
try:
    driver.find_element_by_name('q')
    print('test pass : id found')
    driver.find_element_by_tag_name('form')
    print('passed test : tag name found')
    driver.find_element_by_link_text('About')
    print('Test pass : Element found by link text')
    driver.find_element_by_partial_link_text('हिन्दी')
    print('Test pass : partial link text found')
    driver.find_element_by_xpath("//a[@class='Fx4vi']")
    print('Test pass : link text class by Xpath found')
    driver.find_element_by_link_text('Business').click()
    print('Business link clicked successfully')
except Exception as e:
    print("Exception found ", format(e))

driver.close()