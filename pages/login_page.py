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
        # Added for Negative Testing
        self._error_message = page.locator("[data-test='error']")

    def navigate(self):
        self.page.goto(Config.BASE_URL)

    def submit_login(self, username, password):
        logger.info(f"Attempting login for user: {username}")
        self._username_input.fill(username)
        self._password_input.fill(password)
        self._login_button.click()
