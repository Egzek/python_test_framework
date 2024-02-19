from resources.locators import (
    CartPageLocators,
    GeneralUrlLocators,
)
from resources.PO.navigation import Navigation


class CartPage(Navigation):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        if self.driver.current_url == ("data:," or "about:blank"):
            self.get_page(GeneralUrlLocators.home_page_url + "cart")

    def go_to_checkout(self) -> None:
        self.click_element(CartPageLocators.checkout_button)

    def go_to_inventory(self) -> None:
        self.click_element(CartPageLocators.continue_shopping)
