import re
import json
from collections import defaultdict

with open('C:/Users/Nirajan/Desktop/python 30 days/datacollectionrestaurants/location.json') as f:
     data = json.load(f)
dic=defaultdict(list)
original_urls = [item['link'] for item in data]
modified_urls=[]
urls=[original_urls[0],original_urls[1]]
num=420
value=0
for url in original_urls:
    for i in range(14):
        modified_url = re.sub(r'(?<=g)(\d+)(?=-)', r'\1-oa{}'.format(num), url)
        modified_urls.append(modified_url)
        num=num-30
    num=420
    value=value+1
    dic[value]=modified_urls
    modified_urls=[]
            
with open('C:/Users/Nirajan/Desktop/python 30 days/modified.json','w') as f:
    json.dump(dic, f, indent=4)
print(dic)
