from playwright.sync_api import expect
from utils.config_loader import Config

def test_successful_login(page, login_page):
    # Use the methods from the LoginPage class to perform actions
    login_page.navigate()
    login_page.submit_login(Config.USERNAME, Config.PASSWORD)

    # Verify login success
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_locked_out_user(login_page):
    # Use the methods from the LoginPage class to perform actions
    login_page.navigate()
    login_page.submit_login(Config.LOCKED_OUT_USERNAME, Config.PASSWORD)

    # Verify error message is visible
    expect(login_page._error_message).to_be_visible()
