"""Gets input from user and then extracts data from the search related words."""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Prompt user for topic to search
topic_search = input("Enter the topic to search: ")

# Replace spaces with '+' for the search query
topic_search = topic_search.replace(' ', '+')

# Set up Chrome options (optional, can be configured as needed)
chrome_options = Options()

# Provide the path to the ChromeDriver executable
service = Service('chromedriver.exe')

# Initialize the Chrome WebDriver with the specified service and options
browser = webdriver.Chrome(service=service, options=chrome_options)

# Loop for pagination, use 0 to start from the first page
for i in range(1):  # Adjust the range as needed for multiple pages
    # Correct URL formation for pagination (i * 10 for each page)
    url = f"https://www.shiksha.com/search?q={topic_search}&start={i * 10}"
    # Open the search URL in the browser
    browser.get(url)

    # Wait for a few seconds to load the page
    time.sleep(3)

    # Extract the titles of the search results
    search_results = browser.find_elements(By.CSS_SELECTOR, 'h3')

    # Print out the titles of the search results
    for result in search_results:
        print(result.text)

# Wait for a while to keep the browser open
time.sleep(10)  # Adjust this as needed to see the results

# Close the browser when done
browser.quit()