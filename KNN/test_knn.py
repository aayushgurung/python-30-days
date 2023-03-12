import knn

restaurants = [{'reviews': 30, 'average_rating': 4.5,
                'location': 'New York', 'cuisine': 'Italian'},
               {'reviews': 20, 'average_rating': 3.7,
                   'location': 'Los Angeles', 'cuisine': 'Mexican'},
               {'reviews': 40, 'average_rating': 4.2,
                   'location': 'San Francisco', 'cuisine': 'Chinese'},
               {'reviews': 25, 'average_rating': 4.0,
                   'location': 'Chicago', 'cuisine': 'American'},
               {'reviews': 35, 'average_rating': 4.1,
                   'location': 'New York', 'cuisine': 'Mexican'},
               {'reviews': 28, 'average_rating': 4.6,
                   'location': 'San Francisco', 'cuisine': 'Italian'},
               {'reviews': 23, 'average_rating': 3.9,
                   'location': 'Chicago', 'cuisine': 'Chinese'},
               {'reviews': 32, 'average_rating': 4.3,
                   'location': 'Los Angeles', 'cuisine': 'American'}
               ]

user_prefs = {'reviews': 30,
    'minimum_rating': 4.5,
    'preferred_location': 'New York',
    'preferred_cuisine': 'Italian'}
recommended_restaurants = knn.recommend_restaurants(
    restaurants, user_prefs, k=4)
print(recommended_restaurants)
