import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
driver.get("https://web.whatsapp.com/")
driver.maximize_window()
print(driver.title)
print("Please scan qr code and press any key to continue :")
time.sleep(4)
name= input("enter the name of user or group :")
msg= input("enter your message:  ")
count= int(input("Enter the count: "))
user= driver.find_element_by_xpath("//span[@title='{}']".format(name))
user.click()
msg_box= driver.find_element_by_class_name('_3uMse')
for i in range(count):
    time.sleep(2)
    msg_box.send_keys(msg)
    msg_box.send_keys(Keys.ENTER)
    time.sleep(2)

driver.close()


