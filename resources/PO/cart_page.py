from resources.locators import (
    GeneralUrlLocators,
)
from resources.PO.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        if self.driver.current_url == ("data:," or "about:blank"):
            self.get_page(GeneralUrlLocators.home_page_url + "cart")
