import pytest
from pages.login_page import LoginPage

@pytest.fixture
def login_page(page):
    """Provides a pre-configured LoginPage instance to any test."""
    lp = LoginPage(page)
    return lp
