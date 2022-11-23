from rest_framework import serializers

from .models import Performance
from artists.serializers import ArtistSerializer

class PerformanceSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)
    class Meta:
        model = Performance
        fields = ('artist', 'start', 'end',)