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
