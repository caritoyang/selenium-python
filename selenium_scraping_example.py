# Libraries
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Navigation options
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'D:\selenium-python\webdrivers\chromedriver.exe'

driver = webdriver.Chrome(driver_path, options=options)

# Initialize Browser
driver.get('https://eltiempo.es')

# timeout: 5 segundos - si no encuentra el elemento se corta
# EC -> Expected Condition
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                       'button.didomi-components-button didomi-button didomi-dismiss-button didomi-components-button--color didomi-button-highlight highlight-button'.replace(' ','.'))))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#term')))\
    .send_keys('Madrid')

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.icon.icon-search')))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH, '//a[child::*[text()="Madrid, Madrid"]]')))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Por horas"]')))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.presence_of_element_located((By.XPATH, "(//ul[@class='m_table_weather_hour']//child::ul)[1]")))

texto = driver.find_element_by_xpath("(//ul[@class='m_table_weather_hour']//child::ul)[1]").text

# Split the text until 'Mañana'
tiempo_hoy = texto.split('Mañana')[0].split('\n')[1:-1]

horas = list()
temp = list()
v_viento = list()

for i in range(0, len(tiempo_hoy), 4):
    horas.append(tiempo_hoy[i])
    temp.append(tiempo_hoy[i+1])
    v_viento.append(tiempo_hoy[i+2])

df = pd.DataFrame({'Horas': horas,
                   'Temperatura': temp,
                   'Velocidad del Viento(km/h)': v_viento})

print(df)
df.to_csv('tiempo_hoy.csv', index=False)

driver.quit()