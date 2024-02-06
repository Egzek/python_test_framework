import logging
import os
import time
from functools import wraps

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.remote.webdriver import WebDriver

from helpers.common import get_project_root as ROOT


class ScreenshotListener(AbstractEventListener):
    def on_exception[T](self, exception: T, driver: WebDriver) -> None:
        driver_name = "test_" + f"[{driver.name}]"
        make_screenshot(driver, "driver", driver_name)


def make_screenshot(driver: WebDriver, producer: str, name_function: str) -> None:
    env = os.environ.get("ENV")
    timestr = time.strftime("%Y%m%d-%H%M%S")

    screenshot_name = rf"{name_function}_[{producer}_exception]_" + timestr + f"_{env}_env" + ".png"

    dir_png_path = ROOT() / "results" / "screenshots"
    if not os.path.exists(dir_png_path):
        os.makedirs(dir_png_path)
    screenshot_path = dir_png_path / screenshot_name
    driver.get_screenshot_as_file(str(screenshot_path))
    logging.info(f"\nScreenshot saved as {str(screenshot_path)}")


def screenshot_decorator[T](test_fun: T) -> T:
    @wraps(test_fun)
    def wrapper[T](self, *args, **kwargs) -> T:
        try:
            return test_fun(self, *args, **kwargs)
        except AssertionError as ex:
            make_screenshot(self.driver, "assertion", self.test_name)
            raise ex
        except TimeoutException as ex:
            make_screenshot(self.driver, "timeout", self.test_name)
            raise ex

    return wrapper
