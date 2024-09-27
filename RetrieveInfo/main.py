from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode for faster scraping without UI

# Initialize the WebDriver using WebDriver Manager to automatically handle the ChromeDriver installation
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# URL of the page to scrape
url = "https://www.shiksha.com/college/st-josephs-s-college-for-women-mysore-69661"

# Open the page
driver.get(url)

# Wait for the element to be available before trying to find it
try:
    # Add an explicit wait for the element to appear (10 seconds max wait)
    element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="ovp_section_highlights"]/div[2]/div[1]/div/div/div'))
    WebDriverWait(driver, 10).until(element_present)

    # Extract the content from the element using XPath
    content_element = driver.find_element(By.XPATH, '//*[@id="ovp_section_highlights"]/div[2]/div[1]/div/div/div')
    content_text = content_element.text
    print(content_text)
except Exception as e:
    # Capture and print full exception details
    print(f"An error occurred: {e}")

# Close the browser
driver.quit()
