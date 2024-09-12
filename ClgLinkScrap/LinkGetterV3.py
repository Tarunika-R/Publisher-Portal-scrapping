from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

# Function to generate links based on topic search
def GenLink(browser, topic_search: str):
    topic_search = topic_search.replace(' ', '+')
    url = f"https://www.shiksha.com/search?q={topic_search}"
    browser.get(url)

    try:
        # Wait for the div elements to load (increased timeout to 20 seconds)
        WebDriverWait(browser, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.c8ff'))
        )
        div_elements = browser.find_elements(By.CSS_SELECTOR, 'div.c8ff')

        # Extracting the first link details (adjust for more if needed)
        for div in div_elements:
            link = div.find_element(By.TAG_NAME, 'a')
            widget_label = link.get_attribute('widgetspecificlabel')
            href_url = link.get_attribute('href')
            return f"College: {widget_label}, URL: {href_url}"

    except Exception as e:
        print(f"Error while fetching data for {topic_search}: {str(e)}")
        return None

# Main function
def main():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run headless for faster execution
    service = Service('chromedriver.exe')

    # Start the browser once
    browser = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Reading data from CSV and writing output to text files
        with open('Colleges_Dataset.csv', 'r') as fs, \
             open("Output.txt", 'a') as output_file, \
             open("Err2Scrap.txt", 'a') as error_file:

            csv_reader = csv.reader(fs)
            for row in csv_reader:
                topic_search = ' '.join(row).strip()
                print(f"Searching for: {topic_search}")

                if topic_search:
                    try:
                        result = GenLink(browser, topic_search)
                        if result:
                            print(result)
                            output_file.write(result + "\n")
                        else:
                            print(f"No result for {topic_search}")
                            error_file.write(f"No result for {topic_search}\n")
                    except Exception as e:
                        print(f"Error occurred while generating link for {topic_search}: {str(e)}")
                        error_file.write(f"Error for {topic_search}: {str(e)}\n")

    except Exception as e:
        print(f"An error occurred during the process: {str(e)}")
    finally:
        browser.quit()

if __name__ == "__main__":
    main()
