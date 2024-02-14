import pytest

from mimesis.locales import Locale

from helpers.screenshot_listener import screenshot_decorator
from resources.PO.cart_page import CartPage
from resources.PO.checkout_page import CheckoutPage
from resources.PO.inventory_page import InventoryPage
from resources.data.item_list import ITEM_LIST
from resources.locators import InventoryPageLocators


@pytest.mark.buy
class TestBuyItems:
    @pytest.mark.parametrize("item", ITEM_LIST.values(), ids=ITEM_LIST.keys())
    @screenshot_decorator
    def test_buy_item_from_item_page(self, login_default_user, item):
        page = InventoryPage(self.driver)
        page.add_item_from_item_page_to_cart(item)

    @pytest.mark.parametrize("item", ITEM_LIST.values(), ids=ITEM_LIST.keys())
    @screenshot_decorator
    def test_buy_item_from_inventory(self, login_default_user, item):
        page = InventoryPage(self.driver)
        page.add_item_from_inventory_to_cart(item)

    @screenshot_decorator
    def test_buy_backpack_from_item_page(self, login_default_user):
        page = InventoryPage(self.driver)
        page.add_item_from_item_page_to_cart(InventoryPageLocators.sauce_lab_backpak_item)
        page.open_cart()
        page = CartPage(self.driver)
        page.go_to_checkout()
        page = CheckoutPage(self.driver)
        user_checokut = page.create_user_data_for_checkout(Locale.EN)
        page.finish_checkout(user_checokut)
        page.assert_checkout_sucessfull()


@pytest.mark.cart
class TestCart:
    @pytest.mark.parametrize("item", ITEM_LIST.values(), ids=ITEM_LIST.keys())
    @screenshot_decorator
    def test_add_and_remove_item_to_cart_from_item_page(self, login_default_user, item):
        page = InventoryPage(self.driver)
        page.add_item_from_item_page_to_cart(item)
        page.click_element(InventoryPageLocators.remove_from_cart_item_page)

    @pytest.mark.parametrize("item", ITEM_LIST.values(), ids=ITEM_LIST.keys())
    @screenshot_decorator
    def test_buy_item_from_inventory(self, login_default_user, item):
        page = InventoryPage(self.driver)
        page.add_item_from_inventory_to_cart(item)
        page.click_element(InventoryPageLocators.remove_item_from_inventory(item))
