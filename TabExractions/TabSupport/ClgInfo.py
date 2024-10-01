from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import time

MAX_RETRIES = 3

# Function to initialize the WebDriver with automatic retry mechanism
def init_driver():
    retries = 0
    while retries < MAX_RETRIES:
        try:
            # Use WebDriver Manager to automatically manage ChromeDriver installation
            service = Service(ChromeDriverManager().install(), port=0)  # Automatically pick a free port
            driver = webdriver.Chrome(service=service)
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

def clg_info_top_details(driver, url: str, verbose=False) -> dict:
    if verbose:
        print("Starting to fetch college top details...")

    try:
        driver.get(url)

        # Example of extracting college information
        try:
            college_name = driver.find_element(By.CLASS_NAME, 'e70a13').text
            details_1 = [element.text for element in driver.find_elements(By.CLASS_NAME, 'e9dd86')]
            details_2 = [element.text for element in driver.find_elements(By.CLASS_NAME, 'e1a898')]

            result = {
                'ClgName': college_name,
                'Details_1': details_1,
                'Details_2': details_2
            }

            if verbose:
                print("Fetched details:", result)

            return result

        except Exception as e:
            print(f"Error fetching data: {e}")
            return {}

    except WebDriverException as e:
        print(f"WebDriver exception occurred: {e}")
        quit_driver(driver)

def fetch_college_highlights(driver, url, verbose=False):
    try:
        driver.get(url)  # `driver` should be passed here, not a string like `url`
        output_data = {}

        if verbose:
            print("Fetching college highlights...")

        try:
            wait = WebDriverWait(driver, 20)  # Increase the wait time to 20 seconds

            # Handle popups or overlays
            try:
                overlay_close_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "close-popup")))
                overlay_close_button.click()
                if verbose:
                    print("Closed overlay popup")
            except TimeoutException as e:
                if verbose:
                    print(f"No overlay found or timed out waiting for overlay: {e}")

            # Click 'Read More' to expand content
            read_more = wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@id="ovp_section_highlights"]/div[2]/div[1]/div/span""")))
            driver.execute_script("arguments[0].scrollIntoView();", read_more)
            time.sleep(3)
            try:
                driver.execute_script("arguments[0].click();", read_more)
            except Exception as e:
                print(f"Error clicking 'Read More' with JS: {e}")

            # Scrape highlights, tables, and iframes
            content_div = driver.find_element(By.XPATH, """//*[@id="ovp_section_highlights"]/div[2]/div[1]/div/div/div/div""")

            # Extract tables
            tables = content_div.find_elements(By.TAG_NAME, "table")
            table_data = []
            if tables:
                for table in tables:
                    rows = table.find_elements(By.TAG_NAME, "tr")
                    for row in rows:
                        cols = row.find_elements(By.TAG_NAME, "td")
                        row_data = [col.text for col in cols]
                        if row_data:
                            table_data.append(row_data)

            paragraphs = content_div.find_elements(By.TAG_NAME, "p")
            total_para = ""
            if paragraphs:
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


# Example usage
url = 'https://www.shiksha.com/college/adina-institute-of-science-and-technology-sagar-60309'

# Initialize the driver with retries
driver = init_driver()

# Fetch college highlights with verbose mode
if driver:
    fetch_college_highlights(driver, url, True)  # Pass the driver as the first argument
    quit_driver(driver)  # Ensure driver quits even if everything succeeds
