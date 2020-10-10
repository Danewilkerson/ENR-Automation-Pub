import sys, time, unittest
sys.path.append(".")
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Resources.test_data import TestData
from Resources.locators import Locators
from Pages.page_library import *


class EnrPublicApp(unittest.TestCase):
    url = TestData.BASE_URL

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(cls.url)
        cls.driver.implicitly_wait(10)
        WebDriverWait(cls.driver, 10).until(EC.visibility_of_element_located(Locators.PR_HEADER))

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


class Test_01_InitialPageLoad(EnrPublicApp):    

    def test_0100_validate_page_responses(self):
        t = BasePage(self.driver)
        assert self.driver.title == TestData.PAGE_TITLE
        t.assert_GET_status(TestData.BASE_URL,200)
        t.assert_GET_status(TestData.RESULTS_JSON_URL,200)
        t.assert_GET_status(TestData.MAP_TOPO_JSON_URL,200)
        t.assert_GET_status(TestData.BUILDING_SVG_URL,200)
        t.assert_GET_status(TestData.CAPITAL_SVG_URL,200)
        t.assert_GET_status(TestData.ISSUE_SVG_URL,200)

    def test_0101_validate_page_assertions(self):
        t = BasePage(self.driver)
        t.assert_element_text(Locators.HEADER_TITLE, TestData.HEADER_TITLE_TEXT)
        t.assert_element_text(Locators.ELECTION_HEADER, TestData.ELECTION_NAME)
        t.assert_element_text(Locators.JURISDICTION_HEADER, TestData.JURISDICTION_NAME)
        t.assert_element_is_displayed(Locators.ENR_LOGO)
        t.assert_element_is_displayed(Locators.COUNTY_SEAL)


class Test_02_Search(EnrPublicApp):

    def test_0200_validate_search_textbox_placeholder_and_dimensions(self):
        s = BasePage(self.driver)
        s.assert_element_placeholder(Locators.SEARCH_TEXTBOX_PLACEHOLDER)
        s.assert_element_size(Locators.SEARCH_TEXTBOX, Locators.SEARCH_TEXTBOX_DIMENSIONS)

    def test_0201_search_results_candidates_title_validation(self):
        s = BasePage(self.driver)
        s.search(TestData.SEARCH_TERM_PARTIAL_NAME)
        s.assert_element_text(Locators.SEARCH_RESULT_CANDIDATE_TITLE, TestData.SEARCH_RESULTS_CANDIDATE_TITLE_TEXT)
        s.click(Locators.SEARCH_CANCEL)

    def test_0202_search_results_contest_Issue_title_validation(self):
        s = BasePage(self.driver)
        s.search(TestData.SEARCH_TERM_PARTIAL_NAME_2)
        s.assert_element_text(Locators.SEARCH_RESULTS_CONTEST_ISSUE_TITLE, TestData.SEARCH_RESULTS_CONTEST_ISSUE_TITLE_TEXT)
        s.click(Locators.SEARCH_CANCEL)

    def test_0203_search_partial_name(self):
        s = BasePage(self.driver)
        s.search(TestData.SEARCH_TERM_PARTIAL_NAME)
        s.assert_element_text(Locators.SEARCH_RESULT_PARTIAL_NAME, TestData.SEARCH_RESULT_PARTIAL_NAME)
        s.click(Locators.SEARCH_CANCEL)

    def test_0204_search_full_name(self):
        s = BasePage(self.driver)
        s.search(TestData.SEARCH_TERM_FULL_NAME)
        s.click(Locators.SEARCH_RESULT_FULL_NAME)
        s.click(Locators.SEARCH_CANCEL)

class Test_03_PartiesFilter(EnrPublicApp):

    def test_0300_assert_all_parties_are_present_in_filter(self):
        pf = BasePage(self.driver)
        pf.assert_element_text(Locators.PARTIES_FILTER_ALLPARTIES, Locators.PARTIES_FILTERS_ALLPARTIES_TEXT)
        pf.assert_element_text(Locators.PARTIES_FILTER_DEMOCRATIC, Locators.PARTIES_FILTERS_DEMOCRATIC_TEXT)
        pf.assert_element_text(Locators.PARTIES_FILTER_REPUBLICAN, Locators.PARTIES_FILTERS_REPUBLICAN_TEXT)

    def test_0301_select_republican_from_parties_filter(self):
        pf = BasePage(self.driver)
        pf.click(Locators.PARTIES_FILTER_DROPDOWN)
        pf.click(Locators.PARTIES_FILTER_REPUBLICAN)

    def test_0302_select_democratic_from_parties_filter(self):
        pf = BasePage(self.driver)
        pf.click(Locators.PARTIES_FILTER_DROPDOWN)
        pf.click(Locators.PARTIES_FILTER_DEMOCRATIC)

    def test_0303_select_allparties_from_parties_filter(self):
        pf = BasePage(self.driver)
        pf.click(Locators.PARTIES_FILTER_DROPDOWN)
        pf.click(Locators.PARTIES_FILTER_ALLPARTIES)


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


