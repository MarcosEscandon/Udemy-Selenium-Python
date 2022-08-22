from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(service=Service("C:/Users/User/Desktop/Selenium+Python/Selenium Automation/drivers/chromedriver.exe"))

driver.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")
driver.maximize_window()

user=driver.find_element(By.CLASS_NAME,"form-control")
passwd=driver.find_element(By.CLASS_NAME,"textinput textInput form-control")
time.sleep(1)

user.send_keys("marcos@gmail.com")
passwd.send_keys("12345678910")
time.sleep(1)

btn=driver.find_element(By.CLASS_NAME,"btn btn-primary ")
btn.click()

driver.quit()