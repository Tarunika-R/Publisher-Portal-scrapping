from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from Tools.Tool import (id_to_content, driver, start_verbose, end_verbose, Spinner, Bar)
from alive_progress import alive_bar
from termcolor import colored
import random

def extract_fees_table(url, chrome_driver_path="chromedriver.exe", verbose=False):
        
    if verbose:
        start_verbose("extract_fees_table", url)

    with alive_bar(100, spinner=random.choice(Spinner), bar=random.choice(Bar), title=colored("🔃 Loading", "green")) as bar:
        for _ in range(5):
            time.sleep(0.5)
            bar(20)

    # Initialize Service object for WebDriver
    service = Service(chrome_driver_path)
    
    # Start the WebDriver using the service object
    driver = webdriver.Chrome(service=service)
    
    # Open the website
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    
    # Click the "Read More" button and extract table content
    try:
        # Click the "Read More" button
        read_more = driver.find_element(By.XPATH, """//*[@id="fees_section_overview"]/div[2]/div[2]""")
        read_more.click()
        time.sleep(2)  # Wait for the content to load
        
        # Find the content div that may contain tables
        content_div = driver.find_element(By.XPATH, """//*[@id="fees_section_overview"]/div[2]""")
        
        # Check for any tables (<table>) in the div
        tables = content_div.find_elements(By.TAG_NAME, "table")
        extracted_data = []  # To store table data
        
        if tables:
            for table in tables:
                rows = table.find_elements(By.TAG_NAME, "tr")
                for row in rows:
                    cols = row.find_elements(By.TAG_NAME, "td")
                    row_data = [col.text for col in cols]
                    extracted_data.append(row_data)  # Add each row's data to extracted_data
        
        result = extracted_data if extracted_data else "No tables found"
    
    except Exception as e:
        result = f"Error: {e}"
    
    finally:
        # Close the browser
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
