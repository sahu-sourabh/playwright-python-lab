from playwright.sync_api import Page, expect

def test_sauce_demo(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    # Verify login success
    expect(page.get_by_text("Products")).to_be_visible()