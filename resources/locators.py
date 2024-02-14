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
    add_to_cart_item_page = (By.XPATH, "//div[@id='inventory_item_container']//button[contains(@id,'add-to-cart')]")
    remove_from_cart_item_page = (By.XPATH, "//div[@id='inventory_item_container']//button[contains(@id,'remove')]")
    back_to_products = (By.ID, "back-to-products")

    @classmethod
    def add_to_cart_button_from_inventory(cls, item: tuple) -> tuple:
        return (By.XPATH, f"//a[@id='{item[1]}']/parent::div/parent::div//button[contains(@id,'add-to-cart')]")

    @classmethod
    def remove_item_from_inventory(cls, item: tuple) -> tuple:
        return (By.XPATH, f"//a[@id='{item[1]}']/parent::div/parent::div//button[contains(@id,'remove')]")


class CartPageLocators:
    checkout_button = (By.ID, "checkout")
    continue_shopping = (By.ID, "continue-shopping")


class CheckoutPageLocators:
    first_name_field = (By.ID, "first-name")
    last_name_field = (By.ID, "last-name")
    zip_code_field = (By.ID, "postal-code")
    continue_checkout = (By.ID, "continue")
    finish_checkout = (By.ID, "finish")
    cancel_checkout = (By.ID, "cancel")
    checkout_succesfull_container = (By.XPATH, "//div[@id='checkout_complete_container']/h2[text()='Thank you for your order!']")
    pass


class NavigationLocators:
    shopping_cart_container = (By.ID, "shopping_cart_container")
    burger_menu_button = (By.ID, "react-burger-menu-btn")
