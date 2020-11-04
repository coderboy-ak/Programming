import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
        driver.get("https://www.google.com/")
        titleis= driver.title
        #assertEqual
        # self.assertEqual("Google",titleis,"webpages titles are not same")
        # self.assertNotEqual("Google",titleis,"WebPages titles are same")

        # self.assertTrue(titleis == "Google") #True  used when more than 2 parameters
        self.assertFalse(titleis == "Google123")

        check= None
        self.assertIsNone(check)
        self.assertIsNotNone(driver) #returns true bcoz driver contains value

        #assertIn verifies whther the first element is present in the second element
        #used in verifying presence of value in a list, tuple, set and directory

        list= {"python","selenium","java"}
        self.assertIn("python",list) # true
        self.assertNotIn("ruby",list) #true

        self.assertGreater(100,10)
        self.assertLess(10,100)
        self.assertGreaterEqual(100,100)
        self.assertLessEqual(100,100)

if __name__=="__main__":
    unittest.main()