from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set the correct path to ChromeDriver
chrome_driver_path = r"C:/Users/Hema/Documents/taru/PP scrapping/Publisher-Portal-scrapping/chromedriver.exe"

# Initialize Service object
service = Service(chrome_driver_path)

# Start the WebDriver using the service object
driver = webdriver.Chrome(service=service)

# Define an explicit wait for the driver
wait = WebDriverWait(driver, 10)

# Open the website
driver.get("https://www.shiksha.com/college/iit-madras-indian-institute-of-technology-adyar-chennai-3031")
time.sleep(3)  # Wait for the page to load

# Click the "Read More" button
try:
    # Locate and click the "Read More" button with WebDriverWait
    read_more = wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@id="ovp_section_admission_dates"]/div[2]/div[1]/div/span""")))
    read_more.click()
    
    # Wait for the content to be visible after clicking
    content_div = wait.until(EC.presence_of_element_located((By.XPATH, """//*[@id="ovp_section_admission_dates"]/div[2]/div[1]/div""")))

    # First, check for any paragraphs (<p>) in the div
    paragraphs = content_div.find_elements(By.TAG_NAME, "p")
    if paragraphs:
        print("Extracting paragraph content:")
        for paragraph in paragraphs:
            print(paragraph.text)
    
    # Next, check for any tables (<table>) in the div
    tables = content_div.find_elements(By.TAG_NAME, "table")
    if tables:
        print("\nExtracting table content:")
        for table in tables:
            rows = table.find_elements(By.TAG_NAME, "tr")
            for row in rows:
                cols = row.find_elements(By.TAG_NAME, "td")
                row_data = [col.text for col in cols]
                print(row_data)

    # If neither paragraphs nor tables are found, extract plain text from the div
    if not paragraphs and not tables:
        print("Extracting plain text content:")
        print(content_div.text)

except Exception as e:
    print(f"Error: {e}")

# Close the browser
driver.quit()
