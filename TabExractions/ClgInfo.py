from Tools.Tool import ( id_to_content, driver, start_verbose, end_verbose, Spinner, Bar)
from alive_progress import alive_bar
import time, random
from termcolor import colored

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
        
    with alive_bar(100, spinner=random.choice(Spinner), bar=random.choice(Bar), title=colored("🔃 Loading", "green")) as bar:
        for _ in range(5):
            time.sleep(0.5)
            bar(20) 
    data_dict = [url, {'ClgName':'e70a13', 'Details_1': 'e9dd86', 'Details_2': 'e1a898'}]
    result = id_to_content(data_dict)

    if verbose:
        end_verbose(result)

    return result







# Test the function
clg_info_top_details(url, verbose=True)

# Don't remove this line 🙂... To Close the driver
driver.quit()
