from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")

driver.get('https://demo.mahara.org/')
driver.maximize_window()
username = driver.find_element_by_id("login_login_username")
# enter student11 in the username field
username.send_keys("student1")
# define password web element
password = driver.find_element_by_name("login_password")
# enter password in the password field
password.send_keys("Test@123stu")
username.clear()
username = driver.find_element_by_xpath("//input[@id='login_login_username']")
username.send_keys("Xpath Expression")
mahara_wiki= driver.find_element_by_link_text("Mahara wiki")
mahara_wiki.click()
#driver.back()
mahara_user= driver.find_element_by_partial_link_text("Mahara user")
print(mahara_user.get_attribute("href"))
footer=driver.find_element_by_tag_name("footer")
print(footer.text)
login_link= driver.find_element_by_class_name("login-related-links")
print(login_link.text)
site_logo=driver.find_element_by_css_selector("a.logo")
print(site_logo.get_attribute("href"))
print(site_logo.is_displayed())

# behave features\orangehrm.feature
