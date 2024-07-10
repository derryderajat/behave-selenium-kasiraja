from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class AuthPage:
    URL = 'https://kasirdemo.belajarqa.com'
    EMAIL_FIELD_XPATH = '//input[@id="email"]'
    PASSWORD_FIELD_XPATH = '//input[@id="password"]'
    LOGIN_BUTTON_XPATH = "//button[contains(text(),'login')]"
    
    def __init__(self, driver) -> None:
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.EMAIL_FIELD_XPATH)))

    def enter_email(self, email):
        email_field = self.driver.find_element(By.XPATH, self.EMAIL_FIELD_XPATH)
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.XPATH, self.PASSWORD_FIELD_XPATH)
        password_field.send_keys(password)
    
    def submit_login(self):
        login_button = self.driver.find_element(By.XPATH, self.LOGIN_BUTTON_XPATH)
        login_button.click()

    def is_redirected_to_dashboard(self):
        WebDriverWait(self.driver, 10).until(EC.url_contains("dashboard"))
        return "dashboard" in self.driver.current_url
    
    def is_on_login_page(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.EMAIL_FIELD_XPATH)))
        return self.URL in self.driver.current_url
