<<<<<<< HEAD
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException
import time

# Function to initialize the WebDriver with retry mechanism
def init_driver():
    MAX_RETRIES = 3
    retries = 0
    while retries < MAX_RETRIES:
        try:
            service = Service(ChromeDriverManager().install(), port=0)  # Automatically pick a free port
            driver = webdriver.Chrome(service=service)
            driver.maximize_window()
            print("Driver initialized successfully.")
            return driver
        except WebDriverException as e:
            retries += 1
            print(f"Error initializing driver, retrying... {retries}/{MAX_RETRIES}")
            if retries >= MAX_RETRIES:
                print("Max retries reached. Exiting.")
                raise e
            time.sleep(2)  # Wait before retrying

# Function to quit the WebDriver
def quit_driver(driver):
    try:
        if driver:
            driver.quit()
            print("Driver quit successfully.")
    except Exception as e:
        print(f"Error quitting driver: {e}")

# Function to fetch menu tabs
def fetch_menu_tabs(driver, url: str, verbose=False) -> list:
    if verbose:
        print("Started fetching tabs from the given link 📑")
    
    tabs = []
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#main-wrapper > div.b876.three_col.uilp.reverse_two_col > div > div > ul"))
        )
        menu_items = driver.find_elements(By.CSS_SELECTOR, "#main-wrapper > div.b876.three_col.uilp.reverse_two_col > div > div > ul li")
        for item in menu_items:
            tabs.append(item.text)
    except Exception as e:
        print(f"Error fetching menu tabs: {e}")
    
    if verbose:
        print("Fetched tabs:", tabs)
    
    return tabs

# Function to fetch college highlights
def fetch_college_highlights(driver, url, verbose=False):
    try:
        driver.get(url)
        output_data = {}

        if verbose:
            print("Fetching college highlights...")

        try:
            wait = WebDriverWait(driver, 20)
            try:
                overlay_close_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "close-popup")))
                overlay_close_button.click()
                if verbose:
                    print("Closed overlay popup")
            except TimeoutException:
                if verbose:
                    print("No overlay found or timed out waiting for overlay")

            # Click 'Read More' to expand content
            read_more = wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@id="ovp_section_highlights"]/div[2]/div[1]/div/span""")))
            driver.execute_script("arguments[0].scrollIntoView();", read_more)
            time.sleep(3)
            driver.execute_script("arguments[0].click();", read_more)

            content_div = driver.find_element(By.XPATH, """//*[@id="ovp_section_highlights"]/div[2]/div[1]/div/div/div/div""")

            # Extract tables
            tables = content_div.find_elements(By.TAG_NAME, "table")
            table_data = []
            for table in tables:
                rows = table.find_elements(By.TAG_NAME, "tr")
                for row in rows:
                    cols = row.find_elements(By.TAG_NAME, "td")
                    row_data = [col.text for col in cols]
                    if row_data:
                        table_data.append(row_data)

            paragraphs = content_div.find_elements(By.TAG_NAME, "p")
            total_para = ""
            for paragraph in paragraphs:
                total_para += paragraph.text + "\n"
            output_data['Highlights'] = total_para if total_para else "Content Not Found :\\"

            output_data["Table"] = table_data if table_data else []

            iframes = driver.find_elements(By.TAG_NAME, "iframe")
            iframe_list = [iframe.get_attribute("src") for iframe in iframes if iframe.get_attribute("src")]
            output_data["Iframes"] = iframe_list

        except TimeoutException as e:
            print(f"Timeout while waiting for elements: {e}")
        except Exception as e:
            print(f"Error scraping data: {e}")

        if verbose:
            print("Finished fetching data:", output_data)

        return output_data

    except WebDriverException as e:
        print(f"WebDriver exception occurred: {e}")
        quit_driver(driver)

# Function to fetch top details of the college
def clg_info_top_details(driver, data: dict):
    out_data = {}
    for key, val in data.items():
        print(f"Locating elements with class: {val}")

        try:
            elements = WebDriverWait(driver, 40).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, val))
            )
        except TimeoutException:
            return {'msg': f"Timeout while locating elements with class {val}"}
        except NoSuchElementException:
            return {'msg': f"No elements found with class {val}"}
        except WebDriverException as e:
            return {'msg': f"Webdriver issue: {str(e)}"}

        data_id = []
        for element in elements:
            data_id.extend(element.text.split("\n"))
        out_data[key] = data_id

    return out_data

# Merged Function to fetch both menu tabs and college info
def fetch_and_scrape_college(driver, url, verbose=False):
    tabs = fetch_menu_tabs(driver, url, verbose)
    for tab in tabs:
        if tab == "College Info":
            print("Found 'College Info' tab, fetching details...")
            highlights = fetch_college_highlights(driver, url, verbose)
            print("College Highlights:", highlights)
            
            data = {"line_1": "e9dd86", "line_2": "e1a898"}  # Sample data for clg_info_top_details
            top_details = clg_info_top_details(driver, data)
            print("College Top Details:", top_details)

# Example usage
if __name__ == "__main__":
    url = 'https://www.shiksha.com/college/adina-institute-of-science-and-technology-sagar-60309'
    driver = init_driver()

    try:
        fetch_and_scrape_college(driver, url, verbose=True)
    finally:
        quit_driver(driver)
=======
from TabSupport.Tools.Tool import fetch_menu_tabs
from  TabSupport.ClgInfo import *
from  TabSupport.fees import *
from  TabSupport.admission import *
from  TabSupport.placement import *
from  TabSupport.ranking import *
from  TabSupport.HostelAndInfra import *
from  TabSupport.scholarships import *


url = "https://www.shiksha.com/college/iit-madras-indian-institute-of-technology-adyar-chennai-3031/"
# ['College Info', 'Courses', 'Fees', 'Reviews', 'Admissions', 'Placements', 'Cut-Offs', 'Rankings', 'Hostel & Campus', 'Scholarships']
print(fetch_menu_tabs(url, True))

clg_info = {}
fees = {}
Admissions = {}

def collect_clg_content(url, verbose=False):
    for i in fetch_menu_tabs(url, verbose):
        if i is "College Info":
            clg_info['main_details'] = clg_info_top_details(url, verbose)
            clg_info['info_highlights'] = fetch_college_highlights(url,  verbose)
        elif i  is "Fees":
            fees["fees_table"] = extract_fees_table(url, verbose)
        elif i is "Admissions":
            fees["admission_table"] = extract_admission_table(url, verbose)
        elif i is "Placements":
            fees["extract_placement"] = extract_placement(url, verbose)
        elif i is "Rankings":
            fees["extract_placement"] = extract_ranking_info(url, verbose)
        elif i is "Hostel & Campus":
            fees["extract_placement"] = extract_hostel_info(url, verbose)
        elif i is "Scholarships":
            fees["extract_placement"] = fetch_scholarships(url, verbose)
>>>>>>> parent of c3f406f ("Refactored code organization, removed redundant comments, and updated import statements in multiple files.")
