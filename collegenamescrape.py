from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Set up WebDriver options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless if you don't need to see the browser
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# Set up the WebDriver path
service = Service(executable_path='chromedriver.exe')  # Replace with your path to chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the specified URL
url = 'https://www.shiksha.com/colleges/tamil-nadu-3'
driver.get(url)

try:
    # Wait for the page to load
    time.sleep(10)  # Increase wait time to ensure the page fully loads

    # Debug: Save a screenshot of the page
    driver.save_screenshot('page_screenshot.png')

    # Print current URL and page title for debugging
    print(f"Current URL: {driver.current_url}")
    print(f"Page Title: {driver.title}")

    # Debug: Print the page source to verify content
    with open('page_source.html', 'w', encoding='utf-8') as file:
        file.write(driver.page_source)
    
    # Check if specific elements are present
    try:
        # Replace with appropriate XPath
        college_elements = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'ctpSrp-contnr')]"))
        )
        print("College names loaded")
    except Exception as e:
        print(f"Error locating college names: {e}")
        driver.quit()
        raise

    # Extract college names
    college_names = []
    for element in college_elements:
        college_names.append(element.text.strip())

    # Print extracted college names
    for name in college_names:
        print(name)

    # Optionally, save the results to a CSV file
    df = pd.DataFrame(college_names, columns=["College Name"])
    df.to_csv("college_names.csv", index=False)

finally:
    # Close the WebDriver
    driver.quit()