class Test_05_PrecinctReporting(EnrPublicApp):

    def test_0500_precinct_reporting_card_validations(self):
        pr = BasePage(self.driver)
        pr.assert_element_is_displayed(Locators.PR_ICON)
        pr.assert_element_is_displayed(Locators.PR_HEADER)
        pr.assert_element_is_displayed(Locators.PR_SUBHEADER)
        pr.assert_element_is_displayed(Locators.PR_MAXIMIZE_MAP)
        pr.assert_element_is_displayed(Locators.PR_PIE_CHART_REPORTED)
        pr.assert_element_is_displayed(Locators.PR_TOTAL)
        pr.assert_element_is_displayed(Locators.PR_REPORTED)
        pr.assert_element_is_displayed(Locators.PR_FAVORITE_ICON)
        pr.assert_element_is_displayed(Locators.PR_SHARE_ICON)
        pr.assert_element_is_displayed(Locators.PR_DROPDOWN_ARROW)

    def test_0501_precinct_reporting_table_header_validations(self):
        pr = BasePage(self.driver)
        pr.click(Locators.PR_DROPDOWN_ARROW)
        pr.assert_element_text(Locators.PR_TABLE_PRECINCT_HEADER, TestData.PR_TABLE_PRECINCT_HEADER_TEXT)
        pr.assert_element_text(Locators.PR_TABLE_TURNOUT_HEADER, TestData.PR_TABLE_TURNOUT_HEADER_TEXT)
        pr.click(Locators.PR_DROPDOWN_ARROW)

    def test_0502_precinct_reporting_sort_turnout_table_header(self):
        pr = BasePage(self.driver)
        pr.click(Locators.PR_DROPDOWN_ARROW)
        pr.click(Locators.PR_TABLE_TURNOUT_HEADER)
        pr.click(Locators.PR_TABLE_TURNOUT_HEADER)
        pr.click(Locators.PR_DROPDOWN_ARROW)


class Test_06_VoterTurnout(EnrPublicApp):

    def test_0600_voter_turnout_card_validations(self):
        vt = BasePage(self.driver)
        vt.assert_element_is_displayed(Locators.VT_ICON)
        vt.assert_element_is_displayed(Locators.VT_HEADER)
        vt.assert_element_is_displayed(Locators.VT_SUBHEADER)
        vt.assert_element_is_displayed(Locators.VT_PIE_CHART_REPORTED)
        vt.assert_element_is_displayed(Locators.VT_TOTAL)
        vt.assert_element_is_displayed(Locators.VT_REPORTED)
        vt.assert_element_is_displayed(Locators.VT_FAVORITE_ICON)
        vt.assert_element_is_displayed(Locators.VT_SHARE_ICON)
        vt.assert_element_is_displayed(Locators.VT_DROPDOWN_ARROW)

    def test_0601_voter_turnout_table_validations(self):
        vt = BasePage(self.driver)
        vt.click(Locators.VT_DROPDOWN_ARROW)
        vt.assert_element_text(Locators.VT_TABLE_PARTY_HEADER, TestData.VT_TABLE_PARTY_HEADER_TEXT)
        vt.assert_element_text(Locators.VT_TABLE_TURNOUT_HEADER, TestData.VT_TABLE_TURNOUT_HEADER_TEXT)
        vt.assert_element_text(Locators.VT_TABLE_DEM_TURNOUT, TestData.VT_TABLE_DEM_TURNOUT_TEXT)
        vt.assert_element_text(Locators.VT_TABLE_REP_TURNOUT, TestData.VT_TABLE_REP_TURNOUT_TEXT)
        vt.assert_element_text(Locators.VT_TABLE_DEM, TestData.VT_TABLE_DEM_TEXT)
        vt.assert_element_text(Locators.VT_TABLE_REP, TestData.VT_TABLE_REP_TEXT)
        vt.assert_element_text(Locators.VT_GUIDE, TestData.VT_GUIDE_TEXT)
        vt.click(Locators.VT_DROPDOWN_ARROW)

    def test_0602_voter_turnout_table_click_party_to_view_on_heatmap(self):
        vt = BasePage(self.driver)
        vt.click(Locators.VT_DROPDOWN_ARROW)
        vt.click(Locators.VT_TABLE_REP)
        vt.click(Locators.VT_TABLE_DEM)
        vt.click(Locators.VT_DROPDOWN_ARROW)

