from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Set the correct path to ChromeDriver
chrome_driver_path = "chromedriver.exe"

# Initialize Service object
service = Service(chrome_driver_path)

# Start the WebDriver using the service object
driver = webdriver.Chrome(service=service)

# Open the website
driver.get("https://www.shiksha.com/college/iit-madras-indian-institute-of-technology-adyar-chennai-3031")
time.sleep(3)  # Wait for the page to load

# Click the "Read More" button
try:
    read_more = driver.find_element(By.XPATH, """//*[@id="ovp_section_highlights"]/div[2]/div[1]/div/span""")
    read_more.click()
    time.sleep(2)  # Wait for the content to load

    # Try to find both paragraphs and tables in the expanded content
    content_div = driver.find_element(By.XPATH, """//*[@id="ovp_section_highlights"]/div[2]/div[1]/div/div/div/div""")

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
