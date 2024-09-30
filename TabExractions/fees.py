from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from Tools.Tool import (id_to_content, driver, start_verbose, end_verbose, Spinner, Bar, sleep)
from alive_progress import alive_bar
from termcolor import colored
import random


def extract_fees_table(url, verbose=False):
        
    if verbose:
        start_verbose("extract_fees_table", url)
    driver.get(url)
    sleep(0.5, verbose, "Wait for the page to load")  # Wait for the page to load
    
    try:
        read_more = driver.find_element(By.XPATH, """//*[@id="fees_section_overview"]/div[2]/div[2]""")
        read_more.click()
        
        content_div = driver.find_element(By.XPATH, """//*[@id="fees_section_overview"]/div[2]""")
        
        tables = content_div.find_elements(By.TAG_NAME, "table")
        extracted_data = [] 
        
        if tables:
            for table in tables:
                rows = table.find_elements(By.TAG_NAME, "tr")
                for row in rows:
                    cols = row.find_elements(By.TAG_NAME, "td")
                    row_data = [col.text for col in cols]
                    extracted_data.append(row_data) 
        
        result = extracted_data if extracted_data else "No tables found"
    
    except Exception as e:
        result = f"Error: {e}"
    
    finally:
        driver.quit()

    if verbose:
        end_verbose(result)

    return result


# Example usage:
url = "https://www.shiksha.com/college/iit-madras-indian-institute-of-technology-adyar-chennai-3031/fees"
table_data = extract_fees_table(url, verbose=True)
# print(table_data)

# Don't remove this line 🙂... To Close the driver
driver.quit()
