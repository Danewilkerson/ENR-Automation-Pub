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
        print("Test Pass: All Initial GET items receive a '200' repsonse")

    def test_0101_validate_page_header_data_logoimage_and_sealimage(self):
        t = BasePage(self.driver)
        t.assert_element_text(Locators.HEADER_TITLE, TestData.HEADER_TITLE_TEXT)
        t.assert_element_text(Locators.ELECTION_HEADER, TestData.ELECTION_NAME)
        t.assert_element_text(Locators.JURISDICTION_HEADER, TestData.JURISDICTION_NAME)
        t.assert_element_is_displayed(Locators.ENR_LOGO)
        t.assert_element_is_displayed(Locators.COUNTY_SEAL)
        print("Page Header Data/Text, Logo Image and Seal Image are displayed")


class Test_02_Search(EnrPublicApp):

    def test_0200_validate_search_textbox_placeholder_and_dimensions(self):
        s = BasePage(self.driver)
        s.assert_element_placeholder(Locators.SEARCH_TEXTBOX_PLACEHOLDER)
        s.assert_element_size(Locators.SEARCH_TEXTBOX, Locators.SEARCH_TEXTBOX_DIMENSIONS)
        print("Test Pass: Search Field Placeholder is displays and Textbox Dimensions are correct")

    def test_0201_search_results_candidates_title_validation(self):
        s = BasePage(self.driver)
        s.search(TestData.SEARCH_TERM_PARTIAL_NAME)
        s.assert_element_text(Locators.SEARCH_RESULT_CANDIDATE_TITLE, TestData.SEARCH_RESULTS_CANDIDATE_TITLE_TEXT)
        s.click(Locators.SEARCH_CANCEL)
        print("Test Pass: Candidate title is displayed in the search results")

    def test_0202_search_results_contest_Issue_title_validation(self):
        s = BasePage(self.driver)
        s.search(TestData.SEARCH_TERM_PARTIAL_NAME_2)
        s.assert_element_text(Locators.SEARCH_RESULTS_CONTEST_ISSUE_TITLE, TestData.SEARCH_RESULTS_CONTEST_ISSUE_TITLE_TEXT)
        s.click(Locators.SEARCH_CANCEL)
        print("Test Pass: Issue Title is displayed in the search results")

    def test_0203_search_partial_name(self):
        s = BasePage(self.driver)
        s.search(TestData.SEARCH_TERM_PARTIAL_NAME)
        s.assert_element_text(Locators.SEARCH_RESULT_PARTIAL_NAME, TestData.SEARCH_RESULT_PARTIAL_NAME)
        s.click(Locators.SEARCH_CANCEL)
        print("Test Pass: Able to search a partial name (min 3 characters")

    def test_0204_search_full_name(self):
        s = BasePage(self.driver)
        s.search(TestData.SEARCH_TERM_FULL_NAME)
        s.assert_element_text(Locators.SEARCH_RESULT_FULL_NAME, TestData.SEARCH_RESULT_FULL_NAME)
        s.click(Locators.SEARCH_RESULT_FULL_NAME)
        s.click(Locators.SEARCH_CANCEL)
        print("Test Pass: Able to search full name (min 3 characters")

class Test_03_PartiesFilter(EnrPublicApp):

    def test_0300_assert_all_parties_are_present_in_filter(self):
        pf = BasePage(self.driver)
        pf.assert_element_text(Locators.PARTIES_FILTER_ALLPARTIES, Locators.PARTIES_FILTERS_ALLPARTIES_TEXT)
        pf.assert_element_text(Locators.PARTIES_FILTER_DEMOCRATIC, Locators.PARTIES_FILTERS_DEMOCRATIC_TEXT)
        pf.assert_element_text(Locators.PARTIES_FILTER_REPUBLICAN, Locators.PARTIES_FILTERS_REPUBLICAN_TEXT)
        print("Test Pass: All parties are present in the parties filter")

    def test_0301_select_republican_from_parties_filter(self):
        pf = BasePage(self.driver)
        pf.click(Locators.PARTIES_FILTER_DROPDOWN)
        pf.click(Locators.PARTIES_FILTER_REPUBLICAN)
        print("Test Pass: Able to select 'Republican' party from the parties filter")

    def test_0302_select_democratic_from_parties_filter(self):
        pf = BasePage(self.driver)
        pf.click(Locators.PARTIES_FILTER_DROPDOWN)
        pf.click(Locators.PARTIES_FILTER_DEMOCRATIC)
        print("Test Pass: Able to select 'Democratic' party from the parties filter")

    def test_0303_select_allparties_from_parties_filter(self):
        pf = BasePage(self.driver)
        pf.click(Locators.PARTIES_FILTER_DROPDOWN)
        pf.click(Locators.PARTIES_FILTER_ALLPARTIES)
        print("Test Pass: Able to select 'All Parties' from the parties filter")


