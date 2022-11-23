from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255, unique=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
