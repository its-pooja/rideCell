from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest

from rideCell_Selenium_Framework.rideCell_Framework_Utilities.rideCell_Framework_UI_logger import logGeneration
from ridCell_Framework_Selenium_Tests.rideCell_Framework_Selenium_DataSource.rideCell_Freamework_Selenium_BaseData import BaseData


@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    log = logGeneration.customLogger()

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    if request.param == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        log.info("Launching chrome browser")
    if request.param == "FF":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        log.info("Launching Firefox browser")

    driver.maximize_window()
    driver.get(BaseData.base_url)
    request.cls.driver = driver

    yield
    log.info("Closing the browser")
    driver.close()
