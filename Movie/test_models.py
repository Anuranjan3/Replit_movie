import pytest
from Movie.models import Movie, Booking
from django.contrib.auth.models import User
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MovieBooking.settings')
django.setup()



@pytest.mark.django_db
def test_valid_seat_booking():
    user = User.objects.create_user(username='testuser', password='12345')
    movie = Movie.objects.create(title='Test', description='Testing', showtimes='9:00')
    booking = Booking.objects.create(user=user, movie=movie, seat_number='A1')

    assert booking.seat_number == 'A1'

@pytest.mark.django_db
def test_valid_user_booking_history():
    user = User.objects.create_user(username='testuser', password='12345')
       Booking.objects.create(user=user, movie=movie, seat_number='A1')

    assert user.booking_set.count() == 1