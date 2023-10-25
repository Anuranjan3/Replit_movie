from django.urls import path
from . import views

urlpatterns = [
    # URL for listing available movies
    path('', views.movie_list, name='movie-list'),

    # URL for viewing movie details, including showtimes
    path('movies/<int:movie_id>/', views.movie_detail, name='movie-detail'),

    # URL for booking a seat for a specific showtime
    path('movies/<int:movie_id>/book/', views.book_seat, name='book-seat'),

    # URL for viewing user booking history
    path('bookings/', views.user_booking_history, name='user-booking-history'),
]
