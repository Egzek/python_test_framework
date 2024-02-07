import pytest

from helpers.screenshot_listener import screenshot_decorator
from resources.PO.inventory_page import InventoryPage
from resources.data.item_list import ITEM_LIST
from resources.locators import InventoryPageLocators


@pytest.mark.buy
class TestBuyItems:
    @pytest.mark.parametrize("item", ITEM_LIST.values(), ids=ITEM_LIST.keys())
    @screenshot_decorator
    def test_buy_item_from_item_page(self, login_default_user, item):
        """
        1. Get HomePage
        2. Log in user
        3. Assert user is logged in
        """
        page = InventoryPage(self.driver)
        page.buy_item_from_item_page(item)

    @pytest.mark.parametrize("item", ITEM_LIST.values(), ids=ITEM_LIST.keys())
    @screenshot_decorator
    def test_buy_item_from_inventory(self, login_default_user, item):
        """
        1. Get HomePage
        2. Log in user
        3. Assert user is logged in
        """
        page = InventoryPage(self.driver)
        page.buy_item_from_inventory(InventoryPageLocators.sauce_lab_backpak_item)
