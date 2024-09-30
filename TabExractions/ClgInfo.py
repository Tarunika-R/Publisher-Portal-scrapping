from Tools.Tool import ( id_to_content, driver, start_verbose, end_verbose, Spinner, Bar)
from alive_progress import alive_bar
import time, random
from termcolor import colored

url = 'https://www.shiksha.com/college/adina-institute-of-science-and-technology-sagar-60309'

def clg_info_top_details(url, verbose=False):
    """
    Function to fetch top details of the college with a new loading animation and colored outputs.
    """
    if verbose:
        start_verbose("clg_info_top_details", url)
        
    with alive_bar(100, spinner=random.choice(Spinner), bar=random.choice(Bar), title=colored("🔃 Loading", "green")) as bar:
        for _ in range(5):
            time.sleep(0.5)
            bar(20) 
    data_dict = [url, {'line_1': 'e9dd86', 'line_2': 'e1a898'}]
    result = id_to_content(data_dict)

    if verbose:
        end_verbose(result)

    return result


# Test the function
clg_info_top_details(url, verbose=True)

# Don't remove this line 🙂... To Close the driver
driver.quit()
