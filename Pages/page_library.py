from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Resources.test_data import TestData
from Resources.locators import Locators
import requests, unittest, time, os


class BasePage():

    def __init__(self, driver):
        self.driver=driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
        time.sleep(.5)

    def print_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).get_attribute("textContent")
        print("Element text = " + element)

    def assert_element_text(self, by_locator, element_text):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        assert element.get_attribute("textContent") == element_text

    def assert_element_source(self, by_locator, element_source):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert element.get_attribute("src") == element_source
        
    def assert_element_placeholder(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert element.get_attribute("placeholder") == "Search…"

    def assert_element_is_displayed(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).is_displayed()

    def assert_element_size(self, by_locator, element_size):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).size
        assert element == element_size

    def assert_GET_status(self, request_url, expected_GET_status_code):
        r = requests.get(request_url)
        assert r.status_code == expected_GET_status_code
        print(f"{request_url} recieved expected GET status '{expected_GET_status_code}'")

    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        
    def wait_for_page_to_load(self):
        page = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.PR_HEADER))

class Search(BasePage):

    def __init__(self, driver):
        self.driver=driver

    def search(self, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.SEARCH_TEXTBOX_PLACEHOLDER)).send_keys(text)