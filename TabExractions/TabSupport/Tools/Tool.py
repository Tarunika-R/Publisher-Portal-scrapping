from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from termcolor import colored
import random, time
from alive_progress import alive_bar
from selenium.common.exceptions import StaleElementReferenceException


# Design Variables
Spinner = ['classic', 'stars', 'twirl', 'twirls', 'horizontal', 'vertical', 'waves', 'waves2', 'waves3', 'dots', 'dots_waves', 'dots_waves2', 'it', 'ball_belt', 'balls_belt', 'triangles', 'brackets', 'bubbles', 'circles', 'squares', 'flowers', 'elements', 'loving', 'notes', 'notes2', 'arrow', 'arrows', 'arrows2', 'arrows_in', 'arrows_out', 'radioactive', 'boat', 'fish', 'fish2', 'fishes', 'crab', 'alive', 'wait', 'wait2', 'wait3', 'wait4', 'pulse']
Bar = ['smooth', 'classic', 'classic2', 'brackets', 'blocks', 'bubbles', 'solid', 'checks', 'circles', 'squares', 'halloween', 'filling', 'notes', 'ruler', 'ruler2', 'fish', 'scuba']


# Set up Chrome options
options = Options()
# options.add_argument('--disable-http2')
driver = webdriver.Chrome(options=options)

def id_to_content(data: dict):
    """
    📄 **Function Overview**:
    This function extracts content based on the provided dictionary. 
    The dictionary should contain the URL as the first element 🌐 and a mapping of key-value pairs where the value is the class name 🏷️.

    ✨ **How it works**:
    1. The function navigates to the URL 🌍.
    2. Extracts data from elements based on the provided class names 🔍.
    3. Returns the data in a structured format 📦.

    📥 **Input Parameters**:
    - **url**: The webpage URL from which content needs to be extracted 🔗.
    - **class name mapping**: A dictionary where keys represent names of the content to extract, and values represent the class names from which content is pulled 🏷️.

    💡 **Example**:
    ```python
    [url, {'line_1': 'e9dd86', 'line_2': 'e1a898'}]
    ```
    In this example:
    - `line_1`: The data associated with the class name `e9dd86` will be extracted.
    - `line_2`: The data associated with the class name `e1a898` will be extracted.

    ✅ **Output**:
    The function returns a dictionary with the content extracted from the specified class names 📝.

    """
    try:
        
        out_data = {} 

        for key, val in data[1].items():
            elements = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, val))
            )

            data_id = []
            for element in elements:
                data_id.extend(element.text.split("\n"))  
            out_data[key] = data_id  

        return out_data  

    except Exception as e:
        return {'msg': f"Error in Scraping: {str(e)}"} 


# Design Functions

def start_verbose(function_name, url):
    """
    ### 📑 **Function Overview**:
    This function prints a starting message for verbose mode, indicating the beginning of the execution of a function along with the provided URL.

    ### 🛠️ **Parameters**:
    - **function_name** *(str)*: The name of the function that is being executed 🛠️.
    - **url** *(str)*: The URL that is being fetched or processed 🌍.

    ### ✅ **Output**:
    - Prints a message to the console with the function name and URL in a colorful format.
    
    ### 💡 **Usage Example**:
    ```python
    start_verbose("fetch_college_highlights", "https://example.com")
    ```

    ### 📥 **Example Output**:
    ```text
    🦄 Function: Running 'fetch_college_highlights()'
    Fetching College Info from:  https://example.com ✨
    ```

    ### 📘 **Notes**:
    - This function is typically called at the start of a verbose-enabled process to inform the user about the current operation.
    - The output is colored using the `termcolor` package to enhance readability and user experience.
    """
    print(colored(f"\n🦄 Function: Running '{function_name}()'", "magenta"))
    print(colored("Fetching College Info from: ", "blue"), colored(url+" ✨", "light_yellow"))


def fetch_menu_tabs(url: str, verbose=False) -> list:
    """
    📑 **Function Overview**:
    This function navigates to the provided URL and fetches the tab menu items present on the webpage.

    ### 🛠️ **Parameters**:
    - **url** *(str)*: The URL of the webpage from which the menu tabs are to be fetched.

    ### ✅ **Return**:
    - **tabs** *(list)*: A list of strings representing the text of each menu tab found on the page.

    ### 💡 **Usage Example**:
    ```python
    url = "https://www.shiksha.com/college/shri-shiv-mahavidyalaya-ghazipur-183029"
    tabs = fetch_menu_tabs(url)
    print(tabs)
    ```

    ### 📥 **Return Example**:
    ```python
    ['Overview', 'Courses', 'Reviews', 'Admissions', 'Placements', ...]
    ```

    ### 📝 **Process**:
    - The function waits for the tab menu to be present on the page.
    - It then collects all the text from the menu items and returns them as a list.
    """
    if verbose:
        start_verbose("fetch_menu_tabs", url)
        print(colored("Started Tabs Fetching from the given link 📑", 'light_magenta'))
    
    try:
        driver.get(url)
        tabs = []
        
        # Wait for the menu to be present on the page
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#main-wrapper > div.b876.three_col.uilp.reverse_two_col > div > div > ul"))
        )
        
        # Find the menu items and extract their text
        menu_items = driver.find_elements(By.CSS_SELECTOR, "#main-wrapper > div.b876.three_col.uilp.reverse_two_col > div > div > ul")
        for item in menu_items:
            tabs = item.text.split('\n')
    except:
        pass
    
    if verbose:
        end_verbose(tabs)
    return tabs



