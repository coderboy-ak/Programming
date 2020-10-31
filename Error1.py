import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from self import self


class DemoMaharaOrgLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
    def setUp(self):
        driver=self.driver
        driver.get("https://demo.mahara.org/")
        # define username web element
        username = driver.find_element_by_id("login_login_username")
        # enter student11 in the username field
        username.send_keys("student1")
        # define password web element
        password = driver.find_element_by_name("login_password")
        # enter password in the password field
        password.send_keys("Test@123stu")
        # define login button
        loginbutton = driver.find_element_by_id("login_submit")
        # click on login button
        loginbutton.click()
    def test_change_maximum_tags_in_cloud(self):
        driver=self.driver
        settings=driver.find_element_by_link_text("Settings")
        settings.click()
        driver.implicitly_wait(5)
        maxtags=driver.find_element_by_xpath("//*[@id='accountprefs_tagssideblockmaxtags']")
        maxtags.clear()
        maxtags.send_keys(30)
        self.driver.implicitly_wait(5)
        savebutton=driver.find_element_by_id("accountprefs_submit")
        savebutton.click()
        driver.implicitly_wait(4)
        max_text=driver.find_element_by_xpath("//*[@id='accountprefs_tagssideblockmaxtags']").get_attribute("value")
        print(max_text)
        self.assertTrue(max_text,"30")

    def test_change_default_licence(self):
        driver=self.driver
        settings=driver.find_element_by_link_text("Settings")
        settings.click()
        wait=WebDriverWait(driver,30)
        licence_select=wait.until(EC.presence_of_all_elements_located(By.XPATH,"//*[@id='accountprefs_licensedefault']"))
        select=Select(driver.find_element_by_xpath("//*[@id='accountprefs_licensedefault']"))
        driver.implicitly_wait(5)
        select.select_by_visible_text("Creative Commons Attribution 4.0")
        savebutton = driver.find_element_by_id("accountprefs_submit")
        savebutton.click()
        self.assertTrue(driver.find_element_by_xpath("//*[@id='accountprefs_licensedefault']").text,"Creative Commons Attribution 4.0")

    def tearDown(self):
        driver=self.driver
        logout=driver.find_element_by_link_text("Logout")

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
































































