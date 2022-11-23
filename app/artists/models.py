from django.db import models


class Artist(models.Model):

    class Genre(models.TextChoices):
        ROCK = "rock", "Rock"
        RAP = "rap", "Rap"
        ELECTRONIC = "electronic", "Electronic"
        COUNTRY = "country", "Country"

    name = models.CharField(max_length=255, unique=True)
    music_genre = models.CharField(
        max_length=15,
        choices=Genre.choices
    )

    def __str__(self) -> str:
        return self.name
        