from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
driver=webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")

driver.get('https://demo.mahara.org/')
# do assertion on the title
#driver.assertTrue("Home-Mahara Demo", driver.title)
# define username web element
username = driver.find_element_by_id("login_login_username")
# enter student11 in the username field
username.send_keys("student1")
# define password web element
password = driver.find_element_by_name("login_password")
# enter password in the password field
password.send_keys("Test@123stu")
# define login button
loginbutton = driver.find_element_by_id("login_submit")
# click on login button
loginbutton.click()
print('login completed successfully')
driver.find_element_by_xpath("/html/body/header/div/div/div[2]/button[2]/span[2]").click()
driver.find_element_by_xpath("/html/body/header/div/div/nav[3]/div/ul/li[4]/a").click()
driver.find_element_by_xpath("//*[@id='userchildmenu-0']/li[1]/a").click()
print('preferences clicked ')
select = Select(driver.find_element_by_xpath("//*[@id='accountprefs_licensedefault']"))
driver.implicitly_wait(5)
select.select_by_visible_text("Creative Commons Attribution 4.0")
print('Default licence selected')
maxtags = driver.find_element_by_xpath("//*[@id='accountprefs_tagssideblockmaxtags']")
maxtags.clear()
maxtags.send_keys(30)
print('Maximum tags in cloud is set to 30')
max_text = driver.find_element_by_xpath("//*[@id='accountprefs_tagssideblockmaxtags']").get_attribute("value")
print(max_text)
driver.implicitly_wait(5)
savebutton = driver.find_element_by_id("accountprefs_submit")
savebutton.click()
print('Program completed successfully')
driver.close()