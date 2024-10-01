from Tools.Tool import *

chrome_driver_path = "chromedriver.exe"  # Replace with the correct path to your chromedriver
search_term = "Coimbatore Institute of Technology"  # The search term

first_search_result_url = get_first_search_result_url(search_term, True)
print(f"Retrieved URL: {first_search_result_url}")