class Test_04_DownloadResults(EnrPublicApp):

    def test_0400_validate_download_results_button_text_and_dimensions(self):
        dl = BasePage(self.driver)
        dl.assert_element_text(Locators.DOWNLOAD_RESULTS_BUTTON, Locators.DOWNLOAD_RESULTS_BUTTON_TEXT)
        dl.assert_element_size(Locators.DOWNLOAD_RESULTS_BUTTON, Locators.DOWNLOAD_RESULTS_BUTTON_DIMENSIONS)
        print("Test Pass: Download button text is correct and dimensions of the button are correct")

    def test_0402_download_results_file(self):
        dl = BasePage(self.driver)
        dl.click(Locators.DOWNLOAD_RESULTS_BUTTON)
        time.sleep(3)
        dl.assert_GET_status(TestData.DOWNLOAD_RESULTS_FILE_URL, 200)
        print("Test Pass: Able to click and download the results file.  File url gets a 200 response")


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
        print("Test Pass: All elements in the 'Precinct Reporting Card' are displayed")

    def test_0501_precinct_reporting_table_header_validations(self):
        pr = BasePage(self.driver)
        pr.click(Locators.PR_DROPDOWN_ARROW)
        pr.assert_element_text(Locators.PR_TABLE_PRECINCT_HEADER, TestData.PR_TABLE_PRECINCT_HEADER_TEXT)
        pr.assert_element_text(Locators.PR_TABLE_TURNOUT_HEADER, TestData.PR_TABLE_TURNOUT_HEADER_TEXT)
        pr.click(Locators.PR_DROPDOWN_ARROW)
        print("Test Pass: Precinct Report table headers are displayed and correct")

    def test_0502_precinct_reporting_sort_turnout_table_header(self):
        pr = BasePage(self.driver)
        pr.click(Locators.PR_DROPDOWN_ARROW)
        pr.click(Locators.PR_TABLE_TURNOUT_HEADER)
        pr.click(Locators.PR_TABLE_TURNOUT_HEADER)
        pr.click(Locators.PR_DROPDOWN_ARROW)
        print("Test Pass: Able to sort the Precinct Reporting tables 'Voter Turnout' column")


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
        print("Test Pass: All elements in the 'Voter Turnout Card' are displayed")

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
        print("Test Pass: Voter Turnout table headers are displayed and correct")

    def test_0602_voter_turnout_table_click_party_to_view_on_heatmap(self):
        vt = BasePage(self.driver)
        vt.click(Locators.VT_DROPDOWN_ARROW)
        vt.click(Locators.VT_TABLE_REP)
        vt.click(Locators.VT_TABLE_DEM)
        vt.click(Locators.VT_DROPDOWN_ARROW)
        print("Test Pass: Able to click a Party to view its results on the Heat Map")

class Test_07_Democratic_Card(EnrPublicApp):
    
    def test_0700_democratic_card_visibility_validations(self):
        dc = BasePage(self.driver)
        dc.click(Locators.PARTIES_FILTER_DROPDOWN)
        dc.click(Locators.PARTIES_FILTER_DEMOCRATIC)
        dc.assert_element_is_displayed(Locators.DEM_CARD_HEADER)
        dc.assert_element_is_displayed(Locators.DEM_CARD_ICON)
        dc.assert_element_is_displayed(Locators.DEM_CARD_LEADER_NAME)
        dc.assert_element_is_displayed(Locators.DEM_CARD_LEADER_BARGRAPH)
        dc.assert_element_is_displayed(Locators.DEM_CARD_LEADER_RESULTS)
        dc.assert_element_is_displayed(Locators.DEM_CARD_EXPAND_FOR_MORE_CANDIDATES)
        dc.assert_element_is_displayed(Locators.DEM_CARD_FAVORITE_ICON)
        dc.assert_element_is_displayed(Locators.DEM_CARD_SHARE_ICON)
        dc.assert_element_fill_color(Locators.DEM_CARD_LEADER_BARGRAPH, TestData.DEM_BLUE_BARGRAPH_COLOR)
        print("Test Pass: All Democratic Card visual elements are displayed")

    def test_0701_democratic_card_main_leader_validations(self):
        dc = BasePage(self.driver)
        dc.assert_element_text(Locators.DEM_CARD_HEADER, TestData.DEM_CARD_HEADER_TEXT)
        dc.assert_element_text(Locators.DEM_CARD_SUBHEADER, TestData.DEM_CARD_SUBHEADER_TEXT)
        dc.assert_element_text(Locators.DEM_CARD_LEADER_NAME, TestData.DEM_CARD_LEADER_NAME_TEXT)
        dc.assert_element_text(Locators.DEM_CARD_LEADER_RESULTS, TestData.DEM_CARD_LEADER_RESULTS_TEXT)
        dc.assert_element_text(Locators.DEM_CARD_EXPAND_FOR_MORE_CANDIDATES, TestData.DEM_CARD_EXPAND_FOR_MORE_CANDIDATES_TEXT)
        print("Test Pass: All Democratic Leader data is displayed and correct")

    def test_0703_democratic_card_dropdown_second_place_validation(self):
        dc = BasePage(self.driver)
        dc.click(Locators.DEM_CARD_DROPDOWN_ARROW)
        dc.assert_element_text(Locators.DEM_CARD_DROPDOWN_SECOND_PLACE_NAME, TestData.DEM_CARD_DROPDOWN_SECOND_PLACE_NAME_TEXT)
        dc.assert_element_text(Locators.DEM_CARD_DROPDOWN_SECOND_PLACE_RESULTS, TestData.DEM_CARD_DROPDOWN_SECOND_PLACE_RESULTS_TEXT)
        dc.click(Locators.DEM_CARD_DROPDOWN_ARROW)
        print("Test Pass: Democratic 2nd place candidate data is correct")

    def test_0703_democratic_card_leader_has_highest_results(self):
        dc = BasePage(self.driver)
        dc.click(Locators.DEM_CARD_DROPDOWN_ARROW)
        dc.assert_contest_leader(Locators.DEM_CARD_LEADER_RESULTS, Locators.DEM_CARD_DROPDOWN_SECOND_PLACE_RESULTS)
        dc.click(Locators.DEM_CARD_DROPDOWN_ARROW)


