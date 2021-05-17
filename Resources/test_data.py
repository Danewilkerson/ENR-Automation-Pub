class TestData():
    slug = "wow" # Election Slug
    env = "stage" # Environment Variable ("Dev", "Stage")
    customer_id = "397"
    election_id = "496"

# --- Page Data ---
    BASE_URL = f"https://{slug}.{env}.electionnightresults.com/"
    JURISDICTION_NAME = "Azeroth"
    ELECTION_NAME = "Election of Ironforge | Aug 31, 2020"
    PAGE_TITLE = "Election Night Results"
    HEADER_TITLE_TEXT = "Election Night Results"

# --- File Urls - Shape Files, Result Files  ---
    RESULTS_JSON_URL = f"https://data.{env}.electionnightresults.com/{slug}/results/results.json"
    MAP_TOPO_JSON_URL = f"https://data.{env}.electionnightresults.com/{slug}/config/map.topo.json"
    BUILDING_SVG_URL = f"https://{slug}.{env}.electionnightresults.com/svgs/building.svg"
    CAPITAL_SVG_URL = f"https://{slug}.{env}.electionnightresults.com/svgs/capital.svg"
    ISSUE_SVG_URL = f"https://{slug}.{env}.electionnightresults.com/svgs/issue.svg"

# --- Search Data ---
    SEARCH_TERM_PARTIAL_NAME = "Joh"
    SEARCH_RESULT_PARTIAL_NAME = "John Anderson"
    SEARCH_TERM_PARTIAL_NAME_2 = "dem"
    SEARCH_TERM_FULL_NAME = "John McManus"
    SEARCH_RESULT_FULL_NAME = "John McManus"
    SEARCH_RESULTS_CANDIDATE_TITLE_TEXT = "Candidates"
    SEARCH_RESULTS_CONTEST_ISSUE_TITLE_TEXT = "Contest Title/Issue Name"

# --- Download Results Data ---
    DOWNLOAD_RESULTS_FILE_URL = f"https://data.{env}.electionnightresults.com/{slug}/results/results.txt"

# --- Precinct Reporting Card Data ---
    PRECINCT_REPORTING_SUBHEADER = "Last updated: November 4th, 2020 7:05 AM"
    PRECINCT_REPORTING_TOTAL = "360"
    PRECINCT_REPORTING_REPORTED = "350"
    PR_TABLE_PRECINCT_HEADER_TEXT = "Precinct"
    PR_TABLE_TURNOUT_HEADER_TEXT = "Turnout"

# --- Voter Turnout Card Data ---
    VOTER_TURNOUT_SUBHEADER = "Last updated: November 4th, 2020 7:05 AM"
    VOTER_TURNOUT_TOTAL = "1,080,426"
    VOTER_TURNOUT_REPORTED = "209,229"
    VT_TABLE_PARTY_HEADER_TEXT = "Party"
    VT_TABLE_TURNOUT_HEADER_TEXT = "Turnout"
    VT_GUIDE_TEXT = "Click a party row to see turnout in heatmap."
    VT_TABLE_DEM_TEXT = "Democrat"
    VT_TABLE_DEM_TURNOUT_TEXT = "57.82%"
    VT_TABLE_REP_TEXT = "Republican"
    VT_TABLE_REP_TURNOUT_TEXT = "42.18%"

# --- Wall Board Data ---
    WALLBOARD_BASE_URL = f"https://{slug}.{env}.electionnightresults.com/wallboard/"
    WALLBOARD_LATEST_STATUSES_URL = f"https://api.{env}.electionnightresults.com/api/v1/customers/{customer_id}/elections/{election_id}/results-metafiles/latest-statuses"

# --- Democratic Card Locators ---
    DEM_CARD_HEADER_TEXT = "DEM Delegates-at-Large and Alternates-at-Large to the Na"
    DEM_CARD_SUBHEADER_TEXT = "Last updated: November 4th, 2020 7:05 AM"
    DEM_BLUE_BARGRAPH_COLOR = "#0D47A1"
    DEM_CARD_LEADER_NAME_TEXT = "Joseph R. Biden, Jr."
    DEM_CARD_LEADER_RESULTS_TEXT = "76.8%"
    DEM_CARD_EXPAND_FOR_MORE_CANDIDATES_TEXT = "Expand for more candidates in this race"
    DEM_CARD_DROPDOWN_SECOND_PLACE_NAME_TEXT = "Bernie Sanders"
    DEM_CARD_DROPDOWN_SECOND_PLACE_RESULTS_TEXT = "15.1%"

# --- Republican Card Locators ---
    REP_CARD_HEADER_TEXT = "REP Representative to Congress (10th District)"
    REP_CARD_SUBHEADER_TEXT = "Last updated: November 4th, 2020 7:05 AM"
    REP_RED_BARGRAPH_COLOR = "#d50000"
    REP_CARD_LEADER_NAME_TEXT = "Mike Turner"
    REP_CARD_LEADER_RESULTS_TEXT = "87.6%"
    REP_CARD_EXPAND_FOR_MORE_CANDIDATES_TEXT = "Expand for more candidates in this race"
    REP_CARD_DROPDOWN_SECOND_PLACE_NAME_TEXT = "John Anderson"
    REP_CARD_DROPDOWN_SECOND_PLACE_RESULTS_TEXT = "7.1%"