from .Tools.Tool import ( id_to_content, driver, start_verbose, end_verbose, sleep)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


url = 'https://www.shiksha.com/college/adina-institute-of-science-and-technology-sagar-60309'

def clg_info_top_details(url: str, verbose=False) ->  dict:
    """
    ### 📑 **Function Overview**:
    This function fetches the top details of a college from the provided URL. It includes a loading animation 🌀 and uses colored outputs for enhanced user experience.
    ### 🛠️ **Parameters**:
    - **url** *(str)*: The URL of the college webpage from which the information is to be fetched 🌍.
    - **verbose** *(bool, optional)*: A flag to enable or disable verbose mode. If `True`, additional status messages are printed during execution 📢.
      - Default: `False`

    ### 🔧 **How it Works**:
    1. **Loading Animation**: The function shows a loading animation using random spinners and progress bars 🎛️ from pre-defined sets.
    2. **Scraping Data**: It extracts the relevant college information such as the name, address, and other details using class names 🏷️ from the webpage’s HTML structure.
    3. **Verbose Mode**: If enabled, the function prints information about the start of the operation and the extracted data 📋.
    ### 💡 **Usage Example**:
    ```python
    # Example of usage with verbose mode enabled
    college_info = clg_info_top_details("https://example.com/college-page", verbose=True)
    ```
    ### ✅ **Return Value**:
    - **result** *(dict)*: A dictionary containing the extracted data from the webpage in the following structure:
      ```python
      {
        'ClgName': 'Example College Name',
        'Details_1': ['Detail 1', 'Detail 2', ...],
        'Details_2': ['Detail A', 'Detail B', ...]
      }
      ```
    """
    
    if verbose:
        start_verbose("clg_info_top_details", url)
        
    # sleep(0.5, verbose)
    
    data_dict = [url, {'ClgName':'e70a13', 'Details_1': 'e9dd86', 'Details_2': 'e1a898'}]
    driver.get(data_dict[0])
    
    result = id_to_content(data_dict)

    if verbose:
        end_verbose(result)

    return result



def fetch_college_highlights(url, verbose):
    """
    ### 📑 **Function Overview**:
    This function scrapes the highlights, tables, and iframe links from a college webpage. It interacts with dynamically loaded content (such as clicking a "Read More" button) to retrieve additional information if present. The function supports verbose mode for detailed status output during execution.

    ### 🛠️ **Parameters**:
    - **url** *(str)*: The URL of the college webpage from which the information is to be fetched 🌍.
    - **verbose** *(bool)*: A flag to enable or disable verbose mode. If `True`, additional status messages are printed during the scraping process 📢.

    ### 🔧 **How It Works**:
    1. **Overlay Handling**: The function checks for potential overlay/pop-ups and attempts to close them if present to avoid click obstructions 🚫.
    2. **Read More Button**: Scrolls the "Read More" button into view and clicks it to reveal hidden content 📄.
    3. **Data Extraction**:
        - **Tables**: Scrapes table data from the page, excluding empty rows 🗃️.
        - **Paragraphs**: Scrapes paragraph content, avoiding paragraphs nested inside tables ✍️.
        - **Iframes**: Extracts the URLs from all iframe elements present in the content (e.g., embedded YouTube videos) 🎥.
    4. **Verbose Mode**: If `verbose=True`, prints additional information such as the start and end of the scraping process and the extracted content 🖥️.

    ### ✅ **Return Value**:
    - **output_data** *(dict)*: A dictionary containing the scraped data:
      ```python
      {
          'Highlights': 'Content from the page...',
          'Table': [
              ['Row 1 Col 1', 'Row 1 Col 2', ...],
              ['Row 2 Col 1', 'Row 2 Col 2', ...]
          ],
          'Iframes': ['https://www.youtube.com/embed/example1', ...]
      }
      ```

    ### 💡 **Usage Example**:
    ```python
    # Fetch highlights and other data from a college page with verbose output
    url = 'https://www.shiksha.com/college/adina-institute-of-science-and-technology-sagar-60309'
    output_data = fetch_college_highlights(url, verbose=True)
    
    # Output will contain highlights, tables, and iframes from the page
    print(output_data)
    ```
    """
    
    driver.get(url)
    output_data = {}
    if verbose:
        start_verbose("IN College Info fetching highlights", url)

    try:
        wait = WebDriverWait(driver, 10)
        
        try:
            overlay_close_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "close-popup")))
            overlay_close_button.click()
            print("Closed overlay popup")
        except Exception as e:
            print("No overlay found:", str(e))

        read_more = wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@id="ovp_section_highlights"]/div[2]/div[1]/div/span""")))
        
        driver.execute_script("arguments[0].scrollIntoView();", read_more)
        time.sleep(3)
        try:
            driver.execute_script("arguments[0].click();", read_more)
            sleep(0.5, verbose, "Waiting for highlights to load")
        except Exception as e:
            print(f"Error clicking 'Read More' with JS: {e}")
        
        content_div = driver.find_element(By.XPATH, """//*[@id="ovp_section_highlights"]/div[2]/div[1]/div/div/div/div""")

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

            output_data['Highlights'] = total_para if total_para else "Content Not Found :\\"

        output_data["Table"] = table_data if table_data else []

        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        iframe_list = [iframe.get_attribute("src") for iframe in iframes if iframe.get_attribute("src")]

        output_data["Iframes"] = iframe_list

    except Exception as e:
        print(f"Error: {e}")
        
    if verbose:
        end_verbose(output_data)
    
    return output_data




# Test the function
# fetch_college_highlights(url, True)
# clg_info_top_details(url, True)

# # Don't remove this line 🙂... To Close the driver
# driver.quit()
