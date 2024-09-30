from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from termcolor import colored

# Design Variables
Spinner = ['classic', 'stars', 'twirl', 'twirls', 'horizontal', 'vertical', 'waves', 'waves2', 'waves3', 'dots', 'dots_waves', 'dots_waves2', 'it', 'ball_belt', 'balls_belt', 'triangles', 'brackets', 'bubbles', 'circles', 'squares', 'flowers', 'elements', 'loving', 'notes', 'notes2', 'arrow', 'arrows', 'arrows2', 'arrows_in', 'arrows_out', 'radioactive', 'boat', 'fish', 'fish2', 'fishes', 'crab', 'alive', 'wait', 'wait2', 'wait3', 'wait4', 'pulse']
Bar = ['smooth', 'classic', 'classic2', 'brackets', 'blocks', 'bubbles', 'solid', 'checks', 'circles', 'squares', 'halloween', 'filling', 'notes', 'ruler', 'ruler2', 'fish', 'scuba']


# Set up Chrome options
options = Options()
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
        driver.get(data[0])
        
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
    print(colored(f"\n🦄 Function: Running '{function_name}()'", "magenta"))
    print(colored("Fetching College Info from: ", "blue"), colored(url+" ✨", "light_yellow"))

def end_verbose(result):
    print(colored("🚀 Data fetching complete!", "green"))
    print(colored(f"📤 Fetched Data : {result}\n", "light_yellow"))