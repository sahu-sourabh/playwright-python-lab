import pytest
from playwright.sync_api import expect
from utils.config_loader import Config

@pytest.mark.parametrize("username, password, expected_url, should_see_error", [
    # Case 1: Successful Login
    (Config.USERNAME, Config.PASSWORD, "https://www.saucedemo.com/inventory.html", False),
    # Case 2: Locked Out User
    (Config.LOCKED_OUT_USERNAME, Config.PASSWORD, "https://www.saucedemo.com/", True),
    # Case 3: Invalid User (Optional - adds even more value!)
    ("invalid_user", "", "https://www.saucedemo.com/", True),
])
def test_login_scenarios(page, login_page, username, password, expected_url, should_see_error):
    # Action
    login_page.navigate()
    login_page.submit_login(username, password)

    # Judgment A: Check URL
    expect(page).to_have_url(expected_url)

    # Judgment B: Check Error Message if applicable
    if should_see_error:
        expect(login_page.error_message).to_be_visible()
    else:
        # Ensure error is NOT there on success
        expect(login_page.error_message).not_to_be_visible()
