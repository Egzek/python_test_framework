from selenium.webdriver.common.by import By

from helpers.config_helper import Config


class GeneralUrlLocators:
    home_page_url = Config().get_dotenv_config().get("HOMEPAGE")


class HomePageLocators:
    login_button = (By.ID, "login-button")
    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_containter = (By.ID, "login_containter")
    inventory_container = (By.ID, "inventory_container")


class InventoryPageLocators:
    sauce_lab_backpak_item = (By.ID, "item_4_title_link")
    sauce_lab_bike_light = (By.ID, "item_0_title_link")
    sauce_lab_bolt_tshirt = (By.ID, "item_1_title_link")
    sauce_lab_fleece_jacket = (By.ID, "item_5_title_link")
    sauce_lab_tshirt_red = (By.ID, "item_3_title_link")
    sauce_lab_onesie = (By.ID, "item_2_title_link")
    inventory_items = (By.CLASS_NAME, "inventory_item")
    add_to_cart_button_from_item_page = (By.XPATH, "//div[@id='inventory_item_container']//button")

    @classmethod
    def add_to_cart_button_from_inventory(cls, item: tuple) -> tuple:
        return (By.XPATH, f"//a[@id='{item[1]}']/parent::div/parent::div//button")


class CartPageLocators:
    checkout_button = (By.ID, "checkout")
    continue_shopping = (By.ID, "continue-shopping")


class CheckoutPageLocators:
    pass


class NavigationLocators:
    shopping_cart_container = (By.ID, "shopping_cart_container")
