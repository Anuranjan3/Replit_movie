from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    showtimes = models.TimeField()
  
    def __str__(self):
     return self.title
      
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
  
    def __str__(self):
     return self.user.username + " - " + self.movie.title + " - " + self.seat_number