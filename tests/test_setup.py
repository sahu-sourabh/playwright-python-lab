import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    # 1. Navigate to the page
    page.goto("https://playwright.dev/")

    # 2. Expect the title to contain "Playwright"
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    # 1. Navigate to the page
    page.goto("https://playwright.dev/")

    # 2. Click on the "Get Started" link
    page.get_by_role("link", name="Get Started").click()

    # 3. Expect page to have a heading with the name of installation
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()