import heapq

class KNN:
    def __init__(self,k=3):
        self.k  =k
        
    def euclidean_distance(self,x, y):
        return ((x['reviews'] - y['reviews']) ** 2
                + (x['average_rating'] - y['average_rating']) ** 2) ** 0.5

    def find_k_nearest_neighbors(self,restaurants, target_restaurant):
        distances = [(self.euclidean_distance(r, target_restaurant), r) for r in restaurants]
        neighbors = [r for d, r in distances[:self.k]]
        return neighbors

    def recommend_restaurants(self,restaurants, user_prefs):
        target_restaurant = {'reviews': user_prefs['reviews'], 'average_rating': user_prefs['minimum_rating'],
                            'location': user_prefs['preferred_location'],
                            'cuisine': user_prefs['preferred_cuisine']}
        neighbors = self.find_k_nearest_neighbors(restaurants, target_restaurant, self.k)
        return sorted(neighbors, key=lambda r: r['average_rating'], reverse=True)
    
    def haversine(,latitude,longitude):
        
