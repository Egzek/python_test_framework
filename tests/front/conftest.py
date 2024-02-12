import logging
import pytest

from selenium import webdriver
from selenium.common.exceptions import InvalidSessionIdException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from helpers.test_helpers import login_given_user
from resources.credentials.sample_credentials import Credentials
from resources.models.user import User


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

browsers_options = {
    "chrome": webdriver.ChromeOptions(),
    # "firefox": webdriver.FirefoxOptions(),
}


@pytest.fixture(params=browsers_options.keys(), scope="function", autouse=True)
def setup(request):
    options = browsers_options[request.param]
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )
    logger.debug("Tests running on local chrome instance")

    assert driver is not None

    driver.maximize_window()
    request.cls.test_name = request.node.name
    request.cls.driver = driver

    try:
        yield driver
    except InvalidSessionIdException as ex:
        logging.warning("INVALID SESSION")
        raise ex
    except WebDriverException as ex:
        logging.warning("Invalid Connection")
        raise ex
    finally:
        driver.quit()


def set_default_user():
    return User(
        email=Credentials.default_user_mail,
        password=Credentials.default_user_password,
    )


@pytest.fixture(scope="function", autouse=True)
def get_default_user(request) -> None:
    user_default = set_default_user()
    request.cls.user_default = user_default


@pytest.fixture(scope="function")
def login_default_user(setup: WebDriver) -> None:
    user = set_default_user()
    login_given_user(
        driver=setup,
        user=user,
    )
