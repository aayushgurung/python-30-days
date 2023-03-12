import requests

# api_key = "c6bef7e36beb41c79094a469a043d7f3"
# location = "Nepal"

# # Make a request to the OpenCage geocoding API
# url = f"https://api.opencagedata.com/geocode/v1/json?q={location}&key={api_key}"
https://api.opencagedata.com/geocode/v1/json?q=Manakamana-Marg-Kathmandu-Marriott-Hotel-Kathmandu-44600-Nepal&key=c6bef7e36beb41c79094a469a043d7f3
27.72660776398725, 85.36438776495156
27.654339, 85.269012
# response = requests.get(url)

with open('location.json')as f:
    data=f.read()

print(data)
# Parse the response to extract the latitude and longitude values
# if response.status_code == 200:
#     data = response.json()
#     lat = data["results"][0]["geometry"]["lat"]
#     lng = data["results"][0]["geometry"]["lng"]
#     print(f"Latitude: {lat}, Longitude: {lng}")
# else:
#     print("Error: Failed to retrieve geolocation data")
