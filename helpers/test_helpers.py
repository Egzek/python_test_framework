from selenium.webdriver.remote.webdriver import WebDriver

from resources.locators import GeneralUrlLocators
from resources.PO.home_page import HomePage
from resources.models.user import User


def login_given_user(driver: WebDriver, user: User) -> None:
    page = HomePage(driver)
    page.get_page(GeneralUrlLocators.home_page_url)
    page.login_user(user=user)
