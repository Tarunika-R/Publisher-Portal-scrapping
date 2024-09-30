from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the webpage
url = "https://www.shiksha.com/college/iim-ahmedabad-indian-institute-of-management-vastrapur-307/courses"
driver.get(url)

# Wait for the page to load
time.sleep(5)

# Scroll into the view of the button before clicking
try:
    view_more_button = driver.find_element(By.XPATH, """//*[@id="acp_section_fees_and_eligibility"]/div[2]/div[2]/div[2]""")
    driver.execute_script("arguments[0].scrollIntoView(true);", view_more_button)
    time.sleep(1)  # Wait for scrolling
    view_more_button.click()
    time.sleep(3)  # Wait for the content to load
except Exception as e:
    print("View More button not found or couldn't be clicked:", e)

# Extract the content from the expanded section
try:
    content = driver.find_element(By.XPATH, """//*[@id="acp_section_fees_and_eligibility"]/div[2]/div[2]""")
    print(content.text)
except Exception as e:
    print("Could not extract content:", e)

# Close the driver
driver.quit()
