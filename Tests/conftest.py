import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome(executable_path="./Drivers/chromedriver")
        print("Launching chrome browser.........")
    elif browser=='firefox':
        driver = webdriver.Firefox(executable_path="./Drivers/geckodriver")
        print("Launching firefox browser.........")
    elif browser=='safari':
        driver=webdriver.Safari()
        print("Launching Safari browser.........")
    else:
        driver=webdriver.Chrome(executable_path="./Drivers/chromedriver")
        print("Launching chrome browser.........")
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


########### pytest HTML Report ################
# This is a hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'ENR Functional Regression Suite'
    config._metadata['Module Name'] = 'Test Automation'
    config._metadata['Tester'] = 'Dane Wilkerson'

# This is a hook for Delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Sample Meta Data", None)
    metadata.pop("Plugins", None)

#   # Code below is in progress
    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.set_window_size(1920, 1080)
    #     cls.driver.maximize_window()
    #     cls.driver.get(cls.url)
    #     cls.driver.implicitly_wait(10)
    #     WebDriverWait(cls.driver, 10).until(EC.visibility_of_element_located(Locators.PR_HEADER))

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()
    #     cls.driver.quit()