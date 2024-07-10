from behave import given, when, then
from selenium import webdriver
from pages.auth_page import AuthPage
import os
from dotenv import load_dotenv

# Load environment variables from .env file in the features directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.env'))

@given('the user is on the login page')
def step_impl(context):
        context.driver = webdriver.Chrome()
        context.auth_page = AuthPage(context.driver)
        context.auth_page.open()

@when('the user enters valid credentials')
def step_impl(context):
        email = os.getenv("LOGIN_EMAIL")
        password = os.getenv("LOGIN_PASSWORD")
        context.auth_page.enter_email(email)
        context.auth_page.enter_password(password)

@when('the user submits the login forms')
def step_impl(context):
    context.auth_page.submit_login()

@then('the user should be redirected to the dashboard')
def step_impl(context):
    assert context.auth_page.is_redirected_to_dashboard()
    context.driver.quit()



