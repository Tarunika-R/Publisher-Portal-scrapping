from TabSupport.Tools.Tool import fetch_menu_tabs, driver  # Assuming driver is initialized here
from TabSupport.ClgInfo import *
from TabSupport.fees import *
from TabSupport.admission import *
from TabSupport.placement import *
from TabSupport.ranking import *
from TabSupport.HostelAndInfra import *
from TabSupport.scholarships import *
from TabSupport.reviews import *
import time
from selenium.common.exceptions import WebDriverException

college_url = ["https://www.shiksha.com/college/coimbatore-institute-of-technology-19322", "Coimbatore Institute of Technology"]

def collect_clg_content(url, name, verbose=False):
    """
    This function collects the content of the college from the given url.
    It uses the fetch_menu_tabs function to get the menu tabs and then uses the respective functions 
    to collect the content of each tab.
    url parameter: [url, clg name]
    """
    clg_details = {}

    try:
        tabs = fetch_menu_tabs(url, verbose)  

        if not tabs:
            print("No tabs found, ensure that fetch_menu_tabs is implemented correctly.")
            return

        for i in tabs:
            if i == "College Info1":
                print(f"Fetching college information for: {name}")

                top = clg_info_top_details(url, verbose)
                end = fetch_college_highlights(url, verbose)

                clg_details['college_info1'] = [top, end]
                print("College Info fetched successfully!")
            elif i == "Fees":
                clg_details["fees_table"] = extract_fees_table(url+"/fees", verbose)
            elif i == "Admissions":
                time.sleep(10)
                clg_details["admission_table"] = extract_admission_table(url+"/admission", verbose)
            # elif i == "Placements":
            #     clg_details["extract_placement"] = extract_placement(url, verbose)
            # elif i == "Rankings":
            #     clg_details["extract_ranking"] = extract_ranking_info(url, verbose)
            # elif i == "Hostel & Campus":
            #     clg_details["extract_hostel"] = extract_hostel_info(url, verbose)
            # elif i == "Scholarships":
            #     clg_details["extract_scholarship"] = fetch_scholarships(url, verbose)
            # elif i == "Reviews":
            #     clg_details["extract_review_text"] = extract_review_text(url, verbose)
            else:
                print(f"Tab {i} is not handled yet in the current implementation.")

        print(clg_details)

    except WebDriverException as e:
        print(f"Error encountered: {e}")

    finally:
        try:
            driver.quit()
        except Exception as ex:
            print(f"Error closing driver: {ex}")

collect_clg_content(college_url[0], college_url[1], True)
# table_data = extract_fees_table(college_url[0]+"/fees", verbose=True)
# print(table_data)
