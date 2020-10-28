#import webbrowser
from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")

from Tools.scripts.treesync import raw_input

new =2
tabUrl="http://google.com/?#q=";
term=raw_input("enter search query: ");
#webbrowser.open(tabUrl+term,new=new);
driver.get(tabUrl+term)
driver.close()