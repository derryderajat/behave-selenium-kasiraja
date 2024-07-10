from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.AVATAR_XPATH = "//button[@id='menu-button-14']"
        self.LOGOUT_BTN_XPATH = "//button[@id='menu-list-14-menuitem-12']"
    def is_logged_in(self):
        return "dashboard" in self.driver.current_url

    def click_logout(self):
        # Avatar button
        avatar_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.AVATAR_XPATH))
        )
        avatar_button.click()
        
        # Logout button
        logout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.LOGOUT_BTN_XPATH))
        )
        logout_button.click()