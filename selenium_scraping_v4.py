import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to the CSV file containing college names
csv_file_path = 'college_names.csv'

# Set up Chrome options (optional, can be configured as needed)
chrome_options = Options()

# Provide the path to the ChromeDriver executable
service = Service('chromedriver')

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

            try:
                # Wait for the div elements containing the links to be present
                div_elements = WebDriverWait(browser, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.c8ff'))
                )

                # Flag to check if a relevant link was found
                relevant_link_found = False

                for div in div_elements:
                    link = div.find_element(By.TAG_NAME, 'a')
                    href_url = link.get_attribute('href')
                    
                    # Check if the college name is in the link text or URL
                    if college_name.lower() in link.text.lower() or college_name.lower() in href_url.lower():
                        print(f"College: {college_name}, URL: {href_url}")
                        relevant_link_found = True
                        break  # Exit the loop once a relevant link is found
                
                if not relevant_link_found:
                    # If no relevant link is found, skip the college
                    print(f"College: {college_name}, URL: not available")
            except Exception as e:
                print(f"Error processing {college_name}: {e}")
                print(f"College: {college_name}, URL: not available")
            
            print()  # Print a newline for separation between college results

# Call the function to perform the search and extraction for all college names in the CSV file
search_and_extract(csv_file_path)

# Close the browser when done
browser.quit()
