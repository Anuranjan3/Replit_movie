from django.shortcuts import render

# Create your views herefrom rest_framework import viewsets
from rest_framework import permissions,generics, viewsets,decorators
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Movie, Booking
from django_project.serializer import UserSerializer, MovieSerializer, BookingSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
  
class MovieListCreateView(generics.ListCreateAPIView):
  queryset = Movie.objects.all()
  serializer_class = MovieSerializer


class BookingViewSet(viewsets.ModelViewSet):
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer

  @action(detail=False, methods=['GET'])
  def user_booking_history(self, request):
      user = request.user 
      bookings = Booking.objects.filter(user=user)
      serializer = BookingSerializer(bookings, many=True)
      return Response(serializer.data)
      


class MovieDetailView(generics.RetrieveUpdateAPIView):
  queryset = Movie.objects.all()
  serializer_class = MovieSerializer


class BookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class UserBookingHistoryView(generics.ListAPIView):
  serializer_class = BookingSerializer

  def get_queryset(self):
      user = self.request.user  
      return Booking.objects.filter(user=user)