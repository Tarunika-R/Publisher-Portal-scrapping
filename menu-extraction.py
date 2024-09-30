from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://www.shiksha.com/college/shri-shiv-mahavidyalaya-ghazipur-183029"
driver.get(url)


try:
    tabs = []
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#main-wrapper > div.b876.three_col.uilp.reverse_two_col > div > div > ul")) 
    )
    
    menu_items = driver.find_elements(By.CSS_SELECTOR, "#main-wrapper > div.b876.three_col.uilp.reverse_two_col > div > div > ul")

    for item in menu_items:
        tabs = item.text.split('\n')
finally:
    driver.quit()
    
print(tabs)