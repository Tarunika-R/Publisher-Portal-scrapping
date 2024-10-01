from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()

# int, float, str, list, tuple, dict, set


def getContent(url: str) -> str:
    driver.get(url)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, """//*[@id="iulp_lhs_container"]/div[1]"""))
        )
        text = element.text
        return text
    except TimeoutException:
        return "Timed out waiting for element"