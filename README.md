# rideCell
To verify user repositories

Automation Framework For Github Repository

Clone the framework at your local machine using:
git clone <GitHubProjectLink>

Open the project in pyCharm.

To run the Test Suite in Pycharm/cmd navigate to following path:
ridecell\ridCell_Framework_Selenium_Tests\rideCell_Framework_Selenium_TestCases\rideCell_Tests_GitHub_Repo

Now execute following command:
pytest -s -v --html="../../../rideCell_Selenium_Framework/rideCell_Framework_UI_Reports/Reports.html"

Test report will be generated at below location:
\ridecell\rideCell_Selenium_Framework\rideCell_Framework_UI_Reports with the name "Reports.html"

Failed Test cases screenshots will be saved at below location:
\ridecell\rideCell_Selenium_Framework\rideCell_Framework_UI_Screenshots 

Test logs will be generated at below location:
\ridecell\rideCell_Selenium_Framework\rideCell_Framework_UI_Logs