class Test_07_Democratic_Card(EnrPublicApp):
    
    def test_0700_democratic_card_visibility_validations(self):
        dc = BasePage(self.driver)
        dc.assert_element_is_displayed(Locators.DEM_CARD_HEADER)
        dc.assert_element_is_displayed(Locators.DEM_CARD_ICON)
        dc.assert_element_is_displayed(Locators.DEM_CARD_LEADER_NAME)
        dc.assert_element_is_displayed(Locators.DEM_CARD_LEADER_BARGRAPH)
        dc.assert_element_is_displayed(Locators.DEM_CARD_LEADER_RESULTS)
        dc.assert_element_is_displayed(Locators.DEM_CARD_EXPAND_FOR_MORE_CANDIDATES)
        dc.assert_element_is_displayed(Locators.DEM_CARD_FAVORITE_ICON)
        dc.assert_element_is_displayed(Locators.DEM_CARD_SHARE_ICON)
        dc.assert_element_fill_color(Locators.DEM_CARD_LEADER_BARGRAPH, TestData.DEM_BLUE_BARGRAPH_COLOR)

    def test_0701_democratic_card_main_leader_validations(self):
        dc = BasePage(self.driver)
        dc.assert_element_text(Locators.DEM_CARD_HEADER, TestData.DEM_CARD_HEADER_TEXT)
        dc.assert_element_text(Locators.DEM_CARD_SUBHEADER, TestData.DEM_CARD_SUBHEADER_TEXT)
        dc.assert_element_text(Locators.DEM_CARD_LEADER_NAME, TestData.DEM_CARD_LEADER_NAME_TEXT)
        dc.assert_element_text(Locators.DEM_CARD_LEADER_RESULTS, TestData.DEM_CARD_LEADER_RESULTS_TEXT)
        dc.assert_element_text(Locators.DEM_CARD_EXPAND_FOR_MORE_CANDIDATES, TestData.DEM_CARD_EXPAND_FOR_MORE_CANDIDATES_TEXT)

    def test_0703_democratic_card_dropdown_second_place_validation(self):
        dc = BasePage(self.driver)
        dc.click(Locators.DEM_CARD_DROPDOWN_ARROW)
        dc.assert_element_text(Locators.DEM_CARD_DROPDOWN_SECOND_PLACE_NAME, TestData.DEM_CARD_DROPDOWN_SECOND_PLACE_NAME_TEXT)
        dc.assert_element_text(Locators.DEM_CARD_DROPDOWN_SECOND_PLACE_RESULTS, TestData.DEM_CARD_DROPDOWN_SECOND_PLACE_RESULTS_TEXT)
        dc.click(Locators.DEM_CARD_DROPDOWN_ARROW)

    def test_0703_democratic_card_leader_has_highest_results(self):
        dc = BasePage(self.driver)
        dc.click(Locators.DEM_CARD_DROPDOWN_ARROW)
        candidate1 = dc.return_element_text(Locators.DEM_CARD_LEADER_RESULTS)
        candidate2 = dc.return_element_text(Locators.DEM_CARD_DROPDOWN_SECOND_PLACE_RESULTS)
        assert candidate1 > candidate2
        dc.click(Locators.DEM_CARD_DROPDOWN_ARROW)


class Test_10_WallBoard(EnrPublicApp):

    def test_0800_wallboard_validations(self):
        vt = BasePage(self.driver)
        vt.driver.get(TestData.WALLBOARD_BASE_URL)
        vt.click(Locators.WALLBOARD_MAXIMIZE_ICON)
        vt.assert_GET_status(TestData.WALLBOARD_LATEST_STATUSES_URL, 503) # 503 on weekend/200 on weekdays
        time.sleep(3)

if __name__ == '__main__':
    unittest.main(
    testRunner=HTMLTestRunner(
        combine_reports=True,
        add_timestamp=False,
        open_in_browser=True,
        report_name="EnrPub_Test_Report",
        template='reports/report_template.html'
    )
)