from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
checkbox=driver.find_element(By.XPATH,"//*[@id='main']/div[3]/div[1]/input[1]")
print(checkbox.is_selected())
print(checkbox.is_enabled())
print(checkbox.is_displayed())

driver.quit()