from TabSupport.Tools.Tool import fetch_menu_tabs
from  TabSupport.ClgInfo import *
from  TabSupport.fees import *
from  TabSupport.admission import *
from  TabSupport.placement import *
from  TabSupport.ranking import *
from  TabSupport.HostelAndInfra import *
from  TabSupport.scholarships import *


url = "https://www.shiksha.com/college/iit-madras-indian-institute-of-technology-adyar-chennai-3031/"
# ['College Info', 'Courses', 'Fees', 'Reviews', 'Admissions', 'Placements', 'Cut-Offs', 'Rankings', 'Hostel & Campus', 'Scholarships']
print(fetch_menu_tabs(url, True))

clg_info = {}
fees = {}
Admissions = {}

def collect_clg_content(url, verbose=False):
    for i in fetch_menu_tabs(url, verbose):
        if i is "College Info":
            clg_info['main_details'] = clg_info_top_details(url, verbose)
            clg_info['info_highlights'] = fetch_college_highlights(url,  verbose)
        elif i  is "Fees":
            fees["fees_table"] = extract_fees_table(url, verbose)
        elif i is "Admissions":
            fees["admission_table"] = extract_admission_table(url, verbose)
        elif i is "Placements":
            fees["extract_placement"] = extract_placement(url, verbose)
        elif i is "Rankings":
            fees["extract_placement"] = extract_ranking_info(url, verbose)
        elif i is "Hostel & Campus":
            fees["extract_placement"] = extract_hostel_info(url, verbose)
        elif i is "Scholarships":
            fees["extract_placement"] = fetch_scholarships(url, verbose)
