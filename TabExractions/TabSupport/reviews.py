from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string
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

def generate_random_string(length=10):
    """Generate a random string of fixed length."""
    letters = string.ascii_letters  # Uppercase and lowercase letters
    return ''.join(random.choice(letters) for i in range(length))

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
            
            # Generate random data and fill the input box
            random_data = "Coimbatore Institute of Technology"  # Generate a random string of 10 characters
            search_input.send_keys(random_data)
            print(f"Random data entered into search box: {random_data}")
            break  # If successful, exit the retry loop

        except StaleElementReferenceException:
            attempts += 1
            print(f"Stale Element Reference Exception. Retrying {attempts}/{max_attempts}...")

    if attempts == max_attempts:
        print("Failed to interact with the search input field after several attempts.")

    
    time.sleep(10)
except Exception as e:
    print(f"Error: {e}")

# Close the browser after task completion
# driver.quit()
