from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to the ChromeDriver (update this with your path)
chromedriver_path = 'chromedriver.exe'  # Replace with the actual path to your chromedriver

# Step 1: Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Optional: Start maximized
# chrome_options.add_argument("--headless")  # Optional: Run in headless mode

# Step 2: Start the Chrome WebDriver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Step 3: Load the webpage
url = 'https://www.shiksha.com/college/adhiparasakthi-engineering-college-kanchipuram-42520'
driver.get(url)

# Wait for the page to load completely
time.sleep(3)

# Step 4: Find all "Read More" elements and click them one by one, extracting content
try:
    # Find all elements with the `data-test="read_more"` attribute (all "Read More" buttons)
    read_more_elements = driver.find_elements(By.CSS_SELECTOR, 'span[data-test="read_more"]')

    # Step 5: Iterate through each "Read More" button and click it, then extract content
    for i, element in enumerate(read_more_elements):
        try:
            # Scroll to the element and click it
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            element.click()
            time.sleep(1)  # Add delay to ensure content loads

            # Step 6: After clicking, extract content from the div with class "paper-card"
            try:
                # Wait until the content inside the paper-card is visible
                paper_card_div = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "paper-card"))
                )
                # Extract the content (you can customize this further)
                print(f"Content for Read More {i+1}:")
                print(paper_card_div.text)  # Print the content of the div
                print("-" * 50)  # Separator for readability

            except Exception as e:
                print(f"Error extracting content from 'paper-card': {e}")

        except Exception as e:
            print(f"Error clicking 'Read More' span: {e}")

    print(f"Clicked and extracted content from {len(read_more_elements)} 'Read More' elements.")
except Exception as e:
    print(f"Error finding 'Read More' elements: {e}")

# Close the browser after scraping
driver.quit()
