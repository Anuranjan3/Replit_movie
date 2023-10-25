from django.core.management.base import BaseCommand
from Movie.models import Movie

class Command(BaseCommand):
    help = 'Populate the database with movie data'

    def handle(self, *args, **kwargs):
       
        data = [
            {'title': 'Movie 1', 'description': 'Description 1', 'showtimes': '1:00 PM'},
            # Add more data as needed
        ]

        # Create movie instances and populate the database
        for item in data:
            Movie.objects.create(
                title=item['title'],
                description=item['description'],
                showtimes=item['showtimes']
            )

        self.stdout.write(self.style.SUCCESS('Database populated successfully'))
