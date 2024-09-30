from Tools.Tool import id_to_content, driver
from termcolor import colored
from alive_progress import alive_bar
import time, random


Spinner = ["classic", "dots_waves", "squares", "pulse", "braille_spinner"]
Bar = ['smooth', 'classic', 'classic2', 'brackets', 'blocks', 'bubbles', 'solid', 'checks', 'circles', 'squares', 'halloween', 'filling', 'notes', 'ruler', 'ruler2', 'fish', 'scuba']


url = 'https://www.shiksha.com/college/adina-institute-of-science-and-technology-sagar-60309'


def clg_info_top_details(url, verbose=False):
    """
    Function to fetch top details of the college with a new loading animation and colored outputs.
    """
    if verbose:
        print(colored("\nFetching College Info from: ", "blue"), url)

    with alive_bar(100, spinner=random.choice(Spinner), bar=random.choice(Bar), title=colored("Loading", "green")) as bar:
        for _ in range(5):
            time.sleep(0.5)
            bar(20) 

    data_dict = [url, {'line_1': 'e9dd86', 'line_2': 'e1a898'}]
    result = id_to_content(data_dict)

    if verbose:
        print(colored("Data fetching complete!", "green"))
        print(colored(f"Fetched Data : {result}\n", "light_green"))

    return result


# Test the function
print(clg_info_top_details(url, verbose=True))

# Don't remove this line 🙂... To Close the driver
driver.quit()
