from selenium.webdriver.common.by import By
import time
from .Tools.Tool import (id_to_content, driver, start_verbose, end_verbose, Spinner, Bar, sleep)
from alive_progress import alive_bar
from termcolor import colored
import random


def extract_fees_table(url, verbose=False):
    """
### 📑 **Function Overview**:
The `extract_fees_table` function extracts fee-related table data from a specified webpage. It automates the interaction with the webpage by clicking elements (like a "Read More" button) to expand content and scrapes the table data if available. The function includes a loading animation 🌀 and verbose mode for detailed execution feedback.

### 🛠️ **Parameters**:
- **url** *(str)*: The URL of the webpage containing the fees information from which the data is to be extracted 🌍. fo
- **chrome_driver_path** *(str, optional)*: The file path to the Chrome WebDriver executable. It is used to start the automated browser sessionr web scraping 🖥️.
  - Default: `"chromedriver.exe"`
- **verbose** *(bool, optional)*: A flag to enable or disable verbose mode. If `True`, the function prints additional status messages and uses a progress bar during execution 📢.
  - Default: `False`

### ⚙️ **How It Works**:
1. **Initialize WebDriver**:
   - The function uses Selenium WebDriver to launch a Chrome browser session and open the specified webpage. The browser instance is controlled via the `chrome_driver_path`.
  
2. **Click "Read More" Button**:
   - The function locates the "Read More" button using XPath (`//*[@id="fees_section_overview"]/div[2]/div[2]`) and clicks it to reveal hidden content, such as fees tables.

3. **Extract Table Data**:
   - After expanding the content, the function looks for `<table>` elements within the page's content section.
   - It iterates through each table, extracting rows (`<tr>`) and columns (`<td>`), storing the text in the `extracted_data` list.

4. **Verbose Mode**:
   - When `verbose=True`, the function provides additional feedback using colored text and shows a progress bar with a spinner to indicate the status of the scraping process.

5. **Error Handling**:
   - The function is wrapped in a `try-except` block. In case of any error (e.g., missing elements or webpage issues), it captures the error message and returns it.

6. **Close WebDriver**:
   - After the extraction process, the WebDriver is closed to free system resources, whether the extraction succeeds or fails.

### 🔄 **Return Value**:
- The function returns a list of lists representing the table rows and their corresponding column data:
  - Example:
    [
        ["Program", "Total Fees (INR)"],
        ["MBA", "23,00,000"],
        ["Executive MBA", "25,50,000"]
    ]
- If no tables are found, it returns: `"No tables found"`.
- If an error occurs during execution, the function returns: `"Error: <error_message>"`."""
    print(url)
    if verbose:
        start_verbose("extract_fees_table", url)
    driver.get(url)
    time.sleep(3)

    sleep(0.5, verbose, "Wait for the page to load")
    
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
                    if row_data != []:
                        extracted_data.append(row_data) 
        
        result = extracted_data if extracted_data else "No tables found"
    
    except Exception as e:
        result = f"Error: {e}"
    
    ""

    if verbose:
        end_verbose(result)

    return result


# Example usage:
# url = "https://www.shiksha.com/college/coimbatore-institute-of-technology-19322/fees"
# table_data = extract_fees_table(url, verbose=True)
# # print(table_data)

# # Don't remove this line 🙂... To Close the driver
# driver.quit()
