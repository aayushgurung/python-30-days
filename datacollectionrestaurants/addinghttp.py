import json
from collections import defaultdict

with open ('C:/Users/Nirajan/Desktop/python 30 days/datacollectionrestaurants/temp_location.json') as f:
    urls=json.load(f)
org_urls=[data['link'] for data in urls]
# final_url=defaultdict(list)
# for i in org_urls:
#     urls='https://www.tripadvisor.com'+i
#     final_url.append({'link': url})
# print(final_url)
final_url = [{"link": 'https://www.tripadvisor.com' + url} for url in org_urls]
print(final_url)
with open('C:/Users/Nirajan/Desktop/python 30 days/datacollectionrestaurants/temp_location.json','w') as f:
    json.dump(final_url, f, indent=4)
