import requests
import jsonpath
from rideCell_Selenium_Framework.rideCell_Framework_Utilities.rideCell_Framework_Utilities_BasicAction import \
    BasicAction
from ridCell_Framework_Selenium_Tests.rideCell_Framework_Selenium_DataSource.rideCell_Freamework_Selenium_BaseData import \
    BaseData
from rideCell_Selenium_Framework.rideCell_Framework_Utilities.rideCell_Framework_UI_logger import logGeneration


class gitHubRepositoryAPI(BasicAction):

    @staticmethod
    def GitHub_API():
        """
         returns dictionary of repository name and description from API
         """
        log = logGeneration.customLogger()

        response = requests.get(BaseData.api_url)

        repository_name_api = jsonpath.jsonpath(response.json(), "$.*['name']'")
        repository_desc_api = jsonpath.jsonpath(response.json(), "$.*['description']")

        expected_dict_API = BasicAction.create_dict_from_list(repository_name_api, repository_desc_api)
        log.info("Returning dictionary  of repository names and description from API")
        return expected_dict_API
