from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()




def getContent(url: str, xpath: str) -> str:
    """
    Retrieves the content of a webpage by waiting for a specific element to be visible.

    Args:
        url (str): The URL of the webpage to retrieve content from.
        xpath (str): The XPath of the element containing the content to retrieve.

    Returns:
        str: The text content of the element, or "Timed out waiting for element" if the element is not found within 10 seconds.

    Raises:
        TimeoutException: If the element is not found within 10 seconds.

    Example usage:
        content = getContent("https://www.example.com", "xpath")
        print(content)
    """
    driver.get(url)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        text = element.text
        return text
    except TimeoutException:
        return "Timed out waiting for element"