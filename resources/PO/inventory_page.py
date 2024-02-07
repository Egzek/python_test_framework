from resources.locators import (
    InventoryPageLocators,
    GeneralUrlLocators,
)
from resources.PO.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        if self.driver.current_url == ("data:," or "about:blank"):
            self.get_page(GeneralUrlLocators.home_page_url + "inventory")

    def buy_item_from_inventory(self, item_to_buy: tuple) -> None:
        """
        Buy item from inventory
        :param item_to_buy: Locator for item to buy
        """
        self.click_element(InventoryPageLocators.add_to_cart_button_from_inventory(item_to_buy))

    def buy_item_from_item_page(self, item_to_buy: tuple) -> None:
        """
        Buy item from item page
        :param item_to_buy: Locator for item to buy
        """
        self.click_element(item_to_buy)
        self.click_element(InventoryPageLocators.add_to_cart_button_from_item_page)
