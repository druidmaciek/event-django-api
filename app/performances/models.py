from django.db import models

from artists.models import Artist
from events.models import Event


class Performance(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="performances"
    )
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()

    class Meta:
        ordering = ("start",)

    def __str__(self) -> str:
        return f"{self.artist} on {self.event}"
