import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
driver.get('http://www.facebook.com')

#get the window handle after window has opened
window_before= driver.window_handles[0]
window_before_title=driver.title
print(window_before_title)

#open a new window
driver.execute_script("window.open('http://www.twitter.com', 'new window')")
time.sleep(2)
#get the window handle after the new window has opened
window_after=driver.window_handles[1]

#switch onto new child window
driver.switch_to.window(window_after)
window_after_title=driver.title
print(window_after_title)

#compare and verify that main window and current window title don't match
if window_before_title != window_after_title:
    print('Context switched to Twitter, so the title did not match')
else:
    print('Control did not switch to new window')
#switch back to original window

driver.switch_to.window(window_before)

#verify that the title now match
if window_before_title == driver.title:
    print('Context returned to parent window. Title now match')
print('Current title :',driver.title)
driver.close()
driver.quit()
