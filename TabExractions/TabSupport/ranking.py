from .Tools.Tool import ( id_to_content, driver, start_verbose, end_verbose, sleep)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def extract_ranking_info(url, verbose):
    """
    ### 📑 **Function Overview**:
    This function scrapes hostel and infrastructure details from a college webpage. It interacts with dynamically loaded content (such as clicking a "Read More" button) to retrieve additional information if present. The function supports verbose mode for detailed status output during execution.

    ### 🛠️ **Parameters**:
    - **url** *(str)*: The URL of the college webpage from which the hostel and infrastructure information is to be fetched 🌍.
    - **verbose** *(bool)*: A flag to enable or disable verbose mode. If `True`, additional status messages are printed during the scraping process 📢.

    ### 🔧 **How It Works**:
    1. **Overlay Handling**: The function checks for potential overlay/pop-ups and attempts to close them if present to avoid click obstructions 🚫.
    2. **Read More Button**: Scrolls the "Read More" button into view and clicks it to reveal hidden content, including hostel and infrastructure information 🏢.
    3. **Data Extraction**:
        - **Hostel Details**: Scrapes information about hostel facilities, including rooms, fees, and availability 🛏️.
        - **Infrastructure Details**: Extracts details related to campus infrastructure, such as libraries, labs, sports facilities, and common areas 🏫.
        - **Paragraphs**: Scrapes paragraph content, avoiding paragraphs nested inside tables ✍️.
        - **Iframes**: Extracts the URLs from all iframe elements present in the content (e.g., embedded YouTube videos of hostel tours or infrastructure walkthroughs) 🎥.
    4. **Verbose Mode**: If `verbose=True`, prints additional information such as the start and end of the scraping process and the extracted content 🖥️.

    ### ✅ **Return Value**:
    - **output_data** *(dict)*: A dictionary containing the scraped hostel and infrastructure data:
      ```python
      {
          'Hostel_Details': 'Information about hostel facilities...',
          'Infrastructure_Details': 'Details about the campus infrastructure...',
          'Iframes': ['https://www.youtube.com/embed/example1', ...]
      }
      ```

    ### 💡 **Usage Example**:
    ```python
    # Fetch hostel and infrastructure details from a college page with verbose output
    url = 'https://www.shiksha.com/college/adina-institute-of-science-and-technology-sagar-60309'
    output_data = fetch_college_hostel_infrastructure(url, verbose=True)
    
    # Output will contain hostel details, infrastructure details, and iframe links from the page
    print(output_data)
    ```
"""

    
    driver.get(url)
    output_data = {}
    if verbose:
        start_verbose("IN College Ranking Extraction", url)

    try:
        wait = WebDriverWait(driver, 10)
        sleep(0.2,  verbose, "Waiting for Ranking page to load")

        content_div = driver.find_element(By.XPATH, """//*[@id="rp_section_highlights"]""")

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

        paragraphs = content_div.find_elements(By.TAG_NAME, "p")
        total_para = ""
        if paragraphs:
            for paragraph in paragraphs:
                is_inside_table = False
                for table_parent in table_parents:
                    if table_parent in paragraph.find_elements(By.XPATH, "./ancestor::*"):
                        is_inside_table = True
                        break

                if not is_inside_table:
                    total_para += paragraph.text + "\n"

            output_data['Ranking_Highlights'] = total_para if total_para else "Content Not Found :\\"

        output_data["Ranking_Table"] = table_data if table_data else []

        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        iframe_list = [iframe.get_attribute("src") for iframe in iframes if iframe.get_attribute("src")]

        output_data["Iframes"] = iframe_list

    except Exception as e:
        print(f"Error: {e}")
        
    if verbose:
        end_verbose(output_data)
    
    return output_data

# url = 'https://www.shiksha.com/college/iit-madras-indian-institute-of-technology-adyar-chennai-3031/ranking'
# extract_ranking_info(url, True)