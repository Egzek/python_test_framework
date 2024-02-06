import pytest

from helpers.screenshot_listener import screenshot_decorator
from resources.PO.home_page import HomePage


@pytest.mark.sample
class TestSample:
    @screenshot_decorator
    def test_sample(self):
        """
        1. sample
        """
        page = HomePage(self.driver)
        pass
        # page = HomePage(self.driver)
        # page.login_user(self.user_default)
        # sample_name = generate_unique_name()
        # page.assert_sample(sample_name)
