import time
import pytest
from selenium import webdriver

class TestSample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")
        driver.maximize_window()
        print(driver.title)
        yield
        driver.close()
        print("Test completed")


    def test_login(self,test_setup):
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        time.sleep(4)
    # def test_teardown():
    #     driver.close()
    #     print("Test completed")

