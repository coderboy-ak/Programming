import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
print(driver.title)
driver.implicitly_wait(2)
driver.maximize_window()
total_input=driver.find_elements(By.CLASS_NAME,'text_field')
print(len(total_input))
driver.find_element(By.NAME,"RESULT_TextField-1").send_keys("pawan")
driver.find_element(By.NAME,"RESULT_TextField-2").send_keys("kumar")
driver.find_element(By.NAME,"RESULT_TextField-3").send_keys("5555555555")
driver.find_element(By.NAME,"RESULT_TextField-4").send_keys("INDIA")
driver.find_element(By.NAME,"RESULT_TextField-5").send_keys("GZB")
driver.find_element(By.NAME,"RESULT_TextField-6").send_keys("abc@gmail.com")
status=driver.find_element(By.ID,"RESULT_RadioButton-7_0").is_selected()
print(status)
driver.find_element(By.XPATH,"/html/body/form/div[2]/div[15]/table/tbody/tr[1]/td/label").click()
# driver.find_element(By.ID,"RESULT_RadioButton-7_0").click()#male radio button
driver.find_element(By.XPATH,"/html/body/form/div[2]/div[17]/table/tbody/tr[1]/td/label").click()
# driver.find_element(By.ID,"RESULT_CheckBox-8_0").click()#sunday checkbox
# driver.find_element(By.ID,"RESULT_CheckBox-8_6").click()#saturday checkbox
status_c=driver.find_element(By.ID,"RESULT_CheckBox-8_0").is_selected()
print(status_c)
element=driver.find_element(By.ID,"RESULT_RadioButton-9")
drp=Select(element)
# drp.select_by_visible_text("Morning")
# drp.select_by_index(2)
drp.select_by_value("Radio-2") #Evening

#count number of options
print(len(drp.options))

#capture all the options and print them as output
all_options=drp.options
for option in all_options:
    print(option.text)

links=driver.find_elements(By.TAG_NAME,"a")
print("no of links : ",len(links))

for link in links:
    print(link.text)
#Explicit wait
wait= WebDriverWait(driver,5)
element=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/form/div[2]/div[17]/table/tbody/tr[7]/td/label")))
element.click()
driver.find_element(By.LINK_TEXT,"Software Testing Tutorials").click()
driver.back()
driver.close()

