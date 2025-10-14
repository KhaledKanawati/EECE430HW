from django.db import models

class Movie(models.Model):
    GENRE_CHOICES = [
        ('COM', 'Comedy'),
        ('ROM', 'Romance'),
        ('ACT', 'Action'),
        ('DRM', 'Drama'),
        ('HOR', 'Horror'),
        ('OTH', 'Other'),
    ]

    MovieID = models.CharField(max_length=20, unique=True)   # explicit MovieID field
    MovieTitle = models.CharField(max_length=200)
    Actor1Name = models.CharField(max_length=100, blank=True)
    Actor2Name = models.CharField(max_length=100, blank=True)
    DirectorName = models.CharField(max_length=100, blank=True)
    MovieGenre = models.CharField(max_length=3, choices=GENRE_CHOICES, default='OTH')
    ReleaseYear = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.MovieTitle} ({self.ReleaseYear})"
