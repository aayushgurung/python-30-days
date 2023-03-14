import requests
import folium
from shapely.geometry import Point, Polygon
from IPython.display import display

# Set the geolocation coordinates of the location to check
lat = 27.6875
lng = 85.3256

# Set the API endpoint and parameters to get the boundary coordinates of the district
url = f'https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=27.7083&lon=85.3205'

# Make a request to the API and extract the boundary coordinates of the district
response = requests.get(url)
boundary_coords = response.json()['boundingbox']
print(boundary_coords)
# Convert the boundary coordinates to floats
boundary_coords = [float(coord) for coord in boundary_coords]

# Create a Polygon object from the boundary coordinates of the district
boundary_polygon = Polygon([(boundary_coords[2], boundary_coords[0]),
                            (boundary_coords[3], boundary_coords[0]),
                            (boundary_coords[3], boundary_coords[1]),
                            (boundary_coords[2], boundary_coords[1])])

# Create a Point object from the latitude and longitude of the location to check
point = Point(lng, lat)

# Check if the location falls inside the district
if boundary_polygon.contains(point):
    print("The location falls inside the district")
else:
    print("The location does not fall inside the district")

# Create a folium map centered on the location to check
map_center = [lat, lng]
m = folium.Map(location=map_center, zoom_start=15)

# Add the boundary polygon to the map
folium.GeoJson(boundary_polygon).add_to(m)

# Display the map
m.save('C:/Users/Nirajan/Desktop/python 30 days/a.html')
