from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

url = 'https://www.bip.pw.edu.pl/Sklad-osobowy/Podstawowe-jednostki-organizacyjne/Wydzial-Fizyki/Pracownicy-wydzialu'

options = Options()

service = Service('webdriver/chromedriver.exe')

driver = webdriver.Chrome(service=service, options=options)

driver.get(url)

#main_div = driver.find_element(By.CLASS_NAME, 'class-folder')
main_div = driver.find_element(By.CSS_SELECTOR, 'div.class-folder')

employee_data = main_div.find_elements(By.CLASS_NAME, 'class-pracownik')    

for employee in employee_data:
    print(employee.tag_name)
    print(employee.text.strip())
    print('--------------------------------------')

time.sleep(5000)
driver.close()