from selenium.webdriver.common.by import By
from rideCell_Selenium_Framework.rideCell_Framework_Utilities.rideCell_Framework_Utilities_BasicAction import BasicAction
from rideCell_Selenium_Framework.rideCell_Framework_Utilities.rideCell_Framework_UI_logger import logGeneration


class githubRepository(BasicAction):

    repositoryTab_Tab_CssSelector = (By.CSS_SELECTOR,"nav[class*='js-profile-tab'] ul[class*='list-style'] li:nth-child(1) > a")
    repositories_name_link_xpath = (By.XPATH, "//a[@itemprop='name codeRepository']")
    global log
    log = logGeneration.customLogger()

    def click_repository_tab(self):
        log.info("Clicking on repository tab")
        self.perform_click(self.repositoryTab_Tab_CssSelector)

    def getRepositoriesName(self):
        log.info("Getting repository Names from UI")
        return self.get_elements(self.repositories_name_link_xpath)

    def get_xpath(self,var):
        return self.driver.find_element(By.XPATH, "//a[@href=""'" + var + "'""]//parent::h3//following-sibling::p")

    def getRepositoryNameAndDescription(self):
        repository_desc= []
        repository_names = []

        repositories = self.getRepositoriesName()

        for name in repositories:
            repository_names.append(name.text)
            try:
                href = name.get_attribute("href")
                partial_href = href.replace("https://github.com", "")

                desc = self.get_xpath(partial_href)
                repository_desc.append(desc.text)

            except:
                repository_desc.append(None)
                continue

        log.info("Returning dictionary of repository names and description from UI")
        return BasicAction.create_dict_from_list(repository_names,repository_desc)






