from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(service=Service("C:/Users/User/Desktop/Selenium+Python/Selenium Automation/drivers/chromedriver.exe"))

driver.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")
driver.maximize_window()

recovery=driver.find_element(By.LINK_TEXT,"¿Has olvidado la contraseña?")
recovery.click()
time.sleep(1)



driver.quit()