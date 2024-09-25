from bs4 import BeautifulSoup
import json
import re

# Function to extract JSON data from the script tag
def extract_json_from_html(file_path):
    # Open and read the HTML file
    with open(file_path, 'r', encoding='utf-8') as html_file:
        content = html_file.read()

    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(content, 'html.parser')

    # Find the <script> tag containing the JSON data
    script_tag = soup.find('script', text=re.compile(r'__PRELOADED_STATE__'))

    if script_tag:
        # Use regex to find the JSON data inside the script tag
        json_data_match = re.search(r'window\.__PRELOADED_STATE__\s*=\s*({.*});', script_tag.string)

        if json_data_match:
            # Load the JSON data into a Python dictionary
            json_data = json.loads(json_data_match.group(1))
            return json_data
        else:
            print("No JSON data found in the script tag.")
            return None
    else:
        print("Script tag with __PRELOADED_STATE__ not found.")
        return None

# File path to the HTML file
file_path = 'scraped_page.html'

# Extract the JSON data
extracted_data = extract_json_from_html(file_path)

# Check if data was successfully extracted
if extracted_data:
    # Print or store the extracted JSON data
    print(json.dumps(extracted_data, indent=4))
    # Optionally, write the extracted JSON to a file
    with open('extracted_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(extracted_data, json_file, indent=4)
