from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
options=driver.find_elements(By.TAG_NAME,"option")

for opt in options:
        opt.click()   

driver.quit()