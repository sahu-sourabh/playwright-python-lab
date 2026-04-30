from playwright.sync_api import Page
from utils.config_loader import Config
from utils.logger import get_logger

logger = get_logger(__name__)

class LoginPage:
    # constructor
    def __init__(self, page: Page):
        # object
        self.page = page
        # protected locators
        self._username_input = page.get_by_placeholder("Username")
        self._password_input = page.get_by_placeholder("Password")
        self._login_button = page.get_by_role("button", name="Login")

    def navigate(self):
        self.page.goto(url=Config.SAUCE_BASE_URL)

    def submit_login(self, username, password):
        logger.info(f"Attempting login for user: {username}")
        self._username_input.fill(username)
        self._password_input.fill(password)
        self._login_button.click()

    @property
    def error_message(self):
        # A 'Getter' that returns the locator.
        return self.page.locator("[data-test='error']")

    def smart_click_login(self):
        # Logic: Tries the primary locator, falls back to fuzzy match on timeout.
        try:
            # Strategy A: The Resilient data-test
            self._login_button.click(timeout=2000)
        except Exception as e:
            from utils.logger import logger
            logger.warning(f"Primary locator failed: {e}. Attempting AI-style fuzzy match...")
            # Strategy B: Fuzzy 'Smart' match
            self.page.locator("button", has_text="Login").click()
