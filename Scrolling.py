from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')
print(driver.title)
driver.maximize_window() #maximize window size

#1.Scroll down page by pixels
driver.execute_script("window.scrollBy(0,1000)"," ")

#2.Scroll down page till the element is visible
flag=driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[2]")
driver.execute_script("arguments[0].scrollIntoView();",flag)

#3.Scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

driver.close()

