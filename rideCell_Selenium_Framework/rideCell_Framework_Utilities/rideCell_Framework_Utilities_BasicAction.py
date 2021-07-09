from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from rideCell_Selenium_Framework.rideCell_Framework_Utilities.rideCell_Framework_UI_logger import logGeneration


class BasicAction:

    def __init__(self, driver):
        self.driver = driver

    def perform_click(self, locator):
        """
        Performs click on given locator

        :Args:
        - locator: locator of element to click
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def get_elements(self, locator):
        """
        returns list of elements found

        :Args:
        - locator: locator of elements to find
        """
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))

    def get_element(self, locator):
        """
        returns the element found

        :Args:
        - locator: locator of element to find
        """
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def take_screen_shot(self, name):
        """
        captures screenshot of webpage

        :Args:
        - name: name of test case
        """
        self.driver.save_screenshot(
            "../../../rideCell_Selenium_Framework/rideCell_Framework_UI_Screenshots/" + name + ".png")

    def logs_and_screenshot(self, name):
        """
        captures screenshot and logs

        :Args:
        - name: name of test case
        """
        self.driver.save_screenshot(
            "../../../rideCell_Selenium_Framework/rideCell_Framework_UI_Screenshots/" + name + ".png")
        log = logGeneration.customLogger()
        log.error("Test Case " + name + " has Failed")

    @staticmethod
    def create_dict_from_list(keys_list1, value_list2):
        """
        returns the dictionary created from lists

        :Args:
        - keys_list1: list of keys
        - value_list2 : list of values
        """
        merged_dict = {}
        for key in keys_list1:
            for value in value_list2:
                merged_dict[key] = value
                value_list2.remove(value)
                break
        return merged_dict
