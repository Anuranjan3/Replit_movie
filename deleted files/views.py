from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Movie, Booking
from django_project.serializer import MovieSerializer, BookingSerializer, UserSerializer
from django.contrib.auth.models import User


# View to list available movies
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


# View to view movie details, including showtimes
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def movie_detail(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        return Response(status=404)

    serializer = MovieSerializer(movie)
    return Response(serializer.data)


# View to book a seat for a specific showtime
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def book_seat(request, movie_id):
    # Retrieve the movie, user, and seat number from the request
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        return Response(status=404)

    user = request.user
    seat_number = request.data.get(
        'seat_number'
    )  # Assuming the seat number is provided in the request data

    # Handle booking logic and save the booking to the database
    booking = Booking(user=user, movie=movie, seat_number=seat_number)
    booking.save()

    return Response(status=201)  # Created


# View to view user booking history
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_booking_history(request):
    user = request.user
    bookings = Booking.objects.filter(user=user)
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)
