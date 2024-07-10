from selenium import webdriver
from pages.auth_page import AuthPage
from pages.dashboard_page import DashboardPage
import os
from dotenv import load_dotenv

# Load environment variables from .env file in the features directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.env'))

def login_util(context):
    context.driver = webdriver.Chrome()
    context.auth_page = AuthPage(context.driver)
    context.auth_page.open()
    email = os.getenv("LOGIN_EMAIL")
    password = os.getenv("LOGIN_PASSWORD")
    context.auth_page.enter_email(email)
    context.auth_page.enter_password(password)
    context.auth_page.submit_login()
    context.dashboard_page = DashboardPage(context.driver)
    # assert context.dashboard_page.is_logged_in()
