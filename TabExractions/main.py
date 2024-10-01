# from TabSupport.ClgInfo import init_driver, fetch_college_highlights, clg_info_top_details

# # Example usage
# url = 'https://www.shiksha.com/college/adina-institute-of-science-and-technology-sagar-60309'

# # Initialize the driver
# driver = init_driver()

# # Fetch college highlights with verbose mode
# fetch_college_highlights(driver, url, True)  # Pass the driver as the first argument

# # Fetch college top details with verbose mode
# clg_info_top_details(driver, url, True)  # Pass the driver as the first argument

# # Close the driver after the tasks
# driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
def init_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

def fetch_menu_tabs(driver, url: str, verbose=False) -> list:
    """
    📑 **Function Overview**:
    This function navigates to the provided URL and fetches the tab menu items present on the webpage.
    ### 🛠️ **Parameters**:
    - **url** *(str)*: The URL of the webpage from which the menu tabs are to be fetched.
    - **driver**: The Selenium WebDriver instance that is used to control the browser.
    ### ✅ **Return**:
    - **tabs** *(list)*: A list of strings representing the text of each menu tab found on the page.
    """
    if verbose:
        print("Started fetching tabs from the given link 📑")
    
    tabs = []
    
    try:
        driver.get(url)
        
        # Wait for the menu to be present on the page
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#main-wrapper > div.b876.three_col.uilp.reverse_two_col > div > div > ul"))
        )
        
        # Find the menu items and extract their text
        menu_items = driver.find_elements(By.CSS_SELECTOR, "#main-wrapper > div.b876.three_col.uilp.reverse_two_col > div > div > ul li")
        for item in menu_items:
            tabs.append(item.text)
    except Exception as e:
        print(f"Error fetching menu tabs: {e}")
    
    if verbose:
        print("Fetched tabs:", tabs)
    
    return tabs

# Example usage
if __name__ == "__main__":
    url = 'https://www.shiksha.com/college/shri-shiv-mahavidyalaya-ghazipur-183029'
    
    # Initialize the WebDriver
    driver = init_driver()
    
    # Fetch the menu tabs with verbose mode enabled
    tabs = fetch_menu_tabs(driver, url, verbose=True)
    
    # Print the fetched tabs
    print(tabs)
    
    # Close the WebDriver after completion
    driver.quit()
