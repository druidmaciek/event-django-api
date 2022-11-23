from django.db import models


class Artist(models.Model):
    class Genre(models.TextChoices):
        RAP = "rap", "Rap"
        ROCK = "rock", "Rock"

    name = models.CharField(max_length=255, unique=True)
    genre = models.CharField(max_length=4, choices=Genre.choices)

    def __str__(self) -> str:
        return self.name