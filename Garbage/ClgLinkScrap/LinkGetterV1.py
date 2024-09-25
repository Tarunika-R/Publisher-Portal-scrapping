from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# topic_search = input("Enter the topic to search: ")


def GenLink(topic_search:str):
    topic_search = topic_search.replace(' ', '+')

    chrome_options = Options()

    service = Service('chromedriver')

    browser = webdriver.Chrome(service=service, options=chrome_options)

    for i in range(1):  # Adjust the range as needed for multiple pages
        url = f"https://www.shiksha.com/search?q={topic_search}&start={i * 10}"
        browser.get(url)

        time.sleep(3)

        div_elements = browser.find_elements(By.CSS_SELECTOR, 'div.c8ff')

        for div in div_elements:
            # Select the <a> tag inside the <div>
            link = div.find_element(By.TAG_NAME, 'a')
            # Extract the widget label and URL
            widget_label = link.get_attribute('widgetspecificlabel')
            href_url = link.get_attribute('href')
    time.sleep(10) 
    browser.quit()
    return f"College: {widget_label}, URL: {href_url}"

with open('Colleges_Dataset.csv', 'r') as fs:
    data = fs.readlines()
    for i in data:
        clean_data = i.strip().replace('"', '')
        print(clean_data)
        try:
            Urls = GenLink(clean_data)
            print(Urls)
            with open("Output.txt", 'a') as fs1:
                fs1.write(Urls + "\n")
        except:
            print("Error occurred while generating link for", clean_data)
            with open("Err2Scrap.txt", 'a') as fs2:
                fs.write(clean_data+"\n")

# print(GenLink(topic_search))