# import json


# with open('C:/Users/Nirajan/Desktop/python 30 days/datacollectionrestaurants/location_test.json') as f:
#              data =json.load(f)
# original_urls=[item['link'] for item in data]
# print(original_urls[0])

from collections import defaultdict
username=['Aayush','Gurung','Abiskar','Koirala']
rating=[4,5,3.5,4.5]
partial=['Lorem ipsum dolor sit','amet consectetur adipisicing elit.','neque maiores architecto earum dolor sapiente aliquid tenetur','tempora iure, explicabo magni dolorem repellat eum eius cupiditate quisquam sint!']

final_rating={}
for i in range(len(username)):
    final_rating[username[i]] = {'rated': rating[i], 'comment': partial[i]}
print(final_rating)