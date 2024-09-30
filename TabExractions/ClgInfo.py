from Tools.Tool import id_to_content, driver


url = 'https://www.shiksha.com/college/adina-institute-of-science-and-technology-sagar-60309'
data_dict = [url, {'line_1': 'e9dd86', 'line_2': 'e1a898'}]

result = id_to_content(data_dict)
print(result)




# To Close the driver : )
driver.quit()
