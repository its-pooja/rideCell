import pytest
from rideCell_Framework_Selenium_PageObject.rideCell_PageObject_Github.rideCell_PageObject_github_repositories import \
    githubRepository
from rideCell_Selenium_API.rideCell_API_github_repositories import gitHubRepositoryAPI
from rideCell_Selenium_Framework.rideCell_Framework_Utilities.rideCell_Framework_Utilities_BasicAction import \
    BasicAction

from rideCell_Selenium_Framework.rideCell_Framework_Utilities.rideCell_Framework_UI_logger import logGeneration


@pytest.mark.usefixtures("init_driver")
class Test_GitHub:

    def test_verifyRepositoriesAndDescriptions(self):
        """
        TC : Verify if repository names and descriptions retrieved from UI and API are same.
        """
        log = logGeneration.customLogger()
        base = BasicAction(self.driver)
        self.git = githubRepository(self.driver)
        self.git.click_repository_tab()
        log.info("Getting repository names and descriptions from UI")
        actual_dict_UI = self.git.getRepositoryNameAndDescription()

        log.info("Getting repository names and descriptions from API")
        expected_dict_API = gitHubRepositoryAPI.GitHub_API()

        log.info("Comparing repository names and description from UI and API")
        assert actual_dict_UI == expected_dict_API, base.logs_and_screenshot("test_verifyRepositoriesAndDescriptions")
        log.info("Test Case Passed")
