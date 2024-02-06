from resources.PO.base_page import BasePage
from resources.locators import (
    GeneralUrlLocators,
)


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        if self.driver.current_url == ("data:," or "about:blank"):
            print(GeneralUrlLocators.home_page_url)
            self.get_page(GeneralUrlLocators.home_page_url)
