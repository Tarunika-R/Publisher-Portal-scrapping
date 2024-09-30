from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set the correct path to ChromeDriver
chrome_driver_path = "chromedriver.exe"

# Initialize Service object
service = Service(chrome_driver_path)

# Start the WebDriver using the service object
driver = webdriver.Chrome(service=service)

# Open the website
driver.get("https://zollege.in/")

# Wait for the page to load completely
time.sleep(3)

try:
    # Locate the search input field by using the 'placeholder' attribute
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Search for colleges, Courses, Exams, Q&A or Articles…"]'))
    )
    
    # Click the search input field to activate it
    search_input.click()

    # Enter the search term (e.g., 'engineering')
    search_input.send_keys("engineering")  # You can change the search term as needed
    print("Search term entered successfully.")

except Exception as e:
    print(f"Error: {e}")

# Close the browser
# driver.quit()
