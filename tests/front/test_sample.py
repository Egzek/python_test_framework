import pytest

from helpers.screenshot_listener import screenshot_decorator
from resources.PO.home_page import HomePage


@pytest.mark.login
class TestLogin:
    @screenshot_decorator
    def test_login_username(self):
        """
        1. sample
        """
        page = HomePage(self.driver)
        page.login_user(self.user_default)
