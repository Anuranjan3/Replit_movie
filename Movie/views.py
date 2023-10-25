
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Movie, Booking
from django_project.serializer import MovieSerializer, BookingSerializer, UserSerializer
from django.contrib.auth.models import User

# Allowing GET and POST methods
@api_view(['GET', 'POST'])
@permission_classes([permissions.AllowAny])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# Allowing GET, PUT, DELETE methods
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([permissions.AllowAny])
def movie_detail(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=204)

# POST for booking a seat
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def book_seat(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        return Response(status=404)

    user = request.user
    seat_number = request.data.get('seat_number')  
    booking = Booking(user=user, movie=movie, seat_number=seat_number)
    booking.save()
    return Response(status=201) 

# GET for viewing user booking history
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_booking_history(request):
    user = request.user
    bookings = Booking.objects.filter(user=user)
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)