"""
on giving link it gives all the links available
"""

from selenium import webdriver        
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Provide the URL containing the full list of colleges
url = "https://www.shiksha.com/mba/colleges/mba-colleges-bangalore"  # Replace with the actual URL

# Set up Chrome options (optional, can be configured as needed)
chrome_options = Options()

# Provide the path to the ChromeDriver executable
service = Service('chromedriver.exe')

# Initialize the Chrome WebDriver with the specified service and options
browser = webdriver.Chrome(service=service, options=chrome_options)

# Open the URL in the browser
browser.get(url)

# Wait for a few seconds to load the page
time.sleep(5)

# Initialize WebDriverWait
wait = WebDriverWait(browser, 10)

# Keep track of already visited URLs to avoid duplicates
extracted_urls = set()

# Function to extract all college URLs
def extract_all_college_urls():
    try:
        # Wait until all the college links are present
        college_links = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'a')))
        
        for link in college_links:
            href_url = link.get_attribute('href')
            # You can add a filter to ensure only relevant links are extracted, e.g., if they contain 'college'
            if href_url and 'college' in href_url and href_url not in extracted_urls:
                extracted_urls.add(href_url)
                print(f"College URL: {href_url}")
    except TimeoutException:
        print("Timeout: No college links found.")

# Extract all the college URLs
extract_all_college_urls()

# Output all the extracted URLs at the end
print("\nAll extracted college URLs:")
for url in extracted_urls:
    print(url)

print(len(url))
# Close the browser when done
browser.quit()
