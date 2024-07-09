from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.common.by import By

class AuthPage:
    URL = 'https://kasirdemo.belajarqa.com'
    def __init__(self, driver) -> None:
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        time.sleep(2)

    def enter_email(self, email):
        email_field = self.driver.find_element(By.XPATH, '//input[@id="email"]')
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.XPATH, '//input[@id="password"]')
        password_field.send_keys(password)
    
    def submit_login(self):
        login_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'login')]")
        login_button.click()

    def is_redirected_to_dashboard(self):
        WebDriverWait(self.driver, 10).until(EC.url_contains("dashboard"))
        return "dashboard" in self.driver.current_url
