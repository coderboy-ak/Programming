from selenium import webdriver
from Seleniumpython.LoginUtility import WebElement
driver=webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
element=WebElement()
driver.get('https://demo.mahara.org/')
# do assertion on the title
#driver.assertTrue("Home-Mahara Demo", driver.title)
# define username web element
username=driver.find_element_by_id(element.getSearchValue("LoginPage","LoginUserName"))
username.send_keys("student1")
password=driver.find_element_by_id(element.getSearchValue("LoginPage","LoginPassword"))
password.send_keys("Test@123stu")
loginbutton=driver.find_element_by_id(element.getSearchValue("LoginPage","SubmitButton"))
loginbutton.click()
print('login completed successfully')