from Seleniumpython.PomProjectDemo.Locators.locators import Locators
class HomePage():

    def __init__(self,driver): #creating constructor
        self.driver= driver

        self.welcome_link_id= Locators.welcome_link_id  #"welcome"
        # self.logout_link_linkText= "Logout"    #Locators.logout_link_linkText

    def click_welcome(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()

    def click_logout(self):
        # self.driver.find_element_by_link_text( self.logout_link_linkText).click()
        self.driver.find_element_by_xpath("//*[@id='welcome-menu']/ul/li[2]/a").click()
