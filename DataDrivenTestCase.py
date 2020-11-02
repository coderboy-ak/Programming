import time
from selenium import webdriver
from Seleniumpython import XLUtils

driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
driver.get('http://demo.guru99.com/test/newtours/')
print(driver.title)
driver.maximize_window() #maximize window size

path="C://eclipse/Login1.xlsx"

rows= XLUtils.getRowCount(path,'Sheet1')

for r in range(2,rows+1):
    username= XLUtils.readData(path,"Sheet1",r,1)
    password= XLUtils.readData(path,"Sheet1",r,2)
    time.sleep(2)
    driver.find_element_by_name("userName").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("submit").click()
    print(driver.title)

    if driver.title=="Login: Mercury Tours":
        print("test is passed")
        XLUtils.writeData(path,"Sheet1",r,3,"Test passed")
    else:
        print("Test failed")
        XLUtils.writeData(path,"Sheet1",r,3,"Test failed")

    driver.find_element_by_link_text("Home").click()


