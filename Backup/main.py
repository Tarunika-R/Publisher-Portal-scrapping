from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from TabSupport.Tools.Tool import fetch_menu_tabs, driver

from  TabSupport.ClgInfo import *
from  TabSupport.fees import *
from  TabSupport.admission import *
from  TabSupport.placement import *
from  TabSupport.ranking import *
from  TabSupport.HostelAndInfra import *
from  TabSupport.scholarships import *
from  TabSupport.reviews import *

def collect_clg_content(url: list, verbose=False):
    """
    This function collects the content of the college from the given url.
    It uses the fetch_menu_tabs function to get the menu tabs and then uses the respective functions 
    to collect the content of each tab.
    url parameter: [url, clg name]
    """
    # Set up ChromeDriver service
    chrome_driver_path = "chromedriver.exe"  # Ensure this path is correct
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    
    try:
        # Open the college URL
        driver.get(url[0])

        # Allow some time for the page to load
        time.sleep(3)
        
        clg_details = {}

        # Replace this with your actual tab fetching logic
        tabs = fetch_menu_tabs(url[0], verbose)  # Dummy function, replace with your actual implementation

        # Iterate through each tab and scrape the respective content
        for i in tabs:
            if i == "College Info":
                clg_details['college_info'] = [clg_info_top_details(url[0], verbose), fetch_college_highlights(url[0], verbose)]
            elif i == "Fees":
                clg_details["fees_table"] = extract_fees_table(url[0], verbose)
            elif i == "Admissions":
                clg_details["admission_table"] = extract_admission_table(url[0], verbose)
            elif i == "Placements":
                clg_details["extract_placement"] = extract_placement(url[0], verbose)
            elif i == "Rankings":
                clg_details["extract_ranking"] = extract_ranking_info(url[0], verbose)
            elif i == "Hostel & Campus":
                clg_details["extract_hostel"] = extract_hostel_info(url[0], verbose)
            elif i == "Scholarships":
                clg_details["extract_scholarship"] = fetch_scholarships(url[0], verbose)
            elif i == "Reviews":
                clg_details["extract_review_text"] = extract_review_text(url[1], verbose)

        return clg_details

    except WebDriverException as e:
        print(f"Error while fetching content: {e}")
        return None

    finally:
        # Make sure to quit the driver to release resources
        driver.quit()

# Test the function
college_url = ["https://www.shiksha.com/college/coimbatore-institute-of-technology-19322", "Coimbatore Institute of Technology"]
result = collect_clg_content(college_url, verbose=True)
print(result)
