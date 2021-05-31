from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Navigation options
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver = webdriver.Chrome('D:\selenium-python\webdrivers\chromedriver.exe', options=options)
driver.get('https://www.google.com')
finder = driver.find_element_by_name('q')
finder.send_keys('Automation Step by Step')
finder.send_keys(Keys.RETURN)
time.sleep(4)
driver.close()