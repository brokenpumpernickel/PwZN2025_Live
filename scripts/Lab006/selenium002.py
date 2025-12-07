from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

url = 'https://9gag.com'

options = Options()

service = Service('webdriver/chromedriver.exe')

driver = webdriver.Chrome(service=service, options=options)

driver.get(url)

WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[id^="sp_message_iframe"]'))
)


button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[title="Accept"]'))
)
button.click()

driver.switch_to.default_content()

search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.search'))
)
search_button.click()

search_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#top-navb > div > div > div.general-function > div > div > form > div.ui-input > input[type=text]'))
)
search_input.send_keys('poland')
search_input.send_keys(Keys.ENTER)

# for _ in range(100):
#     driver.execute_script('window.scrollBy(0, document.body.scrollHeight);')
#     time.sleep(1)

for _ in range(100):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(1)

time.sleep(5000)
driver.close()