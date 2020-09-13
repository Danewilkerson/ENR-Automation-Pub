class TestData():
    slug = "wow"

# --- Page Data ---
    BASE_URL_DEV = f"https://{slug}.stage.electionnightresults.com/"
    BASE_URL_STAGE = f"https://{slug}.stage.electionnightresults.com/"
    BASE_URL_PROD = f"https://{slug}.stage.electionnightresults.com/"
    JURISDICTION_NAME = "Azeroth"
    ELECTION_NAME = "Election of Ironforge | Aug 31, 2020"
    PAGE_TITLE = "Election Night Results"
    HEADER_TITLE_TEXT = "Election Night Results"

# --- File Urls - Shape Files, Result Files  ---
    RESULTS_JSON_URL = f"https://data.stage.electionnightresults.com/{slug}/results/results.json"
    MAP_TOPO_JSON_URL = f"https://data.stage.electionnightresults.com/{slug}/config/map.topo.json"
    BUILDING_SVG_URL = f"https://{slug}.stage.electionnightresults.com/svgs/building.svg"
    CAPITAL_SVG_URL = f"https://{slug}.stage.electionnightresults.com/svgs/capital.svg"
    ISSUE_SVG_URL = f"https://{slug}.stage.electionnightresults.com/svgs/issue.svg"

# --- Search Data ---
    SEARCH_TERM_PARTIAL_NAME = "Joh"
    SEARCH_RESULT_PARTIAL_NAME = "John Anderson"
    SEARCH_TERM_PARTIAL_NAME_2 = "dem"
    SEARCH_TERM_FULL_NAME = "John McManus"
    SEARCH_RESULT_FULL_NAME = "John McManus"
    SEARCH_RESULTS_CANDIDATE_TITLE_TEXT = "Candidates"
    SEARCH_RESULTS_CONTEST_ISSUE_TITLE_TEXT = "Contest Title/Issue Name"

# --- Download Results Data ---
    DOWNLOAD_RESULTS_FILE_URL = f"https://data.stage.electionnightresults.com/{slug}/results/results.txt"

# --- Precinct Reporting Card Data ---
    PRECINCT_REPORTING_SUBHEADER = "Last updated: August 31st, 2020 6:15 PM"
    PRECINCT_REPORTING_TOTAL = "360"
    PRECINCT_REPORTING_REPORTED = "350"
    PR_TABLE_PRECINCT_HEADER_TEXT = "Precinct"
    PR_TABLE_TURNOUT_HEADER_TEXT = "Turnout"

# --- Voter Turnout Card Data ---
    VOTER_TURNOUT_SUBHEADER = "Last updated: August 31st, 2020 6:15 PM"
    VOTER_TURNOUT_TOTAL = "1,080,426"
    VOTER_TURNOUT_REPORTED = "209,229"
    VT_TABLE_PARTY_HEADER_TEXT = "Party"
    VT_TABLE_TURNOUT_HEADER_TEXT = "Turnout"
    VT_GUIDE_TEXT = "Click a party row to see turnout in heatmap."