class Test_08_Republican_Card(EnrPublicApp):
    
    def test_0800_republican_card_visibility_validations(self):
        dc = BasePage(self.driver)
        dc.click(Locators.PARTIES_FILTER_DROPDOWN)
        dc.click(Locators.PARTIES_FILTER_REPUBLICAN)
        dc.assert_element_is_displayed(Locators.REP_CARD_HEADER)
        dc.assert_element_is_displayed(Locators.REP_CARD_ICON)
        dc.assert_element_is_displayed(Locators.REP_CARD_LEADER_NAME)
        dc.assert_element_is_displayed(Locators.REP_CARD_LEADER_BARGRAPH)
        dc.assert_element_is_displayed(Locators.REP_CARD_LEADER_RESULTS)
        dc.assert_element_is_displayed(Locators.REP_CARD_EXPAND_FOR_MORE_CANDIDATES)
        dc.assert_element_is_displayed(Locators.REP_CARD_FAVORITE_ICON)
        dc.assert_element_is_displayed(Locators.REP_CARD_SHARE_ICON)
        dc.assert_element_fill_color(Locators.REP_CARD_LEADER_BARGRAPH, TestData.REP_RED_BARGRAPH_COLOR)
        print("Test Pass: All Republican Card visual elements are displayed")

    def test_0801_republican_card_main_leader_validations(self):
        dc = BasePage(self.driver)
        dc.assert_element_text(Locators.REP_CARD_HEADER, TestData.REP_CARD_HEADER_TEXT)
        dc.assert_element_text(Locators.REP_CARD_SUBHEADER, TestData.REP_CARD_SUBHEADER_TEXT)
        dc.assert_element_text(Locators.REP_CARD_LEADER_NAME, TestData.REP_CARD_LEADER_NAME_TEXT)
        dc.assert_element_text(Locators.REP_CARD_LEADER_RESULTS, TestData.REP_CARD_LEADER_RESULTS_TEXT)
        dc.assert_element_text(Locators.REP_CARD_EXPAND_FOR_MORE_CANDIDATES, TestData.REP_CARD_EXPAND_FOR_MORE_CANDIDATES_TEXT)
        print("Test Pass: All Republican Leader data is displayed and correct")

    def test_0803_republican_card_dropdown_second_place_validation(self):
        dc = BasePage(self.driver)
        dc.click(Locators.REP_CARD_DROPDOWN_ARROW)
        dc.assert_element_text(Locators.REP_CARD_DROPDOWN_SECOND_PLACE_NAME, TestData.REP_CARD_DROPDOWN_SECOND_PLACE_NAME_TEXT)
        dc.assert_element_text(Locators.REP_CARD_DROPDOWN_SECOND_PLACE_RESULTS, TestData.REP_CARD_DROPDOWN_SECOND_PLACE_RESULTS_TEXT)
        dc.click(Locators.REP_CARD_DROPDOWN_ARROW)
        print("Test Pass: Republican 2nd place candidate data is correct")

    def test_0803_drepublican_card_leader_has_highest_results(self):
        dc = BasePage(self.driver)
        dc.click(Locators.REP_CARD_DROPDOWN_ARROW)
        dc.assert_contest_leader(Locators.REP_CARD_LEADER_RESULTS, Locators.REP_CARD_DROPDOWN_SECOND_PLACE_RESULTS)
        dc.click(Locators.REP_CARD_DROPDOWN_ARROW)


class Test_10_WallBoard(EnrPublicApp):

    def test_0800_wallboard_validations(self):
        vt = BasePage(self.driver)
        vt.driver.get(TestData.WALLBOARD_BASE_URL)
        vt.click(Locators.WALLBOARD_MAXIMIZE_ICON)
        vt.assert_GET_status(TestData.WALLBOARD_LATEST_STATUSES_URL, 503) # 503 on weekends and after 7pm during weekdays for dev
        print("Test Pass: Wallboard is displayed and Latest Status URL GETS a 200")
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