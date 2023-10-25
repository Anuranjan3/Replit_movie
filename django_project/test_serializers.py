import pytest
from rest_framework.exceptions import ValidationError
from  .serializers import MovieSerializer, BookingSerializer
from  .models import Movie, Booking
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_valid_movie_serializer():
    movie = Movie.objects.create(title="Test Movie", description="Testing", showtimes='9:00')
    serializer = MovieSerializer(movie)

    assert serializer.data == {"title": "Test Movie", "description": "Testing", "showtimes": '9:00'}

@pytest.mark.django_db
def test_valid_booking_serializer():
    user = User.objects.create_user(username="test", password="password")
    movie = Movie.objects.create(title="Test Movie", description="Testing", showtimes='9:00')
    booking = Booking.objects.create(user=user, movie=movie, seat_number='A1')

    serializer = BookingSerializer(booking)

    expected_data = {
        "user": user.id,
        "movie": movie.id,
        "seat_number": "A1"
    }

    assert serializer.data == expected_data


@pytest.mark.django_db
def test_invalid_booking_serializer():
    invalid_data = {
        "user": 999,  # Assuming no user with this ID exists
        "movie": "invalid_movie",
        "seat_number": "A1"
    }

    serializer = BookingSerializer(data=invalid_data)

    with pytest.raises(ValidationError):
        serializer.is_valid(raise_exception=True)