from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def fetch_college_highlights(url, chrome_driver_path="chromedriver.exe"):
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get(url)

    output_data = {}

    try:
        wait = WebDriverWait(driver, 10)
        read_more = wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@id="ovp_section_highlights"]/div[2]/div[1]/div/span""")))
        driver.execute_script("arguments[0].scrollIntoView();", read_more)
        time.sleep(1)
        read_more.click()
        time.sleep(2)
        content_div = driver.find_element(By.XPATH, """//*[@id="ovp_section_highlights"]/div[2]/div[1]/div/div/div/div""")

        tables = content_div.find_elements(By.TAG_NAME, "table")
        table_parents = set()
        table_data = []
        if tables:
            for table in tables:
                rows = table.find_elements(By.TAG_NAME, "tr")
                for row in rows:
                    cols = row.find_elements(By.TAG_NAME, "td")
                    row_data = [col.text for col in cols]
                    if row_data != []:
                        table_data.append(row_data)
                table_parents.add(table)

        paragraphs = content_div.find_elements(By.TAG_NAME, "p")
        total_para = ""
        if paragraphs:
            for paragraph in paragraphs:
                is_inside_table = False
                for table_parent in table_parents:
                    if table_parent in paragraph.find_elements(By.XPATH, "./ancestor::*"):
                        is_inside_table = True
                        break

                if not is_inside_table:
                    total_para += paragraph.text + "\n"

            if total_para:
                output_data['Highlights'] = total_para
            else:
                output_data['Highlights'] = "Content Not Found :\\"
        
        if len(table_data) > 0:
            output_data["Table"] = table_data
        else:
            output_data["Table"] = []

        # Extract all iframes
        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        iframe_list = []
        if iframes:
            for iframe in iframes:
                src = iframe.get_attribute("src")
                if  src != "":
                    iframe_list.append(src)

        output_data["Iframes"] = iframe_list

    except Exception as e:
        print(f"Error: {e}")
    
    driver.quit()
    return output_data

# Example usage
url = "https://www.shiksha.com/university/srm-institute-of-science-and-technology-kattankulathur-chennai-24749"
output = fetch_college_highlights(url)
print(output)
