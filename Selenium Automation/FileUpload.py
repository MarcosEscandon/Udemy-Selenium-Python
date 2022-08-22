from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("https://www.w3schools.com/howto/howto_html_file_upload_button.asp")
button=driver.find_element(By.ID,"myFile")
button.send_keys("C:/Users/User/sc.jpg")
time.sleep(1)

driver.quit()