from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Navigation options
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'D:\selenium-python\webdrivers\chromedriver.exe'

driver = webdriver.Chrome(driver_path, options=options)

# Initialize Browser
driver.get('https://gmail.com')

user = driver.find_element_by_xpath('//input[@id="identifierId"]')
user.send_keys('audio.sitb')
user.send_keys(Keys.ENTER)
time.sleep(2)

password = driver.find_element_by_xpath('//input[@type="password"]')
user.send_keys('some password')
driver.find_element_by_css_selector('button.VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc lw1w4b'.replace(' ','.')).click()
