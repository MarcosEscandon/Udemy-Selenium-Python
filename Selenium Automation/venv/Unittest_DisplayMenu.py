import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class menu_desp(unittest.TestCase):
    def setUp(self) -> None:    
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_recorrer(self):
        self.driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
        options=self.driver.find_elements(By.TAG_NAME,"option")

        for opt in options:
                opt.click()   

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()