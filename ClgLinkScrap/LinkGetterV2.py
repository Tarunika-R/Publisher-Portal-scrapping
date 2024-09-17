from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time, json

# topic_search = input("Enter  the topic to search: ")


def GenLink(topic_search:str):
    topic_search = topic_search.replace(' ', '+')

    chrome_options = Options()

    service = Service('/Users/mac/Documents/Publisher Portal Scrapping/.venv/bin/chromedriver')

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
    return href_url

DicData = {}
ErrDic = {}
with open('Colleges_Dataset_last-till4000.csv', 'r') as fs:
    data = fs.readlines()
    for j, i in enumerate(data):
        clean_data = i.strip().replace('"', '')
        print(clean_data)
        try:
            Urls = GenLink(clean_data)
            DicData[i.replace("\n", "")] = Urls
            print(DicData)
            with open('DicData_last-till4000.json', 'w') as json_file:
                json.dump(DicData, json_file, indent=4)
        except:
            print("Error occurred while generating link for", clean_data)
            ErrDic[j] = i
            with open('ErrDic_last-till4000.json', 'w') as json_file:
                json.dump(ErrDic, json_file, indent=4)