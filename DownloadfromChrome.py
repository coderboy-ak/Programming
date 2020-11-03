import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromeOptions= Options() #set download location  for files
chromeOptions.add_experimental_option("prefs",{"download.default_directory":"C:\df"})

driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe",options=chromeOptions)
driver.get("http://demo.automationtesting.in/FileDownload.html")
print(driver.title)
driver.maximize_window() #maximize window size
time.sleep(2)
# download text file
driver.find_element_by_id("textbox").send_keys("Downloding text file")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()

#download pdf file
driver.find_element_by_id("pdfbox").send_keys("Downloding pdf file")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()
time.sleep(4)
# driver.close()