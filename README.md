# Election Night Results

## 'ENR' public app automation testing

**Technology Used:** 
- Python
- Unittest(Python Module)
- Selenium(Webdriver)

**Framework Used:** 
- Page Object Model

**Features:** 
- This project will help to test the ENR public application using automation to reduce the manual time.
- Full Regression with the click of a button
- Reducing testing time by up to 90%!

## Run Tests

**Run Tests**

    pytest filename.py

**Run Single Test with Reporting**

    pytest filename.py --html=./reports/report.html --html-report=./reports/dashboard.html -rA

**Run Entire Test Suite with Reporting**

    pytest --html=./reports/report.html --html-report=./reports/dashboard.html -rA

## Code Examples

**Page Library**

    def assert_element_size(self, by_locator, element_size):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).size
        assert element == element_size

    def assert_GET_status(self, request_url, expected_GET_status_code):
        r = requests.get(request_url)
        assert r.status_code == expected_GET_status_code

**Test File**

    class Test_04_DownloadResults(EnrPublicApp):

    def test_0400_validate_download_results_button_text_and_dimensions(self):
        dl = BasePage(self.driver)
        dl.assert_element_text(Locators.DOWNLOAD_RESULTS_BUTTON, Locators.DOWNLOAD_RESULTS_BUTTON_TEXT)
        dl.assert_element_size(Locators.DOWNLOAD_RESULTS_BUTTON, Locators.DOWNLOAD_RESULTS_BUTTON_DIMENSIONS)

    def test_0402_download_results_file(self):
        dl = BasePage(self.driver)
        dl.click(Locators.DOWNLOAD_RESULTS_BUTTON)
        time.sleep(3)
        dl.assert_GET_status(TestData.DOWNLOAD_RESULTS_FILE_URL, 200)

**Installation:**
1. [Install python](https://docs.python.org/3/using/index.html)
2. [Install Selenium](https://selenium-python.readthedocs.io/installation.html)

**Testing:**
* Python comes with testing framework Unittest. [Unittest Documentation](https://docs.python.org/3/library/unittest.html)
* How to write and run tests [Running & Writing Tests](https://devguide.python.org/runtests/)

## Current test coverage
**Validate Initial Page Responses:**
* All Initial GET items receive a '200' response
* Page Header Data/Text, Logo Image and Seal Image are displayed

**Searching:**
* Search Field Placeholder is displayed and Textbox Dimensions are correct
* Candidate title is displayed in the search results list
* Issue Title is displayed in the search results list
* Able to search a partial name (min 3 characters)
* Able to search full name (min 3 characters)

**Parties Filter:**
* All parties in the election are in the parties filter list
* Able to select 'Republican' party from the parties filter list
* Able to select 'Democratic' party from the parties filter list
* Able to select 'All Parties' from the parties filter list

**Download Results:**
* Download button text is correct and dimensions of the button are correct
* Able to click and download the results file.  File url gets a 200 response

**Precint Reporting Card:**
* All elements in the 'Precinct Reporting Card' are displayed
* Precinct Report table headers are displayed and correct
* Able to sort the Precinct Reporting tables 'Voter Turnout' column

**Voter Turnout Card:**
* All elements in the 'Voter Turnout Card' are displayed
* Voter Turnout table headers are displayed and correct
* Able to click a Party to view its results on the Heat Map

**Democratic Card:**
* All Democratic Card visual elements are displayed
* All Democratic Leader data is displayed and correct
* Democratic 2nd place candidate data is correct
* Democratic Leaders has higher result than 2nd place(Descending Order)

**Republican Card:**
* All Republican Card visual elements are displayed
* All Republican Leader data is displayed and correct
* Republican 2nd place candidate data is correct
* Republican Leaders has higher result than 2nd place(Descending Order)

**Issues Card:**
* In process of writing tests

**WallBoard:**
* Wallboard is displayed and Latest Status URL GETS a 200
* In proces of writing more tests...