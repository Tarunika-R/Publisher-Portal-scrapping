from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

from selenium.webdriver.common.by import By
import time
from .Tools.Tool import (id_to_content, driver, start_verbose, end_verbose, Spinner, Bar, sleep)
from alive_progress import alive_bar
from termcolor import colored
import random

def extract_admission_table(url, verbose=False):
    """
    Extracts admission-related table data from the specified webpage.
    
    Returns:
    - A list of lists representing the table rows and their corresponding column data.
    - If no tables are found, returns: "No tables found".
    - If an error occurs, returns: "Error: <error_message>".
    """
    
    if verbose:
        start_verbose("extract_admission_table", url)

    driver.get(url)
    sleep(0.5, verbose, "Wait for the page to load")
    
    try:
        # Wait for the "Read More" button to be clickable, if it exists
        try:
            read_more = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, """//*[@id="admission_section_admission_process"]/div[2]/div[1]/div/span"""))
            )
            read_more.click()
            sleep(1, verbose, "Clicked on 'Read More' button")
        except TimeoutException:
            if verbose:
                print("No 'Read More' button found or it took too long to load.")
        
        # Locate the content div containing the tables
        content_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, """//*[@id="admission_section_admission_process"]/div[2]/div[1]/div/div/div/div"""))
        )

        # Extract tables from the content div
        tables = content_div.find_elements(By.TAG_NAME, "table")
        extracted_data = []
        tables_data = []
        
        if tables:
            for table in tables:
                rows = table.find_elements(By.TAG_NAME, "tr")
                for row in rows:
                    cols = row.find_elements(By.TAG_NAME, "td")
                    row_data = [col.text for col in cols]
                    if row_data:  # Only append non-empty rows
                        extracted_data.append(row_data)
                tables_data.append(extracted_data)
                extracted_data = []
        
        result = tables_data if tables_data else "No tables found"
    
    except NoSuchElementException as e:
        result = f"Error: Element not found - {e}"
    except Exception as e:
        result = f"Error: {e}"

    if verbose:
        end_verbose(result)

    return result


# Example usage:
# url = 'https://www.shiksha.com/college/iim-ahmedabad-indian-institute-of-management-vastrapur-307/admission'

# table_data = extract_admission_table(url, verbose=True)
# print(table_data)

# Don't remove this line 🙂... To Close the driver
# driver.quit()
