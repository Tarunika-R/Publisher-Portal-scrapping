from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome options and WebDriver
options = Options()
# Uncomment below if you want to see the browser action (remove headless mode)
# options.add_argument("--headless")  # Run in headless mode (optional)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the website
url = "https://www.shiksha.com/college/shri-shiv-mahavidyalaya-ghazipur-183029"
driver.get(url)

# Wait until the menu is visible
try:
    # Wait up to 10 seconds for the menu to become visible
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#main-wrapper > div.b876.three_col.uilp.reverse_two_col > div > div > ul"))
    )

    # Find the menu items using the correct selector for the navigation menu
    menu_items = driver.find_elements(By.CSS_SELECTOR, "#main-wrapper > div.b876.three_col.uilp.reverse_two_col > div > div > ul")

    # Extract and print the menu names
    for item in menu_items:
        print(item.text)

finally:
    # Close the driver
    driver.quit()