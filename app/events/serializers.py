from rest_framework import serializers

from artists.serializers import ArtistSerializer
from performances.models import Performance

from .models import Event


class PerformanceSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = Performance
        fields = ("id", "artist", "start", "end", "event")


class EventSerializer(serializers.ModelSerializer):
    performances = PerformanceSerializer(read_only=True, many=True)

    class Meta:
        model = Event
        fields = ("name", "start", "end", "performances")


class EventExportSerializer(serializers.Serializer):
    webhook = serializers.URLField()
