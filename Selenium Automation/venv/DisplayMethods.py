from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
menu=Select(driver.find_element(By.XPATH,"//*[@id='main']/div[3]/div[1]/select"))  

menu.select_by_index(6)
time.sleep(3)
menu.select_by_value("6")
time.sleep(3)
menu.select_by_visible_text("Ford")
time.sleep(3)

driver.quit()