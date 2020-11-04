import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
driver.get("http://www.amazon.in/")
driver.maximize_window()
print(driver.title)


#Capture all the cookies created by browser
cookies= driver.get_cookies()
print(len(cookies)) #print no of cookies have been created
print(cookies)

#Adding new cookie to the browser
cookie= {'name':'Mycookie','value':'12324354'}
driver.add_cookie(cookie)

cookies= driver.get_cookies()
print(len(cookies)) #print no of cookies have been created
print(cookies) #print all the cookie pairs

#Deleting cookie
driver.delete_cookie('Mycookie')
time.sleep(2)

cookies= driver.get_cookies()
print(len(cookies)) #print no of cookies have been created
print(cookies) #print all the cookie pairs

#Delete all the cookies
driver.delete_all_cookies() #delete all cookies
cookies= driver.get_cookies()
print(len(cookies)) #print no of cookies have been created
print(cookies) #print all the cookie pairs

driver.close()

# Cookie is a piece of information from website  and saved by your web browser
# cookie stores information in a cookie file as key value pairs
# it stores login information like username,email and password
# http cookie is also known as web cookie , a browser cookie or internet cookie


