from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set the correct path to ChromeDriver
chrome_driver_path = "chromedriver.exe"  # Replace with the correct path to your chromedriver

# Initialize Service object
service = Service(chrome_driver_path)

# Start the WebDriver using the service object
driver = webdriver.Chrome(service=service)

# Open the target URL
driver.get("https://zollege.in/college/183263-coimbatore-institute-of-technology-cit-coimbatore/reviews")

# Wait for the page to load completely
time.sleep(3)  # Adjust based on page load time

try:
    # Locate the parent div with id 'selected-review'
    review_container = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "selected-review"))
    )
    
    # Find all the child divs inside the parent div
    divs = review_container.find_elements(By.TAG_NAME, "div")
    
    # Initialize an empty list to store the text content of each div
    content_list = []
    
    # Loop through each div, extract its text, and append it to the list
    for div in divs:
        text = div.text.strip()  # Get the text and strip any leading/trailing spaces
        if text:  # Ensure the text is not empty
            content_list.append(text)
    
    # Print the list of text content
    print("List of text content from each div inside 'selected-review':")
    # for index, content in enumerate(content_list):
    #     print(f"{index + 1}: {content}")
    print(content_list)
    
    # Optionally, you can return or use this list for further processing
    # return content_list

except Exception as e:
    print(f"Error: {e}")

# Close the browser after task completion
driver.quit()
