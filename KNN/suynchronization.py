from django.db import transaction
from django.shortcuts import get_object_or_404
from django.http import HttpResponseBadRequest

from .models import Restaurant, Reservation

def book_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    user = request.user
    if not user.is_authenticated:
        return HttpResponseBadRequest("You must be logged in to book a restaurant.")
    
    with transaction.atomic():
        # Acquire a lock on the restaurant to prevent concurrent bookings
        restaurant = Restaurant.objects.select_for_update().get(pk=restaurant_id)
        if restaurant.is_full():
            return HttpResponseBadRequest("The restaurant is already fully booked.")
        
        # Create a reservation for the user
        reservation = Reservation.objects.create(user=user, restaurant=restaurant)
        restaurant.num_bookings += 1
        restaurant.save()
    
    return HttpResponse("Your reservation is confirmed!")
