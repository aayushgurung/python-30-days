# import requests

# # api_key = "c6bef7e36beb41c79094a469a043d7f3"
# # location = "Nepal"

# # # Make a request to the OpenCage geocoding API
# # url = f"https://api.opencagedata.com/geocode/v1/json?q={location}&key={api_key}"
# # https://api.opencagedata.com/geocode/v1/json?q=Manakamana-Marg-Kathmandu-Marriott-Hotel-Kathmandu-44600-Nepal&key=c6bef7e36beb41c79094a469a043d7f3
# 27.72660776398725, 85.36438776495156
# 27.654339, 85.269012
# # response = requests.get(url)

# with open('location.json')as f:
#     data=f.read()

# print(data)
# # Parse the response to extract the latitude and longitude values
# # if response.status_code == 200:
# #     data = response.json()
# #     lat = data["results"][0]["geometry"]["lat"]
# #     lng = data["results"][0]["geometry"]["lng"]
# #     print(f"Latitude: {lat}, Longitude: {lng}")
# # else:
# #     print("Error: Failed to retrieve geolocation data")

import requests
import json

# Set the SerpApi endpoint and API key
url = "https://google.serper.dev/places"
api_key = "20b2a666874fc5246328af9e5eac6bb6e1dc0da6"

# Load the JSON file containing the geolocation data
with open('C:/Users/Nirajan/Desktop/python 30 days/datacollectionrestaurants/geolocation_part1.json',encoding='utf-8') as f:
    data = json.load(f)
    
for d in data:
# Set the payload for the request
    if 'latitude' not in d and 'longitude' not in d:
        payload = json.dumps({
            "q": d['name']+' '+'Nepal',
            "location": "text",
            "n_results": 1
        })

        # Set the headers for the request
        headers = {
            "X-API-KEY": api_key,
            "Content-Type": "application/json"
        }
        try:
            # Make the request to the SerpApi endpoint
            response = requests.post(url, headers=headers, data=payload)

            # Parse the response JSON and extract the geolocation data
            response_data = json.loads(response.text)
            # geolocation_data = response_data['places'][0]['location']

            # Print the geolocation data
            print(response_data)
            for j,i in enumerate(response_data['places']):
                if j==0 and 'latitude' in i and 'longitude' in i:
                    d['latitude']=i['latitude']
                    d['longitude']=i['longitude']
                    print(i['latitude'])
                    print(i['longitude'])
                    if 'rating' in i:
                        d['average_rating']=i['rating']
                else:
                    break
        except Exception as e:
            d['latitude']=0
            d['longitude']=0
            continue
    else:
        pass
    
print(data)
with open('C:/Users/Nirajan/Desktop/python 30 days/datacollectionrestaurants/geolocation_copy.json','w',encoding='utf-8') as f:
    json.dump(data, f)
