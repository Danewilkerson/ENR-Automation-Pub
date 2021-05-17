from selenium.webdriver.common.by import By

class Locators():

# --- Page Locators ---
    ENR_LOGO = By.XPATH, "//div[@id='root']//div//div//header//div//div//div//img"
    COUNTY_SEAL = By.XPATH, "//div[@id='root']//div//div//div//div//div//div//div//img"
    HEADER_TITLE = By.XPATH, "//h6[contains(text(),'Election Night Results')]"
    JURISDICTION_HEADER = By.XPATH, "//p[contains(text(),'Azeroth')]"
    ELECTION_HEADER = By.XPATH, "//p[contains(text(),'Election of Ironforge | Aug 31, 2020')]"

# --- Search Locators --- 
    SEARCH_TEXTBOX = By.XPATH, "//body//header//div//div//div//div[2]"
    SEARCH_TEXTBOX_DIMENSIONS = {'height': 35, 'width': 221}
    SEARCH_TEXTBOX_PLACEHOLDER = By.XPATH, "//input[contains(@placeholder,'Search')]"
    SEARCH_CANCEL = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[1]/div[2]/div[2]/div[2]/div[1]/button[1]/span[1]/*[local-name()='svg'][1]"
    SEARCH_RESULT_CANDIDATE_TITLE = By.XPATH, "//div[contains(text(),'Candidates')]"
    SEARCH_RESULTS_CONTEST_ISSUE_TITLE = By.XPATH, "//div[contains(text(),'Contest Title')]"
    SEARCH_RESULT_FULL_NAME = By.XPATH, "//li[contains(text(),'John McManus')]"
    SEARCH_RESULT_PARTIAL_NAME = By.XPATH, "//li[contains(text(),'John Anderson')]"

# --- Download Results Locators ---
    DOWNLOAD_RESULTS_BUTTON = By.XPATH, "//body/div[@id='root']/div/div/div/div/div/div/button[1]"
    DOWNLOAD_RESULTS_BUTTON_TEXT = "Download Results"
    DOWNLOAD_RESULTS_BUTTON_DIMENSIONS = {'height': 36, 'width': 175}

# --- Parties Filter Locators ---
    PARTIES_FILTER_DROPDOWN = By.XPATH, "//body/div[@id='root']/div/div/header/div/div/div/button/span[1]//*[local-name()='svg']"
    PARTIES_FILTER_ALLPARTIES = By.XPATH, "//li[contains(text(),'All Parties')]"
    PARTIES_FILTER_DEMOCRATIC = By.XPATH, "//li[contains(text(),'Democratic')]"
    PARTIES_FILTER_REPUBLICAN = By.XPATH, "//li[contains(text(),'Republican')]"
    PARTIES_FILTERS_ALLPARTIES_TEXT = "All Parties"
    PARTIES_FILTERS_DEMOCRATIC_TEXT = "Democratic"
    PARTIES_FILTERS_REPUBLICAN_TEXT = "Republican"

# --- Precinct Reporting Card Locators ---
    PR_ICON = By.XPATH, "//body//div[@id='root']//div//div//div//div//div//div//div[1]//div[1]//div[1]//div[1]//div[1]//div[1]//div[1]//*[local-name()='svg']" 
    PR_HEADER = By.XPATH, "//body//div[@id='root']//div//div//div//div//div//div//div[1]//div[1]//div[1]//div[1]//div[2]//span[2]"
    PR_SUBHEADER = By.XPATH, "//body//div[@id='root']//div//div//div//div//div//div//div[1]//div[1]//div[1]//div[1]//div[2]//span[2]"
    PR_MAXIMIZE_MAP = By.XPATH, "//div[@id='root']//div//div//div//div//div//div//div//div//div//div//div//button//span[1]//*[local-name()='svg']" 
    PR_PIE_CHART_REPORTED = By.XPATH, "//body/div[@id='root']/div/div/div/div/div/div/div[1]/div//*[local-name()='svg']//*[name()='text'][1]"
    PR_TOTAL = By.XPATH, "//body//div[@id='root']//div//div//div//div//div//div//div[1]//div[1]//div[1]//div[2]//div[2]//div[2]"
    PR_REPORTED = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]"
    PR_FAVORITE_ICON = By.XPATH, "//body/div[@id='root']/div/div/div/div/div/div/div[1]/div//*[local-name()='svg']//*[name()='path' and contains(@d,'M12 21.35l')]"
    PR_SHARE_ICON = By.XPATH, "//body//div[@id='root']//div//div//div//div//div//div//div[1]//div[1]//div[1]//button[2]//span[1]//*[local-name()='svg']"
    PR_DROPDOWN_ARROW = By.XPATH, "//body//div[@id='root']//div//div//div//div//div//div//div[1]//div[1]//div[1]//button[3]//span[1]//*[local-name()='svg']"
    PR_TABLE_PRECINCT_HEADER = By.XPATH, "//th[contains(text(),'Precinct')]"
    PR_TABLE_TURNOUT_HEADER = By.XPATH, "//div[@id='root']//div//div//div//div//div//div//div//div//div//div//div//div//div//div//th//span[contains(text(),'Turnout')]"

# --- Voter Turnout Card Locators ---
    VT_ICON = By.XPATH, "//body//div[@id='root']//div//div//div//div//div//div[2]//div[1]//div[1]//div[1]//div[1]//div[1]//div[1]//*[local-name()='svg']"
    VT_HEADER = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]" 
    VT_SUBHEADER = By.XPATH, "//body//div[@id='root']//div//div//div//div//div//div[2]//div[1]//div[1]//div[1]//div[2]//span[2]"
    VT_PIE_CHART_REPORTED = By.XPATH, "//body/div[@id='root']/div/div/div/div/div/div/div[2]/div//*[local-name()='svg']//*[name()='text'][1]"
    VT_TOTAL = By.XPATH, "//body//div[@id='root']//div//div//div//div//div//div[2]//div[1]//div[1]//div[2]//div[1]//div[2]//div[2]"
    VT_REPORTED = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]"
    VT_FAVORITE_ICON = By.XPATH, "//body//div[@id='root']//div//div//div//div//div//div[2]//div[1]//div[1]//div[3]//button[1]//span[1]//*[local-name()='svg']//*[name()='path' and contains(@d,'M12 21.35l')]"
    VT_SHARE_ICON = By.XPATH, "//body//div[@id='root']//div//div//div//div//div//div[2]//div[1]//div[1]//div[3]//button[2]//span[1]//*[local-name()='svg']//*[name()='path' and contains(@d,'M18 16.08c')]"
    VT_DROPDOWN_ARROW = By.XPATH, "//body//div[@id='root']//div//div//div//div//div//div[2]//div[1]//div[1]//div[3]//button[3]//span[1]//*[local-name()='svg']"
    VT_TABLE_PARTY_HEADER = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[3]/table[1]/thead[1]/tr[1]/th[1]"
    VT_TABLE_TURNOUT_HEADER = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[3]/table[1]/thead[1]/tr[1]/th[2]"
    VT_TABLE_DEM = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[1]/th[1]"
    VT_TABLE_DEM_TURNOUT = By.XPATH, "//tr[1]//td[1]"
    VT_TABLE_REP = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[2]/th[1]"
    VT_TABLE_REP_TURNOUT = By.XPATH, "//tr[2]//td[1]"
    VT_GUIDE = By.XPATH, "//span[contains(text(),'Click a party row to see turnout in heatmap.')]"

# --- Wall Board Locators ---
    WALLBOARD_MAXIMIZE_ICON = By.XPATH, "//body/div/div/div/div/button/span[1]//*[local-name()='svg']"

# --- Democratic Card Locators ---
    DEM_CARD_ICON = By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/*[1]"
    DEM_CARD_HEADER = By.XPATH, "//span[contains(text(),'DEM Delegates-at-Large and Alternates-at-Large to the Na')]"
    DEM_CARD_SUBHEADER = By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/span[2]"
    DEM_CARD_LEADER_NAME = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]"
    DEM_CARD_LEADER_RESULTS = By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]"
    DEM_CARD_LEADER_BARGRAPH = By.CSS_SELECTOR, "div.jss3 div.jss36 div.jss42 div.jss43 div.jss51 div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-4 div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-12.MuiGrid-grid-md-6.MuiGrid-grid-lg-4:nth-child(1) div.MuiPaper-root.MuiCard-root.jss56.MuiPaper-elevation1.MuiPaper-rounded div.MuiCardContent-root.jss62 div.jss79 div.jss86 div.jss87 svg:nth-child(1) > rect:nth-child(2)"
    DEM_CARD_EXPAND_FOR_MORE_CANDIDATES = By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]"
    DEM_CARD_FAVORITE_ICON = By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/button[1]/span[1]/*[1]"
    DEM_CARD_SHARE_ICON = By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/button[2]/span[1]/*[1]"
    DEM_CARD_DROPDOWN_ARROW = By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/button[3]/span[1]/*[1]"
    DEM_CARD_DROPDOWN_SECOND_PLACE_NAME = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]"
    DEM_CARD_DROPDOWN_SECOND_PLACE_BARGRAPH = By.CSS_SELECTOR, "div.jss3 div.jss36 div.jss42 div.jss43 div.jss51 div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-4 div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-12.MuiGrid-grid-md-6.MuiGrid-grid-lg-4:nth-child(1) div.MuiPaper-root.MuiCard-root.jss56.MuiPaper-elevation1.MuiPaper-rounded div.MuiCollapse-container.MuiCollapse-entered div.MuiCollapse-wrapper div.MuiCollapse-wrapperInner div.MuiCardContent-root div.jss110 div.jss113:nth-child(1) div.jss86 div.jss87 svg:nth-child(1) > rect:nth-child(2)"
    DEM_CARD_DROPDOWN_SECOND_PLACE_RESULTS = By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]"

    # --- Republican Card Locators ---
    REP_CARD_ICON = By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/*[1]"
    REP_CARD_HEADER = By.XPATH, "//span[contains(text(),'REP Representative to Congress (10th District)')]"
    REP_CARD_SUBHEADER = By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/span[2]"
    REP_CARD_LEADER_NAME = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/span[1]"
    REP_CARD_LEADER_RESULTS = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]"
    REP_CARD_LEADER_BARGRAPH = By.CSS_SELECTOR, "div.jss3 div.jss36 div.jss42 div.jss43 div.jss51 div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-4 div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-12.MuiGrid-grid-md-6.MuiGrid-grid-lg-4:nth-child(3) div.MuiPaper-root.MuiCard-root.jss56.MuiPaper-elevation1.MuiPaper-rounded div.MuiCardContent-root.jss62 div.jss79 div.jss86 div.jss87 svg:nth-child(1) > rect:nth-child(2)"
    REP_CARD_EXPAND_FOR_MORE_CANDIDATES = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]"
    REP_CARD_FAVORITE_ICON = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[3]/button[1]"
    REP_CARD_SHARE_ICON = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[3]/button[2]"
    REP_CARD_DROPDOWN_ARROW = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[3]/button[3]"
    REP_CARD_DROPDOWN_SECOND_PLACE_NAME = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]"
    REP_CARD_DROPDOWN_SECOND_PLACE_BARGRAPH = By.CSS_SELECTOR, "div.jss3 div.jss36 div.jss42 div.jss43 div.jss51 div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-4 div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-12.MuiGrid-grid-md-6.MuiGrid-grid-lg-4:nth-child(3) div.MuiPaper-root.MuiCard-root.jss56.MuiPaper-elevation1.MuiPaper-rounded div.MuiCollapse-container.MuiCollapse-entered div.MuiCollapse-wrapper div.MuiCollapse-wrapperInner div.MuiCardContent-root div.jss132 div.jss135:nth-child(1) div.jss86 div.jss87 > svg:nth-child(1)"
    REP_CARD_DROPDOWN_SECOND_PLACE_RESULTS = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]"