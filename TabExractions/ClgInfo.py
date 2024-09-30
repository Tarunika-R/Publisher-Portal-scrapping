from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
options = Options()
# Uncomment if you want to run in headless mode
# options.add_argument('--headless')

driver = webdriver.Chrome(options=options)

def id_to_content(data: dict):
    """
    This function extracts content based on the provided dictionary.
    The dictionary should contain the URL as the first element and 
    a mapping of key-value pairs where the value is the class name.
    Example:
    Inp_parameter: [url, {'line_1': 'e9dd86', 'line_2': 'e1a898'}]
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



url = 'https://www.shiksha.com/college/adina-institute-of-science-and-technology-sagar-60309'
data_dict = [url, {'line_1': 'e9dd86', 'line_2': 'e1a898'}]

result = id_to_content(data_dict)
print(result)

driver.quit()
