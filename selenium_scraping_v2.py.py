import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Path to the CSV file containing college names
csv_file_path = 'Colleges_Dataset.csv'

# Set up Chrome options (optional, can be configured as needed)
chrome_options = Options()

# Provide the path to the ChromeDriver executable
service = Service('C:/Users/Hema/Desktop/taru/Publisher Portal/chromedriver.exe')

# Initialize the Chrome WebDriver with the specified service and options
browser = webdriver.Chrome(service=service, options=chrome_options)

# Function to search each college name from the CSV file
def search_college_names(csv_file_path):
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
            
            # Loop for pagination, use 0 to start from the first page
            for i in range(1):  # Adjust the range as needed for multiple pages
                # Correct URL formation for pagination (i * 10 for each page)
                url = f"https://www.shiksha.com/search?q={query}&start={i * 10}"
                # Open the search URL in the browser
                browser.get(url)

                # Wait for a few seconds to load the page
                time.sleep(3)

                # Extract the titles of the search results
                search_results = browser.find_elements(By.CSS_SELECTOR, 'h3')

                # Print out the titles of the search results
                print(f"Results for {college_name}:")
                for result in search_results:
                    print(result.text)
                print()  # Print a newline for separation between college results

    # Close the browser when done
    browser.quit()

# Call the function to perform the search for all college names in the CSV file
search_college_names(csv_file_path)
