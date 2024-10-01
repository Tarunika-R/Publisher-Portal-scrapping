from .Tools.Tool import ( id_to_content, driver, start_verbose, end_verbose, sleep)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def fetch_scholarships(url, verbose):
    """
    ### 📑 **Function Overview**:
    This function scrapes the scholarship highlights, tables, and iframe links from a college webpage. It interacts with dynamically loaded content (such as clicking a "Read More" button) to retrieve additional information if present. The function supports verbose mode for detailed status output during execution.

    ### 🛠️ **Parameters**:
    - **url** *(str)*: The URL of the college webpage from which the scholarship information is to be fetched 🌍.
    - **verbose** *(bool)*: A flag to enable or disable verbose mode. If `True`, additional status messages are printed during the scraping process 📢.

    ### 🔧 **How It Works**:
    1. **Overlay Handling**: The function checks for potential overlay/pop-ups and attempts to close them if present to avoid click obstructions 🚫.
    2. **Read More Button**: Scrolls the "Read More" button into view and clicks it to reveal hidden content if applicable 📄.
    3. **Data Extraction**:
        - **Tables**: Scrapes scholarship-related table data from the page, excluding empty rows 🗃️.
        - **Paragraphs**: Scrapes paragraph content about scholarships, avoiding paragraphs nested inside tables ✍️.
        - **Iframes**: Extracts the URLs from all iframe elements present in the content (e.g., embedded videos or forms) 🎥.
    4. **Verbose Mode**: If `verbose=True`, prints additional information such as the start and end of the scraping process and the extracted content 🖥️.

    ### ✅ **Return Value**:
    - **output_data** *(dict)*: A dictionary containing the scraped data:
      ```python
      {
          'Table': [
              ['Row 1 Col 1', 'Row 1 Col 2', ...],
              ['Row 2 Col 1', 'Row 2 Col 2', ...]
          ],
          'Iframes': ['https://www.youtube.com/embed/example1', ...]
      }
      ```

    ### 💡 **Usage Example**:
    ```python
    # Fetch scholarship information and other data from a college page with verbose output
    url = 'https://www.shiksha.com/college/iit-madras-indian-institute-of-technology-adyar-chennai-3031/scholarships'
    output_data = fetch_scholarships(url, verbose=True)
    
    # Output will contain scholarship details, tables, and iframes from the page
    print(output_data)
    ```
    """
    
    driver.get(url)
    output_data = {}
    if verbose:
        start_verbose("College scholarship extraction", url)

    try:
        wait = WebDriverWait(driver, 10)
        sleep(0.2,  verbose, "Waiting for Scholarship page to load")

        content_div = driver.find_element(By.XPATH, """//*[@id="Overview"]/div/div/div""")

        tables = content_div.find_elements(By.TAG_NAME, "table")
        table_parents = set()
        table_data = []
        if tables:
            for table in tables:
                rows = table.find_elements(By.TAG_NAME, "tr")
                for row in rows:
                    cols = row.find_elements(By.TAG_NAME, "td")
                    row_data = [col.text for col in cols]
                    if row_data:
                        table_data.append(row_data)
                table_parents.add(table)

        output_data["Scolarship_Table"] = table_data if table_data else []

        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        iframe_list = [iframe.get_attribute("src") for iframe in iframes if iframe.get_attribute("src")]

        output_data["Iframes"] = iframe_list

    except Exception as e:
        print(f"Error: {e}")
        
    if verbose:
        end_verbose(output_data)
    
    return output_data

# url = 'https://www.shiksha.com/college/iit-madras-indian-institute-of-technology-adyar-chennai-3031/scholarships'
# fetch_scholarships(url, True)