import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Navigation options
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('D:\selenium-python\webdrivers\chromedriver.exe', options=options)

    def test_buscar(self):
        driver = self.driver
        driver.get('https://www.google.com')
        self.assertIn("Google", driver.title)
        element = driver.find_element_by_name('q')
        element.send_keys('Selenium')
        element.send_keys(Keys.RETURN)
        time.sleep(2)
        assert 'No se encontró el elemento:' not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()