from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from rideCell_Selenium_Framework.rideCell_Framework_Utilities.rideCell_Framework_UI_logger import logGeneration


class BasicAction:

    def __init__(self, driver):
        self.driver = driver

    def perform_click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def get_elements(self, locator):
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        return elements

    def get_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element

    def take_screen_shot(self, name):
        self.driver.save_screenshot(
            "../../../rideCell_Selenium_Framework/rideCell_Framework_UI_Screenshots/" + name + ".png")

    def logs_and_screenshot(self, name):
        self.driver.save_screenshot(
            "../../../rideCell_Selenium_Framework/rideCell_Framework_UI_Screenshots/" + name + ".png")
        log = logGeneration.customLogger()
        log.error("Test Case " + name + " has Failed")

    @staticmethod
    def create_dict_from_list(keys_list1, value_list2):
        merged_dict = {}
        for key in keys_list1:
            for value in value_list2:
                merged_dict[key] = value
                value_list2.remove(value)
                break
        return merged_dict
