import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
driver.get('https://www.techlistic.com/p/demo-selenium-practice.html')
print(driver.title)
#count no of rows
rows= len(driver.find_elements_by_xpath("//*[@id='post-body-5867683659713562481']/div/div[1]/table/tbody/tr"))
time.sleep(2)
#count no of columns
cols=len(driver.find_elements_by_xpath("//*[@id='post-body-5867683659713562481']/div/div[1]/table/tbody/tr[1]/td"))
print(rows)
print(cols)
print("Country"+"            "+"City"+"            "+"Height"+"            "+"Built"+"            "+"Rank"+"            "+"...")
for r in range(1,rows+1):
    for c in range(1,cols+1):
        value=driver.find_element_by_xpath("//*[@id='post-body-5867683659713562481']/div/div[1]/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value,end="              ")
    print()
driver.close()
# /html/body/div[1]/div[3]/div/div[2]/main/div/div[1]/div/article/div/div/div[3]/div/div[1]/table/tbody

# //*[@id="post-body-5867683659713562481"]/div/div[1]/table/tbody/tr[1]/td[6]
