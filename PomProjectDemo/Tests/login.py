#error in creating html reports
import time
import unittest
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from Seleniumpython.PomProjectDemo.Pages.loginPage import LoginPage
from  Seleniumpython.PomProjectDemo.Pages.homepage import HomePage

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver= self.driver # created to avoid self.driver everywhere
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")

        login= LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage= HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner= HTMLTestRunner(output='E:/Programming/Seleniumpython/PomProjectDemo/Reports'))

# Pom ,unit test and html reports
# installed html-test runner and selenium from cmd
# 1.create a simple  login test
# 2.implement unit testing
# 3.implement page object model
# 4.seperate test script and objects
# 5.create a separate class for locators
# 6.run from cmd
# 7.add html reports

# note: classmethod is used due to using setupclass  and teardownclass methods
# run-edit configuration-add pythontest from + sign-delete login in python-pythontest-unittest-name(login)-location.

# print(self.driver.title)
        # self.driver.implicitly_wait(2)
        # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # self.driver.find_element_by_id("btnLogin").click()
        # time.sleep(4)
        # self.driver.find_element_by_id("welcome").click()
        # self.driver.find_element_by_link_text("Logout").click()
        # time.sleep(4)