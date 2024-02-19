import logging

from mimesis import Person, Address
from mimesis.locales import Locale

from resources.models.user import UserCheckout
from resources.PO.navigation import Navigation
from resources.locators import CheckoutPageLocators

logger = logging.getLogger(__name__)


class CheckoutPage(Navigation):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    @staticmethod
    def create_user_data_for_checkout(locale: Locale) -> UserCheckout:
        person = Person(locale=locale)
        address = Address(locale=locale)
        last_name = person.last_name()
        first_name = person.first_name()
        zip_code = address.zip_code()
        user = UserCheckout(
            first_name=first_name,
            last_name=last_name,
            zip_code=zip_code,
        )
        logging.debug(f"Created checkout user: {user.first_name} {user.last_name}, zip-code: {user.zip_code}")
        return user

    def finish_checkout(self, user: UserCheckout) -> None:
        self.input_text_to_element(user.first_name, CheckoutPageLocators.first_name_field)
        self.input_text_to_element(user.last_name, CheckoutPageLocators.last_name_field)
        self.input_text_to_element(user.zip_code, CheckoutPageLocators.zip_code_field)
        self.click_element(CheckoutPageLocators.continue_checkout)
        self.click_element(CheckoutPageLocators.finish_checkout)

    def assert_checkout_sucessfull(self) -> None:
        self.assert_element_visibility(CheckoutPageLocators.checkout_succesfull_container)
