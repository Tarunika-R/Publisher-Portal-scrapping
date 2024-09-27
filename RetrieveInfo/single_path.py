from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Setup Edge options
edge_options = Options()
# edge_options.add_argument("--headless")  # Run i/n headless mode for faster scraping without UI

# Initialize the WebDriver using WebDriver Manager to automatically handle the EdgeDriver installation
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)

# URL of the page to scrape

url = "https://www.shiksha.com/college/st-peter-s-college-sodepur-kolkata-47647"

# Open the page
driver.get(url)

# Wait for the element to be available before trying to find it
try:
    # Add an explicit wait for the element to appear (10 seconds max wait)
    element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="ovp_section_highlights"]'))
    WebDriverWait(driver, 10).until(element_present)

    # Extract the content from the element using XPath
    content_element = driver.find_element(By.XPATH, '//*[@id="ovp_section_highlights"]')
    content_text = content_element.text
    print(content_text)
except Exception as e:
    # Capture and print full exception details
    print(f"An error occurred: {e}")

# Close the browser
driver.quit()
