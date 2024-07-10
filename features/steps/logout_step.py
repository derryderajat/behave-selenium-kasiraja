from behave import given, when, then
from selenium import webdriver
from pages.auth_page import AuthPage
from pages.dashboard_page import DashboardPage
import os
from dotenv import load_dotenv
from features.utils.login_util import login_util

# Load environment variables from .env file in the features directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.env'))


@given('the user is logged in')
def step_impl(context):
    login_util(context)

@when('the user clicks the logout button')
def step_impl(context):
    context.dashboard_page.click_logout()

@then('the user should be redirected to the login page')
def step_impl(context):
    assert context.auth_page.is_on_login_page()
    context.driver.quit()

