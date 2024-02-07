from selenium.webdriver.common.by import By

from helpers.config_helper import get_dotenv_config


class GeneralUrlLocators:
    home_page_url = get_dotenv_config().get("HOMEPAGE")


class HomePageLocators:
    login_button = (By.ID, "login-button")
    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_containter = (By.ID, "login_containter")
    inventory_container = (By.ID, "inventory_container")
