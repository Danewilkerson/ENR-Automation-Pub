from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Resources.test_data import TestData
from Resources.locators import Locators
from utilities.customLogger import LogGen
import requests, unittest, time, os, allure


class BasePage():
    logger=LogGen.loggen()

    def __init__(self, driver):
        self.driver=driver

    @allure.step("Click")
    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
        time.sleep(.5)

    @allure.step("Returning element text")
    def return_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).get_attribute("textContent")
        return element

    @allure.step("Printing element text")
    def print_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).get_attribute("textContent")
        self.logger.info("Printed element text: " + element)

    @allure.step("Asserting element text")
    def assert_element_text(self, by_locator, element_text):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        assert element.get_attribute("textContent") == element_text
        self.logger.info("Validation | Element text: " + element_text)

    @allure.step("Asserting element source")
    def assert_element_source(self, by_locator, element_source):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert element.get_attribute("src") == element_source
        self.logger.info("Validation | Element source: " + element_source)
        
    @allure.step("Asserting search box placeholder")
    def assert_element_placeholder(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert element.get_attribute("placeholder") == "Search…"
        self.logger.info('Validation | Search placeholder is visible and text is: "Search…"')

    @allure.step("Asserting element fill color")
    def assert_element_fill_color(self, by_locator, color):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert element.get_attribute("fill") == color

    @allure.step("Asserting element displays")
    def assert_element_is_displayed(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).is_displayed()

    @allure.step("Asserting element size")
    def assert_element_size(self, by_locator, element_size):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).size
        assert element == element_size
        self.logger.info("Validation | Elements size is: " + str(element))

    @allure.step("Asserting Get status")
    def assert_GET_status(self, request_url, expected_GET_status_code):
        r = requests.get(request_url)
        assert r.status_code == expected_GET_status_code
        self.logger.info(f"Validation | {request_url} recieved expected GET status '{expected_GET_status_code}'")

    @allure.step("Entering text in field")
    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        self.logger.info("Entered text: " + text)
        
    def wait_for_page_to_load(self):
        page = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.PR_HEADER))
        self.logger.info("ENR Public Page has fully loaded")

    @allure.step("Searching")
    def search(self, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.SEARCH_TEXTBOX_PLACEHOLDER)).send_keys(text)
        self.logger.info("Entered " + text + " into the searchfield")

    @allure.step("Asserting contest leaders")
    def assert_contest_leader(self, results1, results2):
        candidate1 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(results1)).get_attribute("textContent")
        candidate2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(results2)).get_attribute("textContent")
        assert candidate1 > candidate2
        self.logger.info(f"Test Pass: Leader has a higher score({candidate1}) than 2nd Place({candidate2})")