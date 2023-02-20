
import json

# Load the JSON file
with open('C:/Users/Nirajan/Desktop/python 30 days/datacollectionrestaurants/json files/final_location/unique_location.json') as f:
    data = json.load(f)

# Create a set of the values
count = len(data)
print(count)
values_set = set()
for item in data:
    values_set.add(item['link'])
    value = item['link']
    if value not in values_set:
        values_set.add(value)  # replace 'key' with the actual key name in your JSON data
unique_data = [{'link': value} for value in values_set]
# Check if all values are unique
if len(values_set) == len(data):
    print('All values are unique')
else:
    print('Some values are repeated')

# with open('C:/Users/Nirajan/Desktop/python 30 days/datacollectionrestaurants/json files/final_location/unique_location.json', 'w') as f:
#     json.dump(unique_data, f,indent=4)

