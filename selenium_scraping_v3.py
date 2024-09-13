import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Path to the CSV file containing college names
csv_file_path = 'college_names.csv'

# Set up Chrome options (optional, can be configured as needed)
chrome_options = Options()

# Provide the path to the ChromeDriver executable
service = Service('chromedriver.exe')

# Initialize the Chrome WebDriver with the specified service and options
browser = webdriver.Chrome(service=service, options=chrome_options)

# Function to search and extract data for each college
def search_and_extract(csv_file_path):
    # Open and read the CSV file
    with open(csv_file_path, newline='') as csvfile:
        # Initialize a CSV reader
        csv_reader = csv.DictReader(csvfile)  # Use DictReader to access columns by name
        
        # Loop through each row in the CSV
        for row in csv_reader:
            # Get the college name from the 'name' column
            college_name = row['name']
            
            # Replace spaces with '+' for the search query
            query = college_name.replace(' ', '+')
            
            # Construct the search URL
            url = f"https://www.shiksha.com/search?q={query}"
            
            # Open the search URL in the browser
            browser.get(url)

            # Wait for a few seconds to load the page
            time.sleep(3)

            # Extract the <div> elements that contain the links
            div_elements = browser.find_elements(By.CSS_SELECTOR, 'div.c8ff')  # Adjust this selector if necessary

            # Iterate through the div elements and extract widget label and URLs
            print(f"Results for {college_name}:")
            for div in div_elements:
                try:
                    # Select the <a> tag inside the <div>
                    link = div.find_element(By.TAG_NAME, 'a')
                    # Extract the widget label and URL
                    widget_label = link.get_attribute('widgetspecificlabel')
                    href_url = link.get_attribute('href')
                    print(f"College: {widget_label}, URL: {href_url}")
                except Exception as e:
                    print(f"Error extracting data for {college_name}: {e}")
            print()  # Print a newline for separation between college results

# Call the function to perform the search and extraction for all college names in the CSV file
search_and_extract(csv_file_path)

# Close the browser when done
browser.quit()
