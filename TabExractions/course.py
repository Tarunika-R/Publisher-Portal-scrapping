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
driver.get("https://www.shiksha.com/college/iit-madras-indian-institute-of-technology-adyar-chennai-3031/courses")

# Wait for the page to load
time.sleep(20)

# Click the "Read More" button
try:
    # Wait for the "Read More" button to become clickable
    read_more = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, """//*[@id="acp_section_fees_and_eligibility"]/div[2]/div[2]/div[2]"""))
    )
    read_more.click()
    
    # Wait for the table to be visible after expanding the content
    table_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, """//*[@id="acp_section_fees_and_eligibility"]/div[2]/div[2]/div[1]/div/table"""))
    )
    
    # Now that the table is visible, extract the table content
    tables = driver.find_elements(By.XPATH, """//*[@id="acp_section_fees_and_eligibility"]/div[2]/div[2]/div[1]/div/table""")
    
    if tables:
        print("\nExtracting table content:")
        for table in tables:
            rows = table.find_elements(By.TAG_NAME, "tr")
            for row in rows:
                cols = row.find_elements(By.TAG_NAME, "td")
                row_data = [col.text for col in cols]
                print(row_data)
    else:
        print("No tables found.")

except Exception as e:
    print(f"Error: {e}")

# Close the browser
driver.quit()
