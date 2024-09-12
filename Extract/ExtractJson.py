from bs4 import BeautifulSoup
import json

def extract_json_objects_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    json_objects = []
    
    script_tags = soup.find_all('script', type='application/ld+json')
    
    for script in script_tags:
        try:
            json_object = json.loads(script.string)
            json_objects.append(json_object)
        except json.JSONDecodeError:
            continue
    return json_objects

file_path = "scraped_page.html"

with open(file_path, "r", encoding="utf-8") as fs:
    html_content = fs.read()

json_objects = extract_json_objects_from_html(html_content)

for obj in json_objects:
    print(json.dumps(obj, indent=4))