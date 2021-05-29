import sys, time, unittest, allure
sys.path.append(".")
from utilities.customLogger import LogGen
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Resources.test_data import TestData
from Resources.locators import Locators
from Pages.page_library import *


@allure.severity(allure.severity_level.NORMAL)
class Test_01_Full_Functional_Regression:
    url = TestData.BASE_URL
    logger=LogGen.loggen()    
    
    @allure.description("This Regression Suite will test UI and Functionality of ENR Public App.  See the log for details")
    @allure.severity(allure.severity_level.NORMAL)
    def test_0100_enr_functional_regression_test(self, setup):
        driver = setup
        driver.get(self.url)
        driver.set_window_size(1920, 1080)

        t = BasePage(driver)
        self.logger.info("************* Starting ENR Regression Tests *************")
        self.logger.info("************* Starting: test_0100_validate_page_responses")
        assert driver.title == TestData.PAGE_TITLE
        t.assert_GET_status(TestData.BASE_URL,200)
        t.assert_GET_status(TestData.RESULTS_JSON_URL,200)
        t.assert_GET_status(TestData.MAP_TOPO_JSON_URL,200)
        t.assert_GET_status(TestData.BUILDING_SVG_URL,200)
        t.assert_GET_status(TestData.CAPITAL_SVG_URL,200)
        t.assert_GET_status(TestData.ISSUE_SVG_URL,200)
        self.logger.info("Test Pass: All Initial GET items receive a '200' response")

        self.logger.info("************* Starting: test_0101_validate_page_header_data_logoimage_and_sealimage")
        t.assert_element_text(Locators.HEADER_TITLE, TestData.HEADER_TITLE_TEXT)
        t.assert_element_text(Locators.ELECTION_HEADER, TestData.ELECTION_NAME)
        t.assert_element_text(Locators.JURISDICTION_HEADER, TestData.JURISDICTION_NAME)
        t.assert_element_is_displayed(Locators.ENR_LOGO)
        t.assert_element_is_displayed(Locators.COUNTY_SEAL)
        self.logger.info("Test Pass: Page Header Data/Text, Logo Image and Seal Image are displayed")
        
        self.logger.info("************* Starting: test_0200_validate_search_textbox_placeholder_and_dimensions")
        s = BasePage(driver)
        s.assert_element_placeholder(Locators.SEARCH_TEXTBOX_PLACEHOLDER)
        s.assert_element_size(Locators.SEARCH_TEXTBOX, Locators.SEARCH_TEXTBOX_DIMENSIONS)
        self.logger.info("Test Pass: Search Field Placeholder is displayed and Textbox Dimensions are correct")
        self.logger.info("************* Starting: test_0201_search_results_candidates_title_validation")
        s.search(TestData.SEARCH_TERM_PARTIAL_NAME)
        s.assert_element_text(Locators.SEARCH_RESULT_CANDIDATE_TITLE, TestData.SEARCH_RESULTS_CANDIDATE_TITLE_TEXT)
        s.click(Locators.SEARCH_CANCEL)
        self.logger.info("Test Pass: Candidate title is displayed in the search results list")
        self.logger.info("************* Starting: test_0202_search_results_contest_Issue_title_validation")
        s.search(TestData.SEARCH_TERM_PARTIAL_NAME_2)
        s.assert_element_text(Locators.SEARCH_RESULTS_CONTEST_ISSUE_TITLE, TestData.SEARCH_RESULTS_CONTEST_ISSUE_TITLE_TEXT)
        s.click(Locators.SEARCH_CANCEL)
        self.logger.info("Test Pass: Issue Title is displayed in the search results list")
        self.logger.info("************* Starting: test_0203_search_partial_name")
        s.search(TestData.SEARCH_TERM_PARTIAL_NAME)
        s.assert_element_text(Locators.SEARCH_RESULT_PARTIAL_NAME, TestData.SEARCH_RESULT_PARTIAL_NAME)
        s.click(Locators.SEARCH_CANCEL)
        self.logger.info("Test Pass: Able to search a partial name (min 3 characters)")
        self.logger.info("************* Starting: test_0204_search_full_name")
        s.search(TestData.SEARCH_TERM_FULL_NAME)
        s.assert_element_text(Locators.SEARCH_RESULT_FULL_NAME, TestData.SEARCH_RESULT_FULL_NAME)
        s.click(Locators.SEARCH_RESULT_FULL_NAME)
        s.click(Locators.SEARCH_CANCEL)
        self.logger.info("Test Pass: Able to search full name (min 3 characters)")

        self.logger.info("************* Starting: test_0300_assert_all_parties_are_present_in_filter")
        pf = BasePage(driver)
        pf.assert_element_text(Locators.PARTIES_FILTER_ALLPARTIES, Locators.PARTIES_FILTERS_ALLPARTIES_TEXT)
        pf.assert_element_text(Locators.PARTIES_FILTER_DEMOCRATIC, Locators.PARTIES_FILTERS_DEMOCRATIC_TEXT)
        pf.assert_element_text(Locators.PARTIES_FILTER_REPUBLICAN, Locators.PARTIES_FILTERS_REPUBLICAN_TEXT)
        self.logger.info("Test Pass: All parties in the election are in the parties filter list")
        self.logger.info("************* Starting: test_0301_select_republican_from_parties_filter")
        pf.click(Locators.PARTIES_FILTER_DROPDOWN)
        pf.click(Locators.PARTIES_FILTER_REPUBLICAN)
        self.logger.info("Test Pass: Able to select 'Republican' party from the parties filter list")
        self.logger.info("************* Starting: test_0302_select_democratic_from_parties_filter")
        pf.click(Locators.PARTIES_FILTER_DROPDOWN)
        pf.click(Locators.PARTIES_FILTER_DEMOCRATIC)
        self.logger.info("Test Pass: Able to select 'Democratic' party from the parties filter list")
        self.logger.info("************* Starting: test_0303_select_allparties_from_parties_filter")
        pf.click(Locators.PARTIES_FILTER_DROPDOWN)
        pf.click(Locators.PARTIES_FILTER_ALLPARTIES)
        self.logger.info("Test Pass: Able to select 'All Parties' from the parties filter list")

        self.logger.info("************* Starting: test_0400_precinct_reporting_card_validations")
        pr = BasePage(driver)
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
        self.logger.info("Test Pass: All elements in the 'Precinct Reporting Card' are displayed")
        self.logger.info("************* Starting: test_0401_precinct_reporting_table_header_validations")
        pr.click(Locators.PR_DROPDOWN_ARROW)
        pr.assert_element_text(Locators.PR_TABLE_PRECINCT_HEADER, TestData.PR_TABLE_PRECINCT_HEADER_TEXT)
        pr.assert_element_text(Locators.PR_TABLE_TURNOUT_HEADER, TestData.PR_TABLE_TURNOUT_HEADER_TEXT)
        pr.click(Locators.PR_DROPDOWN_ARROW)
        self.logger.info("Test Pass: Precinct Report table headers are displayed and correct")
        self.logger.info("************* Starting: test_0402_precinct_reporting_sort_turnout_table_header")
        pr.click(Locators.PR_DROPDOWN_ARROW)
        pr.click(Locators.PR_TABLE_TURNOUT_HEADER)
        pr.click(Locators.PR_TABLE_TURNOUT_HEADER)
        pr.click(Locators.PR_DROPDOWN_ARROW)
        self.logger.info("Test Pass: Able to sort the Precinct Reporting tables 'Voter Turnout' column")

        self.logger.info("************* Starting: test_0500_voter_turnout_card_validations")
        vt = BasePage(driver)
        vt.assert_element_is_displayed(Locators.VT_ICON)
        vt.assert_element_is_displayed(Locators.VT_HEADER)
        vt.assert_element_is_displayed(Locators.VT_SUBHEADER)
        vt.assert_element_is_displayed(Locators.VT_PIE_CHART_REPORTED)
        vt.assert_element_is_displayed(Locators.VT_TOTAL)
        vt.assert_element_is_displayed(Locators.VT_REPORTED)
        vt.assert_element_is_displayed(Locators.VT_FAVORITE_ICON)
        vt.assert_element_is_displayed(Locators.VT_SHARE_ICON)
        vt.assert_element_is_displayed(Locators.VT_DROPDOWN_ARROW)
        self.logger.info("Test Pass: All elements in the 'Voter Turnout Card' are displayed")
        self.logger.info("************* Starting: test_0501_voter_turnout_table_validations")
        vt.click(Locators.VT_DROPDOWN_ARROW)
        vt.assert_element_text(Locators.VT_TABLE_PARTY_HEADER, TestData.VT_TABLE_PARTY_HEADER_TEXT)
        vt.assert_element_text(Locators.VT_TABLE_TURNOUT_HEADER, TestData.VT_TABLE_TURNOUT_HEADER_TEXT)
        vt.assert_element_text(Locators.VT_TABLE_DEM_TURNOUT, TestData.VT_TABLE_DEM_TURNOUT_TEXT)
        vt.assert_element_text(Locators.VT_TABLE_REP_TURNOUT, TestData.VT_TABLE_REP_TURNOUT_TEXT)
        vt.assert_element_text(Locators.VT_TABLE_DEM, TestData.VT_TABLE_DEM_TEXT)
        vt.assert_element_text(Locators.VT_TABLE_REP, TestData.VT_TABLE_REP_TEXT)
        vt.assert_element_text(Locators.VT_GUIDE, TestData.VT_GUIDE_TEXT)
        vt.click(Locators.VT_DROPDOWN_ARROW)
        self.logger.info("Test Pass: Voter Turnout table headers are displayed and correct")
        self.logger.info("************* Starting: test_0502_voter_turnout_table_click_party_to_view_on_heatmap")
        vt.click(Locators.VT_DROPDOWN_ARROW)
        vt.click(Locators.VT_TABLE_REP)
        vt.click(Locators.VT_TABLE_DEM)
        vt.click(Locators.VT_DROPDOWN_ARROW)
        self.logger.info("Test Pass: Able to click a Party to view its results on the Heat Map")

        self.logger.info("************* Starting: test_0600_democratic_card_visibility_validations")
        dc = BasePage(driver)
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
        self.logger.info("Test Pass: All Democratic Card visual elements are displayed")
        self.logger.info("************* Starting: test_0601_democratic_card_main_leader_validations")
        dc.assert_element_text(Locators.DEM_CARD_HEADER, TestData.DEM_CARD_HEADER_TEXT)
        dc.assert_element_text(Locators.DEM_CARD_SUBHEADER, TestData.DEM_CARD_SUBHEADER_TEXT)
        dc.assert_element_text(Locators.DEM_CARD_LEADER_NAME, TestData.DEM_CARD_LEADER_NAME_TEXT)
        dc.assert_element_text(Locators.DEM_CARD_LEADER_RESULTS, TestData.DEM_CARD_LEADER_RESULTS_TEXT)
        dc.assert_element_text(Locators.DEM_CARD_EXPAND_FOR_MORE_CANDIDATES, TestData.DEM_CARD_EXPAND_FOR_MORE_CANDIDATES_TEXT)
        self.logger.info("Test Pass: All Democratic Leader data is displayed and correct")
        self.logger.info("************* Starting: test_0602_democratic_card_dropdown_second_place_validation")
        dc.click(Locators.DEM_CARD_DROPDOWN_ARROW)
        dc.assert_element_text(Locators.DEM_CARD_DROPDOWN_SECOND_PLACE_NAME, TestData.DEM_CARD_DROPDOWN_SECOND_PLACE_NAME_TEXT)
        dc.assert_element_text(Locators.DEM_CARD_DROPDOWN_SECOND_PLACE_RESULTS, TestData.DEM_CARD_DROPDOWN_SECOND_PLACE_RESULTS_TEXT)
        dc.click(Locators.DEM_CARD_DROPDOWN_ARROW)
        self.logger.info("Test Pass: Democratic 2nd place candidate data is correct")
        self.logger.info("************* Starting: test_0603_democratic_card_leader_has_highest_results")
        dc.click(Locators.DEM_CARD_DROPDOWN_ARROW)
        dc.assert_contest_leader(Locators.DEM_CARD_LEADER_RESULTS, Locators.DEM_CARD_DROPDOWN_SECOND_PLACE_RESULTS)
        dc.click(Locators.DEM_CARD_DROPDOWN_ARROW)

        self.logger.info("************* Starting: test_0700_republican_card_visibility_validations")
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
        self.logger.info("Test Pass: All Republican Card visual elements are displayed")
        self.logger.info("************* Starting: test_0701_republican_card_main_leader_validations")
        dc.assert_element_text(Locators.REP_CARD_HEADER, TestData.REP_CARD_HEADER_TEXT)
        dc.assert_element_text(Locators.REP_CARD_SUBHEADER, TestData.REP_CARD_SUBHEADER_TEXT)
        dc.assert_element_text(Locators.REP_CARD_LEADER_NAME, TestData.REP_CARD_LEADER_NAME_TEXT)
        dc.assert_element_text(Locators.REP_CARD_LEADER_RESULTS, TestData.REP_CARD_LEADER_RESULTS_TEXT)
        dc.assert_element_text(Locators.REP_CARD_EXPAND_FOR_MORE_CANDIDATES, TestData.REP_CARD_EXPAND_FOR_MORE_CANDIDATES_TEXT)
        self.logger.info("Test Pass: All Republican Leader data is displayed and correct")
        self.logger.info("************* Starting: test_0702_republican_card_dropdown_second_place_validation")
        dc.click(Locators.REP_CARD_DROPDOWN_ARROW)
        dc.assert_element_text(Locators.REP_CARD_DROPDOWN_SECOND_PLACE_NAME, TestData.REP_CARD_DROPDOWN_SECOND_PLACE_NAME_TEXT)
        dc.assert_element_text(Locators.REP_CARD_DROPDOWN_SECOND_PLACE_RESULTS, TestData.REP_CARD_DROPDOWN_SECOND_PLACE_RESULTS_TEXT)
        dc.click(Locators.REP_CARD_DROPDOWN_ARROW)
        self.logger.info("Test Pass: Republican 2nd place candidate data is correct")
        self.logger.info("************* Starting: test_0703_republican_card_leader_has_highest_results")
        dc.click(Locators.REP_CARD_DROPDOWN_ARROW)
        dc.assert_contest_leader(Locators.REP_CARD_LEADER_RESULTS, Locators.REP_CARD_DROPDOWN_SECOND_PLACE_RESULTS)
        dc.click(Locators.REP_CARD_DROPDOWN_ARROW)
        self.logger.info("Test Pass: Republican Leader has highest results")

        self.logger.info("************* Starting: test_0800_validate_download_results_button_text_and_dimensions")
        dl = BasePage(driver)
        dl.assert_element_text(Locators.DOWNLOAD_RESULTS_BUTTON, Locators.DOWNLOAD_RESULTS_BUTTON_TEXT)
        dl.assert_element_size(Locators.DOWNLOAD_RESULTS_BUTTON, Locators.DOWNLOAD_RESULTS_BUTTON_DIMENSIONS)
        self.logger.info("Test Pass: Download button text is correct and dimensions of the button are correct")
        self.logger.info("************* Starting: test_0801_download_results_file")
        dl.click(Locators.DOWNLOAD_RESULTS_BUTTON)
        time.sleep(3)
        dl.assert_GET_status(TestData.DOWNLOAD_RESULTS_FILE_URL, 200)
        self.logger.info("Test Pass: Able to click and download the results file.  File url gets a 200 response")

        self.logger.info("************* Starting: test_0900_wallboard_validations")
        wb = BasePage(driver)
        wb.driver.get(TestData.WALLBOARD_BASE_URL)
        wb.click(Locators.WALLBOARD_MAXIMIZE_ICON)
        # wb.assert_GET_status(TestData.WALLBOARD_LATEST_STATUSES_URL, 503) # 503 on weekends and after 7pm during weekdays for dev
        self.logger.info("Test Pass: Wallboard is displayed and Latest Status URL GETS a 200")
        time.sleep(3)
        self.logger.info("************* Completed ENR Regression Tests *************")


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