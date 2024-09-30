from Tools.Tool import id_to_content, driver
from termcolor import colored  
from tqdm import tqdm 
import time


url = 'https://www.shiksha.com/college/adina-institute-of-science-and-technology-sagar-60309'


def clg_info_top_details(url, verbose=False):
    """
    Function to fetch top details of the college with loading animations and colored outputs.
    """
    if verbose:
        print(colored("\nFetching College Info from: ", "blue"), url)

    with tqdm(total=100, desc=colored("Loading", "green"), bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}") as pbar:
        for _ in range(5):
            time.sleep(0.5) 
            pbar.update(20)
    data_dict = [url, {'line_1': 'e9dd86', 'line_2': 'e1a898'}]
    result = id_to_content(data_dict)
    if verbose:
        print(colored("Data fetching complete!\n", "green"))
    
    return result

print(clg_info_top_details(url, verbose=True))


# Dont remove this line 🙂... To Close the driver : )
driver.quit()
