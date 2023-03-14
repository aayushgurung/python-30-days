import json
import numpy as np
import random


# Load data from JSON file
with open('C:/Users/Nirajan/Desktop/python 30 days/datacollectionrestaurants/geolocation_part1 copy.json', 'r',encoding='utf-8') as f:
    data = json.load(f)
print(len(data))
i=0
j=0
for d in data:
    random_number = random.randint(5, 15)
    d['capacity']=random_number

# for d in data:
#     if d['latitude']==0:
#         print(d['name'])
#         i=i+1
    
# print(i)
# print(j)
with open('C:/Users/Nirajan/Desktop/python 30 days/final data for restaurant/data.json', 'w',encoding='utf-8') as f:
    json.dump(data, f)
# # Split the data into two equal parts
# split_index = len(data) // 2
# data_part1 = data[:split_index]
# data_part2 = data[split_index:]

# # Save data_part1 as a JSON file
# with open('C:/Users/Nirajan/Desktop/python 30 days/datacollectionrestaurants/json files/final data/FINAL_DATA_Part1.json', 'w') as f:
#     json.dump(data_part1, f)

# # Save data_part2 as a JSON file
# with open('C:/Users/Nirajan/Desktop/python 30 days/datacollectionrestaurants/json files/final data/FINAL_DATA_Part2.json', 'w') as f:
#     json.dump(data_part2, f)

# print('Completed')

# import json

# # Open the first output file and count the number of elements
# with open('C:/Users/Nirajan/Desktop/python 30 days/datacollectionrestaurants/json files/final data/FINAL_DATA_Part1.json', 'r', encoding='utf-8') as f:
#     data1 = json.load(f)
# print(f"Number of elements in Test_900_1.json: {len(data1)}")

# # Open the second output file and count the number of elements
# with open('C:/Users/Nirajan/Desktop/python 30 days/datacollectionrestaurants/json files/final data/FINAL_DATA_Part2.json', 'r', encoding='utf-8') as f:
#     data2 = json.load(f)
# print(f"Number of elements in Test_900_2.json: {len(data2)}")

