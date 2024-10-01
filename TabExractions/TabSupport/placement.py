from selenium.webdriver.common.by import By
import time
from .Tools.Tool import (id_to_content, driver, start_verbose, end_verbose, Spinner, Bar, sleep)
from alive_progress import alive_bar
from termcolor import colored
import random


def extract_placement(url, verbose=False):
    """
    ### 📑 *Function Overview*:
    The extract_placement() function extracts placement-related table data from a specified webpage. It automates the interaction with the webpage by clicking elements (like a "Read More" button) to expand content and scrapes the table data if available. The function includes a loading animation 🌀 and verbose mode for detailed execution feedback.

    ### 🛠 *Parameters*:
    - *url* (str): The URL of the webpage containing the placement information from which the data is to be extracted 🌍.
    - *chrome_driver_path* (str, optional): The file path to the Chrome WebDriver executable. It is used to start the automated browser session for web scraping 🖥.
    - Default: "chromedriver.exe"
    - *verbose* (bool, optional): A flag to enable or disable verbose mode. If True, the function prints additional status messages and uses a progress bar during execution 📢.
    - Default: False

    ### ⚙ *How It Works*:
    2. *Extract Table Data*:
    - After expanding the content, the function looks for <table> elements within the page's content section related to placement data.
    - It iterates through each table, extracting rows (<tr>) and columns (<td>), storing the text in the extracted_data list.

    3. *Verbose Mode*:
    - When verbose=True, the function provides additional feedback using colored text and shows a progress bar with a spinner to indicate the status of the scraping process.

    4. *Error Handling*:
    - The function is wrapped in a try-except block. In case of any error (e.g., missing elements or webpage issues), it captures the error message and returns it.

    5. *Close WebDriver*:
    - After the extraction process, the WebDriver is closed to free system resources, whether the extraction succeeds or fails.

    ### 🔄 *Return Value*:
        
        - The function returns a list of lists, with each inner list representing a specific data table or section from the website. 
        Each list corresponds to rows of data and their respective columns.
        
        *Example Return:*
        [
            [["College Name", "Location", "Ranking"]], 
            [["IIT Bombay", "Mumbai", "1"]], 
            [["IIT Delhi", "Delhi", "2"]], 
            [["IIT Madras", "Chennai", "3"]],
            
            [["Median Salary", "Highest Salary", "Number of Offers"]],
            [["INR 15 LPA", "INR 1.5 Crore", "200"]],
            [["INR 12 LPA", "INR 1.2 Crore", "180"]],
            
            [["Popular Recruiters"]],
            [["Google", "Amazon", "Microsoft"]],
            [["Accenture", "JP Morgan", "Deloitte"]],
            
            [["Placement Statistics"]],
            [["Number of Offers", "1,000"]],
            [["Highest Package", "2.5 Crore"]],
        ]
        
        - Each list contains table rows and their associated data. For instance, the first list contains college information, followed by placement statistics, popular recruiters, and placement details such as the number of offers or highest packages.
        - The output format will depend on the website's structure and the data being extracted.

        - *If no tables are found*, it returns:
        "No tables found"

        - *If an error occurs during execution*, the function returns:
        "Error: <error_message>"
        
    """

    if verbose:
        start_verbose("extract_placement", url)
    driver.get(url)
    sleep(0.5, verbose, "Wait for the Placement page to load")
    
    try:
        content_div = driver.find_element(By.XPATH, """//*[@id="Overview"]/div/div/div/div/div[2]""")
        
        tables = content_div.find_elements(By.TAG_NAME, "table")
        extracted_data = [] 
        tables_data = []
        
        if tables:
            for table in tables:
                rows = table.find_elements(By.TAG_NAME, "tr")
                for row in rows:
                    cols = row.find_elements(By.TAG_NAME, "td")
                    row_data = [col.text for col in cols]
                    if row_data != []:
                        extracted_data.append(row_data) 
                tables_data.append(extracted_data)
                extracted_data = []
        
        result = tables_data if tables_data else "No tables found"
    
    except Exception as e:
        result = f"Error: {e}"
    
    ""

    if verbose:
        end_verbose(result)

    return result


# Example usage:
# url = 'https://www.shiksha.com/college/iit-madras-indian-institute-of-technology-adyar-chennai-3031/placement'

# table_data = extract_placement(url, verbose=True)
# # print(table_data)

# # Don't remove this line 🙂... To Close the driver
# driver.quit()