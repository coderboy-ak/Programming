#error in this program
import unittest
import self as self
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestLogin(unittest.TestCase):
    # define a driver instance , for example Chrome
    def setUp(self):
        self.driver=webdriver.Chrome()

    def test_login_demo(self):
        driver=self.driver
        #navigate to the demo website
        driver.get("https://demo.mahara.org/")
        #do assertion on the title
        self.assertIn("Home-Mahara Demo",driver.title)
        #define username web element
        username =driver.find_element_by_id("login_login_username")
        #enter student11 in the username field
        username.send_keys("student1")
        #define password web element
        password=driver.fine_element_by_id("login_login_password")
        #enter password in the password field
        password.send_keys("Testing1")
        #define login button
        loginbutton=driver.find_element_by_id("login_submit")
        #click on login button
        loginbutton.click()
        #verify that logout link displays
        self.assertTrue(driver.find_element_by_link_text("Logout"),"Logout link")

    def tearDown(self):
        self.driver.close()
if __name__ == '__main__':
    unittest.main()
