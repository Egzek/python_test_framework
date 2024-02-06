from selenium.webdriver.common.by import By

from helpers.config_helper import get_dotenv_config


class GeneralUrlLocators:
    home_page_url = get_dotenv_config().get("HOMEPAGE")


class HomePageLocators:
    login_button = (By.XPATH, "//button[@e2e-id='login']")
    email_input = (By.XPATH, "//input[@name='username']")
    password_input = (By.XPATH, "//input[@name='password']")
    test_input1 = (By.XPATH, "//input[@name='password']")
    test_input2 = (By.XPATH, "//div[@e2e-id='test']/child::input")
    test_input3 = (By.XPATH, "//div[@class='test']/child::div")

    @classmethod
    def test_name1(cls, test: str) -> tuple:
        return (By.XPATH, f"//div[@text()='{test}']")

    @classmethod
    def test_name2(cls, test: str) -> tuple:
        return (By.XPATH, f"//div[@text()='{test}']")
