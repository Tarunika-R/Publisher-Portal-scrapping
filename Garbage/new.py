"""
this code is able to extarct the college's url with ref code 
but  not able to click the 'LOAD MORE COLLEGES option
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException
import time

# Prompt user for topic to search
topic_search = input("Enter the college name or topic to search: ")

# Replace spaces with '+' for the search query
topic_search = topic_search.replace(' ', '+')

# Set up Chrome options (optional, can be configured as needed)
chrome_options = Options()

# Provide the path to the ChromeDriver executable
service = Service('C:/Users/Hema/Desktop/taru/Publisher Portal/chromedriver.exe')

# Initialize the Chrome WebDriver with the specified service and options
browser = webdriver.Chrome(service=service, options=chrome_options)

# Open the search URL in the browser
url = f"https://www.shiksha.com/search?q={topic_search}"
browser.get(url)

# Wait for a few seconds to load the page
time.sleep(3)

# Initialize WebDriverWait
wait = WebDriverWait(browser, 10)

# Keep track of already visited URLs to avoid duplicates
extracted_urls = set()

# Function to extract URLs
def extract_urls():
    try:
        search_results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.c8ff')))
        for result in search_results:
            try:
                link = result.find_element(By.TAG_NAME, 'a')
                href_url = link.get_attribute('href')
                if href_url not in extracted_urls:
                    extracted_urls.add(href_url)
                    print(f"College URL: {href_url}")
            except Exception as e:
                print(f"Error extracting URL: {e}")
    except TimeoutException:
        print("Timeout: No search results found.")
    except StaleElementReferenceException:
        print("Encountered StaleElementReferenceException. Retrying...")

# Scroll function to load more colleges
def scroll_down():
    last_height = browser.execute_script("return document.body.scrollHeight")
    
    while True:
        # Scroll down to the bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Wait for new colleges to load
        time.sleep(3)

        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")
        
        # If no new content is loaded, exit the loop
        if new_height == last_height:
            break
        last_height = new_height

# Scroll down to load all colleges
scroll_down()

# After all colleges have been loaded, extract URLs
extract_urls()

# Output all the extracted URLs at the end
print("\nAll extracted college URLs:")
for url in extracted_urls:
    print(url)

# Close the browser when done
browser.quit()
