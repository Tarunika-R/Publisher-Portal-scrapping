import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome WebDriver with headless mode
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Optional: Run in headless mode for faster scraping
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Load the page
url = "https://www.shiksha.com/college/iit-madras-indian-institute-of-technology-adyar-chennai-3031"
driver.get(url)

# Read the input JSON file
with open('C:/Users/Admin/Documents/Work/XtraCut_Works/Publisher-Portal-scrapping/XPaths.json', 'r') as file:
    json_data = json.load(file)

# Dictionary to store extracted data
extracted_data = {}

# Iterate through the JSON and extract text for each XPath
for section, items in json_data['IIT-Madras'].items():
    extracted_data[section] = []
    for item in items:
        xpath = item['XPath']
        try:
            # Wait for the element to be present and extract its text
            element_present = EC.presence_of_element_located((By.XPATH, xpath))
            WebDriverWait(driver, 10).until(element_present)
            element = driver.find_element(By.XPATH, xpath)
            extracted_data[section].append({'XPath': xpath, 'Text': element.text})
        except Exception as e:
            # Handle any exceptions (e.g., element not found)
            print(f"Error extracting {section} - {xpath}: {e}")
            extracted_data[section].append({'XPath': xpath, 'Text': 'N/A', 'Error': str(e)})

# Close the WebDriver
driver.quit()

# Write the extracted data to a new JSON file
with open('extracted_data.json', 'w') as outfile:
    json.dump(extracted_data, outfile, indent=4)

print("Data extraction completed. Saved to 'extracted_data.json'.")