def end_verbose(result):
    """
    ### 📑 **Function Overview**:
    This function prints a concluding message for verbose mode, signaling the completion of a function execution and displaying the fetched data.

    ### 🛠️ **Parameters**:
    - **result** *(dict)*: The dictionary containing the data that was fetched during the function's execution.

    ### ✅ **Output**:
    - Prints a message indicating that the data fetching is complete.
    - Displays the fetched data in a well-formatted and colorful manner.

    ### 💡 **Usage Example**:
    ```python
    end_verbose({"Highlights": "Example content", "Table": []})
    ```

    ### 📥 **Example Output**:
    ```text
    🚀 Data fetching complete!
    📤 Fetched Data : 
    {'Highlights': 'Example content', 'Table': []}
    ```

    ### 📘 **Notes**:
    - This function is typically called at the end of a verbose-enabled process to inform the user about the completion of data fetching and to display the final result.
    - The result is printed in a colorful format using the `termcolor` package to improve readability.
    """

    print(colored("🚀 Data fetching complete!", "green"))
    print(colored(f"📤 Fetched Data : \n{result}\n", "light_yellow"))
    
def sleep(time_duration, verbose=False, msg="🔃 Loading"):
    """
    ### 📑 **Function Overview**:
    This function introduces a delay in the execution, optionally displaying a loading animation when verbose mode is enabled.

    ### 🛠️ **Parameters**:
    - **time_duration** *(float)*: The duration of time (in seconds) for which the function will sleep or delay execution 🕒.
    - **verbose** *(bool, optional)*: A flag to control whether the function should display a loading animation 📊.
      - Default: `False`
    - **msg** *(str, optional)*: A custom message to display with the loading animation when verbose mode is enabled 🎛️.
      - Default: `"🔃 Loading"`

    ### ✅ **Output**:
    - If `verbose=True`, the function shows a progress bar and a loading spinner for the specified duration.
    - If `verbose=False`, the function simply sleeps for the specified time without any visual output.

    ### 💡 **Usage Example**:
    ```python
    sleep(1.5, verbose=True, msg="Fetching data")
    ```

    ### 📥 **Example Output (Verbose Mode)**:
    ```text
    🔃 Loading |████████████████████| 100/100 [100%] in 1.5s (10.67/s)
    ```

    ### 📝 **How It Works**:
    - **Verbose Mode**: If `verbose` is enabled, the function uses `alive_bar` to show a progress bar with a random spinner and progress bar style. The bar is updated at regular intervals.
    - **Non-Verbose Mode**: If `verbose` is disabled, it simply waits for the specified `time_duration`.

    ### ⚙️ **Internal Behavior**:
    - The progress bar advances in increments, updating every `time_duration / 5` seconds. 
    - The loading animation uses random spinners and progress bars from the `Spinner` and `Bar` sets to keep the animation dynamic.

    ### 📘 **Notes**:
    - This function is useful for introducing a delay in processes that require time to complete or simulate waiting during web scraping.
    - The `alive_bar` package is used for the loading animation and can be customized with different spinners and bar styles.
    """
    if verbose:
        with alive_bar(100, spinner=random.choice(Spinner), bar=random.choice(Bar), title=colored(msg, "green")) as bar:
            for _ in range(5):
                time.sleep(time_duration)
                bar(20) 
    else:
        time.sleep(time_duration)
    
    
            
    

def get_first_search_result_url(search_term, verbose):
    if verbose:
        start_verbose("get_first_search_result_url", "Search term: "+search_term)
    try:
        driver.get("https://zollege.in/")

        time.sleep(3)

        def get_first_search_result(driver):
            try:
                search_result_box = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/header/div/div[2]/div[2]/div/div[2]/div/div'))
                )

                a_tags = search_result_box.find_elements(By.TAG_NAME, "a")

                if a_tags:
                    first_result = a_tags[0]
                    if verbose:
                        end_verbose(first_result.get_attribute('href') )
                    return first_result.get_attribute('href')  
                else:
                    if verbose:
                        print("❌ No <a> tags found in the search result box.")
                    return None

            except Exception as e:
                if verbose:
                    print(f"❌ Error while fetching the search result: {e}")
                return None

        attempts = 0
        max_attempts = 5  

        while attempts < max_attempts:
            try:
                search_input = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Search for colleges, Courses, Exams, Q&A or Articles…"]'))
                )

                search_input.click()
                if verbose:
                    print(colored("✅ Search input field clicked successfully.", "green"))

                search_input.send_keys(search_term)
                if verbose:
                    print(colored(f"✅ Search term entered: {search_term}" ,"green"))
                break 

            except StaleElementReferenceException:
                attempts += 1
                if verbose:
                    print(colored(f"🔃 Stale Element Reference Exception. Retrying {attempts}/{max_attempts}...","light_magenta"))

        if attempts == max_attempts:
            if verbose:
                print("❌ Failed to interact with the search input field after several attempts.")
            return None

        time.sleep(3)
        first_url = get_first_search_result(driver)

        if first_url:
            return first_url
        else:
            if verbose:
                print("❌ No search result found.")
            return None

    except Exception as e:
        if verbose:
            print(f"❌ Error: {e}")
        return None
