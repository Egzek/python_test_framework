from selenium.common.exceptions import (
    ElementClickInterceptedException,
    TimeoutException,
)
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.support.wait import WebDriverWait

from helpers.screenshot_listener import ScreenshotListener


class BasePage:
    def __init__(self, driver):
        self.driver = EventFiringWebDriver(driver, ScreenshotListener())
        self.wait_time = WebDriverWait(self.driver.wrapped_driver, 15)

    def get_page(self, page: str) -> None:
        """
        Gets the page provided by the user.
        :param page: Define the page url to get.
        """
        self.driver.get(page)

    def find_element_on_page(self, element_to_find: tuple) -> WebElement:
        """
        Returns element found on the page
        :param element_to_find: locator used for finding given element
        :return: found element
        """
        return self.driver.find_element(*element_to_find)

    def find_elements_on_page(self, element_to_find: tuple) -> list:
        """
        Returns element found on the page
        :param element_to_find: locator used for finding given element
        :return: found elements
        """
        return self.driver.find_elements(*element_to_find)

    def click_element(self, element_to_find: tuple) -> None:
        """
        Clicks element found using locator
        :param element_to_find: locator used for finding given element
        """
        try:
            element = self.wait_until_element_clickable(element_to_find)
            element.click()
        except ElementClickInterceptedException:
            element = self.find_element_on_page(element_to_find)
            self.scroll_to_element(element)
            element.click()

    def scroll_to_element[T](self, element_to_scroll: T) -> None:
        """
        Scrolls to the given element
        :param element_to_scroll: Element to scroll to
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element_to_scroll)

    def input_text_to_element(self, string_to_input: str, element_to_find: tuple) -> None:
        """
        Finds the input using locator and sends given keys [string]
        :param string_to_input: string to send to given input field
        :param element_to_find: locator used for finding given input
        """
        self.wait_until_element_clickable(element_to_find).send_keys(string_to_input)

    def move_mouse_to_element(self, element_locator: tuple) -> None:
        """
        Moves mouse to the given element
        :param element_locator: locator used for finding element to move mouse to
        """
        element = self.find_element_on_page(element_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element.wrapped_element).perform()

    def wait_until_element_clickable(self, element_to_be_clickable: tuple, timeout: int = None) -> WebElement:
        """
        Waits for the element to be clickable
        :param element_to_be_clickable: element to check
        :param timeout: timeout to use instead of default one
        :return: Returns element
        """
        return (self.wait_time if not timeout else timeout).until(
            EC.element_to_be_clickable(element_to_be_clickable),
            f"Element {element_to_be_clickable} is not clickable on " f"{self.driver.current_url} ",
        )

    def wait_for_element_visibility(
        self,
        element_locator: tuple,
        should_be_visible: bool = True,
        timeout: int = None,
    ) -> WebElement:
        """
        Waits for the element to be visible
        :param element_locator: element to check
        :param should_be_visible: flag if we expect the element to be visible or not
        :param timeout: timeout to use instead of default one
        :return: Returns element
        """
        condition = EC.visibility_of_element_located(element_locator) if should_be_visible else EC.invisibility_of_element_located(element_locator)
        message = f"Element {element_locator} is {'not ' if should_be_visible else ''}" f"visible on {self.driver.current_url}"
        return (
            self.wait_time.until(condition, message)
            if timeout is None
            else WebDriverWait(self.driver.wrapped_driver, timeout).until(condition, message)
        )

    def assert_element_visibility(
        self,
        element_locator: tuple,
        should_be_visible: bool = True,
        message: str = None,
    ) -> None:
        """
        Asserts the element is visible
        :param element_locator: element to check
        :param should_be_visible: flag if we want element to be visible
        :param message: message to display if element not visible
        """
        message = (
            message if message else (f"Element {element_locator} is {'not ' if should_be_visible else ''}" f"visible on {self.driver.current_url}")
        )
        try:
            self.wait_for_element_visibility(
                element_locator=element_locator,
                should_be_visible=should_be_visible,
                timeout=5,
            )
            found = True
        except TimeoutException:
            found = False
        assert found, message
