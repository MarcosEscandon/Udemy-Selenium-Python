from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
checkmark=driver.find_elements(By.CLASS_NAME,"checkmark")

for check in checkmark:
    if check.is_displayed() == True and check.is_selected() == False:
        check.click()   

driver.quit()