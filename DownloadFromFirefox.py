#error : program to skip save location while downloading from firefox
import time
from selenium import webdriver

fp= webdriver.FirefoxProfile() #set download location  for files
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","text/plain,application/pdf")# Mime type
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir","C:\df")
fp.set_preference("browser.download.folderList",2)
fp.set_preference("pdfjs.disabled",True)
time.sleep(6)
driver= webdriver.Firefox(executable_path="C:\driver\geckodriver.exe",firefox_profile=fp)
time.sleep(10)

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
