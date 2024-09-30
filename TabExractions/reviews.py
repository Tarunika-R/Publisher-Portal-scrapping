from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import StaleElementReferenceException

# Set the correct path to ChromeDriver
chrome_driver_path = "chromedriver.exe"  # Replace with the actual path to your chromedriver

# Initialize Service object
service = Service(chrome_driver_path)

# Start the WebDriver using the service object
driver = webdriver.Chrome(service=service)

# Open the website
driver.get("https://zollege.in/")

# Wait for the page to load
time.sleep(3)

def get_first_search_result(driver):
    try:
        # Locate the search result box using the provided XPath
        search_result_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/header/div/div[2]/div[2]/div/div[2]/div/div'))
        )
        
        # Find all the <a> tags inside the result box
        a_tags = search_result_box.find_elements(By.TAG_NAME, "a")
        
        if a_tags:
            # Return the first <a> tag (0th index)
            first_result = a_tags[0]
            return first_result.get_attribute('href')  # Return the URL from the first <a> tag
        else:
            print("No <a> tags found in the search result box.")
            return None

    except Exception as e:
        print(f"Error while fetching the search result: {e}")
        return None

try:
    attempts = 0
    max_attempts = 5  # Set a limit for the retry attempts

    while attempts < max_attempts:
        try:
            # Locate the search input field using the placeholder attribute
            search_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Search for colleges, Courses, Exams, Q&A or Articles…"]'))
            )
            
            # Click the search input field to activate it
            search_input.click()
            print("Search input field clicked successfully.")
            
            # Input the text you want to search for
            search_text = "Coimbatore Institute of Technology"  # The search term
            search_input.send_keys(search_text)
            print(f"Search term entered: {search_text}")
            break  # If successful, exit the retry loop

        except StaleElementReferenceException:
            attempts += 1
            print(f"Stale Element Reference Exception. Retrying {attempts}/{max_attempts}...")

    if attempts == max_attempts:
        print("Failed to interact with the search input field after several attempts.")
    
    # Wait for search results to load
    time.sleep(3)  # Adjust the sleep time based on how long the results take to load

    # Get the URL of the first search result
    first_url = get_first_search_result(driver)

    if first_url:
        print(f"First search result URL: {first_url}")
    else:
        print("No search result found.")

    # Optionally, add a delay before closing the browser
    time.sleep(5)

except Exception as e:
    print(f"Error: {e}")

# Close the browser after task completion
driver.quit()
