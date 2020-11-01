from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
driver.maximize_window()
print(driver.title)
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
print(driver.current_window_handle)

handles = driver.window_handles  # returns all the handles values of opened browser windows

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    # closing a specific window using title
    if driver.title == "Frames & windows":
        driver.close()

driver.quit()
