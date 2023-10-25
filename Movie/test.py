from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Movie, Booking

class MovieAPITest(APITestCase):
    def setUp(self):
        # Create some sample movies for testing
        self.movie1 = Movie.objects.create(title="Movie 1", description="Description 1", showtimes="14:00:00")
        self.movie2 = Movie.objects.create(title="Movie 2", description="Description 2", showtimes="16:00:00")

    def test_list_movies(self):
        # Test the movie listing API endpoint
        url = reverse('movie-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Check if it returns the expected number of movies

    def test_book_seat(self):
        # Test the booking API endpoint
        url = reverse('book-seat')
        data = {
            "user": 1,  # Replace with a valid user ID
            "movie": self.movie1.id,
            "seat_number": 3,
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)  # Check if a booking record is created
      
    def test_invalid_booking(self):
        # Test booking with invalid data (e.g., missing required fields)
        url = reverse('book-seat')
        data = {
            "user": 1,
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
      
    
    def test_booking_invalid_user(self):
        # Test booking with invalid user ID
        url = reverse('book-seat')
        data = {
            "user": -1,  # Invalid user ID
            "movie": self.movie1.id,
            "seat_number": 3,
        }
        response = self.client.post(url, data, format='json')
    
