from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .Tools.Tool import ( get_first_search_result_url, driver, start_verbose, end_verbose, sleep)


def extract_review_text(search_term, verbose):
    
    if verbose:
        start_verbose("extract_review_text", search_term)
    try:
        driver.get(get_first_search_result_url(search_term))
        
        sleep(0.5)
        
        review_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "selected-review"))
        )
        
        divs = review_container.find_elements(By.TAG_NAME, "div")
        
        content_list = []
        
        for div in divs:
            text = div.text.strip() 
            if text:
                content_list.append(text)
        
        if verbose:
            end_verbose(content_list)
        
        return content_list

    except Exception as e:
        print(f"Error: {e}")
        return None

# chrome_driver_path = "chromedriver.exe"  
# url = "https://zollege.in/college/183263-coimbatore-institute-of-technology-cit-coimbatore/reviews"

# reviews = extract_review_text(url, chrome_driver_path)
