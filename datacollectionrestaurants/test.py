import json
import numpy as np
# Load data from JSON file
with open('C:/Users/Nirajan/Desktop/python 30 days/datacollectionrestaurants/json files/final data/FINAL_DATA.json', 'r',encoding='utf-8') as f:
    data = json.load(f)

# Iterate through the list and remove any dictionaries whose url value doesn't start with "http"
# i=0
# j=0
# k=0
# temp_lst=[]
# new_data = [d for d in data if d["number_of_reviews"] != 0]
restaurant_table={}
image_table={}
rating_table={}
i=0
cuisine_unique=list()
id='R_ID'
for d in data:
    s_id=id+str(i)
    i=i+1
    data_1[s_id]=d['name']
print(data_1)
# # Save new_data as a JSON file
# with open('C:/Users/Nirajan/Desktop/python 30 days/datacollectionrestaurants/json files/final data/Test.json', 'w') as f:
#     json.dump(data, f)
# print('Completed')