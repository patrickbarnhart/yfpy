from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set up Chrome in headless mode
options = Options()
options.add_argument("--headless")
options.add_argument("--log-level=3")


# Set up the Selenium webdriver

# %%
def get_razzball_qs():
# Open the page
    driver = webdriver.Chrome(options=options)

    driver.get('https://razzball.com/playerrater-preseason-yahoomlb12-6X6qs/')


    table = driver.find_element(By.ID, 'neorazzstatstable')

    rankings_dict = {}  # Initialize an empty dictionary
    
    sp_count = 0

    # Extract and print data (example)
    for row in table.find_elements(By.TAG_NAME, 'tr')[1:]:  # Skip header
        if sp_count >= 150:  #
            break  
        cols = row.find_elements(By.TAG_NAME, 'td')  
        if cols:  
            rank = cols[0].text.strip()
            name = cols[1].text.strip()
            if rank and name:  
                rankings_dict[name] = rank
                sp_count += 1
    # Clean up
    driver.quit()

    return rankings_dict

# %%
def get_razzball_standard():
    # modify for pitchers vs hitters
    driver = webdriver.Chrome(options=options)

# Open the page
    driver.get('https://razzball.com/top-500-for-2024-fantasy-baseball/')


    table = driver.find_element(By.ID, 'neorazzstatstable')

    rankings_dict = {}  # Initialize an empty dictionary

    sp_count = 0

    # Extract and print data (example)
    for row in table.find_elements(By.TAG_NAME, 'tr')[1:]:  # Skip header
        if sp_count >= 150:  #
            break  
        cols = row.find_elements(By.TAG_NAME, 'td')  # Find all td elements
        if cols and len(cols) >= 5:  # Ensure there are enough columns to check the player's position
            position = cols[4].text.strip()  # The 5th td contains the player's position
            if position != "SP" and position != "RP":  # Check if the position is "SP"
                rank = cols[0].text.strip()
                name = cols[1].text.strip()
                if rank and name:  # Make sure both rank and name are not empty
                    rankings_dict[name] = rank
                    sp_count += 1
    # Clean up
    driver.quit()

    return {k: i for i, (k, _) in enumerate(rankings_dict.items(), start=1)}