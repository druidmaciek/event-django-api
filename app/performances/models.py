from django.db import models

from events.models import Event
from artists.models import Artist

class Performance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()

    def __str__(self) -> str:
        return f"{self.artist.name} on {self.event.name}"