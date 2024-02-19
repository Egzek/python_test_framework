from resources.locators import (
    NavigationLocators,
)
from resources.PO.base_page import BasePage


class Navigation(BasePage):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def open_cart(self) -> None:
        self.click_element(NavigationLocators.shopping_cart_container)
