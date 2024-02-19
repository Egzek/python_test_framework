from resources.locators import (
    HomePageLocators,
    GeneralUrlLocators,
)
from resources.models.user import User
from resources.PO.navigation import Navigation


class HomePage(Navigation):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        if self.driver.current_url == ("data:," or "about:blank"):
            print(GeneralUrlLocators.home_page_url)
            self.get_page(GeneralUrlLocators.home_page_url)

    def login_user(self, user: User) -> None:
        """
        Login user with username and password and assert user is logged in
        :param user: User to login
        """
        self.input_text_to_element(user.email, HomePageLocators.username_input)
        self.input_text_to_element(user.password, HomePageLocators.password_input)
        self.click_element(HomePageLocators.login_button)
        self.assert_element_visibility(HomePageLocators.inventory_container)
        self.assert_element_visibility(element_locator=HomePageLocators.login_containter, should_be_visible=False)
