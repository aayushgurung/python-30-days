import json

# Load the first JSON file
with open('C:/Users/Nirajan/Desktop/python 30 days/datacollectionrestaurants/json files/temp_location.json') as f:
    data1 = json.load(f)

# Load the second JSON file
with open('C:/Users/Nirajan/Desktop/python 30 days/datacollectionrestaurants/json files/final_location/combined_location.json') as f:
    data2 = json.load(f)

# Load the third JSON file
# with open('C:/Users/Nirajan/Desktop/python 30 days/datacollectionrestaurants/json files/Non_unique_location.json') as f:
#     data3 = json.load(f)

# Combine the three lists of dictionaries into a single list
combined_data = data1 + data2

# Save the combined data to a new JSON file
with open('C:/Users/Nirajan/Desktop/python 30 days/datacollectionrestaurants/json files/final_location/combined_location.json', 'w') as f:
    json.dump(combined_data, f,indent=3)
