from math import radians,sin,cos,sqrt,atan2

def haversine(lat1, lon1, lat2, lon2):
    R = 6371 # Earth's radius in kilometers
    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    a = sin(dLat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dLon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

restaurant_distance={
    "Name":["Kaveri Spicy","The Black Gold Halal Restaurant","Legendary fresh food kitchen","Hot Chilli Fast Food Restaurant","Marico Bakery Cafe","Newa Lahana","Sal's Pizza","Rdx Restaurant , Tattoo And Bar"],
    "latitude":[27.74087162217189,27.73337091448128,27.715468732975058,27.70209549894304,27.77786077903816,27.679267495928798,27.721571805244707, 27.71448848565667],
    "longitude":[85.33495111702092,85.36526461191218,85.31150622029004 ,85.313328595116 ,85.36212298808961 ,85.27457195547224 ,85.31867807533973 ,85.31035202163704]
}
user_lat=27.71708846211325
user_long= 85.35055612080632

distances={}
for i,name in enumerate(restaurant_distance["Name"]):
    dis=haversine(user_lat,user_long,restaurant_distance["latitude"][i],restaurant_distance["longitude"][i])
    distances[name]=dis
# sorted_restaurants=sorted(restaurant_distance.item(),key=lambda x:x[1])
k=3
print(distances)

for i in range(k):
    print()